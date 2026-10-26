# dev_policy_assess8.json

Created 2026-10-24T13:21Z on the lead's ruling (c4-lead NOTES 13:19Z item 3). Identical to outputs/dev_policy_assess.json except
max_family_rss_mib 40960 -> 163840 (the g2_policy_v3 value). Reason: item F (the development assessment of the seed from the
frozen layout) runs at 8 fork workers, the production worker count; the guard sums the copy-on-write pages of every forked child,
so the family RSS sum overstates real use and can exceed 40 GiB. Every other limit is unchanged (max_seconds 14400, PSI 5,
min_available 16 GiB and 10%, disk 10 GiB, swap, pageout, load). The old file is not edited. The guard rejects unknown keys, so
this note lives beside the policy file. Development use only; item F is not evidence.
