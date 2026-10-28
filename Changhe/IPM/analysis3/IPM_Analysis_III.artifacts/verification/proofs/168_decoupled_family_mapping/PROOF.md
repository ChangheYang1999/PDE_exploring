# The strong low realization for decoupled angular weights

## Exact spaces and conclusion

Let rho be the exact normalized modal trial of topics 15 and 68, with its canonical full-plane IPM velocity U[rho]. Put

 k=1615536043799051/9007199254740992, ell=1/k,
 V=ell X+U[rho], T=V.grad-1, p(X)=x^2 y,
 beta_0=17/2, eta=37/20, 18/5<=a<=4.

Here beta_0 is a radial exponent and is unrelated to a scalar function beta below. The weight and remainder space are

 w_a(X)=|cos(theta)|^(-2a) r^(-beta_0), 0<r<1,
 w_a(X)=|cos(theta)|^(-2a) r^(-eta), r>=1,
 R_a=L2_P(w_a dX).                                      (1)

The parity P is even in x and odd in y. Values on the axes and the origin are immaterial for these weighted measure spaces. The canonical velocity includes the local term in R_1^2 and no harmonic addition. Define

 g(t)=exp(-t/2) for t<0, exp(123t/20) for t>=0,
 G=L2(g(t)dt), sigma_0=1/4, kappa_0=k+3/40.

Let d(t)=V_2(0,exp(t))/exp(t), b_0=D-d-2d', D=4ell-1, and

 H(t)=exp(-integral_-infinity^t b_0(s)/d(s) ds).

Use the actual positive d and its endpoint bounds certified in the preceding axis verification. Define B by beta=Hz, where z is locally absolutely continuous, z' belongs to L2(omega), z(+infinity)=0, and

 omega(t)=exp(-t/2) for t<0, exp(2 kappa_0 t) for t>=0.

Its Hilbert norm is the sum of the four squared terms in proof 38:

 |J|^2+||z'||omega^2+||z-J||omega,t<0^2+||z||omega,t>0^2,
 J=z(-infinity).

Set E beta=p beta(log r),

 D_a={u in R_a:T u in R_a in distributions},
 Z_a=E B direct-sum D_a, X_a=E B direct-sum R_a,
 Y_a=E G direct-sum R_a.                                (2)

The norm on D_a is its graph norm; all direct sums have the indicated Hilbert product norms. The decomposition is unique since the angular integral of |p|^2 w_a diverges for every nonzero radial coefficient. Its angular power is 4-2a<-1. In particular the scalar coordinate is not a pointwise trace imposed on arbitrary weighted L2 functions.

Let chi_0 be the fixed radial cutoff, equal to 1 near the origin and zero outside a compact set. Define the jointly normalized coupling

 C h=[U[h]+chi_0(c[h]/3)X].grad rho,
 c[h]=(1/pi) integral sin(3theta) r^(-3)h(X) dX.          (3)

For jet inputs the latter integral equals (1/4) integral exp(2t) beta(t)dt. Then the following hold for every a in the interval above.

1. c is a bounded functional on X_a; A beta=d beta'+b_0 beta is an isomorphism B->G and J is continuous on B.
2. C extends boundedly X_a->Y_a. Its scalar coordinate Gamma_C:X_a->G is Hilbert-Schmidt. C E:B->Y_a is Hilbert-Schmidt.
3. C_R=P_R C|R_a is bounded on R_a. For every epsilon>0 a compact self-adjoint K_epsilon on R_a satisfies

 Re<C_R u,u> <= integral (b_plus+epsilon)|u|^2w_a
                                      +<K_epsilon u,u>,
 b_plus=(|grad rho|-rho_y)/2.                            (4)

4. T_R:D_a->R_a is an isomorphism. Both L_ren=T+C and L_red=T+C+c[.]zeta are Fredholm of index zero Z_a->Y_a, where zeta is the actual moving-tail border vector of topics 83 and 167. More generally the latter assertion holds for every fixed zeta in Y_a.
5. The actual high domain and target of topics 150 and 165 embed continuously into Z_a and Y_a. Their operators agree distributionally with these low realizations. Injectivity on Z_a is a sufficient condition for the high inverse as well as the low inverse. Actual injectivity is not proved here.

The proof is qualitative in the mapping and compactness constants. The numerical input for item 4 is the separately certified margin of V171. No finite section, finite-rank approximation, complement norm or numerical inverse norm is inferred from this theorem.

