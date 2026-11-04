# A uniform quadratic pressure bound and the exact local smooth threshold

Status: independent reconstruction and existing Theory Agent C  comparison complete; the stated polynomial and local conclusions are CONFIRMED at their explicit hypotheses. The polynomial result below supplies a conditional local theorem; it does not supply the pressure inequality for a decaying Euler profile.

## 1. Exact statements and notation

All polynomials and matrices are real. For a vector field, (DQ)_ij=partial_j Q_i, so tr((DQ)^2)=sum_ij partial_j Q_i partial_i Q_j. Brackets denote normalized integration over the unit sphere in R3.

If Q is a homogeneous quadratic vector polynomial, div Q=0, and R is a homogeneous quartic scalar polynomial satisfying

    -Delta R=tr((DQ)^2),   R>=(5/32)|Q|^2 on R3,

then Q=R=0. No symmetry of either polynomial is assumed.

Let Gamma_2 be the supremum of feasible gamma>=0 among these Poisson pairs normalized by <|Q|^2>=1, with R>=gamma|Q|^2. This supremum is positive, finite and attained, and

    Gamma_2 < 5/32 < 1/6.

Let 0<r0<infinity, V in C3(B_r0;R3), and P in C4(B_r0;R). Suppose div V=0, -Delta P=tr((DV)^2), and V(0)=DV(0)=P(0)=0. If P>=gamma|V|^2 on the whole ball for a constant gamma>1/6, then V=P=0 throughout the ball. At every gamma<=1/6 a nonzero smooth polynomial Poisson pair satisfies all these hypotheses except the strict lower bound on gamma. Thus 1/6 is the exact threshold for this local class.

Sections 2-9 give a direct proof. They do not use the quartic-cone results, Hilbert's theorem, separation, numerical optimization or any interchange of maxima and minima. Section 10 states a further corollary with its explicit earlier dependency.

## 2. A strictly positive spherical functional

For a symmetric matrix B and a homogeneous quartic F, define C_F by Delta F=x^T C_F x and ell_B(F)=tr(B C_F). Then

    ell_B(F)=15 <(7 n^T B n-tr B)F(n)>.                 (1)

Here is a direct verification on a polynomial basis. Diagonalize B orthogonally. The coordinate x_1 has uniform distribution on [-1,1] on the unit sphere, giving <x_1^4>=1/5 and <x_1^6>=1/7. The identities obtained by multiplying x_1^2+x_2^2+x_3^2=1 by x_1^2 and x_1^4 give <x_1^2 x_2^2>=1/15 and <x_1^4 x_2^2>=1/35. Multiplication by x_1^2 x_2^2 then gives <x_1^2 x_2^2 x_3^2>=1/105. Odd moments vanish by reflection. Substitution into the right side of (1) gives 12b_i for F=x_i^4, 2(b_i+b_j) for F=x_i^2 x_j^2, and zero on every remaining quartic monomial. These are exactly the values of the left side.

If tr B=1 and B>=(1/7)I, the weight in (1) is nonnegative and has positive mean 4/3. Therefore ell_B(F)>=0 for F>=0. In fact the inequality is strict for any nonzero such F. The weight is positive on a nonempty open sphere patch. If F vanished on that whole patch, homogeneity would make it vanish on an open subset of R3, forcing the polynomial to be zero. Otherwise nonnegativity and continuity give a smaller patch where both factors are positive.

For any gamma set

    x^T C_gamma(Q)x=-tr((DQ)^2)-gamma Delta|Q|^2.

For a feasible pressure, F=R-gamma|Q|^2 is nonnegative and C_F=C_gamma(Q). We shall construct a B for which the pairing at gamma=5/32 is nonpositive, and then exclude equality.

## 3. Projection onto all tangential quadratic fields

Let Tspace be the space of solenoidal homogeneous quadratic vector polynomials T with x.T(x)=0. Every such T equals x cross Mx for a symmetric matrix M. Indeed

    x cross curl T=grad(x.T)-T-(x.grad)T=-3T.

Since curl T is linear, this expresses T=x cross Mx for some matrix M. The divergence identity div(x cross Mx)=-x.curl(Mx) and div T=0 force M to be symmetric. Conversely every symmetric M gives a tangential solenoidal field. The kernel consists of scalar matrices, since Mx parallel to x for every x implies M scalar. Thus Tspace has dimension five.

