# Weighted limits of two capped nonprofile families

Date: 2026-10-20. Independent reconstruction of lead referee/scap3 Sections5-7 and the related Gaussian cubic identities in referee/scap2 Section7.5. Analytic verdict: CONFIRMED with the correction that an anisotropic Gaussian is Schwartz rather than compactly supported. Every pair below is a nonprofile. These statements give no lower bound for arbitrary exact or approximate profiles.

## Definitions and dependencies

For a canonical smooth pair set a=rho_y(0), h=rho-ay, W=ell X+U and F=W.grad rho-rho. All pairs here satisfy c=psi_xy(0)=1-ell exactly, so no linear correction to F is needed. Put ||v||_m^2=int_R2 v(X)^2 |X|^(-2m)dX, allowing infinite norms where indicated.

The two preceding independent proofs supply explicit constructions and their global bounds:

* `../capped_gaussian_nonprofiles/PROOF.md` proves the Gaussian family, its canonical inverse, sigma=ell-1, and its nonzero transport residual.
* `../capped_local_and_ball_examples/PROOF.md` proves the compact remote-stream family, its canonical inverse, global cap and exactly affine core. Its nonprofile conclusion uses `../strain_cap_flat_exclusion/PROOF.md`.

We repeat the parameters and all limit arguments needed here. Write the capped Gaussian family as

    ell=2, D=1, L=C B, C=1179936, B>=9,
    delta=B/(L+1)^2, t=1-delta,
    rho_B=4t*y*(1+r^2)^(-1/4)+B*y*exp(-x^2/L^2-y^2),
    a_B=B+4t, U_B=t U_b+U_g.

Here U_b is the canonical velocity of rho_b=4y(1+r^2)^(-1/4). Both families have ||sym DU||<=D. The parity extensions imply |U_1|<=D|x| and |U_2|<=D|y| by integrating the corresponding diagonal strain entries from their respective zero axes. Thus |W|<=A r, A=2ell-1. This bound does not require a global bound on the antisymmetric part of DU.

## 1. Gaussian family at a fixed weight

For every fixed 2<m<4,

    lim_(B->infinity) ||F_B||_m/||h_B||_m = R_m > 0,       (1)

with

    R_m^2 = [int y^2 exp(-2y^2)
                  {T(x,y)(1-2y^2)-1}^2 r^(-2m)dX]
             /[C_m J_m],
    C_m=sqrt(pi)*Gamma(m-1/2)/Gamma(m),
    J_m=int_0^infinity s^(1-m)(1-exp(-s))^2 ds,
    T=(2y+(U_b)_2)/y.

The quotient T has its smooth axis extension. In particular

    R_m^2 >= 4 int_(1/2)^infinity s^(3-m) exp(-2s)ds/J_m,
    R_3 >= 1/sqrt(e log2).                               (2)

Proof. The Fourier multiplier of the Gaussian strain entry is

    hat(S_g)_11 = (B*pi*L/2)*xi_x^2*xi_y^2/|xi|^2
                   *exp(-(L^2*xi_x^2+xi_y^2)/4) >= 0.

Its integral is finite. Fourier inversion with a cosine shows |(S_g)_11(X)|<=(S_g)_11(0)=delta; incompressibility gives the same bound for its negative diagonal partner. Coordinate integration gives |(U_g)_1|<=delta|x| and |(U_g)_2|<=delta|y|. Since delta->0, U_B->U_b uniformly on every compact set. Merely using B/L=1/C would not establish this limit.

The density and its first derivatives divided by B converge locally to f_infinity(y)=y exp(-y^2), while a_B/B->1. Therefore

    h_B/B -> y(exp(-y^2)-1)=h_infinity,
    F_B/B -> y exp(-y^2)[T(1-2y^2)-1]=F_infinity.         (3)

The weighted convergence needs uniform control at both endpoints. Near0, h_B/B=O(r^3) uniformly for B>=9. Its gradient is O(r^2). The strain estimate in the preceding proof is

    ||S_g(X)-S_g(0)||<=4B*r^2/L,

and the base has a smooth even strain with quadratic remainder. Integrating the diagonal entries along the zero axes shows U_B-(x,-y)=O(r^3), uniformly in B. Writing rho_B=a_B y+h_B and using (A x,y).grad(ay)=ay proves F_B/B=O(r^3). Outside the unit disc the density, its gradient and |W|<=3r give |h_B|/B+|F_B|/B<=Cr, with a B-independent constant. The squared radial majorants r^(7-2m) near0 and r^(3-2m) at infinity are integrable precisely for2<m<4. Dominated convergence proves the convergence of both squared norms.

