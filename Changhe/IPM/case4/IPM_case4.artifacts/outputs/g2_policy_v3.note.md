# g2_policy_v3.json

g2_policy_v3 (08:12Z): identical to g2_policy_v2 except max_family_rss_mib 40960 -> 163840. Reason: g2_v4 t3 was terminated at 08:07:48Z by the process-family RSS ceiling at 68,070 MiB; t3 holds the handoff 181D V3 model and the longdouble Model860 (about 17.5 GiB) at once and its fork pools (4 workers) make the guard count the copy-on-write pages of every child again, so the family RSS sum overstates the real use. The box has 1.1 TiB with about 940 GiB available; every other limit (min_available 16 GiB and 10%, PSI 60, disk 10 GiB, swap, pageout, load) is unchanged.

The guard rejects unknown keys, so this note lives beside the policy file.
