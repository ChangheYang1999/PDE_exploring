# Scope audit of the refreshed literature handoff

Status: independent comparison of the full eight-section guide, completed with the existing Theory Agent C  comparison. This is an audit of source scope and mathematical deductions, not a new Liouville theorem.

## 1. Exact object and evidence boundary

The object is the literature agent's in the team records at SHA256
3e4aee2d2187fed920139db6f77f42edce80e4fa9e5a662c7838e48800805cb2.
The previous guide at978b3bb8 was confirmed in A3019-A3020. Both complete
pins and the full70-line difference are retained in verification.
All eight current sections and every changed line were read. The earlier
seven-section independent audit remains a dependency for the unchanged
literature statements; it is not represented as a fresh reading of every
underlying manuscript.

The precise question is whether the revised guide asserts an unconditional
nonexistence theorem for whole-space C2 divergence-free profiles tending
uniformly to zero, with2/5<c<1/2 and every finite omega, or omits a necessary
hypothesis from one of the new compressed theorems. No such mathematical
scope error was found in the changes inspected below.

## 2. New literature and status material

The added Chae1306.5839v1 row states a C1 forced-Euler theorem on R^N,
N>=2. It keeps globally one-signed work D=Phi.v, strictness D=0 exactly
where v=0, and |v|^2+|p| in L^(q/2) for finite q>3N/(N-1). Those are
the premises of the inspected source statement. Its actual pages1-6,
including the forced-Euler proof, were separately read in the work-sign
reconstruction, and the retained images of pages2 and5 were inspected.
The present guide correctly separates the submitted scalar extension from
the printed theorem. No C0 interpretation of the source's unelaborated
k=0 notation or full Navier-Stokes proof is certified.

The ordinary Liu entry adds the independently completed C1 reconstruction
A3059-A3060. It does not remove the actual-period-map condition from the
rotating theorem. In particular ordinary stationarity remains distinct
from rotating-coordinate stationarity, and setwise approach to a periodic
orbit is not substituted for convergence to a sampled periodic point.

The LIT358 status now cites A3011-A3013. Its counterexample has target
dimension k+1 and constant C>1/4 in the auxiliary complex-vector inequality;
zero padding permits larger targets. It supplies neither an Euler profile
nor a result for target dimension at most k. This agrees with the confirmed
scope and leaves the method example separate from the PDE conclusions.

The new six-version construction paragraph agrees with the A3069-A3071
screen. Direct differentiation of
u(x,t)=tau^(gamma-1)U(x/tau^gamma), tau=T-t,
gives the profile coefficients1-gamma and gamma, so c=gamma>1 in the
inspected exact family. The finite-energy theorem is asymptotic. The
boundary source's earlier odd-G theorem is distinguished from its later
exact-odd Gamma-and-G formulation. The pending-status sentence records the
author's checkpoint view; A3069 now supplies the designated confirmation
with its page-specific and coefficient qualifications. No complete
construction proof is certified by this paragraph.

## 3. Pressure symmetry and its growth hypotheses

Section8 item1 retains all premises of A3047: U and P are C1, div U=0,
the full rotating equation holds,0<c<1/2, omega is finite, and U is uniformly
sublinear. The pressure symmetry or zero-angular-momentum premise is on
one ball B_R for which

    B(y).y >= delta |y|^2 for all |y|>=R, delta>0,
    B=(cI-omega J)y+U.

This is the absorbing ball used in the proof, not an arbitrary small ball.
Sublinearity supplies one such ball when pressure symmetry is global.
The conclusion is U=b e_z and P=-(1-c)b z+p0; uniform decay forces b=0.
The proof uses local integrability of Omega_theta/r. It does not assume the
quotient is bounded or impose symmetry on U as a starting hypothesis.

Item2 states E(R)=o(R^3) separately for the source-pressure symmetry result,
where E(R)=integral_(B_R)|U|^2 and q=tr((DU)^2). This premise is indispensable
to the cited argument eliminating harmonic pressure increments. Combining
global axial symmetry of q with item1 first gives an axial constant U.
The retained mean-energy premise then forces that constant to be zero,
since for a constant b,

    E(R)/R^3=(4pi/3)|b|^2.

The guide's zero conclusion is therefore justified. Omitting the premise
would make the statement false: a nonzero horizontal constant b with
P=-[(1-c)b+omega Jb].y has q=0 and solves the full equation but its pressure
is non-axisymmetric in the target range. Indeed the horizontal coefficient
has square norm ((1-c)^2+omega^2)|b|^2>0. The guide explicitly records this
control and does not repeat the separate report's missing-premise error.

## 4. Source-sign and cumulative-pressure summaries

Item3 retains C1 divergence-free U and E=o(R) for the kinematic spherical
source theorem. The positive Hessian is correctly attributed to the
uncut function f=sqrt(1+|y|^2). In the compact test f chi_R the additional
Hessian terms have error at most C E(2R)/R. No positivity is assigned to
the complete compactly supported test. The proof thus has the exact
boundary control required by A3056.

For bounded full C1/C1 profiles with weak dilation Hb and0<c<1/2,
A3053 supplies E=o(R), hence also E=o(R^3). Boundedness separately
supplies uniform sublinearity. A nonzero profile therefore has both signs of the spherical
source mean and both signs of the axial source mean; it has at least one
nonzero angular mode shared by q and the actual P. These are compatible
necessary properties, not a contradiction. No finite Fourier truncation
is introduced.

