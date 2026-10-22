# A whole-plane auxiliary inverse at the hyperbolic source

Status at proof writing: complete proposed proof, pending independent review
and arithmetic checks. This constructs only the auxiliary cut-off-coefficient
operator from topic77. It does not assemble the full IPM inverse.

## Statement and dependencies

Use the unitary Fourier transform and H^r norms defined by J^r=(1-Delta)^(r/2)
on R^2. Set s=31/10, t=s-1. Let D=diag(A,mu), P in R^2, and assume

 10<=A<=51/5, 99/100<=mu<=101/100, 29<=g<=30.

Let w and q be real vector fields in C_c^4(R^2). Write b=D(X-P)+w and

 Aop u=b.grad u-u-gM u+q.Uu,
 Mhat=xi^2/(xi^2+eta^2),
 Uhat=(xi eta,-xi^2)/(xi^2+eta^2).

The value of these bounded multipliers at frequency0 is immaterial.
Vector and derivative tensor norms are Euclidean and Frobenius norms.
Define

 kappa=1687/500,
 E=||div w||infinity/2+s||Dw||infinity,F+||q||infinity,
 R=T_s(w)+sum_i P_s(q_i),
 a_s=kappa-E,
 a0=1+(A+mu)/2-||div w||infinity/2-||q||infinity,
 d=a0-a_s=1+(A+mu)/2-kappa+s||Dw||infinity,F.              (1)

Here, for compact coefficients,

 W_r(f)=(2pi)^(-1) integral <xi>^r |fhat|,
 alpha_r=[2sqrt(pi(r-1))]^(-1),
 beta_r=[2sqrt(pi(r-1)(r-2))]^(-1),
 P_s(f)=s2^(s-2)[W1(f)+alpha_(s-1)||f||Hs],
 T_s(w)=s(s-1)2^(s-4)sum_i[W2(w_i)+beta_(s-1)||w_i||Hs].

All are finite for C_c^4 coefficients. Suppose E<kappa. Then the maximal
realization

 D(Aop)={u in Hs: b.grad u belongs to Hs as a distribution} (2)

is densely defined and generates a strongly continuous semigroup S_A(t).
It has the bound

 ||S_A(t)||_(Hs->Hs)<=C exp(-a_s t),
 C=(1+R/d)^s,
 d>=3121/1000>0.                                         (3)

It is invertible onto Hs, and

 Aop^(-1)f=-integral_0^infinity S_A(t)f dt,
 ||Aop^(-1)||_(Hs->Hs)<=C/a_s.                            (4)

This includes existence, uniqueness and an explicit domain, unlike an a
priori inequality alone. No prescribed outer data is included.

The analytic dependency is topic77, sections2-4, which proves on Schwartz u

 Re<Aop u,u>Hs<=-a_s||u||Hs^2+R||u||Ht||u||Hs,             (5)
 [J^s,w.grad]u=-s sum_(i,j)w_(i,j)partial_ij J^(s-2)u+R_wu,
 ||R_wu||2<=T_s(w)||u||Ht.                                (6)

For clarity, the passage from (6) to a bounded conjugation, the generator,
its maximal domain, its core, and the extension of (5) are proved below.
No external semigroup theorem or unspecified core assertion is needed.

## 1. The L2 transport group and its maximal domain

The field b is globally C1, globally Lipschitz, and grows at most linearly.
Its ODE has a global flow Phi_tau for all real tau. For example, the local
Picard contraction on a time interval shorter than the reciprocal Lipschitz
constant gives existence and uniqueness; the estimate
|Phi_tau(X)|+1<=(|X|+1)exp(C|tau|) prevents finite-time escape, so these
solutions extend and compose for all time. Differentiating the integral
flow equation in X gives a C1 diffeomorphism with inverse Phi_-tau.
Its Jacobian determinant solves

 det D Phi_tau(X)=exp(integral_0^tau div b(Phi_v(X))dv).

Put T(tau)f=f composed with Phi_tau. Change of variables gives

 ||T(tau)||_(L2->L2)<=exp(||div b||infinity |tau|/2).        (7)

For a smooth compact f, T(tau)f tends to f in L2 by uniform convergence on a
fixed bounded support for small tau. Density and (7) prove strong continuity
on L2. On C_c^infinity, differentiation in L2 shows that its generator is
b.grad.

We next identify its full generator domain as

 D0={f in L2: b.grad f in L2 in distributions}.            (8)

First C_c^infinity is a core for the distributional operator in (8).
If f is in D0, multiply by chi_R(X)=chi(X/R), where chi=1 on B1 and0 outsideB2.
Then f_R tends to f in L2, and

 b.grad f_R=chi_R b.grad f+(b.grad chi_R)f

