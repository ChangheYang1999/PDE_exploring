# Canonical tail pressure, weak first correction and scalar helicity compatibility

Status: CONFIRMED at the exact hypotheses below by auditor A531, 2026-11-03T07:19:53.128901+00:00. The full coordinator referee comparison has been read and its precision repairs incorporated.

## 1. Exact statement

Let 2/5<c<1/2, omega be any finite real number, p=(1-c)/c in(1,3/2), q=2p+1, A=cI-omega J and L=(1-c)I+omega J, with J(x1,x2,x3)=(-x2,x1,0). Suppose U in C2(R3;R3), P in C1(R3) satisfy

    div U=0, LU+DU(Ax+U)+grad P=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1).       (1)

Let V,W be the actual A210 tails. Put Q_t=exp(omega tJ). Their precise properties needed here are

    U-V=o(r^-p), curl U-W=o(r^-p-1),
    V(exp(tA)x)=exp(-tL)V(x),
    W(exp(tA)x)=exp(-t)Q_t^T W(x),
    div V=div W=0, curl V=W distributionally.                (2)

The little-o statements are uniform at infinity. V and W are continuous on the punctured space. The natural derivative bound in(1) satisfies A210's exterior Dini premise, so these are consequences, not additional tail assumptions.

There is a constant Pinf such that, with Gamma=1/(4pi|x|),

    P2=D_ij Gamma*(V_iV_j),
    u_t(x)=exp((1-c)t)Q_t U(exp(tA)x),
    p_t(x)=exp(2(1-c)t)(P(exp(tA)x)-Pinf),
    z_t(x)=exp(t)(u_t(x)-V(x)),                              (3)

one has:

1. V is locally Lipschitz, P2 is C1 off zero, and p_t converges to P2 in C1 on compact subsets off zero.
2. z_t is locally uniformly bounded and converges weak-star in local Linfinity to Z=DV V+grad P2. The derivative DV here is weak. This gives neither pointwise convergence of z_t nor convergence of Du_t.
3. If U.curl U=0 everywhere, the locally Lipschitz scalar S=P2-|V|^2/2 satisfies div(SW)=0. Equivalently W.grad S=0 almost everywhere. It is constant along every C1 integral curve of continuous W on the punctured space, even if that curve is not unique.
4. Under the same zero-helicity premise, div(Z cross V)+2Z.W=0 in distributions.

P2 has twisted scalar homogeneity P2(exp(sA)x)=exp(-2(1-c)s)P2(x). All these statements also hold if the natural bounds(1) are replaced by U->0 uniformly and DU=O(sqrt r), using confirmed A498,A492,A476,A477. No conclusion here supplies a derivative bound from velocity decay alone. The main conjecture remains OPEN.

## 2. Pressure normalization and a bounded first remainder

A031 gives actual P equal to its canonical pressure plus a constant. For the decaying tensor F=U tensor U this canonical pressure has an absolutely convergent local/remote split. Write f=D_ij F_ij=tr((DU)^2). With a fixed smooth radial cutoff chi and d>0 set K_d=chi(./d)Gamma and H_d=Gamma-K_d. Then

    Pcan=K_d*f+D_ij H_d*F_ij,
    grad Pcan=grad K_d*f+D_ij grad H_d*F_ij.                  (4)

The first kernels are integrable and compactly supported. The second kernels vanish near their singularity and decay respectively as distance^-3 and distance^-4. Thus every integral in(4) is assigned to a region where it converges absolutely.

At |x|=R take d=R/8 after computing the gradient at fixed d. The local contribution is at most C R^2 R^(-2p-2) for P and C R R^(-2p-2) for its gradient. In the region |y|<=2R, the remote kernels are bounded by C R^-3 and C R^-4, while

    integral_(|y|<=2R) |U(y)|^2 dy <= C R^(3-2p).

Here 2p<3 is essential. Outside that region integrate C|y|^(-3-2p) or C|y|^(-4-2p). Since p>0, the resulting bounds are

    Pcan=O(r^-2p), grad P=O(r^-q).                           (5)

In particular Pcan tends to zero, fixing the name Pinf for the remaining constant. This does not infer normalization from Poisson alone.

For N=DU U+grad P, full momentum gives

    d/ds [exp(sL)U(exp(sA)x)]=-exp(sL)N(exp(sA)x).

