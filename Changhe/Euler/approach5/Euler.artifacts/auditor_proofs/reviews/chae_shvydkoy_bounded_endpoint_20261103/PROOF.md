# The bounded zero-scaling endpoint of an archived Euler theorem

## 1. Exact claim and inspected version

This audit concerns Dongho Chae and Roman Shvydkoy, On formation of a locally self-similar collapse in the incompressible Euler equations, arXiv1201.6009v2, dated12April2012. The official arXiv record confirms the version and nineteen-page length. The actual retained primary text was read at pages1-5 and10-14, including the complete theorem statement and the bounded-pressure step. No journal revision was inspected.

The literal Theorem3.2 on printed page10 includes v in L^p(R^N) intersect C1loc, 3<=p<=infinity, associated pressure as in(8), and the interval -1<alpha<=N/p. It concludes v=0. The framework additionally requires the local energy equality, while page3 explicitly permits infinite total energy. At p=infinity this interval contains alpha=0.

For every integer N>=2 and nonzero v0 in R^N, the constant v(y)=v0 at alpha=0 satisfies these literal profile hypotheses, including the associated pressure and the full equation, but is nonzero. This is an exact counterexample to the printed velocity-triviality conclusion at that endpoint. It is not a blow-up example or a decaying profile.

## 2. Associated pressure and the complete equation

The manuscript's kernel is

    K_ij(z)=(N z_i z_j-delta_ij|z|²)/(N omega_N |z|^(N+2)),

where omega_N is the unit-ball volume. Rotational invariance and the trace identity give integral_(S^(N-1))theta_i theta_j=omega_N delta_ij. Hence K has zero angular mean. On every centered annulus epsilon<|z-y|<R, its contraction with the constant matrix v0 tensor v0 integrates to zero. The centered two-sided truncation of(8) thus gives the representative q=-|v0|²/N. It is a constant BMO function. The conclusion below depends only on grad q=0, so the additive BMO pressure gauge is immaterial.

The complete printed profile equation is

    y.grad v/(1+alpha)+alpha v/(1+alpha)
                    =v.grad v+grad q, div v=0.

For alpha=0 and constant v,q, every term vanishes. The velocity is smooth and bounded. The corresponding physical velocity and pressure are constant in space and time, so the local energy equality follows by integration against compact tests: all spatial flux integrals are zero, and the time derivative of the test reproduces the difference of the two endpoint integrals. Finite global energy is neither used nor available.

## 3. The precise outer-boundary failure

For a nonnegative nonzero compact smooth cutoff sigma,

    L^(-N) integral |v(y)|² sigma(y/L)dy
       =|v0|² integral sigma(z)dz>0

at every L. Thus the outer normalized energy term does not disappear at alpha=0 and p=infinity. For alpha<0 the same expression acquires a factor L^(2alpha) and does tend to zero. The strict negative-alpha subrange is not challenged by this example.

Equation(38) on printed page14 purports to bound the normalized inner energy by an exterior cubic and pressure-oscillation integral in the bounded case alpha<=0. For the constant example at alpha=0 its left side is omega_N|v0|². Every dyadic pressure oscillation q-qbar_k vanishes. Summing the cubic terms gives at most

    C |v0|³ integral_(|y|>=2L)|y|^(-N-1)dy
       =C N omega_N |v0|³/(2L).

This tends to zero. Therefore the displayed inequality fails for this example before any subsequent iteration. Changing the additive pressure constant cannot alter either side in the needed way.

## 4. What an additional vanishing-mean hypothesis repairs

The extra condition L^(-N) integral_(B_L)|v|² ->0 removes this particular missing limit at alpha=0. Uniform v(y)->0 implies it: for a fixed M, divide the finite inner integral over B_M by L^N and bound the rest by omega_N sup_(|y|>M)|v(y)|². First let L tend to infinity and then let M tend to infinity.

For a finite p>2, Holder gives this zero-alpha vanishing immediately. At the different finite-p critical scaling alpha=N/p, split at fixed M as above and apply Holder only to the outer part. Its normalized contribution is bounded by the Lp tail norm squared, which tends to zero as M increases. This explains why the constant countertest does not refute the finite-p endpoint proof.

These calculations repair only the outer limit. No complete new bounded endpoint theorem is claimed without checking the later pressure bootstrap under the extra assumption.

## 5. Consequence for the campaign

The campaign parameter relation is alpha=(1-c)/c. The disputed alpha=0 corresponds to c=1, whereas the campaign has 2/5<c<1/2 and alpha between1 and3/2. The constant field fails velocity decay and does not refute the campaign, its cited energy-growth corollary, or its separate vorticity criterion. A quotation of the archived bounded theorem should omit this literal endpoint or explicitly state the unresolved qualification. No assertion is made about the wording of the uninspected published journal version.

## 6. Verification scope

All five submitted sections and all six independent sections were read. The primary equation, kernel normalization, theorem range, local energy assumption, total-energy disclaimer and equation(38) were checked against actual manuscript pages. The constant example and limits were derived independently without computation. The source comes from the external referee (a second model) literature agent; this finding is submitted for continued comparison through the existing configured model agents, with provider runtime unattested. The campaign's main conjecture remains open.
