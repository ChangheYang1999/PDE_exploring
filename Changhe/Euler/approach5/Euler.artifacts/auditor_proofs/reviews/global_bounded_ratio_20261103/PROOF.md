# Global rigidity with a bounded scalar ratio

## 1. Exact theorem and scope

Let D=R3 minus {0}, Jx=e3 cross x, 0<c<1/2, omega any finite real number, A=cI-omega J and X(x)=Ax. Suppose V:D->R3 and S:D->R are smooth and satisfy

    div V=0, DV X=-((1-c)I+omega J)V,
    X.grad S=-2(1-c)S, X.V=0, (curl V).grad S=0.       (1)

Suppose fixed constants 0<r_-<=r_+<infinity satisfy

    r_-|S|<=|V|^2<=r_+|S|                              (2)

on the unit sphere. Then V=S=0 on D. In the target interval 2/5<c<1/2 the same conclusion holds for V in C2(D) and S in C3(D), with the equations interpreted classically.

The scalar can change sign and its zero set is unrestricted. The assertion uses neither a pressure equation nor bounds on derivatives of the ratio. It is global on the punctured space. It does not establish local unique continuation from a flat point under local ratio bounds, and it does not derive (1) or (2) from bare velocity decay.

Put a=1-2c, b=2-2c, eta=a/b, rho=1/2-eta=c/(2(1-c)), gamma=2rho and m=1/c. These numbers satisfy 0<rho<1/2, 0<gamma<1 and m>2. Write E=|V|^2 and W=curl V.

## 2. Scaling and the normalized form across all zeros

The explicit flow F_t(x)=exp(tA)x exists for every real t, has |F_t(x)|=exp(ct)|x| and meets the unit sphere once. Integrating (1) gives

    V(F_t x)=exp(-(1-c)t)exp(-omega tJ)V(x),
    S(F_t x)=exp(-bt)S(x).

Thus (2) holds throughout D, since E has the same scaling as |S|. In particular their zero sets coincide.

Define beta=|S|^(-eta)V where S!=0 and beta=0 otherwise. We verify the distributional extension, not just its pointwise continuity. The scalar-root input is Ghisi-Gobbino, arXiv1107.2694v2 Theorem2.3, with the source qualification already checked in A1541 and the removal lemma checked in A1748. If f is smooth and 0<theta<1, then |f|^theta has local W1,t regularity for t<1/(1-theta). The finite regularity sufficient for this fact is C^(k,alpha) with k+alpha=1/theta.

Let H_S=|S|^(rho-1)|DS| and H_i=|V_i|^(gamma-1)|DV_i| off the respective zero sets, with value zero on them. The root theorem and Sobolev level-set property give H_S in local L^t for t<1/(1-rho) and H_i in local L^t for t<1/(1-gamma). For epsilon>0 use beta_e=(S^2+epsilon^2)^(-eta/2)V. The upper comparison gives almost everywhere

    |D beta_e| <= |S|^(-eta)|DV|
                  +eta |S|^(-eta-1)|V||DS|
                <= C sum_i H_i+C H_S.                   (3)

For the first bound, |S|^(-eta)<=r_+^eta |V|^(-2eta) and |V|^(-2eta)<=|V_i|^(-2eta) on V_i!=0. On a component zero set its classical derivative is zero almost everywhere. On S=0, V=0 and DV=0 almost everywhere, and the other regularized derivative contains S. The second term in (3) uses |V|<=sqrt(r_+)|S|^(1/2), giving precisely the power rho-1.

Also |beta|<=sqrt(r_+)|S|^rho, so beta is continuous. Splitting |S|<=epsilon and |S|>epsilon proves uniform convergence on compact sets, with error at most C epsilon^rho. In the second region use 1-(1+epsilon^2/S^2)^(-eta/2)<=C epsilon^2/S^2. Weak compactness in any 1<t<1/(1-rho) and (3) prove beta in Wloc^(1,t). Its derivative vanishes almost everywhere on S=0, again by the level-set property. Thus classical zero curl off S=0 extends to distributional zero curl on D. This step imposes no boundary regularity on the zero set and differentiates no ratio.

For 2/5<c<1/2, 1/rho is between 2 and 3 and 1/gamma is between 1 and 3/2. On compact smaller sets S in C3 supplies C^(2,alpha) for alpha=1/rho-2, and V in C2 supplies C^(1,alpha) for alpha=1/gamma-1. Hence the same proof supplies the stated finite regularity version.

## 3. Global exactness and an attained maximum

