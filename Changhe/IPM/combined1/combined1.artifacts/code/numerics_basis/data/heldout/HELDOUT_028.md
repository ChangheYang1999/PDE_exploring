# HELD-OUT set for C1-N1-028 (tag legqs25_nin24_m9to15_gpu_m16). Written 2026-10-29T12:51:53Z, BEFORE launch.
Start: candD2/legqs25_m16to23_gpu_m16_exact.json (= C1-N1-022, 2414 generators) + legqs R0 = 25 functions n = 12..23 (IPM_ADD_LEGQS=1,2,3:9:15:25:24; the existing n = 0..11 are skipped)
in j = 1..3, m = 9..15: 252 more radial functions at the one scale that moved the registered probes (016) -> 2666 generators. 60 GN steps, MID 16, GPU.
Objective rows (67, weight 1e12; no held-in rows): the 27 first-mode k in {0..8,12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096} and the 40 N4-160 probes
n <= 17 at K = (n-1)/2 + {0,8,32,128,512}.
HELD OUT (never rows), probe phi_(n,K) = r v^2 t^K sin(n theta):
- the 25 registered probes (public register): 19:600 19:900 19:1200 19:1800 19:2400 23:600 23:900 23:1200 23:1800 23:2400 25:600 25:900 25:1200 25:1800 25:2400 29:600 29:900 29:1200 29:1800 29:2400 31:600 31:900 31:1200 31:1800 31:2400 
- the N4-160 probes n = 19..31 odd at K = (n-1)/2 + {0,8,32,128,512}: 19:9 19:17 19:41 19:137 19:521 21:10 21:18 21:42 21:138 21:522 23:11 23:19 23:43 23:139 23:523 25:12 25:20 25:44 25:140 25:524 27:13 27:21 27:45 27:141 27:525 29:14 29:22 29:46 29:142 29:526 31:15 31:23 31:47 31:143 31:527 
Purpose: does more radial resolution at scale 25 in the blocks m = 9..15 move the registered probes at r 35 to 50 (the only lever that moved them so far)? Judged against 022 and 027.