For each nonzero y, substitution x=|y|z yields int_R (x^2+y^2)^(-m)dx=C_m |y|^(1-2m), where the constant follows by z=tan(theta) and the beta integral. A second substitution s=y^2 gives ||h_infinity||_m^2=C_m J_m. This is positive. The base cap implies1<=T<=3. On y^2>=1/2 it follows that T(1-2y^2)-1<=-2y^2. Integration in x and then s gives the first bound in(2).

For completeness, a nonnegative integral representation determines J_m without separating divergent signed integrals:

    (1-exp(-s))^2=s^2 int_0^1 int_0^1 exp(-(u+v)s)du dv,
    J_m=Gamma(4-m) int_0^1 int_0^1 (u+v)^(m-4)du dv.      (4)

Tonelli applies and the corner u=v=0 is integrable for m>2. Integrating the square gives

    J_m=Gamma(4-m)*(2^(m-2)-2)/((m-3)(m-2))  for m!=3,
    J_3=2log2.

At m=3 the numerator in(2) is2/e, proving(2). The value is an analytic lower bound, not a decimal quadrature certificate.

An explicit formula used to evaluate T is

    H_b(r)=int_0^1 u^3 (1+r^2u^2)^(-1/4)du
      ={(2/7)[(1+r^2)^(7/4)-1]-(2/3)[(1+r^2)^(3/4)-1]}/r^4,
    H_b(0)=1/4,
    T=2-4H_b-4(x^2/r^2)[(1+r^2)^(-1/4)-4H_b].          (5)

The radial identity r H_b'+4H_b=(1+r^2)^(-1/4) proves the velocity formula; substitution v=1+r^2u^2 proves the displayed integral. Smooth extension handles r=0.

## 2. The cubic-weight endpoint

For each fixed B>=9 define

    b_*=t+B/L^2, e_*=t+B,
    q1=B(1+3L)/(3L^2(L+1)^3),
    q2=B(L+3)/(3(L+1)^3),
    Cx=-6b_*+a_B(t/2+3q1),
    Cy=-2e_*+a_B(t/6+q2).

Then

    lim_(m->4 from below) ||F_B||_m^2/||h_B||_m^2
       =(Cx^2+2CxCy+5Cy^2)/(b_*^2+2b_*e_*+5e_*^2),       (6)
    lim_(B->infinity) lim_(m->4-) ||F_B||_m^2/||h_B||_m^2
       =137/45 = lim_(m->4-) R_m^2.                      (7)

Proof. The density expansion gives h_3=-b_*x^2y-e_*y^3. The base stream is -xy+xy r^2/6+O(r^6). To derive the Gaussian quartic coefficients independently, use alpha=L^-2, beta=1 and

    I(alpha,beta)=int_0^infinity
       (1+4alpha s)^(-3/2)(1+4beta s)^(-3/2)ds
       =1/[2(sqrt(alpha)+sqrt(beta))^2].

The x^3y coefficient of the heat inverse is2B alpha^2[I+(2alpha/3)I_alpha], and the xy^3 coefficient is2B alpha beta[I+(2beta/3)I_beta]. Differentiation under the integral is allowed by the integrable parameter derivatives at positive fixed alpha,beta. Setting beta=1 and alpha=L^-2 gives q1 and q2 as above, with q1+q2=B/(3L^2), confirming the Poisson constraint. Transport at cubic order has linear field(3x,y), so F_3=Cx x^2y+Cy y^3.

For any smooth odd-parity function v=P_3+O(r^5), its inner squared norm is

    ||v||_m^2=int_S1 P_3^2/(8-2m)+O(1), m->4-.

Indeed the P_3^2 radial integral is int_0^1 r^(7-2m)dr; the cross and remainder terms are bounded uniformly as m approaches4. The exterior integrals here are also bounded uniformly. Direct trigonometric integration gives int_S1 x^4y^2=int_S1 x^2y^4=pi/8 and int_S1 y^6=5pi/8, which proves(6). As B->infinity, (b_*/B,e_*/B,Cx/B,Cy/B)->(0,1,1/2,-11/6); their quadratic forms give137/45. Separately, (3) has h_infinity=-y^3+O(r^5) and F_infinity=x^2y/2-11y^3/6+O(r^5). The same cubic argument proves the final equality in(7); no limit interchange is asserted.

