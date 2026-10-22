# What finite continuation comparisons can and cannot establish

Status: exact diagnostic definitions and complete limitations argument written before numerical comparison. The numerical findings will be reported separately. There is no claim of an exact branch or a fold.

## 1. Definitions on a common physical grid

Let S_i be saved B2 coefficient states with beta_i, lambda_i. In the fixed physical Cartesian variables (x,y), independently reconstruct F_i=Theta_i/x^2 and G_i=Omega_i/x by their smooth parity extensions at x=0, then Theta_i=x^2 F_i and Omega_i=x G_i. The coefficient geometry may depend on beta_i. Therefore differences of raw coefficient vectors are not physical field differences.

For each common radius r and a finite set of angles, let A_i(r;H)=max_angle |H_i| and D_ij(r;H)=max_angle |H_j-H_i|, where H is one of F,G,Theta,Omega. Record both D and the old-amplitude ratio D/A_i. Record a symmetric comparison D/max(A_i,A_j) as well. If an amplitude denominator is exactly zero, assign0 if D=0 and infinity otherwise. No positive denominator floor is used. A positive subnormal denominator is evaluated explicitly in extended precision. These comparisons are field-distance diagnostics, not the prompt's pointwise PDE residual normalization.

On any finite regional grid, the absolute maximum distance obeys the triangle inequality. The old-amplitude ratios for multiple successive pairs need not add: their denominators differ. A first-to-last relative change may be compared with, but is not mathematically equal to, the sum of the stage ratios.

All computed maxima are finite-grid maxima, not full-domain upper bounds. In particular a change of a far-field exponent can yield modest change on every fixed compact set while failing uniform control on the whole plane. The fields Theta may themselves be unbounded, and an unweighted global sup norm can be infinite.

## 2. A finite sign scan does not exclude intermediate roots

Let beta_1<...<beta_n be distinct real sample nodes and let m_i<0 be the recorded values. Let p be the polynomial interpolating these values and put

    Q(beta)=product_i (beta-beta_i)^2.

At every sample node, Q=0. Choose any beta_* strictly between two consecutive sample nodes. Then Q(beta_*)>0. For a sufficiently large positive constant A, the polynomial m_A=p+A Q satisfies

    m_A(beta_i)=m_i<0 at every sample,
    m_A(beta_*)>0.

The intermediate value theorem gives a zero between beta_i and beta_*, and another between beta_* and beta_(i+1). Thus even a real analytic scalar function can agree exactly with every negative sample and have roots between samples. An empirical quadratic fit, including agreement with another parameterized run at finitely many states, does not by itself exclude these functions. A justified derivative bound, shape condition, validated continuation or interval enclosure would be additional evidence.

This argument refutes the inference from finite samples to no intermediate root. It does not prove that the actual solver's scalar mismatch has such roots.

## 3. Finite field samples do not establish a continuous solution branch

Let beta_i and finitely many physical points X_j be the saved comparison locations. Choose a smooth bump in beta supported inside an interval between two consecutive beta_i and a smooth nonzero physical bump supported in a disk missing all X_j. Such disks and parameter intervals exist because the sets are finite. Multiplying these bumps and adding an arbitrary multiple to any field interpolation leaves every saved grid value unchanged, while allowing arbitrarily large variation at untested parameters and locations. One can choose parity-compatible bumps by adding reflected copies; the assertion about insufficiency is already true without parity.

Even without a spatial bump, a parameter bump that vanishes at all beta_i can change the interpolation arbitrarily between samples. If continuity of the parameterization is not an assumption, piecewise choices can also share exactly the same sampled values and be discontinuous. Therefore the sampled comparisons alone neither prove continuity, uniqueness of a solution branch, absence of a branch switch, nor fold nondegeneracy. They can identify observed jumps, or report that no large jump was seen in the saved fields on the specified grid. A fold assertion requires the branch and the relevant Jacobian/parameter conditions to be controlled separately.

This limitation is not a counterexample solution of B2 or of a discretized nonlinear system. The point is precisely that the field samples alone do not impose those equations or supply uniqueness. The numerical states under consideration are already refuted as literal unforced B2 fields by independent exact center tests in163.

## 4. Independent checks and scope

Use the verifier's existing SciPy BSpline reader, not the numerics lane's evaluator or code. Evaluate the same serialized coefficients at newly generated physical radii and angles, including origin and axes, with additional radial coverage beyond the reported grid. Freeze each input archive and its hash first. Compare successive accepted states, first-to-last states and successive saved secant evaluations at fixed beta. Match the reported radial ratio definition where comparison is useful, but retain the independently chosen angular grid and record its finite sampling difference.

The experiment does not recompute the full-plane inverse or the PDE residuals; those are separate checks. It must not be reported as another inverse validation, another regional PDE grid or proof of branch regularity. It supplies only direct physical-field comparisons and an audit of the stated inference.

