# Checked literature on Hölder constants

This is a source ledger, not a claim that every relevant publication has been found. Statements below were read in primary-source texts, either saved locally or inspected in the web tool as explicitly recorded. Search titles and abstracts alone are not used as theorem evidence. The investigation concerns only singular-integral Hölder estimates; applications discussed by the sources are outside this project.

## Exact Hilbert-transform information

**V. F. Babenko, *Sharp Estimates for Norms of Functions from Conjugate Classes in Metrics C and L*, arXiv:1402.0829v1 (2014 upload).** The first-page footnote identifies the original Russian publication as a 1973 collection, pages 3–5. Saved source: `sources/conjugate_sharp_2014.pdf` and `.txt`. Source URL: `https://arxiv.org/abs/1402.0829`.

Theorem 1 assumes a concave modulus of continuity $\omega$ satisfying a Dini condition $\int_0^\varepsilon\omega(t)t^{-1}dt<\infty$. For the periodic conjugate function with kernel $-(2\pi)^{-1}\cot((t-x)/2)$, part (2) states the exact maximal increment

$$\sup_{f\in H^\omega}\max_x|\widetilde f(x+h)-\widetilde f(x)|
=\frac2\pi\int_0^{h/2}\frac{\sin(h/2)}{\cos u-\cos(h/2)}
\omega(\rho(u)-u)\,du,$$

where $\rho$ is specified by matching the integrated positive and negative kernel masses. The source also asserts attainment of its extremal relations. Direct integration gives $\tan(\rho(u)/2)\tan(u/2)=\tan^2(h/4)$. This is an **exact periodic modulus theorem**, not merely qualitative boundedness.

The independent proof in `hilbert_exact/PROOF.md` derives the corresponding real-line seminorm

$$N_\alpha=\frac{2^{1-\alpha}}\pi B((1-\alpha)/2,\alpha),\qquad 0<\alpha<1,$$

with an explicit admissible extremizer. It does not assume a periodic-to-nonperiodic limiting argument. Neither formula is asserted to equal a two-dimensional Riesz or Beurling norm.

## Beurling transform: exact hypotheses, unspecified constants

**J. Mateu, J. Orobitg, J. Verdera, *Extra cancellation of even Calderón-Zygmund operators and quasiconformal mappings*, arXiv:0802.1185v2; J. Math. Pures Appl. 91 (2009), 402–431.** Saved as `sources/mov.pdf` and `.txt`. URL: `https://arxiv.org/abs/0802.1185`.

The Main Lemma, source page 8, assumes a bounded domain with $C^{1+\varepsilon}$ boundary, $0<\varepsilon<1$, and an even homogeneous convolution kernel with a $C^1$ angular part of mean zero. It proves

$$\|T(f\chi_\Omega)\|_{\operatorname{Lip}(\varepsilon,\Omega)}
\le C\|T\|_{CZ}\|f\|_{\operatorname{Lip}(\varepsilon,\Omega)},$$

and the analogous exterior-domain estimate. The source's norm includes the supremum norm. Its $C$ depends on dimension, exponent, and domain; it is not given numerically. “Precise form” here means explicit dependence on the kernel seminorm, not a sharp numerical Hölder norm. Classification: **qualitative domain boundedness with tracked parameter dependence**. The even-kernel cancellation on balls is useful structurally.

**E. Doubtsov, A. V. Vasin, *Restricted Beurling transforms on Campanato spaces*, arXiv:1604.07670v1.** Saved as `sources/1604.07670.pdf` and `.txt`. URL: `https://arxiv.org/abs/1604.07670`.

Theorem 1 restates restricted Beurling boundedness on $\Lambda^\alpha(\Omega)$ for bounded $C^{1+\alpha}$ domains. Proposition 2, attributed to Vasin, assumes a Dini modulus and a bounded $C^{1,\omega}$ domain, and maps $\Lambda^\omega$ to $\Lambda^{\widetilde\omega}$ with

$$\widetilde\omega(x)=\int_0^x\frac{\omega(t)}t\,dt+x\int_x^1\frac{\omega(t)}{t^2}\,dt.$$

