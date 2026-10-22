# Annular control of the constant while preserving the entire core

Written 2026-10-21T00:22:18.006742+00:00. Complete informal proof before independent numerical checks. This is an inverse-source and topology result. It neither constructs nor excludes a B2 profile.

## 1. Statement, hypotheses and notation

Fix2<beta<3, s=1/beta and m=1-2s. Use the prompt convention K(Z)=(Z2,-Z1)/(2pi|Z|²), V=K_rel Omega and -Delta Psi=Omega, V=(-Psi_y,Psi_x). Suppose Omega is smooth, x-odd, and has the first two smooth homogeneous tails omega0,omega1 of degrees-s,-2s, with eta=Omega-omega0-omega1=O(r^-3s) at infinity. In particular its ordinary remainder inverse converges absolutely at0 and infinity, and the canonical constant is C=(0,C2)=-U_eta(0), as in packet90. No scalar PDE is imposed in this paragraph.

Choose any nonzero nonnegative smooth chi on the real line supported in[1,2] (hence flat at both endpoints), and let

    I0=integral_1^2 chi(t)dt>0,    I2=integral_1^2 t² chi(t)dt.

For a prescribed real D and R>=1, define the annular first-cosine perturbation

    deltaOmega_R(r,theta)=q_R(r)cos(theta),
    q_R(r)=-2D/(R I0) chi(r/R).                         (1)

Then Omega_R=Omega+deltaOmega_R and V_R=K_rel Omega_R have these properties.

(a) Both differences vanish identically on the entire disk r<=R. Every center derivative of Omega and V, including the normalization and strain, is preserved exactly. The original first two far-field source coefficients are unchanged. The constant changes by exactly

    C2_R-C2=D.                                         (2)

(b) For every finite integer j>=0, define the weighted derivative norm

    ||F||_(a,j)=max_(|k|<=j) sup_X (1+|X|)^(a+|k|)|partial^k F(X)|.

There is a constant M_j depending on s,j,chi but not on R,D or the background source such that

    ||deltaOmega_R||_(s,j)+||V_R-V||_(s-1,j)
                          <=M_j |D| R^(s-1).           (3)

Thus for fixed nonzero D these weighted differences tend to zero, while the constant difference stays D and the fields agree on expanding disks. This remains true with the first two homogeneous tails fixed exactly. In particular C2 is not a continuous functional for these weighted norms on this source class. No estimate bounding |deltaC2| by these differences with an R-independent constant can hold.

(c) Suppose additionally, for all sufficiently large r and every theta in the open right half-plane,

    Omega(r,theta)>=a r^-s cos(theta),   a>0.            (4)

For every fixed D, all sufficiently large R preserve strict positivity on x>0 wherever the background is positive. On the annulus the lower bound can be retained with a/2 in place of a. Outside the annulus the source is unchanged. This conclusion assumes(4); mere pointwise positivity without a uniform lower tail bound is not used as a substitute.

(d) Let Theta be any smooth x-even field with ||Theta||_(-m,j+1), ||Omega||_(s,j+1) and ||V||_(s-1,j+1) finite. Keep Theta fixed and write the scalar residuals

    R_Theta=(beta X+V).grad Theta-(beta-2)Theta,
    R_Omega=(beta X+V).grad Omega+Omega-partial_x Theta.

For a constant M depending also on these background norms and beta,j, the changes obey

    ||R_Theta,R - R_Theta||_(-m,j)<=M |D|/R,
    ||R_Omega,R - R_Omega||_(s,j)
          <=M[|D|R^(s-1)+|D|/R+D²R^(s-2)].            (5)

These are weighted absolute norms, not the prompt's pointwise normalized residuals. They give continuity of the residual map along this perturbation, not an existence result or an unconditional lower-bound impossibility theorem for the full PDE. If a true profile existed in the stated class, (5) would conditionally give fields with its exact center data and arbitrarily small weighted residuals but a shifted constant.

## 2. Exact canonical inverse and the constant

For a first-cosine source q(r)cos(theta) supported away from0, the centered modal stream is p(r)cos(theta), with

    p(r)=1/2[r^-1 integral_0^r rho² q(rho)drho
                              -r integral_0^r q(rho)drho].     (6)

