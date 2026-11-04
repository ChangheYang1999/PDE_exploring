# Independent reconstruction of the source-gradient tradeoff

Status: independent comparison complete; designated verdicts are recorded in the auditor's ledger (AUDIT_LEDGER.md). Source LIT379 is SHA256 74ab8bf057c18c2e72591ab435397de0ec0b8dd096c66458ffb88d20bad6d238. All eight source sections, 42 analytical checks and the support note have been read. The following proof is kinematic; the full-profile application keeps its additional hypotheses. No finite-M optimality of these roots is asserted; Section9 proves first-order sharpness as M tends to infinity in the kinematic class.

## 1. Exact statement and notation

Let U be C1(R3;R3) and divergence-free. Suppose E(R)=integral_(B_R)|U|^2 satisfies E(R)/(LR^beta)->1 for L>0 and 0<beta<1. Let m=2-beta, k=(beta+1)/2 and q=tr((DU)^2). All spherical integrals use ordinary area measure, with area 4pi. About the origin set

    F(R)=integral_(1<r<R)r^(-beta)|U|^2 dx,
    T(R)=integral_(1<r<R)r^(-beta)|U_T|^2 dx,
    G(R)=integral_(1<r<R)r^(2-beta)|DU|_F^2 dx,
    Q(r)=integral_(S2)q(rn)dS,
    J(R)=integral_1^R r^(4-beta)[Q(r)]_+ dr,
    I(R)=integral_(1<r<R)r^(2-beta)[q(x)]_+ dx,
    K_beta=beta m(1-beta).

Here U_T is the orthogonal projection onto the sphere's tangent plane. There is a finite constant C, independent of sufficiently large R, such that

    kF(R)<=sqrt(G(R)T(R))+(k+1)T(R)+C,                (1)
    J(R)>=m[(1-beta)F(R)+beta T(R)]-C.                (2)

Also 0<=J<=I<=G and F(R)/log R->beta L. If

    limsup G(R)/(beta L log R)<=M<infinity,

where M>=0, then

    liminf T(R)/(beta L log R)>=d_beta(M),
    liminf J(R)/log R>=K_beta L+m beta^2 L d_beta(M),  (3)
    d_beta(M)=[2k/(sqrt(M+4k(k+1))+sqrt(M))]^2>0.

The J lower bound holds for I as well. Conversely, a sequence R_n->infinity on which either J(R_n)/log R_n or I(R_n)/log R_n tends to K_beta L must satisfy G(R_n)/log R_n->infinity. This conclusion is on that same sequence; a mere source liminf equality does not give divergence at all radii. Every statement holds at any fixed center using the corresponding integrals and tangent planes.

## 2. Divergence freedom with a logarithmic cutoff

Set t=(beta-3)/2, z=log r and U(rn)=r^t v(z,n). Decompose v=fn+w with w tangent. Then

    f_z+kf+div_S w=0,
    F(R)=integral_0^(log R) integral_(S2)|v|^2,
    T(R)=integral_0^(log R) integral_(S2)|w|^2,
    G(R)=integral_0^(log R) integral_(S2)
                      (|v_z+tv|^2+|nabla_S v|_F^2).

The angular derivative is of the Cartesian vector. Differentiating f=v.n along an orthonormal tangent frame gives

    grad_S f=(nabla_S v)^T n+w,
    |grad_S f|<=|nabla_S v|_F+|w|.                   (4)

The derivative of n contributes w and cannot be dropped.

For R>=8 take 0<=eta_R<=1 supported in (0,log R), equal to one on [log 2,log(R/2)], with bounded first derivative on two transition strips of width log 2. The weighted velocity energy on the outer strip is bounded by (R/2)^(-beta)E(R)=O(1), and the inner one is finite. Thus F_eta=F+O(1), with 0<=T_eta<=T and 0<=G_eta<=G.

Multiply the divergence equation by eta_R f and integrate in z and n. Integration of f f_z and div_S w yields

    k(F_eta-T_eta)
      =integral eta_R grad_S f.w
         +(1/2)integral eta_R' f^2.                 (5)

