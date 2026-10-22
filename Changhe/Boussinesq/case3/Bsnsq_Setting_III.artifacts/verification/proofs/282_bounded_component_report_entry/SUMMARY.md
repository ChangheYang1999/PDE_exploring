# P282: complete bounded-component report entry

Published 2026-10-22T05:36:10.889400+00:00. Verdict: **CONFIRMED with the two exact wording corrections** in verification/required_wording_replacements.json. First pass **223/223** independent controls, 2.277945963s, 2026-10-22T05:35:31.473337+00:00 to 2026-10-22T05:35:33.751287+00:00. Audit interval05:32to05:35. No harness failures occurred.

The first correction removes the false claim that all inner forcing is zero: (V0) is forced by2a1=A!=0, while the prescribed constant coefficients solve it. The second states precisely that both PDE hold near0 and to all axis orders, and that the thermal PDE fails globally. The unchanged proof establishes the field construction, every axis coefficient, compact whole-plane inverse, the specified center drift, J=(-3,3), and A I2 tending to negative infinity at both finite ends. It establishes no B2 profile.

The complete normalized preview was independently reconstructed from all six Z-sections, its17new paragraphs, five unique replacements, table row and all155timeline entries, preserving each of the154original entries. The driver was read but never run or imported. Independent Cartesian coefficient controls reached T5,V4 and curl4. The endpoint polynomial remainder, local exact PDE, factorials, mass identity, all25input hashes and supporting counts were checked. Finite symbolic tests supplement the complete proof.

Approved text SHA256 ad3ece275e2ba0df6739f9542cf3784b9b6011671c8fbb7b38db43c15f09e6ff; approved preview SHA256 3584915412e7a10fe110d628c4d526af922d9b433d148c67b2de27c7032a6a70. The four precise substitution strings are in verification/approved_placeholders.json. Actual adoption requires a fresh comparison. Base report68a71421 / SPEC77.

P278's actual Opus487-490 reviews, all returning claude-opus-5-5, were already independently adjudicated and are frozen here. A161/A162 are separate referee reviews; their availability limitations are preserved. A161's36checks are its reported artifact, not executed by this lane. P283's proposed global thermal improvement is separately under review and is not assumed here. General B2 remains OPEN.
