# An origin restriction on contractive Sobolev energies

## 1. Statement and scope

Let c>0. Let rho be a smooth S1 reference, u its canonical IPM velocity, and V=cX+u. S1 means rho is even in x and odd in y. Assume V is globally Lipschitz and the coefficient derivatives needed for bounded multiplication on H^q are bounded, where q>2. Let

    Lh=V.Dh-h+U[h].Drho,
    U[h]=(-R1R2 h,R1^2 h),
    c+partial_y u2(0)=1.                                  (1)

The canonical strain is c[h]=partial_y U2[h](0). If, on all smooth compact S1 tests with c[h]=0,

    Re <Lh,h>Hq <= -beta ||h||Hq^2,                        (2)

then necessarily

    beta <= c+1-q.                                        (3)

In particular a strictly positive contractive energy gap in H^(2+s) requires s<c-1. Since the case4 c lies strictly between9/5 and37/20, the ordinary H^3 energy cannot have a positive gap: the limiting test energy is 2-c>3/20.

The same necessary condition holds for the dyadic density-velocity graph energy Y in T4-058, with q=2+s, assuming additionally the usual sublinear background decay |D^k rho|+|D^k u|<=C_k <r>^(gamma-k), gamma<1, for k through ceil(q)+2. These bounds ensure the graph quadratic form is finite on the tests. The graph's velocity component does not remove this origin obstruction.

This is a necessary condition for the displayed contractive energy estimate. It does not rule out an equivalent adapted norm, a semigroup bound with a transient prefactor, a stationary inverse, or a different high-space strategy. None of those stronger exclusions is claimed.

## 2. A vertical high-frequency test

Choose a nonzero real smooth amplitude a_epsilon, even in both coordinates, supported on four small disks centered at (plus or minus epsilon, plus or minus epsilon). The disks have radius less than epsilon/10, so the amplitude vanishes near the origin. Put

    h_N=N^(-q) a_epsilon(X) sin(Ny).

These are real compact S1 tests. We first keep epsilon fixed and let the positive integer N tend to infinity.

For a smooth compact amplitude a, Fourier translation and Taylor expansion of (1+|xi|^2)^(q/2) around the two frequencies (0,plus or minus N) give

    J^q(e^(iNy)a)
      =e^(iNy)(N^q a-iq N^(q-1)partial_y a)+O_(L2)(N^(q-2)). (4)

The same expansion holds for every fixed compact smooth coefficient times a. To justify the remainder for arbitrary q>2, split the translated Fourier integral into |eta|<=N/2 and its complement. On the first region the second symbol derivatives are bounded by a constant times N^(q-2), and the Taylor remainder is dominated by N^(q-2)|eta|^2. On the complement the Fourier transform of a has arbitrarily rapid decay. This proves (4); it also proves the analogous higher-order remainder estimates when needed.

The positive and negative frequency packets become orthogonal to every algebraic order because their Fourier centers separate. Thus real sine tests have the same energy ratio as the complex positive packet.

The vector multiplier of U vanishes at the vertical unit direction (0,1). Its first derivatives are bounded on a cone around that direction. Applying the same Fourier split gives

    ||U[h_N]||Hq=O(N^-1).                                 (5)

Bounded multiplication by Drho on H^q then makes the coupling term's contribution to the normalized energy tend to zero. Such bounded multiplication follows, for example, from bounded coefficient derivatives through order ceil(q)+1, using integer Leibniz estimates and the fractional difference-quotient formula. This is one explicit sufficient interpretation of the coefficient assumption in Section1.

## 3. Exact leading transport energy

For the positive packet,

    (V.D-1)(e^(iNy)a)=e^(iNy)(iN V_y a+V.Da-a).

Apply (4) to both factors of the H^q inner product. The leading imaginary term has zero real part. The cross term from differentiating a in the second factor cancels the V_y partial_y a term from differentiating V_y a in the first factor. What remains, after division by N^(2q), is

    integral (V.Da)a - integral a^2
        +q integral (partial_y V_y)a^2.

Since div V=2c, integration by parts gives integral(V.Da)a=-c integral a^2. Therefore

    lim_(N to infinity) Re<Lh_N,h_N>Hq/||h_N||Hq^2
       = -c-1 + q [integral(partial_y V_y)a_epsilon^2]
                         /[integral a_epsilon^2].          (6)

This calculation keeps the first subleading symbol term. Retaining only the leading N^q multiplier would miss the entire q partial_y V_y contribution.

## 4. Exact normalization and the origin limit

The canonical strain kernel away from zero is a constant multiple of sin(3theta)r^-3. Because a_epsilon vanishes on a neighborhood of zero, integration by parts in y shows

    c[h_N]=O(N^-M)

for every prescribed M, at fixed epsilon. The factor N^-q is harmless. Let g be a fixed smooth compact S1 function with c[g]=1, for example g=-4y eta(r), where eta is a smooth radial cutoff equal to one near zero. Set

    htilde_N=h_N-c[h_N]g.

It is exactly normalized. Its H^q norm differs from that of h_N by a quantity tending to zero. Also ||Lh_N||Hq=O(N) at fixed epsilon, while the correction is smaller than every power of N. Thus (6) remains valid for htilde_N. All origin jets of h_N itself vanish; the tiny correction enforces the nonlocal normalization rather than assuming vanishing jets imply zero strain.

By (1), partial_y V_y(0)=1. Let epsilon tend to zero in (6). Smoothness gives the limiting ratio q-c-1. Applying (2) to every htilde_N forces q-c-1<=-beta, proving (3).

## 5. The dyadic density-velocity graph energy

For epsilon small enough, the amplitudes lie where chi0=1 and all the annular density cutoffs of T4-058 vanish. Its density H^q contribution is therefore exactly the one used above. The weighted low term is O(N^-2q), so its energy contribution tends to zero relative to the H^q norm.

The local velocity contribution to the norm is O(N^-2) by (5). For the transported input Lh_N, the leading amplitude is N times a fixed compact amplitude, and applying U again gains N^-1 in the vertical cone. Thus ||U[Lh_N]||Hq=O(1), and its pairing with U[h_N] tends to zero. Multiplication by chi0 preserves these bounds.

Outside a fixed neighborhood of the input supports, the velocity kernel is smooth. Repeated integration by parts in y makes every derivative of the velocity O(N^-M), with the usual odd-source exterior decay. The transport part of Lh_N is compactly supported and has at most one extra factor N, so its exterior velocity has the same rapid-in-N bound. The remaining term Drho.U[h_N] has H^q norm O(N^-1) and exterior decay O(N^-M r^(gamma-4)) for each M. It has a finite first moment because gamma<1. Its velocity has an exterior r^-3 term with a coefficient bounded by a polynomial in N, and a faster-decaying remainder. This follows by subtracting the value of the velocity kernel at the origin of the source, using oddness, and splitting the source integral at half the observation radius. Pairing that polynomial bound with the arbitrarily rapid-in-N exterior bound for U[h_N] makes the exterior graph energy tend to zero. The r^-3 decay and a>0 make the dyadic sums convergent. The exact strain correction is negligible by the argument in Section4.

Hence the limiting graph-energy ratio is again q-c-1, proving the assertion for Y. This conclusion concerns that specific graph inner product; equivalence of norms alone would not transfer a contractive numerical-range bound.

## 6. Status

This is new T4 analytic work, CLAIMED pending independent Opus review. It is an origin audit for proposed high norms, not a numerical candidate rejection. There is no computation or fitted constant. The exact case4 c can be read from the canonical JSON inputs, but the strict interval9/5<c<37/20 already suffices for the stated H^3 conclusion.
