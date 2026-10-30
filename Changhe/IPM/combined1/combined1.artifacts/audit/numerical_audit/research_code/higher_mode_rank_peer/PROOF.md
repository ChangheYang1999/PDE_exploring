# Dimension of the proposed higher-mode radius25 extension

## Exact statement and scope

Fix c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma,
p_j=(3+gamma-j delta)/2, S=1+x^2+y^2, r=sqrt(x^2+y^2),
t=r^2/S, v=1/S and H_m=Re(x+iy)^(2m). Let V_old be the
1922-dimensional potential space with the selected basis in
../optimizer_quotient_audit/source/N1_013_quot_exact.json. Its basis
independence is an accepted dependency. Define the 41-element block set

 B = ({1} x {9,...,19}) union ({2,3} x {9,...,23}).

For each (j,m) in B and N in {0,...,11}, add

 G_jmN=H_m S^(p_j-m) [625/(625+r^2)]^4
                        P_N(2r^2/(625+r^2)-1),

where P_N is the Legendre polynomial normalized by P_N(1)=1. The listed
2414 potential functions are linearly independent. The map
D chi=-partial_y Delta chi is injective on their span V. Consequently
both V and D(V) have dimension2414. These are abstract spaces until an
immutable candidate's complete shape list has been checked against them.
The additional240 functions beyond the accepted candidate016 basis
have density frequencies contained in {31,33,...,47}; frequency31
actually occurs. No conditioning, optimizer minimum or existence follows.

## Potential independence

Angular orthogonality separates the cosine frequencies 2m. A relation
at a fixed m is a finite sum of v^(-p_j) Q_j(v), with Q_j rational
and analytic near v=0. Exact rational calculation gives p_j nonintegral
and p_j-p_k nonintegral for distinct j,k in {0,...,7}. A nonzero Q_j
has a finite integer order e_j at zero. Its first power e_j-p_j is
distinct from every other branch's first power. Divide a proposed
relation by its unique smallest power and let v decrease to zero along
positive values. Its nonzero leading coefficient cannot vanish.
Therefore all Q_j must vanish and each (j,m) block separates.

Put a=624, L(v)=1+a v and v0=-1/a. The new radial factor in a separated
block is

 A_mN(v)=625^4 v^4 (1-v)^m P_N(2(1-v)/L(v)-1)/L(v)^4.

Rodrigues' formula gives leading Legendre coefficient
2^(-N) binom(2N,N). Thus A_mN has pole order4+N at v0, with nonzero
Laurent coefficient

 C_mN=625^4 v0^4 binom(2N,N)(1-v0)^(m+N)/a^(4+N).

Every old radial polynomial is analytic there. In a nontrivial relation
choose the greatest N with a nonzero new coefficient. Its highest pole
cannot be canceled by lower N or old polynomials, a contradiction.
Descending in N removes all new terms; accepted old basis independence
removes the remainder. All41 blocks contribute12 independent functions,
so the dimension is1922+41*12=2414. Negative v0 is used only for a
rational identity, with no continuation of a noninteger physical power.

## Injectivity of the density map

All listed functions are smooth and even separately in x and y. Their
convergent large-r expansions, and their derivatives through order4,
give |D^k chi|=O(r^(3+gamma-k)) for0<=k<=4. The scaled terms have an
additional factor r^-8. In particular d=3+gamma<4 and D^4 chi tends
to zero. Assume D chi=0. Then Delta chi=f(x). For fixed x, sending
|y| to infinity in f''(x)=partial_xx Delta chi(x,y) gives f''=0.
Evenness forces f=K constant. Thus h=chi-Kr^2/4 is entire harmonic,
separately even, and grows as O(1+r^d). The interior harmonic derivative
estimate on a radius-L disk about any fixed point yields
|D^4 h|<=C L^-4 sup|h|=O(L^(d-4)). Letting L tend to infinity proves
D^4 h=0. Consequently h is a polynomial of degree at most3; separate
evenness and harmonicity give h=A+B(x^2-y^2).

