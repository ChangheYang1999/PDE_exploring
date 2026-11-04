# Primary Hardy-Leray statements and the infinite-moment localization

## 1. Statement, notation and scope

For 0<beta<1 set

    gamma=1-beta/2, t=(beta-3)/2, k=(beta+1)/2,
    H_beta=t^2+2-4beta/(2+k^2)=t^2(k^2+4)/(k^2+2).

Here Du is the Cartesian derivative and |Du| is its Frobenius norm. This audit confirms the exact statements on the selected primary theorem pages and their coefficient conversion in this parameter range. It is not an independent proof of each full source theorem in every dimension or parameter range. The separate three-dimensional localized theorem is proved in the team records and confirmed in A3125-A3126.

All four retained primary sources have the target coefficient H_beta. Their function classes are materially different from a general decaying Euler profile with infinite weighted energy. No new Hardy constant is claimed.

## 2. Costin-Mazya: full axisymmetry

In the retained arXiv math/0703116v2 manuscript, Theorem1 on printed page2 assumes n>2, gamma!=1-n/2 and a divergence-free axisymmetric u in C_c^infinity(R^n;R^n). It requires u(0)=0 when gamma<1-n/2. Its inequality is written with the opposite orientation from our convention:

    int r^(2gamma-2)|u|^2 <= C_(n,gamma) int r^(2gamma)|Du|^2.

For gamma<=1 it states

    C_(n,gamma)=4/(2gamma+n-2)^2
                *[1-2/(n+1+(gamma-n/2)^2)].

Corollary1 gives, for n=3 and gamma<=1,

    C_(3,gamma)=(gamma+1/2)^(-2)
                *[2+(gamma-3/2)^2]/[4+(gamma-3/2)^2],

and for gamma>1 gives C_(3,gamma)=1/[(gamma+1/2)^2+2]. The excluded gamma=-1/2 is inherited. We use only gamma in (1/2,1), where no extra condition at the origin is required. Its reciprocal equals H_beta. The separate n=2 theorem is not used, and the full axisymmetry premise is not discarded.

## 3. Hamamoto-Takahashi: axisymmetric swirl

The retained arXiv1904.01338v1 manuscript defines D_gamma as C_c^infinity(R3;R3), with u(0)=0 if gamma<=-1/2. In spherical coordinates about one fixed axis, write u=u_r e_r+u_theta e_theta+u_phi e_phi.

Theorem2 on printed pages2-3 first assumes div u=0 and u_phi=0, without requiring the other components to be independent of the azimuth. It states

    int r^(2gamma)|Du|^2 >= C_(gamma,0) int r^(2gamma-2)|u|^2,
    C_(gamma,0)=(gamma+1/2)^2+2
       +min_(x>=0)[x+8(gamma-1)/(x+2+(gamma-3/2)^2)].

For gamma in (1/2,1), the derivative of the bracketed expression is

    1-8(gamma-1)/(x+2+(gamma-3/2)^2)^2 > 0.

Its minimum is therefore at x=0, giving H_beta. For a fixed nonzero azimuth-independent swirl g e_phi in D_gamma, the same theorem states the sharp constant among divergence-free fields with that prescribed swirl as

    min{C_(gamma,0),
        int r^(2gamma)|D(g e_phi)|^2 /
        int r^(2gamma-2)|g e_phi|^2}.

Corollary3 assumes only that u_phi is independent of azimuth, and gives the reciprocal of the Costin-Mazya three-dimensional coefficient. The two meridional components may depend on azimuth. Thus this is weaker than full axisymmetry, but is still a restriction not available for every target profile.

The retained bytes display both an arXiv v1 date of April2,2019 and an internal manuscript date of August9,2021. This audit records both observations without inferring a publication-priority chronology.

## 4. Hamamoto's earlier nonsymmetric three-dimensional theorem

The OCAMI author manuscript has a repository cover dated2019 and an associated Nonlinear Analysis DOI10.1016/j.na.2019.111634. Theorem2 on printed page2 assumes u in C_c^infinity(R3;R3), div u=0, real gamma, and u(0)=0 if gamma<=-1/2. It removes Theorem1's axisymmetry assumption and keeps the coefficient

    C_gamma=(gamma+1/2)^2
             *[4+(gamma-3/2)^2]/[2+(gamma-3/2)^2], gamma<=1,
    C_gamma=(gamma+1/2)^2+2, gamma>1.

