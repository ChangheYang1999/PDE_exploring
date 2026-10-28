# Results of the uniform comparison (second pass)

Produced by `combine.py` from the node certificates listed below. Every number is the exponential of the upper
endpoint of an Arb ball (200 bits); decimals are rounded up in the last place shown.

## Main result: $U$ = Theorem 3.5 (exterior circles)

- uniform C: log ratio $\le$ `[0.079687236027825129669 +/- 1.88e-23]`, ratio $\le$ 1.0829483075, worst segment near $\alpha=0.6625$ (group 4).
- uniform D: log ratio $\le$ `[0.25452985464421727701 +/- 1.76e-21]`, ratio $\le$ 1.2898550590, worst segment near $\alpha=0.5875$ (group 3).

| group | shape | worst C ratio | at | worst D ratio | at |
|---|---|---|---|---|---|
| 0 | 14/25 | 1.027583 | 147/800 in [33/200, 19/100] | 1.134369 | 19/100 in [33/200, 19/100] |
| 1 | 53/100 | 1.050781 | 7/20 in [13/40, 7/20] | 1.224130 | 7/20 in [13/40, 7/20] |
| 2 | 97/200 | 1.072006 | 1/2 in [19/40, 1/2] | 1.278143 | 1/2 in [19/40, 1/2] |
| 3 | 89/200 | 1.080758 | 19/32 in [23/40, 3/5] | 1.289855 | 47/80 in [23/40, 3/5] |
| 4 | 39/100 | 1.082948 | 53/80 in [13/20, 27/40] | 1.289697 | 97/160 in [3/5, 5/8] |
| 5 | 33/100 | 1.081882 | 113/160 in [7/10, 29/40] | 1.272894 | 7/10 in [7/10, 29/40] |
| 6 | 53/200 | 1.071908 | 129/160 in [4/5, 33/40] | 1.224554 | 4/5 in [4/5, 33/40] |
| 7 | 1/5 | 1.048371 | 723/800 in [9/10, 183/200] | 1.137995 | 723/800 in [9/10, 183/200] |

## Cross-check: $U$ = Theorem 3.4 (reflection orbits)

- uniform C: log ratio $\le$ `[0.10831062755022917383 +/- 4.33e-21]`, ratio $\le$ 1.1143938531, worst segment near $\alpha=0.6125$ (group 4).
- uniform D: log ratio $\le$ `[0.28037296782478137694 +/- 1.25e-21]`, ratio $\le$ 1.3236233893, worst segment near $\alpha=0.5875$ (group 3).

## Consequence on the whole interval

With Theorem 9.1 of the report ($F/L_1\le1.0172482934$ on $(0,0.005]$, $F/H\le1.0262309397$ on $[0.995,1)$) and the
endpoint extension for $D$ in `PROOF.md`, section 5 ($D/L_1\le1.0213$ on $(0,0.005]$, $D/H\le1.0324$ on $[0.995,1)$):

$$\sup_{0<\alpha<1}\frac{\text{certified upper bound for }C_\alpha}{\text{certified lower bound for }C_\alpha}\le1.0830,\qquad
\sup_{0<\alpha<1}\frac{\text{certified upper bound for }D_\alpha}{\text{certified lower bound for }D_\alpha}\le1.2899.$$

The middle interval decides both constants. The interpolation loss (segment bound against the larger nodal ratio) is
about $0.17\%$ at the worst segment.

## Commands

```
python3 nodes2.py
bash run2.sh            # upper_n384_b.json, lower2_g0..7.json, far2_g0..7.json (upper_n384.json from the first pass)
python3 combine.py thm35 --nodes nodes2.json --upper upper_n384.json,upper_n384_b.json --lower lower2_g --far far2_g --tag _pass2
python3 combine.py thm34 --nodes nodes2.json --upper upper_n384.json,upper_n384_b.json --lower lower2_g --tag _pass2
```

Validation runs: `refl_check128.json` (the 128-cell reflection certificate reproduced at the ten exponents of
Table 1) and `far_check_coarse.json` (the coarse exterior certificate reproduced with reference exponent $\frac12$).

## SHA-256

