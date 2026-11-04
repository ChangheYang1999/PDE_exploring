# An improved largest-strain threshold for derivative decay

Status: CONFIRMED in A506 after complete independent reconstruction and full postread. The result is conditional on a strain bound and does not prove profile nonexistence.

## 1. Exact hypotheses and conclusions

Fix 0<c<1 and any finite real omega. Let U in C2(R3;R3), P in C1(R3) solve

    div U=0, ((1-c)I+omega J)U+DU(Ay+U)+grad P=0,
    A=cI-omega J, J(y1,y2,y3)=(-y2,y1,0).

Suppose M=sup|U| is finite. Put G=DU, S=(G+G^T)/2, W=curl U and lambda=lambda_max(S). All norms of linear maps below are operator norms unless marked F.

(a) If lambda<=L outside a ball, for a finite L>=0, then

    |W(y)|<=C(1+|y|)^((L-1)/c),
    |DU(y)|<=C(1+|y|)^max(0,(L-1)/c).

(b) If lambda<=1+gamma+epsilon(|y|) outside a ball, where gamma>=-1 is constant, epsilon is bounded, nonnegative and measurable, and integral_R0^infinity epsilon(r)dr/r<infinity, then

    |W(y)|<=C(1+|y|)^(gamma/c),
    |DU(y)|<=C(1+|y|)^max(0,gamma/c).

Consequently each of the following implies DU->0 uniformly, Dini derivative decay and |DU|+|W|<=C/(1+|y|):

    (i) bounded U and limsup_(|y|->infinity) lambda(y)<1+c/2;
    (ii) uniform U->0 and lambda<=1+c/2+epsilon(|y|),
         with epsilon as in (b).

No smallness of the finite constants in (ii) is needed. At bounded-velocity scope the tail limsup of lambda therefore lies in {0} union [1+c/2,infinity]. If U tends uniformly to zero and DU fails to tend to zero, then for every epsilon in (b), the inequality lambda>1+c/2+epsilon(|y|) holds on an unbounded set. Constants may depend on the fixed profile, c and omega; no estimate uniform in omega is asserted.

## 2. Complete exterior flow and uniform elapsed time

Let B=Ay+U. It is C1 and has at most linear growth, so a solution on any finite time interval remains in a bounded ball by Gronwall. Local C1 existence therefore continues in both time directions. Along its orbit, r=|y| obeys

    cr-M<=r'<=cr+M.

Choose R1>max(1,R0,2M/c), making R1 positive even when U=0. For r>=R1, r'>=cr/2>0. A backward orbit from any exterior point must reach r=R1 in finite time: otherwise r(-t)<=r(0)exp(-ct/2) while r(-t)>=R1. The crossing is unique by strict radial monotonicity. Let s>=0 be the elapsed forward time from this crossing to y. Then

    |cs-log(|y|/R1)|
      <=integral_0^s M/r(t)dt
      <=(2M/c)integral_R1^infinity dr/r^2<1.       (1)

All constants are uniform over the crossing sphere. The rotation term vanishes in the radial scalar product for every omega.

## 3. Growth of the curl and control of the skew part

Curling exact momentum gives the pointwise linear equation along B,

    W'=GW-W-omega JW.

Nonzero W stays nonzero on a finite orbit segment by uniqueness. Since the skew parts of G and J contribute zero to W.W',

    d(log|W|)/ds=(W.SW)/|W|^2-1<=lambda-1.        (2)

Zero trajectories satisfy every resulting upper bound as well. Under (a), (1)-(2) give

    |W(y)|<=max_(|z|=R1)|W(z)| exp(|L-1|/c)
                (|y|/R1)^((L-1)/c).

This estimate handles either sign of L-1. Under (b), the additional integral in the exponent is bounded uniformly by

    integral_0^s epsilon(r(t))dt
       <=(2/c)integral_R1^infinity epsilon(r)dr/r.

The main factor is exp(gamma s), giving the stated exponent gamma/c.

Trace S=0. If each eigenvalue is at most L, the smallest is at least -2L, so |S|<=2L. In (b) use L=1+gamma+sup epsilon, which is finite and nonnegative. The skew part K=(G-G^T)/2 satisfies Kv=(W cross v)/2, hence |K|=|W|/2. Thus |G|<=|S|+|W|/2 gives both derivative growth statements. Compact continuity extends the estimates through the interior ball.

## 4. Applying the confirmed growth theorem

Under (i), choose L between the tail limsup of lambda and 1+c/2. Since lambda>=0, L can be chosen nonnegative. Part (a) gives G=O(r^delta) with delta=max(0,(L-1)/c)<1/2. Hence G=o(sqrt r), and A498(A) gives G->0 under bounded U.

Under (ii), part (b) with gamma=c/2 gives G=O(sqrt r). Uniform velocity decay supplies the other hypothesis of A498(B), so G->0 without a smallness requirement. A476 and A492 then give the Dini and O(1/r) conclusions in both cases. If additionally U(R .)->0 distributionally and c>1/3, A477 gives G=O(r^(-1/c)).

The gap statement follows because lambda is nonnegative and G->0 forces lambda->0. The exceptional-set statement is exactly the contrapositive of (ii), with a fixed but arbitrary permitted epsilon. These are statements about failure of derivative decay, not about all nonzero profiles.

## 5. An immediate scalar corollary and limits

The exact equation gives -Delta P=tr(G^2) and

    |S|_F^2=|W|^2/2-Delta P,
    lambda_max(S)^2<=(2/3)|S|_F^2.

Therefore the sufficient criterion (I) of A504 can now be strengthened to

    limsup_(|y|->infinity)(|W|^2/2-Delta P)
          < (3/2)(1+c/2)^2.                              (3)

It implies (i) and hence derivative decay. Equation (3) is only a sufficient scalar criterion. No PDE sharpness is claimed at its endpoint; the number 3/2 comes from a trace-free matrix inequality. A504's independent finite-bound criterion (II) remains valid.

For Q_s=exp(omega sJ), the physical conversion is orthogonal conjugation:

    sym grad u(x,t)=(T-t)^(-1)Q_s S(y)Q_s^T,
    y=exp(sA)x, s=-log(T-t).

Thus failure of derivative decay permits a sequence at radii |y|->infinity with the dimensionless physical largest strain at least 1+c/2-o(1). A fixed physical point follows a spiral unless omega=0 or it lies on the rotation axis; no fixed-ray inference is used.

The source's separate high-angular-frequency kinematic example is not certified by this verdict. Nor does a residual example prove that every possible proof of a growth bound must invoke vorticity transport explicitly. What is proved here uses exact vorticity transport, and the stated kinematic estimates alone have not supplied a bound. No bounded-strain hypothesis is inferred from bounded or decaying velocity.

## 6. Verification and collaboration

The complete submitted source and complete originating external referee (a second model) were read. The growth and orbit estimates were independently rederived; the downstream A498, A476 and A492 scopes were checked against the ledger. The Theory Agent A configured-model author reports a line-by-line check of the growth estimate. The originating inner model call failed, and is not counted as successful collaboration. Existing configuration is the primary model, with no independent provider runtime attestation.

No computation or formal build is needed for these exact estimates. The source's optional random-matrix checks are not a basis for the verdict.
