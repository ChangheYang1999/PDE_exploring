# Smooth compact fields satisfying every axis Taylor equation

## Exact statement and scope

Fix beta>=2, A!=0 and a prescribed real c0, which may be nonzero. There exist real C-infinity functions Psi,Theta,Omega with compact support in R^2 such that, with

    U=(-Psi_y,Psi_x), Omega=-Delta Psi,
    W=beta(x,y)+U-U(0),
    R_Theta=W.grad Theta-(beta-2)Theta,
    R_Omega=W.grad Omega+Omega-Theta_x,

all of the following hold.

1. Psi and Omega are odd in x; Theta is even in x and Theta(0,y)=0. No y parity is imposed. The canonical full-plane logarithmic inverse of Omega is exactly Psi, with no harmonic correction, and U(0)=(0,c0). In particular U has compact support and is sublinear.
2. Near the origin, Theta=A x^2/2, Omega=2A x/beta and

       W1=(beta-2)x/2, W2=d y-A x^2/beta,
       d=(3beta+2)/2.

   Thus both full transport equations hold on an open neighborhood of the origin. The center identities are a0=A/2, Psi_xy(0)=1+beta/2 and Omega_x(0)=4a0/beta. Here a0 is the prompt's center normalization; it equals a1(0) in the series indexed from n=1 below. There is no constant thermal series coefficient.
3. For every pair of nonnegative integers p,q and every real y,

       partial_x^p partial_y^q R_Theta(0,y)=0,
       partial_x^p partial_y^q R_Omega(0,y)=0.

   The central component of {y:Theta_xx(0,y)!=0} is exactly J=(-3,3). Its second thermal jet and every vorticity and thermal coefficient constructed below are flat at the two endpoints.
4. R_Theta is not identically zero. Indeed,

       integral_R2 Theta R_Theta = 2(1-beta) integral_R2 Theta^2 < 0.

These fields are therefore not B2 profiles. The theorem is a counterexample to the sufficiency of every axis Taylor transport equation, even when the exact whole-plane inverse, center drift, smoothness, parity and sublinear velocity are all imposed. It does not refute any result using the PDE away from the axis. No convergence of an analytic Taylor series is asserted. The construction is smooth and uses cutoffs with successively smaller horizontal supports. No positivity of Omega is asserted. The general B2 endpoint remains OPEN.

## 1. Axis transport with a bounded central component

Let theta(t)=exp(-1/t) for t>0 and0 otherwise. For a<c put

    chi_{a,c}(y)=theta(y-a)/(theta(y-a)+theta(c-y)).

This smooth cutoff is0 for y<=a and1 for y>=c, with values strictly between0 and1 on(a,c). For y>=0 put

    q(y)=(1-chi_{1,2}(y))d y+chi_{1,2}(y)(y-3)^2,
    b_*(y)=(1-chi_{4,5}(y))q(y)+chi_{4,5}(y)beta y,

and extend b_* oddly. Since b_*=d y near0, the extension is smooth. It is positive on(0,3) and(3,infinity), with its only positive zero at3. On a neighborhood of3 it is exactly(y-3)^2; near-3 it is exactly-(y+3)^2. Define the smooth even cutoff chi_out(y)=chi_{4,5}(|y|), which vanishes on a neighborhood of0, and set

    b(y)=b_*(y)-c0 chi_out(y).

Then b=b_* on[-4,4], b=beta y-c0 for |y|>=5 and b(0)=0. Additional zeros outside[-4,4] are harmless; no ODE will be divided by b there. This modification realizes a prescribed canonical center velocity later, while leaving J unchanged. We do not impose oddness on b globally.

Set rho=1 on[-1,1]. On(1,3) and(-3,-1) solve

    rho'/rho=(d-b')/b.

There b is nonzero and the coefficient is smooth. It joins to the zero coefficient to infinite order at y=1 and-1, so the positive solutions join smoothly to rho=1. Within J, b is odd and rho is even. Define

    a1=A/(2rho^2) on J, and a1=0 outside J.

For 2<=|y|<3, put s=3-|y| and tau=1/s. Direct integration gives a positive constant C such that

    rho=C tau^2 exp(d tau),
    a1=(A/(2C^2))tau^-4 exp(-(3beta+2)tau).       (1)

The same C works at both ends by evenness. All y derivatives of a1 tend to0 at either end: each is a polynomial in tau times the exponential in(1). Thus a1 is globally smooth, is nonzero exactly on J and equals A/2 on[-1,1]. Its exact equation is

    b a1'+(3beta+2-2b')a1=0.                    (2)

