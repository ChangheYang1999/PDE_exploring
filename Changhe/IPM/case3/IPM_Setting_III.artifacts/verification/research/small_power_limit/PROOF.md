# The small-power limit, including zeros of the far-field trace

Verifier result 162. Independent proof written 2026-10-21 before supporting algebra checks. The external push1 analysis proposes these formulas; the actual Opus 5.5 lead review did not check this part. This proof supplies an independent check and makes the limiting arguments explicit.

## Exact statement and scope

Assume rho is an exact primary Setting III profile: it is real and smooth on the full plane, even in x and odd in y, a=rho_y(0) is nonzero, ell>1, W=ell X+U and W.grad rho=rho. U is the canonical divergence-free velocity and has the induced parities. Write p=1/ell, delta=1-p and k=psi_xy(0). The previously audited full-class far-field theorem gives a smooth nonzero trace Theta, convergence r^(-p)rho -> Theta, and |U|+r|grad U|=O(r^p). These are consequences of the primary hypotheses, not extra assumptions on an exact primary profile.

Let Z={X:rho(X)=0}, let z be the angular Lebesgue measure of {theta:Theta(theta)=0}, and fix p<lambda<1. For beta>0, set alpha_beta=-2-lambda beta and

    M_beta=integral r^alpha_beta |rho|^beta dX,
    V_beta=integral r^(alpha_beta-2)(U.X)|rho|^beta dX.

These integrals converge absolutely by the power-weight strip. Then

    lim_(beta downarrow 0) beta M_beta
       =2pi/(1-lambda)+(2pi-z)/(lambda-p),                         (1)
    lim_(beta downarrow 0) V_beta
       =pi k/(1-lambda)+ell z/2.                                  (2)

The circular principal value integral of r^(-4)(U.X) is zero independently of k. The zero-set correction satisfies the absolutely convergent identity

    -2 integral_Z r^(-4)(U.X)dX=ell z.                             (3)

Combining (1), (2) with the power-weight transport identity yields precisely k=1-ell. It gives no additional exclusion. In particular, nonzero smooth Theta alone does not imply z=0. Whether all actual profiles have a null zero set remains outside this proof.

## 1. Exact scattering representation, including zero values

For r at least a sufficiently large R_0, ell r+U_r is positive. Parametrize an outward characteristic by its radius s, starting at (r,theta). Its angular equation is

    d theta(s)/ds=U_theta(s,theta(s))/[s(ell s+U_r(s,theta(s)))].     (4)

The right side and its first angular derivative are O(s^(p-2)). They are integrable to infinity. Standard scalar ODE existence and the differentiated flow equation therefore show that the limiting angle H_r(theta) is an orientation-preserving circle diffeomorphism. In lifted coordinates H_r(theta)-theta=O(r^(-delta)) and H_r'=1+O(r^(-delta)), uniformly in theta. The inverse has the same derivative estimate. This follows directly by integrating the angular field and its variational equation, not by assuming convergence of its zero sets.

For q(s)=s^(-p)rho(s,theta(s)), the exact transport equation gives

    q'(s)=c(s,theta(s))q(s),
    c(s,theta)=1/(ell s+U_r(s,theta))-p/s
              =-p U_r(s,theta)/[s(ell s+U_r(s,theta))].            (5)

Here c and its angular derivative are also O(s^(p-2)). Integrating the scalar linear equation, including the solution q=0, and using the far-field trace gives the exact formula

    r^(-p)rho(r,theta)=b_r(theta)Theta(H_r(theta)),
    b_r(theta)=exp[-integral_r^infinity c(s,theta(s))ds]>0,
    b_r=1+O(r^(-delta)).                                          (6)

Thus zeros of rho on every sufficiently large circle are exactly the preimages of zeros of Theta. For any fixed small beta_0>0, changing angular variable in (6) gives uniformly for 0<beta<=beta_0

    G_beta(r):=integral |r^(-p)rho|^beta dtheta
              = S_Theta(beta)+O(r^(-delta))S_Theta(beta),
    S_Theta(beta)=integral |Theta|^beta dtheta.                    (7)

The bound follows from b_r^beta=1+O(r^(-delta)) and the inverse Jacobian estimate; its constant is uniform in beta. Since Theta is bounded, S_Theta(beta) is uniformly bounded and tends by dominated convergence to 2pi-z. The same change of variables, now for the indicator of the zero set, gives its angular measure z_r=z+O(r^(-delta)). No pointwise lower bound for Theta is used.

## 2. The mass limit

Near zero, parity and smoothness give rho=y F(x,y), with F=a+O(r^2). Choose a fixed r_0>0 on which |F| is bounded above and away from zero. Uniformly in small positive beta,

    ||F|^beta-|a|^beta|<=C beta r^2.                              (8)

This is the mean-value theorem for t^beta on a fixed positive compact interval. Therefore the inner mass has principal term

    |a|^beta S_beta r_0^(beta(1-lambda))/[beta(1-lambda)],
    S_beta=integral |sin(theta)|^beta dtheta,

