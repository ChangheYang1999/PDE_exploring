# HELD-OUT set for C1-N1-025 (tag combined_s25s50s100_m16to23_heldin14_gpu_m16). Written 2026-10-29T09:13:13Z, BEFORE launch.
Objective rows (81): the 27 first-mode k in {0..8,12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096}; the 40 N4-160 probes n <= 17 at K = (n-1)/2 + {0,8,32,128,512};
and 14 HELD-IN mid-field rows: n = 19..31 odd at K = (n-1)/2 + 128 and K = (n-1)/2 + 512 (19:137 21:138 23:139 25:140 27:141 29:142 31:143 19:521 21:522 23:523 25:524 27:525 29:526 31:527).
HELD OUT (never rows):
- the 25 registered probes (public register): 19:600 19:900 19:1200 19:1800 19:2400 23:600 23:900 23:1200 23:1800 23:2400 25:600 25:900 25:1200 25:1800 25:2400 29:600 29:900 29:1200 29:1800 29:2400 31:600 31:900 31:1200 31:1800 31:2400 
- the N4-160 probes n = 19..31 odd at K = (n-1)/2 + {0,8,32}: 19:9 19:17 19:41 21:10 21:18 21:42 23:11 23:19 23:43 25:12 25:20 25:44 27:13 27:21 27:45 29:14 29:22 29:46 31:15 31:23 31:47 
Start: candD2/quot013_legqs25_m9to15_cpu_m16_exact.json (016) + IPM_ADD_LEGQS="1,2,3:9:15:50:12;1,2,3:9:15:100:12;1,2,3:16:23:25:12" (2918 generators); 60 GN steps; MID 16.
Addendum 2026-10-29T09:41:40Z (before launch): the 14 held-in rows carry weight 1e16 (IPM_NHELDIN=14 IPM_WPAIR_HELDIN=1e16); the 67 other rows keep 1e12. Reason: in 021 the same rows at 1e12 were inert (row pairings I about 5e-6 cost 25 each against an objective of 1.3e7). The held-out set is unchanged.