Differentiation gives -(p''+p'/r-p/r²)=q, and p has zero linear term at0. Therefore its velocity is divergence-free, has negative curl equal to the source, and vanishes at0. It is bounded at infinity. The canonical relative integral has the same properties, and their difference is an entire harmonic vector field of sublinear growth, hence constant; centering makes that constant zero. Alternatively(6) follows by subtracting the ordinary first-mode inverse's value at0. This proves that (6) is the specified full-plane inverse and introduces no free harmonic strain.

For(1), all integrals in(6) vanish when r<=R. For r>=2R they equal

    integral q=-2D,      integral rho² q=-2D R² I2/I0.

Consequently

    p_R(r)=D r-D R² I2/(I0 r),
    deltaV_R=D e2+E_R r^-2(sin(2theta),-cos(2theta)),
    E_R=-D R² I2/I0.                                  (7)

The sign in(2) also follows directly from the ordinary inverse:

    U_deltaOmega(0)=(0,(1/2) integral q_R dr)=(0,-D).

Since deltaOmega is compactly supported, neither omega0 nor omega1 changes and delta eta=deltaOmega. Thus deltaC=-U_deltaOmega(0)=(0,D), proving(a). The sources and velocities coincide on the core, so every local relation, including either PDE if it held there, is exactly retained when Theta is kept fixed.

## 3. Weighted convergence and positivity

Set Z=X/R. Equation(1) has the form deltaOmega_R(X)=(D/R)F(Z), with F smooth and supported in1<=|Z|<=2. Equation(6) has the form deltaV_R(X)=D G(Z), where G is smooth, zero on |Z|<=1, and by(7) is e2 plus a decaying degree-2 field for |Z|>=2. For every k, the relevant scaled derivatives of F are bounded. For G the derivatives of positive order decay as |Z|^-2-|k|; G itself is bounded. Multiplying partial_X^k deltaOmega by (1+|X|)^(s+|k|), or partial_X^k deltaV by (1+|X|)^(s-1+|k|), gives a bound by a constant times |D|R^(s-1). The region |X|<=R contributes zero. For the exterior region the exponents are bounded above by s-1<0 for k=0 and by s-3<0 for k>=1. Since R>=1 and every nonzero term has r>=R, the weights(1+r) and r are comparable with constants depending only on the finite exponents. Flatness of chi at1 and2 makes F and G smooth across both circles. This proves(3), for all finite j with the same rate.

On the perturbation annulus, the magnitude of the new cosine coefficient is at most2|D| ||chi||_infinity/(R I0). Since r<=2R, (4) gives a lower first-cosine envelope a(2R)^-s. Let r0 be a radius beyond which(4) holds. Choose R>=max(1,r0) so that

    R^(1-s)>=4*2^s |D| ||chi||_infinity/(a I0).

Then |q_R|<=a r^-s/2 throughout the annulus. Multiplication by cos(theta)>0 proves(c), including uniformly near the vertical axis. If D<0 the perturbation is positive there, but the displayed condition covers either sign.

## 4. Residual continuity, without a PDE conclusion

Write deltaV=V_R-V and deltaOmega=Omega_R-Omega. Direct subtraction, with Theta unchanged, gives

    delta R_Theta=deltaV.grad Theta,
    delta R_Omega=(beta X+V).grad deltaOmega+deltaOmega
                    +deltaV.grad Omega+deltaV.grad deltaOmega. (8)

Every term vanishes for r<R. On r>=R, derivatives of deltaV are bounded by constants times |D|r^-k; the background temperature derivatives satisfy |partial^k grad Theta|<=constant r^(m-1-k). Applying Leibniz's rule and the weight r^(-m+j) therefore bounds the first line by M|D|/R.

The term beta X.grad deltaOmega+deltaOmega is supported on the annulus and, after the Omega weight, is O(|D|R^(s-1)). The term V.grad deltaOmega has weighted size O(|D|/R), because V=O(r^(1-s)) and deltaOmega has derivatives of size |D|R^-1-k. The term deltaV.grad Omega also has weighted size O(|D|/R), throughout r>=R. The final term is supported on the annulus and has weighted size O(D²R^(s-2)). Each differentiated term has the same weighted size by Leibniz's rule and the stated symbol bounds. Summing gives(5).

The coefficient C2 can therefore change by a fixed amount while these field norms converge and the residual changes vanish. This does not assert that the background residuals vanish, or that an exact profile exists. It explains why extracting a finite asymptotic coefficient requires additional uniform remainder information. Indeed the stronger third-remainder norm of deltaOmega has size proportional to |D|R^(3s-1), which diverges here since3s>1. The exterior coefficient E_R=-D R² I2/I0 is also unbounded for fixed nonzero D as R grows. The perturbations are also not claimed to remain in a particular finite spline representation, and they do not preserve the global transport equations.

## 5. Dependencies and verification scope

The exact first-mode inverse(6) is proved here and is consistent with packets03 and63. Only the interpretation of C as the constant after two leading tails uses packet90; all source and norm statements are otherwise elementary. Positivity requires the explicit extra hypothesis(4). The proof precedes independent tests, and no numerical result is needed for it. Formal proof-assistant sources are absent, as documented in formal/README.md. No full B2 endpoint follows.
