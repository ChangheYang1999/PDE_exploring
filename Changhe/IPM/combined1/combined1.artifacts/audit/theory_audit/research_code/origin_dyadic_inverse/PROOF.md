# Origin inverse obstruction in the dyadic graph norm

Status: new T4 theory, OPEN pending independent Opus review. No candidate exclusion may use this note before the proof and its numerical inputs are independently checked.

## 1. Statement with the actual input hyperplane

Use exactly Y=Y_(a,s,Rw) of ../dyadic_weighted_closure/PROOF.md, with 0<a<2, 0<s<1, q=2+s, any fixed Rw>0, and the same fixed smooth radial cutoffs. The low norm is L2((1+r^2/Rw^2)^(-a)dX). The remaining summands are the local H^q norms of both h and its canonical velocity U[h], with shell factors2^((1-a)j). All functions are S1 and real. Complexification is unnecessary for the inverse assertion below.

Let c>1 and let L=V.grad-1+U[.].grad rho, V=cX+U[rho]. Assume the normalized origin identities

    V(0)=0, DV(0)=diag(2c-1,1), grad rho(0)=(0,a0), a0>0. (1)

Assume V is globally Lipschitz. For an integer m>q, assume its derivatives of orders1 through m+2 and the derivatives of grad rho through order m+1 are bounded. Let the low realization of L be the injective maximal distributional realization in the dyadic theorem. Suppose its high estimate is

    Y(L^(-1)f)<=M Y(f) for every f in Y with f_y(0)=0.     (2)

As in that theorem, the inverse exists on the stated inputs; M is finite. In particular the uniform hypothesis(H) implies(2) by taking k=0.

Define alpha_v=q-c-1 and alpha_h=q(2c-1)-c-1-a0. Then:

1. If zero is between alpha_h and alpha_v with alpha_h<=alpha_v, estimate(2) is impossible.
2. If alpha_v is nonzero, estimate(2) requires M>=1/|alpha_v|. The analogous lower bound holds using nonzero alpha_h.

A useful campaign specialization is

    1<c<2,   a0>=5c-4.                                  (3)

For q=2+s<3, this implies alpha_h<0. Consequently(2) requires

    0<s<c-1,   M>=1/(c-1-s).                            (4)

Unlike an energy numerical-range bound, this is a necessary condition on the actual stationary inverse with the actual hyperplane f_y(0)=0. No projected output operator is substituted for L.

## 2. A rescaling lemma including the nonlocal tail

For S1 Schwartz f put E_epsilon f(X)=epsilon^(q-1)f(X/epsilon), 0<epsilon<=1, and

    Z_q(f)^2=||f||dotHq^2+||U[f]||dotHq^2.

The following two properties hold:

    Y(E_epsilon f) -> Z_q(f),                           (5)
    Y(E_epsilon f) <= C S_N(f),                         (6)

where N=m+8, S_N(f)=max_(|k|<=m+1) sup_X <X>^N |D^k f(X)|, and C depends on a,s,Rw and the fixed cutoffs, not on epsilon or f. Also

    ||f||dotHq <= Z_q(f) <= sqrt(2)||f||dotHq,            (7)

because the squared Euclidean symbol of U is p(xi)=xi_x^2/|xi|^2 in[0,1].

Here are details ensuring that the velocity in(5)-(6) is controlled globally. An S1 Schwartz function has integral zero. The standard canonical kernel formula for a second-order Riesz transform consists of a fixed local multiple of f and a principal-value homogeneous kernel K of degree-2 with smooth angular part and zero circular average. Direct Taylor expansion of this formula gives, for |X|>=4 and 0<=k<=m,

    |D^k U[f](X)| <= C_m S_N(f)|X|^(-3-k).               (8)

For completeness fix r=|X|, and split f with a smooth cutoff eta(Y/r) supported in |Y|<=r/2 and equal to1 on |Y|<=r/4. In differentiating at this fixed X, keep r and the cutoff fixed. For the inner part, subtract D^k K(X) from D^k K(X-Y). The difference is bounded by C r^(-3-k)|Y|. The omitted mass equals minus the mass of the outer part because integral f=0, and its contribution is bounded by C S_N(f)r^(-N-k). For the outer part commute derivatives through U. Its derivatives through order m+1 are bounded by C S_N(f)<Y>^(-N) on their support. In the kernel integral, |X-Y|<=1 is bounded using cancellation and one derivative; 1<|X-Y|<=r/4 is bounded by C S_N(f)r^(-N)log r; and |X-Y|>r/4 is bounded by C r^(-2)||D^k f_outer||_1 <= C S_N(f)r^(-N). The contact term is bounded by the same decay. Since N=m+8, all these terms satisfy(8). The same r^(-3-k) bound for f itself follows directly from S_N. On bounded regions the Sobolev multiplier bound controls U[f]. This proves all tail estimates used below, with no deletion of the contact term.

