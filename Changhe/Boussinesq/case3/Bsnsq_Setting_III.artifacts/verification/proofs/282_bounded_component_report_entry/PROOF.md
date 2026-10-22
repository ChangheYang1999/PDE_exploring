# Bounded axis component: independent audit of the complete report entry

## Exact statement and audit scope

This packet verifies proposed report section4.49 v2, its five consequential replacements, Table8.1 row and one timeline entry on the frozen actual report of SHA25668a714214af41ecefd3c5d8e72348493d013d1470b9f7726232a91c6c666230b (SPEC77). The frozen text, preview, original154timeline entries and independently proved P278 construction and endpoint mapping are registered in verification/freeze.json. The lead insertion program is only read as source, never executed or imported. The precise mathematical assertion is the P278 theorem reproduced in full below: for each beta>=2, A!=0,c0 real there exist smooth compactly supported Psi,Theta,Omega with Omega=-DeltaPsi, the exact whole-plane inverse, x parity and center velocity(0,c0), exact B2 equations near0, all mixed residual derivatives zero on the entire axis, and central temperature-axis component J=(-3,3). Their thermal residual is globally nonzero. The fourth-jet ratio satisfies D/T~-(6d/beta)(3-|y|)^-2 and A D/T^2 tends to negative infinity at either end inside J, where d=(3beta+2)/2. These are non-solutions and do not settle B2. Neither sign-definite vorticity nor a nonzero vorticity tail is supplied.

## Reindexing and the scope of the reported consequences

The report's v_{2j} is P278's v_j, the coefficient of x^{2j} in W2. In particular report v2=P278v1 equals v in report4.44. The report's q_n is the coefficient of x^{2n+1} in Omega, while a_n is the coefficient of x^{2n} in Theta. Thus T=2a1, eta=q0,D=24a2, and curl gives q_n=-v_{2n}''/(2n+1)-(2n+2)v_{2n+2}, with v0''=b''. Product differentiation gives exactly the report's (T_n),(V_n); complete derivations and smooth realization follow below. There is no convergence assumption on the original formal series: shrinking cutoffs give actual C-infinity fields with these jets. Compact support of Psi legitimates the logarithmic inverse identity Gamma*(-DeltaPsi)=Psi, not merely the differential Poisson equation.

On J the coefficient rho'/rho=(d-b')/b is smooth away from0; it is identically zero on[-1,1] and has all derivatives zero at the attachment points. The prescribed inner coefficients solve the equations there. However the inhomogeneous term of(V0) is 2a1=A, not zero. Thus the literal sentence in v2 that 'all forcing vanishes identically' is false. Its intended consequence, smooth attachment at +/-1, is true by nonsingular ODE uniqueness and matching of the constant solutions. The exact approved replacement is recorded below.