## The scalar space, weight comparisons and canonical velocity

The scalar result of proof 38 applies with sigma_0 and kappa_0 as above. Both are positive, and sigma_0<2 is below the actual inner coefficient rate. H tends to 1 at the inner end and is comparable to exp((k-3)t) at the outer end. Thus H^2 g is comparable to omega at both ends. Since d and its reciprocal are bounded, G is precisely the target in proof 38 with equivalent norms. The formula

 A^(-1)gamma(t)=-H(t) integral_t^infinity gamma(s)/(d(s)H(s))ds

and the reciprocal-weight Cauchy-Schwarz estimate prove item 1 for A and J. Equivalently,

 B={J chi_0+w:J real, w in H1(G)},
 ||beta||B equivalent to |J|+||w||G+||w'||G.              (5)

The equivalence follows by the product rule and the endpoint bounds on H and H'/H; the free term H-1 and its derivative are O(exp(2t)). Conversely the weighted function and derivative conditions give both endpoint limits and force the prescribed ones. This proves (5) as an equality of domains, not only as a formal norm comparison.

The scalar pointwise estimates are

 |beta(t)|<=C||beta||B for t<=0,
 |beta(t)|<=C exp(-q_B t)||beta||B for t>=0,
 q_B=(8-eta)/2=123/40>2.                               (6)

They follow from the two one-sided Cauchy-Schwarz formulas for z and z'. The parameter a does not enter this scalar space.

Write w_a=|x|^(-2a)W_a(r), with W_a=r^(2a-beta_0) inside the unit circle and W_a=r^(2a-eta) outside. W_a is comparable to W_a(R) whenever r/R stays in a fixed compact interval in (0,infinity), uniformly in R. This remains true for annuli meeting r=1. Also

 w_a^(-1)<=|cos(theta)|^(2a)r^eta<=r^eta everywhere,
 w_a^(-1)=|cos(theta)|^(2a)r^beta_0 for r<1.             (7)

Every h in R_a is locally L2, and its velocity's far kernel pairing is absolutely convergent, because integral_1^infinity r^(eta-3)dr is finite. This defines the canonical velocity as a local distribution by the local L2 singular integral and the convergent far integral. Smooth compactly supported parity functions away from the vertical axis and origin are dense in R_a. On them this definition agrees with the standard multiplier U=(-R_1R_2,R_1^2), including the local point mass in the second component. Thus all subsequent extensions have a fixed meaning.

The exact squared remainder norm of the strain functional is

 ||c||_(R_a*)^2=I_c(a)/pi^2 [1/(beta_0-4)+1/(4-eta)],
 I_c(a)=integral_0^(2pi)|cos(theta)|^(2a)sin(3theta)^2dtheta. (8)

The radial integrals converge since beta_0>4 and eta<4. The kernel divided by w_a has the prescribed parity, so equality in the dual norm follows from its Riesz representer. For jet inputs, (6) makes integral exp(2t)|beta(t)|dt finite with a uniform bound by ||beta||B. This proves the complete strain assertion in item 1.

## Axis compactness without a third-derivative assumption

Let K(s,v)=(s^2-v^2)/(2pi(s^2+v^2)^2), the off-diagonal kernel of U_2. For smooth core inputs put T_h(y)=U_2[h](0,y). For fixed y>0, its derivatives j=0,1,2 extend by kernel pairing whenever a>j+1. This holds throughout the stated interval. On a compact y interval away from zero these pairings are bounded into C2. The local singularity test is integral R^(2a-3-2j)dR. At infinity (7) suffices, and there is no singularity at the input origin for fixed y>0.

A uniform third derivative on such an interval is not asserted. Its kernel test would require a>4. To obtain the origin estimate that is actually needed, use parity before estimating. Oddness in v replaces K(s,y-v) by

 K_odd(s,v;y)=[K(s,y-v)-K(s,y+v)]/2.

Its linear term at y=0 is y k_c(s,v), where k_c is the strain kernel in (3). For |Z|>2y, Taylor's integral formula for this odd function of y gives

 |K_odd/y-k_c|+|partial_y K_odd-k_c|
                         <=C y^2 |Z|^(-5).             (9)

Both sides concern ordinary smooth kernels on this separated region. The third derivative here is bounded by separation; no bounded third axis trace of h is used. Squaring (9) and using (7) gives, for 0<y<1/4,

 y^4 [integral_(2y)^1 s^(beta_0-9)ds
                   +integral_1^infinity s^(eta-9)ds]
                         <=C y^4,                     (10)