It holds outside J as well, including the endpoints by continuity.

## 2. All transverse coefficients and their equations

The following expressions are formal Taylor series for now; they are not presumed convergent:

    Theta=sum_{n>=1} a_n(y)x^(2n),
    W2=b(y)+sum_{j>=1} v_j(y)x^(2j),
    W1=(2beta-b'(y))x-sum_{j>=1} v_j'(y)x^(2j+1)/(2j+1),
    Omega=sum_{n>=0} q_n(y)x^(2n+1).

For purposes of second derivatives only write v_0=b, so v_0''=b''. The actual coefficient of x in Psi will be V0=b-beta y+c0, not b. Since V0''=b'', this convention gives exactly the same curl relation for n=0; no value or first derivative of v_0 is used in that relation. The negative-curl identity is equivalent, coefficient by coefficient, to

    q_n=-v_n''/(2n+1)-(2n+2)v_{n+1}, n>=0.      (3)

Multiplying the formal polynomials and comparing each finite coefficient gives the thermal equations, for n>=1,

    b a_n'+[(4n-1)beta+2-2n b']a_n
      =sum_{j=1}^{n-1}[2(n-j)v_j'a_{n-j}/(2j+1)-v_j a_{n-j}'],       (T_n)

and the vorticity equations, for n>=0,

    b q_n'+[(4n+2)beta+1-(2n+1)b']q_n
      =2(n+1)a_{n+1}
       +sum_{j=1}^n[(2(n-j)+1)v_j'q_{n-j}/(2j+1)-v_j q_{n-j}'].    (V_n)

The empty sums vanish. Each coefficient uses finitely many derivatives and products, so these formulas also apply to actual smooth fields having the specified Taylor jets. They include no assumption of analyticity.

Start q_0=2A/beta on[-1,1], solve(V_0) on(1,3) and(-3,-1), and extend by0 outside J. The extension will be justified in Section3. The prescribed constant solves(V_0) near0 because 2beta+1-d=beta/2 and 2a1=A. Define globally v1=-(b''+q0)/2 by(3). On[-1,1], v1=-A/beta.

Next solve(T_2) on the two parts of J outside[-1,1], taking a2=0 on[-1,1], and extend it by0 outside J. Inductively, for n>=1, after a_{n+1}, q_0,...,q_{n-1} and v_1,...,v_n have been obtained, perform these three steps:

    solve(V_n) for q_n with q_n=0 on[-1,1], extend by0 outside J;
    define v_{n+1}=-(q_n+v_n''/(2n+1))/(2n+2) globally;
    solve(T_{n+2}) for a_{n+2} with a_{n+2}=0 on[-1,1],
        and extend by0 outside J.

Each ODE is linear on intervals with b!=0. All forcing for these higher equations vanishes identically on[-1,1]: there a1 and q0 and v1 are constant, and every higher coefficient is0. The resulting solutions join smoothly at y=1 and-1, since the coefficients and forcing already match to all orders at these ordinary ODE points. Resonances of the homogeneous coefficient at the center when beta=2 cause no difficulty: the zero solution is prescribed on a whole neighborhood of that point, and no division by the center coefficient is used.

This triangular induction solves all(T_n), all(V_n), and every curl relation(3), provided the endpoint extensions are smooth. That is proved next.

## 3. Flatness at the finite endpoints

On the interior endpoint neighborhoods 2<=|y|<3, tau=1/(3-|y|) tends to positive infinity and

    b partial_y=partial_tau, b'=-2/tau,
    partial_y=plus or minus tau^2 partial_tau.

Set lambda=3beta+2 and alpha=2beta+1. Both are positive and lambda>alpha. Let E_sigma denote the functions of tau>=1 such that, for each fixed derivative order k, there are C_k,N_k<infinity with

    |partial_tau^k f(tau)|<=C_k tau^(N_k) exp(-sigma tau).

The powers may depend on k and on the coefficient. This class is closed under differentiation in y and tau and multiplication by fixed polynomials in tau and1/tau. Products satisfy E_sigma E_eta subset E_{sigma+eta}. For eta>sigma, E_eta subset E_sigma. Every E_sigma function with sigma>0 extends by0 smoothly across s=0, because y differentiation only changes a polynomial factor.

We use the following elementary ODE fact. If c>sigma>0, nu is fixed and g is in E_sigma, every solution of

    z_tau+(c+nu/tau)z=g

