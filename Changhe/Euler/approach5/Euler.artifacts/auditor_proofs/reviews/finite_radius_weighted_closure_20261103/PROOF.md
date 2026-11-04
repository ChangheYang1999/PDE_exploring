# Finite-radius localization and the failure of the proposed distance weight

## 1. Statement and exact scope

Let 0<c<1, omega be finite, A=cI-omega J and L=(1-c)I+omega J. Suppose U is C2 on R3, P is C1, div U=0 and

    LU+DU(Ay+U)+grad P=0.

Assume U tends uniformly to zero, |U(y)|<=C(1+|y|)^(-a) with 0<a<=3/2, and curl U is bounded outside a ball. Compact regularity makes U and curl U globally bounded. Write M=sup|U|, G=DU, B=Ay+U, e=B/|B| in a sufficiently large exterior region, Pi=I-e tensor e, T=Pi G Pi, and

    k=min(1+a,1/c), Phi(R)=sup_(S<=|z|<=R)|G(z)|.

Here S is fixed and sufficiently large, in particular S>2M/c. All constants below may depend on the fixed profile and S, but not on the varying outer radius R or distance d=R-|y|.

The terminal-anchored characteristic localization remains inside radius R for every d>0. It gives a local Holder logarithm using Phi(R), with a logarithmic boundary cost. The proposed distance-weighted supremum does not turn this estimate into an every-scale lower-growth theorem: its strain and cutoff costs are incompatible. The estimates alone admit smooth scalar concentration examples, even with all fixed finite local Ls means tending to zero. None of these examples is an Euler field. The every-scale conclusion and unrestricted bounded-gradient conjecture remain open.

## 2. Dependencies already independently proved

A1353-A1359 prove the parent C52 conclusions and stronger mean statements. In particular, a global gradient bound O(r^delta) for delta<k gives bounded gradient, and an unbounded gradient has limsup exponent at least k. The transverse identity and pressure estimate are

    |T|²=-Delta P+sigma²-2g.h-(e.h)²,
    |grad P|<=C r^(-a)log²(2+r),

where g=Pi G^T e, h=Ge and sigma=(curl U).e. They imply, for every 0<rho<=r/2,

    average_B |T|² <= C r^(-a)log²(2+r)/rho
                      +C r^(-1-a)log²(2+r)
                      +C r^(-2nu)log²(2+r),             (1)

