# Global axis identity with the exact cutoff terms

## Statement, actual background and regularity

Fix the actual exactly normalized modal trial rho0, ell0=1/k, its leading far density P_infinity(X)=r^k Theta(theta), and the exact moving-tail chart of topics167 and190. The radial cutoff chi_infinity is smooth, zero on r<=1 and one on r>=R_chi for a fixed R_chi. The chart density derivative is

    zeta(X)=-k^2 chi_infinity(r) log(r) P_infinity(X).

It is set to zero on r<=1. This zeta is the density derivative, not proof 167 equation(13)'s bordered high-target vector. Use the canonical full-plane velocities and physical parity, with the exact strain c[q]=partial_y U2[q](0,0). Let nu=3-c[zeta]>0 and

    T=(ell0 X+U[rho0]).grad-1,
    F0=T rho0,
    A0 h=T h+U[h].grad rho0+c[h] M0,
    M0=(X.grad rho0+T zeta+U[zeta].grad rho0)/nu.

These are the exact chart operator and residual, not an unnormalized fixed-parameter operator. The modal density and its canonical velocity have the local regularity required for the axis coefficients and first derivatives below, also at the finite radial joins.

Suppose h has physical parity and finite canonical strain, h=x^4 H with H in C1 locally throughout the plane, and U[h] in C1 locally. These suffice for this pointwise identity. They do not by themselves imply global high-domain membership. The exact Gaussian d of proof 241 satisfies them and, separately, belongs to the actual high domain by V283.

For y in R define

    f(y)=axis(rho0)(y), u(y)=U2[rho0](0,y),
    z(y)=axis(zeta)(y), v(y)=U2[zeta](0,y),
    b(y)=U2[h](0,y), a=c[h]/nu,
    w=b+a(v-u/ell0), lambda=a/ell0=a k,
    R_h=A0 h-lambda F0.

Here axis(q)(y)=lim_(x->0)q(x,y)/x^2. For a C1 scalar velocity q define the one-dimensional first-order expression

    K_q F=q F'-2q' F.

Then for every y, with the value at zero understood continuously,

    axis(R_h)=K_w f+lambda f+a D z,                  (1)
    D F=(ell0 y+u)F'+(2ell0-1-2u')F.

In particular all density-chart cutoff terms are retained. Formula(1) reduces to proof 247's corrected identity on |y|<1.

## Leading cofactor and an identity without its dilation term

For y!=0 put r=|y| and

    f_infinity(y)=axis(P_infinity)(y),
    chi(y)=chi_infinity(|y|), e_chi=f-chi f_infinity.

The prescribed angular factor vanishes quadratically at the vertical axis and has the physical parity. Homogeneity and parity therefore give f_infinity(y)=A sign(y)|y|^(k-2) for its exact real angular coefficient A. No numerical value or nonvanishing of A is needed. In particular

    y f_infinity'=(k-2)f_infinity,
    (ell0 y partial_y+2ell0-1)f_infinity=0,
    z=-k^2 chi log(r) f_infinity.                    (2)

Use chi' for its derivative as a function of y, so chi'=sign(y)chi_infinity'(r). For y!=0, (1) has the equivalent exact form

    axis(R_h)=K_w f+a k e_chi
       -a k^2 [ chi log(r) K_u f_infinity
                +chi (u/y) f_infinity
                +(ell0 y+u) chi' log(r) f_infinity ]. (3)

Every product involving chi or chi' is defined as zero near y=0, where those cutoffs vanish identically. Thus(3) also extends continuously through zero. In the full outer region |y|>=R_chi, it becomes

    axis(R_h)=K_w f+a k (f-f_infinity)
       -a k^2 [(u/y)f_infinity+log(r)K_u f_infinity]. (4)

The explicit leading linear dilation term cancels exactly in(3)-(4). This is an algebraic identity; no accuracy estimate for floating subtraction is asserted.

For the exact Gaussian of proof 241,

    g(y)=-y^3 exp(-y^2)/6,
    b(y)=-g''(y)=(y-(7/3)y^3+(2/3)y^5)exp(-y^2),
    a=1/nu.

The corrected trace b=-g'', not2g-g'', must be used. These formulas give every term in(1)-(4) in terms of the original modal background, its exact chart velocity and cutoff, and this explicit Gaussian trace.

## Proof of the global identity

Incompressibility and parity give U1[q](x,y)=-x partial_y U2[q](0,y)+o(x) and U2[q](x,y)=U2[q](0,y)+o(1). Apply these expansions to the C1 coefficients of the fixed modal background. Then

    axis(F0)=D f,
    axis(U[h].grad rho0)=K_b f,
    axis(T zeta)=D z,
    axis(X.grad rho0)=y f'+2f,
    axis(U[zeta].grad rho0)=K_v f.

No division of a nonzero axis value occurs: rho0 and zeta both have the required x^2 factor. Also axis(T h)=0 since h=x^4 H, partial_x h=O(x^3), partial_y h=O(x^4), and the actual tangent transport has first component O(x). This argument holds at each finite y, not just inside the cutoff disk.

Substitution of the displayed M0 gives

    axis(R_h)=K_b f+a[y f'+2f+K_v f+D z]-lambda D f.

The coefficient of f' outside a D z is b+a v-a u/ell0=w. The coefficient of f is -2b'-2a v'+2a u'/ell0+a/ell0=-2w'+lambda. The ell0 y and2ell0 terms have both been retained in this cancellation. This proves(1) globally.

To prove(3), set E=ell0 y partial_y+2ell0-1, so D=E+K_u. Equation(2) gives E f_infinity=0. The product rule, with d(log|y|)/dy=1/y, therefore yields

    D z=-k^2 {chi log(r) K_u f_infinity
             +(ell0 y+u)[chi' log(r)+chi/y]f_infinity}.

Since k^2 ell0=k, the ell0 part of the chi/y term cancels a k chi f_infinity from lambda f. The remaining term is a k(f-chi f_infinity), which gives(3). Setting chi=1 and chi'=0 proves(4). On |y|<1, z=0 and(1) is exactly the previously confirmed local identity. The Gaussian specialization is the corrected canonical derivative proved in topics241 and247.

## Scope and dependencies

This proves scalar axis identities only. It gives no bound for the high target norm, its fractional derivatives, the bulk remainder or any cutoff transition. The transition term is explicitly present in(3); it is not an error term that has been estimated away. Canonical U[zeta] is global and need not vanish where zeta does. No whole-plane density or velocity is inferred from an arbitrary prescribed scalar trace.

If h is additionally in the actual maximal high domain, R_h belongs to the high target by the existing chart theorem and F0 membership. For the Gaussian this additional membership is already known from proof 241 with its binding clarification. That independent fact, not(1), legitimizes the Gaussian as a test for the necessary closure inequalities. No upper norm bound, violation of(I) or(S), continuum inverse, complement or profile existence follows.

Dependencies: proof 167 for the exact moving-tail chart and justified logarithmic velocity derivative; proof 190 for the exact residual-subtracted target; proof 241 with its clarification for the Gaussian and high-domain membership; proof 247 with all three binding sidecars and V296 for the canonical signs and local derivation. This new global extension is derived by hand and is pending independent audit before theorem adoption.
