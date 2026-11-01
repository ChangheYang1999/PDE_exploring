# A constructive exterior radius for the tuned rational examples

Status: PROVED. The theory part independently confirmed the proof at 2026-10-31T09:56Z; the verifier records that review in V254.

## Statement

Let c=3 and let b be either real root of

    176703765525000 b^6 -222533688701250 b^5 +96180432855375 b^4
    -20675598499400 b^3 +2783057141280 b^2 -243275209320 b
    +10532171936 =0.

Let f_1=epsilon[sin(theta)+b sin(3theta)], epsilon nonzero real. Normalize each resonant stream coefficient by the unique tuning in TheoremT. Assuming the exact response bounds verified below, the density and stream series, with every appropriately weighted Cartesian derivative, converge uniformly on r>=R whenever

    R > 2^180 |epsilon|^(3/2).

The sums are real analytic exterior stationary solutions, with a common C-infinity potential on every strictly smaller exterior region. The density and stream series contain no logarithm; the potential may contain exceptional logarithmic terms. There is no assertion about a canonical whole-plane stationary extension.

## Uniform response lower bound required

For each of the two roots it suffices to prove

    |sigma_k(b)| >= 1/100000,  k>=2.                         (1)

Here sigma_k is the exact response of topic119. For k=2,...,6 this is a finite collection of cubic inequalities on exact isolating rational intervals for b. For k>=7 write

    sigma_k(b) = -(k-1)(2k-1)^2 N(k,b)/D(k),

where D(k) is the positive denominator in topic119. Replace k by t+7. It suffices that every coefficient in t of

    (k-1)(2k-1)^2 N(k,b) - D(k)/100000

be nonnegative for b in the corresponding isolating interval, and at least one be positive. Bounds on each coefficient are obtained by rational interval evaluation of a cubic polynomial in b. This is an all-k certificate; checking finitely many sampled responses would not prove (1).

The arithmetic file must retain the root intervals, Sturm sign variations at their endpoints, all coefficient lower bounds, and all ten small-k response bounds. Until those tests pass, (1) and the explicit-radius claim are conditional.

## An explicit supersolution for the majorant equations

It is enough to treat epsilon=1, then scale. Both roots lie in (0,1), so ||f_1||_1<=2. The maximal leading frequency is3, hence kappa=28/3<=10. Under (1), the equations in topic119 are dominated coefficientwise by those with parameters

    a=2, kappa=10, sigma_*=1/100000,
    d=(3/2)kappa a^2=60, e=3 kappa a d=3600.

Let Y=(W,U,V,E) and let Phi(z,Y) be the polynomial right side of the four generating-function equations of topic119 for these parameters. All coefficients are nonnegative. Write

    Phi(z,Y)=c+JY+z Psi(z,Y),

where c=Phi(0,0) and J=partial_Y Phi(0,Y). The latter is constant and strictly lower triangular:

    J = [[0,0,0,0],
         [60,0,0,0],
         [1800,60,0,0],
         [10800000000,180000000,6000000,0]].

Every coefficient of Psi is nonnegative. Set Q=(I-J)^(-1)=I+J+J^2+J^3. The majorant system is equivalent to

    Y=Y0+z Q Psi(z,Y),  Y0=Qc.

Exact substitution gives

    Y0=(270000,22680000,2041200000,19245600000000000).

Set M=2^55 and z0=2^(-120). Direct integer arithmetic in the certificate verifies

    max_i (Y0)_i <= M,
    max_i [Q Psi(1,2M,2M,2M,2M)]_i <= M 2^120.              (2)

As Psi has nonnegative coefficients, for real 0<=z<=z0 and componentwise 0<=Y<=2M,

    Y0+z Q Psi(z,Y) <= M+z0 Q Psi(1,2M,2M,2M,2M) <=2M.

Iterate this transformed map starting at the zero vector of formal power series. The coefficients are nonnegative and increase. The map has a factor z in every nonconstant iteration term, so each fixed Taylor coefficient stabilizes after finitely many iterations. It is the same unique formal solution as in topic119. Evaluating the iterates at z0 gives vectors bounded by2M. Monotone convergence of the nonnegative coefficient sums proves that the limiting formal series converges absolutely at z0. Each coefficient is therefore at most 2M z0^(-m), and all original x_n and eta_n obey a geometric bound with base z0^(-1)=2^120.

This argument supplies a constructive disk without needing a quantitative implicit function theorem. It does not require the map to contract in the ordinary unweighted supremum norm.

## Exterior convergence and scaling

At epsilon=1, z=r^(-2/3). The geometric majorant converges whenever z<2^(-120), that is r>2^180. On any strictly smaller z disk an angular strip can be chosen with 2^120 exp(4 tau) r^(-2/3)<1. Finite angular bandwidth and the polynomial costs of differentiation then give all weighted derivative bounds, as in topic119. The equations and common potential follow from the already audited theorem.

For general epsilon, every order n scales by epsilon^n. The convergence condition becomes |epsilon| r^(-2/3)<2^(-120), exactly the displayed radius. No asymptotic root fit is used in this proof.

Dependencies: topic119 including exact response formula; exact rational root isolation and inequalities(1); integer inequalities(2); the common-potential theorem in topic109. All hypotheses and numerical certificates are to be retained under verification. The independent review and all exact arithmetic certificates have passed.
