# Fixed logarithmic deficits for delta=2/Q and finite leading profiles

Status: CONFIRMED after the independent theory-part review dated2026-10-31T05:25Z and verifier recheck. This extends the mechanism of topic63 to all integers Q>=3 and arbitrary finite S1 leading polynomials. It does not prove convergence of the complete rational logarithmic expansion.

## Statement and notation

Fix an integer Q>=3, put delta=2/Q and c=Q/(Q-2), and let f_1 be a nonzero real finite sum of odd sine modes. Generate the canonical polynomial-log density and stream coefficients F_n(t,theta), G_n(t,theta), with each resonant stream constant equal to zero. Set t=log r. The first possible stream resonance is n=2Q, and later ones occur at n=Qk, k>=2, with resonant angular frequency m_k=2k-2.

There is an explicitly computable real constant Lambda=Lambda(Q,f_1), defined by the finite linear cycle below, such that for every fixed integer d>=0, q=k-1-d,

    limsup_(k->infinity) (q! ||[t^q]F_(Qk+r)||_A0)^(1/k)
        <=(d+1)|Lambda|,                  1<=r<=Q,       (1)
    limsup_(k->infinity) (q! ||[t^q]G_(Qk+r)||_A0)^(1/k)
        <=(d+1)|Lambda|,                  0<=r<Q.        (2)

Only k large enough that q>=0 is used. The inequalities also apply when Lambda=0. For fixed d, each extracted subseries in independent complex variables z,t,

    sum_k z^(Qk+r)t^(k-1-d)[t^(k-1-d)]F_(Qk+r),

and its stream counterpart is entire in z,t and converges on every bounded complex angular strip, together with every fixed derivative. No uniformity in d is claimed.

For Q=3 and f_1=sin(theta), Lambda=157/129600, recovering topic63. The finite algorithm shows Lambda is homogeneous of degree Q in f_1; scaling f_1 by a real epsilon scales Lambda by epsilon^Q. The bounds therefore respect amplitude homogeneity.

## 1. Log degree and the unique unknown in each block

The degree theorem in topic17 specializes to

    deg F_n<=max(0,floor((n-1)/Q)-1),
    deg G_n<=max(0,floor(n/Q)-1).                         (3)

This specialization holds whether 2/Q is reduced or not. For odd Q its reduced numerator is2; for even Q it is1, and the resonance period computed in topic17 is still Q. In both cases the exceptional first period has no angular stream resonance, so the degree subtraction is1.

For a density coefficient at n=Qk+r,1<=r<=Q, define deficit d to mean degree k-1-d. Use the same convention for stream indices n=Qk+r,0<=r<Q. If both children in a quadratic interaction have indices greater than Q, their allowed log degrees sum to at most k-2. Consequently an interaction reaching target deficit d uses child deficits a,b with

    a+b+ell=d-1 or d-2,                                 (4)

where ell is the number of radial-log derivatives in the product, either0 or1. In particular both child deficits are strictly smaller than d.

If a child index is at most Q, its log degree is zero. An unknown coefficient of deficit d can then occur only in the current block or in its initial G_(Qk). Earlier blocks contribute only at smaller deficit. At n=Qk, the density's maximum degree is k-2, whereas the stream's is k-1. Its nonresonant stream coefficients at degree k-1-d are therefore determined from density and stream data of lower deficit. Modulo known lower deficits, exactly one scalar remains:

    a_(k,d) sin(m_k theta),
    a_(k,d)=[sin(m_k theta)][t^(k-1-d)]G_(Qk).

Every partial_t term at the same target degree uses a higher log column and hence a smaller deficit. Dropping those known terms leaves a finite linear cycle through the Q density orders of the block. No unknown coefficient from an earlier block remains.

## 2. The exact finite cycle

The low profiles f_j=F_j and g_j=G_j for1<=j<=Q are independent of t, finite sine polynomials, and already fixed by the leading profile. Define a linear perturbation H_r(k,theta), J_r(k,theta) as follows. Start with

    J_0=sin(m_k theta).

