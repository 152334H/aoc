'''things you may forget:
char_to_dir(c: str) - convert 'UDLR' or 'NSEW' or '<>^v' to Point
binsearch(f: Callable, hi: int, lo=0) - binary search on f(mid)
PQ(list) - priority queue class
sum_array(List[int]), SAT(List[List[int]]) - sum area array && sum area table
grid_to_graph(Grid)
save_graph(G)

networkx help:
>>> list(G.nodes)
[1, 2, 3, 'spam', 's', 'p', 'a', 'm']
>>> list(G.edges)
[(1, 2), (1, 3), (3, 'm')]
>>> G.edges([2, 'm'])
EdgeDataView([(2, 1), ('m', 3)])
>>> list(G.adj[1])  # or list(G.neighbors(1)). G.successors(1) for a directed graph.
[2, 3]
>>> G.degree[1]  # the number of edges incident to 1
2

>>> # weight assignments
>>> G.add_edge(1, 2, weight=4.7)
>>> G[1][2]['weight'] = 4.7
>>> G.edges[3, 4]['weight'] = 4.2
>>> # The special attribute weight should be numeric as it is used by algorithms requiring weighted edges.

>>> subgraph(G, nbunch) #Returns the subgraph induced on nodes in nbunch.
>>> union(G, H[, rename, name]) # Return the union of graphs G and H.
>>> disjoint_union(G, H) # Return the disjoint union of graphs G and H.
>>> to_undirected(graph) # Returns an undirected view of the graph graph.
>>> to_directed(graph) # Returns a directed view of the graph graph.

>>> # traversal
>>> has_path(G, source, target) #
>>> shortest_path(G) # APSP
>>> shortest_path(G, source, target) # SPSP

'''

from itertools import *
from operator import *
from collections import *
dd,ctr = defaultdict, Counter

_pow = pow
from math import *
pow = _pow # math's pow() doesn't provide the `mod` optional arg

from re import findall
from functools import reduce, lru_cache, singledispatchmethod

# non-generator versions of common funcs
Map = lambda f,it: list(map(f,it))
Filter = lambda f,it: list(filter(f,it))
Reversed = lambda ls: list(reversed(ls))
Zip = lambda *ls: list(zip(*ls))

# for the package
from typing import *

''' === INPUT === '''
def sread(constructor=str, div=None, name='input'):
    '''read file NAME, split it with DIV and parse it with a given constructor
    when DIV is given, `constructor()` is mapped over each elem.
    Otherwise, constructor() is used for the entire input.'''
    with open(name) as f: s = f.read()
    if s[-1] == '\n': s = s[:-1]
    if div == None: return constructor(s)
    return Map(constructor, s.split(div))

def sreadlines(constructor=str, div=None, name='input'):
    '''sread, but split across newlines first
    constructor() is used for each element/line if div is given/None'''
    if div is None: return sread(constructor,'\n',name)
    return Map(lambda l: Map(constructor,l.split(div)), sread(str,'\n',name))

def sreadlinelines(constructor=str, div=None, name='input'):
    '''Split by \n\n, then for each group of lines,
     - if div is None, apply constructor to the whole group of lines
     - else, apply constructor to each subgroup in group.split(div).'''
    if not div: return [constructor(lines) for lines in sread(str, '\n\n', name)]
    return [[constructor(line) for line in lines.split(div)] for lines in sread(str, '\n\n', name)]

