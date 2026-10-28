# Binding audit clarifications for the joint cofactor target

Read this file with the unchanged PROOF.md, SHA256 58369aa93dbfd1dd90cf8b305f3a1ab3f143dbb38bb2359fbf2b57e59049688e. The actual independent audit is retained in evidence/opus_audit.md. These details close its nine findings without changing the space, operator, hypotheses or conclusions.

1. Both derivatives of the full column cofactor are controlled. Put p=2k-1. Outside a fixed disk, proof 217(5) gives M0=O(r^p(1+log r)) with every fixed cylinder derivative used here. Its finite smooth angular factors vanish quadratically on the vertical axis, term by term as explained immediately after that formula. Division by cos(theta)^2 therefore gives a smooth finite angular cofactor with bounded angular derivatives at all angles. Hence

 |M0/x^2|<=C r^(p-2)(1+log r),
 |grad(M0/x^2)|<=C r^(p-3)(1+log r).

The second bound is for both Cartesian derivatives. Splitting distances at r on a comparable annulus gives M_R(M0/x^2)<=C R^(p-2)(1+log R). It agrees with proof 232's thin-cone clarification and also covers the complementary angles, where division is bounded directly.

Near zero use M0=m0+H0 and the exact local identity proof 217(3). With a1=rho0_x/x, a2=rho0_y/x^2, U[zeta]=c[zeta](-x,y)+R_zeta and n'_0=3-c[zeta],

 n'_0 m0/x^2
   =c[zeta](-(2/3)a1+(4/3)y a2)
       +a1 R_zeta1/x+a2 R_zeta2.

The factors a1 and a2 are locally Lipschitz by their actual finite divided origin expansions. The remote-tail velocity is smooth there, R_zeta1 is odd in x, and R_zeta1/x is smooth by integration of its x derivative. Thus this full cofactor is Lipschitz in both variables. The compact column has H0/x^2=chi0(a1+y a2)/3, also Lipschitz. On compact punctured annuli, the C6 joins and smooth axis division give the same bounded first derivatives. This proves the joint cofactor assertion globally without inferring it from an undivided horizontal derivative.

2. The bounded coupling uses proof 234(1) and(2), exactly as stated. Those two lemmas were independently audited by the actual independent model and CONFIRMED in V265 before this audit was recorded. The old 'audit pending' sentence is now historical. Proof 236 introduces no additional unproved divided-velocity hypothesis. The first, undivided velocity line of(6) is from topics222 and228; the second, divided line is proof 234.

3. Specify the fixed-disk split as follows: output points are in B4, the input cutoff is one on B8 and zero outside B16. The remote input is separated from every output point by at least4. First and second separated-kernel derivatives are absolutely integrable against the sublinear tail. The arbitrary fixed larger radii change only the qualitative constant.

4. Write the exterior maximal domain explicitly:

 D_R^(3)={h in F_R^(3): V.grad h belongs to F_R^(3) distributionally on Omega_R}.

No boundary trace is prescribed. Distributional equations have the orbit form by the C1 nonvanishing flow boxes of proof 223, clarification4. The time-change equivalence is proof 228, clarification5. Since the field does not vanish on the exterior vertical axis, the same local argument also applies there directly.

5. The discrepancy formula(5) is an identity on Omega_R. With all types explicit it is

 P_R A0(E_Rh)-A_R^(3)h=(eta_R-1)T_Rh+h V.grad eta_R.

There is generally a nonlocal interior value of A0(E_Rh); the formula makes no statement that it vanishes. This exterior identity is sufficient for the claimed auxiliary inverse and supplies no global matching or global parametrix estimate.

6. The residual expansion is the exact one in proof 213, with the canonical far construction and velocity bound in proof 222: F0=x^2 y B, B=O(r^2) near0 and O(r^(2k-4)) at infinity, with the stated derivatives and C5 joins. Consequently F0/x^2=yB is locally Lipschitz and has annular order r^(p-2). The weighted threshold gamma>4k is unchanged.

7. The turning packets originate in proof 232(8),(10), and proof 234 restates them. Their cofactor has joint C^alpha norm at least c epsilon^(-alpha)-C on a fixed annulus, so their unscaled Z3 norm diverges. Multiplication by epsilon^alpha makes them bounded, but then the old oscillatory lower bound cannot contradict bounded preimages: its crucial factor becomes q^(alpha-1/2) epsilon^(1/2), which tends to zero when q and epsilon satisfy the original scaling. For alpha<1/2 it is equally lambda^(-1/2)q^alpha. No conclusion about global surjectivity follows from this packet family on Z3.

8. To avoid overloaded notation, call the fixed strain-one bump q_c, the exterior reciprocal coefficient q_ext=1/a, and the packet width s. These are distinct objects. None of the estimates identifies them.

9. The exact range of this audited theorem is unchanged: Banach space and embedding, bounded complete coupling with small output tail, actual residual and column membership, closed maximal domains, a nonclosable cubic derivative jet, and a uniform actual exterior auxiliary inverse. It contains no global inverse, Fredholm result, closed normalization, claim about the range of F0, or nonlinear existence assertion. Separate topics237 and238 are not covered by this audit.
