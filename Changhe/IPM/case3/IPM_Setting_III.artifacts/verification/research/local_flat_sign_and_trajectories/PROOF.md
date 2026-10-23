# Local sign oscillation of a flat defect and an exact trajectory criterion

Status: CONFIRMED by independent mathematical reconstruction on2026-10-20. Supporting tests are separate from the proof. This audits FLAT1S(a),(b) in the lead's referee/flat1s/PROOF.md. Neither result proves the extra hypotheses for the whole admissible class.

## Setting and statements

Let ell>1 and let rho,psi be an exact smooth primary full-plane IPM profile:

    W.grad rho=rho, W=ell X+U, U=(-psi_y,psi_x),
    -Delta psi=rho_x.

The density is even in x and odd in y, psi is odd in both coordinates, a=rho_y(0)!=0, rho and its weighted first derivatives have strictly sublinear growth, and the canonical velocity satisfies U=o(r). Put

    D=ell-1, A=2ell-1, H=y-rho/a,
    phi=psi+Dxy, v=(-phi_y,phi_x), V=v2,
    B=X.W/r^2, q=rho/(a y), G=V/y.

The two quotients extend smoothly to the horizontal axis by parity.

1. Suppose H is flat at the origin. Let rd=inf{|X|:H(X)!=0}. Then rd is finite, and H(X)y has both signs in every open ball B_R with R>rd. This includes an exactly affine open core rd>0. There is no global sign, strain, radial cap, or bounded-DU assumption.
2. Suppose every backward orbit of W tends to the origin. Then, for every X,

    q(X)=exp(-int_(-infinity)^0 G(X(t;X)) dt)>0.           (T)

The improper integral converges absolutely. Consequently q<=1 everywhere if and only if these orbit integrals are nonnegative everywhere. In particular the additional inequality W2/y>=1 gives0<q<=1. The pointwise bound partial_y U2>=-D is sufficient for that inequality; it is not asserted equivalent to it.

Both statements are conditional properties of exact profiles, not existence or full-class nonexistence theorems.

## Preliminary identities and growth

Parity gives U(0)=0 and DU(0)=diag(-c,c), c=psi_xy(0). Differentiating W.grad rho=rho at zero in y gives (ell+c)a=a, hence c=-D. Therefore

    W=(Ax,y)+O(r^3), H=O(r^3), V=O(r^3) near zero.

Direct substitution gives

    W.grad H-H=V,       Delta V=a H_xx.                  (1)

In the flat case V is also flat, by the first equation. At infinity H,V=O(r) and W=O(r). Globally W has at most linear growth. The excluded density rho=a y would be the only case H identically zero. Thus the support defining rd is nonempty.

For m>2 define the absolutely convergent, possibly signed moments

    I_m=int H y r^(-2m) dX,  J_m=int V y r^(-2m) dX.

We need the full signed identities, not positivity assumptions:

    J_m = a/[2(m-2)] int H y r^(-2m)
                                   (2m x^2/r^2-1) dX,   (2)
    J_m = 2m int H y r^(-2m) B dX
                 -(2ell+1)I_m-int H W2 r^(-2m) dX.      (3)

Here is a cutoff justification. Set f=y r^(2-2m). Elementary differentiation gives

    Delta f=4(m-1)(m-2)y r^(-2m),
    partial_xx f=2(m-1)y r^(-2m)(2m x^2/r^2-1).

Test Delta V=a H_xx against f times radial cutoffs at eps and R, put both derivatives on the test function, and remove the cutoffs. The outer errors are bounded by C_m R^(4-2m), using only H,V=O(r). At the inner cutoff flatness bounds each error by C_(m,N) eps^(N+3-2m), with N arbitrarily large. This proves(2). Test the first equation of(1) against y r^(-2m) with the same cutoffs, integrate once, use div W=2ell and

    W.grad(y r^(-2m))=W2 r^(-2m)-2m y r^(-2m)B.

The cutoff errors obey the same types of bounds, because W=O(r), and yield(3). All retained terms are absolutely integrable. No division by y is used outside a compact ball.

## Proof of local sign oscillation

Suppose, contrary to claim1, that for some R>rd one can choose s=1 or-1 such that s H y>=0 throughout B_R. Write Hhat=sH, Vhat=sV. Equations(1)-(3) still hold with these two fields and the same a and W.

We first find R1 with rd<R1<R and B>=1/2 throughout0<r<R1. If rd=0 this follows from W=(Ax,y)+O(r^3) and A>1. If rd>0, H=0 in B_rd by the definition of rd, hence V=0 there by(1). Oddness in x and phi_x=V imply

    phi(x,y)=int_0^x V(t,y)dt=0 on B_rd.

The horizontal integration segment stays in the ball. Thus v=0 and W=(Ax,y) throughout B_rd and, by continuity, on its boundary. The minimum of B on that compact sphere is at least1. Uniform continuity therefore supplies the desired outer annulus. Shrink it if necessary to keep R1<R.