For r=1,...,Q use the ordinary, log-free linearized stationary expression

    H_r = 1/[(Qk+r-1)(c-1)] times
      {sum_(i=0)^(r-1) [P_(Qk+i) J_i f_(r-i)'
                           -p_(r-i) J_i' f_(r-i)]
       +sum_(i=1)^(r-1) [P_i g_i H_(r-i)'
                           -p_(Qk+r-i) g_i' H_(r-i)]}.    (5)

For r<Q, set J_r to the ordinary Poisson inverse of H_r at index Qk+r. These indices are not resonant. The required stream solution at the end is resonant, with frequency m_(k+1)=2k. Let K(k) be the sine amplitude of H_Q at frequency2k-1. The resonant Poisson forcing is exactly -2k K(k). Integration divides it by4k times the new positive log degree. Thus

    R(k)=-K(k)/(2k)                                      (6)

is the transfer from a degree k-1 resonant input at G_(Qk) to the degree k resonant output at G_(Q(k+1)). For a fixed deficit d it becomes

    a_(k+1,d)=k R(k) a_(k,d)/(k-d)+E_(k,d),               (7)

where E depends only on strictly smaller deficits. This identity holds once k>d and the finite initial exceptions are passed. The possible negative-frequency reflections are included in (5); for sufficiently large k every generated frequency m_k+s is positive, because the set of offsets s in this fixed Q-step cycle is finite.

Set A_(k,d)=(k-1-d)!a_(k,d). Then

    A_(k+1,d)=k R(k) A_(k,d)+S_(k,d).                    (8)

The homogeneous coefficient is independent of d.

## 3. Existence and computation of the limiting transfer

Every low profile is a finite polynomial. For all sufficiently large k, all coefficients in (5) are finite sums of rational functions of k with coefficients polynomial in the amplitudes of f_1. Each H_r and J_r uses only finitely many offsets from m_k. The number of offsets depends on Q and the leading bandwidth, not k.

We now prove that each coefficient of H_r and J_r has a finite limit as k tends to infinity. In (5), derivatives of high frequencies and the high radial exponents are O(k). The stationary denominator is asymptotic to2c k. Thus finite limits at earlier steps give finite limits for H_r. The ordinary Poisson multiplier on an input mode m_k+s produces

    -1/[2(m_k+s+1+P_(Qk+r))]
          =-1/[2(s+1-2r/Q)]                             (9)

at output offset s+1, and

    1/[2(m_k+s-1-P_(Qk+r))]=O(1/k)                     (10)

at offset s-1. For r<Q, the denominator in (9) cannot vanish: s is odd, s+1 is even, and0<2r/Q<2. Equations(9)-(10) prove the claimed limits inductively. Consequently

    Lambda=lim_(k->infinity)kR(k)=-lim K(k)/2             (11)

exists and is finite.

Here is a finite exact algorithm for Lambda, avoiding any limiting calculation. Represent high density and stream profiles by offsets s from m_k. Start with the stream offset0 of amplitude1. At a high-stream/low-density interaction with stream offset s of amplitude b, low frequency ell of amplitude a, and low exponent p_j, contribute

    offset s+ell:  -ba(ell+p_j)/(2c),
    offset s-ell:   ba(p_j-ell)/(2c).                    (12)

At a low-stream/high-density interaction with low frequency ell of amplitude b, high density offset s of amplitude a, and low stream exponent P_i, contribute

    offset s+ell:   ba(P_i+ell)/(2c),
    offset s-ell:   ba(ell-P_i)/(2c).                    (13)

Sum these contributions in the same order-index pattern as (5). After each nonterminal step r<Q, send a density offset s to stream offset s+1 with multiplier -1/[2(s+1-2r/Q)], discarding the limiting-zero channel(10). After step Q, Lambda is minus one half the density amplitude at offset1. Every operation is finite. For rational leading coefficients, the result is rational.

Each term in the Q-step response contains total low-profile degree Q in the leading input: the profile at low order j is homogeneous of degree j, and each path has total low order Q. Therefore Lambda is homogeneous of degree Q.

## 4. Fixed-deficit induction

The remaining argument is given fully to specify the growth constants. At fixed d, all triangular density and Poisson inverses use only a bounded number of higher log columns. For n=Qk+r with bounded r and a nonresonant even m, the factor |m+P_n| is either at least2/Q or, at a resonant order, at least2 when it is nonzero. The other factor m-P_n is bounded below by a positive multiple of k. Hence all nonzero Poisson denominators have modulus at least C_Q k for sufficiently large k.

All frequencies in the full order-n coefficient are at most Bn for a fixed B depending on f_1. A derivative costs O(k). After factorial normalization, the descending Poisson equations

    (m^2-P_n^2)B_q=H_q+2P_n(q+1)B_(q+1)
                             +(q+1)(q+2)B_(q+2)

and the analogous stationary equation have coefficients bounded by fixed powers of k. Resonant integration has the same property. A fixed block and fixed deficit therefore use finitely many operators of polynomial norm in k. These operations preserve kth-root exponential rates.

For d=0, all nonhomogeneous terms disappear once the finite initial range is passed, by(4). Thus(8) and(11) give limsup |A_(k,0)|^(1/k)<=|Lambda|. This remains valid when Lambda=0: eventually |kR(k)| is smaller than any prescribed positive number. The finite block reconstruction yields(1)-(2) for d=0.

Suppose the conclusion holds for deficits a<d. For epsilon>0, the corresponding factorial norms are bounded by C_a beta_a^K, where beta_a=(a+1)(|Lambda|+epsilon) and K is the block index. For a quadratic term using deficits a,b, let its child degrees be u=K_i-1-a and v=K_j-1-b. Multiplying the product coefficient by(u+v)! gives the binomial factor binomial(u+v,u). Summing over all splits of the order, for fixed residues modulo Q, is bounded by a constant times

    (beta_a+beta_b)^(u+v).

The bounded shifts between u+v and k and all fixed radial-log or angular derivatives cost only a constant and a power of k. By(4), a+b<=d-1, so beta_a+beta_b<=(d+1)(|Lambda|+epsilon). Terms with a low-order child are linear in lower deficits and have no greater rate. The block inverses preserve this rate up to a polynomial. Therefore

    |S_(k,d)|<=C k^M [(d+1)(|Lambda|+epsilon)]^k.          (14)

For any rho>(d+1)|Lambda|, choose epsilon so the bracket is below rho and choose eta with |Lambda|<eta<rho. Eventually |kR(k)|<=eta. Variation of constants in(8) bounds A_(k,d) by a geometric convolution of eta^k with the right side of(14), which is O(rho^k). Letting rho decrease to(d+1)|Lambda| proves the scalar bound. The finite block reconstruction proves(1)-(2).

## 5. Entire subseries and scope

For fixed d and any rho>(d+1)|Lambda|, the coefficients in(1)-(2) are bounded by C rho^k/(k-1-d)!. The angular bandwidth grows only linearly with k. Hence on any bounded complex angular strip the norm costs at most another exponential in k, and the factorial denominator proves convergence for every finite z,t. Every fixed derivative inserts only a polynomial factor or removes finitely many powers, so the same argument applies.

The constants C, the exponent M and the starting order depend on d. This proof supplies no convergent sum over all deficits. It therefore does not decide convergence of the complete rational logarithmic series, at delta2/3, delta1/2, or any other member of this class. Rational parameters with reduced numerator greater than2 have a different degree grading; the strict deficit decrease(4) need not hold there. They are not covered.

Dependencies: the exact canonical recurrence and support bounds in topics01 and10, the rational degree bounds in topic17, and the fixed-deficit organization of topic63. The new steps are the Q-step finite cycle, its limiting map(12)-(13), and the proof that its homogeneous coefficient stays bounded after factorial normalization. The finite Cartesian checks and independent theory-part review have both passed; the theorem may be labeled PROVED with the stated fixed-deficit scope.


## Completed finite checks

Six exact test profiles cover Q=3,4,5,6, including a pure third harmonic and signed mixed data. The limiting offset algorithm gives157/129600 for the original Q=3 single-sine case,3557/10368000 for Q=3 with sin(theta)+(1/10)sin(3theta), -9137/8429568 for Q=4 with sin(theta), and3575370901/5451264000000 for Q=5 with sin(theta). Exact Cartesian cycles at k=16,32,64,128 approach these independently calculated limits. For every profile, six additional positive-log-degree cycles verify that multiplying the transferred amplitude by the new log degree removes all dependence on that degree. All36 identities pass. The original Q=3 transfer also matches the previously proved rational function at all four k values. Actual elapsed time2.2427478209137917 seconds. The separate independent review is retained in sources/lead_review_20261031T0525Z.md.

## Verification closure, 2026-10-31T05:29:25Z

The independent theory-part review is retained in sources/lead_review_20261031T0525Z.md. Its index and sign checks agree with the argument above and the independent exact computations. The stated theorem is CONFIRMED. No convergence of the complete rational logarithmic series is inferred.
