# Canonical relative inversion under sublinear velocity

Date:2026-10-20. Status: PROVED inverse identity and counterexample to absolute convergence. No B2 existence or nonexistence conclusion.

## Statement and normalization

Let U be a smooth divergence-free vector field on R^2, with

    U(X)=o(|X|) uniformly as |X| tends to infinity,
    Omega=-curl U=-(d_x U2-d_y U1).

No pointwise bound on derivatives of U or on Omega at infinity is assumed. Define

    K(Z)=(Z2,-Z1)/(2pi|Z|^2),
    I_R(X)=integral_{|Y|<R}[K(X-Y)-K(-Y)]Omega(Y)dY.

Then

    I_R -> U-U(0) locally in C^infinity as R tends to infinity.    (1)

Here the finite-radius integral has its ordinary locally integrable kernel; derivatives of that integral may equivalently be interpreted distributionally. For each fixed compact X-set, the result is a smooth function for all sufficiently large R. Formula(1) does not assert that its tail integral is absolutely convergent.

The same limit holds for fixed smooth bounded domains scaled about0, with0 strictly in their interior, and for smooth compactly supported cutoffs chi(Y/R) equal to1 near0. Thus this relative inverse is independent of those regularization shapes within this class. It is the unique normalized sublinear divergence-free velocity with vorticity Omega. There remains an additive constant freedom in the absolute velocity.

With B2 parity, Omega is odd in x and Omega(0)=0. The center strain consequently has the ordinary-at-zero, possibly conditional-at-infinity formula

    d_y U2(0) = lim_R (1/pi) integral_{|Y|<R} Y1 Y2 Omega(Y)/|Y|^4 dY.  (2)

A smooth bounded shear will show that absolute convergence of(1) can fail. The existence of the limit is therefore a stronger scope statement than the usual absolutely convergent decaying-vorticity formula, not a justification for silently treating a conditional integral as absolute.

## Finite-radius integration by parts

Let G(Y)=log|Y|/(2pi), and for fixed X put

    g(Y;X)=G(Y-X)-G(Y).

In distributions with respect to Y,

    Delta_Y g=delta_X-delta_0,
    K(X-Y)-K(-Y)=(-g_2,g_1).

Write n for the outward unit normal of the radius-R disk and J for rotation through pi/2, J(v1,v2)=(-v2,v1). If R>|X|, an exact identity is

    I_R(X)=U(X)-U(0)+B_R(X),
    B_R(X)=integral_{|Y|=R}
       [-U d_n g + JU (g_1 n_2-g_2 n_1)] dS.            (3)

For the second component this follows by adding the identically zero term -g_2 div U to g_1 Omega:

    g_1 Omega-g_2 div U
      =-g_1 d_1 U2+g_1 d_2 U1-g_2 d_1 U1-g_2 d_2 U2.

Integration by parts cancels the two mixed derivatives multiplying U1, leaving U2 Delta g and the boundary terms

    -U2 d_n g+U1(g_1 n_2-g_2 n_1).

The first component follows by adding -g_1 div U to -g_2 Omega. Its boundary term is

    -U1 d_n g-U2(g_1 n_2-g_2 n_1).

These are precisely(3). One may justify the computation by removing small disks around0 and X, applying classical integration by parts, and letting their radii decrease to0. Smoothness of U gives the indicated values from the logarithmic fundamental solution. Equivalently the calculation is an integration by parts of distributions on the disk with smooth boundary data.

## Boundary decay and differentiated convergence

Fix |X|<=M and take R>=2M+1. On |Y|=R, the mean-value theorem gives

    |grad_Y g(Y;X)| <= C_M/R^2.

For an X-derivative of order j>=1, derivatives of log|Y-X| give

    |D_X^j grad_Y g| <= C_{M,j} R^(-j-1).

The boundary has length2piR. Thus(3) gives

    sup_{|X|<=M}|B_R(X)| <= C_M sup_{|Y|=R}|U(Y)|/R ->0,
    sup_{|X|<=M}|D_X^j B_R(X)|
       <= C_{M,j} sup_{|Y|=R}|U(Y)|/R^j ->0, j>=1.      (4)

No derivative of U appears in these bounds. Each finite-radius volume potential is smooth for |X|<R: localize Omega smoothly near any compact X-set, where convolution with the fundamental solution is smooth, and the remaining source is separated from that set. Identity(3) also directly identifies it there with the smooth field U-U(0) plus a smooth boundary integral. Equation(4) proves local C^infinity convergence.

