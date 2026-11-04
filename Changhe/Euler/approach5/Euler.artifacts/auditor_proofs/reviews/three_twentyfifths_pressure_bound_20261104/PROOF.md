# Independent audit: the strict three-twentyfifths quadratic pressure bound

## 1. Exact claim and dependencies

Let Q:R3->R3 be a real homogeneous polynomial vector field of degree two with div Q=0, and let R be any real homogeneous polynomial of degree four. Suppose

    -Delta R=tr((DQ)^2),       R(x)>=(3/25)|Q(x)|^2 for every x.

Then Q=R=0. The convention is (DQ)_ij=partial_j Q_i. All harmonic quartic pressure adjustments are allowed. This is a polynomial Poisson assertion, not a theorem that an Euler profile satisfies the pressure inequality.

Write <F> for normalized sphere average. For feasible triples normalized by <|Q|^2>=1 and with coefficient gamma>=0 in R>=gamma|Q|^2, let Gamma_2 be the supremum of gamma. The claimed consequence is g_star<=Gamma_2<3/25, where the lower bound g_star is the already confirmed A2718-A2719 root in (2/17,1/8) of 96g^4+16g^3-23g^2-6g+1. That lower bound is a named dependency, not recomputed here.

The sole cone dependency is A2805, whose elementary proof was repeated in A2858: if B is positive definite and tr(B)tr(B^-1)<=49, then tr(B C)>=0 whenever a nonnegative homogeneous quartic F satisfies Delta F=x^T Cx. Sections 2 to 7 reconstruct the new upper bound. The exact rational data are retained in the team records and reconstructed from the determinant by the independent checker specified in the team records. The exact reconstruction passes; the complete existing coordinator comparison is now read and agrees, as recorded in Section 10.

## 2. A strictly positive functional

For every homogeneous quartic F, the polar Laplacian gives <Delta F>=20<F>, since the sphere Laplacian has integral zero. If Delta F=x^T Cx, then <Delta F>=tr C/3, and therefore tr C=60<F>.

Suppose tr B=1 and B>=3I/22. Put B0=B-I/100. Then B0>=139I/1100, tr B0=97/100 and

    tr(B0)tr(B0^-1) <= (97/100)(3300/139)=3201/139<49.

The cone dependency applies to B0. For nonzero nonnegative F, continuity gives <F>>0. Consequently tr(B C)=tr(B0 C)+(1/100)tr C>0. Thus this functional is strictly positive on every nonzero nonnegative quartic.

Define C_gamma(Q) by x^T C_gamma(Q)x=-tr((DQ)^2)-gamma Delta|Q|^2. For a feasible pair, F=R-gamma|Q|^2 is nonnegative and has Laplacian matrix C_gamma(Q). A nonpositive pairing with a B as above forces F=0 and then C_gamma(Q)=0.

## 3. Complete decomposition of the quadratic field

A tangential solenoidal homogeneous quadratic T satisfies x.T=0. Differentiating this identity and using degree-two homogeneity gives x cross curl T=-3T. Since curl T is linear, T=x cross Mx for a matrix M. Its divergence is -x.curl(Mx), which vanishes identically exactly when M is symmetric. The kernel consists of scalar matrices, so this tangential space has dimension five.

Project Q onto that space in the positive definite sphere inner product and write Q=T+N. For T nonzero choose an oriented orthonormal eigenframe for its symmetric M. Then

    T=(a yz,b xz,d xy),       a+b+d=0,       s=a^2+b^2+d^2>0.

Coordinate reflections acting simultaneously on domain and target split the eighteen component monomials into four characters. The xyz character has three solenoidal coefficients. Each of the other three has five coefficients with one divergence constraint. These give the full fifteen-dimensional solenoidal space. In the xyz character, orthogonality to the two-dimensional tangential subspace makes

    Q_xyz=((a+h)yz,(b+h)xz,(d+h)xy).

