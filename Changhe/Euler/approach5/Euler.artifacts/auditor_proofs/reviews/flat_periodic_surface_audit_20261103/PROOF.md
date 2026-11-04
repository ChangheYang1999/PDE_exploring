# Local geometry and transport near a flat periodic carrier orbit

Status: A763-A767 CONFIRMED at the exact scopes below; the original algebraic step is REFUTED by A768, and the remaining stronger claims are OPEN in A769. No complete exclusion of a flat periodic witness is claimed.

## 1. Statement, spaces and dependencies

Let 0<c<1/2 and omega be finite and real. Let U in C2(R3;R3), P in C1(R3) solve

    div U=0, ((1-c)I+omega J)U+(DU)(Ay+U)+grad P=0,
    U.curl U=0, U(y)->0 uniformly,
    A=cI-omega J, J(y1,y2,y3)=(-y2,y1,0).

Write B=Ay+U, W=curl U, a=1-2c, kappa=1+c, V={W!=0},

    g=U.B, H=P+|U|^2/2+(Ay).U.

The identities used are

    grad H=B cross W-aU, BH=-ag, WH=0,
    [B,W]=-kappa W, div B=3c,
    dH wedge dg=0 on closure(V).                         (1)

The last identity is A413, not an assumed identity for all points outside the vortical closure. Momentum gives grad P in C1, hence P,H,g in C2. B has a complete C2 flow Phi because it is locally Lipschitz with linear growth. Its Cauchy law is

    W(Phi_t x)=e^(-kappa t) D Phi_t(x) W(x).              (2)

Assume Gamma is a nonconstant periodic B-orbit with period T, contained in closure(V), on which W=DW=0, U!=0 and g=0. Let H=H0 there. Assume the nonzero covector has the constant rate rho:

    U(Phi_t x)^T D Phi_t(x)=e^(rho t) U(x)^T,
    rho<=-2a or rho>=2-c.                                (3)

Its Floquet exponents are 0,rho,sigma, where sigma=3c-rho; the two transverse multipliers are positive and lie on opposite sides of one. The following already confirmed inputs are used at exactly this scope: the local unstable cylinder C^u is irrotational in both windows (A474); the local stable cylinder C^s is also irrotational in the upper window (A523). In the lower window W is tangent to C^s and each nearby intersection of C^s with an H-level is a loop (A474). The C2 stable and unstable cylinders and the local characterization by semiorbits staying near Gamma are part of these hyperbolic inputs.

There is a neighborhood N of Gamma with the following conclusions.

1. V intersect {g=0} intersect N is empty. No vortical W-line accumulates at Gamma. No vortical point has B alpha-limit set equal to Gamma, and in the upper window none has B omega-limit set equal to Gamma.
2. The closure of V meets C^u in the lower window, or C^s in the upper window, only on {g=0,H=H0}.
3. An orbit in that corresponding global cylinder and closure(V), with U nonzero along its entire length, stays on {g=0,H=H0}. In particular no such orbit is homoclinic to Gamma.
4. The exact strain, pressure and local stream identities in Sections2 and6 hold. The stream identity is local on transported level patches and includes an additive constant. It has no asserted exact constant exponential rate away from Gamma.

The hypotheses do not exclude vortical passages near Gamma or more complicated backward limit sets. No tail asymptotics, bounded gradient or density premise is used.

## 2. Exact derivatives and the repaired strain identity

Set S=DU on Gamma; it is symmetric and trace free. Differentiating (3) at time zero gives

    SB=(rho-c)U-omega JU-SU.                             (4)

Since B=Ay+U, the equivalent identity is

    S(Ay+2U)=(rho-c)U-omega JU.                          (5)

The source Section1(c) originally wrote S(Ay). That algebra is incorrect. Equations(4)-(5), not that displayed expression, are used below.

Direct differentiation of g gives

    grad g=DU^T B+DB^T U=rho U,
    grad H=-aU.                                         (6)

Thus both level surfaces are regular near Gamma. Their common tangent plane along Gamma is ker U^T. It contains B and the transverse Floquet direction of exponent sigma, since the covector in(3) annihilates the other two Floquet eigendirections. In particular this plane is tangent to C^u in the lower window and to C^s in the upper window. The identities BH=-ag and (6) give d(BH)=rho dH on Gamma. Also dg=rho U^flat on Gamma. Pulling back along the orbit and using(3) gives Phi_t^*dg=e^(rho t)dg there. Differentiating at zero yields

    d(Bg)=rho dg on Gamma.                              (7)

This uses the covector evolution and does not differentiate a pointwise equality in a transverse direction.

Momentum and(4) give

    grad P=SU-(a+rho)U,
    d/dt log|U|=rho-c-n.Sn, n=U/|U|.                    (8)

Consequently

    (1/T) integral_0^T n.Sn dt=rho-c.                   (9)

For the Frobenius norm, symmetric trace-free S obeys |S|^2>=(3/2)(n.Sn)^2: choose n as the first basis vector, minimize the sum of squares of the other diagonal entries subject to their sum being -n.Sn, and discard off-diagonal squares. Thus the period mean of |S| is at least sqrt(3/2)|rho-c|. In the lower window the mean in(9) is at most -(2-3c); in the upper window it is at least 2-2c. Only these bounds, not an interval bound on the actual mean in the lower window, are asserted.