For a fixed smooth domain D containing0, the boundary of RD stays at distances comparable to R, its length is O(R), and its normal is bounded. The same argument proves the asserted domain independence.

For a cutoff chi_R(Y)=chi(Y/R), repeat the integration by parts without an outer boundary. Once R is large enough that chi_R=1 near0 and X, the delta terms again give U(X)-U(0). All error terms are products of U, grad chi_R, and grad_Y g, with their indicated rotations. The support of grad chi_R lies in an annulus at distance comparable to R, its area is O(R^2), and |grad chi_R|<=C/R. The same bounds as(4), with a supremum of |U| on that annulus, therefore apply. This proves the cutoff statement, including differentiated convergence.

## Uniqueness and the center derivative

If two sublinear divergence-free velocities have the same vorticity, their difference has zero divergence and curl and therefore harmonic components. For an entire sublinear harmonic function f, the interior gradient estimate at any fixed point gives

    |grad f| <= C R^(-1) sup_{B_R}|f| ->0.

Thus the difference is constant. Imposing V(0)=0 selects exactly U-U(0), which proves uniqueness of the relative normalization. It does not choose a value for the absolute U(0).

Differentiate the second component of(1) in X2 at0. The kernel is

    d_{X2}K2(X-Y)|_{X=0}=Y1 Y2/(pi|Y|^4).

There is no delta term for this mixed derivative of the logarithmic potential. At Y=0, B2 parity and smoothness give Omega(Y)=O(|Y|), so the absolute integrand is O(1/|Y|), integrable in two dimensions. Consequently the principal-value interpretation agrees here with an ordinary local integral. Local C1 convergence already proved at infinity gives(2). Pairing x>0 and x<0 gives the factor2 form used by the lead.

For example, if Omega(s,eta)<=Omega(s,-eta) for every s,eta>0, every finite paired disk integral in(2) is nonpositive. Its limit is nonpositive too. The center temperature identity gives d_y U2(0)=Psi_xy(0)=1+beta/2>0. This required positive B2 strain rules the reflection-dominance subclass out even without assuming absolute tail convergence. In contrast, a statement about separately convergent upper and lower integrals would require an extra hypothesis.

## Absolute convergence can fail

Take

    U(x,y)=(0,cos x-1), Omega(x,y)=sin x.

The field is smooth, bounded, divergence free, and has the required reflection parity. Fix X=(0,y0), y0!=0. The second relative kernel component is

    s/(2pi) [1/(s^2+(eta-y0)^2)-1/(s^2+eta^2)]
      =s y0(2eta-y0)/[2pi(s^2+(eta-y0)^2)(s^2+eta^2)].   (5)

For large s>0 and eta in[s,2s], its absolute value is bounded below by c|y0|/s^2. Multiplying by |sin s| and integrating in eta proves that the absolute integral dominates a positive multiple of

    integral_large^infinity |sin s|/s ds,

which diverges by comparison with the harmonic series on fixed positive-fraction subintervals of each period. Nevertheless(1) converges to U(0,y0)-U(0,0)=0. This is a kinematic counterexample to absolute convergence, not a solution of the two profile transport equations. A compactly supported stream correction can adjust the center jets without changing this absolute-tail obstruction.

## Dependencies, provenance, and application limits

The argument independently extends lead `astra/auditJ/PROOF.md` partG from its axis-component formula to the full vector field, local differentiated convergence and regularization-shape independence. The only ingredients are the logarithmic fundamental solution, integration by parts, sublinear bounds, and elementary harmonic uniqueness. Packet03 had the more restrictive absolutely convergent power-decay setting; both statements remain valid in their respective scopes.

A proposed Omega by itself does not automatically produce a sublinear U: existence of such a velocity is a hypothesis in(1). A numerical finite-box solution does not meet that hypothesis merely because its boundary values are small. Candidate verification must still check the full-plane continuation and inverse, and an absolute observer convention must still be specified if absolute U(0) is reported. This theorem supplies no full B2 endpoint and no numerical certificate. No formalization is claimed.

External audit: actual claude-opus-5-5, review17, completed2026-10-20T15:36:18Z, confirmed the full-vector identity, differentiated convergence, cutoff extensions and conditional-convergence example. The B2 strain sign is derived explicitly in the center paragraph. Independent square-kernel quadrature evidence is in verification/sublinear_inverse_shear.json and does not replace the proof.
