# Local smoothness propagation for the canonical IPM transport equation

Date: 2026-10-20. This is a new independent audit of the propagation argument in the lead's fred27 proof, not a claim that a profile exists. The original source and its hash are retained in verification/. The earlier verifier's D46 is a comparison record, not an input to the argument below.

## Exact statement and hypotheses

Work in R^2. Let 0<alpha<1. Let rho be C^(2,alpha)_loc and satisfy W dot grad rho=rho in distributions, where W=cX+U[rho], c is constant, and U is the fixed full-plane canonical inverse. Assume the admissible parity and sublinear-growth conditions that define this inverse: rho is even in x, odd in y, and |rho(X)| is bounded by C(1+|X|)^gamma for a gamma<1. For the present result, no source or center normalization is needed. The canonical inverse has local multiplier

    m(xi)=(xi_1 xi_2/|xi|^2, -xi_1^2/|xi|^2), xi!=0,

with a smooth separated remainder after a compact spatial cutoff. In particular, for compact eta equal to one on an open set, U[rho]=m(D)(eta rho)+H_eta there, with H_eta smooth. This property follows below from the specified full-plane normalization; it is not an extra freedom to change U.

Let V be an open set on which rho is smooth. Let O consist of points whose forward W-trajectory reaches V in finite time along a compact trajectory arc on which W is nonzero. Then rho and W are smooth on O. The result is local to each finite arc. It gives no bound uniform as an arc approaches a stationary point and no regularity at a stationary endpoint that lies only in the closure of O.

For the positive x-axis application, the second multiplier component is even in xi_2, so it preserves oddness in y. Equivalently, the paired canonical kernel has U_2(x,-y)=-U_2(x,y). In the localized multiplier version, choose eta even in y; its smooth tail then has the same parity. Thus W_2(x,0)=0, and uniqueness of the C^1 flow makes the axis invariant. Assume w(x)=W_1(x,0)<0 on (0,x*) and that V contains a neighborhood of the origin. Each fixed x in this interval reaches a smaller positive point in V in finite time, because w is bounded away from zero on the intervening compact interval. Thus O contains the open axis segment. This conclusion does not include P=(x*,0).

## Localization and the precise multiplier

The velocity is the local term -rho e_2/2 plus the principal-value integral of a degree-minus-two matrix kernel K against rho. K has zero circular mean, derivatives |D^j K(Z)|<=C_j |Z|^(-2-j), and the parity makes the centered-annulus integral of K(-Y)rho(Y) zero. Its normalized integral can therefore use K(X-Y)-K(-Y). At large |Y| this difference is O_X(|Y|^-3). With the density growth bound the radial absolute majorant is C_X r^(gamma-2), integrable because gamma<1. Near zero the removed K(-Y)rho(Y) is locally integrable since oddness and C^1 regularity give rho(Y)=O(|Y|).

Take a compact smooth eta equal to one in a neighborhood of the compact set being considered. Subtract the ordinary compact-input convolution U[eta rho] from the normalized full-plane velocity. The remaining density vanishes near that set. Each positive derivative of the far kernel has radial majorant C_j r^(gamma-1-j), integrable for every j>=1. The undifferentiated far kernel uses the preceding subtraction. On compact subsets, separation controls the bounded part. These locally uniform integrable majorants justify every derivative of the remainder. No derivative of rho is needed in this tail calculation.

For compact input f, the full velocity is exactly m(D)f. The local term is already included in m, so it must not be added again. This follows distributionally by differentiating E=-(2pi)^(-1)log|X|: -Delta E=delta, -partial_12 E=PV K_1 and partial_11 E=PV K_2-delta/2. Any remaining Fourier distribution supported at zero would be a polynomial in space. The compact-input kernel velocity and bounded-multiplier velocity are both in L^2, so their difference is zero. The bounded symbol gives ||m(D)f||_(H^s)<=C||f||_(H^s).