The coefficient of the last term is +1/2. The integral itself has no fixed sign; its absolute value is uniformly bounded. By (4), the triangle inequality in weighted L2 and Cauchy-Schwarz,

    integral eta_R grad_S f.w
       <=sqrt(T_eta G_eta)+T_eta.

Substituting in (5) proves (1). This argument estimates no endpoint value of E' or DU and uses only local C1 regularity and the energy upper bound E(R)=O(R^beta).

## 3. The radial source test and its errors

Divergence freedom gives q=partial_i partial_j(U_iU_j) distributionally, hence

    integral q phi=integral U.D^2phi U               (6)

for smooth compactly supported scalar phi. This identity uses only first derivatives of U after the distributional cancellation of div U.

Let f0 be smooth, nonnegative and radial, zero on B1 and equal to r^m outside B2. Multiply it by a radial cutoff chi(x/R) which equals one on B1 and vanishes outside B2, with 0<=chi<=1. Outside B2,

    D^2f0=m r^(-beta)(Id-beta n tensor n),
    U.D^2f0 U=m r^(-beta)[(1-beta)|U|^2+beta|U_T|^2]. (7)

The tensor in (7) is positive because 0<beta<1. Inside B2 the contribution in (6) is a fixed finite error. Terms differentiating chi lie in R<r<2R, are O(R^(-beta)) in operator norm, and contribute at most C R^(-beta)E(2R)=O(1). The remaining chi D^2f0 term is nonnegative. Therefore

    integral q f0 chi(x/R)>=m[(1-beta)F(R)+beta T(R)]-C.

Radiality and nonnegativity of the test bound its source side above by J(2R)+C; the inner error is again fixed. Replace R by R/2. The increments of F and T over R/2<r<R are O(1), bounded by the same weighted energy estimate as in Section 2. This gives (2) with J(R).

For each r, [integral q]_+<=integral[q]_+, giving J<=I. Since tr(A^2)=sum A_ij A_ji, Cauchy-Schwarz gives |tr(A^2)|<=|A|_F^2. Thus I<=G. These inequalities use neither positivity of q nor additive splitting of positive parts into angular modes.

## 4. Logarithmic limits and the exact root

Finite-interval integration by parts gives

    F(R)=R^(-beta)E(R)-E(1)
          +beta integral_1^R r^(-beta-1)E(r)dr.

The ratio premise yields F(R)=beta L log R+o(log R). If E(R)=LR^beta+O(R^(beta-1)), then the error is O(1), because the remainder in the integral is O(r^-2). The energy remainder is never differentiated.

Let x_R=T(R)/(beta L log R) and g_R=G(R)/(beta L log R). Then 0<=x_R<=1+o(1), and (1) implies

    k<=sqrt(g_R x_R)+(k+1)x_R+o(1).                  (8)

Take a sequence realizing the liminf of x_R. The assumed limsup bound on g_R implies

    k<=sqrt(Mx)+(k+1)x,

where x is that liminf. The right side is strictly increasing for x>=0. Writing s=sqrt(x), its equality root solves

    (k+1)s^2+sqrt(M)s-k=0.

Rationalizing the positive root gives s=2k/(sqrt(M+4k(k+1))+sqrt(M)), proving the first part of (3). Divide (2) by log R to get the source surplus m beta^2 L d_beta(M). The case M=0 gives d_beta(0)=k/(k+1); it need not describe an existing field, because the combined premises can be inconsistent. The implication itself remains valid.

If J/log R tends to K_beta L on a sequence, (2) and F/log R->beta L imply T/log R->0 on that sequence. The same follows when I/log R has that limit, because J<=I. The right side of

    sqrt(GT)>=kF-(k+1)T-C

is then bounded below by a positive multiple of log R. Consequently T>0 at all sufficiently large sequence radii, and

    G/log R >= [kF/log R-(k+1)T/log R-C/log R]^2
                         /(T/log R) -> infinity.

Division by T is thus legitimate. All-radius divergence requires the corresponding all-radius source limit; it is not inferred from a liminf alone.

