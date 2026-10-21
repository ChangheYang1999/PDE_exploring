# Density bounds and the fifth source trace

Date: 2026-10-20. Status: conditional theorem proved; audit of the lead's D11 and fred39. No bound below is asserted for every profile of the admissible class.

## Statement and dependencies

Use source coordinates (s,y), with P=(0,0), r=-s>0 and W=(a,b). Assume, in a fixed neighborhood of P,

    W.grad f=f,    a_s+b_y=A+1,    b_s-a_y=-f_s,
    W(P)=0,       DW(P)=diag(A,1),    f_y(P)>0.

Here f,b are odd in y and a is even. Let f,W be C^(2,alpha), 0<alpha<1, and smooth at every point of a punctured left cone. Let 1<A<2, q=4/A, and assume on |y|<4 kappa r, 0<r<r0,

    |D^4 f| <= C r^(-p),    |D^5 f| <= C r^(-P0),
    0<=p<q-1,              P0 finite.

All derivative norms include every component of the stated order. If alpha>3-q, then on |y|<2 kappa r,

    |D^4 W| <= C[r^(alpha-2)+r^(-p)(1+|log r|)].       (1)

For R_n=2^(-n)r0 and cone annuli R_n/2<=r<=R_n, |y|<=2 kappa r, define

    d_n=R_n^(q-1) sup_annulus (|D^4 f|+|D^4 W|).

Then sum d_n is finite. The independent theorem in ../weighted-source/PROOF.md gives ell_5=0, where G_5=f_yyyyy/120 and H_5 is a positive solution of

    a(s,0) H_5'(s)+(5 b_y(s,0)-1)H_5(s)=0.

The normalization of H_5 is immaterial to vanishing. It has H_5(-r) asymptotic to a positive constant times r^(-q).

For 1<A<4/3, alpha>3-q holds for every class exponent alpha>0. The choice p=2 is then allowed, and the proof gives the stronger trace estimate

    |f_yyyyy(-r,0)| <= C r^(-3)(1+|log r|).           (2)

The sole transport input needed to deduce ell_5=0 from summability is the stated weighted-source theorem. Its complete argument, including the characteristic exit term, is available in that topic. The elliptic estimate is established below directly, without an external regularity theorem.

## Elliptic equations and local geometry

Differentiate the constant divergence and the curl equation:

    Delta a = partial_s(a_s+b_y)-partial_y(b_s-a_y)=f_sy,
    Delta b = partial_y(a_s+b_y)+partial_s(b_s-a_y)=-f_ss.

Fix Z=(-r,y) in the smaller cone. Choose ell=c r with fixed c>0 small enough that B_ell(Z) lies in the larger cone and its horizontal distances from P are comparable to r. For example c<1/4 and 2 kappa+c<4 kappa(1-c) suffice. Shrink r0 to stay inside the fixed regularity neighborhood.

For a derivative partial^mu of order two of a velocity component, set

    u(X)=partial^mu W_i(X)-partial^mu W_i(Z).

It obeys Delta u=G, where G is one signed fourth derivative of f, and

    sup_B |u| <= M2 ell^alpha,
    sup_B |G| <= M,    sup_B |grad G| <= L,

where M2 is a fixed C^alpha seminorm of D^2 W, M=sup_B |D^4 f| and L=sup_B |D^5 f|.

## Direct logarithmic interior estimate

Rescale U(X)=u(Z+ell X) to B1 and put g(X)=ell^2 G(Z+ell X). Then

    Delta U=g,    ||g||inf<=ell^2 M,    ||grad g||inf<=ell^3 L.

Take a smooth cutoff zeta supported in B1 and equal to one in B_(3/4). With Gamma(X)=log|X|/(2 pi), write U=V+H on B_(3/4), where V=Gamma*(zeta g). The logarithmic kernel is integrable on bounded sets, so ||V||inf on B1 is at most C||g||inf. H is harmonic on B_(3/4). To bound its second derivative at a point of B_(1/2), take any fixed smooth radial averaging kernel supported in a sufficiently small disk about that point. The harmonic mean-value identity represents H as its convolution with this kernel. Differentiating the kernel twice gives

    ||D^2 H||inf;B_(1/2) <= C(||U||inf;B1+||g||inf).