For $\omega(t)=t^\alpha$, this is exactly $x^\alpha/\alpha+(x^\alpha-x)/(1-\alpha)$. The paper's notation equating the power moduli refers to equivalence of regularity classes, not equality of these scalar functions. Theorem 3 proves boundedness on its Campanato space for regular moduli and bounded $C^{1,\omega}$ domains. Constants are unspecified. Classification: **qualitative boundedness and an explicit modulus transformation**, not a sharp operator constant.

**V. Cruz, X. Tolsa, *Smoothness of the Beurling transform in Lipschitz domains*, arXiv:1201.5385v1.** Saved as `sources/1201.5385.pdf` and `.txt`. URL: `https://arxiv.org/abs/1201.5385`.

Theorem 1.2 assumes a $(\delta,R)$-Lipschitz or special $\delta$-Lipschitz domain, $1<p<\infty$, $0<\alpha<1$, and $\alpha p>1$. Besov regularity $B^{\alpha-1/p}_{p,p}$ of the outward normal implies $B\chi_\Omega\in\dot W^{\alpha,p}(\Omega)\cap\dot B^\alpha_{p,p}(\Omega)$, with a bound depending on $p,\alpha,\delta,R$ where relevant. Theorem 1.1 treats one derivative. Its sharpness concerns regularity assumptions on the boundary, not a numerical whole-plane Hölder norm. Classification: **sharp regularity threshold, unspecified norm constant**.

**X. Tolsa, *Regularity of C1 and Lipschitz domains in terms of the Beurling transform*, arXiv:1201.5403v1.** Saved as `sources/1201.5403.pdf` and `.txt`. URL: `https://arxiv.org/abs/1201.5403`.

Theorem 1.1 is a converse domain-regularity result under a sufficiently small Lipschitz slope, with $0<\alpha\le1$ and $\alpha p>1$. It controls the normal's Besov seminorm by a Sobolev norm of $B\chi_\Omega$ plus a boundary-length term. The constants are not numerical. Classification: **domain regularity characterization**, not an estimate for the requested sharp seminorm.

## Schauder and misleading title matches

**P. Fife, *Schauder estimates under incomplete Hölder continuity assumptions*, Pacific J. Math. 13 (1963), 511–550.** Saved as `sources/schauder_incomplete_1963.pdf` and `.txt`. DOI: `10.2140/pjm.1963.13.511`.

Section 2, Theorem 2.1 treats integral operators with explicit kernel-size and integrated-cancellation hypotheses and gives a partial Hölder estimate. The resulting constant $C_3$ depends on the kernel constants, dimensions, and exponent, but is not evaluated. Section 3 applies the estimate to fundamental-solution derivatives. Classification: **Schauder boundedness with unspecified constants**. It supplies no numerical improvement to the present explicit bound.

**R. Redheffer, *An inequality for the Hilbert transform*, Pacific J. Math. 37 (1971), 181–212.** Saved as `sources/hilbert_inequality_1971.pdf` and `.txt`. DOI: `10.2140/pjm.1971.37.181`.

The read sections concern weighted $L^p$ inequalities for a modified Hilbert transform, including its behavior on functions that need not be integrable at infinity. This is a useful warning about normalization and convergence, but it is **not a sharp Hölder norm theorem**. No Hölder constant is attributed to it.

**R. Abreu-Blaya, J. Bory-Reyes, F. Brackx, H. De Schepper, F. Sommen, *Hölder norm estimate for a Hilbert transform in Hermitean Clifford analysis*.** Saved as `sources/hermitean_holder_2012.pdf` and `.txt`. DOI: `10.1007/s10114-012-0377-8`. Repository PDF: `https://biblio.ugent.be/publication/3079018/file/3079019.pdf`.

Theorem 2 concerns matrix-valued boundary transforms on a $d$-summable boundary in $\mathbb R^{2n}$, mapping exponent $\alpha$ to $\beta<(2n\alpha-d)/(2n-d)$. Its bound includes the diameter and a Whitney sum, as well as unspecified constants. Theorem 3 treats an Ahlfors-David regular boundary and again loses exponent. Classification: **different operator and geometry, unspecified constants**. The title is not evidence of a sharp classical real-line Hilbert seminorm.