Local C^(k,alpha) mapping follows by annular cancellation. For a kernel piece at scale s<=1, its convolution with a compact C^alpha input has sup norm <=Cs^alpha [f]_alpha and derivative sup norm <=Cs^(alpha-1)[f]_alpha. Sum scales s<=h directly and h<s<=1 after multiplying the derivative bound by h. Both sums are O(h^alpha). At scales s>1 use the compact input's L^1 norm and the kernel bounds Cs^-2 and Cs^-3. Applying this to derivatives proves the local C^(k,alpha) assertion. Consequently W is C^(2,alpha)_loc, and induction can transfer local H^k regularity from rho to U.

## A multiplier commutator that gains one derivative

Let R be any fixed finite matrix of bounded constant multipliers with symbol satisfying |grad m(xi)|<=C/|xi| away from zero. Then

    |eta| |m(eta)-m(xi)| <= C|xi-eta|.                 (1)

If |eta|<=2|xi-eta| use boundedness. Otherwise every point on the connecting segment has norm at least |eta|/2, so the mean value estimate applies. Values at zero do not matter in L^2.

For chi in C_c^(2,alpha), Fourier convolution and (1) give

    ||[chi,R]partial_j f||_2
       <= C || |zeta| chi_hat(zeta) ||_1 ||f||_2.     (2)

The Fourier L^1 factor is finite: choose 0<delta<alpha. The squared Holder-increment integral for D^2 chi converges as integral_0^1 r^(2alpha-2delta-1)dr, so chi lies in H^(2+delta). Cauchy-Schwarz bounds the L^1 factor because integral_R2 |zeta|^2(1+|zeta|^2)^(-2-delta)dzeta is finite. This explicitly identifies why a positive Holder exponent is used.

## One-derivative lemma

Consider a finite system

    P u = W dot grad u + sum B_n R_n u + C u = F.     (3)

Assume globally u in L^2, F in H^-1, W real and in C_b^(2,alpha), and B_n,C in C_b^(1,alpha). On a bounded nonstationary flow tube suppose F in H^1_loc and u in H^1 near the forward end. Then u is H^1 near each earlier point of the arc.

First take a thin C^(2,alpha) flow tube with coordinates (t,s) in which W dot grad=partial_t. One can shorten a periodic arc to its first arrival in the terminal regular set. Uniqueness and compactness give an injective tube around the remaining arc. For a number lambda>0 to be fixed later, choose

    chi=eta(s) exp(lambda t/2) theta(t).

Here theta rises from zero before the point being estimated and falls to zero only in the terminal regular region. Choose a compact cutoff e supported in that region and covering the falling part. Then

    W dot grad(chi^2) >= lambda chi^2 - K_e e^2.      (4)

All cutoffs extend by zero, belong to C_c^(2,alpha), and may depend on lambda. Their norms will affect only constants multiplying known data.

Use the resolvent J_epsilon=(1-epsilon^2 Delta)^-1, u_epsilon=J_epsilon u, and v=grad u_epsilon. Then ||u_epsilon||_2<=||u||_2, ||v||_2<=C epsilon^-1||u||_2, and the exact commutator identity is

    P u_epsilon=J_epsilon F + E_epsilon u_epsilon,
    E_epsilon=-epsilon^2 J_epsilon[Delta,P].          (5)

It follows by multiplying by 1-epsilon^2 Delta, so no asymptotic symbol expansion is used. The needed distributional formulas are

    [Delta,W dot grad]z
       =2 partial_i((partial_i W_j)partial_j z)
           -(Delta W_j)partial_j z,
    [Delta,B]z
       =partial_i((partial_i B)z)+(partial_i B)partial_i z.  (6)

The second formula uses only first derivatives of B.

Put L_epsilon=epsilon^2 partial_l J_epsilon partial_i and M_epsilon=epsilon^2 partial_l J_epsilon. Their L^2 norms are bounded by1 and Cepsilon. Moreover

    ||[chi,L_epsilon]||_(2->2)<=Cepsilon||grad chi||_infty.   (7)

