# Repair audit of the report assembled at17:09Z

## 1. Snapshot and scope

The pinned report has6213 lines and SHA256 7fbcffbea6e6ac22144a6f13841912287b0b6c1e8d9efdd3a8854ef4f1389754. It was copied at2026-11-03T17:16:20.519077+00:00; the directory suffix is only a name, not an asserted reading time. The agent this report had identical bytes. The entire339-line diff against the16:41 snapshot was read in bounded pieces, including every new table row. The coordinator's full sixteen-item Section2B check was read and compared. README was read completely; the complete THEOREM_ATTEMPTS and PROOF_OBSTRUCTIONS diffs against the earlier handoff pins were read. Earlier unchanged proof bodies were not claimed newly reread.

This is a repair audit following A1708. It preserves the earlier proof approvals and records the new pressure-normalization omission separately from the sound source theorem. It does not prove the full Euler conjecture.

## 2. Source-space and ratio repairs

The Pan-Zhang row now retains a connected planar domain, C^N-valued H1_loc solution, L2_loc coefficient and infinite L2 order. The CPZ Theorem1.3 row retains a locally Lipschitz R^M-valued solution and the Ln_loc full-gradient coefficient. This repairs A1705, including the representative issue.

The positive-pressure margin statement is now restricted to the actual LIT252 counterexample. The negative2/3 endpoint remains explicitly open. LIT253,LIT254,LIT255 are listed separately: zero-helicity positive-pressure axis; compact negative-pressure positive-helicity boundary; and zero-helicity negative-pressure cylindrical boundary. Their properties are not merged. This repairs A1706.

The exact consequences are limsup R>=2/3 and liminf R<=2, not confinement of the entire cluster set. The revised README, summary and obstruction file use these inequalities and explicitly deny the stronger conclusion. This repairs A1777. The scalar example R=3/2+sin(log log(1/r)) in the obstruction file is a logical countertest, not an Euler tail.

## 3. Kelvin, tail-zero and source-endpoint repairs

THEOREM_ATTEMPTS T9 now distinguishes the primitive beta of i_W vol from the actual velocity form U.dx. The Lie equation for beta follows from the Cauchy law; the full U.dx Kelvin law is equivalent to momentum and fails for nonzero compact-velocity models. A066 is restricted to a trapping region and the later attractor is attributed to B24/A252-A253 in its stated parameter range. This repairs A1772-A1775.

README distinguishes finite-jet T0 from existence of at least one common infinitely flat witness under the global smooth-tail hypotheses. Its CO56 clause restores the scaled derivative bound, ratio intervals and punctured negative-scalar premise. This repairs A1778-A1780 without claiming every T0 point is flat.

The Chae-Tsai bounded alpha0 endpoint qualification now appears in the theorem remark, literature discussion and its own table row. The constant velocity with pressure -|v0|^2/3 satisfies the associated pressure formula, and its outer energy term remains nonzero. The correction stays outside the target range and does not change Theorem1. This integration matches A1768-A1771.

## 4. The sharp vorticity table

The ten exact pairs (c_k,M_k) are copied correctly: (.41,.982),(.42,.960),(.43,.938),(.44,.916),(.45,.893),(.46,.870),(.47,.846),(.48,.822),(.49,.797),(.50,.772). The C2/C1 full-profile hypotheses, bounded U, distributionally vanishing dilates and global vorticity supremum remain in Theorem8. Each M_k lies strictly below the continuous sharp threshold at c_k, so the weak bound sup|W|<=M_k is legitimate. Monotonicity gives every0<c<=c_k. The uniform.772 conclusion agrees with A1725.

The statement that C59 is submitted and unaudited was already obsolete at the pinned report time: A1782-A1789 confirmed its closed endpoint, strict monotonicity, Emden representation and comparison additions. This is a stale status, not a defect in the weaker valid theorem. Update the two endpoint-status clauses and current threshold row. The original Lemma NW uses strictly positive scalar density, so its nonattainment statement is consistent with C59's different nonnegative-density endpoint argument. Other weight families and bare decay remain open.

## 5. Section2B algebra and uniformity

All sixteen repairs pass at the unchanged hypotheses. The modified Bernoulli quantity is exactly the report's other H minus c(1-2c)|y|^2/2. The backward multiplier statement retains c<1/2. The signed-area conclusion asserts no pointwise monotone angle.

For the Fourier equality, |sum k|c_k|^2|<=sum |k||c_k|^2<=sum k^2|c_k|^2 is sharp precisely when all nonconstant coefficients have one sign of k and |k|=1. Thus support is in{0,1} or{0,-1}, with unrestricted c0. Nonstationarity in the period-bound equality eliminates the degenerate constant curve.

