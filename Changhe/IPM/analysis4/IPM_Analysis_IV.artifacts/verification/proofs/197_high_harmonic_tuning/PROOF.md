# High-harmonic profiles and vanishing tuning responses at delta = 4/9

Status: sin13 obstruction at36 PROVED inV455 and sin15 obstruction at45 PROVED inV520 after independent polar reproductions. The sin15 reproduction uses modular arithmetic with every inverse checked.

## Statement and hypotheses

Work at delta = 4/9, c = 9/5, with f_1(theta) = sin(M theta), where M is an odd positive integer. Use the pure density/stream exponent lattice p_n = 1 - 4n/9, P_n = p_n + 1, S1 density symmetry and S2 stream symmetry. At the resonant order n = 9k the free stream coefficient is H_(9k) sin((4k-2)theta). Let sigma_k be the coefficient of sin((4k+1)theta) in the change of f_(9k+9) per unit change of H_(9k), keeping all earlier free coefficients fixed.

If M >= 11, the first compatibility condition at order9 holds automatically. If M >= 13, sigma_k = 0 whenever 8k-1 > 9M+8. More precisely, sigma_k can be nonzero only if either 3 or 8k-1 lies in the finite set

    S_M = {Ms+t : s in {-9,-7,-5,-3,-1,1,3,5,7,9},
                    t in {-8,-6,-4,-2,0,2,4,6,8}}.

For M=13 this support condition already forces sigma_3=0 and forces sigma_k=0 for every k>=16. These response zeros alone do not prove an obstruction: the constant part of the corresponding compatibility equation might also vanish. The finite continuation below is intended to distinguish these possibilities.

## Low-order support

Before the first stream resonance, the density f_r has frequencies in

    A_r = {Ms+t : |s|<=r, s=r mod2, |t|<=r-1, t=r-1 mod2}.

The stream g_r has frequencies in the same set with |t|<=r and t=r mod2. This follows by induction. It holds for f_1. The Poisson right side shifts a density frequency by plus or minus1; inversion preserves the shifted frequency. The polar bilinear expression P_i g_i f_j' - p_j g_i' f_j adds signed frequencies, so the bounds for g_i and f_j give the asserted density bound at r=i+j. Derivatives multiply coefficients and do not change the polar frequency. Some frequencies in the stated sets can cancel, which only makes the support smaller.

At r=9 the possible density frequencies have s odd and |t|<=8. If M>=11, none is1 or -1, since |Ms+t|>=M-8>=3. The first obstruction is exactly the frequency1 density coefficient, so it is zero. This proves first compatibility, without choosing H_9.

## Support of the affine response

Let q=4k-2 and set the stream perturbation at order9k equal to sin(q theta). A density perturbation at order9k+r, 1<=r<=9, has frequencies in

    {epsilon q + Ms+t : epsilon in {-1,1},
       |s|<=r, s=r mod2, |t|<=r-1, t=r-1 mod2}.

Its intermediate stream perturbation has the same bound with |t|<=r and t=r mod2. Induct on r in the exact affine-response recurrence. The direct term multiplies the initial stream perturbation by f_r. The remaining terms multiply one intermediate perturbation by an unperturbed low-order factor. The frequency sets add and give the stated bounds. The intermediate Poisson inverse shifts by at most1. It does not add free frequencies because there is no intermediate resonance.

The response is exactly affine through order9k+9. Two factors depending on H_(9k) would first contribute at order9k+(9k+1)>9k+9, including at k=1. Thus this frequency calculation covers the full response, independent of earlier chosen harmonics.

At r=9 the target frequency is q+3=4k+1. A contribution from epsilon=1 requires Ms+t=3. A contribution from epsilon=-1 requires Ms+t=2q+3=8k-1. This proves the finite-set criterion. If M>=13 then |Ms+t|>=M-8>=5, excluding3. Also |Ms+t|<=9M+8, which proves eventual vanishing. For M=13,k=3, the target offset23 has distance10 from13 and16 from39, exceeding8, and has greater distance from every other odd multiple of13. Hence sigma_3=0.

## Finite continuation criterion

At each completed resonant order9k, compute the next obstruction with H_(9k)=0, calling it R_k. Exact affineness gives the next compatibility equation R_k+sigma_k H_(9k)=0. If sigma_k is nonzero the unique solution is H_(9k)=-R_k/sigma_k. If sigma_k=0 and R_k is nonzero, no choice of that harmonic can pass the next resonance. If every preceding response was nonzero, the earlier harmonics were already uniquely fixed, so this is an obstruction to every pure density/stream series with the stated leading profile and symmetry. It says nothing about logarithmic or additional exponent channels.

The independent Cartesian implementation computes each provisional block, its response, and its corrected block in exact rational arithmetic. It verifies the Poisson identities and the affine coefficient identity, and recomputes the corrected block directly rather than relying on a zero-containing interval. It compares the first slope and tuned amplitude to the independently retained evidence in topic36.