The right side is bounded by C|x|^-q exp(-s), because (1-c)-cq=-1. The limit of the bracket is V(x) by(2). Therefore

    U(x)-V(x)=integral_0^infinity exp(sL)N(exp(sA)x)ds,
    |U(x)-V(x)|<=C|x|^-q.                                  (6)

This estimate is uniform in direction, without a differentiated remainder. Equation(6) gives the local uniform bound on z_t in(3).

## 3. Weighted tensor convergence and the pressure gradient

The full natural bounds imply for all t>=0 and x!=0

    |u_t(x)|<=C|x|^-p, |Du_t(x)|<=C|x|^-p-1.                 (7)

Indeed |exp(tA)x|=exp(ct)|x| and exp((1-c)t)=exp(cpt). On every fixed compact annulus the leading asymptotics give u_t->V uniformly, and(7) makes V locally Lipschitz. Its weak derivative has the corresponding bound. The tensors F_t=u_t tensor u_t converge locally uniformly off zero and in L1 on bounded sets including zero. The integrable majorant at zero is C|x|^-2p.

Define the distribution P2 by pairing the tensor with D_ij Gamma convolved with a smooth compactly supported test. The latter function is bounded near zero and O(|x|^-3) at infinity. The weighted product is integrable at both ends because 0<2p<3. Dominated convergence and covariance of the canonical pressure give

    p_t=D_ij Gamma*(F_t)_ij -> P2 in distributions on R3.     (8)

This includes the shrinking original core. It leaves no additional pressure contribution concentrated there. The same covariance proves the stated homogeneity of P2.

Here is an independent near/remote proof of C1 convergence that does not use convergence of Du_t. Fix a compact K off zero and choose a small d with the support of K_d about every point of K avoiding zero. The local sources f_t=tr((Du_t)^2) have a common Linfinity bound on that neighborhood. They converge distributionally to f_V=D_ij(V_iV_j); hence f_V has that same Linfinity bound. The identity f_V=tr((DV)^2) can also be obtained by mollifying the locally Lipschitz divergence-free V and passing its derivative products in finite local Lr spaces. No pointwise convergence of the sources f_t is required.

The scalar and gradient local terms in(4), formed with f_t or f_V, are bounded uniformly on K by C_K d^2 and C_K d, respectively. For each fixed d, the remote tensor terms and their gradients converge uniformly on K: the kernels are smooth and separated from the evaluation singularity, the tensor converges uniformly on compact annuli, the omitted region near zero is controlled by C_K epsilon^(3-2p), and the remote region at radius M by C_K M^-2p or C_K M^(-2p-1). These bounds are uniform in t. They justify uniform dominated convergence by first restricting y to a compact annulus and then removing that restriction.

Thus the scalar and gradient families p_t and grad p_t are uniformly Cauchy on K after an error at most C_K d. Let d tend to zero. Their uniform limits must be P2 and its distributional gradient by(8). The fundamental theorem of calculus on local line segments shows P2 is C1 and the convergence is C1loc. This is the same conclusion as LIT134's independent logarithmic equicontinuity proof. It proves neither C1 convergence of u_t nor convergence of a pressure Hessian.

## 4. The forced coefficient for twisted tails

Set

    n_t(x)=exp((2-c)t)Q_t N(exp(tA)x)
          =div F_t+grad p_t.                               (9)

It converges distributionally off zero to N2=DV V+grad P2. Estimate(7) and the scaled pressure bound give |n_t(x)|<=C|x|^-q on compact annuli. Consequently it converges weak-star locally in Linfinity: approximate any integrable compactly supported test by smooth tests and use the common bound. This argument does not assign pointwise values to the weak derivative DV.

Rescaling(6), and using commutativity of A,L and Q_t, yields

    z_t(x)=integral_0^infinity exp(sL)n_t(exp(sA)x)ds.        (10)

When paired with a compactly supported smooth test off zero, the absolute size of the integrand is bounded by C exp(-s), uniformly for large t. At fixed s its limit follows from(9) after the invertible linear change of variables exp(sA). Dominated convergence therefore passes(10) to the corresponding integral of N2.

The weak chain rule applied to the homogeneity of the locally Lipschitz V, and the already proved C1 homogeneity of P2, gives

    N2(exp(sA)x)=exp(-(2-c)s)Q_s^T N2(x)

for almost every x. Hence exp(sL)N2(exp(sA)x)=exp(-s)N2(x), and the limiting integral equals N2 itself. The uniform bound on z_t upgrades distributional convergence to local weak-star convergence, exactly as for n_t. This proves conclusion2 without axisymmetry, a smooth tail or a derivative remainder.

