# Frozen source Holder inverse with a nonunit transverse rate

## Exact statement and relation to the trial

Let A>mu>0 and g>0. Put

    a=g/(A-mu), b=(A-mu)/A, q=(1+g)/A,
    r(sigma)=b sigma+1/A,

and assume

    1<a mu<A+1.                                         (1)

On L2(R2), define

    L=A x partial_x+mu y partial_y-1-gM,
    Mhat(xi,eta)=xi^2/(xi^2+eta^2).

The value of the multiplier at frequency0 is irrelevant. The domain is the maximal distributional domain of A x partial_x+mu y partial_y in L2. Let R=L^(-1) on this domain.

Fix a compact input support K and a smooth inhomogeneous dyadic decomposition defining C_*^sigma=B_(infinity,infinity)^sigma. Then R exists and

    ||R||_(L2->L2)<=1/(1+(A+mu)/2).                       (2)

For compactly supported f with support in K:

(a) If 0<sigma<1/mu, then ||Rf||_(C_*^sigma)<=C||f||_(C_*^sigma).
(b) If 1/mu<sigma<a, then ||Rf||_(C_*^r(sigma))<=C||f||_(C_*^sigma).
(c) If sigma>a, then ||Rf||_(C_*^q)<=C||f||_(C_*^sigma).
(d) At sigma=1/mu the high block is bounded by C lambda^(-1/mu)(1+log lambda); at sigma=a it is bounded by C lambda^(-q)(1+log lambda).

The constants are finite and depend on A,mu,g,K,sigma and the fixed decomposition. They are not numerical inverse certificates. This topic proves only these upper bounds. It does not claim sharpness of(b)-(d) for general mu; the lower arguments in proof 11 were proved at mu=1.

For 0<alpha<min(1,1/mu), C_*^alpha is equivalent to the bounded classical Holder space C^alpha. Thus(a) is a same-order Holder inverse. The exact modal source certified in proof 15 has

    10<A<51/5, 29<g<30,
    99999997745/10^11 < mu < 99999997750/10^11 <1.         (3)

These bounds imply 3<a mu<10/3<A+1. Hence every 0<alpha<1 is covered for the actual modal source. This discharges the nonunit-rate issue in applying the low-order source theorem. It does not replace the modal trial by raw X3, impose exact stationarity at its source, or invert the variable-coefficient/global normalized IPM operator.

## Domain and explicit semigroup

Let B=diag(A,mu), D_t f(X)=f(exp(Bt)X). Direct Fourier transport gives

    (S_t f)hat(zeta)=exp((a mu-1-A-mu)t)|zeta|^(-a)
       |exp(-Bt)zeta|^a fhat(exp(-Bt)zeta).              (4)

Equivalently,

    S_t=exp(-t)D_t Q_t,
    Q_t(xi,eta)=[(xi^2+eta^2)/(exp(2(A-mu)t)xi^2+eta^2)]^(a/2).

This bounded-multiplier definition avoids separating singular fractional operators at frequency0. The multiplier lies between0 and1, so

    ||S_t||_(L2->L2)<=exp(-(1+(A+mu)/2)t).               (5)

The multiplier ratio telescopes under dilation, proving the semigroup law. Strong continuity follows from dominated convergence and that of D_t. At t=0, the multiplier derivative is -gM; the derivative is uniformly bounded for t>=0 by g. Hence on the transport domain the derivative of S_t at0 equals L.

For completeness, the transport domain and a core can be seen on each physical quadrant. The unitary logarithmic change

    H(u,v)=exp((u+v)/2)h(plus-or-minus exp(u),plus-or-minus exp(v))

conjugates the transport to A partial_u+mu partial_v-(A+mu)/2. Its maximal domain is the L2 domain of this constant directional derivative. Cutoff and convolution approximate both H and its directional derivative, so smooth compact functions in(u,v) form a graph core. Taking the four quadrants gives the original maximal domain. The bounded multiplier -gM does not change it. Thus(4) is the semigroup of precisely the stated closed realization.

The integral Rf=-integral_0^infinity S_t f dt converges in L2 by(5). The closed-generator fundamental theorem gives LR=I and RL=I on the domain: the boundary S_T f tends to0 in L2, and differentiation of S_t on the domain justifies the other identity. This proves(2). Reflections and real-valuedness are preserved.

## Compact-support mixed norm and annular propagation

Write Delta_N for a homogeneous block at dyadic frequency N. For N>=1, compact input support gives

    ||Delta_N f||_infinity+||Delta_N f||_(L_x^1 L_y^infinity)
       <=C_K N^(-sigma)||f||_(C_*^sigma).                (6)