To prove (7), use J_epsilon=integral_0^infty exp(-t)exp(t epsilon^2 Delta)dt. The heat kernel's second derivative has first absolute moment Cs^-1/2 at time s. Multiplication by epsilon^2 and integration gives Cepsilon. The factor chi(X)-chi(Y) is bounded by ||grad chi||_infty |X-Y|. Truncation in t, followed by strong L^2 convergence, justifies this calculation for the distribution kernel; any delta term commutes.

There is a short useful way to estimate grad E_epsilon u_epsilon. Only the terms 2L_epsilon((partial W)v) need a weighted derivative bound. Move chi through L_epsilon: the principal term is bounded by C||DW||_infty||chi v||_2, while (7) and ||v||_2<=Cepsilon^-1||u||_2 bound the commutator by C_chi||u||_2. Every other term is bounded directly by C_chi||u||_2:

- M_epsilon((Delta W)v) uses its epsilon factor and ||v||_2.
- L_epsilon((partial B)R u_epsilon) uses boundedness of L, partial B and R.
- M_epsilon((partial B)R v) uses the epsilon factor and ||v||_2.
- The terms with C are the same with R=I.

Thus

    ||chi grad E_epsilon u_epsilon||_2
       <=K_0||chi v||_2+C_chi||u||_2,                (8)

where K_0 depends on coefficients and the finite system, but not on chi, lambda or epsilon. This estimate requires no third derivative of W and no second classical derivative of B or C.

Also ||chi grad J_epsilon F||_2 and ||e grad J_epsilon u||_2 are bounded uniformly in0<epsilon<=1. Insert smooth cutoffs equal to one near the indicated supports. Their localized inputs are H^1. The separated inputs are H^-1 and L^2, respectively. At a fixed positive separation, the Gaussian integral gives uniform rapidly decaying bounds for every derivative of the resolvent kernel. For the H^-1 input, write it as f_0+partial_1 f_1+partial_2 f_2 with f_j in L^2, which is possible by Fourier multipliers (1+|xi|^2)^-1 and -i xi_j(1+|xi|^2)^-1. Kernel derivatives of one additional order then give the separated bound. Equivalently these kernels are uniformly Hilbert-Schmidt with the observed variable restricted to a compact set.

Differentiate (5) and take the real L^2 pairing with chi^2 v. This is legitimate since v in H^1 and the right hand side is locally L^2 by the bounds just proved. For transport,

    Re integral chi^2 conjugate(v) (W dot grad v)
       =-1/2 integral (W dot grad chi^2 + div(W)chi^2)|v|^2.

The differentiated order-zero terms include (DW)v, B_n R_n v, Cv, and known terms (partial B_n)R_n u_epsilon and (partial C)u_epsilon. Formula(2) moves chi through each R_n acting on v=grad u_epsilon. Their principal bounds depend on coefficient norms, while the commutators multiply only ||u||_2. Combining(4) and(8) therefore yields

    (lambda/2)||chi v||_2^2
        <=K_1||chi v||_2^2+C_chi||chi v||_2+C_chi,    (9)

where K_1 is independent of chi, lambda and epsilon. The e-term is controlled by terminal H^1 regularity. Choose lambda>2K_1+2 and then construct chi. Its possibly large norms cause no circularity: they enter finite constants on known data, independent of epsilon. Inequality(9) bounds chi grad u_epsilon uniformly. Weak compactness and u_epsilon->u in L^2 yield chi grad u in L^2. Since chi is positive near the desired point, this proves the lemma.

## Quasilinear induction and derivative count

The set O in the statement is open by continuous dependence of finite trajectories and is preserved along the relevant arc. Initially rho,U belong to H^2_loc(O). Suppose rho,U belong to H^k_loc(O), k>=2. Choose a compact arc in O ending in V and a slightly larger compact tube contained in O. Let eta be a smooth compact cutoff in O equal to one on that tube, and form the finite L^2 system u_I=partial^I(eta rho), |I|=k.