## 5. Fixed centers and the full-profile interpretation

Ball inclusions E(R-|a|)<=E_a(R)<=E(R+|a|) transfer the ratio premise with the same L to every fixed center a. Repeating Sections 2-4 for U(a+.) proves the stated centered result. The gradient limsup hypothesis must be imposed for the same centered G_a. This argument does not translate the Euler equation.

A full rotating profile means U in C1(R3;R3), P in C1(R3), div U=0 and

    (1-c)U+(((cI-omega J)y+U).grad)U+omega JU+grad P=0,
    J(y1,y2,y3)=(-y2,y1,0).

Here Hb means bounded U and distributional convergence U(R.)->0 on every compact set as R->infinity. For a nonzero full profile with Hb and 2/5<c<1/2, the confirmed energy theorem A3053, rechecked A3114, supplies E(R)=LR^beta+O(R^(beta-1)), L>0, beta=5-2/c. Thus the kinematic theorem applies for every finite omega. Uniformly decaying C2 target profiles meet Hb. No symmetry, pressure sign or pressure normalization is added.

If the extra bound |DU(y)|_F<=D |y|^(-1/c) holds outside some radius, radial integration of the critical weight 2-beta=2/c-3 gives

    G(R)<=4pi D^2 log R+O(1).

For D>0 choose M=4pi D^2/(beta L) in (3). The constant 4pi is the spherical area and D bounds the entire Frobenius norm. For D=0, U is constant on the connected exterior of a ball. A nonzero constant would contradict E(R)~LR^beta with beta<3, while a zero exterior would give finite total energy and contradict L>0 and beta>0. Thus D=0 is impossible under the energy premise. This exclusion uses exterior constancy, not an unsupported strictness assertion in (1).

## 6. Scope and unresolved questions

The source and gradient estimates are kinematic. No pending LIT376, LIT377 or LIT378 result is needed to prove them. Their separately confirmed roles (A3118, A3121 and A3125) are distinct: a family whose positive-source coefficient approaches K_beta L cannot have a uniform finite gradient limsup bound, while a field attaining a finite optimal gradient coefficient must have a strict source surplus. The two optimization problems cannot be conflated.

The constants d_beta(M) and the resulting surplus are explicit sufficient lower bounds, with no finite-M optimality claim. Neither a finite gradient limsup coefficient, a natural derivative bound, nor a useful sign of the source follows here from velocity decay. The full arbitrary-rotation nonexistence problem remains open. No numerical computation, finite angular truncation as a proof, formal certificate or new external theorem is used.

## 7. Independent comparison and the cutoff correction

The full eight-part C comparison of 09:12:21Z is retained in the team records, SHA256 079f9e644b1db23e3f8d25b5ac4d7198b7814b1cc9a17fc7838a7ca7f6207582. It agrees with the theorem, source test, moving-frame derivative and limiting quantifiers. Its numerical script, reported values and grids were not executed or certified here. The actual configured model is reported by the run as model; provider execution is not independently attested.

The initial own Section2 said that the last term of (5) was positive. Only its coefficient is positive. On the outer transition strip eta_R' is negative. To see that this is a real distinction even within the ratio-energy class, choose a smooth scalar radial-logarithmic amplitude supported strictly inside that strip and use a nonzero spherical harmonic Y with f=a(s)Y and w=(a'+ka)grad_S Y/Lambda, where -Delta_S Y=Lambda Y. This gives f_s+kf+div_S w=0. It defines a smooth solenoidal field on a compact annulus. Its cutoff integral is strictly negative. A disjoint homogeneous solenoidal tail beyond the observation ball can supply E(R)~LR^beta without changing the negative integral. A bump supported in the inner strip gives the opposite sign. The corrected Section2 keeps the absolute bound that the proof actually uses. The initial pin remains retained as an erratum record.

## 8. A stronger root from radial derivative energy

Using the same eta_R and compact logarithmic support, direct integration gives

    integral eta_R |v_z+t v|^2
      =integral eta_R |v_z|^2+t^2 F_eta
        -t integral eta_R' |v|^2.

