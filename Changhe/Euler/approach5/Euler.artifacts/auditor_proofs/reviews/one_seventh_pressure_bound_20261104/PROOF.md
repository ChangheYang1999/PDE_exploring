# Strict one-seventh bound for quadratic Poisson pressures

Status: CONFIRMED A2825-A2826; applicability remains OPEN A2827.

## 1. Statement and exact dependency

Let Q:R3->R3 be a real homogeneous quadratic polynomial with div Q=0, and let R:R3->R be a real homogeneous quartic polynomial. If

    -Delta R=tr((DQ)^2),   R>=|Q|^2/7 on R3,

then Q=R=0. Here (DQ)_ij=partial_j Q_i. Both polynomials are unrestricted apart from the stated conditions; in particular every harmonic quartic adjustment to R is allowed.

Normalize nonzero Q by <|Q|^2>=1, with brackets denoting the normalized sphere mean. Let Gamma_2 be the supremum of feasible nonnegative ratios. It is positive, finite and attained, and Gamma_2<1/7. Its exact value is not asserted.

The only imported theorem is the following part of A2805, proved independently in the team records: for any positive definite B with tr(B)tr(B^-1)<=49, the functional ell_B(F)=tr(B C_F), where Delta F=x^T C_F x, is nonnegative on every nonnegative homogeneous quartic F. That theorem has an elementary atomic proof and does not require Hilbert's theorem or separation. The present proof does not depend on the separately confirmed five-thirtyseconds result.

## 2. Strict positivity of the chosen test

If tr B=1 and B>=I/9, put B0=B-I/36. It is positive definite, has minimum eigenvalue at least1/12 and trace11/12. Thus tr(B0^-1)<=36 and tr(B0)tr(B0^-1)<=33<49. The imported theorem applies to B0.

For any homogeneous quartic F, the polar Laplacian identity gives <Delta F>=20<F>. On the other hand <x^T C_F x>=tr C_F/3. Hence ell_I(F)=60<F>. A nonnegative nonzero homogeneous quartic has strictly positive sphere mean. It follows that

    ell_B(F)=ell_B0(F)+ell_I(F)/36>0

for every such F. This includes B with eigenvalue exactly1/9. No pointwise sign of the quadratic spherical weight is needed.

For any gamma define C_gamma(Q) by x^T C_gamma(Q)x=-tr((DQ)^2)-gamma Delta|Q|^2. For a feasible pair, F=R-gamma|Q|^2 is nonnegative and C_F=C_gamma(Q). We will construct an admissible B with nonpositive pairing and exclude equality.

## 3. Projection and the full polynomial space

The space of tangential solenoidal homogeneous quadratic fields is exactly

    T=x cross Mx, M symmetric modulo scalar multiples of I.

Indeed x cross curl T=grad(x.T)-T-(x.grad)T=-3T when x.T=0. Since curl T is linear, this yields the stated form with some M. The identity div(x cross Mx)=-x.curl(Mx) forces symmetry. Conversely symmetry implies zero divergence and tangency. If x cross Mx vanishes for every x, every vector is an eigenvector of M, so M is scalar. The space therefore has dimension five.

Project Q orthogonally onto it using the sphere inner product, writing Q=T+N. If T!=0, diagonalize its symmetric M in a positively oriented orthonormal frame. In this frame

    T=(a yz,b xz,d xy), a+b+d=0, s=a^2+b^2+d^2>0.

The choice of frame depends on Q; it imposes no symmetry on Q. If T=0 choose any frame.

Under Q(x)->D Q(Dx), with D a coordinate sign reflection, the eighteen vector quadratic monomials have four characters. The xyz character has three monomials and automatic zero divergence. Each other character has five monomials and one independent divergence constraint. Hence the full solenoidal dimension is3+3*4=15.

Orthogonality to the two tangential xyz directions makes the xyz part

    Q_xyz=((a+h)yz,(b+h)xz,(d+h)xy).

For the z character, solenoidality gives

    ((u+v)xz,(u-v)yz,d0 x^2+e0 y^2-u z^2).

The tangential direction is (-xz,yz,x^2-y^2). Its inner product with this field is [-2v+2(d0-e0)]/15, using <x^4>=1/5 and <x^2y^2>=1/15. Thus d0-e0=v, and with w=(d0+e0)/2 the remaining part is

    N_z=((u+v)xz,(u-v)yz,
                (w+v/2)x^2+(w-v/2)y^2-u z^2).

Two cyclic copies give the other characters. The five tangential parameters consist of two diagonal parameters and the three parameters used to choose the eigenframe; ten complementary parameters remain. The displayed twelve coefficients in the chosen frame must not be mistaken for a fixed-frame parametrization of only a twelve-dimensional subspace.

For diagonal B the quadratic functional Q->tr(B C_gamma(Q)) is invariant under all these reflections. Its associated bilinear pairing between different characters vanishes, because some reflection changes the sign of exactly one character. Thus the total pairing is the sum of the four individual pairings. All six cross terms have been accounted for.

