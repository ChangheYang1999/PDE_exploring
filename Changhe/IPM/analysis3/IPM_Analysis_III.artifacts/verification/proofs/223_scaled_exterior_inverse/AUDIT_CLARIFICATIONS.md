# Clarifications after independent audit

The audit passes the theorem at its stated strict scaled-space scope. These clarifications are part of the proof and correct two literal details without changing the theorem or the audited proof hash.

1. In the first drift integral, the explicit bound is 2 C r^(k-1)/(ell(1-k)); the factor two follows from the lower radial rate ell/2. All subsequent C constants are generic.

2. Fix the smooth radial extension cutoff with 0<=eta<=1. This is the convention under which its weighted L2 norm does not increase. For a pair straddling its transition, use |eta_R(X)-eta_R(X')|<=C min(1,|X-X'|/R), and |h(X)|<=C N R^beta on the transition annulus. This gives the scaled Holder bound even when the second point is inside the zero collar.

3. The enlarged-annulus Holder comparison follows explicitly as follows. For output radii with ratio at most two, choose the dyadic annulus whose lower radius is at most the smaller radius and less than twice smaller; both points lie in that annulus. For radius ratio greater than two, their distance bounds the smaller radius below and the supremum part gives the difference bound. On any fixed comparable-radius region this yields C N s^(beta-alpha)|X-X'|^alpha. This argument proves the restriction map comparison for the two dyadic grids as well.

4. The actual V is C1 and nonvanishing on r>=R0/2, by the finite differentiated far formulas and its positive radial component. C1 flow-box coordinates convert the continuous distributional equation V.grad h=h+f into a one-dimensional distributional derivative along almost every orbit. Its right side is continuous; integration followed by continuity in the transverse coordinate proves the identity on every orbit. Boundary identities follow by limits from r>R. Conversely the characteristic formula has a jointly continuous orbit derivative Q_R f+f, hence the same distributional derivative. This justifies both exact maximal-domain identities without density of smooth functions in the Holder norm.

5. For h in D_R, E_R h belongs to the global maximal domain D_Z: V.grad(E_R h)=eta_R V.grad h+h V.grad eta_R, and the second term has uniformly bounded scaled norms because V.grad eta_R is O(1) with scale-R coefficient bounds on the transition shell. Thus, after restriction to Omega_R,

 A0(E_R h)-A_R h=(eta_R-1)T_R h+h V.grad eta_R.

The difference is zero for r>2R and by continuity on r=2R. The theorem is still auxiliary; the transition discrepancy is not solved.

6. The transport inverse itself holds in a wider beta,gamma range, but no extension of the stated full-coupling theorem is needed. The weighted pointwise bound can already replace the semigroup bound when gamma>2+2beta; the division used in the proof covers every gamma>4k. The small-tail step uses precisely the full C0 estimates of proof 222, including the strict beta>2k-1 endpoint. No numerical radius, global inverse, closed cubic normalization, or Avenue IV complement estimate follows.
