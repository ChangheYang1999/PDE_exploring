# Candidate 020: independent acceptance of the registered complete weak test

## Statement and hypotheses

Fix c=4076476460239181/2251799813685248 and candidate
C1-N1-020-legqs25p50-quot013 with raw SHA256
 bddbd3120852a815cfe850635564cb09ab52a98ec596a4cce3b72c98cf04f7cf.
Set gamma=1/c, delta=1-gamma, rho=-chi_xxy-chi_yyy,
u=(-chi_xyy,chi_xxy), and F=(cX+u).grad rho-rho from that exact potential.
Let h be a real S1-symmetric member of L2(R2). Assume rho+h is stationary
in distributions at this same c, with the canonical decomposition
U[rho+h]=u+U[h], div U[h]=0, ||U[h]||2<=||h||2 and locally integrable weak
products. These hypotheses are required; the certificate does not prove
existence or an inverse.

For t=r^2/(1+r^2), v=1/(1+r^2), use
 phi_(n,K)=r v^2 t^K sin(n theta).
The independently reproduced (19,1800) certificate implies the strict
necessary bound

 ||h||2 > 231921834680339/125000000000000000.

This exceeds 25/54684, the registered original graded L2 ceiling. Applying
this to any named correction ball requires its L2 embedding and the weak
hypotheses above. Changing c needs the separate tail-pinning theorem.
The probe belongs to the 25-probe preregistered extension and lies outside
the recorded analytic objective span from 007 through 013 and 016 to 020, as proved
in the hash-bound candidate020_holdout/PROOF.md. This is not statistical
independence from the sampled objective, and no maximum is asserted.

## Complete weak argument

Put Mfield=(2c+1)phi+(cX+u).grad phi, I=int F phi,
M=||Mfield||2, C=||phi grad rho||2, and H=||grad phi||infinity.
The reference has smooth fields with rho,u=O(r^gamma), gamma<1. For our
odd n and2K+1>=n the probe is smooth at zero, since its numerator is a
harmonic polynomial of degree n times an even radial power. It decays
as r^-3 and has bounded gradient. All reference integrals converge.

Subtract the stationary equations and test against phi. Integrating the
drift and transport terms by parts, using div(cX+u)=2c, gives the term
-int h Mfield. The other linear term is int U[h].grad rho phi; the
quadratic term is -int h U[h].grad phi. Cauchy-Schwarz and the velocity
contraction yield

 |I| <= (M+C)||h||2+H||h||2^2.

Smooth radial cutoffs justify every integration. Reference boundary terms
vanish from gamma<1 and probe decay; correction boundary terms vanish by
L2 tails, bounded probe derivatives and Cauchy-Schwarz. Testing only the
reference transport equation also gives I=-int rho Mfield. For a rational
Hbar>=H the nonnegative quadratic is increasing, so

 ||h||2 >= 2|I|/(D+sqrt(D^2+4Hbar|I|)), D=M+C.

An outward interval whose lower endpoint is strictly above the proposed
rational floor proves the stated strict bound.

## Independent full-plane arithmetic

The original N4-293 calculation uses Cartesian differentiation of the
exact rational radial class, local Taylor partial fractions and a
recurrence in the pole order for factored moments. The independent T4
path rebuilds density and stream coefficients from polar Laplacian and
stream identities. For S=1+r^2 and a potential S^p A(t)cos(m theta), set
E_p A=2tv A'+2pt A, B=E_p^2 A-m^2 A, D_p=E_p B-2B.
Its density modes m-1,m+1 have numerators (D_p+mB)/2 and
-(D_p-mB)/2, divided exactly by t^2. Its stream modes m+2,m-2 have
numerators [E_p(E_p A-mA)-(m+2)(E_p A-mA)]/4 and
-[E_p(E_p A+mA)+(m-2)(E_p A+mA)]/4, also divided by t^2.
Negative sine modes change sign. This follows by differentiating the
polar Laplacian and chi_xy; division is checked as a polynomial identity.

Writing rho=r sum v^a R sin and psi=r^2 sum v^a S sin, radial
coefficients differentiate by T_d A=(d-2at)A+2tv A'. Thus u_r=-r sum
m v^a S cos, u_theta=r sum v^a T_2 S sin, rho_r=sum v^a T_1 R sin and
rho_theta/r=sum m v^a R cos. Ordinary sine/cosine product identities
construct every matching Fourier coefficient of F and Mfield. Complete
angular integration of phi^2|grad rho|^2 gives the factors
 2[m=l]-[|m-l|=2n]+[m+l=2n]