Differentiating momentum along Gamma gives

    dS/dt+S^2+S+omega(JS-SJ)=-D^2P.                     (10)

Indeed its general matrix form is B(DU)+(DU)^2+DU+omega(J DU-DU J)=-D^2P. Along Gamma DU=S and its derivative along the orbit is dS/dt. Taking the trace gives Delta P=-|S|^2. Contracting(10) with n leaves the unknown quantity n.D^2P n; the trace gives no sign for this contraction. W=DW=0 also makes D2U fully symmetric, with vanishing traces obtained from div U=0; the order-two velocity jet is a harmonic-gradient jet.

On Gamma, U is normal to the regular H-level and U.B=0. Hence U=-(Ay)^normal and B=(Ay)^tangential, so

    |U|^2+|B|^2=|Ay|^2,
    P=H0+|U|^2/2,
    integral_0^T |B|^2 dt=-omega integral_Gamma (Jy).dy. (11)

For the last equality, |B|^2=Ay.B and the c y.B integral is zero over a closed orbit. The right side is minus twice omega times signed horizontal area. The established period restriction A030/A587 is consistent with(11); no new area or embeddedness premise is inferred.

## 3. No vortical zero-work point near the orbit

Let M={g=0} near Gamma, define N_g=grad g/|grad g|^2, and define the C1 field

    Y=B-(Bg)N_g.

It is tangent to M everywhere. On Gamma it equals B. For v tangent to M there, differentiating Y and using Bg=0 and(7) gives DY v=DB v. Therefore the return map of Y on a transversal in M has multiplier e^(sigma T). The positive multiplier also makes the local annular collar two-sided. In the lower window this is greater than one, so, after taking an annular neighborhood adapted to its return map, every backward Y-semiorbit stays in the collar and tends to Gamma. The upper window gives the corresponding forward statement. This follows by making the inverse return map, or return map respectively, a contraction on a short interval and saturating the interval between consecutive returns. Return times remain bounded and close to T.

At every point in V intersect M, (1) gives dg=l dH with the continuous coefficient

    l=(grad g.grad H)/|grad H|^2.

Hence Bg=l BH=-a l g=0 there, and Y=B. Suppose a Y-semiorbit in the contracting time direction starts at a vortical point of M. On its maximal vortical time interval it coincides with the B-semiorbit. It cannot cease to be vortical at a finite endpoint: the B-flow and its invertible derivative extend across that endpoint, and(2) preserves a nonzero W. Local uniqueness then continues equality of the two flows. Thus the entire semiorbit is a vortical B-semiorbit tending to Gamma.

In the lower window the local hyperbolic characterization places it on C^u; in the upper window it places it on C^s. Both relevant cylinders are irrotational by the explicit inputs in Section1. This contradiction proves conclusion1's first assertion.

The remaining assertions follow carefully. The commutator identity and WH=0 imply

    -a Wg=W(BH)=B(WH)+[W,B]H=0,

so g is constant on every maximal W-line, and H is also constant there. A vortical W-line with a point of Gamma in its closure therefore has g=0 and enters the forbidden neighborhood. No completeness of the W-flow is used. For clarity, with M0=sup|U| the radius obeys r' >= c r-M0. Every backward orbit is bounded. A forward orbit having Gamma as its omega-limit cannot cross a sufficiently large outward barrier, so it too is bounded. Thus a semiorbit with limit set exactly Gamma eventually stays in its local neighborhood. A vortical point with alpha-limit exactly Gamma therefore lies on the global unstable cylinder, which is irrotational by (2); the upper-window omega-limit assertion uses the stable cylinder. On each connected vortical B-segment inside N, g is continuous and nonzero, so H is strictly monotone. Also B and W are linearly independent there: W=fB with f nonzero would give 0=WH=-afg.

## 4. Trace of the vortical closure on the level-tangent cylinder

In the lower window let z belong to closure(V) intersect C^u intersect N. The backward B-semiorbit lies in that cylinder near Gamma and tends to Gamma. The set closure(V) is invariant because each Phi_t is a homeomorphism preserving V by(2). Along this semiorbit the rank identity extends by continuity and gives

    d/dt g(Phi_t z)=-a l(Phi_t z) g(Phi_t z),
    -a l(Phi_t z)->rho<0 as t->-infinity.              (12)

If g were nonzero at some sufficiently negative time, integrating(12) backward with coefficient at most rho/2 would force its absolute value to grow without bound. Continuity and approach to Gamma instead force g to zero. Therefore g vanishes identically along the local semiorbit. Then BH=-ag gives H=H0. The upper window has rho>0 and the same argument forward along C^s.

