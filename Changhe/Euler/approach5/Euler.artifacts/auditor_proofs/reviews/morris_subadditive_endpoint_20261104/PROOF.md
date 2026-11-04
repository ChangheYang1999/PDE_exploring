# Two finite-estimate repairs in the discrete subadditive source

Status: A2778 and A2780 REFUTE the two printed finite estimates only. A2779, A2781 and A2782 CONFIRM the repaired lemmas and discrete attained-maximum theorem. A2783 CONFIRMS the same two errors on the inspected pages of the separate author-hosted copy. No continuous-flow theorem is inferred from discrete attainment alone.

## 1. Exact source and statement

The source inspected is the actual arXiv:1109.4615v1 manuscript by Ian D. Morris, dated 21 September 2011, with PDF SHA256 a419195fb0f988aa195bd60015026b384be426ecf529b62c5c01a572458e02c5. Its printed pages23 and26 were visually inspected, not inferred only from extracted text. The existing archive has an older filename containing2013; this is not evidence of a journal version. No later version or entire-paper audit is claimed.

Let X be a nonempty compact metric space, T:X->X continuous, and f_n:X->R union {-infinity}, n>=1, upper semicontinuous. Suppose

    f_(n+m)(x)<=f_n(T^m x)+f_m(x).

Put f_0=0. Fix x with f_n(x)/n tending to c in R union {-infinity}, and let

    mu_n=(1/n) sum_(j=0)^(n-1) delta_(T^j x).

Then every subsequential weak limit mu is T-invariant and

    inf_(m>=1) (1/m) integral f_m dmu >= c.                  (1)

This is the source's Lemma A.6. Each f_m is bounded above on compact X, so its integral is well-defined, possibly minus infinity. Sections2-5 prove the lemma with the corrected index. Section6 supplies a second repair, in the proof of Fekete's lemma A.1. Section7 checks that the attained-maximum theorem A.3 survives both repairs.

## 2. The false finite identity on page26

For fixed n>=m and 0<=i<m, write

    n=i+q_i m+r_i, 0<=r_i<m.

The pairs (i,j) with 0<=i<m and 0<=j<q_i correspond exactly to integers k=i+jm with 0<=k<=n-m. The forward implication follows from

    i+(q_i-1)m=n-r_i-m<=n-m.

For the reverse implication, take the residue i of k modulo m and j=(k-i)/m. The inequality k+m<=n implies j+1<=q_i.

Thus the correct identity is

    sum_i sum_(j=0)^(q_i-1) f_m(T^(i+jm)x)
      =sum_(k=0)^(n-m) f_m(T^k x).                          (2)

The printed right endpoint n-m+1 is too large by one. On the singleton space with T the identity and f_n=n, take n=5,m=2. The i=0 block contains k=0,2 and the i=1 block contains k=1,3. The left side is 8, whereas the printed sum through k=4 is10. This exact countertest refutes the finite identity, not Lemma A.6.

Every related occurrence of the endpoint in that decomposition must be repaired. The terminal terms needed to recover the full empirical sum then have positions n-m+1,...,n-1, or T^(n-ell)x for 1<=ell<=m-1. In particular there are m-1 terminal terms, with an empty sum when m=1.

## 3. Finiteness and control of terminal terms

If c=-infinity, inequality (1) is automatic once invariance is proved. Assume c is finite. Every f_i(x) is then finite: otherwise subadditivity and boundedness above would force f_n(x)=-infinity for every n>i, contradicting the finite limit.

Fix k,ell>=1. For n sufficiently large, subadditivity gives

    f_(n+k-ell)(x)-f_(n-ell)(x)
      <=f_k(T^(n-ell)x)<=sup_X f_k.

Both terms on the left are finite. Dividing by n, their difference tends to zero because each divided by n tends to c. The finite upper bound divided by n also tends to zero. Consequently

    f_k(T^(n-ell)x)/n -> 0.                                 (3)

The same bounds show that these orbit values cannot equal minus infinity. No lower bound for f_k on the whole space is needed.

## 4. Corrected block estimate

Repeated subadditivity in the i-th residue class gives

    f_n(x)<=f_i(x)+sum_(j=0)^(q_i-1)f_m(T^(i+jm)x)
                        +f_(r_i)(T^(n-r_i)x).

Summing over i and using (2),

    m f_n(x)<=sum_(i=0)^(m-1) f_i(x)
             +sum_(k=0)^(n-m)f_m(T^k x)
             +sum_(i=0)^(m-1)f_(r_i)(T^(n-r_i)x).           (4)