The distribution D_ij Gamma is its principal-value kernel plus a bounded multiple of the delta distribution. Away from zero the kernel is O(|X|^(-2)) and its angular mean is zero. For X in B_(1/2), split the integral defining D^2 V(X) into |X-Y|<delta and its complement, with 0<delta<=1/8. The cutoff is one on the first set. Subtract g(X) in that set and use the Lipschitz bound; its contribution is at most C delta ||grad g||inf. The remaining integral is at most C||g||inf(1+log(1/delta)), including the contact term. With

    delta=min(1/8, ||g||inf/(||g||inf+||grad g||inf)),

we obtain, when ||g||inf>0,

    ||D^2 U||inf;B_(1/2)
      <= C[||U||inf;B1+||g||inf(1+log(2+||grad g||inf/||g||inf))].

If g=0, the harmonic argument alone proves the conclusion. Dividing by ell^2 yields

    ||D^4 W||inf;B_(ell/2)
      <= C[M2 ell^(alpha-2)+M(1+log(2+ell L/M))].     (3)

The M term is defined as zero at M=0. This proof keeps all scaling factors and does not silently use an L-infinity endpoint Schauder estimate.

## Substitution and summability

For B>=0 the function F_B(x)=x[1+log(2+B/x)] is increasing for x>0, because

    F_B'(x)=1+log(2+B/x)-B/(2x+B)>0.

It is increasing in B as well. Thus upper bounds for M and L may be inserted even when the actual M is arbitrarily small. Since ell is comparable to r,

    ell L/M_bound <= C r^(1-P0+p),

and the logarithm of 2 plus this quantity is at most C(1+|log r|). Formula (3) proves (1). It follows that

    d_n <= C[R_n^(q+alpha-3)+(1+n)R_n^(q-1-p)].       (4)

When p<q-1, the explicit majorant on the right is summable if and only if alpha>3-q. Indeed R_n^delta is geometric for delta>0, constant for delta=0 and increasing for delta<0; the second term is a polynomial factor times a decaying geometric sequence. This assertion concerns the majorant, not the actual d_n. Failure of the sufficient exponent condition does not imply failure of summability for a particular solution.

The weighted-source theorem now implies ell_5=0. For the sharper estimate (2), q>3 and (1) imply |D^4(f,W)|<=C r^(-2)Lambda(r), Lambda=1+log(r0/r). The bounded second derivatives and Taylor's formula on segments of length at most c r give |D^3(f,W)|<=C r^(-1)sqrt(Lambda). In the notation of the weighted-source proof,

    K=f_yyyy-(f_y/a)a_yyy,
    (W.grad+4b_y-1)K=F,
    |K|<=C r^(-2)Lambda,    |F|<=C|y|r^(-3)Lambda.

Follow a backward characteristic from (-r,y) to its first lateral exit |Y|=kappa R. Its integrating factor J satisfies J|Y|/|y|<=C(R/r)^q. The exit contribution after division by |y| is at most C r^(-q)R_exit^(q-3)Lambda(R_exit), which tends to zero as y tends to zero. The integrated forcing is at most

    C r^(-q) int_0^r R^(q-4)Lambda(R)dR
      = C r^(-3)[Lambda(r)/(q-3)+1/(q-3)^2].

The correction (f_y/a)a_yyy divided by |y| has the same bound by parity and the fourth derivative estimate. Taking y to zero proves (2). This calculation identifies explicitly why the strict condition q>3 is used.

## The logarithm cannot be removed under just these norms

