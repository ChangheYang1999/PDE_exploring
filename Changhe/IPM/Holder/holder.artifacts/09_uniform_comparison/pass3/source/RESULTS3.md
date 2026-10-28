# Results of the uniform comparison (third pass)

Produced by `combine3.py` (modes `thm35` and `thm37`, same nodes and lower certificates) and this script. On each upper
segment the smaller of the two segment bounds is used (`PROOF3.md`, "Minimum"). Every number is the exponential of the
upper endpoint of an Arb ball (200 bits), rounded up in the last place shown.

- `thm35` alone: C log ratio $\le$ `[0.079191728384680823602 +/- 3.52e-22]` (ratio $\le$ 1.0824118313, near 0.65942, group 4); D log ratio $\le$ `[0.25414851282537280670 +/- 9.23e-22]` (ratio $\le$ 1.2893632771, near 0.59066, group 3).
- `thm37` alone: C log ratio $\le$ `[0.060616150630642690128 +/- 4.01e-22]` (ratio $\le$ 1.0624909995, near 0.68442, group 4); D log ratio $\le$ `[0.25414851282537280670 +/- 9.23e-22]` (ratio $\le$ 1.2893632771, near 0.59066, group 3).

| group | worst C ratio (min of both) | segment | from | worst D ratio | segment |
|---|---|---|---|---|---|
| 0 | 1.0259006430 | [33/200, 19/100] | thm35 | 1.1318416169 | [33/200, 19/100] |
| 1 | 1.0501142617 | [13/40, 7/20] | thm35 | 1.2231013549 | [13/40, 7/20] |
| 2 | 1.0518914754 | [19/40, 1/2] | thm37 | 1.2773204342 | [19/40, 1/2] |
| 3 | 1.0598843404 | [23/40, 3/5] | thm37 | 1.2893632771 | [23/40, 3/5] |
| 4 | 1.0624909995 | [27/40, 7/10] | thm37 | 1.2891972347 | [3/5, 5/8] |
| 5 | 1.0621472812 | [7/10, 29/40] | thm37 | 1.2728944042 | [7/10, 29/40] |
| 6 | 1.0553816204 | [4/5, 33/40] | thm37 | 1.2245543504 | [4/5, 33/40] |
| 7 | 1.0469441854 | [9/10, 183/200] | thm35 | 1.1374195265 | [9/10, 183/200] |

Uniform on $[1/200, 199/200]$: $\log\rho_C\le$ `[0.060616150630642690128 +/- 4.02e-22]`, $\rho_C\le1.0624909995$ (segment [27/40, 7/10], group 4, thm37);
$\log\rho_D\le$ `[0.25414851282537280670 +/- 9.24e-22]`, $\rho_D\le1.2893632771$ (segment [23/40, 3/5], group 3).

Nodal cross-check. The `thm37` upper values for $C_\alpha$ at the nodes $\frac12$ (groups 2 and 3), $\frac34$ (group 5) and $\frac9{10}$ (group 6) are
`[2.1970179508472502293 +/- 1.88e-21]`, `[2.1970179508472502293 +/- 1.88e-21]`, `[2.6442935977670703615 +/- 1.50e-20]` and `[5.0137426872952893322 +/- 2.03e-20]`. They agree with the single-exponent
Theorem 3.7 certificates $C_{1/2}\le2.1970179509$, $C_{3/4}\le2.6442935978$, $C_{9/10}\le5.0137426873$ of the report (Table 1).

The end intervals are unchanged (`../uniform/PROOF.md`, section 5: $C$ ratio at most $1.0263$, $D$ ratio at most $1.0324$ there).

## Reproduction

```
bash run3.sh            # local and middle node chunks (local/, mid/)
python3 combine3.py thm37 --nodes ../uniform/nodes2.json --upper ../uniform/upper_n384.json,../uniform/upper_n384_b.json --lower ../uniform/lower2_g --far ../uniform/far2_g --tag _pass3
python3 combine3.py thm35 --nodes ../uniform/nodes2.json --upper ../uniform/upper_n384.json,../uniform/upper_n384_b.json --lower ../uniform/lower2_g --far ../uniform/far2_g --tag _pass3
python3 make_results3.py
```