In the z character the tangential direction is (-xz,yz,x^2-y^2). A general solenoidal field has first two components (u+v)xz,(u-v)yz and last component Cx^2+Dy^2-u z^2. The sphere inner product with that tangential direction is (-2v+2(C-D))/15. Orthogonality gives C-D=v, hence

    N_z=((u+v)xz,(u-v)yz,(w+v/2)x^2+(w-v/2)y^2-u z^2).

There are two independent cyclic copies. For diagonal B, the pairing tr(B C_gamma(Q)) is invariant under every reflection. A cross term between distinct characters changes sign under a reflection, so it vanishes. The full pairing is exactly the sum of these four character pairings, with every normal degree of freedom included. If T=0, use any frame, a=b=d=0 and the same normal groups.

## 4. Curved weights, their domain and the xyz square

Fix g=3/25. When s>0 put p=abd, r=p^2/s^3 and

    mu=26/(22+sqrt(484-21762r)),       tau=(1-mu)/3,
    B_ii=tau+mu a_i^2/s,              (a_1,a_2,a_3)=(a,b,d).

The identities sum a_i^4=s^2/2 and product of squared pair differences=s^3/2-27p^2 show 0<=r<=1/54. The radical therefore lies in [9,22], and all definitions are real with positive denominator and trace B=1.

For any distinguished entry write q=d^2/s. From a+b=-d, one obtains q in [0,2/3], r=q(1-2q)^2/4 and (a^2-b^2)^2/s^2=q(2-3q). Set Z(q)=484-(10881/2)q(1-2q)^2 and zeta=sqrt(Z). Then

    k=B_33=1/3+(q-1/3)26/(22+zeta).

For q>=1/3 this is at least 1/3. For q<1/3 the bound k>=3/22 is equivalent to zeta>=22-132q. If q>=1/6 the latter is immediate. For q in [0,1/6], both sides to be squared are nonnegative and

    Z-(22-132q)^2=(q/2)(735+8676q-43524q^2)>=0.

The parenthesis is concave with endpoint values 735 and 972, so it is positive throughout. Every diagonal entry has the same proof; hence 3/22<=B_ii<=8/11. Section 2 applies.

For a pure xyz field (A yz,B1 xz,D1 xy), the diagonal entries of C_g are -2B1D1-2g(B1^2+D1^2) and its two cyclic versions. Substituting the shifted coefficients and using a+b+d=0 gives

    tr(B C_g(Q_xyz))=[tau-g(1+tau)]s
                     +6mu(1+2g)(p/s)h-2(1+2g)h^2.

The chosen branch satisfies (837/2)r mu^2-22mu+13=0, including r=0 where mu=13/22. This is the radical's defining quadratic. It is equivalent to tau-g(1+tau)+(9/2)(1+2g)r mu^2=0. Completing the square yields

    tr(B C_g(Q_xyz))=-2(1+2g)[h-(3mu/2)p/s]^2<=0.

No sampling of r is involved.

## 5. Direct normal-block calculation

For the z character put alpha=u+v, beta=u-v, C=w+v/2 and D=w-v/2. Differentiation gives

    tr((DN_z)^2)=4alpha C x^2+4beta D y^2+(6u^2+2v^2)z^2.

The x^2 coefficient of Delta|N_z|^2 is 2u^2+2uv+4v^2+16w^2+12wv-4uw; the y^2 coefficient changes the signs of uv and wv; the z^2 coefficient is 16u^2+4v^2-8uw. Combining them with k=B_33 and delta=B_11-B_22 gives

    -25 tr(B C_g(N_z))=(u,w,v) H(u,w,v)^T,
    H=[[6+192k,44-56k,28delta],
       [44-56k,48(1-k),68delta],
       [28delta,68delta,62]].

The same calculation holds for each cyclic group. Define

    P(k)=-103+866k-772k^2,
    D(k,delta)=31P(k)+(3193-33232k)delta^2.

The first leading minor of H is positive. Expanding the next two gives 16P and 32D. The concave P has values 89/121 and 14337/121 at 3/22 and 8/11, so P>0 on the entire allowed interval. The determinant remains to be checked for the actual weights, not for arbitrary k and delta.

