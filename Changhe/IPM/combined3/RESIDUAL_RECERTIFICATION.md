# Residual recertification for unchanged Candidate 013

## Result

**Both requested inequalities PASS.** Fresh whole-plane certificates give
\[
\boxed{\|F_*\|_2<7.960467\times10^{-7}
<7.961207\times10^{-7}<7.96121055107\times10^{-7}},
\]
\[
\boxed{Q(F_*)<0.016684<0.094.}
\]

| Required certification | Fresh containing upper | Verdict |
|---|---:|---|
| Actual \(L^2\) residual | \(7.960466701000260\times10^{-7}\) | **PASS**, including the optional stronger target |
| Actual \(Q\) residual | \(0.016683060263749470\) | **PASS** |

The decimal uppers in this table are rounded outward. The exact rational
energy uppers and strict power comparisons are in
[the final certificate](IPM.artifacts/residual_recertification/validated_summary.json)
and [the independent rational check](IPM.artifacts/residual_recertification/independent_threshold_check.json).

This report concerns only the actual residual
\[
F_*=(\bar c_l X+u_*)\cdot\nabla\rho_*-\rho_*,\qquad
\bar c_l=\frac{4076476460239181}{2251799813685248}.
\]
Candidate 013, its coefficients and parameter are unchanged. No coercivity,
closure constant, correction radius or existence argument is recalculated here.

The new numerical evidence is independent of the unavailable historical
residual evidence. The calculations read the two preserved rational source
files and the source-evaluation algorithms; they do not import a historical
residual norm, regional integration result, Taylor table, complex majorant or
endpoint certificate. Previously published final scalar summaries are not used
as validated inputs.

## Source identification and reconstruction

All paths below are relative to the repository root.

| Object | Exact source | SHA256 |
|---|---|---|
| Candidate 007 potential | `Changhe/IPM/combined1/combined1.artifacts/candidates/C1-N1-007-d2w-j7-e2bal/d2w_j7_n4_E2bal_mid180_exact.json` | `ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21` |
| Candidate 013 correction | `Changhe/IPM/combined2/IPM.artifacts/exchange/candidate_snapshots/C2-N1-013-phi-007-sector-d8-leg24-lat-nf2/phi_007_b18s2_phi_exact.json` | `a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a` |

The source identities are
\[
\rho_*=-\Delta\chi_y-\Delta\phi,\quad
\psi_*=\chi_{xy}+\phi_x,\quad
u_*=(-\psi_{*,y},\psi_{*,x}).
\]
The input files both specify the displayed exact parameter; the correction
also binds the Candidate 007 hash. Exact rational grouping and differentiation
precede interval evaluation. Source coefficients are never inferred from
rounded field samples. Each grouped potential term has radial factor
\[
r^n(1+r^2)^b(t+r^2)^{-v}
P\!\left(\frac{r^2}{t+r^2}\right),\quad t>0,
\]
times a sine or cosine harmonic. The residual is a finite sine sum over
positive odd harmonics. No angular sampling or angular quadrature is used.

The reused evaluator `coercivity_residual/fields013.py` has SHA256
`2ac292c416860432c0b64cb97d66e7e68b17aa12fef126b0979a5b1f0917f23c`;
`coercivity_residual/asymptotics013.py` has SHA256
`1d7c89105fd5c4ce2a9d558e278b63fe0e2d39e9079c419221c2694a4b042f21`.
Their relevant algebraic and analytic formulas are described below, rather
than treating old certificate outputs as evidence.

## Whole-plane coverage and error accounting

All new programs and raw certificates are in
`IPM.artifacts/residual_recertification/`, beside this report's existing
artifact tree. Exact rational endpoints and a coverage check partition the
plane into an origin disk, consecutive finite annuli, and an infinite exterior.
Here the final regions are \(r\le10^{-3}\), 342 exact consecutive annuli
covering \(10^{-3}\le r\le10^6\), and \(r\ge10^6\).
Boundary circles have measure zero. The final reducer checks every adjacency,
the number of panels, the origin and exterior endpoints, the source hashes and
the strict rational comparisons against both requested thresholds.

