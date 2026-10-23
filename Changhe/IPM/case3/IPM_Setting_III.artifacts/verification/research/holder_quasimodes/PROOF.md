# Smooth approximants and the norm dependence of a quasimode

Date: 2026-10-20. Status CONFIRMED under the stated norm and background hypotheses, with independent exact and convolution checks passed at2026-10-20T16:25:15Z and a final proof reread at 2026-10-20T16:27:51.432373+00:00. This is an independent reconstruction of the substantive conditioning claims in the lead's scal1 proof. It concerns linear operators with precisely stated norms. It does not construct a nonlinear profile or give a nonexistence theorem.

## 1. Operator and statements

For A>1 and real a define, on smooth compactly supported even-x odd-y densities,

    Lh=(A x partial_x+y partial_y-1)h+a U[h]_2,
    U[h]=(-chi_y,chi_x), -Delta chi=h_x.

The velocity is the canonical decaying full-plane inverse. Write B=A-1 and ell=(A+1)/2. The following conclusions hold.

1. If a>=0, ||Lh||_2>=(A+3)||h||_2/2. More generally the exact Sobolev energy in Section 2 supplies lower bounds outside a specified interval of orders.
2. For every 1<d<2, at A=d and a=(d-1)(d+3) there are smooth compactly supported h_T, all jets zero at zero, with uniformly positive and bounded C1,d-1 norms, but ||Lh_T||_C1,d-1<=C/T. Their canonical strains and far-field amplitudes vanish.
3. The same quasimodes persist for a smooth background with the same source jet, subject to the global multiplication assumption in Section 5. A separate sharp far-field weighted norm admits distant quasimodes at smooth compactly supported backgrounds with any prescribed source data.
4. These statements do not imply a singular-value law for an unspecified discretization. The two norms must be specified and convergence to a continuum graph domain must be verified.

## 2. Energy in two different norms

A unitary Fourier transform has U_2 multiplier -xi_1^2/|xi|^2. Integration by parts gives

    Re<Lh,h>_L2=-(A+3)||h||_2^2/2
                -a integral (xi_1^2/|xi|^2)|hhat|^2.

For a>=0, Cauchy-Schwarz proves statement 1. In the homogeneous Sobolev norm of order s>=0, the Fourier transform of the transport part is

    -A xi_1 partial_1 hhat-xi_2 partial_2 hhat-(A+2)hhat.

Integrating against |xi|^(2s) conjugate(hhat) gives exactly

    Re<Lh,h>_Hdot^s
      = integral |xi|^(2s) [s-(A+3)/2
                       +(sB-a)xi_1^2/|xi|^2]|hhat|^2.   (1)

A frequency cutoff justifies the integration at zero; oddness gives hhat=O(|xi|), and s>=0 is sufficient. Both endpoint coefficients have the same nonzero sign when s is below both thresholds or above both thresholds, where the thresholds are

    (A+3)/2, [a+(A+3)/2]/A.

The minimum of their absolute values is then a lower-bound constant. The interval between them is not decided by this estimate. At A=3/2,a=9/4,s=3/2, (1) has coefficient -3/4-(3/2)xi_1^2/|xi|^2, although the Holder quasimodes below exist at this same s. The norm matters.

For a background operator P_b h=W_b.grad h-h+U[h].grad rho_b, assume div W_b=2ell and grad rho_b=a e2+O(r^2) at zero. For h supported in B_epsilon, the error in its L2 pairing is bounded by C epsilon^2 ||U[h]||_2||h||_2. The vector velocity multiplier has norm at most one. Thus for a>=0,

    ||P_b h||_2 >= (ell+1-C epsilon^2)||h||_2.           (2)

This uses the support of h in the pairing, even though U[h] is not supported there.

## 3. Exact canonical stream of a sine-one radial field

