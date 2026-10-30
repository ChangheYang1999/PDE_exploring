# Candidate 025: independent acceptance of the registered complete weak test

## Statement and hypotheses

Fix c=4076476460239181/2251799813685248 and candidate
C1-N1-025-combined-heldin1e16 with raw SHA256
 3b1c9f7199b56fc892815eefac8696e811a72d729ead5b955491e20961221f17.
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

 ||h||2 > 516450316394513/250000000000000000.

This exceeds 25/54684, the registered original graded L2 ceiling. Applying
this to any named correction ball requires its L2 embedding and the weak
hypotheses above. Changing c needs the separate tail-pinning theorem.
The probe belongs to the 25-probe preregistered extension and lies outside
the recorded analytic objective span through the actual025 stage, parent016 shapes/launch and exact013 quotient, as proved
in the hash-bound candidate025_holdout/PROOF.md. This is not statistical
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

The original N4-364 calculation uses Cartesian differentiation of the
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

## Actual three-scale validation and general scalar fixtures

All three factors1+624v,1+2499v,1+9999v occur in actual025 fields and moments. Each rational denominator stores three nonnegative powers. Independently inspect addition, multiplication, differentiation and all angular assembly formulas for use of all three slots. Recheck eight fresh scalar fixtures, including each pole separately, mixed pairs and simultaneous simple/repeated triple factors. Require every exact CRT identity and at least150 relative accuracy bits for every nonzero moment. No fixture is skipped. For each actual I, parts, M and C grouping, record all three positive poles and require at least one group with all three active. Compare all63 complete integrals with N4-364; no new residual quadrature is used by this acceptance. Own construction has independent Cartesian differentiation and local Taylor partial fractions. Peer construction uses polar identities and CRT inverses. Source files are read as text only.

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

The checker records any difference in denominator powers and requires every
corresponding complete integral to overlap. It does not infer equality of
stored numerators from equality of those integrals. Algebraic reconstruction
is justified by the complete formulas and exact identities above. The accepted
020 algorithm had a comparison repair for this representation issue; the
present025 checker begins with that corrected rule and recomputes every
current interval comparison.

## Current candidate and independent provenance

The own complete Cartesian certificate is N4-364. The independent actual025 polar/CRT/direct-hypergeometric record is frozen by its exact SHA256 before comparison; it retains its full proof, source graph, eight manufactured fixtures,63 whole-plane integrals, six actual point checks and global gradient certificate. The current81-row objective span was independently accepted in N4-365 through T4-436. The public25-probe register predates the snapshot; prior source history is inherited with its existing observation limits, not newly witnessed. The weak inequality does not require probe novelty. All statements about the full correction norm retain fixed-c, canonical realS1 and weak-product hypotheses. The necessary bound supplies no actual residual upper bound, inverse, optimizer cause or existence theorem.

Written 2026-10-29T13:17:51.509506+00:00 before this comparison code. The proof is adapted from the accepted scalar argument, with the actual three-scale integration and all current numerical inputs checked independently. No publisher or peer program is executed.
