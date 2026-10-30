# Independent audit of theory_v03

The audited publication is the frozen source/theory_v03.md, SHA256
 e541f3ba19c8a67d51c5792600a461c971cc8575eab18ffeb07cc9a29c2e0b19.
This audit concerns the new Newton and Gauss-Newton statements in R6 to
R9, the scalar defect criterion, and their stated scope. Existing
background inverse theorems retain their previously audited hypotheses.
No existence theorem or new candidate is established here. The proof was
written before the scalar arithmetic in verification/.

## 1. Newton-step necessary bound

Let H be the real closed subspace of L2(R2) consisting of functions even
in x and odd in y. Fix a smooth real S1 reference density rho, a real c,
and its canonical divergence-free IPM velocity U[rho]. The velocity
operator U on H has Fourier symbol

    (xi1 xi2, -xi1^2)/|xi|^2,

and norm at most one from H to L2(R2;R2). Write V=cX+U[rho] and

    Lh=V.grad h+U[h].grad rho-h,
    F=V.grad rho-rho.

For a smooth real S1 test function phi assume that

    M=(2c+1)phi+V.grad phi belongs to H,
    phi grad rho belongs to L2(R2;R2),

and that testing the stated distributional equation against phi is
justified by compact cutoffs with vanishing error. If h in H and Lh=-F
in this sense, integration by parts using div V=2c gives

    <F,phi>=<h,M>-<U[h],phi grad rho>.

Consequently, with I=<F,phi> and D=||M||2+||phi grad rho||2,

    |I| <= D ||h||2.                                      (1)

This proves R6(a), including its sign. There is no assumption that L is
invertible and no derivative gain. For any h for which the same pairing
is defined, the reverse triangle inequality also gives

    |<F+Lh,phi>| >= |I|-D||h||2.                           (2)

This proves R9(e) before its numerical substitution. The frozen mode-7
probe has already been justified and independently reproduced in
T4-185, R1-022, N4-157 and T4-196. This audit uses those certified I,M,C
intervals and does not claim an additional independent field evaluation.

For the printed constants a=0.0047694 and I0=0.000017647, its last
assertion follows from the two strict inequalities

    I>I0,  I-Da>0.

Indeed, I-Dm-I0(1-m/a) is affine in m and nonnegative at both endpoints
of [0,a]. Hence it is positive throughout that interval. This argument
avoids replacing D by an unjustified rounded upper bound. The local
Arb check in verification/result.json verifies both endpoint comparisons.

### Exact inverse interpretation

R6(b) must specify an operator domain: transport is an unbounded
operator on L2. Let L:D(L) subset H -> H be a closed densely defined
realization, bijective with bounded inverse H -> H, and assume F in H.
Let P be a linear subspace of D(L*) whose image L*P is dense in H.
For h0=-L^-1 F, the adjoint identity yields

    sup(phi in P, L*phi != 0) |<F,phi>|/||L*phi||2=||h0||2. (3)

The upper bound is Cauchy-Schwarz. For the lower bound approximate h0
by vectors L*phi in the dense image and divide their scalar products
with h0 by their norms. If h0=0 the equality is immediate. For admissible
smooth probes the adjoint expression is

    L*phi=-M+U*(phi grad rho),

so ||L*phi||2<=D. This confirms the proposed dual interpretation under
the precise domain, range and density hypotheses above. Neither a
closed realization with this inverse nor the required density of the
probe image has been verified for candidate007 in this audit.

## 2. The full generator span is not an L2 correction space

Let Vpot be the 1922-dimensional potential span of the 2982 generators
of candidate007, as in T4-195. T4-199, independently reviewed in R1-024
and accepted in T4-212, proves injectivity of chi -> -d_y Delta chi on
Vpot. Write Vdens for its 1922-dimensional density image.

The entire density of candidate007 belongs to Vdens. Its leading term
is r^gamma Theta(theta), where gamma=1/c>0 and Theta is nonzero; its
first sine coefficient is strictly between 18 and 19 (T4-203, T4-208).
The finite expansion is uniform in angle. Since ||Theta||L2(S1)>0,
for all sufficiently large r the angular L2 norm of this density is
bounded below by a positive constant times r^gamma. Integrating its
square against r dr diverges. Thus Vdens is not a subspace of L2(R2).