Project Q onto this entire space using the positive definite inner product <Q.T>, and write Q=T+N with N perpendicular to Tspace. If T is nonzero, diagonalize its symmetric M in an oriented orthonormal frame. Changing the sign of one eigenvector makes the frame oriented without changing diagonality. Then

    T=(a yz,b xz,d xy),   a+b+d=0,
    s=a^2+b^2+d^2>0.                                  (2)

There is no restriction on the original Q in this choice of frame. If T=0, choose any orthonormal frame instead.

## 4. Complete parity decomposition

Under coordinate reflection x -> D x, with D=diag(epsilon_1,epsilon_2,epsilon_3), vector fields transform as Q(x) -> D Q(Dx). The eighteen vector quadratic monomials split into four characters. The xyz character has the three monomials (A yz,B0 xz,D0 xy), which are automatically divergence free. Each remaining character has five component monomials and one divergence constraint, leaving four coefficients. The total solenoidal dimension is 3+3*4=15.

Orthogonality of N to the two-dimensional diagonal-M part of Tspace forces its xyz coefficients to be equal. Thus the xyz part of Q is

    Q_xyz=((a+h)yz,(b+h)xz,(d+h)xy).                    (3)

For the z-character write a general solenoidal part as

    ((u+v)xz,(u-v)yz,d0 x^2+e0 y^2-u z^2).

The remaining tangential direction in this character is (-xz,yz,x^2-y^2). Orthogonality, using the fourth moments in Section 2, gives d0-e0=v. With w=(d0+e0)/2 the part is exactly

    N_z=((u+v)xz,(u-v)yz,
                (w+v/2)x^2+(w-v/2)y^2-u z^2).         (4)

There are two further independent parts obtained by cyclic permutation. Consequently (3) and the three forms (4), together with the choice of eigenframe, retain all fifteen original degrees of freedom: five in the tangential projection and ten in its perpendicular complement. The displayed coefficients describe the actual rotated Q. They are not claimed to parametrize the entire fifteen-dimensional space in one fixed frame.

For diagonal B, the quadratic functional Q -> tr(B C_gamma(Q)) is reflection invariant. Distinct characters are orthogonal for its associated bilinear form: choose a reflection on which their character product is -1, so invariance makes the mixed pairing its own negative. Thus all six mixed pairings between these four parts vanish. This argument does not assume that the functional is positive definite.

## 5. Adapted test and the xyz estimate

For nonzero T choose

    b_i=1/7+4a_i^2/(7s),   (a_1,a_2,a_3)=(a,b,d),
    B=diag(b_1,b_2,b_3).                               (5)

Then tr B=1 and B>=(1/7)I. Put p=abd. The relation a+b+d=0 implies

    sum a_i^4=s^2/2,    sum a_i^3=3p,
    (a-b)^2(b-d)^2(d-a)^2=s^3/2-27p^2.

The last identity follows by expanding the discriminant of the cubic with roots a,b,d, or by direct multiplication with d=-a-b. It gives p^2<=s^3/54, with equality exactly when two roots agree.

For Q=(A yz,B0 xz,D0 xy), the first diagonal coefficient of C_gamma is -2B0 D0-2gamma(B0^2+D0^2), with cyclic analogues. To check the substitution into (3), the two sums needed are

    sum b_i(a_j+h)(a_k+h)=-s/14+h^2-12ph/(7s),
    sum (1-b_i)(a_i+h)^2=4s/7+2h^2-24ph/(7s).

Here {i,j,k}={1,2,3}. At gamma=5/32 these yield

    tr(B C_gamma(Q_xyz))
       =-s/28+9ph/(2s)-(21/8)h^2
       =-(21/8)(h-6p/(7s))^2-s/28+27p^2/(14s^2)
       <=0.                                           (6)

Equality requires two of a,b,d to be equal and h=6p/(7s). Up to permutation, this is

    (a,b,d)=(2t,-t,-t), h=2t/7, t!=0,
    Q_xyz=(t/7)(16yz,-5xz,-5xy).                        (7)

## 6. Explicit estimate on each normal part