Hence chi=A+B(x^2-y^2)+Kr^2/4. At each angular frequency its right
side is an integer Laurent polynomial in v, whereas the left side has
the separated fractional branches above. Their exponent classes are
noninteger and distinct from each other and from the integer class.
The same unique-lowest-exponent argument forces both sides to vanish.
Thus chi=0, proving injectivity. This is the same harmonic argument
independently reviewed by Opus in ../scaled_density_injectivity/PROOF.md;
the present proof checks its hypotheses for the enlarged finite set.

## Frequencies and the new endpoint

The Laplacian preserves cos(2m theta); -partial_y produces only
sin((2m-1)theta) and sin((2m+1)theta). The240 newly appended functions
have m in {16,...,23}, so the asserted containment follows. For j=1,
m=16,N=0, the envelope at zero is

 S^(p_1-16)[625/(625+r^2)]^4
   =1+(p_1-16-4/625)r^2+O(r^4).

Since Delta H_16=0, Delta(r^2 H_16)=4*33 H_16 and
-partial_y H_16=32 Im(x+iy)^31, the leading density coefficient is
4*33*32*(p_1-16-4/625), which is nonzero. This establishes the lower
endpoint as an actual mode of the extension; containment alone does
not claim every listed frequency is present in any fitted candidate.

## Finite verification and provenance

Construct the exact proposed shape list from the frozen candidate016
basis and the published launch's existing-block rule. Check that its
available blocks in the requested range are exactly j=1,m=16..19 and
j=2,3,m=16..23, yielding240 new tuples and2414 distinct total tuples.
Compare with the closed-form41-block list plus the old quotient basis.
Bind the accepted old rank, single-scale rank and Opus-reviewed density
injectivity records with all their inputs. For m=9,...,23 and N=0,...,11,
independently evaluate the rational numerator at v0 and compare all180
Laurent coefficients with the formula above. Check all36 nonintegrality
conditions, growth exponents and the density31 coefficient exactly.
The finite checker validates these explicit numerical hypotheses; the
analytic proof above is also needed. The new theorem remains OPEN for
independent review. A future actual candidate needs a separate hash-bound
shape and history comparison. Only own code is executed, without GPU,
JavaScript, servers, cluster access or a formal build.

## Independent acceptance of the preceding theorem

The OPEN review status at the end of the original calculation above is
superseded here by independent T4-369. The candidate-shape qualification
is retained: no actual022 coefficients are bound by this acceptance.
T4 independently constructs U_N(v)=(1+624v)^N P_N((1-626v)/(1+624v))
using the Legendre three-term recurrence

 (N+1) U_(N+1)=(2N+1)(1-626v)U_N-N(1+624v)^2 U_(N-1).

Multiplying by625^4 v^4(1-v)^m gives the numerator of A_mN at its stated
pole order4+N. At v0=-1/624, division of this numerator by624^(4+N)
is exactly the Laurent coefficient in the formula above. The recurrence
proves the full numerator construction; evaluating only a claimed
leading coefficient without that identity would not suffice.

The T4 proof independently repeats angular and fractional-branch
separation, descending pole orders and the full harmonic injectivity
argument. It checks all180 witnesses, with84 previous radius25 values
as calibration, the full2414 shape list,36 nonintegrality conditions,
growth exponents, launch rule and the actual frequency31 coefficient.
Our first path constructs each rational radial generator directly using
the accepted scaled-field backend. Both complete proofs and all finite
inputs are necessary dependencies of this acceptance.

The acceptance checker freezes or retains every T4 manifest, code,
proof, result and invoked input by SHA256, and compares every finite
claim with our own independently computed record. It recomputes the
closed-form coefficients, growth, branch conditions, shapes and endpoint
in exact arithmetic. The peer code is read as text and is not executed.
All source/raw hashes are bound; the prior Opus-reviewed injectivity and
accepted old-basis independence retain their stated scopes. Exact rank
provides no condition number or residual minimum. No formal source or
Lean build is claimed; verification/ contains finite exact evidence.