converges to b.grad f in L2. Indeed |b.grad chi_R| is bounded independently
of R>=1 and supported where R<=|X|<=2R, so its L2 product with f tends to0.
Now mollify a compactly supported f_R by eta_epsilon. For any f in L2 the
transport commutator is

 b.grad(eta_epsilon*f)-eta_epsilon*(b.grad f)
 =integral grad eta_epsilon(X-Y).(b(X)-b(Y)) f(Y)dY
    +integral eta_epsilon(X-Y)div b(Y)f(Y)dY.              (9)

Its L2 operator norm is at most

 ||Db||infinity integral |Z||grad eta(Z)|dZ+||div b||infinity,

uniformly in epsilon, by Young's inequality and Lipschitz continuity.
For smooth compact f it tends to0 in L2, by ordinary differentiation and
mollification. Density and the uniform bound show strong convergence to0
for every f in L2. Thus eta_epsilon*f_R is a smooth compact graph
approximation to f_R, and a diagonal sequence proves the core assertion.

Because generators are closed, (8) is contained in the generator domain:
the graph approximants lie in the generator domain and their derivatives
converge to b.grad f. Conversely, if a difference quotient for T(tau)f has
an L2 limit, pair it with a compact test phi and change variables. The
paired derivative is -integral f div(b phi), since the derivative of
phi composed with Phi_-tau times its Jacobian is -div(b phi).
Thus that L2 limit is b.grad f in distributions. This proves (8).
Closedness itself follows directly from T(t)f-f=integral_0^t T(v)Gf dv:
pass to graph limits and then divide by t and use strong continuity.

Finally, the L2 integration-by-parts identity

 Re<b.grad f,f>2=-1/2 integral div b |f|^2                (10)

extends from smooth compact functions to all D0 using the graph core and
bounded div b. This will be used for a second energy inequality.

## 2. Bounded Sobolev conjugation

On Schwartz u, Fourier differentiation gives

 [J^s,D(X-P).grad]J^(-s) f
       =F^(-1)[s(Axi^2+mu eta^2)/(1+xi^2+eta^2) fhat].    (11)

The sign is positive. This multiplier is bounded on L2 by s max(A,mu).
The constant translation by P commutes with J^s. In (6) put u=J^(-s)f.
Its leading term becomes

 -s sum_(i,j) w_(i,j) partial_ij J^(-2) f.

Pointwise tensor Cauchy-Schwarz and
sum_ij||partial_ij J^(-2)f||2^2<=||f||2^2 bound it by
s||Dw||infinity,F||f||2. The remainder norm is at most
T_s(w)||J^(-s)f||Ht<=T_s(w)||f||2. Hence

 C_s=[J^s,b.grad]J^(-s)

extends to a bounded L2 operator with norm at most
s max(A,mu)+s||Dw||infinity,F+T_s(w).
The lower-order B=-1-gM+q.U also has a bounded conjugation B_s=J^s B J^(-s),
by the multiplication estimate of topic77; one possible bound is

 ||B_s||<=1+g+||q||infinity+sum_i P_s(q_i).                (12)

The pointwise vector inequality for q.U controls its leading term, and
[J^s,q_i]U_i controls the remainder. All symbols commute with J^s.

These identities extend as distributions to arbitrary u in Hs by Schwartz
approximation. Indeed linear-coordinate multiplication and differentiation
are continuous on tempered distributions; the compact C4 products here
are continuous on the indicated Sobolev spaces. The identity gives

 J^s b.grad u=b.grad J^s u+C_s J^s u.                    (13)

Consequently b.grad u belongs to Hs if and only if J^s u belongs to D0.
This proves that (2) is precisely J^(-s)D0.

## 3. Construction, generator and core

On L2 let G0 be the transport generator in (8), let C0=C_s+B_s be the
bounded operator just obtained, and let G=G0+C0 with domain D0.
For t>=0 construct

 S0(t)=T(t),
 S_(n+1)(t)=integral_0^t T(t-v) C0 S_n(v)dv,
 S_G(t)=sum_(n>=0) S_n(t).

By (7), ||S_n(t)||<=exp(omega t)||C0||^n t^n/n!, where
omega=||div b||infinity/2. The series converges uniformly on compact
time intervals in operator norm after its n=0 term. It is strongly
continuous. Its Volterra equation has a unique strongly continuous solution:
the difference of two solutions is bounded by the n-fold integral estimate
for every n, which tends to0. Splitting that equation at time t and using
uniqueness proves S_G(t+v)=S_G(t)S_G(v).

We verify its generator domain, rather than asserting it from boundedness.
For lambda>omega+||C0||, the Laplace transform of T is
R0(lambda)=integral_0^infinity exp(-lambda t)T(t)dt.
Integrating the generator identity first on its domain and then using
strong continuity proves R0=(lambda-G0)^(-1). Equivalently, for arbitrary
f the integral over a finite interval belongs to D0 by its difference
quotients, and taking the infinite graph limit proves the same conclusion.
Integrating the convergent Dyson series gives

 integral_0^infinity exp(-lambda t)S_G(t)dt
   =R0(lambda)[I-C0 R0(lambda)]^(-1).                    (14)