## Further checked Schauder and Riesz references

**L. Marino, S. Menozzi, E. Priola, *Poisson process and sharp constants in Lp and Schauder estimates for a class of degenerate Kolmogorov operators*, arXiv:2107.06012v3.** Saved as `sources/schauder_poisson.pdf` and `.txt`.

Section 4.2 defines full anisotropic Hölder-Zygmund norms in (4.8). Under the paper's Kalman hypothesis, (4.9) assumes a Schauder estimate with an unspecified constant $C_\beta$. Equation (4.17) proves that adding a continuous nonnegative second-order perturbation preserves that same constant. Thus “sharp constants” refers to **preservation of an existing constant under perturbation**, not computation of its numerical value. It does not supply a numerical whole-plane seminorm bound for the present transforms. The exact formulas (4.8), (4.9), and (4.17), and their surrounding hypotheses, were read.

**J. Sauer, S. A. Smith, *Schauder estimates for germs by scaling*, arXiv:2412.01486v2.** Saved as `sources/schauder_germs.pdf` and `.txt`.

Theorem 1 assumes $0<\alpha<1<\eta<2$ and bounds a germ's $G^\eta$ norm by its Laplacian's $G^{\eta-2}$ seminorm and a compatibility seminorm. Theorem 4 extends this to a scaling-homogeneous elliptic constant-coefficient operator of order $m$, for noninteger $0<\alpha<\eta<m$. Both assert the existence of a constant, with no numerical formula. The first-page discussion explicitly identifies non-explicit constants as a limitation of the indirect scaling argument. Classification: **qualitative Schauder bounds in a different norm setting**.

## Remaining questions

A sharp finite-alpha whole-plane Beurling or second-order Riesz seminorm formula has not been established from the sources checked so far. This is an unresolved search result, not an assertion that the literature contains none. Further downloaded papers remain unclassified until their exact statements are read. The project theorems and certified numerical bounds rely on the independent proofs in the other topic folders.

## Additional primary statements checked

**J. García-Cuerva and A. E. Gatto, *Lipschitz spaces and Calderón-Zygmund operators associated to non-doubling measures*, arXiv:math/0212289v1.** Saved as `sources/garcia_cuerva_gatto.pdf` and `.txt`; source URL `https://arxiv.org/pdf/math/0212289`.

The measure is a Radon measure on $\mathbb R^d$ satisfying $\mu(B(x,r))\le Cr^n$ for $0<n\le d$. Definition 3.2 requires that the operator already be bounded on $L^2(\mu)$ and represented off the support by an $n$-dimensional standard kernel. The kernel has a size bound and first-variable Hölder regularity of exponent $\varepsilon$. Definition 3.4 extends it to Lipschitz functions modulo constants using a local truncation plus a convergent kernel difference at infinity. **Theorem 3.6**, on source page 6, states that for $0<\alpha<\varepsilon\le1$, such an operator is bounded on $\operatorname{Lip}(\alpha,\mu)$ if and only if $T(1)=0$ in that quotient space. No numerical operator bound is stated. Classification: **qualitative boundedness with a precise quotient-space formulation**. Omitting the pre-existing $L^2$ boundedness would enlarge the statement beyond the theorem read.

**Adrián González-Pérez, *Hölder classes via semigroups and Riesz transforms*, Math. Z. 301 (2022), 3245–3284, DOI `10.1007/s00209-022-02982-0`.** Saved as `sources/holder_riesz_semigroups.pdf` and `.txt`.

Theorem A uses the homogeneous semigroup seminorm $\sup_{s>0}s^{1-\alpha}\|\partial_sP_sf\|_\infty$, where $P$ is subordinate to a Markovian semigroup. Under $\Gamma^2\ge0$ and the derivation intertwining assumption stated immediately before the theorem and in (3.2), the Hilbert-valued transform $\delta A^{-1/2}$ is bounded on this semigroup Hölder class for $0<\alpha<1$. Corollary B gives classical metric Hölder boundedness of the gradient Riesz transform on a connected geodesically complete manifold of nonnegative Ricci curvature. The seminorm comparison in Corollary 4.4 is an equivalence, not an equality; Theorem 3.7 uses constants depending on $\alpha$ without numerical values. Classification: **qualitative first-order Riesz boundedness in semigroup and manifold settings**. It supplies no sharp planar second-order constant.

