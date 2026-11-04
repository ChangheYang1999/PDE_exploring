# Persistent weak-L2 tails on a closed set

This is an independent reconstruction of LIT353, submitted source SHA256 97e2e1d9a3b2df9ffb3a687ae393fa789cd72e0151a2325c9e525d5ccf1be41f. The full seven source sections and 34 manual checks were read. This is a coefficient example, with no scalar solution or Euler profile attached to it. The existing configured model comparison is pending at initial writing.

## 1. Exact assertion

Let D be a bounded open planar disc, F a nonempty compact subset of D with empty interior, U an open neighborhood of F with compact closure in D, and kappa>0. There is a nonnegative measurable function b on D, finite everywhere, zero on F and smooth on D minus F, with support in U, such that

    M_D(b)^2 := sup_(t>0) t^2 area({b>t}) <= 16 pi kappa^2/3.

For every open V contained in D and meeting F,

    T_V(b) := limsup_(t->infinity) t^2 area({b>t} intersect V)
             >= pi kappa^2.

Also b belongs to Lp(D) for every 0<p<2, whereas the integral of b^2 on every such V is infinite. These assertions allow F to have positive area or to be a perfect Cantor set; they require empty interior, not zero area.

## 2. A locally finite family of disjoint supports

Choose a nonnegative smooth radial cutoff psi on the plane, equal to 1 on the closed unit disc, at most 1 everywhere, and zero outside the disc of radius 2. Such a cutoff follows by composing a smooth one-dimensional step with the radius squared. List all open discs with rational centers and radii whose closures are contained in U and that meet F. This is a countable nonempty list. Enumerate it with repetitions so that every listed disc occurs infinitely often; for example list the first disc, then the first two, then the first three, and continue. Denote the resulting sequence by B_n.

Inductively choose centers z_n and amplitudes a_n. Put r_n=kappa/a_n. Require a_1>=1, a_n>=2a_(n-1) for n>1, and require the closed discs E_n of radius 2r_n about z_n to be pairwise disjoint, contained in B_n minus F, and at distance less than 1/n from F at every point.

At step n choose x in F intersect B_n. The finite union of previously chosen E_j is compact and avoids x. Therefore a sufficiently small ball about x lies in B_n and avoids that union. Empty interior of F supplies a point z_n outside F in this ball, with |z_n-x|<1/(4n). Since F and the preceding union are closed, a small positive-radius closed ball about z_n avoids both and stays in B_n. Choose a_n large enough to meet the doubling condition and to make 2kappa/a_n smaller than this radius and than 1/(4n). Every point of E_n is then within 1/(2n) of x. This proves all requirements without a lower bound on the available radius.

Any compact K in D minus F has positive distance delta from F. If n>1/delta, E_n misses K. Thus this family is locally finite on D minus F. If V is open and meets F, choose x in V intersect F and a rational disc B containing x with closure in V intersect U. Each occurrence of B in the enumeration gives a full E_n in V. Hence infinitely many such discs lie in V, with unbounded indices.

## 3. Definition, support and regularity

Set b(z)=a_n psi((z-z_n)/r_n) on E_n and set b=0 elsewhere, including on F. Disjointness makes this definition unambiguous and finite at every point. Equivalently it is the sum of nonnegative smooth bumps, extended by zero on F, so it is measurable. On D minus F the sum is locally finite and smooth. At an individual support boundary all derivatives agree with zero because psi is globally smooth with compact support.

The support is the relative closure in D of the nonzero set. Each E_n is contained in U. A limit of points in discs with bounded indices stays in a finite union of closed E_n. A limit with indices tending to infinity lies in F by the distance bound. Thus every support point lies either in an E_n or in F, and therefore in U. Merely having each bump in U would not by itself prove this support assertion; the accumulation control is the necessary additional step.

Each plateau disc of radius r_n has area pi kappa^2/a_n^2 and value a_n. The containing disc E_n has area 4 pi kappa^2/a_n^2. No continuity of b on F is claimed or needed.

## 4. Global estimates

Fix t>0 and let N be the first index with a_N>t. It exists by doubling. Bumps with index below N have height at most t and contribute nothing to the strict superlevel set. Hence

    area{b>t} <= 4 pi kappa^2 sum_(n>=N) a_n^(-2)
               <= 4 pi kappa^2 a_N^(-2) sum_(j>=0) 4^(-j)
               = (16 pi kappa^2/3) a_N^(-2).

Multiplication by t^2 gives the weak norm bound. This includes t=a_j, since N then starts after that bump; strict superlevels are used consistently.

For 0<p<2, disjointness and the height bound give

    integral_D b^p <= 4 pi kappa^2 sum_(n>=1) a_n^(p-2)
                   <= 4 pi kappa^2 a_1^(p-2)
                                    sum_(j>=0) 2^(j(p-2)) < infinity.

The last inequality reverses no sign: the exponent p-2 is negative, so the lower bound on a_n gives an upper bound on its power.