The quadratic endpoint transport has b partial_y=partial_tau, b'=-2/tau, tau=1/(3-|y|). T=C_T tau^-4 exp(-2d tau), q0 in E_(2beta+1), and v2=-sign(y)-q0/2. From24(T2), bD'+(7beta+2-4b')D=8v2'T-12v2T'. Division by T yields K_tau+(4beta+4/tau)K=-24d tau^2-48tau+E_(2beta+1). A polynomial particular approximation with coefficients k2=-6d/beta, k1=3(beta+6)/(2beta^2), k0=-15(beta+6)/(8beta^3) leaves only O(1/tau) forcing. Its stable integrating factor exp(4beta tau)tau^4 gives K=k2tau^2+k1tau+k0+O(1/tau). Since A D/T^2=rho^2K, its sign is eventually negative for either sign of A, with limit negative infinity. The asserted a0 times ratio uses a0=A/2, so has the same limit sign. The endpoints are limits from inside J only.

The first paragraph of report4.41 assumes the smooth fields, beta>=2, both global transport PDE, divergence and curl equations, sublinear velocity, x parity and the nonzero center coefficient, together with nowhere-zero T. Report4.42 removes the last condition outside the central component. Our manufactured fields satisfy the geometric and regularity assumptions, but not the simultaneous global transport equations. The proven failure is specifically R_Theta!=0. To avoid an unsupported reading that each of R_Theta and R_Omega has separately been proved nonzero, the second exact correction below states precisely this failure. The construction proves every Taylor coefficient of both residuals vanishes on the axis, not that either residual vanishes on a full neighborhood of the entire axis. Only near0 are both equations exact on an open set.

Report4.13(i),(iii),(v) use the low-order axis equations and predict the constructed positivity on J for A>0, the inward flow at the degenerate endpoints and flatness there. For A<0 the report's signed y-reflection changes A to-A and the two ends interchange. In report4.13(vi), analytic Theta on a neighborhood of the whole axis makes a(y)=Theta_xx(0,y)/2 analytic and nonzero at0. It therefore cannot be flat at a finite point or identically zero on an interval. The low-order axis ODE forces every zero of b to be simple. At a nearest attracting simple zero, smooth nonzero one-sided asymptotics force integer exponents n=2+(3beta+2)/k and m=1+(2beta+1)/k, k=-b'>0. They imply integer1/k and beta/k, and continuation to the next repeller with b=beta y+o(|y|) forces their sum odd. Thus no such nearest zero can occur at irrational beta or reduced beta=P/Q with P,Q both odd. This is why analyticity can exclude the manufactured bounded component although smoothness alone cannot. No analyticity is assumed in this construction.

Report4.42(b) and4.43 exclude two constant ratios on any J; here I2 diverges and is nonconstant. The infinite-end restrictions4.42(c),4.44,4.45,4.47(c),4.48 do not constrain the finite-end limits at hand. The comparison with4.30 is restricted to the previously adopted claims:4.30 has exact global thermal transport and J=R, while this compact-temperature construction has boundedJ and only axis thermal equations. A new possible exact-thermal boundedJ construction is treated separately in P283; it is not a premise or an approved theorem here.

Compact support yields every required polynomial upper bound and a zero exterior vorticity tail. Integration by parts against the harmonic function x gives integral x Omega=-integral Psi Delta x=0. Oddness in x and the nonzero local coefficient Omega_x(0)=2A/beta imply Omega cannot have a single sign on x>0. An exclusion using a sign or nonzero tail is therefore not tested by this example. These are precise missing hypotheses, not counterexamples to any full-profile theorem.

## Exact editorial corrections and document verification

Replace the one normalized sentence

    On [-1, 1] all forcing vanishes identically (a_1, q_0 and v_2 are constant there and the higher coefficients are 0), so these solutions are smooth across -1 and 1.

by

    On [-1, 1] these constant and zero coefficients solve their equations; the coefficients match to every order at -1 and 1, where b is nonzero, so the solutions attach smoothly.

Replace the one normalized clause

    except (T) and (V), which hold near 0 and to every order on the axis but not on R^2;

by

    except the simultaneous global equations (T) and (V): both hold near 0 and to every order on the axis, while (T) fails globally;

The first is a required factual repair. The second makes the already proved failure explicit without altering the construction. The whole-preview comparison must preserve every other mathematical and numerical statement. Controls independently parse the six Z-sections, insert the17paragraph item, apply each unique literal replacement, add the table row, and rebuild all155chronological timeline entries from the154frozen originals and the one specified new entry. Actual later adoption needs a fresh comparison. No finite symbolic control is represented as a proof of the all-order assertion. Public model487-490 reviews are read and adjudicated in the underlying P278 record; their actual returned model is claude-opus-5-5. The lead's A161 and A162 are separate referee answers, with their own model-availability statements.

## Complete underlying construction

The following is the verifier's complete previously proved P278 argument, included here so all mathematical construction dependencies are explicit.

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


## Complete endpoint and low-order mapping argument

# Transfer of the bounded-endpoint asymptotics to the all-axis construction

## Statement

Use the C-infinity construction of P278 for beta>=2, A!=0 and any prescribed realc0, with b_*,b,rho,a_n,q_n,v_n as defined in its complete PROOF.md. On J=(-3,3), put T=2a1, eta=q0, v=v1, D=24a2 and I2=D/T^2. Then the four axis identities of P273 hold and its functionsT,eta,v,D agree with these four functions onJ. Consequently, at either endpoint withs=3-|y|,

    D/T=-(6d/beta)s^-2(1+o(1)), A I2 -> -infinity,
    d=(3beta+2)/2.

These limits concern this specific manufactured b, with its quadratic zeros at the two endpoints; they are not a necessary asymptotic law for every bounded component of a genuine B2 profile. The compact full-plane realization and arbitraryc0 do not change these statements. This is a statement about manufactured non-solutions, not a consequence deciding existence of B2 profiles.

## Proof

In P278, b=b_* throughout[-4,4], so the coefficients in all ODEs onJ are independent ofc0 and agree with P273. Both rho functions equal1 on[-1,1] and solve the same ordinary linear equation forlogrho on each of(1,3),(-3,-1); uniqueness at any point adjacent to the inner interval proves equality. ThusT=2a1=A/rho² is the P273 secondjet.

The P278 vorticity equationV0 is bq0'+(2beta+1-b')q0=2a1=T. Bothq0 and P273eta equal2A/beta on[-1,1]. The same linearODE uniqueness on the two nonsingular intervals proves equality throughoutJ. The curl identity is v1=-(b''+q0)/2, so the two v-functions agree there as well.

