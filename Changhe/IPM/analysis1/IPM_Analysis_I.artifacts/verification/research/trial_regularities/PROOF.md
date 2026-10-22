# X3 regularity and existence of its canonical velocity

Status: analytic proof. This verifies the trial's kinematic admissibility, not its stationary transport equation.

## Statement and exact data

Let L>0, 0<k<1, r_0>0, and p=6+2k/(2-k). Let b_m, 0<=m<=M, be degree-seven clamped splines on [0,1], with simple interior knots, eightfold endpoint knots, and first spline coefficient zero. Let T be a polynomial of degree at most five. Define q, chi, H and rho by the ansatz in PROMPT.md. For the exact X3 data, these conditions hold by the input and polynomial audits in ../canonical_inverse/evidence/exact_audit.json.

Then rho has the required parity, rho=x^2 y a with a continuous and a(0)=1, and rho belongs to C^{2,alpha}_loc for every 0<alpha<1. There is a finite constant C such that

|rho(X)|+(1+|X|)|grad rho(X)| <= C(1+|X|)^k.

There is a unique parity-compatible canonical velocity U with div U=0, curl U=-rho_x and U=o(|X|). It is C^{2,alpha}_loc for every alpha<1. Its stream function, fixed by oddness in both coordinates, is C^{3,alpha}_loc. Thus the center strain exists classically and the integral identity in ../canonical_inverse/PROOF.md applies. No quantitative residual or transport assertion follows.

## Center and axis regularity

Write R=x^2+y^2. Near R=0, q is analytic in R, vanishes simply at R=0, and each b_m(q)=q B_m(q), with B_m a polynomial on the first knot interval. Also chi=R/(R+L^2 r_0^2). For m>=1, let P_{2m}(x,y)=Re((x+iy)^{2m}). Then

chi^{m-1} b_m(q) cos(2m theta)
= [b_m(q)/R] P_{2m}(x,y)/(R+L^2 r_0^2)^{m-1}.

The right side is analytic near the origin because b_m(q)/R has a removable analytic value. For m=0 the term is just b_0(q), which is analytic. All these terms tend to zero at the center. The logarithmic term is analytic there and also vanishes.

The apparently singular final term in H has the exact Cartesian form

|x|^{p-2} y^2 (L^2+R)^{-p/2} T(2q-1).

Since p>6, the function |x|^{p-2} has four continuous derivatives and its fourth derivative is locally Hölder of any exponent below min(1,p-6). In particular it is C^{3,alpha}_loc for every alpha<1. The remaining factors are smooth near the center. This proves more regularity than C^{2,alpha} is needed there, and the final term also vanishes at zero. Thus a=exp(H) is continuous, even in both coordinates, and a(0)=1.

Away from the origin, the polar coordinate formula for each smooth angular mode defines a C^6 function across the simple spline knots. The singular Cartesian factor just displayed is C^{3,alpha}_loc for every alpha<1; its other radial factors are C^6. Therefore H, a and rho are C^{2,alpha}_loc across every axis and every radial knot. No assertion that a is smooth is made.

## Bounds at infinity

On q in [0,1], every spline b_m and its first derivative are bounded, as are T and T'. There are finitely many modes. The angular function |cos(theta)|^{p-2}sin^2(theta) and its first derivative are bounded. For r>=1,

r q_r = (1-k) [r^2/(L^2+r^2)](1-q),
r chi_r = 2 chi(1-chi),
r s_r = 2s(1-s),  s=r^2/(L^2+r^2).

It follows that S=H-(k-3)log(1+(r/L)^2)/2, r S_r and S_theta are uniformly bounded for r>=1. Hence exp(H)<=C r^{k-3}, |r H_r|+|H_theta|<=C, and rho=r^3 cos^2(theta)sin(theta)exp(H) gives

|rho|<=C r^k,  |grad rho|<=C r^{k-1}.

The compact region is covered by local regularity. These estimates include the axes by continuity.

## Construction of the canonical inverse

Use the kernel K from PROMPT.md. Each component is homogeneous of degree -2 and has zero circular mean. Define

U(X) = -rho(X)e_2/2 + PV integral_{R^2} [K(X-Y)-K(-Y)]rho(Y) dY.

The term K(-Y)rho(Y) is locally integrable near zero because rho(Y)=O(|Y|^3). Near Y=X, subtract rho(X) in the principal-value singular part; local C^1 regularity makes the remainder absolutely integrable. At infinity, the kernel difference is O_X(|Y|^{-3}) and rho(Y)=O(|Y|^k), so the tail is absolutely integrable since k<1. The circularly truncated integral of K(-Y)rho(Y) is zero on every annulus: the first component is odd in x and the second is odd in y. Thus this definition is the symmetric canonical singular integral.

The distributional identities for K and the local term can be checked from G(X)=-(1/(2pi))log|X|, with -Delta G=delta_0: U=(-partial_xy(G*rho), partial_xx(G*rho)). Differentiation is understood after the convergent subtraction above. Indeed -G_xy=K_1 away from zero, G_xx=K_2 away from zero, and G_xx has the additional distributional term -delta_0/2. It follows that div U=0 and curl U=-rho_x. Reflections give the required velocity parity.

For completeness, the growth estimate is explicit at the level of exponents. Fix |X|=R>=2 and separate |Y-X|<R/2, |Y|<=2R outside that ball, and |Y|>2R. On the first region, circular cancellation and |grad rho|<=C R^{k-1} give C R^k. On the second region the nonsubtracted kernel is bounded by C/R^2, and integral_{|Y|<=2R}|rho(Y)| dY<=C R^{k+2}. On the third, the difference bound gives C R integral_{2R}^infty t^{k-2}dt<=C R^k. The removed K(-Y) term over the full disk |Y|<=2R has integral zero by parity. If the near ball is separated before this cancellation, its removed piece is bounded by C R^{-2} times its area R^2 times the density bound R^k, since |Y|>=R/2 there. The local term is also O(R^k). Thus U=O(R^k)=o(R).

Local regularity uses the classical interior Schauder implication: if -Delta v=f in distributions, f is locally C^{0,alpha}, and v is a distribution, then v is locally C^{2,alpha}. One may prove it by a compactly supported Newton potential for f and Weyl's lemma for the harmonic remainder. Here -Delta U_1=-rho_xy and -Delta U_2=rho_xx, so this implication yields U in C^{2,alpha}_loc. The simply connected plane and div U=0 give a stream function with grad psi=(U_2,-U_1); it is C^{3,alpha}_loc. Parity fixes its additive constant and makes it odd in both coordinates.

For uniqueness, the difference of two admissible velocities has zero divergence and curl, so its components are entire harmonic functions. They have sublinear growth. The harmonic interior gradient estimate at radius R gives |grad v(X)|<=C R^{-1} sup_{B_R(X)}|v|=o(1) as R tends to infinity. Each component is constant. Velocity parity forces both constants to zero. In particular no linear strain from a harmonic lambda*x*y is allowed.

## Scope and dependencies

The proof uses the exact finite spline data, standard polynomial spline continuity at simple knots, the elementary power-function regularity test, the logarithmic fundamental solution, Weyl's lemma and interior Schauder regularity. It supplies qualitative finite constants for membership, not usable numerical operator constants. It does not prove the transport equation, scalar normalization for the held c_l, an inverse estimate, or a nearby exact solution.