## 5. Local tails and the nonadditivity test

Let V be open and meet F. It contains infinitely many entire plateaus. For any fixed epsilon in (0,1), at the levels t_n=(1-epsilon)a_n associated with those plateaus,

    t_n^2 area({b>t_n} intersect V) >= (1-epsilon)^2 pi kappa^2.

The levels tend to infinity. First take the limsup and then let epsilon tend to zero. This yields T_V>=pi kappa^2. Each such plateau contributes exactly pi kappa^2 to the integral of b^2. Summing over the disjoint plateaus proves local divergence.

If F contains six distinct points, take six pairwise disjoint small open discs V_j about them inside D. Then

    sum_(j=1)^6 T_(V_j) >= 6 pi kappa^2
                         > 16 pi kappa^2/3 >= T_D.

This is a literal failure of additivity or of the corresponding upper bound by a global mass. At a fixed t the six superlevel areas are additive, but their separate limsup sequences need not be synchronized. The construction does not contradict fixed-level area additivity.

For completeness, if x is outside F, some compact neighborhood of x lies in D minus F and meets only finitely many supports. There b is bounded and its local high tail is zero. Thus the construction indeed permits an arbitrary such F to be exactly the locus where no neighborhood has zero high tail. This observation follows from the same local finiteness, although the submitted theorem only needs the lower bound on F.

## 6. Application scope

The sufficient scalar continuation condition of LIT346 uses a small local high tail. Choosing kappa=n/2 makes the present lower bound equal to its threshold pi n^2/4 at every point of F. A finite global weak norm alone therefore cannot force points failing that sufficient condition to be isolated or finite. In particular a proof that treats the local limsup quantities as summable atoms is invalid.

This coefficient is not asserted to equal a derivative quotient of any nonzero scalar function. No condition relating it to a C1 or C2 scalar solution, a real carrier or an Euler velocity is checked. Consequently the finite-regularity scalar problem and the unrestricted Euler conjecture remain open. The construction uses only the elementary cutoff, countability, empty interior, disjointness and geometric series proved above. No numerical computation or formalization was used. Existing configured model comparison is requested through the existing working files, with actual provider execution independently unattested.

## 7. Existing model comparison and diagnostic limits

The entire Theory Agent C  comparison recorded 2026-11-04T05:19:03Z has been read against Sections 1-6 and all 34 source checks. Its support construction, weak norm, local tails, nonadditivity and scope agree with the independent proof. This is the existing configured model file comparison; actual provider execution is independently unattested. No new model client or agent was used.

One optional sentence needs a qualification. The comparison says the support equals the union of all closed radius-2r_n discs and F. For the source's stated conditions on psi, only containment follows: psi may already vanish on an annulus below radius 2. Equality can be arranged by choosing psi positive at every radius below 2, as in the diagnostic's explicit logistic bump, but is unnecessary for the theorem. The proof here uses only containment. F itself is in the support since every neighborhood of a point of F contains a nonzero plateau.

The complete 237-line diagnostic script, 21-line final log and 23-line first-run log were read, not rerun. The final log contains twenty predicates: five SYM, one EXACT, two GRID, one QUAD, six SAMPLE and five EX. The symbolic superlevel-radius predicate permits a numerical fallback, but the retained output explicitly says simplified=0. Its elementary identity can also be checked by substituting u=2/(sqrt(L^2+4)-L+2) into 1/(1-u)-1/u=L; the denominator is greater than 2, so 0<u<1. The three tested subcritical p values do not replace the general geometric-series argument in Section 4. The quadrature and level-grid bounds are numerical, not uniform proofs. The rational Cantor geometry is exact only for its forty constructed discs.

The first-run failure of strict bump monotonicity near floating-point saturation is disclosed. The corrected finite grid stays away from the endpoints, and the analytic derivative of 1/(2-rho)-1/(rho-1) is positive throughout (1,2). This proves strict monotonicity of the smooth bump independently of either grid. One absolute local prefix in the retained first-run warning was replaced by the relative agent prefix; both original and retained hashes are recorded.

The last two EX controls use exact rational arithmetic, although the note calls all EX controls numerical. In particular, forty discs in one compact set do not by themselves disprove local finiteness. The displayed infinite family does: centers (c0,1/40+2^(-n-10)) and radii 2^(-n-20) have pairwise disjoint closed discs of twice those radii and converge to the point (c0,1/40), which is outside the line containing F. Every such disc lies in the fixed disc of radius 1/80 about that point. For consecutive indices the center gap is 2^(-n-11), while the sum of twice the radii is 3*2^(-n-20), smaller by the strict inequality 3<512; more distant pairs are also separated. This is an elementary counterexample to local finiteness after dropping the distance-to-F condition, not an inference from a finite computation.

The other geometric control concerns a disc contained in the interior of F. No point in it lies outside F by set containment; its finite grid is illustrative only. None of these diagnostic qualifications changes the source theorem. The independent proof and the mathematical comparison suffice without any diagnostic output.