Every basis of Vdens contains at least one vector outside L2; otherwise
all its finite linear combinations would belong to L2. A purported L2
Gram matrix on that full basis has at least one infinite diagonal entry.
It therefore cannot define the generalized finite matrix problem in
R9(c). Removing ker Phi alone does not repair this domain problem.

### A sufficient admissible restriction

One can first restrict to the tail-preserving kernel Kpot in T4-209.
There are 420 independent tail rows: in every block (j,m) the leading
moment vanishes, and for j=0,1,2 its first descendant also vanishes.
The block potential is

    H_m(X)(1+r^2)^(p_j-m)P(t),
    p_j=(3+gamma-j delta)/2, delta=1-gamma, t=r^2/(1+r^2).

The conditions P(1)=0 and, where applicable, P'(1)=0 give respectively
one and two extra factors (1-t). After three derivatives, each resulting
density is O(r^(gamma-j delta-2)) for j>=3, and
O(r^(gamma-j delta-4)) for j=0,1,2. These estimates hold with the
corresponding differentiated powers, since every expression is a finite
smooth algebraic expansion. The largest exponent is 4gamma-5<-1.
The densities are smooth near the origin, so every element of the
density image Kdens is in L2. Its dimension is 1922-420=1502.

Fixing strain leaves dimension1501. Imposing the five independent
Taylor differentials at007 leaves dimension1496 (T4-209). These latter
five are tangent conditions at the actual candidate values; candidate007
is not itself exactly on the zero-Taylor level set. This distinction
must be preserved in a constrained Gauss-Newton interpretation.

For any independent finite density basis e_i of Kdens, its L2 Gram
matrix G_ij=<e_i,e_j> is finite and positive definite: v^T G v equals
the squared L2 norm of a nonzero linear combination. A chosen closed
realization of L still needs e_i in D(L), and its output must be in the
specified row domain. Only after these verifications is

    sigma=min(h in W, h!=0) ||R Lh||/||h||2               (4)

a well-defined finite-dimensional quantity for W subset Kdens. This
argument supplies a sufficient correction space, not a classification
of all possible L2 subspaces or a PDE Jacobian rank calculation.

### What a generalized singular value can prove

Let W be any finite subspace of D(L) intersect H, and let R be linear on
L W with values in a normed finite row space. If c_R>0 satisfies

    ||R g|| >= c_R ||g||Y for all g in L W,

then a minimizer in (4), normalized in H, gives

    inf(h in W, ||h||2=1) ||Lh||Y <= sigma/c_R.

If a left inverse maps Y to H and agrees with inversion on L W, its
operator norm is at least c_R/sigma. A zero sigma rules out such an
inverse. These are the conditional assertions of R9(d). The lower
row domination c_R is substantive and has not been supplied by merely
choosing point samples or weak rows. A large finite sigma gives no
control on the infinite-dimensional complement.

For any coefficient Jacobian J=R L Phi, ker Phi subset ker J. Thus its
nullity is at least1060, and J*J has at least1060 zero eigenvalues. Saying
that the usual min(number of rows,number of columns) singular-value
list itself has1060 zero entries requires enough rows; the nullity
formulation is valid without that extra assumption.

The 1.5e-8 normal-equation resolution statement in R9(c) is a binary64
scale heuristic, not a verified universal bound. An actual certificate
needs dimension-dependent assembly errors, Gram errors, and the
conditioning of its orthonormalization as well as eigenvalue errors.

## 3. The missing defect feasibility condition

Let A>0, mu real, and m,B,epsilon>=0. A radius r>0 satisfies

    beta=mu-Ar>0,  m+(epsilon+Br)/beta<=r                 (5)

if and only if

    mu-Am-B>0,
    epsilon<=((mu-Am-B)^2-4ABm)/(4A).                    (6)

This is the already audited scalar statement of T4-065. For completeness,
put x=r-m. Multiplying by beta gives

    -Ax^2+(mu-Am-B)x-Bm-epsilon>=0, x>=0.

