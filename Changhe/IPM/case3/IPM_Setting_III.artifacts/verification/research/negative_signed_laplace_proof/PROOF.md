# A real-integral proof of the negative-sign inner ODE obstruction

Result 228. Written and checked algebraically before the numerical tests. This is
an independent derivation prompted by the Laplace representation in the external
sec379 review. No code or numerical values from that review are used as proof.
The statement concerns an ordinary differential equation on z>0. It does not
exclude any full-plane IPM profile or establish an expansion for a PDE solution.

## Exact statement and notation

Fix 0<p<1 and lambda>0. Define d=1/(p+1), r=p-2d and theta=z d/dz. If a real
function h belongs to C^3((0,infinity)), extends to C^1 at zero, has h'(0)=0, and
satisfies

    (theta-p)(theta-r)(theta-p-2)h+2 lambda h''=0,     (1)
    h(z)=O(z^p) as z tends to infinity,

then h is identically zero. The derivative condition is precisely the additional
condition supplied by an even C^1 extension. No analyticity at zero is assumed.

We prove this by constructing two smooth real solutions E and O, with initial
jets (E(0),E'(0))=(1,0) and (O(0),O'(0))=(0,1), and proving that every C^1
solution is their linear combination. Their coefficients at the forbidden
power z^(p+2) are explicit and nonzero. The argument uses convergent real
integrals and Abel's identity, without a Meijer-G connection formula or a formal
asymptotic completeness theorem.

## A convergent real Gauss integral

For -1<a<1, a!=0, c>0, c-a>0 and a+1>0, set beta=1-a>0 and, for u>=0, define

    J_(a,c)(u)=1+C_(a,c) integral_0^1
                  t^(a-1)(1-t)^(c-a-1)[(1+ut)^beta-1]dt,
    C_(a,c)=Gamma(c)/[Gamma(a)Gamma(c-a)].             (2)

The bracket is O(t) at zero. Thus the integral converges for a>-1, including
negative a, and at t=1 convergence follows from c-a>0. Formula (2) is not an
ordinary Euler integral with a negative beta-integral parameter: the subtraction
is essential.

For |u|<1 the binomial series may be integrated term by term after this subtraction.
For every coefficient n>=1, a+n>0 and the ordinary beta integral gives

    coefficient of u^n = (-1)^n (a)_n (a-1)_n/[(c)_n n!].

Consequently J is the analytic continuation to u>=0 of
2F1(a,a-1;c;-u). For this proof that name is optional: the coefficient recurrence
shows directly that

    [delta(delta+c-1)+u(delta+a)(delta+a-1)]J=0,
    delta=u d/du.                                    (3)

The integral is real analytic on (-1,infinity), by differentiation under the
integral on compact subintervals. Since the left side of (3) is real analytic
there and vanishes for |u|<1, it vanishes everywhere in that interval. This proves
(3) without using a large-argument special-function expansion.

For j>=1 differentiation gives

    J^(j)(u)=C_(a,c) beta(beta-1)...(beta-j+1)
       integral_0^1 t^(a+j-1)(1-t)^(c-a-1)(1+ut)^(beta-j)dt.   (4)

In particular J'(u) has the sign of a. The coefficient Gamma(a) is negative for
-1<a<0 and positive for a>0; all other factors in (4) for j=1 are positive.
Every derivative exists at u=0 and has at most polynomial growth as u grows.
These facts will justify the Laplace integrals and all integrations by parts.

There is an elementary leading asymptotic:

    lim_(u->infinity) J_(a,c)(u)/u^(1-a)
       =Gamma(c)/[Gamma(a)Gamma(c-a+1)].               (5)

Indeed the bracket in (2), divided by u^beta, tends to t^beta. Its product with
t^(a-1) is t^0. When beta<=1 use (1+v)^beta-1<=v^beta. When beta>1 use
(1+v)^beta-1<=C_beta(v+v^beta), with u>=1; the resulting majorants have powers
t^a and t^0 at zero and are integrable. Dominated convergence leaves
int_0^1(1-t)^(c-a-1)dt=1/(c-a), proving (5). The same estimates give
|J(u)|<=C(1+u)^beta for all u>=0.