## 3. The family with an exactly affine core

Fix ell>1, D=ell-1, A=2ell-1. Use the explicit radial background rho0, U0 and smooth compact functions fstar,Kstar,g from the cited local-and-ball construction: Kstar=-1 on[-1,1], fstar=0 there, g''=y on[-1,1], and both g and Kstar vanish outside[-2,2]. Put

    psir=(b/L) fstar(x/L)g(y),
    rhor=-(b/L^2)fstar'(x/L)g(y)-b Kstar(x/L)g''(y),
    rho=rho0+rhor, a=4D+b, U=U0+Ur,
    L>=max(2,Rstar,16000000*b/D),
    Rstar=(6ell)^(1/(1-1/ell)).

The exact defect is

    F=F0+(ell X+U0).grad rhor-rhor
          +Ur.grad rho0+Ur.grad rhor,
    F0=(ell X+U0).grad rho0-rho0.                         (8)

Both F and h vanish on B1 and grow at most linearly, so their weighted norms exist for every m>2. Let

    G=(ell y+(U0)_2)g'''(y)-g''(y), v=g''(y)-y.

For fixed ell,m:

(a) If b=D L/16000000 and L->infinity, then

    ||F||_m/||h||_m -> ||G||_m/||v||_m > 0.              (9)

(b) If b>0 is fixed and L->infinity through the admissible range, then

    ||F||_m/||h||_m
       -> ||F0+bG||_m/||rho0-4Dy+bv||_m > 0.             (10)

For sufficiently large L, on any given compact set rhor=b g''(y) and Ur=0 exactly. Thus the pointwise limits follow from(8), dividing by b in(a). In(a), b=DL/16000000>=1 for all sufficiently large L; this also controls the fixed F0/b term. Uniform bounds on the cutoff functions and their derivatives, L>=1 and |W|<=Ar give |F|/b+|h|/b<=Cr outside B1 in(a), with a constant depending only on ell and the fixed functions. The same argument without division applies in(b). Dominated convergence uses int_1^infinity r^(3-2m)dr<infinity.

The first denominator is nonzero since v=-y for |y|>2. The second tends to-(4D+b)y as x->infinity at a fixed |y|>2 and is also nonzero. At fixed0<y<1, the radial background has (U0)_2(x,y)->0 as x->infinity, so G(x,y)->Dy. Also F0(x,y)->0: rho0 and (rho0)_y are O(x^(p-1)), (rho0)_x=O(x^(p-2)), (U0)_1=O(x^p) and (U0)_2=O(x^(p-1)), with p=1/ell<1. Each term of F0 therefore vanishes. These limits prove both numerators are nonzero. A nonzero continuous function has a positive squared norm.

At m=3 the first ratio has the explicit bound

    ||G||_3/||v||_3 >= D/[4863 sqrt(375pi) Rstar^(5/2)].   (11)

Indeed on the four rectangles Rstar<=|x|<=2Rstar, 1/2<=|y|<=1, the background strain is bounded by D/2 along each vertical integration segment. Hence |(U0)_2|<=D|y|/2 and |G|>=D/4. These rectangles have total area2Rstar and r^2<=5Rstar^2, proving ||G||_3^2>=D^2/(1000 Rstar^5). The independent cutoff bound |g''-y|<=4863|y|, with zero value for |y|<=1, gives ||v||_3^2<=4863^2(3pi/8) by integrating first in x. This proves(11). There is no uniform bound here for all cutoff choices or joint limits of ell and b.

## 4. Changing the weight toward two

For each fixed member of either family, as m decreases to2,

    ||h||_m^2=pi a^2/[2(m-2)]+O(1),
    ||F||_m -> ||F||_2 in(0,infinity),
    ||F||_m/||h||_m
       ~sqrt(2(m-2))*||F||_2/(|a|sqrt(pi)) ->0.           (12)

At infinity rho=O(r^p), p<1, so h^2=a^2y^2+O(r^(p+1))+O(r^(2p)). The error terms remain absolutely integrable with weight r^-4. The first term integrated over r>1 is exactly pi a^2/[2(m-2)]. At zero, h=O(r^3) or h vanishes on a ball, which leaves a bounded contribution.

For the Gaussian family the radial part has leading degreep=1/2 and its next term has degreep-2. The leading linear transport term vanishes because ell p=1. The Gaussian density is Schwartz, not exactly absent outside a compact set, and its velocity decays; these terms contribute faster-decaying errors for each fixed B,L. Thus the total F is O(r^beta) with beta<1. In the remote-stream family the perturbation is compact and the background has exactly the two radial powers of density degreesp and0 outside r=e; linear transport on the second contributes O(1), and nonlinear transport is O(r^(2p-1))+lower terms, again with exponent less than1. Near0 the same cubic or vanishing estimates hold. Therefore F lies in L2(r^-4 dX), and a fixed radial majorant proves convergence of its norms as m decreases to2. Its norm is positive by the previously proved nonprofile conclusions. This proves(12).

A ratio made small by choosing m close to2 is small in a changing norm. It does not contradict the fixed-m gaps in(1), (9) or(10). Finally under the genuine dilation rho_lambda=lambda rho(X/lambda), both h and F transform by the same rule; their squared norms scale by lambda^(4-2m). Their ratio, a, ell and sigma remain invariant. Enlarging the exactly solved ball by dilation cannot improve a fixed-weight ratio.

## 5. The transport correction in weighted identities

For each of the normalized pairs above the canonical strain identity

    c=(1/pi) int xy*r^(-4)*rho_x dX

is absolutely convergent: rho_x=O(r^2) near0, and rho_x=O(r^(p-1)) at infinity. It is obtained by differentiating the inverse fundamental solution -(2pi)^(-1)log r. In terms of q=rho/(ay), angular integration first gives

    c/a=-1/4-(4/pi) int_0^infinity
           [int_0^(pi/2) sin(theta)^2*(4sin(theta)^2-3)*q dtheta] dr/r.

The radial integration by parts has boundary value-1/4 since q tends to1 at zero and to0 at infinity for these examples; the angular kernel has mean zero, so its integral is O(r^2) at0. Its exterior behavior is O(r^(p-1)). Thus this is an angular-first identity with an absolutely convergent final radial integral, not an assertion about the absolute double integral before cancellation.

Set V=U_2+D y. From R=W.grad h-h+aV, integration against h r^(-2m) gives, for2<m<4,

    ((m-1)ell-1)||h||_m^2
       +m int (X.U/r^2)h^2 r^(-2m)dX
       =-a int Vh r^(-2m)dX+int Rh r^(-2m)dX.           (13)

Indeed div W=2ell and W.grad(r^(-2m))=-2m(ell+X.U/r^2)r^(-2m). The inner and outer fluxes are O(epsilon^(8-2m)) and O(R^(4-2m)), respectively, hence vanish. This independently recovers the transport correction from integration by parts rather than dropping the residual of a nonprofile.

For the Gaussian family the last term is positive for m sufficiently close to4 and diverges as m tends to4 from below. The coefficients in Section2 satisfy tau_x=t/2+3q1<=1 and tau_y=t/6+q2<=1/4 since B/L^2<1/4. Thus Cx<=B+4 and Cy<=-B. Moreover b_*+e_*<=B+3 and b_*+5e_*>=5B. Direct angular integration gives

    int_S1 h_3 R_3=(pi/8)[-(b_*+e_*)Cx-(b_*+5e_*)Cy]
      >=(pi/8)(4B^2-7B-12)>0, B>=9.

The last polynomial is 4(B-9)^2+65(B-9)+249. Since Rh=h_3R_3+O(r^8), the integral in(13) equals int_S1 h_3R_3/(8-2m)+O(1). The exterior term is uniformly bounded as m approaches4. Hence these examples fail the transport equality without its explicit correction. The elliptic identity and inequalities alone do not detect this failure.

## Verification scope

The adjacent checker independently verifies the Gaussian quartic coefficients, full cubic transport formula, angular Gram matrix, endpoint rational137/45, positive J_m integral and the elementary norm constants. Numerical quadratures support the closed expressions but do not certify uniform error. The complete limit arguments and all dominating bounds are in this proof; they are not inferred from finitely many tests.

Independent checker PASS at2026-10-20T21:58:27.965750+00:00: exact identities, seven positive60-digit J_m quadratures (largest discrepancy1.1e-13 near an endpoint) and three heat-quartic comparisons. See verification/checks.json.
