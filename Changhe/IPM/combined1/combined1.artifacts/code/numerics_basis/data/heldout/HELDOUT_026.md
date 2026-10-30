# HELD-OUT set for C1-N1-026 (tag legqs25_m16to23_heldin1e16_gpu_m16). Written 2026-10-29T11:31:32Z, BEFORE launch.
Start: candD2/legqs25_m16to23_gpu_m16_exact.json (= C1-N1-022, 2414 generators; no new functions). 60 GN steps, MID 16.
Objective rows (81): the 27 first-mode k in {0..8,12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096} and the 40 N4-160 probes n <= 17 at K = (n-1)/2 + {0,8,32,128,512}
(weight 1e12); plus 14 HELD-IN mid-field rows n = 19..31 odd at K = (n-1)/2 + 128 and + 512 (19:137 21:138 23:139 25:140 27:141 29:142 31:143 19:521 21:522 23:523 25:524 27:525 29:526 31:527)
at weight 1e16 (IPM_NHELDIN=14 IPM_WPAIR_HELDIN=1e16).
HELD OUT (never rows), probe phi_(n,K) = r v^2 t^K sin(n theta):
- the 25 registered probes (public register): 19:600 19:900 19:1200 19:1800 19:2400 23:600 23:900 23:1200 23:1800 23:2400 25:600 25:900 25:1200 25:1800 25:2400 29:600 29:900 29:1200 29:1800 29:2400 31:600 31:900 31:1200 31:1800 31:2400 
- the N4-160 probes n = 19..31 odd at K = (n-1)/2 + {0,8,32}: 19:9 19:17 19:41 21:10 21:18 21:42 23:11 23:19 23:43 25:12 25:20 25:44 27:13 27:21 27:45 29:14 29:22 29:46 31:15 31:23 31:47 
Purpose: the best-G0 basis (022) with active mid-field rows; judged on the 25 registered probes against 022 and 016.