## 6. Exact radical determinant certificate

For the actual weights set t=22+zeta and n=zeta-4+78q. Then k=n/(3t), delta^2=676q(2-3q)/t^2, and direct multiplication gives the polynomial numerator

    9t^3 D=31[-927t^3+2598nt^2-772n^2t]
            +676q(2-3q)[28737t-99696n].

Reduce this expression uniquely in the ring Q[q,zeta]/(zeta^2-Z(q)); write the result A(q)+C(q)zeta. Define A0=A/93 and B0=2C/93. The exact coefficient data specify the polynomial T0 of degree six such that

    A^2-C^2 Z=(57005559/8)q(6q-1)^2 T0.

These are exact polynomial definitions and an identity checked by rational arithmetic. The data file contains the coefficient expressions and the complete 26 Bernstein coefficients. No table is accepted solely because it was imported. The independent checker reconstructs A,C and T0 from the displayed numerator, compares the coefficient expressions, and recomputes every Bernstein coefficient.

For a degree-n polynomial f on [l,u], expand f(l+(u-l)t)=sum_j a_j t^j and set beta_i=sum_{j<=i} a_j binom(i,j)/binom(n,j). Expanding powers shows f(l+(u-l)t)=sum_i beta_i binom(n,i)t^i(1-t)^(n-i). These nonnegative basis functions sum to one on [0,1], so positive beta_i prove strict positivity throughout the interval. The exact data give the following positive minima:

| Polynomial | Interval | Degree | Minimum coefficient |
| --- | --- | --- | --- |
| A0 | [0,1/6] | 4 | 93984 |
| A0 | [1/6,1/3] | 4 | 773910 |
| A0 | [1/3,2/3] | 4 | 14987071/3 |
| B0 | [1/10,2/3] | 3 | 5385586/125 |
| T0 | [0,1/10] | 6 | 35466126112/15 |

It follows that A>0 on [0,2/3]. On [1/10,2/3], C>0 and zeta>0, so A+C zeta>0. On (0,1/10], the squared-difference identity is strictly positive, since q>0 and 6q-1 is nonzero. Thus A>|C|zeta and again A+C zeta>0. At q=0, both A0(0)=93984 and B0(0)=8544 are positive. Since t>0, D>0 everywhere. Sylvester's criterion makes H positive definite for every actual weight and all three normal groups.

## 7. Equality and zero projection

For s>0 the total pairing is nonpositive, with equality only when all normal groups vanish and h=(3mu/2)p/s. A feasible F is nonnegative, so strict positivity from Section 2 forces F=0. Therefore C_g(Q)=0, and Q is pure xyz. Such a nonzero field cannot have C_g=0 for any g>0: if one coefficient vanishes, the equations force the other two to vanish; if all are nonzero, all three pairwise products must be negative. Their product is the positive square (AB1D1)^2, a contradiction. This excludes every s>0 case.

When s=0 the radical formula is not used. Choose B=I/3. The xyz pairing is -2(1+2g)h^2. Each normal block has k=1/3,delta=0 and is positive definite by Section 5. Thus every nonzero Q has strictly negative total pairing, impossible for nonnegative F. Hence Q=0. The pressure R is then nonnegative and harmonic homogeneous quartic; tr C_R=60<R>=0 implies R=0. The endpoint theorem follows.

## 8. Compactness and exact scope

The feasible class is nonempty: take Q0=(xz-sqrt(6)yz,yz+sqrt(6)xz,-x^2-y^2-z^2) and R0=(2/17)|Q0|^2+z^4/34. With rho^2=x^2+y^2, direct differentiation gives div Q0=0, -tr((DQ0)^2)=4rho^2+6z^2, and Delta|Q0|^2=34rho^2+48z^2. Hence Delta R0=4rho^2+6z^2 and its nonnegative surplus is explicit. Normalize its positive sphere energy.

