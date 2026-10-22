# Smooth angular tails of a horizontal primitive

Status: proved criterion, independently audited by actual claude-opus-5-5; numerical controls pending. This is not a B2 exclusion. Written before implementing the criterion.

## Exact statement and hypotheses

Let 0<m<1. Let f be smooth on R2 minus0, homogeneous of degree m-1, and odd under x reflection. Define

    T(x,y)=int_0^x f(s,y) ds.

For y=0 the integral is interpreted as the convergent improper integral at0; it converges because m-1>-1. Then T is continuous on R2, homogeneous of degree m, even in x, and smooth away from the origin and the horizontal line y=0. It vanishes on x=0. Put a=f(1,0), f_sigma(u)=f(u,sigma), sigma in{+1,-1}, and

    C_sigma=lim_(R->infinity)[int_0^R f_sigma(u)du-a R^m/m].       (1)

Both limits exist. The following are equivalent:

1. T is C1 on a neighborhood of each point (x,0), x!=0.
2. C_+=C_-=0.
3. T is smooth on the whole punctured plane, equivalently it has a smooth angular profile on the unit circle.

For each fixed x>0 and sufficiently small |y|, T has the exact decomposition

    T(x,y)=H(x,y)+C_sign(y)|y|^m,                               (2)
    H(x,y)=a x^m/m-int_x^infinity[f(v,y)-a v^(m-1)]dv.           (3)

Here H extends smoothly through y=0 and H(x,0)=a x^m/m. Formula (2) is also understood continuously at y=0. Thus the two constants are necessary cancellation conditions when defining a temperature by horizontal integration and requiring a smooth homogeneous leading tail. They are not automatically implied by smoothness of f on the punctured plane.

## Proof

Oddness of f makes its primitive even in x. For fixed y!=0 its smoothness follows from differentiation of the finite integral. Homogeneity follows by changing variables s=lambda u for lambda>0. Since f is bounded by C r^(m-1),

    |T(x,y)|<=C int_0^|x| (s^2+y^2)^((m-1)/2)ds<=C |x|^m/m.

The last inequality uses m-1<0 and s^2+y^2>=s^2. This proves continuity at0 and a bound uniform near the line y=0. At fixed x>0, dominated convergence with the integrable majorant C s^(m-1) proves continuity as y tends to0. Reflection covers x<0.

For u>=1, homogeneity gives f_sigma(u)=u^(m-1)f(1,sigma/u). Taylor expansion in the smooth second argument at0 gives

    f_sigma(u)-a u^(m-1)=O(u^(m-2)).

Since m-2<-1, the difference is integrable on [1,infinity), proving (1). For y!=0, homogeneity and (1) give

    T(x,y)=|y|^m int_0^(x/|y|) f_sigma(u)du
           =a x^m/m+C_sigma|y|^m
             -|y|^m int_(x/|y|)^infinity[f_sigma(u)-a u^(m-1)]du.

Changing variables v=|y|u yields (2)-(3).

Fix a compact interval 0<x_1<=x<=x_2 and |y|<=x_1/2. The integrand in (3) is O(|y|v^(m-2)) uniformly for all v>=x_1. Every y derivative of positive order j is O(v^(m-1-j)) by homogeneity and bounded derivatives of f(1,y/v). These are integrable for all j>=1 because m<1. Split int_x^infinity as int_x1^infinity minus int_x1^x. Derivatives in x then differentiate a finite smooth integral and the smooth term a x^m/m; every mixed derivative involving x reduces to derivatives of the integrand at its lower endpoint. Dominated convergence for each derivative therefore proves H is smooth jointly in this neighborhood. In particular H(x,y)-H(x,0)=O(|y|).

If either C_sigma is nonzero, the one-sided difference quotient of T in y contains a nonzero multiple of |y|^(m-1), which is unbounded. Thus T cannot be C1 at any x>0 on that side. If both constants vanish, (2) equals H and is smooth across the positive horizontal half-axis. Evenness gives the same conclusion on the negative half-axis. Smoothness elsewhere was already proved. This proves every implication.