## Dependencies and scope

The Cartesian derivative identities, signs, density recurrence and Poisson equation were established in topic01. The low-order engine is the exact Laurent implementation from topics21 and24. Affine block tuning and the distinction between a free stream harmonic and a pure potential were established in topics36 and131. A pure density/stream obstruction also rules out the more restrictive pure-potential ansatz. The support theorem alone is a limitation of the nonzero-response tuning method, not an all-order incompatibility theorem. Any finite incompatibility must be supported by the separately retained exact nonzero R_k.

## Exact sin13 continuation, V403

For f1=sin(13theta), delta=4/9, exact Cartesian calculations give unique nonzero-response corrections at H9 and H18. The first correction agrees exactly with V043. Eighteen complete affine coefficient identities pass, and all 51 computed particular Poisson identities pass. At the third tuning step sigma3=0 exactly, while R3 is strictly between0.03095 and0.03096. Its full rational numerator and denominator are retained in sin13_block3.json. Runtime 112.31008579581976 seconds; 945 ordered products. The support argument separately predicts the vanishing response.

The obstruction is a positive exact rational. Since sigma1 and sigma2 are nonzero, H9 and H18 have no remaining freedom. At order36 the compatibility equation is R3+0*H27=0 with R3>0, which is impossible. This proves the claimed pure-series obstruction, conditional only on the independently recorded exact arithmetic and the support/affineness derivation. Independent team review is pending.

## Nonzero amplitude scaling

Every stated obstruction for leading sin(M theta) also applies to a sin(M theta) for each real a different from zero. Indeed, if a pure series with this leading coefficient existed, dividing every density and stream coefficient of order n by a^n would give a pure series with leading sin(M theta). The quadratic recurrence preserves this normalization because its ordered pairs satisfy i+j=n, and the Poisson equation is linear at each order. The resonant free amplitudes undergo the same invertible normalization. Thus an obstruction for the unit profile rules out all its nonzero scalar multiples. This argument makes no claim at a=0.

## Exact sin15 continuation, V407

The first three compatibility responses are nonzero. They uniquely fix H9 approximately-0.0011047455853532978, H18 approximately0.00002054766027390991, and H27 approximately0.0008115679113394548. At the fourth step sigma4 is exactly zero, whereas the constant obstruction R4 is strictly between3.7559 and3.7560. Thus no H36 can pass order45. The full positive rational is retained in verification/sin15_block4.json, and the support criterion separately explains its zero response. The computation checks27 affine coefficient identities,68 Poisson identities and1584 ordered products. Independent team reproduction is pending.

For sin13, independent exact polar reproduction completed by the theory part and audited at 2026-10-31T16:19:41+00:00. Its sign, zero response, all displayed constants and the 2282/2283 digit counts agree with the Cartesian result. The polar log retains no complete rational, so exact equality of the two full rational encodings is not claimed.

## Independent modular proof of the sin15 obstruction

The following verification is complete. It uses the theory part's independently derived polar recurrence, specialized to delta4/9 and f1=sin(15theta), in two modular coefficient rings. Each division is checked by multiplying the proposed inverse by its divisor and obtaining1 modulo the modulus. This is sufficient for reduction of rational arithmetic, even without assuming primality: the exact rational denominators lie in the localization generated by these checked units, and the reduction map is a ring homomorphism. Induction over the finite recurrence therefore identifies every modular output with the image of its exact rational counterpart. A nonzero modular image proves the exact rational is nonzero; a zero image alone proves no exact vanishing.

The first compatibility is zero by the support argument above. At the first three steps, nonzero response images imply nonzero exact responses, so the earlier three harmonics are uniquely fixed. The fourth response is zero for an independent exact reason: neither3 nor31 belongs to S_15. Indeed the nearest allowed odd multiples of15 are15 and45, with distances at least12 from3 and14 from31, exceeding the allowed shift8. Thus the support theorem gives sigma4=0 for all earlier harmonics. A nonzero image of the fourth constant obstruction then proves incompatibility at45 for every H36. The modular computation was checked against the reductions of all eleven retained exact constants, responses and tuned amplitudes, as well as its original published output. The exact Cartesian rational separately supplies the stated real interval3.7559<R4<3.7560.

Both fresh modular replays passed at 2026-10-31T18:08:41+00:00. Each run checked35049 inverse calls, involving2160 distinct unit residues. The fourth constants are893328309944763636 modulo2305843009213693951 and1103484672948005963 modulo4611686018427387847. Both are nonzero. The first three responses are nonzero in both rings. All eleven exact-rational reductions match the independently derived polar recurrence in each ring. This proves the finite obstruction without inferring exact equality of the entire rationals from finitely many residues. The original exact Cartesian real bound remains separately verified.