For normalized feasible triples Q belongs to a finite-dimensional compact unit sphere. Its Poisson-source coefficients are uniformly bounded. The sphere identity fixes <R> from the trace of those coefficients. Since R>=gamma|Q|^2>=0, it bounds gamma and the sphere L1 norm of R. This L1 norm is a norm on the finite-dimensional space of homogeneous quartics, so all coefficients of R are bounded. The feasible triples are also closed, hence compact. Their largest gamma is attained, and the endpoint exclusion makes it strictly less than 3/25. The stronger existing lower bound g_star is imported only from A2718-A2719.

This improves the full polynomial upper bound. It neither evaluates Gamma_2 nor changes the local smooth threshold 1/6 or the center-Holder threshold 1/(4+2alpha). All whole-ball Euler pressure premises remain additional hypotheses. No restriction on rotation is obtained from this polynomial statement.

## 9. Verification record

All nine source sections of dd6c191877ac67f8be8e9d6b7015155225a7e42f2bbe1938d7d7a8af88651a9f, the full source plan, both input data files, the complete source checker and all144reported checks were read. The source computation is not rerun. The new calculation is independently implemented with standard-library rational arithmetic and reconstructs the reduced determinant numerator before reading the expected coefficient expressions. All 98 independent rational checks passed and were read, including all26Bernstein coefficients, both radical identities, every interval join and all five minima. The run was from 2026-11-04T03:47:48.292016+00:00 to 2026-11-04T03:47:48.301068+00:00, lasting0.009048020001500845seconds, on CPU55 with nice19 and one OMP thread. The exact results, input and script hashes, and environment are retained in the team records. The complete existing configured model coordinator comparison is read and agrees; actual provider execution is independently unattested. No formal build or Euler-profile computation is used.


## 10. Complete coordinator comparison and computation provenance

The complete coordinator comparison dc31939bd13764c9849eb7f0148935027b54a3d65c7e93fecbc8b4c405bcae88 was read, including all nine numbered items and W1-W3. It agrees with the independent proof. Both its final37-check log and earlier37-check log were read, as was the exact script difference. The earlier run had one failed floating size threshold and exited zero; the final script normalizes the test family to s=1 and adds a failure-dependent exit code. The normalization and exit-code changes do not alter any analytic identity. The final37checks pass. No supplementary script was run in this agent.

The analytical details agree: all fifteen quadratic dimensions are included, the separate zero-projection case is defined, every actual weight is at least3/22, the complete xyz pairing has zero Schur remainder, and the three normal blocks are strictly negative in the pairing. The scalar factor 735+8676q-43524q^2 in the weight argument is quadratic and concave; the comparison's phrase "concave cubic factor" is merely a degree typo. The polynomial identities, endpoints and inequality are correct.

The supplementary finite grids and random fields are numerical diagnostics only. Their reported smallest determinant and eigenvalue are sampled minima, not certified global minimum values. Positivity on the full interval follows from the rational Bernstein argument of Section 6. The near-equality sample range is correctly stated as2.04e-5 to4.10e-4 after normalization. The exact bound on Gamma_2 follows from the proof, not from these samples.

## 11. Exact tightness of this fixed weight family

For every nonzero tangential triple a+b+d=0, the pure xyz field with h=(3mu/2)p/s gives equality in the pairing at g=3/25. The weights are well-defined and positive for this field. If gamma<g while these same weights are retained, then

    tr(B C_gamma(Q))=tr(B C_g(Q))+(g-gamma)tr(B D_Q),

where x^T D_Q x=Delta|Q|^2. For Q=(A yz,B1 xz,D1 xy), D_Q is diagonal with entries2(B1^2+D1^2),2(A^2+D1^2),2(A^2+B1^2). All are nonnegative and at least one is positive. Since B is positive definite, tr(B D_Q)>0. Hence the fixed weight family cannot give a nonpositive pairing for every Q at any smaller coefficient. This proves the precise certificate limitation described in W2. It neither fixes the value of Gamma_2 nor excludes a different weight family.

## 12. Source confirmation revision

