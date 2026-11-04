# Sparse and positive-density recurrence of the pressure source

Status: confirmed in A3084 with the qualified C comparison and refinements in A3085. The counterexample is kinematic and fails full Euler; the full-profile sparse-return question remains OPEN in A3086.

## 1. Exact statements

There is a smooth divergence-free U on R3, all of whose derivatives including order0 are bounded, such that q=tr((DU)^2) is nonzero, U is nonzero, and

    E(R)=integral_(B_R)|U|^2=O(R^d), d=log(3)/log(10)<1,
    integral_R3 |U|^2=infinity.

The field satisfies U(R.)->0 locally in L2 and hence in distributions, but does not decay uniformly. For every compact K, all sufficiently large integers k give

    U(y+10^k e3)=U(y), q(y+10^k e3)=q(y), y in K,

and equality of all their derivatives. No C1 pressure makes this U a full rotating profile for any finite c!=0 and finite omega.

Separately, let V be any C1 divergence-free field on R3 with E_V(R)=o(R). Fix a!=0 in R3 and a subset D of the positive integers with positive upper natural density. If q_V(.+n a)->q_V in distributions as n tends to infinity within D, then V=0. In particular any nonzero translation period of q_V forces zero. No pressure, velocity bound or Euler equation is assumed in this positive theorem.

Here all derivative squares are matrix products. Neither statement proves or refutes a full-profile theorem for arbitrary sparse returns under bounded Hb.

## 2. Exact center set

Let S be the integers with a finite balanced base-ten expansion

    m=sum_(j>=0) epsilon_j 10^j, epsilon_j in {-1,0,1}.

After omitting leading zeros the expansion is unique. At the largest differing position k the leading difference has magnitude at least10^k, and all lower differences have total magnitude at most2(10^k-1)/9<10^k. Distinct centers are consequently distinct integers and have separation at least1.

If k is a center's highest nonzero position, then

    |m|>=10^k-(10^k-1)/9=(8*10^k+1)/9.

Hence centers with |m|<=R have k<=floor(log_10(9R/8)) for R>=1. Counting three possibilities at every position gives

    #(S intersect [-R,R])<=3(9R/8)^d.

The harmless constant can be enlarged near R=0.

For every fixed finite M, and all sufficiently large k,

    m in S iff 10^k+m in S, for every integer |m|<=M.      (1)

For the forward direction, choose k larger than all possible leading positions of centers in [-M,M] and insert digit1 at position k. Conversely take M<10^k/4. An allowed expansion in [10^k-M,10^k+M] cannot end below position k, since all lower positions sum to at most(10^k-1)/9. It cannot end above k, by the leading-position lower bound. Its leading digit is positive1, because a negative leading digit dominates all lower positions and yields a negative integer. Removing that digit leaves precisely m with an allowed expansion. This proves exact local matching, not approximate recurrence.

## 3. Smooth field, energy and return

Choose0<delta<1/4 and eta in C_c^infinity(B_delta), equal to1 near0. Define

    psi=eta(y)(y1^2+y2^2)/2,
    W=(partial2 psi,-partial1 psi,0),
    U(y)=sum_(m in S) W(y-m e3).

The bumps have disjoint supports and the sum is locally finite. Thus U is smooth, divergence-free and each of its derivatives has the same uniform bound as the corresponding derivative of W. Smooth compact support makes all derivatives agree with zero across a support boundary. The quadratic source is the sum of translated sources, with no cross terms. Near each center,

    W=(y2,-y1,0), q_W=-2, curl W=-2e3.

In particular U and q are nonzero. Put e0=integral |W|^2>0. A bump meeting B_R has |m|<=R+delta, so the center count bounds E(R) by C(R+1)^d. Infinitely many disjoint bumps each carry energy e0, proving infinite total energy.

For fixed L, the scaling identity R^-3 E(LR)=||U(R.)||_(L2(B_L))^2 gives convergence to zero. On the other hand, choose a point y0 where W(y0)!=0; the values at y0+m e3 remain W(y0) for unbounded positive m in S. Thus uniform decay fails.

For a compact K contained in B_L, a contribution to U(y+10^k e3) can only have a center of the form10^k+m with |m|<=L+delta. Formula(1) matches those centers with the centers contributing to U(y). All translated arguments of W agree. This proves exact equality on K for sufficiently large k, with one threshold that works for every derivative. It also proves source equality. The return sequence has zero natural density since it has only O(log R) members up to R.

## 4. Failure of the full equation

Set A=cI-omega J, where J rotates the horizontal plane. The centers0 and1 belong to S. For y in B_delta, U(y)=U(y+e3)=W(y) and their derivatives agree. Suppose a C1 pressure P solved

    (1-c)U+[(Ay+U).grad]U+omega JU+grad P=0.

Subtracting its equations at y+e3 and y gives

    grad[P(y+e3)-P(y)]=-c partial3 W(y),

since A e3=c e3 and all other terms cancel. Distributional curl is legitimate for the C1 pressure difference, and yields c partial3 curl W=0 in B_delta.

The latter derivative cannot vanish identically. If it did, curl W would be constant along every connected vertical segment of B_delta. Compact support strictly inside B_delta makes it zero near each segment's endpoints. On the central segment this contradicts curl W(0)=-2e3. Therefore c!=0 is impossible for every finite omega, independently of any pressure normalization. No assertion about c=0 is needed.

## 5. Positive upper density forces zero

For C1 divergence-free V, local mollification gives q_V=partial_i partial_j(V_i V_j) in distributions. Fix a smooth compact scalar test phi supported in B_K and let

    I_n=<q_V(.+n a),phi>
       =integral V_i(y)V_j(y) partial_i partial_j phi(y-n a)dy.