For (4), put k=b_3 and delta=b_1-b_2. Direct differentiation gives

    tr((DN_z)^2)
       =4(u+v)(w+v/2)x^2+4(u-v)(w-v/2)y^2
            +(6u^2+2v^2)z^2.

The coefficients of Delta|N_z|^2 are

    x^2: 2u^2+2uv+4v^2+16w^2+12wv-4uw,
    y^2: 2u^2-2uv+4v^2+16w^2-12wv-4uw,
    z^2: 16u^2+4v^2-8uw.

Pairing these expressions with B at gamma=5/32 proves

    -32 tr(B C_gamma(N_z))=(u,w,v) H(k,delta)(u,w,v)^T,

    H=[[10+262k,54-74k,37delta],
       [54-74k,80(1-k),94delta],
       [37delta,94delta,84]].                          (8)

For the adapted weights, q=d^2/s lies in [0,2/3] because d=-(a+b). Also (a^2-b^2)^2/s^2=q(2-3q). Since k=(1+4q)/7, these give

    1/7<=k<=11/21,
    delta^2=-3k^2+2k-11/49.                            (9)

The first leading principal minor of H is positive. Its second is 4P(k), where

    P(k)=-529+7038k-6609k^2.

This concave quadratic is positive throughout the interval in (9), since its endpoint values are 16736/49 and 197600/147. Expansion of the determinant gives

    det H=336P(k)+48delta^2(3703-56672k)=48D(k),
    D(k)=170016k^3-170716k^2+(3400320/49)k-222180/49.

The derivative D'=510048k^2-341432k+3400320/49 is positive on the whole real line: its leading coefficient is positive and

    4*510048*3400320-49*341432^2=1225090940864>0.

Thus D is increasing, and D(1/7)=16736/7>0 proves the determinant is positive on (9). Sylvester's criterion proves H positive definite. The same calculation applies to both cyclic normal parts.

When T=0 use B=I/3 instead. In (8), k=1/3 and delta=0. The upper block has diagonal 292/3 and 160/3 and determinant 12992/3, and the final entry is 84. It is positive definite. The xyz part then has all coefficients h and pairing -(21/8)h^2. Hence every nonzero Q with T=0 has strictly negative total pairing.

## 7. Endpoint exclusion

Suppose a nonzero Q had a feasible pressure at gamma=5/32, and put F=R-gamma|Q|^2. If T=0, Section 6 contradicts ell_B(F)>=0. If T is nonzero, the absence of mixed terms, (6), and strict negativity on nonzero normal parts imply ell_B(F)<=0. The strict positivity in Section 2 forces F=0, so C_gamma(Q)=0.

Equality of the total pairing also forces every normal part to vanish and forces (7). For that explicit remaining field, however,

    C_gamma(Q)=(t^2/49)diag(-525/8,1155/16,1155/16),    (10)

which is nonzero. The first entry follows from -2*(-5)*(-5)-(5/16)*(25+25); the other two follow from -2*16*(-5)-(5/16)*(256+25). This is the required contradiction. Once Q=0, R is a nonnegative harmonic homogeneous quartic and its sphere mean is zero, so R=0. Any larger gamma implies the already excluded endpoint inequality.

## 8. Attainment and a strictly smaller supremum

For a self-contained positive feasible example, let rho^2=x^2+y^2 and take

    Q=z(-y,x,0),
    R=rho^4/160-rho^2 z^2/20+11z^4/60.

Then div Q=0, -tr((DQ)^2)=2z^2, and Delta R=2z^2. Moreover

    R-|Q|^2/100
       =(rho^2-24z^2/5)^2/160+59z^4/1500>=0.

Scaling Q and R by the corresponding squared normalization gives <|Q|^2>=1 while preserving gamma=1/100. Thus Gamma_2>0 without any external polynomial example.

On the finite-dimensional quadratic space the sphere L2 norm is a genuine norm, so the normalization bounds the coefficients of Q and consequently of N defined by -tr((DQ)^2)=x^T Nx. For any homogeneous quartic pressure, averaging its polar-coordinate Laplacian gives

    <R>=tr N/60.