Arb encloses rounding errors in every real arithmetic operation. All saved
intervals are containing rational endpoints or containing Arb balls. In
particular, the workflow does not estimate rounding errors by comparing two
floating-point runs. See the [Python-FLINT arithmetic documentation](https://python-flint.readthedocs.io/en/latest/general.html).

### Origin disk

The analytic variable is \(s=r^2\), with complex Cauchy radius \(1/32\).
The denominator scales are positive, with minimum \(1/8\), so the chosen
disk does not meet a pole or branch cut. Exact expansion through degree 16
gives every density derivative through order four and velocity derivative
through order three. Finite homogeneous coefficients are combined exactly;
their absolute sums and analytic remainders are saved as dyadic enclosures.

An independent low-degree source reconstruction forms the residual polynomial
through total power ten. Its fourteen nonzero coefficients begin at degree
three: the linear coefficient cancels exactly. Larger potential harmonics
cannot contribute to this polynomial because differentiation reduces total
degree by at most four. The finite terms omitted from the residual polynomial
are bounded by positive coefficient sums, with exact polynomial derivative
factors; analytic field errors enter through the full product rule, including
both finite-times-tail terms and the tail-times-tail term.

These bounds cover the entire disk \(r\le10^{-3}\), including its center.
The stored pointwise envelopes give local positive differential energies;
regional integration by parts is not assumed.

### Finite annuli: exact angular reduction and validated radial quadrature

Write \(F_*(r,\theta)=\sum_n f_n(r)\sin(n\theta)\). Then
\[
\|F_*\|_{2,\text{panel}}^2
=\pi\int_{c-h}^{c+h}r\sum_n f_n(r)^2\,dr.
\]
Arb radial Taylor coefficients are convolved in the angular Laurent index
before the density is subtracted. A Kronecker encoding with stride \(2K+1\)
performs the product exactly at the polynomial-index level: two input radial
degrees at most \(K\) cannot carry into a neighboring angular index.
Radial scaling prevents artificial loss of precision in this encoding.

For the complex disk \(|z-c|\le c/4\),
\(\Re(z^2)\ge9c^2/16\). Thus every \(t+z^2\) remains in the right
half-plane. The complete grouped polynomial is shifted about
\(c^2/(t+c^2)\), and its complex deviation is bounded explicitly. Jointly
factoring \(z^n(1+z^2)^b(t+z^2)^{-v}\) avoids the excessive bounds obtained
by taking the absolute values of its large radial factors separately.
Cauchy's derivative estimate on the inner disk of radius \(R=c/8\), and
the exact Cartesian polar differentiation formulas, give a fresh bound
\(H\) on \(\sum_n|f_n(z)|\) throughout that inner disk.

If \(P_n\) is the degree-\(K\) Taylor polynomial and \(z_0=h/R<1/2\),
\[
\sum_n\sup_{|r-c|\le h}|f_n(r)-P_n(r)|
\le\delta=H\frac{z_0^{K+1}}{1-z_0}.
\]
This is an angular coefficient-sum bound, obtained by summing inside Cauchy's
contour integral. Set
\(B=\sum_{n,k}|f_n^{(k)}(c)/k!|h^k\). The complete polynomial
\((c+hx)\sum_n P_n(c+hx)^2\) is integrated coefficient by coefficient;
every even coefficient has exact integration factor \(2h\pi/(k+1)\).
The omitted analytic contribution is at most
\[
2h\pi(c+h)(2B\delta+\delta^2).
\]
The raw files save the full integrated-polynomial coefficient intervals,
its integral, this error, \(H,R,K,B,\delta\), precision, exact geometry and
all modal derivative intervals used for the second certification.

### Infinite exterior

The analytic variable is \(u=r^{-2}\), with complex Cauchy radius
\(1/3600\). Since the largest denominator scale is 900, all analytic
factors remain away from their singularities. Exact homogeneous expansions
and angular convolution preserve cancellations in the finite residual.
The retained exact prefix includes every residual exponent at least \(-5\).
It is first reconstructed from degree-two potential expansions, then reused
with degree-six expansions for the smaller final exterior radius. Additional
potential terms have field exponent at most \(1/\bar c_l-6<-5\);
additional nonlinear terms have exponent at most \(2/\bar c_l-7<-5\).
Thus they cannot change this retained prefix. The reducer checks exact equality
of its 1,306 coefficients, and all lower powers enter the remainder envelope.

The first nonzero residual exponent is
\[
p=-\frac{11375183046454913}{4076476460239181}<-2.
\]
No asymptotic leading-term approximation is used without a remainder.

For each potential group the Cauchy tail is bounded explicitly after Cartesian
differentiation. A conservative geometric tail denominator \(1-8z\),
\(z=3600/r^2\), works for all derivative orders used here: consecutive
majorants have ratio below \(8z\). The nonlinear residual error includes
finite-times-tail and tail-times-tail contributions with every Leibniz
multiplicity. Finite terms below the retained cutoff are also bounded, not
discarded. The saved raw data are positive power envelopes for every
\(\partial_x^i\partial_y^j F_*\), \(i+j\le3\).

Each term \(A r^a\) contributes at most
\[
\sqrt{2\pi}\,A\frac{R_\infty^{a+w+1}}
{\sqrt{-2(a+w)-2}}
\]
to \(\|r^w\partial_x^i\partial_y^jF_*\|_{2,r\ge R_\infty}\),
for \(w=0,1\). Every required exponent is checked to satisfy \(a+w<-1\).
Minkowski's inequality then supplies a rigorous whole-exterior norm bound.

## The high-order norm

Let \(V=(F_*,2xF_*,2yF_*)\), \(q=21/10\), and
\(E_m=\|J^mV\|_2^2\), where \(J=(1-\Delta)^{1/2}\).
Fourier differentiation and integration by parts give
\[
Q(F_*)^2=\|J^qV\|_2^2
-8q\|J^{q-1}F_*\|_2^2
-4q(q-2)\|\nabla J^{q-2}F_*\|_2^2
\le\|J^qV\|_2^2.
\]
The fresh regional derivative estimates prove the weighted \(H^3\)
membership needed to justify this identity by approximation. Spectral
interpolation yields
\[
Q(F_*)\le E_2^{9/20}E_3^{1/20}.
\]
The final threshold test uses the exact rational inequality
\(E_2^9E_3<(47/500)^{20}\).

For each finite sine mode define
\[
g_n=f_n-f_n''-f_n'/r+n^2f_n/r^2,\qquad
a_{n,\pm}=rg_n-2f_n'\pm2nf_n/r.
\]
The exact positive differential formulas are
\[
E_2=\pi\sum_n\int r\left(g_n^2+2\sum_{\pm}a_{n,\pm}^2\right)\,dr,
\]
\[
E_3=E_2+\pi\sum_n\int r\left[(g_n')^2+\frac{n^2g_n^2}{r^2}
+2\sum_{\pm}\left((a_{n,\pm}')^2+
\frac{(n\pm1)^2a_{n,\pm}^2}{r^2}\right)\right]\,dr.
\]
Cross terms from neighboring angular modes cancel between the two coordinate
components of \(V\). The factor two also accounts for the zero cosine mode
when \(n=1\). These identities were independently verified using exact
Cartesian polynomials, including overlapping modes one, three and five.

The finite-panel calculation encloses the positive modal formulas for
\(\|(1-\Delta)V\|_2^2\) and
\(\|(1-\Delta)V\|_2^2+\|\nabla(1-\Delta)V\|_2^2\).
Taylor derivative remainders through order three are bounded by
\[
\frac{H}{R^d}\frac{(K+1)!}{(K+1-d)!}
\frac{(h/R)^{K+1-d}}{1-2h/R},\quad 0\le d\le3.
\]
Interval upper bounds on their nonnegative integrands are multiplied by the
exact panel width. The origin and exterior contributions use pointwise tensor
contraction and triangle inequalities for the same positive differential
energies. Consequently no unaccounted regional boundary term is introduced.

For completeness, on either endpoint region let
\(N_j\ge\|D^jF_*\|_2\), \(B_j\ge\|rD^jF_*\|_2\) denote ordered
tensor bounds. A sufficient vector bound is
\[
L_j=N_j+2B_j+2\sqrt{j(j+1)}N_{j-1},
\]
with the last term omitted for \(j=0\). Then the regional positive energies
are at most \((L_0+\sqrt2L_2)^2\) and
\((L_0+\sqrt2L_2)^2+(L_1+\sqrt2L_3)^2\), respectively. The origin
program also computes the vector tensor bounds directly from its pointwise
derivative envelopes.

## Validated numerical accounting

The following entries are containing upper bounds rounded upward from the
raw replay. The finite integer-energy replay may enlarge the producer's
original upper endpoints slightly because it reconstructs intervals from
their saved rational endpoints.

| Region | \(\int |F_*|^2\) upper | Local positive \(E_2\) upper | Local positive \(E_3\) upper |
|---|---:|---:|---:|
| Origin \(r\le10^{-3}\) | \(1.939251\times10^{-25}\) | \(1.581806\times10^{-11}\) | \(1.599796\times10^{-5}\) |
| 342 finite annuli | \(6.336903009521434\times10^{-13}\) | \(0.000113529578142\) | \(0.890266683462\) |
| Exterior \(r\ge10^6\) | \(2.500227\times10^{-23}\) | \(1.360845\times10^{-10}\) | \(1.360845\times10^{-10}\) |

In particular the full integer energies satisfy
\[
E_2<0.00011353,\qquad E_3<0.890283.
\]
The final norm comparisons use the tighter exact rational energy sums saved
in the final certificate, rather than these rounded table entries.

The finite producer uses 640-bit arithmetic and Taylor degrees 74 through
112. Its summed analytic \(L^2\) quadrature error is below
\(1.211780\times10^{-32}\). All coefficient rounding errors are already
contained in the saved polynomial intervals. Ninety-nine panels use the
original convolution layout and 243 use its equivalent parity-compressed
layout; both implementations are preserved. The final raw-data reducer runs
at 1,024 bits, independently re-evaluates the polynomial integrals, modal
integer energies and exterior power integrals, and checks the exact coverage.
The last threshold checks use Python rational arithmetic only.

## Reproduction, checks and limitations

The artifact directory contains the programs **and primary enclosure data**:

| Files | Purpose |
|---|---|
| `source_bindings.json`, `manifest.json`, `verify_manifest.py` | Exact source/evaluator bindings and SHA256 checks for every published artifact |
| `origin_certificate.py/.json`, `origin_large_certificate.py/.json` | Complete fresh origin field coefficients, Cauchy tails, cancellation-preserving residual polynomial and disk energies |
| `far_certificate.py`, `far_certificate.json`, `far_degree6.json`, `far_prefix_binding.json` | Exact source-derived exterior prefix, refined finite/remainder power envelopes and their explicit binding |
| `finite.py`, `finite_fast.py`, `run_finite_legacy.py`, `run_finite.py`, `high_order.py` | Both validated convolution layouts, complex majorants and interval integration |
| `finite_data_core/configuration.json`, `finite_data_core/panel_*.json.gz` | Every finite panel's geometry, raw polynomial intervals, errors and modal derivative enclosures |
| `finite_receipt.py`, `finite_run_receipt.json` | Exact finite-domain coverage, source/code hashes, raw-file hashes and summed error accounting |
| `assemble_certificate.py`, `validated_summary.json` | Independent raw-data replay, source bindings, whole-plane energy sums and exact comparisons |
| `verify_final_thresholds.py`, `independent_threshold_check.json` | Separate pure-rational verification of both requested bounds and displayed upper bounds |
| `crosscheck_convolution.py`, cross-check JSON files, `independent_modal_check.py/.json`, `audit_fast_encoding.py`, `fast_encoding_exact_audit.json` | Cross-checks of residual coefficients, integer modal identities and compressed convolution indexing |
| `FINITE_METHOD.md`, `FINITE_KERNEL_AUDIT.md`, `origin_method.md`, `high_order_method.md` | Detailed mathematical estimates and implementation audit |
| `reproduce.py` | Portable saved-data replay or complete regeneration in a temporary directory |

`executed_sources/` preserves the two original programs containing workstation
paths. Their portable copies change repository lookup only; the arithmetic
kernels are identical. `source_path_portability.json` records both hashes.
The independent finite-kernel audit binds the preserved executed source where
this path-only change applies.

From the repository root, create an environment outside the repository and
replay all saved evidence:

```bash
repo_root="$PWD"
artifact="$repo_root/Changhe/IPM/combined3/IPM.artifacts/residual_recertification"
python3 -m venv /tmp/ipm-residual-verify
/tmp/ipm-residual-verify/bin/python -m pip install python-flint==0.9.0 numpy==2.5.4
/tmp/ipm-residual-verify/bin/python -B "$artifact/reproduce.py" --repo-root "$repo_root"
```

The replay first checks the complete file manifest and immutable evaluator
hashes, then replays all 342 raw panels and both endpoints. It writes its new
summary outside the repository. The published arithmetic environment is
Python 3.12.3, Python-FLINT 0.9.0 and NumPy 2.5.4; NumPy is imported by the
existing evaluator, while certified arithmetic uses FLINT rational/Arb types.

To regenerate the primary enclosures directly from the exact source, including
all origin coefficients, far coefficients, majorants and panel Taylor data:

```bash
/tmp/ipm-residual-verify/bin/python -B "$artifact/reproduce.py" \
  --repo-root "$repo_root" --regenerate --workers 20
```

This selects a new temporary output directory and prints every producer
command. It does not reuse saved regional enclosures. The degree-two far
prefix is regenerated before the degree-six exterior certificate; every
finite annulus is regenerated. The exact input source and evaluator hashes
are checked again. The number of workers can be reduced without changing the
mathematical estimates.

The original and compressed residual convolutions each passed 2,430
coefficient cross-checks against the separate Acb convolution at five radii.
Another exact rational regression passed 640 compressed-index checks through
the full product degree. These are additional implementation checks; the
norm proof itself is the validated source-to-enclosure computation and its
complete error accounting. The scalar verifier independently confirms the
strict displayed bounds using rational powers, without importing Arb or the
numerical producer.

The final portable saved-data replay passed, including strict integrity
checks for all 383 archive files and both exact source files. The manifest
SHA256 is
`075e3c428961ed11520fb0a7820f560125ace33c16504fdaa330d56193ea9c34`.
The archive retains each panel's convolution-layout metadata; fresh regeneration
uses the equivalent compressed implementation and can produce slightly
different containing endpoints while verifying the same strict inequalities.

The historical provenance audit found 549 recorded dependencies: 46 matching,
497 missing and six mismatched. These facts motivate the fresh calculations;
none of those missing or mismatched records is a numerical premise here.
The unfinished audit supplied during this task reports the same provenance
gap. Its historical summation and forcing replay are not numerical inputs to
this replacement certificate.

This report certifies only the two residual inputs for this fixed candidate.
It does not independently audit other premises of the stationary existence
theorem or make a new existence claim.
