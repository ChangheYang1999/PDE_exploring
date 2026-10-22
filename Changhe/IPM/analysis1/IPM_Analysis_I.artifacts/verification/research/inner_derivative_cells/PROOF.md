# Inner derivative Taylor models from exact Green ODE defects

Written before implementation on 2026-10-22. Status: analytic theorem pending independent review; numerical application OPEN. This result concerns the distinguished normalized finite modal trial. It asserts no distance to X3, inverse, existence or exclusion.

## Exact statement, hypotheses and notation

Let k=1615536043799051/9007199254740992, L=8614738245908811/1125899906842624, a=-685794559684773/140737488355328, R=exp(a), c_l=1/k and c=3/k-1. Let rho be the exact canonical normalized trial specified by the accepted modal_repair and canonical_residual_composition results. Those results, their exact coefficient data and their canonical identification are explicit application dependencies. Write t=log r, tau=t-a and D=partial_tau. On tau<=0 its finite sine series is

    rho=r^3 sum_(j=0)^260 H_j(tau) sin((2j+1)theta),
    H_j=C_j+sum_(l=0)^6 d_(j,l)exp((2l+2)tau)+exp(b_i tau)E_j(tau).

Here b_i>=49 is the exact pinned exponent, E_j has degree at most6, C_0=C_1=1/4, and all other C_j=0. Coefficients are fixed exact rationals. Put H_261=0. The complete piecewise modal extension, rather than the inner expression continued to infinity, defines the canonical velocity U. Require its already accepted canonical strain identity psi_xy(0)=c. Let

    eps=(c_l X+U) dot grad rho-rho,
    ||f||_X(A)^2=integral_A [f^2+r^2|grad f|^2] w(r)dX,
    w(r)=L^6 r^-6(1+r^2/L^2)^(3/2-k).

For each exact cell [s_-,s_+] subset[-5,0], the construction below yields whole-cell upper bounds B_p>=sum_nu |D^p eps_nu| for p=0,1,2 and C_p>=sum_nu nu|D^p eps_nu| for p=0,1. If all44 cells of the partition below are certified with the same canonical inputs, and the accepted derivative_end_tails bound at tau=-5 is reused with its exact source pins, summing the resulting squared norm bounds gives rigorous upper bounds for ||eps||_X(r<=R) and ||eps-D eps||_X(r<=R).

This is a conditional analytic construction. No44-cell computation has been performed for this result. A numerical theorem requires separately verified finite arithmetic, every coefficient, exact covering, output audit, replay, actual model review and later independent adjudication.

## Canonical Green identities and exact strain cancellation

For m=2n, n=1,...,261, put

    F_n=[H_(n-1)'+H_n'+(4-m)H_(n-1)+(4+m)H_n]/2,
    G_n=r^4 F_n,
    A_n=r^-m integral_0^r s^(m+1) f_n(s)ds,
    B_n=r^m integral_r^infinity s^(1-m) f_n(s)ds,
    f_n=r^2 F_n.

Direct differentiation gives D A_n=-m A_n+G_n and D B_n=m B_n-G_n. The canonical stream mode is (A_n+B_n)/(2m). Consequently U_r/r has cosine coefficient -(A_n+B_n)/(2r^2), and U_theta/r has sine coefficient (B_n-A_n)/(2r^2). Signs follow from U_r=-r^-1 partial_theta psi, U_theta=partial_r psi.

For n=1 subtract the exact affine strain by defining Bhat_1=B_1-2cr^2. The canonical strain integral c=(1/2)integral_0^infinity f_1(s)/s ds gives

    Bhat_1=-r^2 integral_0^r f_1(s)/s ds,
    D Bhat_1=2 Bhat_1-G_1.

For n>=2 put Bhat_n=B_n. Thus all Bhat_n solve D Bhat_n=m Bhat_n-G_n. Define

    p_n=-(A_n+Bhat_n)/(2r^2), s_n=(Bhat_n-A_n)/(2r^2).

They represent U-(-cx,cy). With rho_0=x^2y, eta=rho-rho_0, P=sum_n p_n cos(2n theta), S=sum_n s_n sin(2n theta), the exact residual is

    eps=Lin+P D rho+S partial_theta rho,
    Lin=(D/k-1)eta-c cos(2theta)D eta+c sin(2theta)partial_theta eta.   (1)

Indeed the affine velocity acts as -c cos(2theta)D+c sin(2theta)partial_theta, and (3/k-c-1)rho_0=0. Remove rho_0 algebraically, before interval arithmetic. Lin has odd frequencies at most523, and eps at most1043. No independent choice of a harmonic strain is allowed.

For an independent construction define

    i_n(tau)=integral_(-infinity)^tau exp(-(m+4)(tau-u))H_(n-1)(u)du,
    j_n(tau)=integral_tau^infinity exp((4-m)(u-tau))H_n(u)du.