Let chi_epsilon(r) be nonnegative and smooth, supported on epsilon<r<1/2 and equal to one on 2 epsilon<r<1/4. Define

    g_epsilon(r,theta)=-chi_epsilon(r) cos(2 theta),
    u_epsilon=Gamma*g_epsilon.

The sources and the potentials are uniformly bounded. The latter follows directly from the local integrability of the logarithm and the common compact support. At zero,

    partial_11 u_epsilon(0)
      = (1/(2 pi)) int_0^infinity chi_epsilon(r) dr/r
                    int_0^(2 pi) cos^2(2 theta)dtheta
      = (1/2) int_0^infinity chi_epsilon(r) dr/r
      >= (1/2) log(1/(8 epsilon)).

Thus the second derivatives are unbounded as epsilon tends to zero while the displayed L-infinity data remain bounded. There is no local contact contribution at zero because the source vanishes there. This is a Poisson counterexample, not an IPM solution. The accompanying independent modal integration reproduces the logarithmic growth.

## Audit of the transport examples and exact scope

The earlier transport-only examples have |D^4 f|<=C r^(3-q), |D^5 f|<=C r^(-q). On the full range 1<A<2, they satisfy the nonnegative-exponent density hypothesis with

    p=max(q-3,0),    P0=q.

The draft's p=q-3 is invalid when q<3 because it violates p>=0; the maximum repairs the statement. Since p<q-1 and these examples are C^3, any alpha<1 can be used. If alpha>3-q, equation (1) would give D^4 W=o(r^(1-q)), contrary to the independently verified cutoff-layer lower bound |a_yyyy| comparable to r^(1-q). This is consistent with their nonzero curl defect. It does not prove the density bounds for a coupled profile.

Low regularity and the local velocity law without transport give no a priori polynomial bound for these norms. To see this, take disjoint odd-in-y smooth packets centered at (-3R_n/4,0), with radii h_n<R_n/100 and density amplitudes 2^(-n)h_n^(2+alpha). Their C^(2,alpha) norms form a summable series, while their fourth-derivative suprema equal a nonzero shape constant times 2^(-n)h_n^(alpha-2). Choosing h_n small makes d_n exceed any prescribed finite sequence. Applying the compactly supported canonical velocity operator preserves C^(2,alpha): after commuting two derivatives, the kernel cancellation bounds the C^alpha norm by splitting near and far increments at the separation of the observation points. Subtract its affine Taylor field and add (As,y) to impose the source jets. The subtracted affine field has zero divergence and curl because the packet density has zero first derivatives at P. These local pairs obey divergence and curl and have the specified parities. They are not asserted to obey transport or a fixed global gauge. Therefore a missing bound must use the coupled equations, rather than low regularity and elliptic inversion separately.

## Improvement when third velocity derivatives are bounded

Suppose in addition that D3W is uniformly bounded on the larger cone (a slightly larger cone than the estimate's target suffices). In every interior ball B_ell(Z), the second derivative u used above now obeys |u(X)-u(Z)|<=C ell by the mean-value formula. Repeating the identical Newtonian decomposition replaces M2 ell^(alpha-2) in (3) by C ell^(-1). Consequently

    |D4W|<=C[r^(-1)+r^(-p)(1+|log r|)],
    d_n<=C[R_n^(q-2)+(1+n)R_n^(q-1-p)].

For every 1<A<2, q>2 and p<q-1, both exponents are positive. No condition on the class exponent alpha is then needed. This additional bounded-third-derivative assumption is not deduced from the baseline class. The argument proves the new clause (J) in the lead's o29/D11 draft.

In the local packet example, the exact lower bound needed for arbitrarily large d_n is the density's fourth-derivative supremum c_F 2^(-n)h_n^(alpha-2) on its disjoint support. No comparability estimate for the nonlocal velocity's fourth derivatives is required. If a statement about the whole pair's exact order is desired, the h_n can be selected recursively to dominate the earlier packets and to make later packets' tails small; that extra selection is avoidable by stating only the density norm.