''' === GRIDS === '''
class Point(namedtuple('Point2d', ['x', 'y'])):
    '''A 2d point'''
    # + 
    @singledispatchmethod
    def __add__(self, other): return Point(self.x + other.x, self.y + other.y)
    @__add__.register
    def _(self, other: int): return Point(self.x + other, self.y + other)
    # -
    @singledispatchmethod
    def __sub__(self, other): return Point(self.x - other.x, self.y - other.y)
    @__sub__.register
    def _(self, other: int): return Point(self.x - other, self.y - other)
    # *
    @singledispatchmethod
    def __mul__(self, other): return Point(self.x * other.x, self.y * other.y)
    @__mul__.register
    def _(self, other: int): return Point(self.x * other, self.y * other)
    # /
    @singledispatchmethod
    def __truediv__(self, other): return Point(self.x / other.x, self.y / other.y)
    @__truediv__.register
    def _(self, other: int): return Point(self.x / other, self.y / other)
    # //
    @singledispatchmethod
    def __floordiv__(self, other): return Point(self.x // other.x, self.y // other.y)
    @__floordiv__.register
    def _(self, other: int): return Point(self.x // other, self.y // other)
    #
    def __abs__(self): return abs(self.x) + abs(self.y) # manhattan distance
    def __repr__(self): return 'Point({}, {})'.format(self.x, self.y)

def char_to_dir(c: str) -> Point:
    '''Convert a cardinal direction to a Point'''
    try: return Point(*{'N':(0,1),'S':(0,-1),'E':(1,0),'W':(-1,0), 
            'U':(0,1),'D':(0,-1),'L':(-1,0),'R':(1,0),
            '<':(-1,0),'>':(1,0),'^':(0,1),'v':(0,-1)}[c])
    except KeyError: raise ValueError('Invalid direction: {}'.format(c))

class DirectedPoint(Point):
    def __new__(cls, x, y, z):
        return super(DirectedPoint, cls).__new__(cls, x, y)
    def __init__(self, x, y, dir: Union[str,tuple]):
        if isinstance(dir,str): dir = char_to_dir(dir) # will raise ValueError if invalid
        self.dir = Point(*dir)
    def __repr__(self): return 'DirectedPoint({}, {}, dir={})'.format(self.x, self.y, self.dir)
    def move(self, n=1): return DirectedPoint(self.x + n*self.dir.x, self.y + n*self.dir.y, self.dir)
    def rotate(self, n=1):
        '''rotate the point n times, clockwise'''
        n %= 4
        if n == 1: dir = Point(self.dir.y, -self.dir.x)
        elif n == 2: dir = Point(-self.dir.x, -self.dir.y)
        elif n == 3: dir = Point(-self.dir.y, self.dir.x)
        else: dir = self.dir
        return DirectedPoint(self.x, self.y, dir)

class PointND(tuple):
    '''A point in n-dimensional space'''
    # + 
    @singledispatchmethod
    def __add__(self, other): return PointND(a + b for a, b in zip(self, other))
    @__add__.register
    def _(self, other: int): return PointND(a + other for a in self)
    # -
    @singledispatchmethod
    def __sub__(self, other): return PointND(a - b for a, b in zip(self, other))
    @__sub__.register
    def _(self, other: int): return PointND(a - other for a in self)
    # *
    @singledispatchmethod
    def __mul__(self, other): return PointND(a * b for a, b in zip(self, other))
    @__mul__.register
    def _(self, other: int): return PointND(a * other for a in self)
    # /
    @singledispatchmethod
    def __truediv__(self, other): return PointND(a / b for a, b in zip(self, other))
    @__truediv__.register
    def _(self, other: int): return PointND(a / other for a in self)
    # //
    @singledispatchmethod
    def __floordiv__(self, other): return PointND(a // b for a, b in zip(self, other))
    @__floordiv__.register
    def _(self, other: int): return PointND(a // other for a in self)
    #
    def __abs__(self): return sum(abs(a) for a in self) # manhattan distance
    def __repr__(self): return 'PointND({})'.format(', '.join(map(str, self)))

class Grid(defaultdict):
    def __init__(self, it: Union[str,list,dict], **kwargs):
        '''it: a string representing the grid, or a list of list where
        it[y][x] is the value at (x,y).
        walkable and forbidden are optional functions
        oob_behaviour can be 'error', 'expand', or 'loop'
        default for what an empty tile should contain; default is to fail.
        '''
        # convert stuff to dict
        if isinstance(it, str): it = it.split('\n')
        if isinstance(it, list) and isinstance(it[0], str):
            it = [list(l) for l in it]
        if isinstance(it, list):
            res = {}
            for y, row in enumerate(it):
                for x, val in enumerate(row): res[Point(x,y)] = val
            it = res
        # init
        default = kwargs.get('default', lambda: (_ for _ in ()).throw(RuntimeError("Grid has no default value")))
        self.walkable = kwargs.get('walkable', lambda v: True)
        if isinstance(self.walkable, str):
            walkset = set(self.walkable)
            self.walkable = lambda c: c in walkset
        self.forbidden = kwargs.get('forbidden', lambda v: False)
        if isinstance(self.forbidden, str) or isinstance(self.forbidden, list):
            self.forbidden = set(self.forbidden)
        if isinstance(self.forbidden, set):
            temp = self.forbidden # lambda capture; not sure if this is necessary
            self.forbidden = lambda c: c in temp
        self.oob_behaviour = kwargs.get('oob_behaviour', 'error')
        # get rid of all used keys here
        kwargs = {k: v for k, v in kwargs.items() if k not in {'default', 'walkable', 'forbidden', 'oob_behaviour'}}
        super().__init__(default, it, **kwargs)
        # find grid boundaries
        xmi,xma,ymi,yma = (float('inf'),-float('inf'))*2
        for p in it:
            xmi = min(xmi, p.x)
            xma = max(xma, p.x)
            ymi = min(ymi, p.y)
            yma = max(yma, p.y)
        self.xrange,self.yrange = range(xmi,xma+1),range(ymi,yma+1)

    def width(self): return len(self.xrange)
    def height(self): return len(self.yrange)

    def to_string(self, MAP=type('',(object,),{'__getitem__':lambda _,v:v})()):
        return '\n'.join(''.join(MAP[self[x,y]] for x in self.xrange) for y in self.yrange)
    def __repr__(self): return self.to_string()

    def __getitem__(self, key):
        if isinstance(key, tuple): key = Point(*key)
        if isinstance(key, Point):
            if key.x in self.xrange and key.y in self.yrange:
                return super().__getitem__(key)
            elif self.oob_behaviour == 'expand':
                self.xrange = range(min(self.xrange.start, key.x),max(self.xrange.stop, key.x+1))
                self.yrange = range(min(self.yrange.start, key.y),max(self.yrange.stop, key.y+1))
                return super().__getitem__(key)
            elif self.oob_behaviour == 'loop':
                return super().__getitem__(Point(self.xrange.start + (key.x % self.width()),
                                                 self.yrange.start + (key.y % self.height())))
            else: raise IndexError('Grid index {} out of bounds'.format(key))
        elif isinstance(key, int): # grab a row
            return [self[(x,key)] for x in self.xrange]
        else: raise TypeError('Grid indices must be integers or Point, not {}'.format(key))

    def __setitem__(self, key, value):
        if isinstance(key, tuple): key = Point(*key)
        if isinstance(key, Point):
            if key.x in self.xrange and key.y in self.yrange:
                super().__setitem__(key, value)
            elif self.oob_behaviour == 'expand':
                self.xrange = range(min(self.xrange.start, key.x),max(self.xrange.stop, key.x+1))
                self.yrange = range(min(self.yrange.start, key.y),max(self.yrange.stop, key.y+1))
                super().__setitem__(key, value)
            elif self.oob_behaviour == 'loop':
                super().__setitem__(Point(self.xrange.start + (key.x % self.width()),
                                          self.yrange.start + (key.y % self.height())), value)
            else: raise IndexError('Grid index {} out of bounds'.format(key))
        else: raise TypeError('Grid indices must be integers or Point, not {}'.format(key))

    def find_unique(self, v: Any) -> Point:
        for p, val in self.items():
            if val == v: return p
        return None

    def adj(self, point: Point) -> List[Point]:
        res = []
        for d in [Point(0,-1), Point(1,0), Point(0,1), Point(-1,0)]:
            nxt = point + d
            if self.oob_behaviour != 'error' or (nxt.x in self.xrange and nxt.y in self.yrange):
                res.append(nxt)
        return res

    def adj8(self, point: Point) -> List[Point]:
        res = []
        for d in [Point(0,-1), Point(1,0), Point(0,1), Point(-1,0),
                  Point(1,-1), Point(1,1), Point(-1,1), Point(-1,-1)]:
            nxt = point + d
            if self.oob_behaviour != 'error' or (nxt.x in self.xrange and nxt.y in self.yrange):
                res.append(nxt)
        return res

    def distance_map(self, start: Point, end: Point=None) -> Dict[Point,int]:
        if self.oob_behaviour != 'error':
            print('Warning: distance_map() is not guaranteed to work on a grid without static boundaries.')
        if not self.walkable(self[start]) or self.forbidden(self[start]): return {}
        distance_map = {start: 0}
        frontier = deque([start])
        while frontier:
            current = frontier.popleft()
            for nxt in self.adj(current):
                if nxt not in distance_map and self.walkable(self[nxt])\
                        and not self.forbidden(self[nxt]):
                    distance_map[nxt] = distance_map[current] + 1
                    if nxt == end: return distance_map
                    frontier.append(nxt)
        return distance_map

    def dist_between(self, start: Point, goal: Point) -> Optional[int]:
        return self.distance_map(start, goal).get(goal, None)

    def all_distance_maps(self) -> List[Dict[Point,int]]:
        seen = set()
        res = []
        for pt in self:
            if pt not in seen:
                res.append(self.distance_map(pt))
                for p in res[-1]: seen.add(p)
        return res

import lazy_import
nx = lazy_import.lazy_module("networkx")
def grid_to_graph(grid: Grid, ignore: Callable[[Any],bool]=lambda v: False, important: Callable[[Any],bool]=lambda v: True):
    '''grid: a Grid object
    ignore: a function that takes a value and returns True if the node
    should be ignored.
    important: a function that takes a value and returns False if the
    node should be ignored.
    returns an nx.DiGraph where the nodes are the points in grid.
    '''
    graph = nx.DiGraph()
    for start,dmap in grid.all_distance_maps():
        if ignore(grid[start]) or not important(grid[start]): continue
        graph.add_node(start, value=grid[start])
        for end, dist in dmap.items():
            if ignore(grid[end]) or not important(grid[end]): continue
            graph.add_node(end, value=grid[end])
            graph.add_edge(start, end, weight=dist)
    return graph

def save_graph(G, outfile: str="graph.png"):
    import matplotlib.pyplot as plt
    nx.draw(G, with_labels=True)
    plt.savefig(outfile)

''' === MISC === '''
def binsearch(f: Callable, hi, lo=0):
    ''' f(x) returns True if x is too big, False otherwise
    lo <= x < hi '''
    while lo < hi:
        mid = (hi + lo) // 2
        if f(mid): hi = mid
        else: lo = mid + 1
    return lo

def sum_array(ls: int) -> List[int]: return [0] + list(accumulate(ls))

class SAT(list):
    ''' summed array table of a 2d matrix
    !!! (y,x) !!! '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = len(self[0])
        self.height = len(self)
        self.sat = [[0 for _ in range(self.width+1)]\
                for _ in range(self.height+1)]
        for y in range(self.height):
            for x in range(self.width):
                self.sat[y+1][x+1] = self.sat[y][x+1] + self.sat[y+1][x] - self.sat[y][x] + self[y][x]
    def area(self, x1, y1, x2, y2):
        x1,y1,x2,y2 = x1+1,y1+1,x2+1,y2+1
        if x1 > x2 or y1 > y2 or x1 < 0 or y1 < 0 or x2 > self.width or y2 > self.height: raise RuntimeError('Invalid region')
        return self.sat[y2][x2] - self.sat[y2][x1] - self.sat[y1][x2] + self.sat[y1][x1]

import heapq
class PQ(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        heapq.heapify(self)
    def push(self, v): return heapq.heappush(self, v)
    def pop(self): return heapq.heappop(self)

if __name__ == '__main__':
    # points
    assert Point(1,2) + Point(3,4) == Point(4,6)
    assert Point(1,2) - Point(3,4) == Point(-2,-2)
    assert Point(1,2) * Point(3,4) == Point(3,8)
    assert Point(1,2) * 5 == Point(5,10)
    dp = DirectedPoint(0,0,'N')
    dp = dp.move()
    assert dp == DirectedPoint(0,1,'N')
    dp = dp.rotate(3)
    dp = dp.move(4)
    assert dp == DirectedPoint(-4,1,'E')

    # grid
    grid = Grid('''#############
#b.A.@.a#Cd#
#############''', forbidden=lambda c: c == '#')
    print(grid[(1,1)])
    print(grid.adj(Point(1,1)))
    print(grid.adj8(Point(0,0)))
    print(grid.distance_map(Point(1,1)))
    print(grid.dist_between(Point(1,1), Point(4,1)))
    # test an expanding grid
    expanding = Grid({Point(0,0): '*'}, default=lambda: '#', forbidden='#', oob_behaviour='expand')
    print(expanding.distance_map(Point(0,0)))
    print(repr(expanding))
    # SAT
    sat = SAT([[31,2,4,33,5,36],
        [12,26,9,10,29,25],
        [13,17,21,22,20,18],
        [24,23,15,16,14,19],
        [30,8,28,27,11,7],
        [1,35,34,3,32,6]])
    print(sat.area(1,2,4,4))