For fixed m, the first sum divided by nm tends to zero. The same is true of the last sum: r_i takes only finitely many values; positive values are covered by (3), and r_i=0 contributes zero. Rearranging (4) and using f_n(x)/n->c therefore gives

    liminf_n (1/(nm))sum_(k=0)^(n-m)f_m(T^k x)>=c.

The m-1 omitted terminal terms have normalized limit zero by (3) with k=m and ell=1,...,m-1. Hence

    liminf_n (1/m)integral f_m dmu_n>=c.                    (5)

This argument is valid also for m=1.

## 5. Invariance and upper semicontinuity

For every continuous real h,

    integral(h o T-h)dmu_n=[h(T^n x)-h(x)]/n -> 0.

Continuity of h and T lets this identity pass to a subsequential weak limit mu, proving invariance.

For an upper semicontinuous f bounded above and possibly minus infinity, choose continuous real g_j decreasing pointwise to f on X. Such approximations exist on a compact metric space, for example by truncation followed by decreasing Lipschitz upper approximations. For each j, weak convergence gives

    limsup_k integral f dmu_(n_k)
      <=lim_k integral g_j dmu_(n_k)=integral g_j dmu.

Monotone convergence after subtracting a common finite upper bound gives integral g_j dmu decreasing to integral f dmu. Thus

    limsup_k integral f dmu_(n_k)<=integral f dmu.           (6)

Combine (5) and (6) with f=f_m. Each normalized integral at mu is at least c. Taking the infimum proves (1), including its extended-value scope.

## 6. A second finite-estimate repair on page23

The source's proof of Lemma A.1 chooses lambda>inf_n a_n/n and m with a_m<=m lambda, writes n=q_n m+r_n, and gives the upper bound n lambda+r_n a_1. That last bound is not valid for arbitrary negative lambda.

Take a_n=-n, lambda=-3/4, m=2 and n=3. This additive sequence meets every premise and a_m=-2<=-3/2=m lambda. But

    q_n a_m+a_(r_n)=-3
    n lambda+r_n a_1=-13/4,

so the asserted inequality -3<=-13/4 is false. The missing remainder term is -r_n lambda.

Here is the complete correction. If any a_m=-infinity, subadditivity makes all a_n with n>m equal minus infinity and Fekete's conclusion follows. Otherwise every a_n is finite. Set a_0=0, choose lambda and m as above, and use

    a_n<=q_n a_m+a_(r_n)
        <=n lambda+[a_(r_n)-r_n lambda]
        <=n lambda+C_(m,lambda),

where C_(m,lambda)=max_(0<=r<m)(a_r-r lambda) is finite. Divide by n and let n tend to infinity, obtaining limsup a_n/n<=lambda. Since lambda is arbitrary above the infimum, the limit equals inf_n a_n/n, possibly minus infinity.

Equivalently, when using a_r<=r a_1, the corrected printed expression is n lambda+r_n(a_1-lambda). This repair changes no limit conclusion. It is separate from the page26 index repair submitted as LIT325.

## 7. Why the attained-maximum theorem remains valid

Write a_n=sup_X f_n and b=lim_n a_n/n=inf_n a_n/n, using the repaired Fekete lemma. The invariant probability measures form a nonempty compact convex set M_T, by the empirical-limit argument. For mu in M_T, let

    F(mu)=inf_n (1/n)integral f_n dmu
         =lim_n (1/n)integral f_n dmu.

The equality is again Fekete, now for the invariant integral sequence. Equation (6) makes F upper semicontinuous, so it attains a maximum beta. Also beta<=b.

For finite b there is a point z with f_n(z)>=nb for every n. To prove this, suppose no such point exists. Upper semicontinuity and a finite open cover give epsilon>0, M>=2 and a choice r_1(x) in {1,...,M-1} with

    f_(r_1(x))(x)<r_1(x)(b-epsilon).

No measurability of this choice is needed. Define r_(k+1)(x)=r_k(x)+r_1(T^(r_k(x))x). Induction using subadditivity gives

    k<=r_k(x)<=k(M-1),
    f_(r_k(x))(x)<r_k(x)(b-epsilon).