Then D i_n=-(m+4)i_n+H_(n-1) and D j_n=(m-4)j_n-H_n, and integration by parts yields

    A_n/r^2=r^2[(H_(n-1)+H_n)/2-m i_n],
    B_n/r^2=r^2[m j_n-(H_(n-1)+H_n)/2].                  (2)

All boundary terms vanish under the accepted modal asymptotics. For n=1 use the displayed direct Bhat integral, avoiding subtraction of two interval strain enclosures. Canonical center values are fixed by their convergent integrals, never by independent free ODE data. Stable finite integrals at nearly resonant exponents and their independent arithmetic are inherited from inner_cells/PROOF.md. The primary physical Green ODE has maximum absolute rate522; the independent density ODE has maximum absolute rate526.

## Derivative Taylor model algebra

Fix a cell, t_c=(s_-+s_+)/2, h=(s_+-s_-)/2>0, v=(tau-t_c)/h, and Q>=8. A derivative Taylor model consists of a degree at mostQ polynomial P(v), with interval enclosures of its fixed exact coefficients, and nonnegative numbers e_0,e_1,e_2 such that

    |D^p f-h^-p partial_v^p P|<=e_p on |v|<=1, p=0,1,2.

These are three separately proved remainder bounds. Differentiating a zeroth-order inequality is forbidden. Define

    N_(P,p)=sum_(l=p)^Q (l)_p |P_l| h^-p,

where (l)_p is a falling factorial, zero for l<p. Addition and constant multiplication act on each derivative error by the triangle inequality.

For analytic inputs exp(lambda tau)sum_(j=0)^d c_j tau^j, d<=6, form the exact Taylor coefficients

    A_l=h^l sum_(j=l)^d binom(j,l)c_j t_c^(j-l), ell=lambda h,
    P_q=exp(lambda t_c)sum_(l=0)^min(q,d) A_l ell^(q-l)/(q-l)!.

For p<=2, x=|ell| and N_l=Q-l+1, a valid derivative remainder is

    exp(lambda t_c)h^-p exp(x)sum_l |A_l|x^N_l
          sum_(q=0)^p binom(p,q)(l)_(p-q)/(N_l-q)!.       (3)

Proof: expand the omitted entire series, differentiate it uniformly on the compact cell, and use (l+j)_p=sum_q binom(p,q)(l)_(p-q)(j)_q. The omitted q term is bounded by x^q sum_(i=N_l-q)^infinity x^i/i!<=exp(x)x^N_l/(N_l-q)!. Since N_l>p, all factorials are defined and x=0 gives zero. Sum analytic terms before coefficient absolute values; sum their positive remainder bounds. An independent method first forms c^(p+1)=lambda c^(p)+(c^(p))', expands the differentiated analytic function to degreeQ-p, and applies its ordinary exponential remainder formula. Its exact retained polynomial equals h^-p partial_v^p P. Every independent coefficient enclosure is compared, but interval overlap is only a consistency test.

If f=P+e and g=T+d have such models, let U be the full degree at most2Q polynomial PT and let W be its truncation through degreeQ. Then the error for the model W of fg satisfies

    e_(fg,p)<=sum_(l=0)^p binom(p,l)[N_(P,l)e_(g,p-l)
                +N_(T,p-l)e_(f,l)+e_(f,l)e_(g,p-l)]
                +sum_(q=Q+1)^2Q (q)_p |U_q|h^-p.        (4)

This follows by applying Leibniz to the exact functions and their polynomial remainders, and then bounding the derivative of the explicitly discarded polynomial. In particular the derivative of a discarded high-degree term carries its falling factorial. Formula (4) will be used when multiplying Green moments by r^-2 in the primary construction and r^2 in (2). It prevents an unnoticed derivative loss from that intermediate truncation.

## Derivative errors from the exact ODE defect

Suppose D y=lambda y+sigma G with constant real lambda and |sigma|<=1, and G has a degreeQ derivative Taylor model (g,e_(G,0),e_(G,1),e_(G,2)). Let y_0 be the canonical value at t_c, rigorously enclosed. Define the exact polynomial coefficients

    p_0=y_0,
    p_(q+1)=h[lambda p_q+sigma g_q]/(q+1), 0<=q<Q,
    d=lambda p_Q+sigma g_Q.

Let e=y-P and r_G=G-g(v). The recurrence implies the exact identity

    D e=lambda e+sigma r_G+d v^Q, e(t_c)=0.              (5)

Variation of constants in v, in either direction from0, proves

    e_0=exp(|lambda|h)h[|d|/(Q+1)+e_(G,0)].             (6)

Here integral_0^|v| u^Q du<=1/(Q+1) and every propagator has magnitude at most exp(|lambda|h). No small denominator or rate separation is used.

