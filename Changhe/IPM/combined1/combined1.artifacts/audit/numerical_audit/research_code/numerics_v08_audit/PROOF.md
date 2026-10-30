# Scope audit of numerical publicationv08

## Optimization statements and complete counterexample

Let V be a finite-dimensional coefficient space contained in a larger
space W. Let J be a nonnegative residual objective defined on W. From
computed trial points v in V and w in W with J(w)<J(v), no positive
lower bound on inf_V J follows. This remains true if V has an exact
independent basis and W adds independent directions. Every trial gives
an upper bound on the minimum; comparing two such upper bounds does not
reverse that inequality. A finite number of positive damped residuals
likewise does not bound the undamped optimum from below.

For an exact counterexample take V={(x,0):x in R}, W=R^2 and
J(x,y)=(1-x-y)^2+y^2. The old residual column(1,0) and added column(1,1)
are independent. J(0,0)=1 and J(0,1/2)=1/2, a strict improvement using
only the added coordinate. Nevertheless J(1,0)=0, so inf_V J=0.
All these values and the determinant are checked as exact rationals.
This refutes the general inference from the observed trial improvement
to a positive old-space minimum. It neither computes nor refutes the
actual IPM minimum. The actual old-space floor remains OPEN.

Coordinate changes and Levenberg damping can change the computed trial
without changing the exact function space. Removing exact zero-potential
directions, adding different generators or observing a better candidate
can guide design, but does not establish an exact least-squares minimum,
stationarity, a physical coercivity bound or a uniform family distance.
A small coordinate-scaled singular value of a sampled matrix describes
that matrix in that metric. It is not the dimension of the function
space or a proved density dependency. Binary64 loss of positivity of a
large Gram matrix is a numerical conditioning diagnostic.

## Finite probe maxima and spatial interpretations

If a finite sampled set S of nonnegative integers has largest reported
value m, it only supplies max_(K in S) d_K=m at the stated numerical
precision. An omitted integer can in general have a larger value; for
example d_K=0 on S and d_(Kstar)=1 for Kstar outside S. To extend the
claim to all K requires a complete bound on every remaining index.
N4-230 provides a uniform upper bound0.00363271754961139 for all
K>=3000000 for007's full first-mode test, and six smaller ceilings at
larger cutoffs. It does not prove the asserted0.000173 global maximum
at12288 below that cutoff. That maximum remains OPEN.

For this specific residual the positive-beta majorant of N4-230 tends
to zero: each term is a constant times(2K+3)B(beta,K+2), beta>4/3,
which is asymptotic to2Gamma(beta)K^(1-beta). The finite sum therefore
tends to zero. Thus absence of a positive limiting test value is a
statement about this first-mode test family as K tends to infinity.
It is not a statement that exact profiles have zero correction distance,
and is not supplied by the finite far-field model alone.

## Signed pairing and model magnitude

N1 far_weak.py stores I_far=abs(sum terms). The table inv08 labels it
an exact-sector sum and compares it with signed full residual pairings.
The signs in that table cannot be interpreted as agreement of signed
pairings. The independently accepted N4-221 full and truncated model
pairings are both negative atK100000 and1000000 and positive at3162278.
The checker binds these exact containing intervals and the actualN1
magnitude field. It verifies their sign and a stated floating conversion
tolerance for the magnitude, without executing N1 code.

N4-221 already compares the whole-plane signed pairings with the exact
finite model at19listed K, including1e6 and3162278. The actual relative
model errors at1e5 and1e6 are about0.0276054 and0.000399286. The v08
mesh comparison at1e6 is a different0.2percent observation and should
not replace that exact comparison. These finitely many model errors
are neither a uniform remainder bound nor a convergence radius. The
last retained term fails to bound the actual error at all15large K
in the accepted audit. The table's30 nonzero first-sine sectors are a
finite model, not the full residual.

## Angular support, probe provenance and scope

The exact unit generator witness and complete calculation of N4-248
show that the added m9 block produces mode17 as well as19. Thus the
complete new density support is contained in17,19,...,31, with17
actually present. This correction does not put the separately registered
n>=19tests into the objective whose weak-test modes are at most17.
N4-243 records the complete objective history and finite25test register.
The19,1800probe belongs to the N4-229 extension; it is not one of the
original N4-160grid offsets. Neither sample separation nor registration
establishes statistical independence or a decrease of the exact distance.

The artifact freezes the publication and current N1 final/status wording
before proposing a new version. Existing immutable publications remain
untouched. Finite numerical claims not explicitly re-evaluated here stay
FLOAT. The checker uses accepted exact records and an exact logical
counterexample; no optimization or foreign code is executed. The proof
precedes the checker. Verdicts separate refuted inferences, exact report
corrections and unresolved actual maxima/minima.
