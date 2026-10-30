# Positive-pole moments with an unexpanded localization power

## Exact statement

Let b>-1 be rational, m>=0 an integer, and let a_1,...,a_s be distinct
positive rational numbers with positive integer powers d_1,...,d_s.
Let N(v) be a rational polynomial. The finite moment

    L=integral_0^1 v^b (1-v)^m N(v)/prod_i(1+a_i v)^d_i dv       (1)

exists absolutely. Its numerator, poles, powers and parameters are exact
inputs. The following finite formulas compute (1) with outward real-ball
arithmetic, retaining (1-v)^m as a scalar exponent even for large m.
No quadrature or spatial cutoff is involved.

Exact polynomial division and partial fractions give

    N(v)/prod_i(1+a_i v)^d_i
        =Q(v)+sum_(i,k=1..d_i) c_(i,k)/(1+a_i v)^k.             (2)

The implementation must replay (2) after multiplying by the complete
exact denominator. Then

    L=sum_j Q_j B(b+j+1,m+1)+sum_(i,k) c_(i,k) J_k(b,m,a_i),    (3)

where

    J_0=B(b+1,m+1),
    J_k=B(b+1,m+1) 2F1(k,b+1;b+m+2;-a), k>=1.                 (4)

The positive real parameters avoid every endpoint singularity beyond
the integrable v^b factor. A computed ball is accepted only after its
required relative accuracy, exact decomposition replay and independent
moment comparisons pass. The result is a scalar primitive; no candidate
residual, weak norm or existence statement follows from fixtures alone.

## Derivation of the direct formula

For k>=1 the Euler integral for the displayed Gauss hypergeometric
function is precisely

    B(b+1,m+1)^(-1) integral_0^1
                             v^b(1-v)^m(1+a v)^(-k)dv.

This follows by expanding (1+a v)^(-k) near a=0 and integrating each
monomial, and then continuing the equality along the positive real a
axis. Both sides are real analytic there because 1+a v stays positive;
the Euler integral gives the continuation without a branch ambiguity.
The identity at k=0 is the beta integral. The polynomial terms in (3)
are beta integrals by definition. Absolute integrability and the finite
number of terms justify the linear combination.

## A second recurrence in the pole power

For k>=2 differentiate

    f(v)=v^(b+1)(1-v)^(m+1)(1+a v)^(1-k).

The endpoints of f vanish since b+1>0 and m+1>0. Its derivative is
integrable, so its integral is zero. Dividing the derivative by
v^b(1-v)^m and using the denominator(1+a v)^k yields the numerator

    (b+1)+[a(b+2-k)-(b+m+2)]v-a(b+m+3-k)v^2.

Replace v by((1+a v)-1)/a and collect denominator powers. Multiplication
by a gives

    0=(k-1)(a+1)J_k
       +[a(b+2-k)+b+m+4-2k]J_(k-1)
       -(b+m+3-k)J_(k-2).

Thus J0 and the direct J1 determine every higher pole power by

    J_k=[(b+m+3-k)J_(k-2)
          -(a(b+2-k)+b+m+4-2k)J_(k-1)]/[(k-1)(a+1)].         (5)

No denominator in (5) is zero under the stated hypotheses. The recurrence
may be ill-conditioned at finite precision, so each moment used in a
certificate is compared with its direct value (4), and a containing
interval is never narrowed by assuming agreement. An accuracy failure
requires more precision or a different enclosing evaluation.

The polynomial beta moments have the separate recurrence

    B(b+j+2,m+1)=B(b+j+1,m+1)(b+j+1)/(b+m+j+2).               (6)

All ratios in (6) are positive. Direct gamma quotients give an independent
comparison when requested. These checks retain cancellation in the
finite rational expression rather than discarding small terms.

## Independent fixtures and source fidelity

At m=0, formula (1) reduces to the independently audited positive-pole
primitive in ../rational_pole_moments/PROOF.md. At small integer m the
polynomial(1-v)^m can be expanded exactly and passed to that older
primitive; the two containing results must overlap. Noninteger b,
large m, repeated and mixed positive poles, and numerator cancellation
must be included among the fixtures. Direct (4) is compared against
(5) for every tested pole power, including those used with m near1045
for the proposed n21,K522 probe.

With no poles, (3) becomes the previously audited finite Beta moments.
The exact finite decomposition is the existing independently audited
algorithm, read from the own lane and hash-bound. Its validity is not
restricted to the earlier radial scales10 and100. New a=624 represents
R=25, since R^2-1=624.

The proof was written and checked before implementation. Exact JSON
fixtures, source hashes, real times and outward result balls belong in
the adjacent verification directory. No external source code is executed
and no formal build is required. Candidate-level acceptance remains a
separate audit with complete fields, source identities and weak hypotheses.