because beta_0>8 and eta<8.

On |Z|<=2y, scale Z=yY. The dual squared norms of T_h(y)/y, T_h'(y) and the restricted strain pairing are at most C y^(beta_0-4). The scaled kernel singularities at (0,1) and (0,-1) are integrable for the first two terms since a>2. The restricted strain term is integrable at Y=0 since beta_0>4. Thus their dual norms are O(y^(beta_0/2-2))=O(y^(9/4)), which is bounded by C y^2 for y<=1. Combining the two input regions proves

 ||T_h(y)/y-c[h]||_(R_a*)
       +||T_h'(y)-c[h]||_(R_a*) <=C y^2, 0<y<=1.       (11)

The extension from y<1/4 to y<=1 uses the bounded trace pairings on a compact annulus. In particular V_h=T_h/y satisfies ||V_h-c||+||partial_t V_h||<=C y^2. This is the precise replacement for the old C3 trace argument.

For y>=1, a global scaling argument using w_a^(-1)<=|cos(theta)|^(2a)r^eta gives

 ||T_h^(j)(y)||_(R_a*)<=C y^(eta/2-1-j), j=0,1.         (12)

The dimensionless integrals converge near the axis point because a>j+1, near input zero because eta>-2, and at infinity because eta<2+2j. All these inequalities are strict here.