On a fixed enlargement of the x-projection of K use the usual block bound and finite interval length. Outside it, the Schwartz convolution kernel and compact input support give C_M N^(-M)(1+distance(x,K))^(-M)||f||_infinity; choose M sufficiently large and integrate. Applying |D|^a to an annular block costs C N^a in both norms, by its localized L1 kernel.

The kernel of Delta_lambda |D|^(-a) has L1 norm C lambda^(-a), and

    integral sup_x |K_lambda(x,y)|dy <= C lambda^(1-a),

by scaling a fixed Schwartz kernel. The dilation preserves the supremum norm and multiplies the mixed norm in(6) by exp(-At). From(4), viewed only on an annulus, one obtains

    ||Delta_lambda S_t Delta_N f||_infinity
      <=C exp((a mu-1)t)(N/lambda)^a N^(-sigma)
            min(1,lambda exp(-At))||f||_(C_*^sigma).     (7)

The support relation zeta=exp(Bt)eta restricts the time to

    log(lambda/N)/A <= t <= log(lambda/N)/mu,

up to fixed additive constants depending only on the chosen annular supports. There is no contribution for N larger than a fixed multiple of lambda.

Using only the first branch in(7), integrating to the upper endpoint gives a factor C(N/lambda)^(1/mu), since a mu-1>0. Alternatively split the time integral at t=log(lambda)/A. Before that time the exponent a mu-1 is positive; after it the exponent a mu-1-A is negative by(1). Both integrals are bounded by C N^a lambda^(-q), because

    q=a-(a mu-1)/A=(1+g)/A.

Consequently,

    ||Delta_lambda R Delta_N f||_infinity
      <=C N^(-sigma) min((N/lambda)^(1/mu),N^a/lambda^q)
                               ||f||_(C_*^sigma).       (8)

All shifts caused by annular overlaps are bounded constants and are absorbed in C. The two powers in(8) cross at N=lambda^b, because

    b(a-1/mu)=q-1/mu.

## Low input frequencies and the zero-frequency issue

For N<=1 use |fhat|<=||f||_1. The part of the input annulus mapped into the output annulus has x-width at most C lambda exp(-At) and y-width at most CN, hence area at most C N lambda exp(-At). Changing Fourier variables in(4) therefore gives

    ||Delta_lambda S_t Delta_N f||_infinity
      <=C||f||_1 lambda^(1-a)N^(a+1) exp((a mu-1-A)t).

Its time integral begins no earlier than log(lambda/N)/A, up to a fixed shift. Since the exponent is negative,

    ||Delta_lambda R Delta_N f||_infinity
      <=C||f||_1 lambda^(-q)N^(q+2).                    (9)

The dyadic sum over N<=1 converges because q>0. Splitting the inhomogeneous low block in this way is legitimate in L2; (9) gives absolute convergence after projecting to a high output annulus. Thus the argument never applies a singular multiplier separately to an uncontrolled zero mode.

The low output block is bounded in L-infinity by its L2 convolution kernel times ||Rf||_2. Compact support bounds ||f||_2 by |K|^(1/2)||f||_infinity, so(2) supplies the required low-output estimate.

## Geometric sums and Holder interpretation

For lambda>=2, (8)-(9) give

    C||f||_(C_*^sigma) [lambda^(-q)
      +lambda^(-q) sum_(1<=N<=lambda^b) N^(a-sigma)
      +lambda^(-1/mu) sum_(lambda^b<=N<=C lambda) N^(1/mu-sigma)].  (10)

The sums are over powers of two. By(1), a>1/mu. If sigma<1/mu, the last sum is bounded by C lambda^(1/mu-sigma). The first high sum is O(lambda^(-r(sigma))), with r(sigma)-sigma=(1-mu sigma)/A>0. Thus(10) is O(lambda^(-sigma)), proving(a). If 1/mu<sigma<a, both nonconstant sums are dominated by their crossover endpoint and give lambda^(-r(sigma)), proving(b). For sigma>a both give lambda^(-q), proving(c). At either endpoint a zero-power geometric sum counts O(1+log lambda) terms, proving(d).

For 0<alpha<1 the equivalence to the classical bounded Holder norm can be checked directly: cancellation of each high dyadic kernel gives ||Delta_N f||_infinity<=C N^(-alpha)[f]_alpha. Conversely split a difference at N comparable to |X-X'|^(-1), use the derivative bound C N ||Delta_N f|| below that scale and twice the block norm above it, and sum the two geometric series. This gives the classical alpha difference bound. The low block gives the supremum norm. Thus no integer-order interpretation is being hidden in(a).

Finally, substituting the rational box(3) verifies(1) without rounding. This proves the same-order low Holder result for the nonunit transverse rate actually certified at the modal source. The rank-one strain column, source matching, localization errors and global tail are outside the theorem.