Dependencies: exact field definitions from PROMPT.md, elementary interpolation, the intermediate value theorem and smooth bump functions. The independent numerical reader is verification infrastructure, not a premise of sections2-3. No numerical fact is needed for the limitations proof.

Written UTC 2026-10-21T12:36:43.563427+00:00, before comparison code.

## 5. Exact horizontal-ray tail check for the saved representation

This is a conditional algebraic conclusion about the literal serialized fields. Let b=beta_basis>2, L>0, and let c_(k,n) be the temperature coefficients of the clamped spline representation. On the physical ray (x,y)=(r,0), r>0, the angular coordinate is phi=atan2(x,-y) and the Chebyshev argument is cos(phi)=-y/r=0, so odd modes vanish and T_(2j)(0)=(-1)^j. Write

    z=(1+(r/L)^2)^(-1/(2b)),   t=1-z,
    C=sum_j (-1)^j c_(2j,last).

A clamped spline tends to its last coefficient as t tends1. Thus the exact representation gives

    Theta(r,0)=r^2 z^(b+2) [C+o(1)]
              =L^(1+2/b) C r^(1-2/b) [1+o(1)]       (when C!=0).

If C>0 and b>2, the coefficient and exponent are positive. For two states with b_j>b_i>2 and C_i,C_j>0, the exponent 1-2/b_j is strictly larger. Dividing Theta_j-Theta_i by r^(1-2/b_j) gives the positive limit L_j^(1+2/b_j) C_j. Hence

    sup_R2 |Theta_j-Theta_i|=infinity.

It suffices to check b>2, strict ordering of b and C>0 by exact rational arithmetic on the saved binary coefficients. The powers of L are positive and do not require numerical evaluation for this conclusion. These arithmetic checks are registered separately from the finite grids. This is an actual infinite global temperature-distance statement for those literal archives once the checks pass; it is not an assertion that a physically relevant parameter branch must be continuous in an unweighted global sup norm. The finite compact-grid comparisons remain useful in their stated topology.

Section5 written UTC 2026-10-21T12:39:38.402085+00:00, before exact tail-certificate implementation.


Representation qualification for section5: the field being certified is the exact mathematical clamped r2-spline series encoded by the archives and used by the independent reader. The r2 map and radial factor in the format are global for finite real r; knots repeat the right endpoint degree+1 times and no extra temperature amplitude factor multiplies the stored cF. This was checked by read-only inspection of the defining format and the independent reader, whose code is registered. Each of the nine certified fields has b>2 and C>0, so each individually has unbounded temperature and is not an element of the unweighted bounded-function space. The stated sufficient hypotheses are not necessary: for a pair it suffices that b_j>max(b_i,2), C_j is nonzero and C_i is finite. No equal-exponent pair is asserted here.

The NUM arbitrary-point floating helper does clip its spline evaluation argument to [0,1-1e-16] and applies nan_to_num. This roundoff guard is not hidden or adopted as a mathematical outer boundary. It is inactive on the tested grid. All nine accepted archives have b>3 and L=3/2. For0<=r<=10^8, q=1+(r/L)^2<2^53, hence z=q^(-1/(2b))>2^(-53/6)>2^-9. Thus the exact margin z is greater than1/512, whereas the effective floating clip is t<=1-2^-53. The strict rational inequalities and nominal z at the largest grid radius are recorded per archive. Section5 concerns the exact encoded spline series as r tends infinity, not an assertion about executing a floating helper at arbitrarily large machine numbers. The independent reader uses the unmodified mathematical t and stable logarithmic prefactors; finite-grid comparisons use only represented finite values. This reader supplies finite-grid evidence only; the infinite-tail conclusion uses coefficient arithmetic and the displayed exact formula. nan_to_num is irrelevant to this mathematical series and inactive wherever the helper receives finite spline values. A newly imposed clipped or exterior-replaced mathematical profile would require its own tail audit.

## 6. Saved scalar secants

For a saved state, define the exact center mismatch m=c_self+lambda c_seed-1-beta/2, with the canonical center moments given by the rational formula proved and checked in160 and163. For two saved evaluations at the same beta and different lambda, the quotient (m_j-m_i)/(lambda_j-lambda_i) is an exact secant of their recorded scalar values. A positive quotient describes this finite pair only. Even when every recorded quotient is positive, no derivative lower bound between evaluations, local uniqueness, implicit-function neighborhood or fold nondegeneracy follows without additional control. The polynomial perturbation construction of section2 applies to derivative behavior as well by choosing perturbations that vanish at the saved nodes.

Section6 and the explicit format/roundoff-margin qualifications recorded2026-10-21T12:48:51.594490+00:00. The existing exact secant computation had already used the center formula from160; this is its scope statement, not a new unverified center formula.