A nonpositive linear coefficient is impossible: at x>0 every term is
negative or nonpositive, while equality at x=0 would require
Bm=epsilon=0 and beta>0,r=m>0, forcing B=0 and mu-Am>0, a contradiction.
For a positive linear coefficient the maximum over x>=0 occurs at
x=(mu-Am-B)/(2A). Its nonnegativity is exactly the second condition in
(6). That vertex gives a positive r and beta, proving sufficiency.

The theory_v03 phrase 'feasible iff mu-Am-B>0' omits the second
condition. Even existence of any allowable epsilon>=0 needs the printed
epsilon_max to be nonnegative. For A=m=B=1 and mu=3 the first condition
holds, while epsilon_max=-3/4, so no nonnegative epsilon is feasible.
This refutes the compressed criterion, not the underlying defect theorem
or its explicitly verified scalar boxes.

## 4. Strictness for a closed exclusion ball

The full nonlinear weak test gives

    |I| <= Dm+Hm^2,  m=||h||2,  D,H>=0.

For a closed ball m<=b, exclusion follows from the strict inequality
|I|>Db+Hb^2. The non-strict inequality printed in R6(d) does not by
itself exclude a boundary solution. It excludes the open ball m<b
when D or H is positive. As a scalar logical counterexample to the
claimed implication, take D=1,H=0,I=b>0,m=b: both the necessary weak
inequality and the asserted exclusion premise are equalities.
All currently used certified exclusions have a positive strict gap,
so this correction does not reverse any of those exclusions.

## 5. Scaling and scope

The elementary scaling identities in R7(a) hold for canonical U,
interpreted by Fourier multipliers for decaying fields and by the fixed
homogeneous canonical continuation for the growing S1 references.
For S_lambda g(X)=lambda g(X/lambda), homogeneity of U and the chain
rule give U S_lambda=S_lambda U and F(S_lambda rho;c)=S_lambda F(rho;c).
The change of variables X=lambda Y gives

    ||S_lambda g||2=lambda^2||g||2,
    ||(1+r^2)^(-a/2)S_lambda g||2
      =lambda^2||(1+lambda^2 r^2)^(-a/2)g||2.

The derivative of S_lambda rho at the origin is independent of lambda,
as is the derivative of its canonical velocity. For the probe
phi_lambda(X)=phi(X/lambda), I scales by lambda^3, D by lambda,
and H=||grad phi||infinity by lambda^-1. Thus its necessary L2 radius
scales by lambda^2, exactly as the L2 distance. The operator identity
for the linearization follows by differentiating the equivariance.
It does not turn an inadmissible dilation direction into a member of
a fixed L2 correction domain.

To obtain the printed asymptotic for Lambda rho=rho-X.grad rho from
a leading asymptotic for rho alone, a differentiated remainder estimate
is needed. Under rho=r^gamma Theta+o(r^gamma) and
X.grad rho=gamma r^gamma Theta+o(r^gamma), its leading term is
(1-gamma)r^gamma Theta. The registered algebraic references have such
expansions. For a general solution the derivative estimate must be
proved or derived from its equation and stated growth controls; it is
not a formal consequence of an undifferentiated little-o statement.

Normalizing a localized weight by inf psi=0 gives
||exp(psi)h||2>=||h||2. This forces any007-containing closed ball in
that norm to have radius strictly above the established lower distance
bound. It does not forbid a new theorem certifying a larger radius.
Section1's statement that the normalized localized route cannot be a
larger-ball route is therefore unsupported and should be replaced by
this necessary radius condition.

A rigorous violation by an objective row remains mathematical evidence;
using that row during optimization does not invalidate it. A small row,
held out or optimized, does not prove proximity or existence. Likewise,
lower distance bounds do not order actual distances, so 'closest
candidate' should be replaced by a diagnostic comparison with its named
objective. The summary's universal exclusion of001..007 and every A2
refit from every registered ball overstates the dyadic coverage: the
published dyadic scheme exclusions are for state131,d2,007 only.
Use the separately audited scalar/graded and dyadic scopes.

Dependencies: the frozen publication; T4-065; T4-185/196; T4-195/199/212;
T4-203/208; T4-209; Plancherel, integration by parts, Hilbert-space
adjoints, finite-dimensional linear algebra and elementary asymptotics.
No claim about the unknown full inverse or global nonexistence is made.