Write the background axis cofactor as A_0(t)=rho_2(exp(t))/exp(t). It satisfies A_0=1+O(exp(2t)), A_0'=O(exp(2t)) at the inner end, and A_0,A_0'=O(exp((k-3)t)) at the outer end. The exact normalized axis coupling is

 Gamma_C[h]=(A_0+A_0')T_h/y-2A_0 T_h'
                       +c[h]chi_0(A_0+A_0'/3).         (13)

Where chi_0=1, its constant strain cancels. In terms of V_h it becomes

 (A_0'-A_0)(V_h-c)-2A_0 partial_t V_h+(4/3)c A_0'.

Equations (11)-(12) therefore give the evaluation-functional bounds

 ||Gamma_C[.](t)||_(R_a*)<=C exp(2t), t<=0,
 ||Gamma_C[.](t)||_(R_a*)<=C exp((k-163/40)t), t>=0.      (14)

After squaring and multiplying by g, the endpoint powers are exp(7t/2) and exp(2(k-1)t). Both are integrable. Parseval for the Riesz representer at each t and Tonelli show that Gamma_C:R_a->G is Hilbert-Schmidt. Measurability follows from the kernel formulas and approximation by the smooth core. No compactness of a trace operator at an excluded endpoint is assumed.

## Jet inputs and their complete image

The exact moment calculation in topics 46 and 47 is independent of the weights. For beta in B put

 P=integral_r^infinity s beta(log s)ds,
 Q=r^(-4)integral_0^r s^5 beta(log s)ds,
 S=r^(-6)integral_0^r s^7 beta(log s)ds,
 B_0=r^2 beta(log r), z=cos(theta)^2.

Then U_1[E beta]/x and U_2[E beta]/y are the fixed polynomials

 P_1=-P/4-3Q/4+5S/2+(Q-10S+B_0)z+(8S-B_0)z^2,
 P_2= P/4- Q/4+ S/2+(Q- 6S)z    +(8S-B_0)z^2.          (15)

The defining moments converge by (6). Their derivation by the two radial Poisson equations has vanishing end terms because q_B>2 and q_B<6,8. Formula (15) contains no derivative of beta. It yields, in the norm of B* and with two angular derivatives,

 P_1+c, P_2-c=O(r^2) as r->0,
 P_1,P_2=O(r^(2-q_B))=O(r^(-43/40)) as r->infinity.      (16)

Let rho=p b(t,theta). The exact cofactor of C(E beta) is

 F=P_1[2b+z b_t-cos(theta)sin(theta)b_theta]
  +P_2[b+(1-z)b_t+cos(theta)sin(theta)b_theta]
  +(c chi_0/3)(3b+b_t).                                 (17)

The angular and radial coefficient bounds in topics 47 and 48 hold for the actual finite-modal background. Its inner b-1 and derivatives are O(r^2); its outer b and derivatives are O(r^(k-3)). The constant-strain contribution to (17) near zero is exactly

 c[(4/3-2z)b_t+2cos(theta)sin(theta)b_theta].

Hence it is O(r^2). All remaining terms have the same inner bound by (16). At infinity (16) gives O(r^(k-163/40)). The two angular derivatives needed for subtraction obey these same bounds.

The axis value F(t,pi/2) is (13). Evenness about the vertical axis and Taylor's integral formula give

 ||F(t,theta)-F(t,pi/2)||_(B*)<=C cos(theta)^2 D(t),
 D(t)=O(exp(2t)) at -infinity,
 D(t)=O(exp((k-163/40)t)) at +infinity.                   (18)

The angular integral is now

 I_a=integral |cos(theta)|^(8-2a)sin(theta)^2dtheta
    =2 Beta((9-2a)/2,3/2)<infinity.                      (19)

The radial powers for both the lifted remainder and the axis target are exactly those of g. Equations (18)-(19), Tonelli and Parseval prove that C E:B->Y_a is Hilbert-Schmidt, including both its scalar and remainder coordinates. This proves item 2 for jet inputs.

## Remainder mapping on the decoupled weight

For remainder input define gamma_U by (13) with its last term omitted, and

 D h=U[h].grad rho-p gamma_U[h](log r).                  (20)

Use dyadic output annuli r in [R,2R] and input annuli [R/8,8R]. The proof of proof 48 applies with the following explicit replacements, which account for all weight uses. Put d_0(R)=R^3 for R<=1 and R^k for R>=1. The actual background has uniformly bounded C5 annular norms after division by d_0(R), including the allowed one-sided derivatives at the fixed spline knots.

On comparable annuli W_a(r) is comparable to W_a(R). Away from the vertical wedge the unweighted L2 velocity bound and |grad rho|<=C d_0(R)/R give the operator bound C d_0(R)/R. In the vertical wedge apply the exact strip estimate of proof 23 with radius 8R. Its range 5/2<a<9/2 contains the whole present interval. The coefficients of rho_x=2x rho_2+x^3 r_1 and rho_y=x^2 rho_2'+x^4 r_2 scale respectively as d_0(R)R^(-2), d_0(R)R^(-3), d_0(R)R^(-4), d_0(R)R^(-5). The common factor W_a(R) cancels between input and output. This gives the same C d_0(R)/R bound for the vertically subtracted image.

To change the lift from log|y| to log r, the j=0,1,2 kernel pairings on the scaled input annulus obey

 |T_h^(j)(y)|<=C R^(a-1-j)W_a(R)^(-1/2)||h||R_a.

Here a>3 ensures the j=2 bound. Thus gamma_U and its t derivative are bounded by C d_0(R)R^(a-5)W_a(R)^(-1/2)||h||. The inequality |log r-log|y||<=C cos(theta)^2 in the wedge and (19) give the same operator bound for the lift difference. Consequently

 ||1_[R,2R] D_near h||R_a
     <=C d_0(R)/R ||1_[R/8,8R]h||R_a.                  (21)

Finite overlap proves boundedness and vanishing output tails for this part.

For separated scales, the parity-reflected kernel and angular subtraction of proof 48 give, with Q(theta)=|cos(theta)|^4|sin(theta)|,

 |D(X,Z)|<=C Q(theta)d_0(r)r^(-3), |Z|<=r/4,            (22)
 |D(X,Z)|<=C Q(theta)r^5(|Z|^(-3)+|Z|^(-5)),
                                      r<=1, |Z|>=4r,  (23)
 |D(X,Z)|<=C Q(theta)r^k|Z|^(-3), r>=1, |Z|>=4r.        (24)

These kernel identities and estimates do not use any weight exponent. They follow by dividing the odd velocity components by x and y, subtracting the axis value of the cofactor, and using the constant-strain cancellation in the inner background. In (23), the linear source-free velocity c_Z(-x,y) cancels when b=1; its b-1 contribution and the cubic velocity remainder supply r^5. Separation justifies every kernel derivative.

The inverse-weight input volume in (22) is bounded by C r^(beta_0+2) for r<=1 and C r^(eta+2) for r>=1. Multiplication by the output weight and area gives the Hilbert-Schmidt radial integrals

 integral_0^1 r^3dr+integral_1^infinity r^(2k-3)dr.       (25)

For (23) the squared source integral is bounded uniformly: its worst inner power is s^(beta_0-9), integrable because beta_0>8; its worst outer power is s^(eta-5), integrable because eta<4. The squared output integral is bounded by integral_0^1 r^(11-beta_0)dr, finite because beta_0<12. For (24), the squared source integral is O(r^(eta-4)), leaving the outer integral in (25). The angular integral is (19) in every case. Hence the entire separated part is Hilbert-Schmidt on R_a.

Finally C_R-D is c[.] times a fixed compactly supported function whose cofactor after axis subtraction is O(r^2 cos(theta)^2) at the origin. Its R_a norm is finite by beta_0<12 and (19). Equation (8) makes it bounded rank one. This proves the full remainder mapping and completes item 2. All extensions agree with the canonical distributional formula by density, the local L2 velocity convergence and the convergent far pairings.

## Compact localization and the Garding inequality

The proof of (4) can be given directly, so that no conclusion for the old weight is being transferred by an inclusion in the wrong direction. Equation (21) and the separated compact part imply vanishing radial output tails. On a fixed compact annulus, split the input into |x|<epsilon_0 and its complement. For the first part, proof 23 gives an O(epsilon_0) norm for the vertically subtracted image. The lift difference is O(x^4)||h|| pointwise, by the j=2 trace bound just used, so its output norm in |x|<delta is O(delta^(9/2-a)). For the second input part, the source is separated from sufficiently small |x| and the same angular Taylor subtraction gives O(x^4), with a constant allowed to depend on epsilon_0. Choose epsilon_0 first and then delta. Since 9/2-a>=1/2, this proves

 lim_(delta->0)||1_{r_0<r<r_1,|x|<delta}C_R||=0.         (26)

Thus C_R can be localized in output to a smooth compact cutoff chi away from the vertical axis and origin with arbitrarily small norm error. There the lifted axis row is compact by (14), and the normalization is rank one. Localizing also the input changes the remaining velocity coupling by a Hilbert-Schmidt kernel: at input infinity use eta<2, and at the origin use the integrable inverse weight. On these compact sets the weight has a positive locally Lipschitz square root, including at r=1. Conjugation by this square root changes the localized velocity multiplier only by a compact commutator.

For completeness, a commutator with a Lipschitz coefficient constant outside a compact set is compact on unweighted L2: within distance delta its kernel is bounded by C|X-Y|^(-1), whose Schur norm is O(delta); outside that distance it is square integrable. The local point mass commutes. This argument also applies to the first-order Riesz transforms used next.

Modulo compact forms, the localized coupling has the real quadratic form of the matrix

 [[-chi rho_y, chi rho_x/2],[chi rho_x/2,0]]

on (R_1 f,R_2 f). Its largest eigenvalue is chi b_plus. Commuting this Lipschitz coefficient back through the Riesz transforms and using R_1*R_1+R_2*R_2=I gives the bound by integral chi b_plus |f|^2 plus a compact form. The omitted output has arbitrarily small norm, chi<=1 and b_plus>=0. Taking the self-adjoint part of the compact term proves (4).

## Transport, Fredholm index, and the actual border

The physical field is globally C1 and Lipschitz, its divided components V_1/x and V_2/y are bounded, and it is tangent to both axes. The exact energy multiplier for (1) is

 kappa_a=1+ell+(mu'/2)q+a tan(theta)vtheta,
 mu'=-beta_0 inside r=1, mu'=-eta outside,
 q=V.e_r/r, vtheta=V.e_theta/r.                          (27)

The weight is continuous across r=1, so there is no interface measure. V171 certifies kappa_a-b_plus>=1.13 for a=4 and >=1.10534 for a=18/5. Since (27) is affine in a, every intermediate a has the corresponding convex-combination lower bound. In particular

 kappa_a-b_plus>=m_*=1.10534 for all 18/5<=a<=4.         (28)

The complete flow defines S_s h=exp(-s)h(Phi_s). Change of variables yields ||S_s||<=exp(-m_* s) for s>=0. The group is strongly continuous by density and the bounded energy multiplier. Its generator is precisely the maximal distributional T_R: the weak equation paired with transported test functions gives the integrated group identity. Therefore T_R is closed and

 T_R^(-1)f=-integral_0^infinity S_s f ds,
 ||T_R^(-1)||_(R_a->R_a)<=1/m_*.                        (29)

Angular cutoffs have uniformly bounded transport derivatives because vtheta=O(cos(theta)); radial cutoffs smooth in log r do also because q is bounded. They give graph approximation away from the axis and both ends. Ordinary Friedrichs approximation on the remaining compact sets gives a smooth parity core. Hence the exact energy identity extends from that core to D_a.

The lift identity is

 T(E beta)=E(A beta)+p cos(theta)^2[a_1 beta'+a_0 beta].  (30)

The actual coefficients satisfy |a_1|<=C and |a_0|<=C min(r^2,1), as established by the normalized modal origin cancellation. Equations (5), (19), and g=exp((8-beta_0)t) or exp((8-eta)t) show that the error in (30) is bounded B->R_a. The pure full transport is therefore an invertible lower triangular block.

For T_R+s C_R, 0<=s<=1, use (4) with epsilon=m_*/2 and (28) to obtain a compact-error estimate with constant m_*/2. The same estimate controls the fixed graph norm because C_R is bounded on R_a. Each member is upper semi-Fredholm. The norm-continuous path begins at the isomorphism T_R. The Schur-complement argument of proof 44 shows that, within the upper semi-Fredholm set, finite codimension of the range and the index are locally constant. Thus every member is Fredholm of index zero. The full operator is the corresponding lower triangular block plus its Hilbert-Schmidt scalar row. This proves the first Fredholm assertion in item 4. Adding any bounded rank-one vector in Y_a preserves the index.

For the actual border, the verified expansions give cofactor O(r^2) at the origin and physical size O(r^(2k-1)(1+|log r|)) at infinity. Subtracting its axis cofactor gives the additional cos(theta)^2 factor. The inner squared radial power is 12-beta_0=7/2 and the outer squared radial power is 4k-eta<0. The angular integral is (19). The scalar G coordinate has the same radial exponents. Thus the actual zeta belongs to Y_a. This is membership, not a numerical target norm.

## Relation to the high realization and limits of this result

Let w_old=|cos(theta)|^(-17/2) times r^(-17/2) inside and r^(-5/4) outside. Since a<=4<17/4 and eta>5/4,

 w_a<=w_old everywhere.                                (31)

Thus the old low remainder space embeds into R_a, not conversely. The actual high remainder space X_s embeds into the old space by its separately proved cofactor Hardy estimate, hence into R_a. The high scalar space B_H=J chi_0+a_H H^(29/4), with a_H=exp(9t/5) at the inner end and exp(-7t/2) at the outer end, embeds into B by (5): its inner squared weighted exponent is 18/5-1/2>0 and its outer exponent is -7+123/20<0. The same calculation embeds the high scalar target into G. The high transport graph maps into D_a because its image belongs to the high target remainder and hence to R_a; the distributional definitions coincide. This proves item 5.

The high Fredholm theorem remains the previously proved one, with its own fixed spaces and order. If the low full operator on Z_a is injective, any high kernel vector is a low kernel vector and vanishes. Index zero then gives both inverses; low uniqueness makes their values agree on high forcing. This implication does not establish the hypothesis. The finite-dimensional S_1 calculations do not check the complement and do not prove that hypothesis.

The new low spaces also retain a closed free cubic coefficient J. This does not by itself make the independent low remainder classically differentiable at the origin. A pointwise cubic normalization still uses the high solution and the argument already given for it. Numerical radii, perturbation constants, residual norms in these new spaces, and a computable compact approximation are separate tasks.

## Dependencies and verification scope

Dependencies are the actual source and axis certifications; the exact strip theorem (proof 23); scalar Hardy theory (38); canonical modal moments and coefficient bounds (46-48); the localized compact-commutator argument (49); actual high embeddings and Fredholm theorem (115, 123, 150); the border expansions (83, 167); and the independent global margin V171. Every use of a weight-sensitive endpoint has been recomputed above. In particular, the old a>4 uniform third-axis-derivative step has been replaced by (9)-(11). The accompanying exact rational audit records all endpoint exponents and the normalization and norm-comparison identities. It is an algebraic check of this proof, not a substitute for it.

The exact beta-integral formula (8), evaluated independently at 384 and 768 bits, also gives the useful certified bounds

 ||c||_(R_(18/5)*)<0.239392, ||c||_(R_4*)<0.230190.

At a=4, I_a=pi and I_c=31pi/128, so the latter norm is exactly sqrt(4123/(24768pi)). The norm decreases as a increases because its angular integrand in (8) decreases pointwise. Consequently ||c||_(R_a*)<0.239392 uniformly for the stated interval. These are norms on the remainder input only; the full X_a strain norm also includes its separate B coordinate.

Verdict: CONFIRMED. The Fredholm and mapping assertions hold for the actual normalized trial on the stated decoupled family. The inverse assertion remains conditional on actual injectivity.