on[tau0,infinity), tau0>0, belongs to E_sigma. Its integrating-factor formula is

    z=tau^-nu exp(-c tau)
      [C+integral_{tau0}^tau t^nu exp(c t)g(t)dt].                (4)

The integral is bounded by a polynomial in tau times exp((c-sigma)tau), since c-sigma>0. This proves the zeroth derivative bound. The ODE and its successive derivatives give all the higher bounds. Real powers of tau cause no issue on tau>=tau0; they and each derivative are polynomially bounded.

By(1), a1 belongs to E_lambda. Equation(V_0) is

    (q0)_tau+(alpha+2/tau)q0=2a1.

This is a separate direct use of the integrating-factor formula, not an application of the c>sigma bound with sigma=alpha. Here (4) with c=alpha and nu=2 has an integrable forcing factor t^2 exp(alpha t)2a1, since lambda>alpha. Its bracket is bounded, so q0 is in E_alpha. Differentiating the equation proves the higher bounds. Hence the promised zero extension of q0 is smooth. Near the positive endpoint b''=2, and near the negative endpoint b''=-2. Consequently

    v1=-1+E_alpha near3, v1=1+E_alpha near-3,

and every positive-order y derivative of v1 belongs to E_alpha.

We now prove inductively that

    a_n in E_lambda for all n>=1,
    q_n in E_alpha for all n>=0,
    v_j in E_alpha for all j>=2.                (5)

For(T_n) with n>=2 the left side becomes

    (a_n)_tau+[(4n-1)beta+2+4n/tau]a_n.

The constant coefficient (4n-1)beta+2 exceeds lambda. All terms on its right belong to E_lambda: v1 is bounded by a constant plus an E_alpha function, its derivatives are in E_alpha, all other v_j are in E_alpha, and the lower a coefficients and their derivatives are in E_lambda. Thus (4) proves the next a_n bound. For(V_n) with n>=1 the constant coefficient is (4n+2)beta+1>alpha, and its1/tau coefficient is4n+2. Its forcing belongs to E_alpha, by the same product argument and a_{n+1} in E_lambda subset E_alpha. Equation(4) proves the q_n bound. Finally(3) gives v_{n+1} in E_alpha: for n=1 the constant part of v1 disappears after two derivatives; for n>=2 the induction gives the claim directly. This proves(5) in exactly the construction order of Section2.

All a_n and q_n therefore extend smoothly by0 outside J. The v_j are globally smooth by their derivative recurrence. Outside J that recurrence, where all q_n=0, reduces to

    v_j=(-1)^j b^(2j)/(2j)!, j>=1.              (6)

The formula follows by induction starting from v1=-b''/2. Near each endpoint b is quadratic on both sides, so v1 matches the stated constant plus a flat function and every v_j for j>=2 matches0 to infinite order. For |y|>=5, b=beta y-c0; hence every v_j vanishes there. All a_n,q_n,v_j are thus supported in one fixed compact y interval. The identities(T_n),(V_n) hold outside J because all thermal and vorticity coefficients vanish there; they hold at the endpoints by continuity. Possible further zeros of b outside J have not been divided by.

## 4. A direct smooth realization of the complete jets

Let chi be a smooth even function of one variable, equal to1 for |x|<=1/2 and0 for |x|>=1. Such a function follows from the cutoff in Section1. Define

    V0(y)=b(y)-beta y+c0.

It is smooth and supported in[-5,5], and V0(0)=c0. Choose positive widths epsilon_j<=1 and delta_n<=1 and set

    Psi(x,y)=V0(y)x chi(x/epsilon_0)
        +sum_{j>=1} v_j(y)x^(2j+1) chi(x/epsilon_j)/(2j+1),
    Theta(x,y)=sum_{n>=1} a_n(y)x^(2n) chi(x/delta_n).             (7)

Here epsilon_0 may be1. The other widths are chosen successively small as follows. For a fixed coefficient f with compact y support, a term f(y)x^m chi(x/epsilon) and all its mixed derivatives of total order at most k<m are bounded by C_{f,m,k} epsilon^(m-k) for0<epsilon<=1. This follows by differentiating the product; each horizontal derivative removes at most one power of epsilon, and on its support |x|<=epsilon. The y derivatives of f have finite suprema.