The normalized logarithmic derivative identity now has the required divisor |Omega(a)|. For a compact K0 in{Omega!=0}, choose a backward-invariant enclosing ball D'. The exact Cauchy formula gives

    |Dpsi_t(a)Omega(a)|=exp(-(1+c)t)|Omega(psi_t(a))|
      <=[sup_D'|Omega|/inf_K0|Omega|] exp(-(1+c)t)|Omega(a)|.

The denominator is positive by compactness. The ball is backward invariant by the radial trapping inequality. This is a bound along Omega and supplies no uniform hyperbolicity in the complementary directions.

The quotient norm is explicitly |(B cross Omega)(v)|; exact contraction in that norm becomes a two-sided bounded-factor assertion for Euclidean quotient norms on the compact regular set. The smaller/larger flow-box changes place every plaque arc in the region where DF inverse is controlled. The entropy claim now retains the smoothness or nonvanishing-vorticity premise, rather than dropping the finite-regularity loss.

## 6. Section2B periodic and cited consequences

At a vortical cycle the multipliers1,exp((1+c)T),exp((2c-1)T) give a hyperbolic saddle when0<c<1/2. Its backward basin is contained in its two-dimensional unstable manifold for the forward flow, hence has Lebesgue measure zero. Hyperbolic periodic orbits are countable: each has a spatial neighborhood and a period interval isolating it among such cycles, and these can be selected from countable rational bases. The union of their null unstable manifolds is null. This supplies the new short argument, rather than assuming all periodic basins vanish from divergence alone.

The revised completeness lemma claims global strong-stable curves only on the compact regular hyperbolic set. The A158 half-line result, kinematic realizations and finite-network result are marked as cited inputs. The vortex line through a vortical equilibrium meets the limit set only at that point; absence of other intersections does not assert absence of accumulation. The affine examples violate uniform sublinearity and decay, and the line-zero example has curl2omega e3, so its vortical qualification requires omega!=0. These repairs do not change the approved proof steps.

## 7. New acceleration-row normalization error

The new LIT257 row states -P>=kappa|V|^2 and concludes exclusion at a flat zero without requiring P(x0)=0. That literal statement is false. Let f(s)=exp(-1/s^2) for s!=0 and f(0)=0, and set near0

    V(x)=(f(x2),0,0), P(x)=-1.

This is smooth, divergence free, infinitely flat in value at0 and nonzero in every neighborhood. Since V differentiates only in x1 while its coefficient depends only on x2, (V.grad)V=0. Constant pressure gives the full stationary momentum equation and div div(V tensor V+P I)=0. On a sufficiently small ball, -P=1>=|V|^2, so kappa=1 and acceleration constant K=0 meet the printed conditions. The claimed conclusion V=0 is nevertheless false. The finite-order version is likewise contradicted by replacing f(s) with s.

The repair is to write M=P(x0)-mean P and require P(x0)-P>=kappa|V|^2, or explicitly normalize P(x0)=0 before using -P. Under this correct hypothesis, M(0)=0 and flatness gives flat M, exactly as in A1698-A1702. In the actual common-flat tail application P2(x0)=0 is already part of the data, so that application and LIT257 itself remain sound. This counterexample concerns the report's missing hypothesis, not the target Euler equation or similarity class.

## 8. Two scope qualifiers and current integration

The new Hardy row says that the time-slice version holds with L1_loc in time. A1718's repair also explicitly assumes local integrability of the quadratic weak products, besides the L1-in-time L2 velocity and Hardy pressure. Restore that clause and the distributional stress or weak-Euler premise. L1_t L2_x alone does not imply locally integrable v tensor v: v(t,x)=|t|^(-3/4)w(x) for0<|t|<1, defined as zero at t=0, with nonzero smooth compactly supported w, is L1_loc((-1,1);L2) while its squared norm is not time integrable near the interior time0. This is a premise-separation test, not a solution counterexample.

The new B59-B61 row labels all conclusions over0<c<1/2 and gives only 'local structure' in the hypothesis column. The actual escaping-W2 conclusions in A1729-A1740 retain the helicity-free profile with natural bounds and its scattering/tail inputs in2/5<c<1/2. The elementary contact algebra is wider, but the current citation does not by itself certify a wider actual-W2 theorem. State the actual-profile range and natural class explicitly, and separate the local identities if keeping their wider range. The C3-pressure qualification can now be shortened to C3 velocity by A1799. The earlier B58 row still needs the equality-rate rho=-2(1-c), grad S!=0 premise already identified in the B integration notes.

The newly added C54,C55 and angular-frequency/ratio summaries otherwise preserve their local or conditional roles; no unconditional flat-tail exclusion was added. The full report still needs these concrete normalization and scope repairs before whole-report approval. The full bare-decay, arbitrary-helicity, every-omega conjecture remains OPEN.
