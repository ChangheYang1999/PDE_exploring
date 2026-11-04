# A velocity decay rate raises the sufficient strain threshold

Status: CONFIRMED in A520 after full independent reconstruction and postread of Theory Agent A C41. This is a conditional derivative-decay theorem, not a nonexistence theorem.

## 1. Exact statement

Let 0<c<1, omega be any finite real number, and let U in C2(R3;R3), P in C1(R3) satisfy

    div U=0, ((1-c)I+omega J)U+DU(Ay+U)+grad P=0,
    A=cI-omega J, J(y1,y2,y3)=(-y2,y1,0).

Set S=(DU+DU^T)/2 and lambda(y)=lambda_max(S(y)). Suppose, for finite C and some k>0,

    |U(y)|<=C(1+|y|)^(-k).

Put delta_*=min(1,(1+k)/2). If

    limsup_(|y|->infinity) lambda(y)<1+c delta_*,          (1)

then DU tends uniformly to zero and

    |DU(y)|+|curl U(y)|<=C_1/(1+|y|)                     (2)

for some finite profile-dependent C_1. Consequently the tail limsup of lambda belongs to {0} union [1+c delta_*,infinity]. A sufficient scalar form of (1) is

    limsup_(|y|->infinity)(|curl U|^2/2-Delta P)
                     <(3/2)(1+c delta_*)^2.             (3)

A separate envelope statement is valid. Suppose 1/2<delta_0<1, U=o(|y|^(1-2delta_0)) uniformly, and outside a ball

    lambda(y)<=1+c delta_0+epsilon(|y|),                 (4)

where epsilon is bounded, measurable, nonnegative and integral_R^infinity epsilon(r)dr/r is finite. Then the same conclusion (2) holds.

In particular, a prescribed bound U=O(1/r) gives the strict threshold1+c in (1). A prescribed natural bound U=O(r^(1-1/c)) is at least this strong when 0<c<=1/2. No such rate is derived from U->0 alone in this argument. The endpoint lambda<=1+c, corresponding to delta=1, is not covered by the A507 input used here.

## 2. Growth supplied by the strain bound

We recall the complete relevant content of A506. B=Ay+U has complete flow since U is bounded. On an exterior trajectory the radius r satisfies

    cr-M<=r'<=cr+M, M=sup|U|.

Each exterior point is reached from a fixed sufficiently large sphere, in elapsed time t satisfying ct=log(r/R)+O(1), with error uniform in the crossing point. This follows by integrating |(log r)'-c|<=M/r and using r'>=cr/2.

For W=curl U, exact vorticity transport gives

    d|W|/dt<=(lambda-1)|W|

where W is nonzero; uniqueness handles zeros. Thus lambda<=L outside a ball implies

    |W(y)|<=C(1+r)^((L-1)/c).

Because tr S=0, an upper bound lambda<=L also gives |S|<=2L. The skew part of DU has operator norm |W|/2. Hence

    |DU(y)|<=C(1+r)^delta,
    delta=max(0,(L-1)/c).                              (5)

If (4) holds, the extra orbit integral is at most (2/c) integral epsilon(r)dr/r, uniformly in the exterior point. The same argument gives

    |DU(y)|<=C(1+r)^(delta_0).                          (6)

These conclusions use no derivative decay or pressure estimate in advance. Their derivation is uniform over all directions; constants may depend on the fixed finite omega through the fixed profile.

## 3. Closing with the confirmed velocity-gradient tradeoff

Choose L strictly between the tail limsup in (1) and 1+c delta_*, with L>=0. Equation(5) gives a delta<delta_*.

If delta<=1/2, then U->0 and |DU|=O(sqrt r). The confirmed A498(B) applies for every 0<c<1 and finite omega, with no smallness requirement on the coefficient. It yields DU->0.

If delta>1/2, then

    1/2<delta<1, 2delta-1<k.

The velocity hypothesis implies

    |U(y)| r^(2delta-1)<=C r^(2delta-1-k)->0.

Therefore U=o(r^(1-2delta)), with exactly the exponent needed in A507. Its derivative hypothesis is (5), so A507 again gives DU->0. This strict exponent comparison is why the big-O velocity hypothesis is sufficient in (1).

For the envelope assertion, (6) supplies the derivative bound and its velocity hypothesis is already precisely U=o(r^(1-2delta_0)). A507 applies directly. All instances of A507 retain 1/2<delta<1, including its strict upper endpoint. After DU->0, global boundedness of U and DU holds by local continuity. A492 and A476 then give (2), and also Dini derivative decay.

## 4. Scalar form, gap, and boundaries

Taking divergence of full momentum gives

    |S|_F^2=|W|^2/2-Delta P.

For a real symmetric trace-free3x3 matrix with largest eigenvalue lambda>=0, the two remaining eigenvalues sum to -lambda. Their squares have sum at least lambda^2/2. Thus |S|_F^2>=3lambda^2/2 and

    lambda^2<=(2/3)(|W|^2/2-Delta P).

The strict scalar threshold (3) implies (1). If a finite positive tail limsup of lambda were below1+c delta_*, (1) would force DU->0 and therefore lambda->0, a contradiction. This proves the stated gap. Neither implication asserts endpoint sharpness or existence above the threshold.

Used results: A506 only for the independently recalled exterior growth estimate; A498(B) in the square-root case; A507 for the strict intermediate powers; A492/A476 for the final rate. There is no helicity, symmetry, smallness, finite-energy or pressure-gauge hypothesis. The fixed polynomial velocity decay is an explicit additional assumption.

## 5. Verification

The entire revised Theory Agent A in the team records was read, and Section3A was independently reconstructed above. The configured-model Theory Agent A source gives the same two exponent cases and explicitly preserves the velocity-rate hypothesis. Its older optional random computations and separate kinematic example are not used. No computation or formal build is needed for this corollary.