Choose epsilon_j<=2^-j so that the j-th summand of Psi has C^k norm at most2^-j for every k<=j. This is possible since2j+1>j. Choose delta_n<=2^-n so that the n-th summand of Theta has C^k norm at most2^-n for every k<=n, possible since2n>n. For each fixed k, the tails converge uniformly with every derivative of order at most k; the omitted initial summands are finite in number. These estimates prove that(7) defines C-infinity functions, without invoking convergence of the formal Taylor series. Psi vanishes outside[-1,1] times[-5,5], and Theta vanishes outside the smaller rectangle[-1,1] times[-3,3]. Psi is odd in x and Theta is even.

For any fixed horizontal derivative order at x=0, termwise differentiation is justified by the corresponding uniform convergence. Since chi=1 near0, only the matching polynomial power can contribute, and every larger power has zero derivative. Thus the Taylor coefficients of Psi are V0 for x, and v_j/(2j+1) for x^(2j+1), and those of Theta are exactly a_n. This holds as an identity of smooth y functions and after any fixed number of y derivatives.

Define U and Omega from Psi exactly as in the statement. Then U(0)=(0,c0), div U=0 and div W=2beta. The coefficient of x in W1 is beta-V0'=2beta-b', and the axis value of W2 is beta y+V0-c0=b. Higher coefficients are precisely those of Section2. Because V0''=b'', the actual Taylor coefficients of Omega=-Delta Psi are exactly q_n by(3). The two actual residuals have all horizontal Taylor coefficients0 by(T_n) and(V_n). Their y derivatives vanish on the axis as well, since each coefficient is identically0 as a smooth y function. This proves the infinite-order assertion. Smooth division by the parity factors x^2 and x also leaves residuals flat along the axis; no claim about small normalized ratios near vanishing denominators is needed.

All coefficients beyond a1,q0,v1 vanish on[-1,1]. In a sufficiently small neighborhood of(0,0), the three relevant cutoff factors for V0,v1,a1 equal1. Formula(7) there becomes exactly

    Psi=c0 x+(d-beta)yx-Ax^3/(3beta), Theta=A x^2/2.

The fields and center identities in item2 follow by differentiation. Direct substitution proves both transport equations in this neighborhood, including at beta=2. Finally Theta_xx(0,y)=2a1(y), so its nonzero component is exactly J.

## 5. The exact full-plane inverse and a nonzero PDE defect

Let G(Z)=-(1/(2pi))log|Z|. In distributions, -Delta G is the point mass at0. For the smooth compactly supported Psi in(7), Omega=-Delta Psi is also smooth and compactly supported. The ordinary logarithmic convolution is well defined: the logarithmic singularity is locally integrable and the source is compact. Distributional integration by parts, with Psi compactly supported, gives

    G*Omega=G*(-Delta Psi)=(-Delta G)*Psi=Psi.

This identity holds pointwise since both sides are smooth. Equivalently it follows by regularizing G and passing to the locally integrable limit. There is no boundary term at infinity because the differentiated function Psi is compactly supported, and no omitted inner boundary term because the distributional Laplacian includes the point mass. Thus the prescribed canonical full-plane inverse is exactly the constructed stream function, including its constant. Its differentiated velocity is the ordinary full-plane Biot-Savart velocity. The velocity kernel singularity is locally integrable against the smooth source, so this integral is absolutely defined at every fixed point. In particular the center velocity is the prescribed c0 obtained from that source, not an appended uniform flow. Compact support implies U=o(|X|), and all polynomial tail requirements are satisfied.

Finally Theta is nonzero because its center quadratic coefficient is A/2. Since Theta has compact support and div W=2beta, ordinary integration by parts on R^2 gives

    integral Theta W.grad Theta
      =(1/2)integral W.grad(Theta^2)=-beta integral Theta^2.

Subtracting(beta-2)integral Theta^2 proves item4. Its right side is strictly negative for beta>=2 and A!=0. Therefore R_Theta cannot vanish everywhere. As all its axis jets are0, the defect necessarily occurs off the axis. This proves the theorem and its strict limitation: every axis Taylor condition, exact elliptic inversion and admissible velocity growth can hold for smooth manufactured fields that fail the defining transport PDE.

## Dependencies and verification scope

The proof uses only the displayed smooth cutoffs, scalar linear ODEs, exact finite coefficient identities, a directly proved smooth series construction, and distributional integration by parts for the fundamental solution. P273 motivates the bounded component, but its proof or external review is not needed as an unproved premise here. The base b on[-4,4] agrees with that construction. No physical Boussinesq evolution is asserted, because the global stationary PDE fails. Independent symbolic controls, source hashes and the actual model review belong in verification/. No Lean or Lake build is authorized.
