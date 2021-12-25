int __cdecl main(int argc, const char **argv, const char **envp)
{
  unsigned int *v3; // rbx
  unsigned int *v4; // rsi
  __int64 v5; // rsi
  __int64 v6; // rdi
  _BOOL8 v7; // rdx
  __int64 v8; // rcx
  __int64 v9; // rsi
  __int64 v10; // rcx
  _BOOL8 v11; // rdx
  __int64 v12; // rcx
  _BOOL8 v13; // rax
  __int64 v14; // rsi
  __int64 v15; // rcx
  __int64 v16; // rcx
  __int64 v17; // rdi
  __int64 v18; // rcx
  __int64 v19; // rdx
  __int64 v20; // rdi
  __int64 v21; // rsi
  _BOOL8 v22; // rax
  __int64 v23; // rcx
  __int64 v24; // rdi
  __int64 v25; // rcx
  _BOOL8 v26; // rax
  __int64 v27; // rsi
  __int64 v28; // rdi
  __int64 v29; // rsi
  _BOOL8 v30; // rax
  __int64 v31; // rcx
  __int64 v32; // rdi
  __int64 v33; // rcx
  _BOOL8 v34; // rax
  __int64 v35; // rsi
  __int64 v36; // rdi
  __int64 v37; // rsi
  __int64 v38; // rcx
  __int64 v39; // rdx
  __int64 v40; // rsi
  _BOOL8 v41; // rax
  _BOOL8 v42; // rdx
  unsigned __int64 v43; // rcx
  _BOOL8 v44; // rdx
  unsigned __int64 v45; // rcx
  unsigned __int64 v46; // rax
  _BOOL8 v47; // rdx
  unsigned __int64 v48; // rcx
  __int64 v49; // rdx
  unsigned __int64 v50; // rcx
  _BOOL8 v51; // rdx
  unsigned __int64 v52; // rcx
  unsigned __int64 v53; // rax
  _BOOL8 v54; // rdx
  unsigned __int64 v55; // rcx
  __int64 v56; // rdx
  unsigned __int64 v57; // rsi
  _BOOL8 v58; // rdx
  unsigned __int64 v59; // rcx
  _BOOL8 v60; // rdx
  unsigned __int64 v61; // rsi
  _BOOL8 v62; // rax
  unsigned __int64 v63; // rcx
  _BOOL8 v64; // rdx
  unsigned __int64 v65; // rax
  _BOOL8 v66; // rdx
  unsigned __int64 v67; // rcx
  _BOOL8 v68; // rdx

  v3 = input;
  do
  {
    v4 = v3++;
    __isoc99_scanf(&unk_2004, v4, envp);
  }
  while ( &input[14] != v3 );
  v5 = input[1];
  v6 = input[3];
  v7 = (input[0] + 7LL) * (input[0] != 12LL)
     - 26
     * ((__int64)((unsigned __int128)(0x4EC4EC4EC4EC4EC5LL * (__int128)((input[0] + 7LL) * (input[0] != 12LL))) >> 64) >> 3)
     + 13 != v5;
  v8 = v5 + 8;
  v9 = input[2];
  v10 = v8 * v7 + (input[0] + 7LL) * (input[0] != 12LL) * (25 * v7 + 1);
  v11 = v10 - 26 * ((__int64)((unsigned __int128)(0x4EC4EC4EC4EC4EC5LL * (__int128)v10) >> 64) >> 3) + 13 != v9;
  v12 = (v9 + 10) * v11 + v10 * (25 * v11 + 1);
  v13 = v12 - 26 * ((__int64)((unsigned __int128)(0x4EC4EC4EC4EC4EC5LL * (__int128)v12) >> 64) >> 3) - 2 != v6;
  v14 = (v6 + 4) * v13
      + ((__int64)((unsigned __int128)(0x4EC4EC4EC4EC4EC5LL * (__int128)v12) >> 64) >> 3) * (25 * v13 + 1);
  v15 = (input[4] + 4LL) * (v14 % 26 - 10 != input[4]) + v14 / 26 * (25LL * (v14 % 26 - 10 != input[4]) + 1);
  v16 = (input[5] + 6LL) * (v15 % 26 + 13 != input[5]) + v15 * (25LL * (v15 % 26 + 13 != input[5]) + 1);
  v17 = (input[6] + 11LL) * (v16 % 26 - 14 != input[6]) + v16 / 26 * (25LL * (v16 % 26 - 14 != input[6]) + 1);
  v18 = v17 / 26;
  v19 = v17 % 26;
  v20 = input[8];
  v21 = (input[7] + 13LL) * (v19 - 5 != input[7]) + (25LL * (v19 - 5 != input[7]) + 1) * v18;
  v22 = v21 % 26 + 15 != v20;
  v23 = v20 + 1;
  v24 = input[9];
  v25 = v23 * v22 + (25 * v22 + 1) * v21;
  v26 = v25 % 26 + 15 != v24;
  v27 = v24 + 8;
  v28 = input[10];
  v29 = v27 * v26 + (25 * v26 + 1) * v25;
  v30 = v29 % 26 - 14 != v28;
  v31 = v28 + 4;
  v32 = input[11];
  v33 = v31 * v30 + v29 / 26 * (25 * v30 + 1);
  v34 = v33 % 26 + 10 != v32;
  v35 = v32 + 13;
  v36 = input[12];
  v37 = v35 * v34 + (25 * v34 + 1) * v33;
  v38 = v37 / 26;
  v39 = v37 % 26;
  v40 = input[13];
  v41 = v39 - 14 != v36;
  __printf_chk(
    1LL,
    "z: %ld\n",
    (25LL * (((v36 + 4) * v41 + v38 * (25 * v41 + 1)) % 26 - 5 != v40) + 1)
  * (((v36 + 4) * v41 + v38 * (25 * v41 + 1))
   / 26)
  + (v40 + 14) * (((v36 + 4) * v41 + v38 * (25 * v41 + 1)) % 26 - 5 != v40));
  v42 = (input[0] + 7LL) * (unsigned __int64)(input[0] != 12LL) % 26 + 13 != input[1];
  v43 = (input[1] + 8LL) * v42 + (input[0] + 7LL) * (input[0] != 12LL) * (25 * v42 + 1);
  v44 = v43 % 26 + 13 != input[2];
  v45 = (input[2] + 10LL) * v44 + v43 * (25 * v44 + 1);
  v46 = v45 / 26;
  v47 = v45 % 26 - 2 != input[3];
  v48 = ((input[3] + 4LL) * v47 + (25 * v47 + 1) * (v45 / 26)) / 26;
  v49 = (input[3] + 4LL) * v47 + (25 * v47 + 1) * v46 - 26 * v48;
  v50 = (input[4] + 4LL) * (v49 - 10 != input[4]) + v48 * (25LL * (v49 - 10 != input[4]) + 1);
  v51 = v50 % 26 + 13 != input[5];
  v52 = (input[5] + 6LL) * v51 + v50 * (25 * v51 + 1);
  v53 = v52 / 26;
  v54 = v52 % 26 - 14 != input[6];
  v55 = ((input[6] + 11LL) * v54 + (25 * v54 + 1) * (v52 / 26)) / 26;
  v56 = (input[6] + 11LL) * v54 + (25 * v54 + 1) * v53 - 26 * v55;
  v57 = (input[7] + 13LL) * (v56 - 5 != input[7]) + (25LL * (v56 - 5 != input[7]) + 1) * v55;
  v58 = v57 % 26 + 15 != input[8];
  v59 = (input[8] + 1LL) * v58 + (25 * v58 + 1) * v57;
  v60 = v59 % 26 + 15 != input[9];
  v61 = (input[9] + 8LL) * v60 + (25 * v60 + 1) * v59;
  v62 = v61 % 26 - 14 != input[10];
  v63 = (input[10] + 4LL) * v62 + v61 / 26 * (25 * v62 + 1);
  v64 = v63 % 26 + 10 != input[11];
  v65 = ((input[11] + 13LL) * v64 + (25 * v64 + 1) * v63) / 26;
  v66 = ((input[11] + 13LL) * v64 + (25 * v64 + 1) * v63) % 26 - 14 != input[12];
  v67 = (input[12] + 4LL) * v66 + (25 * v66 + 1) * v65;
  v68 = v67 % 26 - 5 != input[13];
  __printf_chk(1LL, "z: %ld\n", (25 * v68 + 1) * (v67 / 26) + (input[13] + 14LL) * v68);
  return 0;
}