| file | sha256 |
|---|---|
| `PROOF.md` | `ad6a77fa6f098fe50e445824ec0e396585d51b40558614f22a34a36b4e07f71e` |
| `nodes2.py` | `a4f5c493e82c67eb2bd6140789cab615668cd428a3f3029fdfa02a4dfa2d0fbd` |
| `nodes2.json` | `ddc797eedf0bbf64ab6cc81453dc5de2f79d5b45720233beefbcef3d36d28cc4` |
| `refl_nodes.py` | `d706104154548afc36a4cc3b07ed758846caa0c93e579a8573027fbffcce9298` |
| `far_nodes.py` | `af23dab44880711fdae64d81f0b2d0a208c27deccec9f5cc9ef481ee326b4db6` |
| `certify_structured_full.py` | `1d683844422a3bd7206af69954fb796079a99f06da7030832d47f4c702370fb7` |
| `circle_transport_plan.py` | `b61a003cd05e990c64fcb00b82275e54cf0c53acbe1baba2faaa6428150db82f` |
| `combine.py` | `e9efa2fec3b9d689a059df03b386c1850e7c09c2d6a4bcf6089de1b254be8d3d` |
| `upper_n384.json` | `92ea18a45ff3f8c948a11917b5d9849a2f54b68e2fecc56875c5d9836765db1a` |
| `upper_n384_b.json` | `edb4ae5afa493420f3ee2fb645e1bbde3bf58a112f93f85df0db6006b24ee16b` |
| `lower2_g0.json` | `9d0e7ba9c193c296075407f7d37bb68426dbe6e49f70831938c0078d5c0e14a8` |
| `lower2_g1.json` | `2d159422b3a5a62a5845cdbbeebf3de5a0097550fb3fe957ca6f8b7a843cea51` |
| `lower2_g2.json` | `bb4d79ba59489e2517a2813e1644334284bb35cea864c75657fdf7012f6b6a47` |
| `lower2_g3.json` | `16995790b33729a499ba8542001bb6e0fdb440c455b647ad73ce10851bff0e9a` |
| `lower2_g4.json` | `a76412c744361d05b39358ed26237bcab4ecdb7c4c8e2c57d457d1a3bcca43e8` |
| `lower2_g5.json` | `10fc76ac9199553a65a13399183cafa5f80c35042fe292c1ffefced9744aa021` |
| `lower2_g6.json` | `5914fd88f34e3c15911f569a27b3bd6c5b48924777cd7dfb6822bf6bfebf9184` |
| `lower2_g7.json` | `25d517ca453cdaac0a182666220ec868f75db9533dde56f55b179728fdb56a17` |
| `far2_g0.json` | `1043faa3b3ee3bf65a6c080eada67974e8d5c514281dcb18ba8a46ab3f031906` |
| `far2_g1.json` | `667673b5880162596fcb45df5546fc6908bc91bfce9254eddcdb893806ce83b1` |
| `far2_g2.json` | `788cf1f7b8caf37c0a7fa527d0f65f401331a34a0c8509c338da58e5ab64ffce` |
| `far2_g3.json` | `987d73f57d5ecc4f1efc1356b976c62a11bbc4e36130a43f36aef0e88ea85337` |
| `far2_g4.json` | `ca81a469239a59142df58d9ac3d079a92f8395e3b26a4d7066ce910365cffc7e` |
| `far2_g5.json` | `e80bc05d5ad82ae888153d0493360cd007400fd955303e9680ac0a01cc57e798` |
| `far2_g6.json` | `827152cb5a824d77efd7ad6bc9a656af8ef2fb787ed142583f0ff60c679c39b0` |
| `far2_g7.json` | `662a507628875d8f6dcf7437b9752b44c46190ad163628f5e9b9e326f0ad7990` |
| `uniform_result_thm35_pass2.json` | `0450ad952065d81a5ca96b84b492f80577cd362b5d91a91b347601218450cb89` |
| `uniform_result_thm34_pass2.json` | `f6256bde7b08e4feee7815a5b8a60ac7e08f0188c22f712d37b78cf71e4850c6` |
| `refl_check128.json` | `bb53a36f7ff8bf117bd5e1c4a698594972939bb7c51f07e30f4cc24ff8b851f4` |
| `far_check_coarse.json` | `1e77c217c80c99bc6ff39ff663edb448baba2f9b67b330342567a885c3c7a369` |