Feasibility and normalization imply gamma<=<R>, giving a finite uniform upper bound. For a sequence tending to the supremum we may take gamma positive, because the positive example has already been exhibited. Then every pressure R in the sequence is nonnegative, so its sphere L1 norm equals its bounded mean. Sphere L1 is a norm on the finite-dimensional quartic space: zero integral of absolute value forces zero on the sphere and hence zero everywhere by homogeneity. Norm equivalence therefore bounds its coefficients.

Extract convergent subsequences for Q, R and gamma. Polynomial identities, pointwise inequalities and normalization all survive coefficient convergence. The limiting Q is nonzero and realizes Gamma_2. Section 7 excludes Gamma_2>=5/32, proving the strict bound. The argument supplies no numerical size for the gap below 5/32.

## 9. Local smooth vanishing and exact sharpness

Assume the local C3/C4 hypotheses of Section 1. Positivity of gamma gives P>=0. Its linear Taylor term vanishes at its minimum. Its quadratic term is nonnegative with zero trace, since DV(0)=0 and the Poisson equation gives Delta P(0)=0; it therefore vanishes. Its cubic term must vanish too, since an odd nonzero leading term cannot be nonnegative in both opposite directions.

Write V=Q+O(|x|^3), P=R4+o(|x|^4). Taylor expansion of the differentiated equations is justified by V in C3 and P in C4. It gives div Q=0, -Delta R4=tr((DQ)^2), and R4>=gamma|Q|^2. As gamma>1/6>5/32, Section 7 forces Q=R4=0. Hence V=O(r^3).

Let S=V tensor V+P I. Incompressibility and the Poisson equation give div div S=0. For every centered sphere its continuous field div S has zero total flux. Put

    e(r)=<|V(rn)|^2>, v(r)=<(V(rn).n)^2>,
    A(r)=v(r)+<P(rn)>.

Differentiating n=x/|x| gives div(Sn)=(div S).n+(tr S-n.S n)/r. The average of its left side is A'+2A/r. Since tr S=|V|^2+3P, the zero flux gives

    rA'=e-3v,
    A(r)=integral_0^r (e(t)-3v(t))dt/t.                (11)

The second formula uses A(0)=0 and integrability near zero; V=O(r^3) makes e,v=O(r^6). Thus A=O(r^6). The whole-ball inequality gives A>=gamma e>=0, and (11) yields A'<=A/(gamma r). Consequently r^(-1/gamma)A is nonincreasing. Its limit at zero is zero because 6-1/gamma>0. It is also nonnegative, so it is zero at every radius. Now e=0 forces V=0, and positivity with zero sphere mean forces P=0. This is a whole-ball argument and uses no unique continuation claim.

For sharpness let V=rho^2(-y,x,0), P=rho^6/6. It is polynomial, divergence free, and (V.grad)V=-rho^4(x,y,0)=-grad P. Hence it satisfies the Poisson equation and P=|V|^2/6. Its center values and first velocity derivative vanish. It is feasible at every gamma<=1/6, nonzero, and grows at infinity. Therefore it is not a counterexample in the decaying class.

## 10. Center Holder corollary, evidence and scope

The earlier independently confirmed center Holder theorem A2735-A2737 has the following exact hypotheses: V in C2(B_r0;R3), P in C1(B_r0;R), the Poisson equation in distributions, div V=0, V(0)=DV(0)=P(0)=0, and for some finite C and some smaller ball,

    |D2V(x)-D2V(0)|<=C|x|^alpha, 0<alpha<=1.

Together with the same whole-ball pressure inequality, its exact threshold was max(Gamma_2,1/(4+2alpha)); the proof and sharpness are in the team records. Since 1/(4+2alpha)>=1/6>Gamma_2, that threshold is now exactly 1/(4+2alpha). This corollary imports the earlier theorem with all its stated regularity and normalization assumptions. In particular, alpha=1 allows only C1 pressure and a center Lipschitz modulus for D2V; it does not assert C4 regularity of that pressure.

All nine submitted source sections and all 72 existing exact-check entries were read. The archived check reports 2.1606482318602502 seconds, but it was not rerun. Sections 2-9 are independent hand reconstructions of the general argument, including every normal coefficient, all determinant constants, the equality field and compactness. The positive example in Section 8 is an additional hand-checked construction. The complete existing Theory Agent C  comparison is checked in Section 11.