and an error O(beta). Multiplying by beta and using S_beta -> 2pi gives the first term of (1). Any fixed middle annulus contributes a bounded M_beta, hence zero after multiplication by beta.

For r>=R>=R_0, equations (6)-(7) show that the outer mass, multiplied by beta, is

    beta integral_R^infinity r^(-1-beta(lambda-p))G_beta(r)dr
      = S_Theta(beta)R^(-beta(lambda-p))/(lambda-p)+O(beta).

The error is bounded by a constant times beta integral_R^infinity r^(-1-delta-beta(lambda-p))dr. The main term tends to (2pi-z)/(lambda-p). Adding the three regions proves (1). Merely knowing rho/r^p -> Theta, without the exact multiplicative scattering formula, would not justify this step at a zero arc of Theta.

## 3. The zero-set flux

The circular cancellation is exact. Incompressibility and smoothness on a disc give integral U_r(r,theta)dtheta=0, so integral U.X dtheta=0 at every r>0. Thus every annular integral of r^(-4)(U.X) vanishes and its circular principal value is zero.

The characteristic invariance of Z also has a direct distributional proof. Set chi_epsilon=exp(-rho^2/epsilon^2). The profile equation gives

    W.grad chi_epsilon=-2(rho^2/epsilon^2)exp(-rho^2/epsilon^2).

The right side is bounded by 2/e and tends pointwise to zero, including where rho=0. On each compact set, chi_epsilon -> 1_Z and dominated convergence in the weak derivative identity yields W.grad 1_Z=0 distributionally. Product differentiation away from zero gives

    div(W r^(-2)1_Z)=-2r^(-4)(U.X)1_Z.                            (9)

The zero set near zero is just y=0 because F is nonzero, so it has zero planar measure there. The right side of (9) is absolutely integrable: it vanishes almost everywhere in that small disc, and at infinity its radial absolute bound is O(r^(p-2)). On a large circle its radial flux is

    F_Z(R)=integral (ell+U_r(R,theta)/R)1_{rho(R,theta)=0}dtheta.

Using (6), its zero set has measure z+O(R^(-delta)), and U_r/R=O(R^(-delta)). Hence F_Z(R) -> ell z. Applying (9) first with radial cutoffs supported away from zero and then taking the two limits gives (3). Equivalently the annular identity holds for almost every radius; at large radii (6) represents its boundary integral on a fixed measurable angular zero set with smooth bounded weights, so the same limit follows. No smoothness of the boundary of Z is required.

## 4. The singular velocity-weight limit

Parity gives U.X=-k r^2 cos(2theta)+D(r,theta), with D=O(r^4). Its angular average is zero for every r, since both U.X and cos(2theta) have zero angular average. The exact angular identity

    integral cos(2theta)|sin(theta)|^beta dtheta
      =-beta S_beta/(beta+2)                                     (10)

follows by integrating the derivative of cos(theta)sin(theta)^(beta+1) on (0,pi), then reflecting. The leading part of V_beta on r<r_0 is consequently

    k |a|^beta S_beta r_0^(beta(1-lambda))/[(beta+2)(1-lambda)],

which tends to pi k/(1-lambda). The error in replacing |F|^beta by |a|^beta contributes O(beta) by (8) and the extra r^2. The D term is dominated by an integrable O(r) radial function for small beta. Away from the null axis its integrand tends to r^(-4)D, whose angular average is zero. Dominated convergence thus makes its full inner integral tend to zero.

For r>=r_0 the integrand of V_beta is dominated uniformly by an integrable function. Indeed r^(-lambda beta)|rho|^beta is bounded on the compact part and bounded by C r^(-beta(lambda-p)) at infinity; r^(-4)|U.X| has radial bound O(r^(p-2)). Pointwise the density factor tends to 1_{rho!=0}, not necessarily to one. Hence the outer limit is

    integral_(r>=r_0, rho!=0) r^(-4)(U.X)dX
       =-integral_Z r^(-4)(U.X)dX=ell z/2,

where circular cancellation and (3) were used. Together with the inner limit this proves (2).

## 5. What the limit does and does not imply

The already proved power-weight identity is

    V_beta=beta(1-ell lambda)M_beta/(2+lambda beta).

Using (1), its limit is

    -pi(ell-1)/(1-lambda)+ell z/2.

Comparing with (2) yields k=1-ell; the z terms cancel exactly. This is the center relation already obtained by differentiating the PDE at the origin. The circular principal value alone is identically zero and places no restriction on k. The formulas remain valid when z>0 and do not prove or assume that such a trace is realized by an actual profile. A smooth nonzero angular function may vanish on an interval, so dropping z from the formulas needs an additional argument about actual profiles.

Dependencies: the primary far-field regularity theorem; elementary scalar ODE flow and variational equations; the power-weight identity with its zero-set regularization; divergence theorem and dominated convergence. All were either proved explicitly here where needed or independently audited previously. Supporting exact algebra is separate from the improper-integral proof. Verdict: the proposed small-beta formulas are CONFIRMED under the exact primary hypotheses. Actual Opus 5.5 review of this part is requested separately. No primary endpoint follows.