with nu=min(1+a',1/c) for any fixed 0<a'<a. Also h is small and g is bounded. These facts require no gradient envelope or Holder hypothesis.

The local physical Holder estimate used below is A757 Section4, reread for this audit. Its proof is the characteristic difference inequality with an integrable margin kernel v^(-1/2)(1+|log v|), the bounded-vorticity local div-curl estimate, and an ordinary integral Gronwall inequality. The bounds needed for the current substitution are displayed in Section4; no complete theorem from A757 is applied outside its scope.

## 3. Exact terminal-anchored containment

The case M=0 has U=0 and is immediate. Otherwise put K=M/c, r=|y|, tau=r^(-1/c), t=1-tau and b=d/(4r). In physical coordinates the center xstar has norm one. For an earlier time q set

    D(q,t)=K((1-q)^c-tau^c),
    lambda=((1-q)/tau)^c>=1.

Bounded physical velocity gives displacement at most D(q,t). Pair paths ending in the ball of radius b lie in radius b+D(q,t), and their joining segments lie there too. The larger radius b+2D(q,t) leaves the required elliptic margin. Its maximal profile radius is exactly

    (1-q)^(-c)(1+b+2D(q,t))
      =2K+(r+d/4-2K)/lambda
      <=r+d/4<R.                                      (2)

The inequality uses r>S>2K. The radius b+2D is positive throughout the backward interval, even if its representation as a constant plus 2K(1-q)^c has a negative constant. Retaining A757's additional terminal padding would instead create a lower restriction on d; that padding is unnecessary here.

For final inversion use ell=min(r/64,d/8), and propagate on a slightly larger terminal ball. The same calculation with d/2 still stays below R. Clipping by r prevents the ball meeting the origin when d is large. Choose a fixed initial time sufficiently close to one. All these physical balls then lie in a fixed annulus, their initial profile images are in a fixed compact exterior annulus, and their initial Holder seminorms are uniformly bounded by compact C2 regularity. This choice is independent of R and d.

## 4. Holder logarithm without an exterior gradient envelope

On every pair path and local margin region in(2), the physical fields satisfy

    |grad u(q)|<=C(1+Phi(R))/(1-q),
    |xi(q)|<=C/(1-q).

The accumulated stretching is at most C(1+Phi(R))log(2+r). In the A757 difference inequality, the inhomogeneous terms are bounded by a fixed power of tau^(-1), since the vorticity exponent is now exactly one. The time-margin kernel remains integrable. Gronwall therefore gives

    log(2+[xi(t)]_(1/2))<=C(1+Phi(R))log(2+r).          (3)

The final elliptic localization at physical length ell/r costs powers of r/ell. After taking a logarithm, and forming the cutoff transverse divergence and curl, their global one-half-Holder seminorm K_v obeys

    log(2+K_v)<=C(1+Phi(R))log(2+R)+C log_+(R/d).       (4)

Products of the local algebraic coefficients only add logarithms of already bounded quantities and Phi(R), absorbed on the right. The zero extension uses a cutoff vanishing near its support boundary.

The fixed-annulus Biot-Savart localization may extend outside radius R. Its remote term and harmonic remainder use only the globally given bounds for U and curl U, as is explicit in A757(17). The unknown gradient and local Holder seminorm occur only on the nested regions in(2). The pressure lemma also uses U and curl U, not Phi outside R. Thus(4) has no concealed outward gradient envelope. A positive but arbitrarily small d is legitimate.

## 5. What the localized transverse inversion gives

For any fixed 0<b0<k, the previously proved h and sigma bounds can be weakened to C r^(-b0). The exact transverse div-curl identities then give data bounded by

    C r^(-b0)+C r^(-1-a)(1+T_loc),

where T_loc is the supremum on a ball of radius comparable to ell. Combining the logarithmic inversion with(4), and absorbing a small pointwise coefficient at large r, yields the prototype

    |T(y)|<=C+C(r^(-b0)+r^(-1-a)T_loc)L_R(d)
                 +C r^(-a)/ell,
    L_R(d)=(1+Phi(R))log(2+R)+log_+(R/d).             (5)

The cutoff error is written favorably without a logarithmic multiplier. Its data lie away from y, where the kernel integrates to at most C/ell times the velocity bound. Retaining a logarithm there only makes the forthcoming problem worse.

## 6. Two independent failures of the weighted closure

Put epsilon=d/R and Theta_R=sup((R-|y|)/R)^gamma |T(y)| for gamma>0. The envelope is finite, continuous and nondecreasing in R; it is bounded for all R exactly when T is bounded. These topological facts do not control the unweighted Phi(R).

At a fixed R a smooth scalar field of height A in an outer layer of thickness eta has unweighted supremum A and weighted supremum at most A(eta/R)^gamma. Taking eta/R=A^(-2/gamma) makes the latter at most A^(-1). Thus no fixed same-radius estimate Phi(R)<=C(1+Theta_R) follows from the weighted definition. Bounded g,h do not remedy this transverse example. Control through Theta_(2R) is possible but restores an outward-radius dependence.

Alternatively redo the strain bound from Theta_R. Near r comparable to R, the backward distance to the outer sphere grows comparably to d+Rs, by cr-M<=dr/ds<=cr+M. The strain integral supplied by the weighted bound contains

    C Theta_R F_gamma(epsilon),
    F_gamma(epsilon)=integral_epsilon^1 u^(-gamma)du.   (6)

The local transverse bound T_loc<=C Theta_R epsilon^(-gamma) consumes the whole positive weight in the nonlinear term of(5). That term is then bounded only by

    C R^(-1-a)Theta_R² F_gamma(epsilon).              (7)

For gamma>=1, F_gamma diverges as epsilon tends to zero: logarithmically at one and by a power above one. For 0<gamma<1 it stays bounded, but the favorable cutoff error in(5), after weighting, is

    C R^(-1-a)epsilon^(gamma-1),                     (8)

which diverges. No gamma controls both stated estimates. At fixed R, epsilon can be arbitrarily small, so changing log R to log² R does not absorb the defect. This proves insufficiency of these bounds, not that a genuine Euler profile attains their worst values.

A nondecreasing general weight w(epsilon) faces the same stated mechanism when the local supremum is estimated at a smaller boundary distance: cutoff control requires w(epsilon)<=C epsilon, while the strain estimate contains integral du/w(u), which diverges. The local weight ratio cannot provide a compensating small factor. This observation is restricted to this particular supremum and inversion argument.

## 7. The distinct radial-supremum issue and its conditional repair

A coefficient r^(-b0) cannot be replaced by R^(-b0) when maximizing over S<=r<=R. The maximizer may remain at a smaller radius; removing a fixed compact set does not fix the power. There is nevertheless a valid repair if one first proves the stronger, currently unavailable, unweighted same-radius pointwise inequality

    |T(y)|<=C+C r^(-b0)log r(1+Phi(r))².              (9)

At the first radius r where the continuous envelope attains a new sufficiently large level H, the maximizer lies on that sphere. Bounded g,h and(9) give H>=c0 r^b0/log r. The latter comparison function is increasing for large r. If the envelope is unbounded and at a sufficiently large R it were below c0 R^b0/log R, choose a level strictly between that threshold and the larger of Phi(R) and the fixed initial threshold. Its first attainment occurs after R, contradicting the preceding inequality. Hence(9) would imply an every-scale lower bound for an unbounded envelope. The present weighted argument does not establish(9).

## 8. Exact scalar concentration test, including every fixed finite Ls mean

Fix lambda>1 and p>max(b0,1+a,k). Choose a smooth nonnegative bump psi supported in[-1,1] with maximum one at zero. Let r1 be large, r_(n+1)=r_n^(n+2), H_n=r_n^p, and choose

    0<epsilon_n<=min(exp(-H_n),r_n^(-a-1)/H_n²,1/10)

small enough that the annuli are disjoint. Define the locally finite smooth radial scalar field

    f(y)=sum_n H_n psi((|y|-r_n)/epsilon_n),
    F(R)=sup_(|y|<=R)f(y).

It has polynomial upper growth p. On the n-th bump F(lambda r)>=H_n, so

    f(y)<=C r^(-b0)log r(1+F(lambda r))².             (10)

Outside the bumps the inequality is immediate. At R_n=r_(n+1)/(2lambda), F(R_n)=H_n, so log F(R_n)/log R_n tends to zero and F(R_n)log²R_n/R_n^b0 tends to zero. At peak radii the exponent is p. Thus the limsup conclusion is respected while an every-scale lower bound fails for this scalar example.

For a ball of radius rho<=r/2 meeting one annulus, integration of spherical caps gives intersection volume at most C epsilon_n rho² when rho>=epsilon_n; otherwise use the full ball volume. Consequently

    average_B f²<=C H_n² min(1,epsilon_n/rho)
                 <=C r^(-a)/rho.                   (11)

The large spacing ensures such a ball meets at most one annulus. The exponential width also gives, for every fixed finite s>=1, a unit-ball integral bounded by C_s H_n^s exp(-H_n), tending to zero. Thus even all fixed finite local Ls means, the strengthening proved in A1358, do not by themselves prevent these scalar plateaus.

The same field satisfies the finite-radius prototype(5) for every R>r when T_loc and Phi are replaced by the scalar local supremum and F. If R>=r_n, the nonlinear factor r^(-1-a)(1+F(R))log(2+R) eventually exceeds one, since p>1+a, and the local supremum includes y. If R<r_n while y lies in its bump, then d=R-r<r_n-r<epsilon_n. The cutoff term r^(-a)/ell dominates H_n by the width choice. Outside the bumps there is nothing to check. No carrier, curl or Euler identity is claimed for f.

## 9. Verification and model comparison

All nine consultation sections, its answer and the parent addendum were read and pinned. The independent proof checks the exact radius, the A757 substitution, the boundary powers, the first-attainment argument and the scalar example. No numerical computation or formal build is necessary. Sections6 and8 add explicit scope and the all-finite-Ls strengthening.

The parent agent is configured for model, with provider runtime unattested. Its nested consultation reports that credential retrieval failed before any requested model inference; this is not a received model response. The mathematical conclusions here come from the written arguments and this independent reconstruction. The every-scale theorem for actual profiles and the main bare-decay arbitrary-helicity all-omega conjecture remain open.