The Neumann series converges because ||C0 R0||<1. Direct multiplication
shows that this is the inverse of lambda-(G0+C0) on domain D0. The same
finite-integral difference-quotient argument identifies the Laplace
transform of S_G with the resolvent of its generator. A shared resolvent
identifies both domain and operator, so its generator is exactly G.

Conjugate back to Hs:

 S_A(t)=J^(-s) S_G(t) J^s.

It is a strongly continuous semigroup with generator Aop and domain (2).
Bounded perturbation preserves graph cores: graph convergence for G0 is
equivalent to graph convergence for G0+C0. Thus J^(-s)C_c^infinity is a
core for Aop. Each such function is Schwartz, since J^(-s) is a smooth
Fourier multiplier with polynomially controlled derivatives and preserves
the Schwartz class. This is the promised core on which (5) was proved.

## 4. Energy on the full domain and exponential decay

Graph convergence from that core passes every term of (5) to the limit:
Aop u and u converge in Hs, and Hs convergence implies Ht convergence.
Therefore (5) holds for every u in D(Aop).
Also u in D(Aop) implies u is in D0 as an L2 function, since
b.grad u=Aop u-Bu belongs to Hs, hence to L2. By (10), positivity of M,
and the vector symbol bound ||Uu||_(L2 vector)<=||u||2,

 Re<Aop u,u>2<=-a0||u||2^2.                              (15)

For initial u in the generator domain, the semigroup preserves that domain
and its trajectory is differentiable there in Hs. This follows directly
from the difference quotient: Aop S_A(t)u=S_A(t)Aop u.
Hence y(t)=||S_A(t)u||2<=exp(-a0 t)y0. Fourier Holder interpolation gives

 ||v||Ht<=||v||Hs^(1-1/s)||v||2^(1/s).

For x(t)=||S_A(t)u||Hs while x(t)>0, (5) yields

 x'<=-a_s x+R x^(1-1/s)y^(1/s).

If x first reaches0, the trajectory is identically0 afterwards by the
semigroup property; thus integrating only up to that time suffices.
For z=x^(1/s), multiplication by exp(a_s t/s) and integration give

 x(t)^(1/s)<=exp(-a_s t/s)
 [x0^(1/s)+(R/d)y0^(1/s)(1-exp(-dt/s))].                  (16)

The box implies

d=1+(A+mu)/2-kappa+s||Dw||infinity,F
 >=1+(10+99/100)/2-1687/500=3121/1000.

Since y0<=x0, (16) proves (3) on domain initial data. Density and strong
continuity extend it to every initial u in Hs. No low-frequency compactness,
Fredholm argument or smallness of the unbounded transport perturbation was
assumed in this construction.

## 5. Inversion and the remaining rank-one condition

The integral in (4) converges in Hs by (3). For every f, a finite semigroup
integral is in the generator domain and

 Aop integral_0^T S_A(t)f dt=S_A(T)f-f.

Take the graph limit as T tends to infinity. The negative integral is in
the domain and is a right inverse. If Aop u=0, then S_A(t)u=u for all t;
(3) forces u=0. This proves both-sided inversion and its stated norm.

For any ell_delta in Hs, let sigma[u]=psi[u]_xy(0) be the raw canonical
strain, Delta psi=partial_x u. Its Fourier symbol at the evaluation point
has magnitude |eta xi^2/(xi^2+eta^2)|<=|(xi,eta)|. Thus Cauchy-Schwarz gives

 |sigma[u]|<=beta_s||u||Hs,
 beta_s=[2sqrt(pi(s-1)(s-2))]^(-1).                       (17)

This defines a continuous functional without invoking a pointwise singular
integral or origin vanishing. The bounded rank-one perturbation
Aop+ell_delta sigma has the same domain and is invertible if and only if

 Delta_sigma=1+sigma[Aop^(-1)ell_delta] !=0.               (18)

If (18) holds, its inverse is

 Aop^(-1)f - Aop^(-1)ell_delta
                 sigma[Aop^(-1)f]/Delta_sigma.

If the scalar vanishes, v=Aop^(-1)ell_delta satisfies sigma[v]=-1,
so v!=0 and is a null vector of the perturbed operator. With
K_A=C/a_s, the inverse norm when (18) holds is at most

 K_A+K_A^2 ||ell_delta||Hs beta_s/|Delta_sigma|.           (19)

No nonzero enclosure of Delta_sigma for the actual trial is supplied.

## Scope and remaining tasks

This theorem closes the generator/domain gap left explicitly open in
topic77, for the auxiliary global C4 cut-off coefficients satisfying E<kappa.
It is consistent with the local estimate there. It proves neither a
solution with arbitrary outer data nor invertibility for the full IPM
linearization. The actual derivative bounds that ensure E<kappa, a useful
numerical value of the auxiliary inverse constant, the rank-one denominator,
outer matching, centre and far-field spaces, high-norm residual control,
and a nonlinear contraction are still required. No decisive endpoint follows.
