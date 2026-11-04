# A genuine local irrotational-vortical tail interface

Status: CONFIRMED at A617. Exact hypotheses, proof and limitations are stated below. Informal independent verification; no formal build or numerical proof is claimed.

## 1. Statement and notation

Fix 2/5<c<1/2 and any finite omega. Define

    p=(1-c)/c, d=p-1, sigma=1-d, a=1-2c=cd,
    beta=d/(2p), q=1/beta=2p/d, A=cI-omega J,
    J(x1,x2,x3)=(-x2,x1,0).

Then 0<d<1/2 and sigma>0. There are delta>0, a locally C1,1 vector field V and locally C2,1 scalar P2 on the cone

    D_delta={x: r=|x|>0, |z|<delta}, z=x3/r,

with the following properties. They are axisymmetric and V has no azimuthal component. Their degrees are -p and -2p, respectively, so their ordinary homogeneities give the required twisted homogeneities for every omega. With the ACTUAL W=curl V, k=(Ax).V and S=P2-|V|^2/2 they satisfy pointwise on D_delta

    div V=0, V.W=0, -Delta P2=tr((DV)^2),
    W.grad S=0,
    grad k cross grad S=0 wherever W!=0.

The scalar S is negative everywhere after decreasing delta, and |S|^beta is locally A2. The open negative-z side is irrotational; the open positive-z side is vortical. Across z=0, V and all its first derivatives match, P2 and all its derivatives of order at most two match, and the value and first normal derivative of the harmonic irrotational-side scalars k and Pi=P2+|V|^2/2 are supplied by the actual vortical side. Rank still fails everywhere on the sufficiently small negative-z side. The velocity is not C2 across the interface.

This refutes the local inference of global rank from those equations, the known tail regularity, a positive weight and those interface traces. It supplies no global angular continuation or canonical pressure. The positive-side full momentum residual is explicitly nonzero.

## 2. Representation, actual curl and exact pressure equation

Use the spherical orthonormal frame (er,e_theta,e_phi), with z=cos(theta) and w=1-z^2. For a function f(z) put

    R=f'/sigma, T=f/sqrt(w),
    V=r^-p(R er+T e_theta).