For k=X.V, direct differentiation gives

    grad k=A^T V+DV^T X
          =A^T V+DV X+X cross W
          =-aV+X cross W.

Since k=0, X cross W=aV. The triple-product identity, W.grad S=0 and X.grad S=-bS imply

    grad S cross V=(b/a)S W.

Therefore curl beta=|S|^(-eta)[W-eta(grad S cross V)/S]=0 wherever S!=0. Section2 proves distributional closedness on all of D.

A continuous distributionally closed form has local C1 potentials: mollify on a larger ball, take normalized radial primitives on a smaller ball and pass to the uniform limits of both primitives and gradients. Since D is simply connected, these local primitives join to one single-valued C1 function phi with grad phi=beta. Equivalently, local exactness and homotopy invariance make path integrals independent of path. There is no period condition left to assume.

We have X.grad phi=0 everywhere, including S=0 where beta=0. Hence phi(F_t x)=phi(x) for every t. Its restriction to the compact unit sphere attains a maximum M. Every point of D lies on a spiral meeting that sphere, so M is the global maximum of phi on D, attained at an interior point. Only completeness of the explicit linear flow has been used. Neither the V-flow nor the W-flow is assumed complete.

## 4. A full physical-space weak equation

On S!=0 let h=|S| and R=E/h. Since grad phi=h^(-eta)V,

    |grad phi|^2=R h^gamma,
    h^eta=R^(-tau)|grad phi|^(m-2),
    tau=eta/gamma=(m-2)/2.

Consequently

    V=q|grad phi|^(m-2)grad phi, q=R^(-tau).              (4)

On S=0 assign q=r_+^(-tau). Both V and grad phi vanish there, so (4) holds at every point. The resulting coefficient is measurable and satisfies

    0<r_+^(-tau)<=q<=r_-^(-tau)<infinity.

Incompressibility becomes the full-domain distributional equation

    div(q|grad phi|^(m-2)grad phi)=0.                    (5)

The solution belongs to Wloc^(1,m) because it is C1. There is no deleted interface, quotient drift, boundary term, or derivative of q in this statement.

## 5. Primary maximum-principle input

The external input is James Serrin, Local behavior of solutions of quasi-linear equations, Acta Mathematica111(1964),247-302. For nonnegative weak W1,m solutions of (5), positive bounded measurable q gives local Harnack. Theorems5,6,9 cover respectively m<3, m=3 and m>3. Divide the flux by lambda=inf q>0: A=(q/lambda)|p|^(m-2)p satisfies |A|<=(sup q/lambda)|p|^(m-1) and p.A>=|p|^m. Set B and all lower-order coefficients to zero in structural condition(6). The weak formulation is(9), and every additive Harnack constant is zero. This mapping uses no continuity of q and allows degeneracy at p=0.

The actual journal PDF and text are pinned. Printed247-251,255-256,259-260,264-269,272-273 were read; pages251 and264 were visually checked. This includes the full Theorem5 proof, Theorem6 statement and its stated reduction, Theorem9 proof and the relevant additive constants. The remaining pages and all preliminary inequalities are not independently certified here. Classical Moser, Sobolev and John-Nirenberg inputs remain external dependencies.

## 6. Conclusion and exact limitations

Set u=M-phi. It is nonnegative, C1 and a weak W1,m solution of (5), since its flux is the negative of phi's flux. At a zero of u, take a ball whose triple lies in D. Harnack gives u=0 on a smaller ball. Thus the nonempty set {u=0} is open; continuity makes it closed. Connectedness gives u=0 throughout D. Equation(4) gives V=0, and the lower comparison gives S=0.

This proves the theorem for every finite omega, with no Fourier truncation or symmetry restriction. It handles arbitrary scalar zero sets. Local Harnack does not imply unique continuation from an arbitrary flat zero of a sign-changing solution; here it is applied to the globally nonnegative function M-phi. The compact orbit-space maximum is therefore essential to this proof. The earlier local theorem A1754 retains its separate full-disk W1,2 ratio hypothesis. No claim has been made that a general profile supplies k=0 or global positive finite ratio bounds. The main bare-decay question remains OPEN.

## 7. Verification record

All seven submitted sections and this seven-section reconstruction were read. Source pins and reading coverage are in verification. The local scalar-root removal argument from A1748 was rechecked at each use. No numerical computation, formal build or new client was needed. Formal sources are absent because this is an informal proof with explicit external analytic dependencies.

The submitting agent uses a second model the external referee (a second model). The existing configured model coordinator and theory agents receive these findings through working files; actual provider runtime is not independently attested. No new model or agent was invoked.