## SHA-256

| file | sha256 |
|---|---|
| `PROOF3.md` | `d77096847a5658eda398a9a4c5e0fc5592dab30b8a9a87d7c2f09c5ae86a7574` |
| `combine3.py` | `ae26319d314bfd03158722ea10a9bed58bb0c8a18d61744db892a6235264d130` |
| `make_results3.py` | `5c8ef9a9a176d4fd183869a7779b8456b178ad89856d5246c135390c2da2c2e1` |
| `local_nodes.py` | `808028d0874fb203d85ec20628e3c459176c0741d2c3aa67a014d5e9a7b0cd8f` |
| `mid_nodes.py` | `81dc4c89a4e3768efafae3c2754b1249d9c3aa63bd48716714cf409f9f9aaeee` |
| `run3.sh` | `87a2bae21df510d1586862f3a88143b1a26395d0ead5dbe2acabefd91a1c1d58` |
| `certify_local_circles_greedy.py` | `38b0dd756ac0656f07bbf6889199810d9be31475e440acc08870499bcc72a16b` |
| `local_circle_greedy.py` | `5245fb3d224a76661c8eae63afc06ae59d38dff2a50b95481446e528b73f5384` |
| `middle_circle_plan.py` | `4921fda2f3451cad9e729462cde30cfe45f942b41e83bf55359b790712051fa9` |
| `circle_transport_plan.py` | `b61a003cd05e990c64fcb00b82275e54cf0c53acbe1baba2faaa6428150db82f` |
| `uniform_result_thm35_pass3.json` | `290f34929e3173cf6c9f5746d5e12390b0027842be419bf386aaa6ae67270848` |
| `uniform_result_thm37_pass3.json` | `c90095411430cf5535ff21f5ea817db04d3791bcbc10f179395be048f64e43ac` |
| `local/r0_128_11_20.json` | `c2e9d96350ef9ae36e1131a5c40a6c2c6b86932fe91ad5f989219732ba016724` |
| `local/r0_128_13_20.json` | `606b80054885462c2a68157b51bd8d842f683c9cd719d5a0badb72664fdc2331` |
| `local/r0_128_17_20.json` | `59dd2c484bfdb976a2b162961b42c092ffdea85fbe9a8a3871d0281b6db5ba0c` |
| `local/r0_128_17_40.json` | `bf8a38c310bfeef68329a77503fcd08ffb7ace2e28b26285841b476aa7d0512f` |
| `local/r0_128_19_40.json` | `d434f0f55bb36af48816e5ed95cede1ec673e2f0f95dc702d23269fc38757221` |
| `local/r0_128_1_2.json` | `3ac75097ca07b600108b7737ce32612a0db85912dc85aa877f7a2aaa0f4afcff` |
| `local/r0_128_21_40.json` | `c2c40df71b687b5720ed8cb2c5d7441d3305b2583ae4df681bdeea9424f6990e` |
| `local/r0_128_23_40.json` | `2bdcfe9494dafd697a029715fb014a99431713f03c19b30ea7fb8761b93d37d3` |
| `local/r0_128_27_40.json` | `915e0ad60b3caeffef9de6a4ab3438da0d1101cac42d09b10f1f604536695f5f` |
| `local/r0_128_29_40.json` | `3d214bff4ddafd0d4a42b8e10b7dd4022c11b5e95a3ae7e651b13ca32fa5cadb` |
| `local/r0_128_2_5.json` | `d22bf13b98a2b764cbcefc29455528dd9870a6ca14fdc58b87fddee72165c297` |
| `local/r0_128_31_40.json` | `e7e3313f4b6f4eda93ac334dca1a35fc4e6e6cfa805a3994f21779e44d2cc165` |
| `local/r0_128_33_40.json` | `c19ff957615b6c8e178917d7b3390020b4c5a17af0e7e1aa6d9b1ad520a0b3c0` |
| `local/r0_128_3_10.json` | `dc10025219c7a04ad11cf70d2c3972d0f7376eea0a85ac7e699e9e3f937fcb80` |
| `local/r0_128_3_4.json` | `1c41e46bb113cbb7fd0a72c794e3cc9d5aab0757cb53693defb791d608f71dc6` |
| `local/r0_128_3_5.json` | `03cc07915766eda0d795c02609240b64cd50802cf0190b7567bf865844e76620` |
| `local/r0_128_3_8.json` | `0748b75217bf273b0d2c888a130e32a10bfd1e9837bd06f6446eb93fb7c61fb6` |
| `local/r0_128_4_5.json` | `7a6f9ab0ffe8b6f8e6ce33376e69f895a66281a513c2c78e8195a8a24ac69d35` |
| `local/r0_128_5_8.json` | `b978825c31f71a241a7347dfb6abd3a23fa2a67b46009c505222c5e91c944db3` |
| `local/r0_128_7_10.json` | `2559405f4d754d3117d25b551853bf6c4350cc7a0c797746f59424f469b84553` |
| `local/r0_128_7_20.json` | `b66ae013eba40c261a1009eac67dc3fcfa8f574abd4499766b6dec6e3ec1437e` |
| `local/r0_128_7_8.json` | `fe79b83bf7b4137ccf2f1cbce2209e2bec651596b16f07fcfde4b3d5749d02c1` |
| `local/r0_128_9_10.json` | `0e4586c286587dfc55becf384893dd52dcf4da07dc817d1d53b058e111f9acdc` |
| `local/r0_128_9_20.json` | `82955dae70ec919f4885cec37e0ef75ccb9c28c199975ee9c41609c035c4080e` |
| `local/r128_256_11_20.json` | `72356d721113b6a2067f6a5ab90f8c15bc42c22a5876475a8ce7bb3a0b19b2eb` |
| `local/r128_256_13_20.json` | `b02518d13bc27d54e13a2d730592ca4aecbf26352f1cf2fb647698ec93988956` |
| `local/r128_256_17_20.json` | `324be3687432c2644d04c79f587ba6a123a398b59d2509bafa2791f12ec57e20` |
| `local/r128_256_17_40.json` | `dd76a30f4f2051bab6473f2b7badc48ed70994ae21dbad320a299d04bbad4da8` |
| `local/r128_256_19_40.json` | `27d64804975d8ff6a0085472c6bf3fcdd4e0a4ef278894a9e172ec5f0ac23e20` |
| `local/r128_256_1_2.json` | `be55902503e4cc1daa386e085aeeb67f57046fab46e4dd9c2fec9e0f92cab357` |
| `local/r128_256_21_40.json` | `9970f77768f7022bec6182af26c050e5440717ea7be41fd130bf3845521979fc` |
| `local/r128_256_23_40.json` | `e626577466b5d925bd8e8dbee107dc77a517c9c1631a1471ed89ccb8c7179018` |
| `local/r128_256_27_40.json` | `d929dc4291622f375e715bf2dd3d6634c70a4c9fa1d4f4e41e5900b69ccce7cf` |
| `local/r128_256_29_40.json` | `c8dc533bb8f21610f2bd52e49bac551a03d09adea7c1cf22d99137ffcf47e8b4` |
| `local/r128_256_2_5.json` | `0eb5b77453629317c6ca93acbf20e470a94a7adf72d7a9b747093ada47130924` |
| `local/r128_256_31_40.json` | `3f912b39a3471e9c896fbfd9a21c3ee7a6cd5220affa8d953e3aa7d6809b1f67` |
| `local/r128_256_33_40.json` | `a2b562d9946ecc7d3ba48f51c905839d30e037dff813f381eec5b9c653a46a9b` |
| `local/r128_256_3_10.json` | `a2364e834113f33452ab71a4f9b46e8ad423b7ff4e253dfb9ada9b3cfa1ff494` |
| `local/r128_256_3_4.json` | `ddd299d1d20b17823695d8055e65f414dfb07947a0399c82e876d331a283a78e` |
| `local/r128_256_3_5.json` | `a0a4fdf35e295ec4128244bc7eaa1a5a10136fed32c367f95e1e15fd444f6b36` |
| `local/r128_256_3_8.json` | `2140501a79a969601b8a693b62259a6e54dded09b0c381b1effc072c09b3dcdf` |
| `local/r128_256_4_5.json` | `a8ad380f4123fc2b3ccd22ca37d8dc6d789f8de9cdcf57d1b1ad9d32b690accf` |
| `local/r128_256_5_8.json` | `10f90efe36b4d2605f3a78cf26e0dc232bb8f51071f7b95baa4a3da198d37314` |
| `local/r128_256_7_10.json` | `dceb3030d0aaa89580ebd83899113d2fb44f8ce65da77824e10b4c7538575d76` |
| `local/r128_256_7_20.json` | `a08062f1fbd7080a061d2ed4735f4f73dc5535c894b32d3f6c43c08fee099205` |
| `local/r128_256_7_8.json` | `2f64b84d9f3ab750d9c2625ef8ab12d4ce9a860cdac1a24927bbea4ed13a3794` |
| `local/r128_256_9_10.json` | `21b70b1c6fdb7f88c9d5a30a04a266f66864ddc7a967e7e97f06b3d3184d4737` |
| `local/r128_256_9_20.json` | `0cb8e357ddf42c19542dbf9eb2ebf0b37502d18203ddde93e4526ae10a43bd55` |
| `mid/n512_0.json` | `3b5d6656ec950d109e5284702168332fc00ccd2cdd30f217fb3ad6149747f11d` |
| `mid/n512_128.json` | `7a184ceca1742dd727ca9f406c12fd4d5adf677cc3e6f4a6561784dee5597079` |
| `mid/n512_160.json` | `bb199eb319a009e0ec6f9a66df217d504d1906781c540cec9ae378cd4ca5a491` |
| `mid/n512_192.json` | `8a4f577a3f08205a11b4ad346ef40ae054c7b14413e06cfdfbcb994aea6a1b79` |
| `mid/n512_224.json` | `b6f9aaf865bd0e70d31e3d7d841e14ebc21f7cbd35350dcbe18a39286ad5aee7` |
| `mid/n512_256.json` | `e49191ba92f54e88ab13ea3c05d3dba0c43984dd1e6fc49a28171e3733ed9229` |
| `mid/n512_288.json` | `d0806a7f3fa282c43dad90354a2cfd3ab2f4f2aabb7dda23902b390fdd93576f` |
| `mid/n512_32.json` | `81b94ec825d951c8bdd9abfec09c7c57f34fa1c1ea89b308949a0490c922aca5` |
| `mid/n512_320.json` | `ee907ff102f230905735f24cbc26880dc53f7fcb7a571672ca24f6c9118e1449` |
| `mid/n512_352.json` | `7d5c1ee6d0e1fb961c5f59cdb5fe2bac9f1736c2aa93bff52dfbb83cd44d8711` |
| `mid/n512_384.json` | `1c5036bce9c02fe80eef46b892f35c4f91caad6cf879480c1a45760984ed9070` |
| `mid/n512_416.json` | `463042b10a4f36287f15a2e320462ba5bd62dc71ecf88ebc8c3a2d2f0c43b051` |
| `mid/n512_448.json` | `edd816ce17e8f0ffd412bfddb1a6cbe2b64066f795909e77c83dbf552190451d` |
| `mid/n512_480.json` | `03ec4942e1a0a536a2d8f4767f3ddfc07b26b71b5005680022cf646a3900118f` |
| `mid/n512_64.json` | `c528812a0cc7e6cf04d713fab783fc35e868fac84d879b03e89ac08a040a7231` |
| `mid/n512_96.json` | `983dfe4983fe4b1253a8c629236311d057b532e34ee9e6bcc17172219c467ae6` |