## 4. Adapted weights and the xyz part

For T!=0 put p=abd and choose

    b_i=1/9+2a_i^2/(3s), B=diag(b_1,b_2,b_3).

Then tr B=1 and B>=I/9. The identities sum a_i^4=s^2/2, sum a_i^3=3p and

    (a-b)^2(b-d)^2(d-a)^2=s^3/2-27p^2

follow by expanding with d=-a-b. In particular p^2<=s^3/54, with equality exactly when two of a,b,d coincide.

For general adapted weights b_i=b0+beta a_i^2/s with 3b0+beta=1, the sums needed for the xyz pairing are

    sum_i b_i(a_j+h)(a_k+h)=-b0*s/2-3beta*p*h/s+h^2,
    sum_i(1-b_i)(a_i+h)^2=(1+b0)*s/2-6beta*p*h/s+2h^2.

The first identity uses a_j a_k a_i^2=p a_i and sum a_i=0. The second uses sum a_i^4=s^2/2. For Q=(A yz,B1 xz,D1 xy), the first diagonal entry of C_gamma is -2B1D1-2gamma(B1^2+D1^2), with cyclic analogues. Substituting b0=1/9, beta=2/3 and gamma=1/7 therefore gives

    tr(B C_gamma(Q_xyz))
       =-s/21+36ph/(7s)-18h^2/7
       =-(18/7)(h-p/s)^2-s/21+18p^2/(7s^2)<=0.

Equality forces two equal tangential coefficients and h=p/s. Up to permutation,

    (a,b,d)=(2t,-t,-t), h=t/3, t!=0,
    Q_xyz=(t/3)(7yz,-2xz,-2xy).

## 5. Every normal part is strictly negative

For the z character put k=b3 and delta=b1-b2. Directly from N_z,

    tr((DN_z)^2)=4(u+v)(w+v/2)x^2
                +4(u-v)(w-v/2)y^2+(6u^2+2v^2)z^2.

The x^2,y^2,z^2 coefficients of Delta|N_z|^2 are respectively

    2u^2+2uv+4v^2+16w^2+12wv-4uw,
    2u^2-2uv+4v^2+16w^2-12wv-4uw,
    16u^2+4v^2-8uw.

Consequently, at gamma=1/7,

    -7 tr(B C_gamma(N_z))=(u,w,v)H(k,delta)(u,w,v)^T,
    H=[[2+56k,12-16k,8delta],
       [12-16k,16(1-k),20delta],
       [8delta,20delta,18]].

For q=d^2/s, the relation d=-(a+b) gives0<=q<=2/3. Also (a^2-b^2)^2/s^2=q(2-3q). Since k=1/9+2q/3, it follows that

    1/9<=k<=5/9, delta^2=-3k^2+2k-5/27.

The first leading minor is positive. The second is16P(k), with

    P(k)=-7+78k-72k^2,
    P(1/9)=7/9, P(5/9)=127/9.

Concavity proves strict positivity throughout the interval. Expansion by the final row gives

    det H=288[P(k)+delta^2(7-92k)]=288D(k),
    D(k)=276k^3-277k^2+(2944/27)k-224/27.

The derivative is828k^2-554k+2944/27. Its leading coefficient is positive and

    4*828*2944-27*554^2=1463796>0,

so its discriminant is negative and D'>0 on the real line. Since D(1/9)=7/9>0, the full determinant is strictly positive on the interval. Sylvester's criterion proves H positive definite. The cyclic normal parts have exactly the same argument.

If T=0 use B=I/3. The same H has k=1/3 and delta=0; the upper block has positive first entry and determinant16P(1/3)=176, and the last diagonal entry is18. Its pairing is strictly negative on any nonzero normal part. The xyz part now has coefficients(h,h,h) and pairing-18h^2/7. Thus the total pairing is strictly negative for every nonzero Q with T=0.

## 6. Equality exclusion

For a feasible pair at gamma=1/7 set F=R-|Q|^2/7. If T=0, strict negative pairing contradicts nonnegativity. If T!=0, all four pairings are nonpositive. Strict positivity of ell_B on every nonzero nonnegative quartic forces F=0, so C_gamma(Q)=0. Equality also forces all normal parts to vanish and Q=(t/3)(7yz,-2xz,-2xy) up to permutation.

For this field the first diagonal coefficient of C_gamma is

    t^2[-8/9-16/63]=-8t^2/7,

and each of the others is

    t^2[28/9-106/63]=10t^2/7.

Thus C_gamma(Q)=t^2 diag(-8/7,10/7,10/7), which is nonzero. This contradiction excludes nonzero Q. Then R is nonnegative and harmonic, and its sphere mean is zero by the homogeneous Laplacian identity. Hence R=0.

## 7. Attainment, strict gap and scope

For a positive feasible example independent of any pending result, take Q=z(-y,x,0) and

    R=(x^2+y^2)^2/160-(x^2+y^2)z^2/20+11z^4/60.