The low term in Y(E_epsilon f) is at most epsilon^q||f||_2, and hence tends to zero. For either v=f or v=U[f], (8) and the chain rule imply on the fixed shell cutoff, for j>=1,

    ||chi(.) E_epsilon v(2^j .)||Hq
       <= ||chi(.) E_epsilon v(2^j .)||Hm
       <= C S_N(f) epsilon^(q+2) 2^(-3j).                (9)

For epsilon near1 and the finitely many points with 1<=|2^j X/epsilon|<4, the same estimate holds after changing C, using local smoothness bounds controlled by S_N and the kernel formula. Thus all shell squares are bounded by a constant times

    S_N(f)^2 epsilon^(2q+4) sum_(j>=1) 2^(-2(2+a)j),

and tend to zero. Outside the core plateau, the same tail calculation gives

    ||(1-chi0) E_epsilon v||Hq <= C S_N(f)epsilon^(q+2)

for small epsilon. The global Bessel norm has the exact formula

    ||E_epsilon v||Hq^2
       =integral (epsilon^2+|xi|^2)^q |hat v(xi)|^2 dxi
       ->||v||dotHq^2.

This proves(5). To prove(6) for every epsilon<=1, multiplication by chi0 is bounded on Hq: Fourier convolution, the inequality <xi>^q<=C_q<xi-eta>^q<eta>^q, and Young's inequality prove this directly for the fixed smooth cutoff. Use ||E_epsilon v||Hq<=||v||Hq, the L2 multiplier bound for U, and(9). This proves(6).

## 3. Frozen tests and localization errors in Y

Section2 to Section4 of ../origin_spectral_line/PROOF.md constructs real S1 Schwartz tests w_n, with smooth compact Fourier support away from the axes, such that

    ||w_n||dotHq=1,
    ||(L0-lambda)w_n||dotHq ->0,                         (10)

for real lambda equal to either alpha_v or alpha_h, or any value between them when alpha_h<alpha_v. Here

    L0w=diag(2c-1,1)X.grad w-w-a0 Qw,
    hat Qw=p(xi)hat w.

To recall the substantive step, logarithmic frequency coordinates u=log xi_y and v=log(xi_x/xi_y), with the exact homogeneous Sobolev weight, turn L0 into

    -partial_u-(2c-2)partial_v+alpha_v
                        +(alpha_h-alpha_v)e^(2v)/(1+e^(2v)).

Boundary packets are long cutoffs centered at v=+-n^2. For an interior lambda the v profile is

    exp((alpha_v-lambda)v/(2c-2))
                   (1+e^(2v))^((alpha_h-alpha_v)/(4c-4)),

which decays at both ends. Long cutoffs in u and v give(10). A purely imaginary positive-quadrant Fourier amplitude with S1 extension gives real tests. Thus the dependencies from that note are explicit and do not concern an assumed full-space spectral theorem.

The exact localization error is

    L E_epsilon w-E_epsilon L0w=E_epsilon R_epsilon(w),
    R_epsilon(w)=(V(epsilon X)/epsilon-DX).grad w
                   +(grad rho(epsilon X)-(0,a0)).U[w].  (11)

For every fixed w_n, U[w_n] is Schwartz as its multiplier is smooth on the compact frequency support. Under the coefficient assumptions, R_epsilon(w_n) is S1 Schwartz to the finite orders needed here and

    S_N(R_epsilon(w_n)) ->0.                            (12)

Indeed on each fixed compact set all coefficient differences and their derivatives converge uniformly to zero. Globally the first coefficient is bounded by C|X|, its first derivatives are bounded and its higher derivatives carry positive powers of epsilon. The second coefficient and its derivatives are bounded. The fixed Schwartz factors give an integrable and uniformly vanishing tail in every weighted supremum of the finitely many derivatives in S_N. Combining(6),(11),(12) proves that the Y norm of the localization error tends to zero. There is no interchange of a limit in epsilon with the sequence n.

The word Schwartz in the preceding paragraph can be replaced by finite weighted smoothness through m+1 throughout: that is all the rescaling lemma uses. The assumptions on the background do not require bounded derivatives of every order.

## 4. Exact strain pinning and the forcing hyperplane

Choose a real S1 Schwartz g with smooth compact Fourier support away from the axes and c[g]=partial_y U2[g](0)=1. Such a function exists: take the positive-quadrant Fourier amplitude to be a nonzero imaginary nonnegative bump, extend with S1 parity, and rescale by its nonzero strain integral. The multiplier -xi_x^2/|xi|^2 times i xi_y has fixed nonzero sign against this amplitude on that quadrant. Then g and U[g] are Schwartz, and Lg has the finite weighted smoothness required by Section2. In particular g,Lg belong to Y.