For n=2 the P278 thermal recurrence is

    b a2'+(7beta+2-4b')a2=(2/3)v1'a1-v1a1'.

Multiplying by24 and usingT=2a1 gives

    b D'+(7beta+2-4b')D=8v1'T-12v1T'.

For the P273 definition throughG, differentiating rho³v=c2+(A/8)(dRI-kappaG), withG'=rhoI anddR=b rho, gives8v'T-12vT'=T²[bI'+(beta-2)I]. SinceD=T²I andbT'/T=-(3beta+2-2b'), this is precisely the same D equation. Thus this derivation uses the defining functions rather than assuming their identification. BothD=24a2 and the P273 D vanish on[-1,1]. Once again uniqueness proves equality onJ. No division by b at0 or at either endpoint is used. Both constructions prescribe the zero solutions on a neighborhood of0 and have already proved smooth flat continuation across the endpoints. They need not have identicalb orv outside[-4,4] for this argument.

For completeness the endpoint asymptotic can be derived directly. Settau=1/s. At both ends b partial_y=partial_tau, b'=-2/tau, T=C_T tau^-4 exp(-2d tau) withC_T=A/C_rho² nonzero, q0 inE_alpha withalpha=2beta+1, andv1 is-1+E_alpha near3 and1+E_alpha near-3. HereE_alpha means that each fixedtau derivative is bounded by a polynomial intau times exp(-alpha tau), andpartial_y=plus or minus tau²partial_tau preserves this property. The two signs cancel to give

    (8v1'T-12v1T')/T=-24d tau²-48tau+E_alpha.

Let K=D/T. Dividing the D equation byT, usingT_tau/T=-4/tau-2d and7beta+2-2d=4beta, yields

    K_tau+(4beta+4/tau)K=-24d tau²-48tau+E_alpha.

There is a degree-two polynomialk2tau²+k1tau+k0 whose residual against the left side matches the degree-two, degree-one andconstant terms on the right, leaving onlyO(tau^-1): k2=-6d/beta, k1=(-48-6k2)/(4beta), k0=-5k1/(4beta). Let Z be the difference betweenK and this polynomial. Then Z_tau+(4beta+4/tau)Z=O(tau^-1)+E_alpha. The integrating-factor formula withfactor tau^4 exp(4beta tau) boundsZ=O(tau^-1) plus an exponentially decreasing polynomial term. To justify the O(tau^-1) estimate directly, split the integral at tau/2. The earlier part is exponentially small after division; on[tau/2,tau] its integrand is bounded by a constanttau³ exp(4beta t), givingO(tau^-1). The exponentially decaying forcing is treated by the same split or by its actual exponent; no sign of4beta-alpha is needed. ThusK/tau²->k2<0. FinallyA I2=(A/T)K=rho²K andrho²=C_rho²tau^4exp(2dtau) tends topositiveinfinity, giving the assertednegativeinfinity at both endpoints.

The smooth realization of P278 preserves each coefficient exactly: the cutoffs equal1 nearx=0, and all series derivatives converge uniformly. Therefore derivatives atx=0 areT andD, regardless of the selected cutoff widths. The other global claims follow from the already proved P278 construction. Its nonzero integrated thermal residual is an explicit failure of the full PDE. Within the C-infinity class, the following listed conditions alone cannot exclude a bounded central component J: every axis Taylor equation of both PDE residuals, the exact full-plane inverse, the prescribed center drift, x-parity, and compactly supported (hence sublinear) velocity. Any exclusion must use a property not implied by that list, such as the transport equations off the axis or an additional regularity, positivity or asymptotic-class requirement derived from the PDE or admissible class. The example does not refute any previously proved global necessary condition. In particular it proves no compatibility of bounded J with the full B2 equations.

## Dependencies and verification scope

The all-order flatness and smooth realization are proved inP278 PROOF.md. The low-order identification uses P273's actual definitions and the derivations of its four axis identities on J, rechecked directly against research/273_bounded_axis_component/PROOF.md. Its endpoint asymptotic theorem is not used. A frozen copy of that source accompanies the model-review adjudication. The endpoint argument above reproves the particular P273 limit needed for a combined reportentry. The exact controls are supplementary; no finite symbolic truncation establishes an infinite-order existence theorem. No formalization is claimed or authorized.

Complete argument written at2026-10-22T05:15:00.697649+00:00 before supplementary controls.