Using the exact identity (5), rather than differentiating (6), gives

    e_1=|lambda|e_0+e_(G,0)+|d|,
    e_2=|lambda|e_1+e_(G,1)+Q|d|/h.                    (7)

Indeed D(v^Q)=Q v^(Q-1)/h and |v|<=1. These formulas remain valid for lambda=0 and either sign of sigma. If coefficients are intervals, choose the exact center and forcing coefficients belonging to the actual fixed solution. The recurrence encloses their corresponding exact polynomial. Equations (5)-(7) hold for that polynomial; interval bounds enlarge each positive quantity. Center uncertainty is already enclosed in p_0 and all propagated coefficients, so it is not silently omitted from the model.

In the primary method apply (5)-(7) to A_n and Bhat_n with forcing G_n. In the second method apply them to i_n,j_n with forcing H_(n-1),H_n and use (2), with direct Bhat_1. These use different ODE rates, forcing data, center evaluations and intermediate polynomial products. Their exact degreeQ Taylor polynomials for the final p_n,s_n coincide because both constructions represent the same analytic function with exact Taylor coefficients and truncate only aboveQ. Every coefficient must be compared independently. Their positive error bounds may differ and need not overlap. Higher derivative polynomial equality is checked using exact falling factorials and the physical h factors.

## Residual norms and the complete inner join

Use (1) with derivative models of Lin, P, S, D rho and partial_theta rho. Form the full degree2Q residual polynomial Z before coefficient absolute values and retain all522 real sine modes. Primary signed Fourier convolution and independent exact integer center-radius convolution use radial stride2Q+1, so there is no aliasing. Every resulting coefficient is compared. The derivative residual error is

    delta_p=e_(Lin,p)+sum_(l=0)^p binom(p,l)[
       N_(P,l)e_(D rho,p-l)+N_(D rho,p-l)e_(P,l)+e_(P,l)e_(D rho,p-l)
      +N_(S,l)e_(theta rho,p-l)+N_(theta rho,p-l)e_(S,l)
      +e_(S,l)e_(theta rho,p-l)].                       (8)

Here each N and e sums over all corresponding real angular modes. Product-to-sum has total absolute coefficient at most1, proving the Wiener algebra inequality used in (8). Lin is formed from eta, D eta with its exact frequency shifts; its cubic part is identically absent. Since the angular support is finite, the angular derivative error is at most1043 delta_p.

For each sine mode of Z_p=h^-p partial_v^p Z, convert degrees0,...,Q to a degreeQ Bernstein polynomial on v=2x-1. Let b_(nu,p) be its maximum absolute Bernstein coefficient plus the absolute sum of all remaining radial coefficients. Nonnegative Bernstein basis functions sum to1, and the latter sum bounds every remaining monomial. Thus

    B_p=sum_nu b_(nu,p)+delta_p,
    C_p=sum_nu nu b_(nu,p)+1043 delta_p.                 (9)

Put v_w(t)=L^6 exp(-4t)(1+exp(2t)/L^2)^(3/2-k). Its logarithmic derivative is -4+(3-2k)exp(2t)/(L^2+exp(2t))<0 because0<k<1. Full-circle orthogonality and r^2|grad f|^2=|Df|^2+|partial_theta f|^2 show that the cell contributes at most

    pi(s_+-s_-)v_w(a+s_-)[B0^2+B1^2+C0^2],
    pi(s_+-s_-)v_w(a+s_-)[(B0+B1)^2+(B1+B2)^2+(C0+C1)^2] (10)

to the two squared X norms. These use true cell widths, not Taylor radii. Independent positive interval evaluations enclose the weight. The factor is pi since there is no zero frequency.

The44-cell partition comprises15 cells of width1/5 from-5 to-2,19 cells of width1/10 from-2 to-1/10, and10 cells of width1/100 from-1/10 to0. It is exactly the last44 cells of the accepted54-cell inner partition. Check all consecutive rational endpoints. Add the squares of the accepted derivative_end_tails strict norm ceilings on tau<=-5, without changing their constants. This tail theorem already handles the singular weight at the origin. The exact functions and required weak derivatives match at the artificial cell boundaries; these boundaries have measure zero. The same accepted canonical piecewise regularity identifies the inner/middle interface at tau=0. Therefore additivity of nonnegative integrals proves the claimed inner norm bounds if all finite and tail inputs are certified.

A later whole-plane composition must also have certified middle and exterior contributions for the identical trial, normalization, weights and interfaces. It is a new composition with new ceilings. It does not modify earlier bounds or prove any old19389-cell W targets. A complete implementation must publish exact source maps, every finite coverage record and all derivative errors, independent coefficient counts and arithmetic, fresh output audits and maximizer replays, actual model review and a later own adjudication. No numerical application is claimed in this note.