Item4 retains the identity

    A(r)=integral_0^r s S(s) ds=r N(r)-E(r),
    S(r)=integral_(B_r) q,
    N(r)=integral_(partial B_r)|U.e_r|^2.

Under the stated E=o(r), eventual A>=-C gives total energy at most C.
Eventual S>=0 supplies some such lower bound because A'=rS>=0 there.
It does not give total energy zero by itself. For the actual C1 pressure,
S=-4pi r^2 pbar'(r), with no unprescribed harmonic normalization.
The subsequent zero conclusion explicitly uses the full bounded-Hb
profile and2/5<c<1/2. The critical exponent is not included in that
finite-energy exclusion.

The quantitative negative-radius conclusion uses
E=Lr^beta+O(r^(beta-1)),0<beta<1, and the integrated inequality
A<=rE'-E. It does not differentiate the error term. It is already a
consequence of the energy theorem and the exact radial identity; it is
not a further incompatible requirement. No pointwise asymptotic for A
is claimed. This matches A3063-A3064.

## 5. Inventory and remaining scope

The manifest at SHA256
88c41ddbe8964158ba8d25cb7d2e7fb2c41e649cb79a1108c0da5118ce893959
contains155 distinct registered manuscript paths. Each path was checked
for a PDF header and agreement with its registered byte count. All passed;
the per-file record is in the team records. This verifies
the inventory count at this snapshot only. It does not certify a fresh
hash of all155 files, their completeness, or full reading of them. The six
construction-PDF hashes were separately checked in A3069's evidence.

The guide retains the missing2023 main manuscripts, the source-specific
reading boundaries, viscosity and rotation-range restrictions, the C2
versus smooth coverage distinction and the helicity-sign condition. It
uses the accurate statement that the extra symmetry, sign and monotonicity
premises are not known to follow from decay. It does not claim a full-PDE
counterexample to those implications.

The final pending list is a checkpoint list, not a new negative verdict.
By the completion of this comparison, all five listed results have their
own confirmations: LIT366 in A3075, LIT368 in A3084, LIT369 in A3072,
LIT370 in A3087 and LIT371 in A3079. Their open extensions in A3074,
A3077, A3081, A3086 and A3089 remain open. These later verdicts do not
retroactively supply any missing proof in the guide. Its dated pending
sentences should be read historically, not as current queue information.
The main arbitrary-rotation conjecture remains OPEN.

## 6. Existing-agent comparison and the refreshed file inventory

The complete five-part C comparison of 2026-11-04T08:34:51Z is retained
in the team records, SHA256
05ecda9fe88df2623ad081136bd1ec3eeca53dfd7c2b1f71ad23cbd9085828b5.
It compares the full guide, the full 70-line difference and this review's
original five sections. Its conclusions agree with Sections 2-5 above.
The following checks address the substantive points independently of its
diagnostic scripts.

For a generic differentiable velocity, put
M=(1-c)U+((cI-omega J)y+U).grad U+omega JU and Gamma=(Jy).U.
Skew symmetry of J and the product rule give

    (Jy).M = B.grad Gamma+(1-2c)Gamma.

For a full profile, this equals minus the angular pressure derivative.
On the prescribed backward-invariant ball, pressure symmetry therefore
makes Gamma grow as exp((1-2c)t) under backward time. Gamma is bounded
there, so it vanishes when 0<c<1/2. The converse follows from the same
identity. This verifies the equivalence used in guide item 8.1 without
assuming that U is axisymmetric.

For a horizontal constant b, direct substitution gives the pressure
coefficient (1-c)b+omega Jb and its squared norm
((1-c)^2+omega^2)|b|^2. Thus its pressure is not axisymmetric in the target
range despite q=0. This checks the need for the separate mean-energy
hypothesis in item 8.2. In item 8.4, A>=-C and N<=E' give
rE'>=E-C. Hence ((E-C)/r)'>=0; its limit is zero under E=o(r), so E<=C.
Finally the divergence theorem applied to -Delta P=q gives
S=-4pi r^2 pbar'. No harmonic-pressure choice enters these deductions.

The unchanged threshold conversions follow by substituting
alpha=1/c-1 with c>0. For an equivariant field,
(Jy).grad U=JU, so the rotation generator vanishes. This cancellation
concerns precisely the equivariant mode; it supplies no estimate for
other angular modes. The C comparison retains this restriction.

C also reported a complete registered-file hash check. Independently,
at 2026-11-04T08:39:31.039343+00:00 this agent read each registered PDF
and checked its header, byte count and SHA256 against the refreshed
manifest at SHA256
372a3632a1b314cff9aa2759638652a3dd9302fb4098562e1671c656718decfd.
All 155 entries passed, with 155 distinct paths and 155 distinct hashes.
The complete manifest and per-file results are retained in verification.
This is a file-identity check. It certifies neither reading of all those
manuscripts nor their mathematical correctness. The other C diagnostic
scripts and their executions are not certified here.

This audit uses the existing configured model agent comparison;
actual provider execution is independently unattested. No new model
client, mathematical computation or primary-source retrieval was used.
Missing main manuscripts, unread construction proofs and the
unrestricted rotating conjecture remain outside the confirmation.