For each fixed w_n define

    h_(n,epsilon)=E_epsilon w_n-c[E_epsilon w_n]g.         (13)

The strain is exactly zero. Homogeneity gives

    c[E_epsilon w_n]=epsilon^(q-2)c[w_n] ->0,

since q>2. Equations(5),(7),(10)-(12) imply, after first choosing n and then epsilon sufficiently small,

    Y(h_(n,epsilon)) -> Z_q(w_n),
    Y((L-lambda)h_(n,epsilon))
       <= Z_q((L0-lambda)w_n)+o_epsilon(1).              (14)

The factor Z_q(w_n) is between1 and sqrt2. A diagonal choice and normalization therefore produces real h_n with

    Y(h_n)=1, c[h_n]=0, Y((L-lambda)h_n)->0.             (15)

Both h_n and Lh_n lie in Y and in the maximal low graph domain. The latter assertion is concrete: h_n and U[h_n] are finite linear combinations of compact-frequency Schwartz functions, V has at most linear growth, and grad rho is bounded. Thus Lh_n lies in the low space and the distributional graph condition is satisfied.

Set f_n=Lh_n. Its derivative at the origin is exactly zero. To check rather than assume this condition, parity gives h_n(0)=U[h_n](0)=0. Differentiate Lh_n at0 using(1): the y-linear transport term is h_(n,y)(0), which cancels -h_(n,y)(0), leaving

    (Lh_n)_y(0)=a0 c[h_n]=0.                            (16)

The canonical strain in(13),(16) includes its local term. Because the low operator is injective and h_n is in its domain, L^(-1)f_n=h_n. Estimate(2) therefore requires

    1<=M Y(f_n).

By(15), Y(f_n)->|lambda|. If lambda=0 this is impossible; otherwise M>=1/|lambda|. This proves Section1, including the exact input hyperplane, without requiring L to map ker c into itself.

## 5. A sharper necessary residual ceiling

Assume(3), the dyadic theorem's positive low energy rate beta, and its closure inequalities. The previously audited far-field rate theorem gives

    beta<=beta_infinity(a)=1+c-ca.

For every actual velocity bound C_U, the closure inequalities and(4) imply

    Y(F)< beta_infinity(a)/(C_U+a)
                      (c-1-s)sqrt(4 pi s(1+s)),
    0<s<c-1.                                           (17)

Here the strict inequality comes from C1 R(C_U+a)<beta, whereas M Y(F)<=R and M>=1/(c-1-s) are non-strict. All registered choices of C_U are at least1. More generally a valid weighted S1 velocity norm bound is at least1, by high-frequency packets with nearly horizontal frequency direction in a fixed region and their disjoint S1 reflections. Thus a weaker necessary ceiling independent of the velocity estimate is

    Y(F)< H(c-1) beta_infinity(a)/(1+a),                 (18)
    H(d)=max_(0<s<d) (d-s)sqrt(4 pi s(1+s)), 0<d<1.

Differentiate the square. Its only interior maximum is at

    s_star=(2d-3+sqrt((2d-3)^2+16d))/8,
    H(d)=(d-s_star)sqrt(4 pi s_star(1+s_star)).           (19)

Both endpoints give zero. A directed upper bound for(19), combined with the audited lower bound

    Y(F)>=5^((a-2)/2) N_a(F),

or with any finite angular projection of N_a, gives a new exclusion test. For a cell[l,h], monotonicity yields the sufficient obstruction

    5^((l-2)/2) N_projected(h)
          >= H_upper (1+c-c l)/(1+l).                   (20)

The right side is decreasing in a because its derivative is -(1+2c)/(1+a)^2. A strict positive interval margin is the preferred numerical test. This ceiling uses the actual inverse rather than a reciprocal energy-rate conjecture. No numerical value or candidate exclusion is claimed until the separate arithmetic is completed and independently checked.

## Dependencies and scope

The frozen packet calculation is stated explicitly in Section3 and fully proved in ../origin_spectral_line/PROOF.md. The dyadic norm and conditional theorem are T4-058, the weighted-Laplacian lower comparison is T4-107, and the low far-field rate upper bound is the audited TP-3. Sections2 and4 are the new transfer arguments. Their tail estimate retains the nonlocal velocity and the canonical contact term, and Section4 enforces the actual forcing hyperplane.

This theorem obstructs one stationary high inverse in one fixed norm and, through(17)-(20), one conditional closure scheme. It neither refutes nearby exact solutions in other spaces nor proves any new inverse. The assumptions(1),(3), coefficient bounds, and maximal low realization must be checked for each reference. No Lean or Lake build is used.