## Two smooth Laplace solutions

For epsilon=0 or 1, put

    a=(epsilon-p)/2, gamma=(epsilon-r)/2=a+d>0,
    c=epsilon+1/2, q=z^2/lambda,
    F_epsilon(q)=1/Gamma(gamma) integral_0^infinity
                   exp(-t)t^(gamma-1) J_(a,c)(tq)dt,
    H_epsilon(z)=z^epsilon F_epsilon(z^2/lambda).      (6)

All parameter conditions in (2) hold: for epsilon=0, -1/2<a<0 and c=1/2;
for epsilon=1, 0<a<1/2 and c=3/2. Also gamma=a+d>0 in both cases because
r=p-2/(p+1)<0 for 0<p<1. Bounds (4)-(5), together with the exponential weight,
allow differentiation of (6) any finite number of times on q>=0. For each
finite m, extend F to q<0 by its degree-m Taylor polynomial at zero. The
resulting function is C^m near zero, since its first m derivatives match there.
Composition with z^2/lambda and multiplication by z^epsilon therefore give C^m
functions through zero. Since m is arbitrary, E=H_0 extends smoothly and evenly
through z=0, and O=H_1 smoothly and oddly. Their
initial jets are E(0)=1,E'(0)=0,O(0)=0,O'(0)=1. These are statements of smoothness;
the associated Taylor series need not converge.

To verify (1), let delta=q d/dq. Integrate (3) against the gamma weight. For any
of the differentiated integrands G(tq), integration by parts gives

    integral_0^infinity exp(-t)t^gamma G(tq)dt
      =integral_0^infinity exp(-t)t^(gamma-1)(gamma+delta)G(tq)dt.

The boundary terms vanish: t^gamma G(tq) tends to zero at t=0 because gamma>0,
and the exponential dominates its polynomial growth at infinity. Hence

    [delta(delta+c-1)+q(delta+a)(delta+a-1)(delta+gamma)]F=0.   (7)

For H=z^epsilon F(q), theta H=z^epsilon(epsilon+2delta)F. Since epsilon is 0 or 1,
substitution into (1), followed by multiplication by q/(8z^epsilon), gives
exactly (7). Therefore E and O are genuine solutions on every z>0.

Formula (5) and dominated convergence in the Laplace integral give

    H_epsilon(z)=A_epsilon z^(p+2)(1+o(1)),
    A_epsilon=Gamma(c)Gamma(1+d)lambda^(-(p+2-epsilon)/2)
               /[Gamma(a)Gamma(a+d)Gamma(c-a+1)].    (8)

Here gamma+(1-a)=1+d. Domination follows from
|J(tq)|/q^(1-a)<=C(1+t)^(1-a) for q>=1, which is integrable against the gamma
weight. For epsilon=0 every gamma factor is positive except Gamma(-p/2), so

    A_E=sqrt(pi)Gamma(1+d)lambda^(-(p+2)/2)
          /[Gamma(-p/2)Gamma(d-p/2)Gamma((p+3)/2)]<0. (9)

For epsilon=1 all gamma factors are positive, giving

    A_O=(sqrt(pi)/2)Gamma(1+d)lambda^(-(p+1)/2)
          /[Gamma((1-p)/2)Gamma(d+(1-p)/2)Gamma((p+4)/2)]>0. (10)

There is no exceptional parameter in the stated open interval. Also E'(z)<0
for z>0 by (4), and E tends to negative infinity by (9). It therefore has exactly
one positive zero. The ratio O(z)/z is positive and strictly increasing, because
J_(a,c)(0)=1 and its derivative is positive for the odd parameters. These are
additional statements about this ODE, not about the underlying PDE density.

## Every C^1 solution lies in this two-dimensional space