Choose rd<r0<R1 for which c0=int_(r<r0) Hhat y dX>0. Such r0 exists: H is nonzero at some point of any ball larger than rd, that point is off y=0 by oddness, and the assumed sign plus continuity gives positive mass on an open set. Denote

    P_m=int_(r<R1) Hhat y r^(-2m) dX >=c0 r0^(-2m),
    E_m=int_(r>=R1) |Hhat y| r^(-2m) dX.

Growth and compactness give constants C_H,C_W such that |H|<=C_H r and |W|<=C_W r on r>=R1. Therefore

    E_m <=2pi C_H R1^(4-2m)/(2m-4),
    int_(r>=R1)|Hhat W2|r^(-2m)dX
                  <=2pi C_H C_W R1^(4-2m)/(2m-4).        (4)

Both quantities divided by P_m are at most a fixed constant times (r0/R1)^(2m)/(2m-4). In particular E_m/P_m tends to zero even after multiplication by m. The full signed moment Ihat_m satisfies |Ihat_m-P_m|<=E_m, so Ihat_m>0 for large m and P_m/Ihat_m=1+o(1). The same exponentially small error estimates hold with Ihat_m in the denominator.

The absolute elliptic multiplier in(2), including its prefactor, is bounded by

    |a|(2m-1)/[2(m-2)],

which is bounded as m tends to infinity. Since total absolute mass is P_m+E_m, equation(2) gives a uniform bound for |Jhat_m|/Ihat_m.

Equation(3) instead implies divergence to positive infinity. Indeed B>=1/2 on the positive inner measure and |B|<=C_W outside. Thus

    int Hhat y r^(-2m)B / Ihat_m >=1/2-o(1),

with m times the error tending to zero. On the compact ball, W2/y=int_0^1 partial_y W2(x,ty)dt has a finite absolute bound C1. The inner part of int Hhat W2 r^(-2m) is at most C1 P_m; its outer absolute value is controlled by(4). Consequently(3) gives

    Jhat_m/Ihat_m >=m-(2ell+1)-C1-o(1) ->+infinity.

This contradicts the bound from(2). Neither sign can hold on such a ball, proving claim1.

The result does not exclude flat defects with sign oscillation arbitrarily close to their innermost support. Flatness by itself is insufficient for a NO theorem.

## Proof of the trajectory criterion

Parity gives the smooth extensions

    q(x,y)=a^(-1) int_0^1 rho_y(x,ty)dt,
    G(x,y)=int_0^1 partial_y V(x,ty)dt.

They satisfy q(0)=1 and G=O(r^2) near zero. Substitute rho=a y q into transport off y=0 to obtain

    W.grad q=-G q.                                      (5)

Both sides are smooth, so(5) also holds on the axis.

The flow exists for all finite positive and negative times. Local smoothness gives local existence and uniqueness, while |W(X)|<=C(1+|X|) and Gronwall's inequality prevent escape to infinity in finite time. The horizontal axis is invariant; off-axis trajectories never reach it in finite time, either by uniqueness or by the scalar equation ydot=(W2/y)y.

Fix X and its backward trajectory. By the extra convergence assumption it eventually stays in a ball where B>=1/2. For t<=t0 there,

    d(log r)/dt=B>=1/2,
    r(t)<=r(t0) exp((t-t0)/2).

If the orbit is stationary at zero, the conclusion is immediate. Otherwise G(X(t))=O(r(t)^2)=O(exp(t)), so its absolute integral over(-infinity,t0] is finite. The remaining finite trajectory segment is compact and G is continuous, hence its integral is also finite.

Solve the scalar linear equation(5) between T and0:

    q(X)=q(X(T;X)) exp(-int_T^0 G(X(t;X))dt).

As T tends to negative infinity, q(X(T;X)) tends to1, and the absolutely convergent integral tends to its full value. This proves(T), including axis starting points by the same smooth ODE argument. Positivity follows without a separate assumption on rho's sign.

Taking logarithms in(T) proves the equivalence with the nonnegative cumulative integral. Since G=W2/y-1=U2/y+D, the pointwise sufficient criterion follows. Finally

    U2(x,y)/y=int_0^1 partial_y U2(x,ty)dt,

so partial_y U2>=-D is sufficient for it. An average of a function being bounded below does not assert that every pointwise value has the same bound.

## Scaling, dependencies and scope

Under the genuine scaling rho_lambda(X)=lambda rho(X/lambda), psi_lambda=lambda^2 psi(X/lambda), the constants a,ell,D,A do not change. H,V,W scale like length, the radii scale by lambda, and I_m,J_m both scale by lambda^(4-2m). Trajectories transform X_lambda(t)=lambda X(t), and G is composed with X/lambda. Thus both conclusions and all integral signs are scale invariant without an exceptional normalization.

Dependencies: elementary differentiation, cutoff integration by parts, local smooth ODE existence and uniqueness, Gronwall's inequality, and the exact profile equations. The moment formulas agree with result70 but have been rederived here. No sampled maximum, unproved strain cap, global source-flow assumption, or analytic unique continuation has been inserted into claim1. Claim2 explicitly requires backward convergence of every orbit; establishing it for all admissible exact profiles remains open.