## Angular form and finite-radius remainder

Write f(r cos theta,r sin theta)=r^(m-1) phi(theta), so a=phi(0). Since the difference in (1) is integrable both at0 and infinity,

    C_sigma=int_0^infinity[f(u,sigma)-a u^(m-1)]du.

Substitute u=cot theta to obtain the ordinary convergent improper integral

    C_sigma=int_0^(pi/2) [phi(sigma theta)-a cos(theta)^(m-1)]
                                 sin(theta)^(-1-m) dtheta.     (4)

Near0 the bracket is O(theta), giving O(theta^(-m)); near pi/2 the only possible singularity is the integrable cos(theta)^(m-1). Thus neither endpoint needs an unadvertised regularization. This derivation also checks the sign of both constants.

Let C_sigma(R) denote the bracketed finite-radius expression in (1). Taylor expansion one order further gives, with b_sigma=sigma partial_y f(1,0),

    C_sigma-C_sigma(R)=b_sigma R^(m-1)/(1-m)+O(R^(m-2)).

The O constant is for the fixed source and exponent. Thus direct finite-radius subtraction can converge slowly as m approaches1. It is not a uniform bound for a family of sources.

## Examples and the distinction between a smooth field and a smooth angular limit

First let f(x,y)=x(x^2+y^2)^((m-2)/2). Then

    T(x,y)=[(x^2+y^2)^(m/2)-|y|^m]/m,
    C_+=C_-=-1/m.

Thus f has a smooth angular profile but T does not have a C1 angular profile. The globally smooth regularization

    f_e(x,y)=x(1+x^2+y^2)^((m-2)/2),
    T_e(x,y)=[(1+x^2+y^2)^(m/2)-(1+y^2)^(m/2)]/m

still satisfies partial_x T_e=f_e and T_e(0,y)=0. Its rescaled leading limit is the preceding nonsmooth T. Consequently global smoothness of a numerical field alone does not certify smoothness of its homogeneous angular limit.

For a compatible example take T=x^2(x^2+y^2)^((m-2)/2), which is smooth on the punctured plane and zero on the axis. Its x derivative is

    f=2x r^(m-2)+(m-2)x^3 r^(m-4).

It has C_+=C_-=0, either by the theorem or directly by subtracting the exact primitive's leading x^m term in (1). These examples are primitive controls, not B2 profiles, and no Poisson claim is made for them.

## Scope for the B2 search and dependencies

For beta>2, m=1-2/beta lies in(0,1). For a smooth odd stream Psi define Omega=-Delta Psi, U=(-Psi_y,Psi_x), V=U-U(0), W=beta X+V, and F=W.grad Omega+Omega. The vorticity equation and Theta(0,y)=0 require Theta=int_0^x F. Suppose f_infinity is an independently derived leading homogeneous coefficient of F of degree m-1, with a smooth angular profile. Then its horizontal primitive has a smooth angular profile precisely under the two conditions above. The entire F need not itself be homogeneous. Applying this statement to actual computed profiles additionally requires a justified interchange of rescaling and horizontal integration, or direct proof of convergence of the primitive. For each fixed x,y a sufficient condition is convergence of the rescaled source at almost every horizontal integration point and a uniform integrable bound C s^(m-1) on 0<s<=|x|; dominated convergence then applies. The normalization of the primitive matters: adding c_sigma|y|^m changes the criterion to C_sigma+c_sigma=0. The B2 condition Theta(0,y)=0 fixes that freedom. This packet does not assert that interchange for every trial stream or that the broad prompt requires a smooth angular limit without further hypotheses.

The proof uses only homogeneity, parity, Taylor's theorem, integrable bounds and dominated differentiation. All definitions and arguments are standalone. There is no formal Lean development and no existence or nonexistence conclusion for B2.

Written UTC: 2026-10-21T05:30:30.998428+00:00