No arbitrary-omega Euler profile is ruled out by this theorem alone. The original question still requires the whole-ball pressure lower bound and center normalization for an actual profile, or some different global argument. Neither follows here from decay. No value of the unrestricted Gamma_2 is computed; its comparison with 1/6 is settled by the confirmed polynomial theorem.


## 11. Existing model comparison and final verdict scope

The complete Theory Agent C 03:06 comparison and all32 entries of its independent check log were read. Its hand arguments agree with every substantive step: positive spherical functional, full projection and parity decomposition, orthogonality, equality exclusion, attainment, pressure Taylor expansion, finite-ball stress identity, radial monotonicity and the Holder corollary. The log checks all cyclic normal groups and all relevant determinant constants; no source or comparison code was rerun. A separate coordinator comparison remains an additional check, not a missing mathematical hypothesis.

Sections 2-7 confirm the unrestricted homogeneous polynomial endpoint exclusion. Section 8 confirms a positive attained Gamma_2 strictly below5/32. Section 9 confirms the exact local C3/C4 threshold1/6. Section 10 confirms the exact center-Holder threshold1/(4+2alpha) using the explicitly named prior theorem A2735-A2737. These are separate conclusions, with all regularity, ball, center and pressure-bound assumptions retained. The growing stationary swirl proves sharpness only in the local kinematic Poisson class. No actual-profile pressure premise, center normalization for every decaying profile, exact value of Gamma_2 or arbitrary-omega nonexistence theorem follows.

The C agent is configured as model; actual provider execution is independently unattested. All exchange was through the existing shared files. No new model client, agent, mathematical computation or forbidden runtime was used.


## 12. Additional coordinator comparison and numerical scope

All eight coordinator items and W1-W3, all39 final check entries, the initial log and the one-hunk script repair were read. The analytic comparisons in items1-7 agree with Sections1-10. The initial three failed checks came from pairing a cyclic component permutation with the inverse coordinate permutation. The repair uses x->y,y->z,z->x together with the matching component order, which carries the z character into the x character; its formula agrees with the hand proof. The initial exit code0 did not mean the checks passed: the log explicitly says SOME FAIL. Both records are retained. No check was rerun.

W1 is correct: b_i>=1/7 implies sum1/b_i<=21<49, so the weights are strictly inside the dual region, although their pointwise spherical weights can vanish. W2's tightness concerns this particular adapted test at its equality field, not the actual value of Gamma_2. The lower bound g_star comes from the separately confirmed equivariant optimum A2718-A2720. W3 preserves the exact local regularity and whole-ball pressure premises. The later A2826 gives the stronger upper bound1/7.

One numerical phrase in item8 is not supported by the retained summary. The source computes worst_eq=min(abs(val)) over200 perturbed equality fields, logging5.56e-6; it does not record their maximum absolute value. Therefore the statement that the200 values were all within6e-6 of zero must be replaced by the smallest absolute normalized value being5.56e-6. The logged nonpositive test over all4000 fields and the generic maximum-0.7912 are separate diagnostics. The near-equality threshold in the actual check was1e-3 for the minimum, not6e-6 for all values. This has no role in the analytic proof and does not alter A2820-A2823.


## 13. Repaired numerical statement and source status

The coordinator comparison now gives the full recorded range of the200 absolute normalized near-equality pairings:5.56e-6 to9.12e-5, rounded in its prose to5.6e-6 to9.1e-5. The complete revised comparison and final39-entry log were read. This is consistent with the retained data and resolves the unsupported all-values bound in A2830. Zero values were counted above the positive1e-12 threshold; the reported minimum absolute value is above that threshold, so these retained diagnostics are consistent with negative sampled pairings. They remain numerical observations, not the proof of nonpositivity. The earlier log is retained separately.

The revised sourcef85097343eda1cf19a18b542b0de849b3cf673b88b975ed0245d5df635be7645 was compared line by line against its retained original. Its confirmation status, resolved comparison with1/6 and additional comparison record agree with A2820-A2824 and A2829-A2830. No mathematical formula or hypothesis has been strengthened. Its record of A2830 is historical; the repaired numerical statement above supplies the resolution. No check was rerun.