**V. Babenko, V. Babenko and O. Kovalenko, *Korneichuk–Stechkin lemma, Ostrowski and Landau inequalities, and optimal recovery problems for $L$-space-valued functions*, arXiv:2006.14581v1.** Saved as `sources/korneichuk_stechkin_2020.pdf` and `.txt`; source URL `https://arxiv.org/pdf/2006.14581`.

Lemma 8, source pages 8–9, assumes bounded positive-a.e. weights $\psi_1$ on $[a,a']$ and $\psi_2$ on $[b',b]$, where $a<a'\le b'<b$, with equal total masses. It defines a decreasing mass-matching map by $\int_a^s\psi_1=\int_{\rho(s)}^b\psi_2$. For functions with modulus of continuity at most $\omega$, the difference of the two weighted integrals is at most $\int_a^{a'}\psi_1(s)\omega(\rho(s)-s)\,ds$. For concave $\omega$ and an isotropic target $L$-space, including the scalar real line, equality holds; formula (9) gives an extremizer through integrals of $\omega'$ evaluated at matched distances. The second integral in printed formula (8) has reversed limits, an apparent typographical error; the first integral and the proof have the correct nonnegative orientation. Classification: **exact one-dimensional modulus transport theorem**. Application to singular or unbounded weights needs a separate limiting argument; the lemma itself assumes bounded weights on finite intervals.

Theorem 1 of the same paper gives a general upper bound using the Korneichuk rearrangement of a cumulative signed weight, under a finite one-sided-limits hypothesis. Its equality conditions require compatible extremal pieces and should not be assumed automatically for a multi-lobe circular kernel.

**A. A. Shcherbakov, *The Beltrami equation with parameters and uniformization of holomorphic foliations with hyperbolic leaves*, arXiv:1812.08851v1.** Saved as `sources/beltrami_parameters_2018.pdf` and `.txt`. Only the singular-integral estimates on pages 143–144 and their reference were inspected for this project.

Proposition 40 interpolates a uniform bound and a weighted Lipschitz bound to a weighted Hölder estimate. Proposition 41 gives weighted bounds for its parameter-dependent integral transform with an unspecified uniform constant. In the discussion of (7.80), the ordinary Beurling term is estimated by an unspecified constant depending on the Hölder exponent, referring to the Astala–Iwaniec–Martin book. No exact Beurling norm or numerical Schauder constant is stated there. Classification: **qualitative Hölder estimate; a citation chain to a book whose relevant statement has not yet been checked**. The source's applications are outside the present scope.


## Classical conjugate-function sources, checked 2026-10-28

**I. Priwaloff [I. I. Privalov], *Sur les fonctions conjuguées*, Bulletin de la Société Mathématique de France 44 (1916), 100–103, DOI `10.24033/bsmf.965`.** Saved source: `sources/privalov_1916.pdf` and `.txt`, retrieved from `https://www.numdam.org/item/10.24033/bsmf.965.pdf`. The catalog renders the initial as J.; the printed article says I.

The theorem on page 100 states that for conjugate harmonic functions on the unit disk, a boundary function satisfying a periodic angular Hölder condition of exponent 0<alpha<1 has a conjugate boundary function satisfying the same exponent. Pages 101–102 split at epsilon=3|h| and prove a bound with unspecified constants C1 and C2. At alpha=1 the proof gives C1|h|log(1/|h|)+C2|h|, hence every exponent below one. Pages 102–103 give an example showing that Lipschitz regularity itself need not be preserved. All four printed pages were read. Classification: **classical qualitative exponent preservation and the endpoint modulus, no sharp numerical constant**. An initial incorrect DOI suffix 962 retrieved an unrelated Barré paper; it is explicitly named `wrong_target_barre_1916` and is not evidence for this statement.

**C. A. Nolder, *Conjugate functions and moduli of continuity*, Illinois Journal of Mathematics31(4)(1987),699-709.** UNVERIFIED citation lead. Current local downloads are challenge HTML. The access claims in V153 are withdrawn by V154. No exact theorem from this source may be cited until a readable primary source is obtained.


**Periodic exact-norm corollary, independently checked.** The proof in `hilbert_periodic/PROOF.md` derives from Babenko's Theorem 1(2) the exact angular-geodesic seminorm norm N_alpha=2^(1-alpha) B((1-alpha)/2,alpha)/pi. It explicitly proves the tangent-substitution majorant and the limiting sharpness. The same value holds for complex inputs by real phase projection. This is not a claim about the chordal metric or a full norm. The source theorem, rather than an unproved transfer from the real line, is the dependency.

**Xu-Jia Wang, *Schauder Estimates for Elliptic and Parabolic Equations*, Chinese Annals of Mathematics B 27(6) (2006), 637-642, DOI `10.1007/s11401-006-0142-3`.** Saved primary PDF and text: `sources/wang_schauder_2006.pdf` and `.txt`, retrieved from the ANU repository. Theorem 1.1 and its proof on pages 637-639 were checked. For a C^2 solution of Delta u=f on B1 with Dini f, it bounds the Hessian modulus on B_(1/2) by C_n times d sup|u| plus the two standard Dini integrals. Equation (1.3) gives a full local Schauder bound with f's Hölder norm divided by alpha(1-alpha). The constant C_n is unspecified. Classification: **explicit exponent dependence, no numerical dimensional multiplier, and a local full-norm estimate**. This does not give a sharp whole-plane seminorm constant.

## Further checked boundary-operator statements (2026-10-28T04:12:16.955796+00:00)

Juan Jose Marin, Jose Maria Martell, Dorina Mitrea and Marius Mitrea,
*Characterizations of Lyapunov domains in terms of Riesz transforms and
the Plemelj-Privalov theorem*, arXiv:2604.19143v1, April2026.
Primary PDF: https://arxiv.org/pdf/2604.19143 . Theorem1.3(i), pages5-6,
was read in full. It assumes an Ahlfors regular domain in R^n, n>=2,
with compact boundary, a bounded doubling nondecreasing Dini modulus
omega vanishing at zero, and an odd C^2 divergence-free vector kernel
homogeneous of degree1-n. The generalized double-layer principal value
maps C^omega(boundary) boundedly into C^omega_Z(boundary), where
omega_Z(t)=integral_0^t omega(s)ds/s+t integral_t^diam omega(s)ds/s^2.
If omega_Z<=C omega it maps into C^omega. The theorem gives no numerical
operator norm. Its operators are on domain boundaries and have different
kernels and measures from the whole-plane second-order Riesz transforms.
It is a qualitative modulus-of-continuity comparison, not a value for
C_alpha or D_alpha. Local source: sources/marin_martell_mitrea_mitrea_2026.pdf.

Yifei Pan and Yuan Zhang, *Cauchy singular integral operator with parameters
in Log-Holder spaces*, arXiv:2001.03778v1, January2020.
Primary PDF: https://arxiv.org/pdf/2001.03778 . Definition1.1 and
Theorem1.2, pages1-2, were read. The slice Cauchy operator on D times a
parameter domain sends the stated C^(k,L^alpha Log^nu L) space into
C^(k,L^alpha Log^(nu+1)L), with C depending on the domain and indices.
The norm includes suprema of derivatives and the joint-variable modulus
|h|^alpha |log|h||^nu. The introduction assumes disjoint C^(1,alpha)
Jordan boundary components; the displayed Theorem1.2 uses C^(k,alpha)
boundary, k>=0. No attempt is made here to resolve that boundary-notation
issue at k=0, and no result from this source is used in our proof.
The claimed sharpness concerns the additional logarithmic regularity
loss under parameter dependence; its numerical constant is unspecified.
It is not a sharp Holder operator-norm result for the planar Beurling
transform. Only the singular-integral statement was investigated.
Local source: sources/pan_zhang_2020.pdf.


## Douglis boundary transforms, primary statement checked

**Y. Peña Pérez, M. P. Árciga Alejandre, R. Abreu Blaya, J. Bory Reyes, *Hölder norm estimate for the fractal Hilbert transform in Douglis analysis*, Journal of Inequalities and Applications (2017), article 213, DOI `10.1186/s13660-017-1488-7`.** The complete primary PDF is saved as `sources/douglis_holder_2017.pdf` with extracted text.

The operator acts on Douglis-algebra-valued functions on the Jordan boundary gamma of a planar domain. The paper uses the full generalized Hölder norm, the increment seminorm plus the supremum norm. Its majorants phi,psi belong to the Bari-Stechkin class defined in section 2.3. Write alpha_psi and beta_phi for the power comparison indices in Remark 1. Theorem 1 (page 7) assumes alpha_psi <= beta_phi and that gamma is h-summable, with h(t)=phi(t)^p t^(2-p), p=2/(1-alpha_psi). It constructs the boundary operator H*_gamma=2 C*_{gamma,+}-I and shows H*_gamma:H^phi(gamma) -> H^psi(gamma).

Theorem 2 (page 8) bounds its full norm by

    1+c1 phi(|gamma|)/psi(|gamma|)
      +c2 s(h)^((1-alpha_psi)/2) psi(|gamma|)
      +c3 s(h)^((1-alpha_psi)/2),

where |gamma| is the diameter and s(h) the Whitney sum. The constants c1,c2,c3 are not given numerically; the statement says they depend only on phi,psi. Theorem 3 (page 10) assumes a rectifiable boundary of length l and alpha_psi < 2 beta_phi - 1. It bounds the conventional boundary Hilbert transform by the same displayed expression with |gamma| replaced by l and s(h) replaced by l. For the power majorants phi(t)=t^alpha,psi(t)=t^beta, this condition reads beta<2alpha-1, so it loses exponent and requires alpha>1/2.

Classification: **a different boundary operator, full norms, explicit geometric factors but unspecified numerical constants**. These statements do not give a sharp real-line Hilbert seminorm or a planar Beurling/Riesz constant. The exact statements and definitions were read; no application to the present operator is inferred.

The distinct 2010 title *Hölder norm estimate for a Hilbert transform in Clifford analysis*, DOI `10.1007/s00574-010-0017-9`, was located through Crossref. Its Springer PDF endpoint returned an HTML page containing an abstract and a paywall. Saved as `sources/clifford_holder_2010.html` and extracted text. No theorem statement was available, so it remains **UNVERIFIED** and is not used as theorem evidence.

## Further exact-statement check (2026-10-28T05:43:43.296184+00:00)

Satyanad Kichenassamy, *Schauder-type estimates and applications*, Handbook of Differential Equations: Stationary Partial Differential Equations, volume3 (2006), pp401-464; author copy deposited as arXiv:2507.01818 in2025. Primary PDF: https://arxiv.org/pdf/2507.01818. The title page and sections3.1,3.3 were read. This is a2006 chapter, not a new2025 theorem. Theorem9 (PDFp25) states the second derivative formula for compactly supported C^alpha data on a bounded smooth domain: integral of the differentiated fundamental solution against f(Q)-f(P), minus the boundary term f(P) integral_boundary partial_i g n_j. Theorem10 (PDFp26, equation10) estimates the full sup-plus-Holder second-derivative norm on B_R by an unspecified C times sup|f|+R^alpha[f]_alpha on B_2R. Theorem13 (PDFp30) is a qualitative C^(2+alpha) conclusion with a Fourier-flatness hypothesis. Footnote2 (PDFp5) explicitly adopts variable unspecified constants and says their values are not the subject of the chapter. Thus this checked source supplies the familiar potential-theoretic mechanism, including the nonzero boundary correction, but no sharp or numerical constant for the present homogeneous whole-plane norm. Only these estimate statements were inspected; its applications were not studied. Local PDF/text and hash are in sources/holder_further_manifest.json.

Astala-Iwaniec-Martin, *Elliptic Partial Differential Equations and Quasiconformal Mappings in the Plane* (2009): the primary publisher contents, downloaded directly with curl at2026-10-28T08:15:36Z from https://press.princeton.edu/chapters/c8958.pdf and read through pdftotext, list section4.7, Holder Estimates, p147; section4.7.1, Holder Bounds for the Beurling Transform, p147; section4.7.2, The Inhomogeneous Cauchy-Riemann Equation, p149. An earlier entry named the wrong subsections and an unavailable c8868 URL; that bibliographic detail is retracted. The actual estimate statement has NOT yet been seen. This located citation lead cannot support any claimed norm or constant. The downloaded contents are saved as sources/aim_contents_8958_candidate.pdf and .txt; PDF SHA256:4a670769e8970b94f39d63d8aad3fce0e239ad1f980765b2485519af6d1c45d8. No browser-tool result is used as evidence.


## Sharp Lp norm, distinct from the requested Holder norm (2026-10-28T06:30:34.728719+00:00)

**Stefan Geiss, Stephen Montgomery-Smith and Eero Saksman, *On singular integral and martingale transforms*, arXiv:math/0701516v2,5 November2008.** Primary source https://arxiv.org/pdf/math/0701516, saved as `sources/geiss_montgomery_smith_saksman_2008.pdf` and `.txt`. Theorem1.1 on source page2 and Corollary1.2 on page3 were read, together with the operator definitions on page6. For1<p<infinity, Corollary1.2 states that the scalar Lp norm of Re(BA) is p*-1, where p*=max(p,p/(p-1)). Theorem1.1 gives equality of the real and imaginary component norms with the UMD constant in a real Banach-valued Lp space. Its kernel is BA f=-(1/pi)pv integral f(w)/(z-w)^2 dA(w), so Re(BA)=-2T_xx and Im(BA)=2T_xy in the present conventions. Thus it supplies an exact Lp component norm, not a Holder seminorm formula. No substitution of p for the Holder exponent is justified. Classification: **sharp numerical norm in a different function space**. The paper's historical comments about the full complex Lp norm are not used as a claim about the state of the literature in2026.

## Cauchy-potential estimate in the Dragicevic lecture notes

**Oliver Dragicevic, Analysis of the Ahlfors-Beurling Transform, arXiv:2109.04555 (2021 upload of lecture notes for the Seville summer school of September2013).** The complete primary PDF was retrieved from https://arxiv.org/pdf/2109.04555 and saved as `sources/dragicevic2021_candidate.pdf`, with extracted text. The title, table of contents, and the complete statement and proof of Lemma2.22 on printed pages18-19 were read.

For p>2 and h in Lp(C), the modified Cauchy potential is

    P h(z)=-(1/pi) integral_C h(zeta)[1/(zeta-z)-1/zeta] dA(zeta).

Lemma2.22 asserts continuity and a uniform Holder estimate of exponent1-2/p. Its proof gives the explicit constant

    [P h]_(1-2/p) <= C_p ||h||_p,
    C_p=(1/pi)(integral_C |eta(eta-1)|^(-q) dA(eta))^(1/q),
    q=p/(p-1) in(1,2).

The integral defining C_p is finite: its two local singularities are integrable for q<2, and its far tail is integrable for q>1. The proof uses Holder's inequality, dilation and translation of the kernel difference. It is an estimate for a potential mapping Lp into Holder space, not an operator bound of the Beurling transform on a Holder space. No C_alpha or D_alpha value follows from it by relabelling p. Classification: **explicit constant for a different source space and operator**. Its subsequent applications were not studied.

## Campanato T1 statement checked 2026-10-28T07:36Z

**Andrei V. Vasin, T1 theorem for Campanato spaces on domains, arXiv:1711.09303.** The retrieved PDF has the v1 banner dated 25 November2017 and an internal submission footer dated13 November2018; these distinct dates are preserved rather than reconciled by assumption. Source: `sources/vasin_campanato_t1_2017.pdf` and extracted text.

Pages1-5 were read. Theorem2 assumes a bounded Lipschitz domain, a smooth homogeneous Calderon-Zygmund operator, and an increasing modulus omega of upper type below one (also allowing omega=1). Its restricted operator T_D f=T(f1_D)1_D is bounded on the Campanato space precisely when (T1_D)1_D belongs to the space with modulus

    omega_tilde(x)=omega(x)/(integral_x^1 omega(t)dt/t).

The norm is the cube mean-oscillation seminorm plus the L1(D) norm. For Dini moduli, the two moduli are equivalent. Theorem3 gives boundedness for even kernels when the boundary is C^(1,omega_tilde). Proposition1 supplies the characteristic-function estimate under C^(1,omega) boundary regularity. Page5 explicitly uses variable unspecified constants. The word sharp concerns domain regularity. Classification: **qualitative restricted-domain boundedness, not an exact or numerical whole-plane Holder norm**.

## Parameter-dependent Cauchy integrals, checked 2026-10-28T07:52:10Z

**Yifei Pan and Yuan Zhang, *Cauchy singular integral operator with parameters in Log-Holder spaces*, arXiv:2001.03778v1 (11 January2020).** Primary PDF and text saved as `sources/pan_zhang_log_holder_2020.{pdf,txt}`; SHA256 alongside. Source: `https://arxiv.org/pdf/2001.03778v1`.

Definition1.1 uses a full derivative supremum norm plus the modulus quotient with denominator `|h|^alpha |log|h||^nu`, restricted to `0<|h|<=1/2`. Its operator (1) is the Cauchy boundary integral on a planar slice of `D times Lambda`, with parameter in an open real or complex set. Theorem1.2, page2, maps this Log-Holder class with logarithmic index `nu` to index `nu+1`, and explicitly states an unspecified constant depending on the domain, derivative order, exponent and logarithmic index. The sharpness asserted immediately afterward is the necessity of the one-unit logarithmic loss in parameter dependence. It does not compute a scalar operator norm. The displayed theorem prints `C^{k,alpha}` boundary, while the introductory geometric assumption gives finitely many disjoint `C^{1,alpha}` Jordan curves; this audit makes no attempt to resolve that presentation discrepancy or use the theorem beyond its source scope. Theorem2.2 is a qualitative classical Cauchy-potential and boundary-integral estimate with an unspecified constant. Classification: **sharp regularity loss for a parameter-dependent boundary operator, no numerical whole-plane Beurling or Riesz seminorm constant**. The paper's applications were not investigated.

## Arsenovic-Mateljevic: unverified citation lead

The exact theorem remains UNVERIFIED. V153 repeated an unsupported primary-access claim and is withdrawn by V154. Current local downloads are HTML errors. See `arsenovic_mateljevic/STATEMENT.md`. No theorem or numerical constant from this paper is used.

## Unverified corrected modulus theorem, access checked 2026-10-28T09:51:16.675447+00:00

The read bibliography of Arsenovic-Mateljevic cites L. O. Rode and I. B. Simonenko, *Multidimensional singular integrals in classes of common leading moduli of continuity*, Siberian Mathematical Journal9,690–696(1968), DOI10.1007/BF02199106, together with a correction in volume11(3),543(1970), DOI10.1007/BF00967097. Neither exact statement nor correction was obtained. A metadata request supplied no public full-text location, and the attempted Math-Net issue page returned no article. Both must be read before importing any claim. This is a citation lead only; the existence of a correction is a reason to retain the source limitation explicitly. Evidence:sources/rode_simonenko_access_manifest.json.

## Retractions and current access status

V140 and V143 claimed that the Arsenovic–Mateljevic statement had been read. Those access claims were unsupported and are retracted by V141 and V144. The exact theorem remains unseen. No operator estimate uses it. Current record: `arsenovic_mateljevic/STATEMENT.md`.

A later actual Crossref response and the DOI-resolved journal landing page confirm the bibliography and abstract only. The saved journal page contains the reference list, including the Rode–Simonenko correction. They do not expose the theorem. Evidence: `arsenovic_mateljevic/verification/crossref_1031.json`, `doi_landing_1031.html`, and `journal_embedded_1032.html`. The embedded page was inspected as text; no script was executed.


V146 made the same unsupported access claim and is retracted by V147. The article remains unverified. Further checking requires a readable local primary source.


V153 is RETRACTED by V154. Arsenovic-Mateljevic, Nolder, the Rode-Simonenko paper and correction, and the AIM book theorem remain unseen in the accepted local-source audit.