The inequality has gradient energy on the left and C_gamma times velocity energy on the right. At our gamma this is exactly H_beta. This manuscript is distinct from the Hamamoto-Takahashi paper. The final publisher version has not been read here, so textual identity of that version is not asserted.

## 5. Hamamoto2023: the finite weighted norm

The retained arXiv2305.12177v1 manuscript defines D_gamma(R^N), N>=3, as the smooth fields with

    int_RN (|Du|^2+|u|^2/r^2) r^(2gamma) < infinity.

Theorem1.1 on printed page3 assumes u in that space and div u=0, with no symmetry premise. Its sharp constant, formula(1.2), is

    C_(N,gamma)=(gamma+(N-2)/2)^2
      +min{N-1, 2+4(N-1)(gamma-1)/(N-1+(gamma-N/2)^2)}.

It states equality only for u=0 within that finite-norm class. For N=3 and gamma=1-beta/2, the second branch is smaller than2, gamma+1/2=-t, and gamma-3/2=-k. This gives H_beta. The algebraic identity k^2-t^2=2beta-2 also yields the equivalent rational expression in Section1, proving consistency with the earlier formulas. No numerical minimization is needed in our range.

The source cites a separate2021 density argument. That paper and the full all-dimensional proof are not independently certified in this review.

## 6. Why the profile application requires another proof

Let U in C1(R3;R3) be divergence-free and define E(R)=int_(|y|<R)|U|^2. Assume E(R)/R^beta -> L>0. Integration by parts, valid for the C1 energy function, gives

    F(R):=int_(1<|y|<R) r^(-beta)|U|^2
       =R^(-beta)E(R)-E(1)+beta int_1^R r^(-beta-1)E(r)dr.

Hence F(R)=beta L log R+o(log R). Under the stronger E(R)=LR^beta+O(R^(beta-1)), the remainder here is O(1). In both cases the global lower-order norm in the primary theorem is infinite. Compactly supported fields also cannot have L>0. Multiplication by a radial cutoff is not enough to repair this: div(chi(r)U)=chi'(r)U_r need not vanish.

The confirmed A3125 proof resolves that precise issue by a full vector spherical-harmonic decomposition and cutoff integration by parts whose errors use only velocity energy on fixed-width logarithmic annuli. It yields

    int_(1<|y-a|<R)|y-a|^(2-beta)|DU|^2
       >= beta H_beta L log R-C_a

under the precise energy law at a fixed center a, and the corresponding liminf under a ratio law. A smooth control attains this logarithmic coefficient with an infinite weighted norm, so there is no contradiction with the source's finite-norm equality statement. The control fails the full Euler profile equation. This is not an Euler counterexample or an automatic integrability theorem.

The application to the full rotating PDE uses the separately confirmed profile energy law, with beta=5-2/c for 2/5<c<1/2, and its pressure hypotheses. The source papers alone do not prove that application or eliminate arbitrary non-axisymmetric rotating profiles.

## 7. Exact reading and evidence record

The four complete PDFs and extracted texts are retained in `formal_sources/`; the hashes and actual source-agent HTTP retrieval records are in the team records. Retention of a full PDF does not imply a full reading.

Our actual coverage is: Hamamoto2023 printed pages1-3 and the beginning of4 in extracted text, with rendered pages2,3 inspected; Hamamoto2019 cover and extracted lines1-190 through the start of printed3, with rendered printed1,2 inspected; Costin-Mazya extracted lines1-155 through the start of printed3, with rendered page2 inspected; Hamamoto-Takahashi extracted lines1-245 through the start of printed4, with rendered pages2,3 inspected. The source agent reports fuller readings, but those are not claimed as this auditor's work.

The complete source scope note was read. The existing configured model coordinator comparison of LIT378 checks the target coefficient against the2023 rendered theorem pages; its analytic argument was independently checked in A3125-A3126. Actual provider execution is independently unattested. No new model client, build or mathematical computation was used here.

Two fresh web metadata templates were written without any supporting returned web tool message. Both are WITHDRAWN_INVALID, and their original bytes are preserved. This review certifies no fresh web retrieval. Neither template, abstract nor landing-page metadata is used to establish a theorem. The source formulas and classes in Sections2-5 depend only on the retained actual PDF pages and the stated readings. The source-agent HTTP retrieval records are separately retained; they are not this auditor's retrieval events.
