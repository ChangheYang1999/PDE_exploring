# Candidate snapshots

This folder holds the candidate profile snapshots of the campaign. INDEX.md is the snapshot index. Each snapshot folder keeps its original SHA256SUMS file, which lists the sha256 of every file of the full snapshot.

Complete snapshots (every file present; data files byte-identical to the original):

- C1-N1-007-d2w-j7-e2bal
- C1-N1-016-legqs25-quot013

Complete snapshots with the large data file stored gzip-compressed (gzip level 9, no name, mtime 0) to save space. The original sha256 refers to the decompressed file:

- C1-N1-021-heldin14-legqs25p50
- C1-N1-022-legqs25-m16to23

Manifest-only snapshots (MANIFEST.json, SHA256SUMS and the small result files under 100 KB; the large exact data file is not included):

- C1-N1-001-refit860-jabs
- C1-N1-002-7branch-frf
- C1-N1-003-8branch-frf
- C1-N1-004-4branch-l2fw
- C1-N1-005-d2w-j7-x3
- C1-N1-006-8branch-e2
- C1-N1-008-d2w-j7-x3bal
- C1-N1-009-d2w-j7-x3balk
- C1-N1-010-d2w-j7-x3bal-legqs
- C1-N1-011-e2bal-legqs-from007
- C1-N1-012-e2balk1e7-from009
- C1-N1-013-pairU-from007
- C1-N1-014-pairB-from007
- C1-N1-015-pairQ-quot013
- C1-N1-017-legqs50-quot013
- C1-N1-018-legqs25-cont12
- C1-N1-019-legqs50-cont12
- C1-N1-020-legqs25p50-quot013
- C1-N1-023-legqs25p100-quot013
- C1-N1-024-rulem32-legqs25
- C1-N1-025-combined-heldin1e16
- C1-N1-026-heldin1e16-legqs25-m16to23
- C1-N1-027-cont60-legqs25-m16to23
- C1-N1-028-legqs25-nin24

Notes:

- MANIFEST.json files had local absolute paths rewritten to folder-relative paths, so their sha256 differs from the value in the snapshot SHA256SUMS. All other files are unmodified.
- To verify a complete snapshot: `cd candidates/<ID> && sha256sum -c SHA256SUMS` (MANIFEST.json reports a mismatch for the reason above).
- To restore a compressed file and verify it: `cd candidates/<ID> && gunzip -k <file>.json.gz && sha256sum -c SHA256SUMS`.
- To verify a manifest-only snapshot against the full snapshot set, compare the data file with the sha256 listed below.

## Original sha256 of every snapshot file