The complete delta from the original dd6c1918 submission to source revision f6ec13924fe54880a968d5bb5e9140c7200c40c3d262ba5554ddf6d523e76706 was read. It changes the status line and adds Section10 recording A2882-A2885. Every equation and hypothesis is unchanged. Its statement that its own files did not read or rerun the two supplementary check logs is consistent with this independent audit, which did read them. The old pending-review wording is explicitly identified as historical.

The coordinator's subsequent degree correction, retained in the report-transfer review, replaces cubic by quadratic for735+8676q-43524q^2 and adds the revision time. This repairs the harmless typo identified in Section10 above; it does not change any identity or positivity argument.

## 13. Further Theory Agent C  comparison and an ineffective diagnostic

The complete Theory Agent C  comparison dated04:04:05, both associated Python scripts, the full57-check log and the6000-sample stress log were read. This is a further existing configured model comparison; actual provider execution remains independently unattested. None of those scripts was rerun here, and their runtime is not our computation time.

Its algebraic reconstruction agrees with Sections1-11. The additional exact upper bound for tr(B0)tr(B0 inverse), under B>=3I/22 and tr B=1, is correct. Write the eigenvalues of B0=B-I/100 as x_i>=a=139/1100, with sum t=97/100. The convex function sum1/x_i on this compact simplex reaches its maximum at a vertex: two x_i=a and the third t-2a=789/1100. Hence the maximum product is

    t(2/a+1/(t-2a))=1832039/109671<49.

The proof already uses the weaker valid bound3201/139<49, so this observation changes no hypothesis or theorem. The factorization Z(q)-81=(403/2)(2-3q)(6q-1)^2 is consistent with the exact root range. The additional sampled minima and alternative decimal root test remain numerical diagnostics, not a replacement for the rational Bernstein certificate.

One of the57 reported checks is ineffective. The line named “(16) completed square symbolic in (s,p,r,h) with p^2=r s^3” asks only whether an expanded SymPy expression is unequal to None. Any ordinary returned expression passes, even a nonzero residual. It supplies no identity verification. The separate immediately following check, named “(16) residual = S*(branch)/3 after P^2 = r S^3”, does compare a simplified residual with zero and verifies the needed symbolic relation. Thus deleting the ineffective line leaves56 substantive recorded checks, several of which are explicitly floating spot checks rather than exact checks. The script also prints SOME FAIL without exiting nonzero if a rec condition fails. Its current log has no recorded failure; an exit-zero result by itself would not prove that future checks pass. This is a diagnostic defect, not a defect in the already independently confirmed theorem or its98-check rational certificate.

The stress test reports6000 sampled fields, including2000 perturbed equality-family fields, no sampled pairing above its1e-12 tolerance, and equality-family roundoff of order1e-15. Its output and code agree on that finite sampling scope. No continuum claim, rigorous numerical minimum, exactness of a floating transformed field, or proof of optimality follows. The exact equality-family statement remains the analytic statement in Section11.

## 14. A denominator typo in the later report comparison

The complete Theory Agent C  report comparison dated04:05:50 and its one-line2625-assertion log were read. The report-scope observations agree with the approved assembly and retain the previously identified optional zero-function qualification. Its equality-family sentence, however, writes h=(3mu/2)abd/s^2. With the source notation s=a^2+b^2+d^2, the correct expression is h=(3mu/2)abd/s. This follows directly from the completed square in Section4 and from degree-one scaling in a,b,d.

For a=2, b=d=-1, s=6 and mu=26/31, the correct value is h=13/31; the later note's formula gives h=13/186. The completed-square pairing at that latter value is

    -2(1+2g)(13/186-13/31)^2<0,    g=3/25,

so it is not an equality field. The earlier Theory Agent C  source comparison and script both use the correct denominator. This is confined to the later explanatory note and does not alter the report or A2882-A2884. The current report already contains the required zero-function alternative in the theorem; making its method clause explicit remains a useful wording repair, not a new hypothesis.

## 15. Further Theory Agent A  comparison and its diagnostic scope