## 5. The direct exact helicity argument

Write Omega=curl U and h=U.Omega. The full momentum and vorticity equations imply

    B.grad U=-(1-c)U-omega JU-grad P,
    B.grad Omega=DU Omega-Omega-omega J Omega,
    B=Ax+U.

Taking the scalar products with Omega and U, respectively, and adding cancels the two skew terms. Since U.DU Omega=Omega.grad(|U|^2/2), this gives

    B.grad h=-(2-c)h-Omega.grad(P-|U|^2/2).                  (11)

Therefore global h=0 implies div((P-Pinf-|U|^2/2)Omega)=0. The scaled equation is

    div((p_t-|u_t|^2/2)curl u_t)=0.                         (12)

By(2), curl u_t->W uniformly on compact annuli. Section3 gives uniform convergence of p_t, and u_t->V uniformly. Thus the entire product in(12) converges uniformly on compact annuli. Passing to distributions gives div(SW)=0, where S=P2-|V|^2/2. As S is locally Lipschitz and W continuous and divergence-free, the product rule gives W.grad S=0 almost everywhere. This route uses only uniform scalar pressure convergence, not Section4's correction theorem or full gradient convergence.

To justify the claim for every W curve, let gamma be any C1 solution of gamma'=W(gamma) on a compact time interval whose image avoids zero. Choose delta>0 so that the closed delta-neighborhood of this compact image avoids zero and lies in a fixed bounded open set. On that neighborhood S has a finite Lipschitz constant C and W has a modulus of continuity m. Require epsilon<delta. A local mollification S_epsilon satisfies

    W(x).grad S_epsilon(x)
       =integral [W(x)-W(y)].grad S(y) phi_epsilon(x-y)dy,
    |W(x).grad S_epsilon(x)|<=C m(epsilon).

The first identity uses the almost-everywhere equation at y. Integrate the derivative of S_epsilon(gamma(t)) and let epsilon tend to zero. Uniform convergence of the mollification and m(epsilon)->0 prove constancy of S along gamma. No chain rule is imposed directly on an exceptional nondifferentiability set of S, and no uniqueness of the continuous vector field's integral curves is needed.

## 6. Independent check using the weak correction

The uniform convergence in(2) gives V.W=0. With epsilon=exp(-t), u_t=V+epsilon z_t, exact zero helicity becomes

    V.curl z_t+z_t.W+z_t.(curl u_t-W)=0.                    (13)

For each fixed t, z_t is locally Lipschitz because u_t is C2 and V is locally Lipschitz, so its curl and the products in (13) are defined almost everywhere. The final term tends uniformly to zero on compact annuli. The first two terms have the well-defined distributional form

    div(z_t cross V)+2z_t.W.

Pairing this with a smooth scalar test produces an integrable compactly supported coefficient of z_t. Section4's weak-star convergence therefore yields div(Z cross V)+2Z.W=0.

For completeness, if E=|V|^2/2 then

    Z=grad(P2+E)-V cross W,
    Z cross V=grad(P2+E) cross V-2E W.

The first uses the Lipschitz vector identity DV V=grad E-V cross W; the second uses V.W=0. Distributional product rules give

    div(Z cross V)+2Z.W=W.grad(P2-E).

They are justified by local mollification of the Lipschitz fields and strong convergence of their weak gradients in finite local Lr spaces. W is continuous; no classical derivative of W is taken. This agrees with the direct argument in Section5 and checks every sign in the compatibility.

## 7. Scope and remaining applications

This reconstruction confirms internally the general twisted-tail derivation of LIT134, including its assertion along every continuous-vorticity integral curve. The finite-dimensional obstruction for the particular A514 family is a separate application, reconstructed in the team records. Other tails satisfying the necessary scalar condition have not been classified. The first correction remains a weak coefficient; its value on a prescribed thin sheet or curve is not determined by the weak convergence alone.

The exact scalar identity(11) is already present in the team's exact-identity sources; it is not a new equation. The new use here is the justified passage to the singular homogeneous tail. The argument requires global zero helicity only for Sections5-6, and natural derivative decay for pressure compactness and the actual curl tail. No computational test was needed. The actual coordinator referee comparison in the team records has now been read in full; the model configuration is the primary model, without independent provider attestation.