On the tube, differentiating W dot grad rho=rho gives four groups:

1. W dot grad u_I.
2. Terms with exactly one derivative on W. They are a matrix formed from DW multiplying k-th derivatives of rho.
3. Terms with all k derivatives on W. Since k>=2, partial^I(cX)=0, and localization writes these as grad rho dot m(D)u_I plus a smooth tail multiplied by grad rho. The latter is locally H^1.
4. Intermediate products (partial^J U)grad partial^(I-J)rho for2<=|J|<=k-1.

The last products are H^1 locally. To see the derivative count explicitly, after one more derivative their two factors have orders a,b in[2,k] with a+b=k+2. Regard them as derivatives of D^2 U and D^2 rho. The remaining derivative orders sum to k-2, and each base function is bounded and H^(k-2). The tame estimate

    ||D^r f D^(m-r)g||_2
        <=C_m(||f||_infty||g||_(H^m)
                       +||g||_infty||f||_(H^m))     (10)

with m=k-2 proves the assertion. Undifferentiated terms have one fewer total derivative. For k=3 these are products of bounded D^2 quantities, and their derivatives are covered by m=1; for k=2 the group is empty.

For completeness, (10) follows from the interpolation bound ||D^r f||_(2m/r)<=C||f||_infty^(1-r/m)||D^m f||_2^(r/m). A low-frequency split at length t gives Ct^-r||f||_infty; high-frequency dyadic bands give Ct^(m-r)M(|D^m f|), where M is the Hardy-Littlewood maximal function. Optimizing t, using the L^2 bound for M, then Holder and weighted arithmetic-geometric mean proves(10), including its endpoint cases. The maximal L^2 bound follows from the disjoint-ball covering weak(1,1) bound applied to f1_(|f|>lambda/2), followed by the layer-cake integral. Compact smooth cutoffs give the local version. Mollification extends the calculation to the stated Sobolev classes.

Thus the system has the form(3), with coefficients in C^(1,alpha) and forcing H^1 on the tube. Extend coefficients with a smooth cutoff from a larger bounded neighborhood. This leaves the equation on the tube unchanged and makes Pu in H^-1 globally, since u in L^2. All differentiations are distributional; the transport term has order k+1 only in H^-1, while(10) controls the other products. No H^(k+1) regularity is assumed in deriving the system. Terminal smoothness gives u_I in H^1 near the forward end. The one-derivative lemma therefore gives rho in H^(k+1) near the initial point.

This argument applies to each point of the same open O for every finite k. Induction gives all local integer Sobolev orders, hence all classical derivatives by H^m_loc embedding into C^ell_loc for m>ell+1 in dimension2. Localization transfers smoothness to W.

## Audit verdict and scope

The lemma, localization and quasilinear induction are CONFIRMED by this independent reconstruction, subject to the explicit hypotheses above. The conclusion does not infer smoothness at P, bounded transverse traces there, a nonzero B_j, a coupled solution, a family, or a nonexistence endpoint. It does justify using classical derivatives on compact subsegments of the open axis when a solution is already smooth near the origin. The threshold rho in C^(2,alpha), alpha>0, is used in the cutoff commutator and baseline product bounds; it has not been weakened here.

Verification code will check finite algebraic identities and derivative bookkeeping. Such checks support the reconstruction but are not a substitute for the analytic energy, localization, and compactness arguments.

## Completed second-model review

The first actual Opus5.5 request ended in all-thinking token exhaustion with no final response. The shorter review completed2026-10-20T22:32:53Z, actual response model claude-opus-5-5, end_turn. I read and independently checked its full term-by-term review. It confirms the localization, weighted resolvent lemma and induction, and requests that axis invariance be explicit. The preceding axis paragraph now supplies that parity argument. The word only in the error estimate applies only to grad E_epsilon; the separate order-zero commutators are still handled by(2). No stationary-endpoint claim is added.