The full A97 comparison, repaired script and complete 47-item output were read. The mathematical comparison agrees with Sections1-10: it reconstructs the same pairing, normal block, determinant and strict cone step. The exact root-count checks of A0, B0 and T0 corroborate the already independently verified Bernstein certificate. The stronger cone bound is the same convexity calculation in Section13. The finite random samples are numerical corroboration only. The repaired cross-product line now uses the correct symmetric matrix E12+E21 and tests all three components; the earlier ineffective predicate is disclosed in the source note, not accepted as verification here.

Two remaining diagnostic descriptions require qualification. First, the item labelled max of r(q) on [0,2/3] checks only the two displayed values. It does not test maximality. The mathematical maximum is nevertheless true: for r=q(1-2q)^2/4, r'=(1-2q)(1-6q)/4. Check the interval endpoints and critical points q=1/6,1/2 to obtain the stated maximum1/54. Second, the printed identity Z-81=(10881/2)(1/54-r) is false: the coefficient is21762. At q=0, its left side is403 and the displayed right side is403/4. The actual predicate includes an additional factor4 and tests the correct identity. This is a diagnostic label defect, not a false algebraic result in the proof or report.

The script's zeta lower-bound item mixes a root count and a finite floating grid; neither the grid nor a raw total root count proves a global sign without the sign logic. Here the explicit factorization from Section13, Z-81=(403/2)(2-3q)(6q-1)^2, proves the bound. The pure-xyz zero claim is justified by the analytic sign argument already in Section7, independently of the computer solver's completeness. The final script only prints RESULT FAIL if a condition fails; it does not set a failing process status. Its current output says PASS. No fresh computation was run by the auditor, and no claim of independent execution is made.

This comparison continues the existing configured model file exchange; provider execution remains independently unattested. The source snapshots and real capture time are retained under in the team records.

## 16. A98 repairs of the polynomial diagnostic

The full A98 note, revised script and complete output were read and retained without rerunning. The script now has a failing exit status whenever a recorded condition is false. Its two exact factorizations are

    1/54-r(q)=(6q-1)^2(2-3q)/108,
    Z(q)-81=21762(1/54-r(q))=(403/2)(6q-1)^2(2-3q).

Together with0<=q<=2/3 and r(q)=q(1-2q)^2/4, these prove the complete range0<=r<=1/54, including equality only atq=1/6 or2/3 for the upper bound. Thus9<=zeta<=22 follows fromZ=484-21762r. The derivative ofmu=26/(22+zeta) is negative, giving the displayed range13/22<=mu<=26/31. The exact negative leading coefficient ofP(k), with its positive endpoint values, gives positivity on the full interval. These repairs replace the earlier point checks and sampled zeta assertion with explicit algebra and sign reasoning.

The smaller-root comparison remains a two-point numerical diagnostic; its universal branch identification is supplied by the proof's rationalized quadratic formula. The random4000-field and300-perturbation checks remain numerical only. The script's real-solution filter is not needed for the pure-xyz exclusion, which has the direct sign proof in this audit. The output contains46 PASS-labelled conditions plus the overall RESULT PASS, rather than47 separate conditions as the note says. It contains no reported failed condition. A98 also corrects the earlier note's04:10 label to04:09 or earlier; only the actual capture times of this audit are independently established. None of these diagnostic repairs changes A2882-A2884.

## 17. Repaired Theory Agent C  diagnostic

The complete difference from the already read Theory Agent C 343 script to its rev58 v2 and its full57-condition log were read. The vacuous !=None condition is removed. A new free-symbol identity checks both k and delta squared against the weight matrix. Every condition now has a class, and a failed condition exits with status1. The reported count is30 symbolic identities,3 complete linearity checks,19 exact finite statements,2 exact example checks and3 finite floating samples. The last class and the separately printed sampled minima remain numerical evidence only. The entry's equality offset is corrected to h=(3mu/2)abd/s; its prior erroneous s^2 text remains in the archived copy. These repair A2891 and A2893 without altering A2882-A2884. No script was rerun here.
