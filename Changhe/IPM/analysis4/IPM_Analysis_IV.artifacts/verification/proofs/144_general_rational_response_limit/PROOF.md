# A direct limiting-response operator for rational similarity exponents

Status: PROVED response-limit formula and first-resonance structure. Exact comparisons are recorded in V280; the theory part independently rederived the Cartesian carrier limit and accepted the argument at11:34Z, recorded in V299. This file does not assert convergence by itself.

## Statement and notation

Fix positive coprime integers h,Q with2h<Q, put delta=2h/Q, c=1/(1-delta), p_j=1-j delta and P_j=2-j delta. The leading profile is a finite S1 sine polynomial. Compute the pure nonresonant density coefficients F_1,...,F_Q and stream coefficients G_1,...,G_(Q-1) from the stationary recurrence. If h=1 these orders are all before the first positive stream resonance. If h>=2, orderQis the first resonance and only its density coefficient is used here. All these fields are finite sine polynomials. Their coefficients can be real or complex.

Use the real signed Laurent convention S_m=(z^m-z^(-m))/2. It represents sin(m theta) with its common factor i suppressed; the Cartesian operators below incorporate this convention. For a field z^m with radial degree a set

    X_a z^m = ((a+m) z^(m-1)+(a-m) z^(m+1))/2,
    Y_a z^m = ((a+m) z^(m-1)-(a-m) z^(m+1))/2.

The encoded advection is T(G,F)=XG YF-YG XF. Define finite Laurent polynomials

    A_j(z)=sum_m (p_j+m) F_(j,m) z^m,
    B_j(z)=sum_m (P_j+m) G_(j,m) z^m.

For a Laurent polynomial v with odd exponents and1<=s<Q define

    (L_s v)(z) = -sum_vindex v_(vindex) z^(vindex+1)
                            /[2(vindex+1-delta s)].       (1)

The denominator never vanishes: vindex+1is even, while delta s is an even integer only if Qdividess. Define finite Laurent polynomials u_r for1<=r<=Q recursively by

    u_r=(1-delta)[-A_r/2
             +sum_(s=1)^(r-1)(u_s B_(r-s)-(L_s u_s) A_(r-s))].  (2)

For a large integer k put n=kQ and q=2hk-2. At ordernadd a unit free harmonic sin(q theta) to the stream. Let phi_r^(k) be the linear density response at ordern+r, and let sigma_k be the sine coefficient at angular frequency2h(k+1)-3in phi_Q^(k). Then

    lim_(k->infinity) sigma_k = 2 [z^(2h-1)] u_Q.          (3)

The convergence is locally uniform in the finite leading-amplitude parameter space. The right side is a homogeneous degreeQpolynomial in the leading amplitudes, with rational coefficients when delta is rational.

## Resonance and affine response

An allowed stream mode has positive even frequency. Resonance at ordernmeans |P_n| is such a frequency. Since n>0and P_n<2, a resonance requires P_n=2-2hk with n=kQ. At h=1,k=1the frequency is zero and the sine mode is absent; the first resonance is2Q. At h>=2the first resonance isQwith frequency2h-2. The first pure compatibility condition is the vanishing of the coefficient of sin((2h-3)theta) in F_Q: at P_Q=-(2h-2), the resonant forcing coefficient is -(2h-2)times this coefficient. No higher density frequency contributes to that forcing because its coefficient is zero at resonance.

For any such nthe dependence of ordersn+1throughn+Qon the new harmonic is affine. A product of two factors depending on that harmonic has order at least2n+1>n+Qfor n>=Q. Differentiating the ordered bilinear recurrence therefore gives exactly

    lambda_(n+r) phi_r = T(e_k,F_r)
      +sum_(s=1)^(r-1)[T(G_(r-s),phi_s)+T(Pi_(n+s)phi_s,F_(r-s))],

where lambda_j=delta(j-1)/(1-delta), e_k=S_q, and Pi is the nonresonant stream inverse. This is a finite linear-response calculation and does not assume compatibility of the new full infinite series.

## Proof of the limiting operator

All frequency offsets generated through Qresponse steps are bounded independently of k, since the low fields have finite support. Separate the positive carrier z^qfrom the negative carrier z^(-q). For large kthese supports are disjoint. The positive part of e_kis z^q/2. The radial degrees of the high density and high stream at step s are respectively -q-1-delta s and -q-delta s. For a carrier coefficient z^(q+v), the exact Cartesian formulas show

    q^(-1)X(z^(q+v)) -> -z^(q+v+1),
    q^(-1)Y(z^(q+v)) ->  z^(q+v+1).

The low-field sum X+Y maps its mthcoefficient to(a+m)z^(m-1). Hence the leading advection with the high stream first is -q times its carrier amplitude multiplied by A_j. With the high density second it is +q times its carrier amplitude multiplied by B_j.

For the stream inverse applied at steps, the leading Xforcing at positive output offsetu=v+1is -q times the density carrier coefficient. Its denominator is

    (q+u)^2-(-q-delta s)^2 = 2q(u-delta s)+u^2-delta^2 s^2.

Since u-delta s is nonzero for1<=s<Q, the limiting inverse is exactly(1). Also lambda_(n+r)/q tends to1/(1-delta). Induction on rnow proves that every positive-carrier coefficient of phi_r tends to(2); the finite support lets limits pass through every convolution. Reflection symmetry determines the negative branch. The requested final sine frequency is q+2h-1, so its coefficient is twice the positive Laurent coefficient at offset2h-1, proving(3).

Every exact finite-kresponse coefficient is a rational function of kwhose coefficients are homogeneous polynomials of degree r in the leading amplitudes. The displayed nonzero leading denominators give locally uniform convergence coefficient by coefficient. Since the number of amplitudes, response steps and offsets is finite, the limit is locally uniform and has the stated polynomial degree.

## What remains open

At h>=2the first obstruction has degreeQ, the same upper degree as the limiting response. The degree-separation argument used for delta=2/Qdoes not apply. It is necessary to check whether the limiting response vanishes on the first compatibility variety. Furthermore, the earlier general-period majorant begins its free harmonics after orderQ; it cannot be reused without changing its initial split when h>=2. These are independent obstacles, not resolved by(3).

## Dependencies and evidence

Cartesian signs and the pure stream inverse are independently checked in01and119. The earlier exact Q3,Q4,Q5response limits are in119,142and130. The planned implementation computes(1)-(2) directly with rational Laurent polynomials and compares those old limits before applying the formula at4/9. No symbolic large-kexpansion from the theory part is imported.

## Explicit first resonance pairs

For h>=2, the first three positive even stream resonances are

| k | Order n | Stream frequency | Obstruction density frequency |
| --- | --- | --- | --- |
| 1 | Q | 2h-2 | 2h-3 |
| 2 | 2Q | 4h-2 | 4h-3 |
| 3 | 3Q | 6h-2 | 6h-3 |

The first compatibility condition is therefore the coefficient of sin((2h-3)theta) in f_Q. At delta=4/9 these pairs are (n,q)=(9,2),(18,6),(27,10), with obstruction frequencies 1,5,9. The free coefficient at order 9k changes the next obstruction at order 9(k+1), whose density frequency is 4k+1. At h=1 the k=1 frequency is zero and is not a positive sine mode; the first three positive stream resonances instead correspond to k=2,3,4, with pairs (2Q,2),(3Q,4),(4Q,6). This explains the different starting index in145.