The divergence is r^(-p-1)[(2-p)R-(sqrt(w)T)']=0. The actual velocity derivative, whose columns are derivative directions and rows are output components, is r^(-p-1) times

    M=[[-pR, -sqrt(w)f''/sigma-T, 0],
       [-pT, dR-zf/w,            0],
       [0,   0,                  R+zf/w]].

For example, the second column follows by differentiating both scalar components and the spherical basis: its first entry is partial_theta R-T and its second is partial_theta T+R. The third diagonal entry is R+cot(theta)T. Their sum with -pR is0 because p=d+1.

Consequently

    W=r^(-p-1)eta e_phi,
    eta=M_(theta,r)-M_(r,theta)
       =[w f''-d sigma f]/[sigma sqrt(w)].

This gives helicity zero and W.grad S=0 for every axisymmetric S. Since Jx is azimuthal, k=c r^-d R. The linear Lamb identity Ax cross W=aV+grad k also follows directly from homogeneity and rotational equivariance, so no omitted linear tail equation is needed.

For P2=r^-2p Q(z), the exact Poisson equation is

    (wQ')'+lambda Q+T_f=0, lambda=2p(2p-1),

where

    T_f=2(d^2+d+1)(f')^2/sigma^2
         +2zff'/w+2z^2 f^2/w^2
         +2pff''/sigma+2pf^2/w.

Indeed the coefficient of R^2 in tr(M^2) is p^2+d^2+1=2(d^2+d+1). The mixed diagonal terms add to 2(1-d)Rzf/w=2zff'/w. The remaining diagonal terms are 2z^2f^2/w^2. The two off-diagonal products are 2pff''/sigma+2pf^2/w. These are all entries of the trace; it is not replaced by the Frobenius norm. The spherical Laplacian supplies (wQ')'+lambda Q. This proves the pressure reduction exactly.

## 3. Analytic branches and their jets

On the negative side take the analytic solution

    w f_minus''=d sigma f_minus,
    f_minus(0)=0, f_minus'(0)=sigma.

A regular analytic linear ODE gives its existence and uniqueness. The solution is odd. Set e=[(f')^2/sigma^2+f^2/w]/2 and Q_minus=-e_minus. Then eta=0, and V is divergence free and curl free, hence harmonic componentwise. Thus -Delta P2=Delta(|V|^2/2)=tr((DV)^2). All full momentum terms cancel here: the linear terms vanish by degree and equivariance, while DV V=grad(|V|^2/2).

Its jets are

    f_minus''(0)=0, f_minus'''(0)=d sigma^2,
    Q_minus(0)=-1/2, Q_minus'(0)=0,
    Q_minus''(0)=-sigma.

The last equation follows from e''(0)=f'''(0)/sigma+sigma^2=d sigma+sigma^2=sigma. Equivalently let K be the convergent even harmonic function of A607 with K(0)=1 and (wK')'+d(d-1)K=0. Then

    R_minus=K, f_minus=wK'/d,
    k_minus=c r^-d K.

In particular this is the exact harmonic cone already checked, at a different nonzero normalization.

For the positive side impose, where f'>0,

    h=-(f'/sigma)^q, e=[(f')^2/sigma^2+f^2/w]/2,
    Q=h+e.

Then S=r^-2p h=-(k/c)^q because dq=2p and k/c=r^-d f'/sigma>0. Hence the scalar rank equation holds on this whole branch. Substitute this Q into the exact Poisson equation. The coefficient of f''' is

    w [f'/sigma^2-(q/sigma)(f'/sigma)^(q-1)].

At the initial data f(0)=0, f'(0)=sigma, f''(0)=0 it is (1-q)/sigma!=0. The equation can therefore be solved for f''' as a real analytic function of (z,f,f',f'') near those data. The fractional power has a single holomorphic branch near f'/sigma=1. On a sufficiently small complex polydisk the normal form and its first derivatives are bounded; the integral Picard operator on a small complex disk is a contraction preserving a closed sup-norm ball. Its holomorphic iterates converge uniformly, and their limit solves the integral equation. Differentiation gives the ODE, and reality follows from uniqueness. This verifies convergent analytic existence, not just compatible formal jets.

At zero the Poisson equation becomes

    (1-q) f_plus'''(0)/sigma+sigma^2
       -lambda/2+2(d^2+d+1)=0.

The constant part is sigma(2-d), and q-1=(d+2)/d. Therefore

    f_plus'''(0)=d sigma^2(2-d)/(d+2),
    eta_plus'(0)=f_plus'''(0)/sigma-d sigma
                 =-2d^2 sigma/(d+2)<0.

After shrinking delta, f_plus'>0 and eta_plus!=0 for 0<z<delta. This is an actual open vortical side.

## 4. Interface regularity, pressure and Cauchy traces

Join f_minus to f_plus at zero. Their derivatives through order two agree. Their one-sided third derivatives are bounded up to zero, so f is C2,1. The representation of V then gives V in C1,1 in smooth Cartesian charts on the cone. Its curl is continuous and Lipschitz, with eta=0 on z<=0. No vortex-sheet distribution is present.

Join Q_minus to Q_plus. Both have value -1/2 and first derivative0 at zero. The Poisson equation fixes the second derivative from the common f,f',f'' data:

    Q''(0)=lambda/2-2(d^2+d+1)=d-1=-sigma.

Thus Q is C2,1, and P2 is C2,1 on the cone. All Cartesian derivatives through order two match because the changes of variables are smooth there. The source tr((DV)^2) is continuous and the Poisson equation holds at zero by continuity, without a surface source.

The scalar S is -2e_minus on the negative side and h on the positive side. Its common value is -1 and its common first z-derivative is0. It is C1,1 and remains negative nearby. On every sufficiently small closed ball in the cone, both b=|S|^beta and b^-1 are bounded, proving local A2 by the product-of-averages definition.

For Pi=P2+|V|^2/2 the actual negative-side values are identically0, whereas on the positive side Pi=r^-2p(h+2e). At the interface the two traces are

    k=c r^-d, partial_z k=0,
    Pi=0, partial_z Pi=0.

At z=0 the physical unit normal derivative is r^-1 partial_z; the radial derivatives of the displayed values and all azimuthal derivatives are also fixed. Thus these really are the Dirichlet and first normal-derivative traces of the harmonic scalars. They are supplied by a constructed vortical branch. They do not include unspecified higher derivatives. In particular Pi need only be C1,1, since V is only C1,1 even though P2 is C2,1.

The velocity is genuinely not C2. Its radial amplitude has the jump

    R_plus''(0)-R_minus''(0)=-2d^2 sigma/(d+2)!=0.

At a fixed positive r, the other terms in a second angular derivative of V use the common lower jets. Thus its radial component has this nonzero jump. Smooth or analytic continuation through the interface is not available at this regularity.

## 5. Failure of rank on the irrotational side

Put M0=d^2 K^2+w(K')^2. On the negative side,

    k=c r^-d K, S=-d^-2 r^-2p M0.

Writing n=x/r and t_z=e3-zn gives

    grad k cross grad S
       =(c/d^2)r^(-d-2p-2)
          [dK M0'-2pK'M0](n cross t_z).

The harmonic equation gives K'=d sigma z+O(z^3), M0'=2d KK'+2z(K')^2. Hence

    dK M0'-2pK'M0=-2d^4 sigma z+O(z^3).

This is nonzero for every sufficiently small negative z and tends to0 on the interface, consistently with C1 scalar regularity. Rank is identically0 on the vortical positive side by the exact relation S=-(k/c)^q. Thus the local equations and the matched first harmonic Cauchy traces do not propagate rank into the irrotational region.

## 6. The nonzero full momentum residual and global limitations

Every linear similarity term of this homogeneous equivariant V cancels, for every omega. Write Pi=r^-2p B(z), with B=h+2e on the positive side. The Lamb formula DV V=grad(|V|^2/2)-V cross W gives the radial full momentum residual

    (DV V+grad P2).er=r^(-2p-1)[-2pB-T eta].

At zero B=B'=0 and

    B''=Q''+e''=-sigma+f_plus'''/sigma+sigma^2
       =f_plus'''/sigma-d sigma=eta_plus'(0).

Consequently B=(eta_plus'(0)/2)z^2+O(z^3), T=sigma z+O(z^3), and eta=eta_plus'(0)z+O(z^2). Since p+sigma=2,

    -2pB-T eta=-2 eta_plus'(0)z^2+O(z^3)
              =[4d^2 sigma/(d+2)]z^2+O(z^3).

It is nonzero on the sufficiently small positive side. The example is therefore explicitly not a full profile on its whole domain. For an actual tail A531 and A539 identify this residual with its first velocity correction Z=DV V+grad P2. The additional identity div(Z cross V)+2Z.W=0 is equivalent to W.grad S=0 and holds here. Thus the nonzero residual excludes treating V itself as a full profile, but does not exclude its leading-tail realization.

No poles, origin, whole-sphere flux or global canonical pressure are supplied. A global swirl-free axisymmetric completion is already excluded by A561 through pole continuity and vortical rank; the broader canonical-pressure result A569 is also available. Nor does it establish that an actual tail can contain such an interface. It proves that the listed local equations, current tail regularity, positive local A2 weight and the stated genuine interface traces are insufficient for the proposed rank-continuation shortcut.

The complete source, its eight exact symbolic checks and its output were read; each relevant algebraic identity and jet has also been rederived above by hand. The symbolic checks are corroboration, not analytic existence or a global proof. No computation was rerun in this agent. The actual configured-model focused comparison in the team records was fully read on 2026-11-03. It agrees with A617 and supplies the preceding citation clarifications. It also reports a FORMAL higher-order rank failure at two sampled parameters, with an approximate series residual. That observation is not an independently certified identity or a proved necessary actual-tail expansion. Stronger local consequences of the full profile could still exclude this example. No new model client or computation was used by this agent.


## 7. Subsequent exact next-order audit

A647-A648 establish the next actual scalar tau=p1-2V.gradP2 without assuming a differentiated correction limit, for the global helicity-free natural class and c!=3/7. A650 then proves an exact all-parameter local incompatibility for this specified positive-side pair: no candidate p1 satisfies both its next Poisson equation and scalar rank. Thus it cannot be the actual local leading pair under that nonresonant global scope, even if the global tail is nonaxisymmetric elsewhere. The local incompatibility also holds at d1/3, but its actual-tail consequence at c3/7 is not proved. The five leading-equation construction and the limited countertest in Sections1-6 remain valid. See in the team records for the complete new argument.