Direct differentiation gives Delta R=2z^2=-tr((DQ)^2), and

    R-|Q|^2/100=((x^2+y^2)-24z^2/5)^2/160+59z^4/1500>=0.

Scaling Q and R together normalizes <|Q|^2>=1 without changing the ratio. In this normalization the quadratic coefficients and the coefficients of N_Q defined by -tr((DQ)^2)=x^T N_Q x are bounded. Every feasible R satisfies <R>=tr N_Q/60. Hence gamma<=<R> has a uniform finite upper bound.

Choose a maximizing sequence with positive gamma, which is possible by the explicit example. Then R>=0, so its sphere L1 norm equals its uniformly bounded mean. All norms on the finite-dimensional quartic space are equivalent; its coefficients are therefore bounded. Extract convergent subsequences of Q,R,gamma. All identities, nonnegativity and the normalization pass to the limit, which attains Gamma_2 with nonzero Q. Endpoint infeasibility gives Gamma_2<1/7.

This determines a strict upper bound, not the exact value or a numerical gap below1/7. It does not improve the sharp local smooth threshold1/6 proved by A2822, since the cubic stationary swirl still realizes1/6. It gives no pressure lower bound or center normalization for an actual decaying rotating Euler profile.

## 8. Verification record

All seven source sections and all72 supplementary exact-check entries were read. The source check reports2.105149387381971seconds and was not rerun. The hand reconstruction above includes every normal coefficient, the full determinant, its discriminant constant and endpoint values, the xyz completed square and the equality residual. The positive-functional dependency is explicitly the already confirmed A2805; no symmetry reduction, pressure ansatz or minimax exchange is hidden.

Existing configured model collaboration is through the shared files. The completed Theory Agent C  comparison is recorded below; actual provider execution is independently unattested. No new client, remote job or subagent was used.


## 9. Completed existing model comparison

The complete Theory Agent C 03:07 note and all29 entries in its check log were read. Its full projection, all parity cross terms, adapted weights, completed square, normal matrix, determinant, endpoint signs, equality residual and compactness agree with Sections2-7. The exact matrix checks and a separate20000-sample diagnostic were not rerun here. The sample maximum22.988694 is not used in any inequality proof.

The optional sharper bound in the note can be verified directly: for B0>=I/12 with trace11/12, convexity of the sum of reciprocal eigenvalues puts its maximum at the vertices (1/12,1/12,3/4), up to permutation. The trace product there is209/9. The proof needs only the weaker33 bound, already derived without an optimization.

This provides the existing configured model comparison requested by the standing collaboration preference. The agent designation is known; the actual provider execution is not independently attested. The additional coordinator comparison is welcome but is not a missing mathematical hypothesis. No new model client or agent was launched, and no mathematical computation was performed in this audit.

## 10. Additional coordinator comparison and numerical wording

All five coordinator items, W1-W3, all36 final log entries, the initial failed run and every script repair were read. The analytic checks agree with Sections1-9. The first run stopped at an undefined xv before any LIT337-specific identity; the correction defines the coordinate vector. The repaired script also records both minimum and maximum absolute values in its200 near-equality tests. Its final log ranges from4.77e-6 to9.23e-5. Therefore the comparison's sentence that all these values were within5e-6 of zero is false. It should state the recorded range, or only the closest value. No analytic conclusion uses that numerical claim.

The random tests use a positive threshold1e-12 to count violations, so an absence of counted violations is not by itself an exact nonpositivity proof. The exact analytic argument above provides the nonpositivity statement. The highest generic normalized value was approximately-0.7819 in this finite sample. These are source-log observations, not a computation run by this agent. The initial traceback path has been rewritten relative to the agent roots in the archived copy; the error text is otherwise unchanged.

The tightness observation W2 also follows directly. At Q=(t/3)(7yz,-2xz,-2xy), B=diag(5,2,2)/9, the trace in (6) is -8t^2(7gamma-1)/9. It is positive below1/7, so this particular adapted test cannot yield a smaller threshold. This does not obstruct a different choice of matrix. The full Gamma_2 remains bounded below by the separately established g_star, not evaluated by the trace test.


## 11. Repaired numerical statement and source status

The revised coordinator comparison replaces the false all-values bound by the actual range4.77e-6 to9.23e-5 for absolute normalized pairings, rounded in prose to4.8e-6 to9.2e-5. Every changed line and the complete final36-entry log were read. This resolves the requested correction in A2837. The threshold for counted positive values remains1e-12, and the recorded minimum absolute value is above it. The numerical observations are therefore consistent with negative pairings in this finite sample. They do not prove the analytic inequality or evaluate Gamma_2.

The revised source1e8060b6285e4c2f184c8e2941741363ba1c20f9abfe2b03c24bc22a085813ac has been compared with the retained original and all changed lines read. Its confirmation status and new comparison section agree with A2825-A2827; no equation has changed. The optional209/9 bound is justified in Section9 above. No check was rerun.