Let h=yF(r) be smooth and compactly supported away from zero. Then h_x=(r F'/2)sin2theta. The regular and decaying radial Green formula is

    chi_2(r)=1/4 [r^-2 integral_0^r s^3 (s F'/2)ds
                     +r^2 integral_r^infinity s^-1(s F'/2)ds].

Integration by parts cancels the local F(r) terms and gives

    chi(r,theta)=-sin2theta/(2r^2) integral_0^r s^3 F(s)ds. (3)

It vanishes identically inside the density's inner radius. Outside its outer radius it is a multiple of r^-2 sin2theta. Both properties fix the harmonic freedom. In particular its center strain is zero. Formula (3) follows from the canonical inverse; no freely chosen stream is retained after a cutoff.

For a homogeneous field h_0=r^d sin theta with 1<d<2, the local homogeneous inverse is chi_0=-r^(d+1)sin2theta/[2(d+3)]. Its superlinear growth makes this a local indicial calculation, not a globally admissible density. The sin theta and sin3theta coefficients of Lh_0/r^d are respectively

    [(A+3)(d-1)-a]/4,
    (d-1)[B-a/(d+3)]/4.                                 (4)

At A=d,a=(d-1)(d+3), both vanish.

## 4. A cutoff whose nonlocal error tends to zero

Choose eta in C-infinity_c((-1,1)), with eta=1 near zero. Set

    alpha=d-1, epsilon=e^-T,
    a_T(r)=eta((log r+2T)/T), h_T=r^d a_T(r)sin theta.

The support lies in e^-3T<r<e^-T. Every h_T extends smoothly by zero across the origin, with all jets zero. Derivatives through order two satisfy |D^j h_T|<=C r^(d-j), with constants independent of T>=1. This implies the uniform upper C1,alpha bound: for a pair with separation comparable to its radii use the first derivative bound; for a closer pair use the second derivative and the mean value theorem. Pairs crossing the support boundary satisfy the same bounds by smooth extension. The lower bound follows by comparing partial_y h_T(0,e^-2T)=d e^-2Talpha with partial_y h_T(0,0)=0. Thus

    d <= [D h_T]_Calpha <= C,
    ||h_T||_C1,alpha <= C.                               (5)

For its exact stream, define

    Q_T(r)=r^(-d-3) integral_0^r u^(d+2)a_T(u)du
          =integral_0^infinity e^(-(d+3)v)a_T(r e^-v)dv.

Writing D_r=r partial_r, subtract a_T(r) under the last integral. Since ||D_r^(j+1)a_T||_infty<=C_j T^(-j-1),

    ||D_r^j(Q_T-a_T/(d+3))||_infty<=C_j/T, j>=0.        (6)

The exact relation D_r Q_T=a_T-(d+3)Q_T will also be useful. Formula (3) is chi_T=-r^(d+1)Q_T sin2theta/2. Differentiate this expression in Cartesian coordinates and substitute into L. Using A=d and a=(d-1)(d+3), the only nonzero angular coefficients are

    (Lh_T)_1/r^d=(d+3)D_r a_T/4,
    (Lh_T)_3/r^d=(d-1)[D_r a_T/4
                        +(d+3)(Q_T-a_T/(d+3))].         (7)

This displays both the transport cutoff error and the error of the canonical stream. Equation (6), with enough derivatives, proves

    |D^j Lh_T|<=(C/T)r^(d-j), 0<r<=epsilon, 0<=j<=2.

For r>=epsilon, a_T=0 and Q_T(r)=Q_T(epsilon)(epsilon/r)^(d+3). Equation (6) at epsilon gives |Q_T(epsilon)|<=C/T. Hence

    |D^j Lh_T|<=(C/T)epsilon^(d+3)r^(-3-j), r>=epsilon. (8)

The preceding two-point Holder estimate, with pairs crossing r=epsilon split at that radius, yields ||Lh_T||_C1,alpha<=C/T. This and (5) prove the second statement. Since the fields are compactly supported, their leading growing far-field traces also vanish.

Their L2 norms tend to zero. Nothing in this proof says that ||Lh_T||_2/||h_T||_2 tends to zero, so (1) and (2) are respected.

A fixed rescaling cutoff would not suffice. Indeed for E_d=r partial_r-d and u=r^s v(log r), at a maximum of |v| one gets

    ||E_d u||_(s) >= |s-d| ||u||_(s),
    ||u||_(s)=sup_r r^-s|u(r)|.

Long logarithmic cutoffs approach this lower bound. Their vanishing ratio occurs at the critical weight s=d in this scalar model, not at every weight below a regularity ceiling.

## 5. Background perturbations and a separate far-field obstruction

Suppose W_b=(Ax,y)+O(r^3), grad rho_b=a e2+O(r^2), and the background is smooth near zero. Assume grad rho_b has bounded global C1,alpha norm. This last condition is explicit; it may be replaced by weighted multiplication estimates that control the decaying tail in (8). For an exact smooth primary profile it now follows from ../local_ipm_continuation/PROOF.md, since all higher derivatives have the proved sublinear symbol bounds. The quasimode construction still concerns only the stated special values A=d and a=(d-1)(d+3), not every exact profile.

On the support of h_T, the difference (W_b-(Ax,y)).grad h_T has C1,alpha norm <=C epsilon^2. The local product U[h_T].(grad rho_b-a e2) has the same bound. On epsilon<r<1, the latter product has derivatives of order j<=2 bounded by (C/T)epsilon^(d+3)r^(-1-j), from (3) and the quadratic vanishing of the coefficient. Its C1,alpha norm is <=C epsilon^2/T. Beyond r=1 the global coefficient assumption and tail give C epsilon^(d+3)/T. Consequently

    ||P_b h_T||_C1,alpha / ||h_T||_C1,alpha
                       <= C/T+C e^-2T.                  (9)

The h_T have bounded norm also in the transport graph norm ||h||_C1,alpha+||W_b.grad h||_C1,alpha: on their support W_b=O(r), and differentiating through the Holder estimate costs no negative power beyond those already in (5). Thus a bounded-below claim in that graph norm fails too. Neither statement extends automatically to stronger smoothness norms.

For a distinct far-field example, choose a smooth nonnegative radial cutoff chi, one near zero and compactly supported. Let

    rho_b=a y chi(r)+k(3x^2 y-y^3)chi(r),
    J=integral_0^infinity r chi(r)dr,
    k=(a/4-B/2)/J.

The exact strain formula gives c=-B/2=1-ell, hence the prescribed source jet. This background need not solve transport. Its velocity is O(r^-3) with differentiated bounds, by its mode-two and mode-four Green formulas. For noninteger s=m+alpha>0 define

    ||h||_(s,p)=||h||_Cs(B2)
       +sup_(R>=1) R^-p||h(R .)||_Cs({1<|X|<2}), p=1/ell.

Put v_T=r^p eta((log r-2T)/T)sin theta. It is supported in e^T<r<e^3T and its weighted norm is bounded above and below. Formula (3) shows U[v_T]=0 inside its inner radius, which contains the support of grad rho_b for large T. Therefore U[v_T].grad rho_b is identically zero. Since ell p=1, the Euler transport of v_T differentiates only the logarithmic cutoff, of norm O(1/T). The background transport U_b.grad v_T has norm O(e^-4T). Thus

    ||P_b v_T||_(s,p) / ||v_T||_(s,p)
                         <= C_s/T+C_s e^-4T.             (10)

Both the center jet and the growing far-field trace of each v_T vanish. This shows why source data alone cannot prove a lower bound in a sharp far-field weight. It does not concern the stronger topology with an explicitly retained r^p leading term and a remainder of weight q<p, and it does not supply a counterexample at an exact nonlinear profile.

## 6. Scalar approximation rates and the missing discrete norm

For delta>0 and n>=1, the Chebyshev coefficient of r^delta on 0<=r<=1, using r=(1+x)/2, is

    c_n=2^(1-2delta) Gamma(2delta+1)
                    /[Gamma(delta+n+1)Gamma(delta-n+1)]. (11)

To check constants, put I_n=integral_0^pi cos^(2delta)(theta/2)cos(n theta)dtheta, so c_n=2I_n/pi. The beta integral gives I_0 and I_1=delta I_0/(delta+1). The identity (1+cos theta)f'=-delta sin theta f, integrated against sin(n theta), gives

    2n I_n+(n+1+delta)I_(n+1)+(n-1-delta)I_(n-1)=0.

The expression (11) satisfies the recurrence and initial data. Reflection and Stirling's formula give c_n=(-1)^(n+1)C_delta n^(-2delta-1)(1+O(n^-1)) for noninteger delta. Summing absolute values gives the uniform tail upper bound O(N^-2delta). At x=-1 the eventual signed terms have one sign, proving the matching lower order. The jth derivatives of T_n at -1 have size comparable to n^(2j) and the same eventual sign after the coefficient is included. Thus for integers 0<=j<delta the differentiated tail has order N^(-2(delta-j)). Integer delta gives a polynomial. These are rates for this scalar series only.

For a discrete matrix J and positive-definite Gram matrices M_D,M_Y, the smallest singular value representing specified domain and residual norms obeys

    sigma^2=min_(z!=0) (Jz)^*M_Y(Jz)/(z^*M_D z).          (12)

Equivalently it is the Euclidean singular value of M_Y^(1/2) J M_D^(-1/2). Changing coordinates requires transforming the Gram matrices too. Raw Euclidean values after arbitrary row or column scaling have no invariant functional-analytic meaning.

If trial vectors approximate a continuum h_T in both domain and image norms with error epsilon_N, (9) gives only the conditional upper bound sigma_N<=C/T+C e^-2T+C epsilon_N. No relation between T and resolution follows without an approximation estimate for the actual scheme. Conversely discrete lower bounds pass to a closed continuum operator only after approximation of a graph core and convergence of its residual norm have been established. Apply the inequality to each core approximant, take its limit, and use graph density. A raw matrix singular value does not supply those hypotheses.

## 7. Dependencies and verification scope

Dependencies are the canonical modal inverse, the explicit strain identity, elementary Fourier integration by parts, two-point Holder estimates, and the beta/gamma identities proved through (11). This proof independently checks scal1 Sections 5-8. Scaling and forced-branch statements in its Sections 1-4 were independently checked in the earlier forced_structure result; none of these linear-space arguments establishes a nonlinear implicit-function theorem with derivative gain.

Exact polynomial/trigonometric checks and numerical convolution checks are recorded in verification. They are tests of the formulas, not proofs of a continuum norm bound. The proof above supplies the norm estimates and all stated scope qualifications.