The two surfaces {g=0} and {H=H0} have the same tangent plane on Gamma. If the entire local level-tangent cylinder lies in closure(V), the preceding result puts it in both surfaces; their common dimension and local graph representations make the three surfaces agree after shrinking N. If only a relatively open piece of that cylinder is in closure(V), only that piece is certified. The function g+(rho/a)(H-H0) and its first derivative vanish on Gamma. On a local vortical coordinate patch, l stays near -rho/a and g is a strictly monotone local function of H. There is no assertion that every connected vortical component meets H=H0 or admits one global branch of that function.

## 5. Nonzero-velocity homoclinic exclusion

In the lower window consider an orbit in closure(V) intersect W^u(Gamma) on which U never vanishes. Its backward end lies in the neighborhood of Section4 and has g=0,H=H0. Its entire unstable cylinder is irrotational by(2). Hence grad H=-aU is nonzero along the entire orbit. The rank coefficient l is continuous there, so the scalar equation(12) propagates g=0 across every finite time interval. It follows that H=H0 for all time.

If the same orbit tended to Gamma forward, it would eventually lie in C^s intersect {H=H0}. Their tangent planes along Gamma are span(B,e_rho) and span(B,e_sigma); they are transverse. Their local intersection is consequently just Gamma after shrinking the neighborhood, by the implicit function theorem and compactness of Gamma. Uniqueness of the B-flow would make the whole orbit Gamma, a contradiction. In the upper window use C^s as the level-tangent cylinder and C^u at the opposite end; it too is irrotational. This proves conclusion3. If U vanishes at some point of the proposed connecting orbit, this argument gives no continuous coefficient l through that point. Such connections remain open.

## 6. Exact level stream functions and local transport

For regular H-levels Sigma_h in a sufficiently small product neighborhood of Gamma, set N_H=grad H/|grad H|^2, nu_h=i_(N_H)vol, and beta_h=i_W nu_h restricted to the level. These are C1 forms. In coordinates (h,z1,z2) write vol=m dh dz1 dz2. Since WH=0 and div W=0, differentiation in the two z variables shows d beta_h=0.

In the lower window, the circle ell_h=C^s intersect Sigma_h generates the annulus Sigma_h. W is tangent to both surfaces, hence to ell_h, so beta_h vanishes on the circle. Its period is zero, and every period on the annulus is zero. Therefore beta_h=d psi_h for a single-valued C2 function on the annulus, uniquely normalized by psi_h=0 on ell_h. In the upper window use ell_h=C^u intersect Sigma_h, which is transverse to the H-level and irrotational. The same conclusion follows. This proves zero flux through any generator loop, with its area density nu_h.

For transport, restrict to a local vortical bundle of connected level patches whose images stay in vortical coordinate patches. There dg=l dH implies g=G(H) locally. The level map h_t obeys h_t' in time=-aG(h_t); denote its derivative with respect to the initial level by D_h h_t. It is positive and equals exp(-a integral_0^t G'(h_s) ds). Branches can be continued along a specified compact flow segment; no global G on an arbitrary connected component is needed. On such a transported level patch,

    Phi_t^* beta_(h_t(h))=e^(-at)/(D_h h_t) beta_h.     (13)

To verify the factor, the pulled-back volume is e^(3ct)vol, the pulled-back vector W is e^(-kappa t)W by(2), and the pulled-back N_H has normal component N_H/(D_h h_t). Its tangential component contributes zero to the volume with two other level-tangent vectors. Since 3c-kappa=-a, (13) follows. Integrating along the connected level patch gives

    psi_(h_t(h)) o Phi_t
      =e^(-at)/(D_h h_t) psi_h+C(t,h).                 (14)

The additive constant need not vanish under the chosen annular normalizations: the argument does not establish that Phi_t maps the complete normalizing circle ell_h to a single circle ell_(h_t(h)). On portions of those circles outside closure(V), the rank identity is unavailable.

If the entire considered forward segment lies in a neighborhood where |-a l-rho|<=epsilon, its positive multiplier in(14) lies between e^((-a-rho-epsilon)t) and e^((-a-rho+epsilon)t). A corresponding bound holds with |t| for negative times. This is the precise near-orbit growth statement. Exact e^((-a-rho)t), or a bounded ratio to it on arbitrarily long segments, requires additional information on the integral of l+rho/a. Proximity to Gamma alone is insufficient.

## 7. Scope, corrections and open steps

The source's literal strain display is corrected by(5). Its exact pressure-gradient, mean-strain and Riccati conclusions survive. The local stream formula(14) and zero annular flux survive, but the unsupported global branch, normalization and exact exponential claims are not part of this theorem. The statement that a connected vortical component must cross H=H0 is not inferred from the rank identity.

The source's Section5 is explicitly heuristic and is not certified as a nonlinear passage theorem. Nor do the existing intrinsic countermodels, which omit some Euler equations, prove that every combination of the identities here is powerless. They demonstrate their own stated insufficiencies only. A general W2 exclusion, a normal pressure-Hessian sign, and connections through zeros of U remain open.

All arguments use exact differentiation, finite-dimensional hyperbolic inputs already audited, continuity, and one-dimensional integration. No numerical computation or formal build is used. The source is from the existing team; its originating consultation reports that its second model was unavailable. Continuing configured-model review is through working files, with no new model client and no claim of independent provider-runtime attestation.