Set ell_k(x)=kM-r_k(x), so k<=ell_k(x)<=k(M-1), and b_k=sup_(n>=k)a_n/n. Then b_k decreases to b and

    f_(kM)(x)
      <=r_k(x)(b-epsilon)+ell_k(x)b_k
      <=kM b-k epsilon+k(M-1)(b_k-b).

Taking the supremum over x, dividing by kM and letting k tend to infinity contradicts a_(kM)/(kM)>=b. This proves existence of z. Squeezing f_n(z)/n between b and a_n/n gives its limit b. The corrected Lemma A.6 applied at z supplies an invariant mu with F(mu)>=b. Hence beta=b. If b=-infinity, beta=b already and every point has inf_n f_n(x)/n=-infinity.

The maximizing measures form a compact convex face of M_T. Indeed F is affine in the extended sense because it is the limit of normalized invariant integrals, all bounded above uniformly; no positive infinity occurs. If beta is finite, a proper convex combination can attain beta only when both constituents do. If beta=-infinity, all of M_T is maximizing. A nonempty compact convex face has an extreme point, and the extreme invariant probability measures are precisely the ergodic ones. These standard compact-convex and invariant-measure facts give an ergodic maximizer. This identifies the supremum over ergodic measures with beta, with attainment.

Finally

    beta<=inf_n sup_(mu in M_T) (1/n)integral f_n dmu<=b

gives the remaining minimax equality. Each fixed-n supremum over X or M_T is attained by upper semicontinuity and compactness. The pointwise supremum of inf_n f_n(x)/n is attained at z when b is finite, and at every point when b=-infinity. Every infimum other than the pointwise one is a Fekete limit, because the corresponding scalar sequence is subadditive. This proves the exact A.3 statement used in the source discussion, with both finite-estimate repairs in place.

## 8. Verification and remaining scope

All six original LIT325 sections were read; all eight sections of the updated submission were subsequently read. The actual source text from the AppendixA setup through the complete A.3 proof was read, including A.1-A.8. Printed page26 was inspected from the retained rendered image; printed page23 was rendered locally and inspected to check the second error. No new network retrieval or mathematical computation was needed.

Section7 uses the standard fact that a nonempty compact convex set has an extreme point and the characterization of ergodic invariant measures as extreme points. Neither is a new claim of this campaign. The source's Corollary A.8 was read but is not asserted or needed by this audit.

This is a discrete-map result. The report's full-flow attainment still requires the additional normalized-derivative argument A2721/A2733 or the averaging argument A2731. The two source repairs do not alter those independent arguments, do not remove any Euler hypothesis, and do not resolve the unrestricted conjecture.

## 9. Completed comparison and separate author copy

The six-item existing coordinator comparison and both wording points were read in full. All eight entries of its exact-arithmetic log were inspected, not rerun. Its finite checks agree with Sections2 and6; the independent limiting and attained-maximum arguments are Sections3-7 above. The coordinator explicitly did not reread the entire A.3 proof in the PDF; this audit did read the actual source text from the AppendixA setup through the complete A.3 proof. No agreement beyond those scopes is claimed.

The updated eight-section source has SHA256 dbccff2e4c3f9038b3bcdada1164fa086d6b341fcdabc9b2fcb522d5156f5aca. Its Section8 records a separate author-hosted PDF with SHA256 0fc26afd823d023a50e193ac346ebcabddb6d64130e0e4cbdbf9eb2ed5390de3 and 486663 bytes. The retained retrieval record was read. This audit read its complete printed pages23,25,26 and visually inspected the rendered pages23 and26. Both errors are present on those pages. The PDF metadata gives July2011; the author page's association with a 2013 journal article does not identify the linked file as the final journal version. No whole-paper comparison or claim about an unavailable typeset journal text follows.

The source addition and comparison are retained under verification. The exact time and hashes are in the team records there. The report may note both repairs without changing its independent full-flow proof or any Euler hypothesis. Existing configured model collaboration was through the coordinator's files; its actual provider execution was not independently attested.


## 10. Source status revision

The complete delta from the archived submission to current source SHA256 c40a24fb3d0723c7d8722f545cb7f45c2941df1ed4f417bfc941c293942a47d2 was read. The revision changes status, dates the earlier pending statement, and adds Section9. It preserves both finite repairs, every source-version limitation, and the distinction between the discrete theorem and the independent continuous-flow argument. No proof equation changes.

All added reading-scope statements distinguish this audit from the submitting agent's own reading. The retained delta and hashes are in the team records and in the team records. This revision needs no new mathematical computation.