The last term is O(1) by the same strip energy bound. Thus, with G_S,eta=integral eta_R|grad_S v|^2,

    G>=G_S,eta+t^2 F-C,
    kF<=sqrt(T (G-t^2 F+C))+(k+1)T+C.

The quantity under the radical may be taken nonnegative because it bounds G_S,eta. Consequently any finite limsup M for G/(beta L log R) satisfies M>=t^2 and

    liminf T/(beta L log R)>=d_beta(M-t^2),
    liminf J/log R>=K_beta L+m beta^2 L d_beta(M-t^2).

The same holds for I. The proof follows the liminf-realizing sequence of Section4 and takes subsequences if necessary; it never substitutes a liminf for the gradient limsup. The denominator defining d_beta is strictly increasing, so this improves the earlier root. Separately, A3125 gives the stronger admissibility condition M>=H_beta>t^2. This section does not require the pending LIT381 result.

For the degree-one Hardy control of A3125, x*=k^2/(k^2+2) and its angular energy ratio is H_beta-t^2=2t^2/(k^2+2). These identities follow by substituting Lambda=2 into the poloidal angular energy. The decimal grid bounds and monotonicity statements in C's comparison are not used or certified here.

## 9. First-order sharpness and the profile qualification

The large-M asymptotic can be checked without the diagnostic grid. Use the belt construction of A3118 with Z=sin and frequency n. Before normalization,

    g_n=-(k/n)chi sin(n(theta-pi/2)),
    h_n=chi cos(n(theta-pi/2))
          +(chi'+cot(theta)chi)sin(n(theta-pi/2))/n.

Let K_n=integral(h_n^2+g_n^2), T_n=integral g_n^2 and c_chi=(1/2)integral chi^2>0, with spherical measure. Periodic integration by parts gives

    K_n=c_chi+O(1/n), T_n=k^2 c_chi/n^2+O(1/n^3).

The derivative h_n' has leading term -n chi sin, all other derivative-matrix contributions have order at most1, and the belt stays away from the poles. Thus the full homogeneous gradient energy divided by K_n is M_n=n^2(1+O(1/n)). The tail tangential ratio is x_n=T_n/K_n, so M_n x_n->k^2. The smooth compact completion used in A3118 gives E_0(R)=LR^beta for R>=2 once n is sufficiently large. Its compact terms do not affect logarithmic ratios; its solid-rotation core excludes full Euler.

For completeness, the exact angular source formula for a homogeneous solenoidal field follows from a radial compact test psi. If H_n=integral h_n^2, its Hessian pairing is

    integral r^(beta-1)[H_n psi''+(T_n/r)psi']dr.

Twice integrating by parts gives the sphere source integral

    Q_n=m[(1-beta)H_n+T_n]
       =m[(1-beta)K_n+beta T_n]>0.

After normalizing the sphere energy to beta L, the spherical positive-source coefficient is exactly K_beta L+m beta^2 L x_n. Since M d_beta(M)->k^2 and M d_beta(M-t^2)->k^2, both tangential roots and their spherical-source surplus are sharp to first order along this sequence M_n->infinity. No pointwise-positive-source sharpness follows: positive parts do not commute with angular integration. The asserted O(1/n) remainder is analytically sufficient; no O(1/n^2) conclusion is drawn from finitely many numerical samples.

For a nonzero full C2/C1 bounded-Hb profile in the target range, the additional condition DU=o(r^(1/2)) implies DU->0 and then |DU|_F<=D r^(-1/c) for a finite D, by the separately confirmed derivative results A498/A477 and A3102. Hence its tangential and source surplus can use d_beta(4pi D^2/(beta L)-t^2). The argument is valid for every finite omega. As D->infinity this lower surplus has leading term m beta^3 k^2 L^2/(4pi D^2).

This is a conditional profile consequence. The constructed sharpness sequence consists of kinematic controls that fail the full equation. It limits universal inequalities on that larger class, not possible improvements obtained from the full Euler equation. Neither an a priori profile bound on D^2/L, nor actual-profile sharpness, nor the main rotating nonexistence statement is proved.