for the radial products and the same factor with the final sign minus
for angular products. Every ordered pair is included. There is no
angular quadrature or omitted sector.

The radial integrations reduce, without a spatial cutoff, to
 J=integral_0^1 v^b(1-v)^L N(v)/D(v) dv, b>-1,
where L is K or2K and N includes the remaining factor1-v. All denominator
factors are1+a v>0. T4 obtains their exact partial fractions using an
extended-Euclidean CRT inverse and replays the complete polynomial
identity. It evaluates polynomial moments by Beta(b+j+1,L+1), and each
pole moment directly by
 Beta(b+1,L+1) 2F1(k,b+1;b+L+2;-a).
The equality follows from Euler's convergent beta integral since b>-1,
L>=0 and a>0. The special-function integer flags are valid because
c-b=L+1 and c-a-b=L+1-k are integers. The latter may be negative.
The underlying ball evaluation must remain finite with more than150
relative accuracy bits for every nonzero grouped moment. Direct and
integration-by-parts pairings independently overlap.

## Global probe gradient and acceptance checks

At fixed t the squared gradient is the sum of squared radial/angular
amplitudes times sin^2/cos^2. Its angular maximum is the larger amplitude.
They are t^K(1-t)^2[(2K+1)-(2K+4)t] and n t^K(1-t)^2. The endpoints vanish.
The angular maximum occurs at t=K/(K+2). The radial stationary points
are the two roots in(0,1) of
 (2K+4)(K+3)t^2-[(K+2)(2K+1)+(K+1)(2K+4)]t+K(2K+1)=0.
Evaluation at these three points proves the global rational Hbar. The
checker independently recomputes them and the stable quadratic root.

Freeze every T4 input with its recorded hash, using identical own files
where available. Recheck the raw identities, all eight complete scalar
intervals, signs/positivity, Hbar, strict floors, objective registration,
all endpoint exponents, CRT replay flags, grouped-moment accuracy and
the scalar fixtures. Point fixtures bind the actual candidate fields;
the radius1 exact map fixture checks the entire old polynomial path.
Compare complete moment groups too wherever the two representations
coincide. This is acceptance of a genuinely different polar and direct
special-function computation, not rerunning its code. Only own comparison
and scalar recomputation code is executed. Both original full computation
records and all source hashes remain available alongside this proof.

## Actual two-pole validation

Both factors1+624v and1+2499v occur jointly in this candidate. Recheck
six fresh manufactured scalar fixtures, including both single-pole and
mixed-pole cases, against explicitly expanded localization. Every exact
CRT identity and nonzero accuracy requirement must pass. No fixture-skip
or single-scale source equivalence is assumed. Independently review the
full mixed polar primitive and rational class. All63 actual groups have
fresh field reconstruction, direct hypergeometric moments and point
checks. Compare the two denominator power slots and both actual pole
slopes where recorded. Every actual interval and strict floor is newly
checked. The own N4-293 full mixed Cartesian computation is independent
of the peer's polar assembly and CRT partial fractions.

## Noncanonical denominator representations

A denominator exponent is part of a rational representation, not an
invariant of its function or integral. For D_i=1+a_i v>0, the pairs
(N,prod_i D_i^k_i) and (N prod_i D_i^h_i,prod_i D_i^(k_i+h_i))
represent the same function for any nonnegative h_i. Assembly can retain
such uncancelled factors, so equality of stored denominator powers is
not an acceptance condition. Each path must use the correct positive
slopes, establish b>-1, replay its own exact partial fraction identity,
and enclose its complete integral. All corresponding integral intervals
must overlap; equality of the underlying reconstruction is justified by
the separate Cartesian and polar derivations above.

In ten actual direct/by-parts groups, ell4 through8, the N4 common
powers are37/37 or36/36 and the T4 powers are19/19 or18/18. This does
not assert that their stored numerators are equal. The initial comparison
checker incorrectly required identical powers and failed only those ten
checks. Its source and failure log remain unchanged. The revised checker
records both representations, validates their slopes and nonnegative
integer orders, retains every integral comparison and exact-replay check,
and additionally checks every N4 pole-recurrence/direct-2F1 comparison.
No numerical enclosure or strict correction floor changes.
