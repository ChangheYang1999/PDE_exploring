# Stress, action and moment tests for the critical-tail reconstruction

## Part I. Real rotating homogeneous Beltrami fields

Let J y=e3 cross y, beta be real, Q_l=exp(-beta J log l), and 1<eta<2. Let V be real and C2 on R3 minus the origin, with div V=0,

    V(l Q_l y)=l^(-eta) Q_l V(y),  l>0,
    V cross curl V=0.

Then V=0. The statement holds for every finite beta and does not require regularity at the origin.

Set T=V tensor V-|V|^2 I/2. The hypotheses give div T=0. For n=y/|y|, grad n=(I-n tensor n)/|y|, so

    div(Tn)=(trace T-T_nn)/|y|=-|V dot n|^2/|y|.

Let A(r) and C(r) be the integrals over the unit sphere of the squared radial and tangential components of V(r theta), respectively. Integration on an annulus, followed by differentiation of its outer radius, gives

    d/dr [r^2(A(r)-C(r))/2]=-r A(r).

Rotation covariance preserves spherical measure and normal vectors. Therefore A(r)=r^(-2eta)A(1), C(r)=r^(-2eta)C(1), and substitution yields

    (2-eta) A(1)+(eta-1) C(1)=0.

Both coefficients are positive. Since these are real nonnegative squares, V vanishes on S2 and then everywhere by scaling. At eta=1 or eta=2 the proof does not establish the same conclusion. For complex bilinear squares positivity is absent.

## Part II. Precise reconstruction setting

Fix 2/5<c<1/2, arbitrary finite omega, A0=cI-omega J, a=1-2c and gamma=1/c in (2,5/2). Assume the smooth fields U0,W and their Biot-Savart reconstruction V satisfy all conclusions of A179:

    U0 compactly supported, div U0=div W=0, W nonzero,
    B0=A0 y+U0, [B0,W]=-(1+c)W,
    div V=0, curl V=W,
    D^j W=O(r^(-gamma-j)), D^j V=O(r^(1-gamma-j)),
    W=Wh outside a ball, D^j(V-Vh)=O(r^(-3-j)),
    E_V(R)=C_h R^alpha+C_def+O(R^(1-gamma)),
    alpha=5-2gamma in (0,1), C_h>0.

Here Wh and the nonzero Vh have exact rotating homogeneity, with curl Vh=Wh and Vh of degree 1-gamma. The complete W-flow and all smoothness assertions are part of A179. The missing equation is

    [V-U0,W]=0.                                             (R)

It is not assumed unless stated explicitly below.

## Part III. A primitive and automatically vanishing helicity

The old bracket law gives curl(B0 cross W)=aW. Hence V-(B0 cross W)/a is a globally curl-free smooth field on simply connected R3. It equals grad g for a smooth scalar g.

Its decay is O(r^(1-gamma)), an integrable radial power since gamma>2. Radial integration gives a finite limit of g along each ray and a remainder O(r^(2-gamma)). The oscillation of g on S_r is at most pi r times the supremum of |grad g| there, hence tends to zero. The radial limits coincide. Normalize this common limit to zero; then g=O(r^(2-gamma)).

Dotting with W gives V dot W=W dot grad g=div(gW). The integrand is O(r^(1-2gamma)), absolutely integrable in dimension three because gamma>2. Its integral over B_R equals the flux of gW, of size O(R^(4-2gamma)), which tends to zero. Therefore total helicity is zero before (R) is solved.

For any compactly supported invariant probability of the complete W-flow, integrate the finite-time identity for g. Invariance gives mean W.grad g=0, hence mean V dot W=0. Also V has zero circulation along every closed orbit of the OLD carrier B0: its cross-product part annihilates B0 and the remaining one-form is exact. This does not identify old and new carrier trajectories.

## Part IV. Consequences conditional on the missing equation

Assume (R), and put D=V-U0. Since D and W are divergence free,

    curl(D cross W)=-[D,W]=0.

Thus D cross W=grad F globally. Outside the support of U0, grad F=V cross W=O(r^(1-2gamma)). The same radial-limit and spherical-oscillation argument normalizes F to zero at infinity and gives F=O(r^(2-2gamma)). Since W.grad F=0, every full W-orbit starting where F is nonzero lies in a compact level set of F. The set {F!=0} is open.

This open set is nonempty arbitrarily far out. Otherwise F would vanish throughout some exterior, making V cross W=0 there. Since W=Wh and V=Vh+O(r^-3),

    Vh cross Wh=O(r^(-gamma-3)).

The left side has exact rotating degree 1-2gamma. Scale a fixed point by l Q_l, multiply by l^(2gamma-1), and undo the rotation. The right side becomes O(l^(gamma-4)), tending to zero. Thus Vh cross Wh=0 on the punctured space. Part I applies with eta=gamma-1 in (1,3/2), forcing Vh=0, a contradiction.

Consequently (R) requires a nonempty open set, indeed such a set at arbitrarily large radii, of bounded complete W-orbits. If the chosen independent model has almost every W-orbit unbounded, (R) is impossible. This last unboundedness property has NOT been established for A121. Recurrence alone does not decide it.

Equation (R) also implies that V is a smooth decaying Euler profile: its momentum residual has zero curl and therefore a global pressure potential. By the audited energy theorem A052-A053,

    E_V(R)=L R^alpha+O(R^(alpha-1)).

Comparing with the stated reconstruction expansion first gives L=C_h and then C_def=0. No sign or nonzero value for C_def has been established.

Finally grad F=D cross W is absolutely integrable, and its integral over B_R is the flux of F times the outward normal, of size O(R^(4-2gamma)). Therefore integral D cross W=0. Independently,

    V cross W=grad(|V|^2/2)-div(V tensor V),

whose stress flux also tends to zero at rate O(R^(4-2gamma)). Both integrands are absolutely integrable. Subtracting gives the necessary compact vector moment

    integral_R3 U0 cross W=0.

Neither vanishing nor nonvanishing of this moment for the existing construction is asserted.

## Part V. At most one nonzero amplitude

For fixed U0,W,V, the vorticity residual of lambda V is

    [A0 y+lambda V,lambda W]+(1+c)lambda W
      =lambda(lambda[V,W]-[U0,W]).

For nonzero lambda it vanishes exactly when [lambda V-U0,W]=0. If two distinct nonzero real amplitudes satisfied this, subtraction would give [V,W]=0 and [U0,W]=0. The old bracket law would reduce to [A0 y,W]=-(1+c)W throughout R3. Its linear-flow solution is

    W(exp(A0 t)y)=exp(-t)exp(-omega Jt)W(y).

As t tends to minus infinity, exp(A0 t)y tends to zero, so the left side is bounded by smoothness at zero. The right side has norm exp(-t)|W(y)|. Thus W=0, contrary to hypothesis. At most one nonzero amplitude works; no such amplitude has been produced.

The energy constant scales by lambda^2, and the compact moment test by lambda, so a nonzero amplitude cannot repair failure of either test.

## Verification and scope

Parts I and IV's bounded-orbit test verify LIT37. Parts III, IV's energy and moment tests, and V verify LIT38. Verdicts A191 and A192 are CONFIRMED with their conditional hypotheses. Beltrami alignment is stronger than the leading steady-curl condition [Vh,curl Vh]=0 and must not replace it. These tests do not prove a full profile exists or rule out all reconstructions.