| Snapshot | File | Size (bytes) | In this folder | Original sha256 |
|---|---|---|---|---|
| C1-N1-001-refit860-jabs | MANIFEST.json | 3970 | included | `ad21fbebe42daac80cbe6bca1b50c81c93d01ddde08e5d51a83e03158f454146` |
| C1-N1-001-refit860-jabs | candA_Jabs_exact.json | 151909 | not included | `8077f1305e5403264831de280689bb9334628bd1aa1233ce4dec58017dc355c7` |
| C1-N1-001-refit860-jabs | sector_table.json | 8647 | included | `72b97b016884aec44979b36715d741ed64a11c47699b29d5eede4bcf664a5c6d` |
| C1-N1-002-7branch-frf | MANIFEST.json | 5293 | included | `5491f4cd005caf44b2b0c2701bbf35e84ddc6c039ad656b5be407c9bc5d27837` |
| C1-N1-002-7branch-frf | candB_j6_exact.json | 1783190 | not included | `74f3b4cbcb3cb83289f518ce25e27a54273959dc78f637b6b9e12efb41c8669b` |
| C1-N1-002-7branch-frf | candB_j6_n4_d012_FrF_R1e4_gauss160_diag_mid200.json | 4382 | included | `cc1c60204798dec12d2c08c657c1b1c05810ec21029debd60313bad5ad863361` |
| C1-N1-002-7branch-frf | sector_table.json | 16781 | included | `2ee200240032615af8affb82535dbcb5f80e24c34743d966b187d3083b5ac50f` |
| C1-N1-003-8branch-frf | MANIFEST.json | 4821 | included | `822a16c58be628a00ec38f6ccb832ceae9f80fb04876c9d4cff34a7c2c881397` |
| C1-N1-003-8branch-frf | candB_j7_exact.json | 2824276 | not included | `a4814f4b93aa4904a67fa773ca11ef84bf050971b1f5ea2ca62eeab5b9952ee3` |
| C1-N1-003-8branch-frf | candB_j7_n4_d012_FrF_R1e4_mid200_diag_mid200.json | 4377 | included | `915e4b7f2eeb8c124f5369561c7eea4358fa0eb0a285fc7d98b20658aa291ee0` |
| C1-N1-003-8branch-frf | sector_table.json | 13146 | included | `c143c8721f070e67b63da39cb9064485f70295a7f14838e1a7b9e42ee012b286` |
| C1-N1-004-4branch-l2fw | MANIFEST.json | 4613 | included | `2d1c0b32ca13d6135990d647f0ac979a326e0e7edbd9bf1e9ac23a42daf81a2f` |
| C1-N1-004-4branch-l2fw | sector_table.json | 16808 | included | `5a3b44bbd4441881f2763cf8ed3edee4bb2bf48b4720670b8a63b140347510d3` |
| C1-N1-004-4branch-l2fw | x_j3_exact.json | 313478 | not included | `898981d8e2e86fd31a0373cd102afcef8295e2c90e62ebe5bc3a3de34031b528` |
| C1-N1-005-d2w-j7-x3 | MANIFEST.json | 6360 | included | `d0a1e5a242cc7c7d8967d1cef34f4cfbd9ac963f45109324507ee058fee1f9b9` |
| C1-N1-005-d2w-j7-x3 | d2w_j7_n4_X3_mid180_diag2.json | 12900 | included | `6ae2116f4e964ab257299d831f541b9b8d49f261ddc52054a5a0d1f900923dec` |
| C1-N1-005-d2w-j7-x3 | d2w_j7_n4_X3_mid180_exact.json | 2928439 | not included | `bd2a8db13b164b8ba83e1667f89686fb42d80464d523a22b537eaccd5fbdbafa` |
| C1-N1-005-d2w-j7-x3 | sector_table.json | 13409 | included | `614e2af6f59a0c78b9322962eb87ba5f946d9329183d72ef0c9861ffee54891a` |
| C1-N1-006-8branch-e2 | MANIFEST.json | 6308 | included | `745d5b0ef9edac7ce019271e91ac9b2640e9fae03e8af6ecb94221a9d7ad660e` |
| C1-N1-006-8branch-e2 | e2_j7_n4_d012_mid200_fromFrF_diag2.json | 12598 | included | `b013da64814b448eb83e2598c4f04a4c30199524131dcef8be4bfb741f4619bf` |
| C1-N1-006-8branch-e2 | e2_j7_n4_d012_mid200_fromFrF_exact.json | 2824478 | not included | `9a09b1a2b54d08f9edbb21d9c83acc21be67e32e3b5334a9115130df5d7f6d3e` |
| C1-N1-006-8branch-e2 | sector_table.json | 13132 | included | `a009b68b5b562391659c2389628668dbc7dcc4a6478a4c74203caf4d09341629` |
| C1-N1-007-d2w-j7-e2bal | MANIFEST.json | 7044 | included | `da19f6ee596f191f5c46ae23eb162c985a5745c2fbc0d63cdc6e3764a46bb143` |
| C1-N1-007-d2w-j7-e2bal | d2w_j7_n4_E2bal_mid180_diag2.json | 14291 | included | `d78123998359f07f266c2758a4e5b3fa8b3b72487ae06e6788977f211311e944` |
| C1-N1-007-d2w-j7-e2bal | d2w_j7_n4_E2bal_mid180_exact.json | 2926809 | included | `ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21` |
| C1-N1-007-d2w-j7-e2bal | sector_table.json | 13414 | included | `9d54471429323126d6270de5779ef6566f6753a1ce943bee65073be75b68f42a` |
| C1-N1-008-d2w-j7-x3bal | MANIFEST.json | 6129 | included | `7fbfaed4867a92d66a1cd3d5fcd5b6d43e82ae61042bad79bf7f829f722773c4` |
| C1-N1-008-d2w-j7-x3bal | d2w_j7_n4_X3bal_mid180_diag2.json | 14224 | included | `32472225005bb68798787d44dfed7edb08efa1b589b3c68c7ca600f139e8f657` |
| C1-N1-008-d2w-j7-x3bal | d2w_j7_n4_X3bal_mid180_exact.json | 2928460 | not included | `ac5eeb9603133a37ca49b621c5d7c9559b3ffcc5d65af150054a246827fbfa5e` |
| C1-N1-008-d2w-j7-x3bal | sector_table.json | 13405 | included | `709feb87184b27b717f7b8ce922047e813ab47cec835f6793c04431e122469dc` |
| C1-N1-009-d2w-j7-x3balk | MANIFEST.json | 6625 | included | `fc9895de1fa2a29b2f8cc07e654830d6e16b00345a96310dc8c1b3d75295bf03` |
| C1-N1-009-d2w-j7-x3balk | d2w_j7_n4_X3balK_mid180_diag2.json | 14246 | included | `84ae149ea6d5c9a2e360753e35f49273ec3d27ec11f82e925bfa0c9f8399f0d7` |
| C1-N1-009-d2w-j7-x3balk | d2w_j7_n4_X3balK_mid180_exact.json | 2926625 | not included | `0d6bddf6a80fcab5afa00efa6989b28b98bf8f43d54493874b8d0d3d4bf98a6c` |
| C1-N1-009-d2w-j7-x3balk | sector_table.json | 13414 | included | `2a3810d4cf8f45c460df7ff0fbcdd85ed80ec7431beca9e92eebeafde611f514` |
| C1-N1-010-d2w-j7-x3bal-legqs | MANIFEST.json | 6508 | included | `2f1c3fc4acc2697be51e3c479d4c1ab2a93a2ee33ee9914fd3ca4dbacaf4645c` |
| C1-N1-010-d2w-j7-x3bal-legqs | d2w_j7_n4_X3bal_legqs_mid180_diag2.json | 14225 | included | `2488ac7bcbc375054678393820fefa59364ea0d44ab942ebb5e84a969a8f3537` |
| C1-N1-010-d2w-j7-x3bal-legqs | d2w_j7_n4_X3bal_legqs_mid180_exact.json | 3057753 | not included | `2341ac50f06d89f6a0dbdf0f27a0e40449edcb62ca772ac66a155e0b7c3fb615` |
| C1-N1-010-d2w-j7-x3bal-legqs | sector_table.json | 13421 | included | `17104bc9e4115a42e0ca1fb04b3a4635129c6994162fd0d0e90f3818c3a467f2` |
| C1-N1-011-e2bal-legqs-from007 | MANIFEST.json | 5452 | included | `264708b6a74159da5b42732464e028b92c409a34ee054a07abcb4d582204d82a` |
| C1-N1-011-e2bal-legqs-from007 | d2w_j7_n4_E2bal_legqs_cpu_m8_diag2.json | 14280 | included | `2526bb3aae39aedd503992bd2fe55a1906b116aa5d5963463c2cdbd394547130` |
| C1-N1-011-e2bal-legqs-from007 | d2w_j7_n4_E2bal_legqs_cpu_m8_exact.json | 3061225 | not included | `ad50dcfa585805c5f563225efadba1121ce71fea6770827f9389cd0b86725c30` |
| C1-N1-011-e2bal-legqs-from007 | d2w_j7_n4_E2bal_legqs_cpu_m8_weaktests2.json | 13187 | included | `e5448317be76a6165cb328c063d7dc9e61f3cbd677994f337eb3f13ccf4ebb7a` |
| C1-N1-011-e2bal-legqs-from007 | sector_table.json | 13401 | included | `e169bc037e2f084b9bf9c625976890cdddec9b5d2ad4bc9a04d9369b51c58c77` |
| C1-N1-012-e2balk1e7-from009 | MANIFEST.json | 5249 | included | `2a367f49897336d8d18bf623025a5f31912f418ca338fde53b6c9eafb071c18e` |
| C1-N1-012-e2balk1e7-from009 | d2w_j7_n4_E2balK_cpu_m8_diag2.json | 14228 | included | `02d94ae562346c8dd78e8f6b3610f1456a63bd047d68b9c924a398d7d668cb1c` |
| C1-N1-012-e2balk1e7-from009 | d2w_j7_n4_E2balK_cpu_m8_exact.json | 2926652 | not included | `3a578c95a394f84fdad2edfdcb52dfa43c284404ce441e68b749ca55ff6ab6fc` |
| C1-N1-012-e2balk1e7-from009 | d2w_j7_n4_E2balK_cpu_m8_weaktests2.json | 13086 | included | `ec4b4f5f6710119d6822cc0454c2ada5f215b46d135c46d52a99f790afe34aa8` |
| C1-N1-012-e2balk1e7-from009 | sector_table.json | 13418 | included | `3a7937d07e4e414a402dd5bb8c7bf365774962a56cebeccc99facabe0bec0162` |
| C1-N1-013-pairU-from007 | MANIFEST.json | 5385 | included | `75d28547996923f5ae39b4663b6641e6b60e7cd7431023fc9debfff351e84b00` |
| C1-N1-013-pairU-from007 | d2w_j7_n4_E2bal_pairU_cpu_m16_diag2.json | 14273 | included | `3053a387d0554ccd5136b65d659980e294520d83a3eb1119bac6dceee451a38a` |
| C1-N1-013-pairU-from007 | d2w_j7_n4_E2bal_pairU_cpu_m16_exact.json | 2928285 | not included | `c07f87ddfe35e1fd82cfb86e01949749381aac7209a752c713dd01b48a478940` |
| C1-N1-013-pairU-from007 | d2w_j7_n4_E2bal_pairU_cpu_m16_weaktests2.json | 13202 | included | `e217a8f9be3a22bede507bccc7c9f04ec5518082e41523beaaed7f8abd0e79b1` |
| C1-N1-013-pairU-from007 | sector_table.json | 13403 | included | `bac5f78f424fa812c82f17e385a22ed0a6313039311c4b5b19a4f756e3e7d0a5` |
| C1-N1-014-pairB-from007 | MANIFEST.json | 5322 | included | `1ebba4b1ebacae6eb3c6562e463a04718814871c40840ad033e81a44b9a82d31` |
| C1-N1-014-pairB-from007 | d2w_j7_n4_E2bal_pairB_cpu_m16_diag2.json | 14292 | included | `78b8efbbb8d4e654d16a4e270228810d62b80e386f3726c61e182429af67964f` |
| C1-N1-014-pairB-from007 | d2w_j7_n4_E2bal_pairB_cpu_m16_exact.json | 2931981 | not included | `8dfc33c3dc5f8265e802831a500d757e2da09bc26890c457c0d3603afc3cb746` |
| C1-N1-014-pairB-from007 | d2w_j7_n4_E2bal_pairB_cpu_m16_weaktests2.json | 13205 | included | `ca2af791b6f68d06aa70f47a680607e5d3a9e6da468134f6dad0d9a908dd487a` |
| C1-N1-014-pairB-from007 | sector_table.json | 13405 | included | `b1f237688d61cf98fb4f07ea9bddaf9beaa7c18fa8a443a86192a3a9ec74d0b7` |
| C1-N1-015-pairQ-quot013 | MANIFEST.json | 5268 | included | `e7dc4a09af97d3b9f449031baa697ac79acd3ade73379c7033d99a4edb2a466e` |
| C1-N1-015-pairQ-quot013 | quot013_pairQ_cpu_m16_diag2.json | 14279 | included | `4781ce0bfa2baa3a42ce388e4c98c79d7426ec8457592ccb677d4fbcad95d9ba` |
| C1-N1-015-pairQ-quot013 | quot013_pairQ_cpu_m16_exact.json | 2801333 | not included | `d7759bbaa98fb5d686c8f88af4ec6b9ddd96e457acc2d9166924c5c729ee8eae` |
| C1-N1-015-pairQ-quot013 | quot013_pairQ_cpu_m16_weaktests2.json | 13196 | included | `727b3573c410f3e0ae201e6412fe54b513ea941201c27fca0647108dfb3727e0` |
| C1-N1-015-pairQ-quot013 | sector_table.json | 13415 | included | `5032fb0ebbb30a21dd7c7ede287b15226bde387e56c86b10bb3a20579c2a5fd6` |
| C1-N1-016-legqs25-quot013 | MANIFEST.json | 5411 | included | `64872cff3b23ba9e068411527648de3a4b335a7f9737b3a99f12efc186925d21` |
| C1-N1-016-legqs25-quot013 | quot013_legqs25_m9to15_cpu_m16_diag2.json | 14293 | included | `11c980a7415aafde53c020cc682fa75025ce76f4c8ada21ebb5136d3a84107e6` |
| C1-N1-016-legqs25-quot013 | quot013_legqs25_m9to15_cpu_m16_exact.json | 2835333 | included | `a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42` |
| C1-N1-016-legqs25-quot013 | quot013_legqs25_m9to15_cpu_m16_weaktests2.json | 13213 | included | `4f55bf3ca194c24b254ccb3d76962263e93daf43163264fc2b36a5015cf535ad` |
| C1-N1-016-legqs25-quot013 | sector_table.json | 13403 | included | `c8241fef3410dbca2322d15264a386fcfc26c1b5922621b93a08c9495000dde8` |
| C1-N1-017-legqs50-quot013 | MANIFEST.json | 5253 | included | `a1e6695c0b2872d25b81b12b23d1ed6e8b95d1f6eafd97f4b83ac72ccc2391c6` |
| C1-N1-017-legqs50-quot013 | quot013_legqs50_m9to15_cpu_m16_diag2.json | 14277 | included | `5fdfd97afe148cf9690abaecc18cb6e2378aae262eca2788b1dbef088560e0d7` |
| C1-N1-017-legqs50-quot013 | quot013_legqs50_m9to15_cpu_m16_exact.json | 2835543 | not included | `7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114` |
| C1-N1-017-legqs50-quot013 | quot013_legqs50_m9to15_cpu_m16_weaktests2.json | 13214 | included | `df8b95ba98d2d0284ed8673ffb2dfafa25ea82ff29695c6d768662076c7236fc` |
| C1-N1-017-legqs50-quot013 | sector_table.json | 13412 | included | `4dda865d23c0da62b1943d4e32634c15d72a39be87227f2d3395c8848d2255f1` |
| C1-N1-018-legqs25-cont12 | MANIFEST.json | 5148 | included | `b5c56ceb00dc7596aada3ac457cf24200b0545d7b627f840fb6bceba95cb7f5e` |
| C1-N1-018-legqs25-cont12 | quot013_legqs25_cont12_cpu_m16_diag2.json | 14298 | included | `07168f39d526d1c337e3b219263127bc3e3f66d925a992f22c21196a1ae8895d` |
| C1-N1-018-legqs25-cont12 | quot013_legqs25_cont12_cpu_m16_exact.json | 2835166 | not included | `1c99bf4d77865f7c576a9ba6c08bc08cf008416a737d4a8626b5799ceb4a85e2` |
| C1-N1-018-legqs25-cont12 | quot013_legqs25_cont12_cpu_m16_weaktests2.json | 13195 | included | `8e8fc20138712aa4c1d0bd0849baa477ba535d7796f07b246dc45b61ac715e5d` |
| C1-N1-018-legqs25-cont12 | sector_table.json | 13416 | included | `29c0e10270237e35ceea9c0215e88a5d2f8bae17f9c62210c9febfeabeb7adc8` |
| C1-N1-019-legqs50-cont12 | MANIFEST.json | 5145 | included | `9804b7edc19ba01fc47b2287a622e3b2001f38ff5f1afbbfe47aa3c02e905790` |
| C1-N1-019-legqs50-cont12 | quot013_legqs50_cont12_cpu_m16_diag2.json | 14288 | included | `e7d023056f4bc0685b8e7e77c6ebae00d9f1618d5797792f1933547b6fdfe626` |
| C1-N1-019-legqs50-cont12 | quot013_legqs50_cont12_cpu_m16_exact.json | 2835534 | not included | `ca0fffafe2aa7ea3c6049e0b5a83651113451087027b0783800c046ae170d419` |
| C1-N1-019-legqs50-cont12 | quot013_legqs50_cont12_cpu_m16_weaktests2.json | 13191 | included | `67f74599850ac54c8c93f087d0cc61681bea263972986752c92804fd3a87a5ce` |
| C1-N1-019-legqs50-cont12 | sector_table.json | 13403 | included | `e8017691c88312ff9383452a3cae595ee0506347baa39a47973a3737cae3f2d2` |
| C1-N1-020-legqs25p50-quot013 | MANIFEST.json | 5208 | included | `4fcedd739bb6846f59157298f57017aa5abc8b13a5234e7635d8b646b665f140` |
| C1-N1-020-legqs25p50-quot013 | quot013_legqs25p50_m9to15_cpu_m16_diag2.json | 14284 | included | `ac9e916498f508007d01dc0a67b1616b7ad405f2db7e08ea4970e1a450721b24` |
| C1-N1-020-legqs25p50-quot013 | quot013_legqs25p50_m9to15_cpu_m16_exact.json | 2870608 | not included | `bddbd3120852a815cfe850635564cb09ab52a98ec596a4cce3b72c98cf04f7cf` |
| C1-N1-020-legqs25p50-quot013 | quot013_legqs25p50_m9to15_cpu_m16_weaktests2.json | 13217 | included | `1f56cc04517bbe283b121bb78a7fe6ac437b67c60856b2ba849c4b53add69fb2` |
| C1-N1-020-legqs25p50-quot013 | sector_table.json | 13408 | included | `acc598370eb89e1bce2ff025fb6db1cce17c6b7435bbbc29af358c0ba15942cd` |
| C1-N1-021-heldin14-legqs25p50 | MANIFEST.json | 5506 | included | `0e3ea89f0c0050883f3808895a36df18c611577e21d7916e9ebf62702d384307` |
| C1-N1-021-heldin14-legqs25p50 | legqs25p50_heldin14_gpu_m16_diag2.json | 14279 | included | `afb2dda5787d22a71ff4f9a9fe053613c15b664db9d1f72ec7408f82fdfa5b67` |
| C1-N1-021-heldin14-legqs25p50 | legqs25p50_heldin14_gpu_m16_exact.json | 2871223 | included as legqs25p50_heldin14_gpu_m16_exact.json.gz | `c6ed292b9f7129ad236f8441140745ec6accc3918d477ca2268e55bf7efc85c8` |
| C1-N1-021-heldin14-legqs25p50 | legqs25p50_heldin14_gpu_m16_weaktests2.json | 13194 | included | `7bbc9dfc7d0a9d7b033df452de37216bd83713b599e37cc57c14c2918cf1cf9d` |
| C1-N1-021-heldin14-legqs25p50 | sector_table.json | 13414 | included | `c6456e56cfde2649032ef3f71db0f64142f5b03696b798e6cd2a02f5f8e513b4` |
| C1-N1-022-legqs25-m16to23 | MANIFEST.json | 5570 | included | `14deff3eb17f789e3eb27f578f24e170bf420390eedc863e22bc9970359473a3` |
| C1-N1-022-legqs25-m16to23 | legqs25_m16to23_gpu_m16_diag2.json | 14280 | included | `c37895400b89df253bb76a52234276058938ac39436bc432a08daa6c25a9b1a4` |
| C1-N1-022-legqs25-m16to23 | legqs25_m16to23_gpu_m16_exact.json | 2868980 | included as legqs25_m16to23_gpu_m16_exact.json.gz | `85c7e4e2c060f1124f2f1d77a2b7f07cd67b32849bd849c1e0a2ec8aa85ce75f` |
| C1-N1-022-legqs25-m16to23 | legqs25_m16to23_gpu_m16_weaktests2.json | 13205 | included | `fa7bc63264e0efc14e2bc48d86b32501b54424eec97885d10017c53475d318cc` |
| C1-N1-022-legqs25-m16to23 | sector_table.json | 13405 | included | `dfa992ba26504a20002348517837aed704621ea2a83356006aba0f3ed9bd440b` |
| C1-N1-023-legqs25p100-quot013 | MANIFEST.json | 5454 | included | `c97c63747b29e1520c80d9ab799ab451f2ea13b3d3c437ed5e0809c3d7f8c4dc` |
| C1-N1-023-legqs25p100-quot013 | legqs25p100_m9to15_gpu_m16_diag2.json | 14289 | included | `ee8e2a52e4bfc24b73ca691155586b004649cdf9c08df6638472ce11d67ce16b` |
| C1-N1-023-legqs25p100-quot013 | legqs25p100_m9to15_gpu_m16_exact.json | 2870789 | not included | `d67bdd9ff05917736e686af5f834a2e12afede891098ccf8f9de8a6e2d7a71df` |
| C1-N1-023-legqs25p100-quot013 | legqs25p100_m9to15_gpu_m16_weaktests2.json | 13203 | included | `f9dc7739d5c55396c5be3f327260887503e09d57766c5302f41bc3423d4fedc5` |
| C1-N1-023-legqs25p100-quot013 | sector_table.json | 13407 | included | `41c8576c6d4ea45d9ddc42d0ae9dd52417172ad93e80bbb8be820cfc47cee7fe` |
| C1-N1-024-rulem32-legqs25 | MANIFEST.json | 5497 | included | `5faa874f48cbdfcc256b350057c8d31c0328314497544ab690ec76a748d79212` |
| C1-N1-024-rulem32-legqs25 | quot013_legqs25_m9to15_gpu_m32_diag2.json | 14281 | included | `93f6717452dfb7c6a0a1a69a700bcbdda2642858c7f7b092513d6a6e6aed0ed3` |
| C1-N1-024-rulem32-legqs25 | quot013_legqs25_m9to15_gpu_m32_exact.json | 2835550 | not included | `3472badc9c6b49b8d1d244b0eb3c7569706d541a0ab3df56e0284ca70a35307d` |
| C1-N1-024-rulem32-legqs25 | quot013_legqs25_m9to15_gpu_m32_weaktests2.json | 13195 | included | `96662ed7c29aaf210fdf60548e925ca7d6e1617200564bc46e63444d314503fb` |
| C1-N1-024-rulem32-legqs25 | sector_table.json | 13407 | included | `95d55f520873a33046fe038ef58e4682a4553efc202ac6e9a99c6e04a5cff1ec` |
| C1-N1-025-combined-heldin1e16 | MANIFEST.json | 5711 | included | `c36e44773c1569557dc7084626531122c74d6a56e43b6e2d3030ea40da191732` |
| C1-N1-025-combined-heldin1e16 | combined_s25s50s100_m16to23_heldin14_gpu_m16_diag2.json | 14310 | included | `67890264f808e3ddbc4b67f85af2123925ed82d3b302f70bc4d861495a55fec5` |
| C1-N1-025-combined-heldin1e16 | combined_s25s50s100_m16to23_heldin14_gpu_m16_exact.json | 2940696 | not included | `3b1c9f7199b56fc892815eefac8696e811a72d729ead5b955491e20961221f17` |
| C1-N1-025-combined-heldin1e16 | combined_s25s50s100_m16to23_heldin14_gpu_m16_weaktests2.json | 13212 | included | `128f457ef1a0353d9c4f6173175a4471273862fbdeb4024e3be9e56989f7b4fb` |
| C1-N1-025-combined-heldin1e16 | sector_table.json | 13409 | included | `2fcfba7c49197b168f495723949aa11bf3c679514b395c0c35bcebf4414fc8df` |
| C1-N1-026-heldin1e16-legqs25-m16to23 | MANIFEST.json | 8214 | included | `2d6c6e984ba9e004774e7eaa23f35c298630acbe77699e7d3e3f221790b4d170` |
| C1-N1-026-heldin1e16-legqs25-m16to23 | legqs25_m16to23_heldin1e16_gpu_m16_diag2.json | 14284 | included | `90e2341c571d0a6dc1a0f1be178e40c1b0754e9358510f5a1e7631d191b831cf` |
| C1-N1-026-heldin1e16-legqs25-m16to23 | legqs25_m16to23_heldin1e16_gpu_m16_exact.json | 2869349 | not included | `2978faab0e8b4a1da1ec06991ebaf03eb9bfa7ed388b0dbbae9d955ca3a095f3` |
| C1-N1-026-heldin1e16-legqs25-m16to23 | legqs25_m16to23_heldin1e16_gpu_m16_weaktests2.json | 13205 | included | `625650bade172138eb39b4c29d07d08e04f9238a3e4ae2a3aa19a5fc30820cfd` |
| C1-N1-026-heldin1e16-legqs25-m16to23 | sector_table.json | 13406 | included | `dbc580c6e96d56107d6c9062af4f20c5e37582dcc3d0b62ef11b676fb9ba6f23` |
| C1-N1-027-cont60-legqs25-m16to23 | MANIFEST.json | 6786 | included | `1b13ea7ecc9f14a30363999073c7be061af596db80bf435e281eca87db19fdc8` |
| C1-N1-027-cont60-legqs25-m16to23 | legqs25_m16to23_cont60_gpu_m16_diag2.json | 14304 | included | `f5e8674cb929ab743f55ffe9abb1d5d42f074e435bcafe52285a79542055cfbc` |
| C1-N1-027-cont60-legqs25-m16to23 | legqs25_m16to23_cont60_gpu_m16_exact.json | 2868943 | not included | `a3bd6a5152716b05baf2c377c9bb253e73e20024515558632349119157624b40` |
| C1-N1-027-cont60-legqs25-m16to23 | legqs25_m16to23_cont60_gpu_m16_weaktests2.json | 13196 | included | `ea8e2bbaf1b4c2ee5d08cdeae546b6a682103091a494353e607299a0b5baf48a` |
| C1-N1-027-cont60-legqs25-m16to23 | sector_table.json | 13412 | included | `a72b20d23d17bfdb6a4f86d22cb512b361426be4aca8f708b06ba81ae930ae5f` |
| C1-N1-028-legqs25-nin24 | MANIFEST.json | 6325 | included | `1aa4d4e83d0794d6fe6c9a94a9223b3ce2f8e297075ecc0735d03dc44e2ae2d9` |
| C1-N1-028-legqs25-nin24 | legqs25_nin24_m9to15_gpu_m16_diag2.json | 14302 | included | `2ab9ec4a7b5ad334015a7e40d540934586be5fc577a9d9a67a9fd1cac10b42ad` |
| C1-N1-028-legqs25-nin24 | legqs25_nin24_m9to15_gpu_m16_exact.json | 2904513 | not included | `70afa847663c4ba0c6af4023800c1529171506cbd94ec0e0df542e24ae3206f2` |
| C1-N1-028-legqs25-nin24 | legqs25_nin24_m9to15_gpu_m16_weaktests2.json | 13206 | included | `c30848c4a2e2e92c1520318c2f9b828b75b352ed78cad4f6fdf41a9ec5eba648` |
| C1-N1-028-legqs25-nin24 | sector_table.json | 13406 | included | `bc5cef9d388810a4af3e8046be6ea7e984c8455868b458fc7d37b7494ac72399` |