A point y can lie in only a bounded number of the balls B_K+n a: projection onto a/|a| puts n in an interval of length2K/|a|. Thus the overlap bound is uniform in N. All first N balls lie in B_(N|a|+K), so

    sum_(n=1)^N |I_n|<=C_(phi,a) E_V(N|a|+K)=o(N).        (2)

Let I=<q_V,phi>. If I!=0, the stated distributional convergence gives |I_n|>=|I|/2 for all sufficiently large n in D. Positive upper density supplies a fixed epsilon>0 and an unbounded sequence N_j with #(D intersect[1,N_j])>=epsilon N_j. Removing the finitely many initial indices still leaves at least epsilon N_j/2. Consequently the left side of(2) is at least epsilon |I|N_j/4, a contradiction. Hence I=0 for every test and q_V=0 as a distribution.

To conclude V=0 without any Euler input, test this identity against f chi_R, where f=sqrt(1+|y|^2) and chi_R is a nonnegative cutoff equal to1 on B_R and zero outside B_(2R). The Hessian of f has eigenvalues f^-3 radially and f^-1 tangentially. Product differentiation gives

    0=integral chi_R V.D^2 f V+Err_R,
    |Err_R|<=C E_V(2R)/R ->0.

The error contains f D^2 chi_R and the two first-derivative products, all bounded by C/R on the annulus. For every fixed L the main integral is at least(1+L^2)^(-3/2)E_V(L) when R>=L. Thus E_V(L)=0, and continuity gives V=0. This proves the theorem without assuming an absolutely integrable uncut source moment. An exact nonzero translation period takes D to be every positive integer.

## 6. Source, comparison and limits

All seven LIT368 source sections, all twenty-five manual checks, its reading record and formal-source note were read. The center count, matching, full-equation failure and positive-density estimate have been reconstructed above. The proof uses no numerical sample or formal build. Existing configured model comparison is pending, with actual provider execution independently unattested.

The smooth sparse example proves that bounded derivatives, Hb and E=o(R) do not kinematically exclude arbitrary sparse source return. It does not contradict the uniform-decay return criterion A3044, because this example fails decay; it does not refute a full-profile Hb criterion because it fails momentum. Positive upper density is sufficient, and no optimal density threshold is claimed. The unrestricted rotating conjecture remains open.


## 7. Complete C comparison and quantitative refinements

The complete C comparison dated 2026-11-04T07:58:02Z was read, including
all eight analytical items. It agrees with Sections 1-6. Its numerical
samples, failed and revised scripts, execution records and diagnostic
counts are not independently certified. The following refinements are
checked analytically here.

First, the bounded-overlap argument proves, for every epsilon>0,

    #{1<=n<=N: |I_n|>=epsilon}
        <= C_(phi,a) E_V(N|a|+K)/epsilon.                (3)

If I=<q_V,phi> is nonzero and q_V(.+na) tends to q_V along D, then
|I_n|>=|I|/2 eventually on D. Thus the counting function of D is at most
2C E_V(N|a|+K)/|I| plus a fixed finite number. For a hypothetical nonzero
bounded-Hb target profile, A3053 gives the bound O(N^beta),
beta=5-2/c in(0,1). No positive-density assumption is needed for this
quantitative conclusion.

The fixed-test bound has the correct order for the constructed field.
Choose a nonnegative phi supported in the flat core of W, where q_W=-2,
with nonzero integral, so I is nonzero. For a=e3, disjoint supports and
integer centers give I_n=I if n belongs to S, and I_n=0 otherwise.
There are order N^d positive centers below N. Indeed, if10^k<=N<10^(k+1),
all allowed positive expansions with positions below k lie below N and
number(3^k-1)/2, whereas the earlier upper bound is O(N^d).
The same counting argument on fully contained bumps and on intersecting
bumps gives E(N) of order N^d. This attains (3) up to constants for this
one test. It does not assert full distributional convergence along every
positive center or a return set of that counting order.

Second, scalar azimuthal projection Pi_m about the vertical axis commutes
with translation by ne3. Its adjoint sends a test supported in B_K to a
smooth test in the same ball, with no increase in the supremum norm of
the Hessian: rotations conjugate the Hessian by orthogonal matrices, and
averaging with a phase of modulus one preserves the norm bound. Repeating
(2) for that projected test shows that positive-upper-density return of
Pi_m q_V forces Pi_m q_V=0. For m=0 this already forces V=0, because every
radial compact test pairs with q_V exactly as it pairs with Pi_0 q_V, and
the convex test at the end of Section 5 is radial. For m not equal to zero,
vanishing of that source mode alone does not force V=0. In a full C1/C1
profile with E=o(R^3), A3042 then also gives the vanishing pressure mode.
This argument uses vertical translations; it does not assume commutation
with general horizontal translations.

Third, C points out that the radial-cutoff version of the example fails
momentum also at c=0. A still simpler local calculation covers the example
for every allowed eta. On a neighborhood of the origin, eta=1 and no other
bump contributes, so U=-Jy. There y.grad U=U, (Jy).grad U=JU, and
(U.grad)U=-(y1,y2,0). Hence the full momentum terms except grad P are

    -Jy-(y1,y2,0),

independently of c and omega. Their curl is -2e3. They cannot be the
negative gradient of a C1 pressure even locally. Thus the original
construction in fact fails full momentum for every finite c and omega.
The weaker c!=0 statement and its subtraction proof remain correct.

These refinements do not turn the example into a full-profile counterexample
or settle sparse source return under bounded Hb for actual profiles. The
existing configured model collaboration is through retained working files;
actual provider execution is independently unattested.