Expanding (1) gives the scalar equation

    h'''+P(z)h''+Q(z)h'+R(z)h=0,
    P(z)=(1-2p-r)/z+2lambda/z^3,
    Q(z)=(p^2+2pr+r-1)/z^2,
    R(z)=-pr(p+2)/z^3.                              (11)

For three solutions E,O,h, Abel's identity gives

    W(E,O,h)=C z^(2p+r-1) exp(lambda/z^2).           (12)

The 2 by 2 Wronskian W2=EO'-OE' tends to 1 at zero. Expanding the determinant
in (12) along h,h',h'' yields

    W2 h''+(OE''-EO'')h'+(E'O''-O'E'')h
       =C z^(2p+r-1) exp(lambda/z^2).               (13)

If h extends C^1 to zero, h and h' are bounded there. The other coefficients in
(13) are bounded, since E and O are smooth. If C!=0, then for all sufficiently
small positive z, h'' has a constant sign and magnitude bounded below by a
positive multiple of z^(2p+r-1) exp(lambda/z^2). The integral of this function
from z to any fixed positive point diverges as z tends to zero. This contradicts
boundedness of h'. Thus C=0.

On an interval where W2!=0, (13) is a regular second-order equation whose
fundamental pair is E,O. Hence h=A E+B O near zero. Uniqueness for the regular
third-order equation (11) at any positive point extends this identity to the
entire half-line. In particular B=h'(0)=0 under the even C^1 condition. If A!=0,
(9) gives a nonzero z^(p+2) term, contradicting h=O(z^p). This proves the theorem.

## Relation to the independently established corner solution

Let a0=-p/2, b0=(1-p)/2 and use the coefficients of result 224,

    C_E=Gamma(a0)Gamma(d+a0)Gamma(1/2)/Gamma(2-a0),
    C_O=Gamma(b0)Gamma(d+b0)Gamma(-1/2)/Gamma(2-b0).

They are negative. Equations (9)-(10) imply, by cancelling gamma factors and using
Gamma(-1/2)=-2Gamma(1/2),

    -A_E/A_O=(C_O/C_E)/sqrt(lambda).                (14)

Thus the linear combination with cancelled z^(p+2) growth has nonzero right
slope relative to its nonzero constant term, consistently with the independent
Barnes-contour construction. Equating it to that corner solution also uses the
already proved Frobenius matching statement of result 224; (14) alone is a
coefficient identity, not a distributional assertion at zero. An even reflection
with nonzero slope has a delta in its second derivative and is not a classical
or distributional solution of the displayed inner pair across zero.

## Verification plan, sources and scope

The implementation will evaluate (2),(6) through positive beta and gamma weights,
using separately coded value and derivative formulas; test (7) and (1); compare
several quadrature orders; compare the exact gamma coefficients and the
independent Barnes value at selected points; and verify the symbolic transformation,
Abel factor and coefficient ratio. Manufactured integrands with known beta/gamma
moments test the new quadrature before it is used. No producer inverse, special
function implementation, ODE integrator or saved numerical trajectory is imported.
The quadrature is not a rigorous error enclosure. The proof above is analytic.

The independent prior dependencies used only for the optional comparison are
../negative_signed_inner_layer/PROOF.md and ../sec379_text_audit/PROOF.md.
The real-integral proof of the theorem itself uses neither result. Standard
Gauss series, differentiation and differential-equation notation can be compared
with DLMF 15.5, 15.6 and 15.10, whose retrieved source bytes and hashes are frozen
under verification/sources. Initial direct .tex requests returned HTTP403; the
HTML section retrievals succeeded. Formula (2) is derived explicitly here so the
negative a case is not passed incorrectly to the usual Euler integral.

The derivation verifies only the fixed negative-sign leading inner boundary problem.
It assumes the sign lambda>0, 0<p<1, the prescribed matching growth and the C^1
axis condition. It gives no contradiction on the complete Setting III class.
