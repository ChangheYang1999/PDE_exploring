# Sign and translation restrictions on the pressure source

Status: CONFIRMED A3044 at the exact hypotheses below, with comparison A3045 and scope A3046.

## 1. Exact statements and dependencies

Let 0<c<1 and omega be any finite real number. Set J(x_1,x_2,z)=(-x_2,x_1,0), A=cI-omega J, and B(y)=Ay+U(y). Suppose U belongs to C^1(R^3;R^3), P belongs to C^1(R^3), and

    (1-c)U+(B.grad)U+omega JU+grad P=0,   div U=0.

Write E(R)=integral_(B_R)|U|^2 and q=tr((DU)^2). Either of the following additional hypotheses implies U=0 and P constant:

1. Uniform sublinearity U(y)=o(|y|), E(R)=o(R^2), and q>=0 everywhere or q<=0 everywhere.
2. Uniform decay U(y)->0 and a nonzero translation a with q(y+a)=q(y). It is enough instead that some sequence |a_n|->infinity satisfies q(.+a_n)->q in distributions on every compact set.

No bound on DU, source integrability, pressure growth or pressure normalization is assumed. The two statements below are proved directly, without using the separate pressure-symmetry theorem. An optional corollary invokes the separately confirmed energy theorem A052 at its C1/C1 bounded weak-dilation scope. These are restrictions under additional hypotheses, not unconditional rotating nonexistence.

## 2. Double divergence and the two ways to force q=0

For a smooth divergence-free field, differentiating the product gives

    partial_i partial_j(U_i U_j)=partial_i U_j partial_j U_i=q.

For C1 fields, convolve locally with a smooth approximate identity in a neighborhood of the compact test support. Divergence is still zero; the fields and their first derivatives converge uniformly on that support. Passing to the limit in the smooth identity proves it in distributions. This avoids using second derivatives of U.

Choose chi in C_c^infinity(B_2), with 0<=chi<=1 and chi=1 on B_1, and set chi_R(y)=chi(y/R). For K=sup ||D^2 chi||_op,

    |integral q chi_R|=|integral (U tensor U):D^2 chi_R|
                     <=K R^-2 E(2R).

If q>=0, every fixed ball B_L has integral q bounded by this quantity for every R>=L. The right side tends to zero under E=o(R^2); hence the nonnegative continuous q vanishes on every ball. For q<=0, apply the same argument to -q. Big-O at exponent two would not make this cutoff argument close.

For the second statement, let phi be a compact smooth test. Uniform decay implies U(.+a_n)->0 uniformly on its support whenever |a_n|->infinity. Thus

    integral q(y+a_n)phi(y)dy
      =integral (U(y+a_n) tensor U(y+a_n)):D^2 phi(y)dy ->0.

No derivative decay is inferred or needed. An exact nonzero period gives a_n=n a and q(.+a_n)=q, forcing q=0. The stated distributional return condition gives the same conclusion by uniqueness of distributional limits. Continuity makes this a pointwise equality.

## 3. The actual harmonic pressure is constant

Taking divergence of the full momentum equation yields -Delta P=q. In index form the derivative of Ay in the transport contributes -omega sum J_ji partial_j U_i, while divergence of omega JU contributes the opposite contraction. The c div U terms vanish. The nonlinear term is the double divergence of Section 2. Thus this identity is valid distributionally under C1 regularity.

Both hypotheses of Section 1 imply E(R)=o(R^3). This is immediate from the stronger energy assumption in the first case. In the second, split the integral into a fixed compact ball and its complement where |U| is uniformly small, then let that bound tend to zero. Since q=0, Weyl regularity makes the actual P smooth and entire harmonic.

For completeness, set U_R(z)=U(Rz). Integrating the full momentum equation against a compact smooth scalar phi gives the vector identity

    integral grad P(Rz)phi(z)dz
      =integral U_R[(4c-1)phi+(Az).grad phi]
       -omega integral JU_R phi
       +R^-1 integral U_R[U_R.grad phi].

Here grad P(Rz) is the original gradient evaluated at Rz. The linear coefficient is -(1-c)+div(Az)=4c-1, and the quadratic sign is positive after integrating by parts. On any fixed B_L,

    ||U_R||_(L2(B_L))^2=R^-3 E(LR)->0.

The linear terms tend to zero by Cauchy-Schwarz; the last is bounded by R^-1 ||grad phi||_infinity ||U_R||_2^2. The argument also applies to phi(z-x/R) for any fixed x: their supports stay in one fixed ball and their required derivatives have common bounds for R>=1.

Take radial phi in C_c^infinity(B_1) with integral one. Every component of grad P is harmonic, so the spherical mean-value property integrated against this radial weight gives

    grad P(x)=integral grad P(x+Rz)phi(z)dz
             =integral grad P(Rw)phi(w-x/R)dw ->0.

The left side is independent of R, so grad P=0. Poisson's equation alone would not imply this; the full momentum equation and the vanishing mean energy remove its nonconstant harmonic freedom.

## 4. Complete characteristics and zero velocity

Uniform sublinearity gives |U(y)|<=C_epsilon+epsilon|y|. Thus the C1 field B has at most linear growth, and Gronwall's inequality bounds every local trajectory on a finite time interval in both directions. Local continuation therefore supplies a complete flow Phi_t.

For some R0, skew symmetry of J and sublinearity give

    y.B(y)>=c|y|^2/2   when |y|>=R0.

Every sphere of radius larger than max(R0,|y|) has strictly inward reverse-time vector field. The first-crossing argument keeps the entire backward orbit from y inside this fixed compact ball. General point convergence is neither asserted nor used.

With grad P=0, take the scalar product of momentum with U. Since U.JU=0,

    B.grad |U|^2=-2(1-c)|U|^2,
    |U(Phi_t y)|^2=exp(-2(1-c)t)|U(y)|^2.

Because c<1, a nonzero value would grow unboundedly as t->-infinity. Continuity on the compact backward orbit forbids this. Hence U=0, completing both statements. The strict c>0 is used in backward trapping and c<1 in damping.

## 5. Campaign consequence and exact tests

The already confirmed A052 energy theorem says that a C1/C1 full profile with bounded U and U(R.)->0 in distributions is zero for 0<c<2/5, has bounded E(R) at c=2/5, and has E(R)=O(R^(5-2/c)) for 2/5<c<1. For 0<c<2/3 these statements give E(R)=o(R^2). Boundedness gives sublinearity, so the sign criterion applies. At c=2/3 only O(R^2) is obtained; this proof supplies no endpoint conclusion.

Consequently a hypothetical nonzero uniformly decaying profile in the campaign interval must have both positive and negative values of q, and no nonzero translation period or distributional return of q at infinity. In the notation S=(DU+DU^T)/2 and Omega=curl U,

    q=|S|_F^2-|Omega|^2/2.

Neither global direction of the corresponding strain-vorticity inequality is possible for such a nonzero profile. This does not supply either inequality for an arbitrary candidate.

The following checks isolate hypotheses. Let f be smooth and compactly supported on R^2 with f(0)=1. The shear U=(f(x_2,z),0,0), P=0 is divergence-free, has q=0 and E(R)<=2R integral |f|^2, but its full residual at the origin is (1-c)e_1+omega e_2, nonzero for c<1. It is not a profile or a uniformly decaying whole-space field.

For real k, let M have horizontal block -I_2/2+kJ_2 and vertical entry 1, and set U=My. Then tr M=0, JM=MJ, and M+M^2 has entries (-1/4-k^2,-1/4-k^2,2). The pressure

    P=(1/8+k^2/2)(x_1^2+x_2^2)-z^2

cancels the full residual (M+M^2)y for every c,omega. Its source q=3/2-2k^2 can have either sign or vanish. At k^2=3/4 the pressure is harmonic and nonconstant. These fields have linear growth and E of order R^5, so they test precisely why the growth and energy assumptions cannot be silently removed. They are not decaying counterexamples.

## 6. Verification scope

All seven source sections, all eighteen author checks, Theorem A's setting and statement, and the energy-law corollary through Section 3 were read. The optional corollary uses A052 as a named existing result; its energy proof is not freshly certified by this argument. The pressure proof and both criteria are otherwise independent of LIT359-LIT361. No numerical or symbolic computation was needed or performed. The complete existing A113 and C07:02:05 comparisons were read; their detailed assessment follows. Actual provider execution is independently unattested.


## 7. Completed existing-agent comparison

The full A113 comparison and the full C note of 2026-11-04T07:02:05Z were read. Their analytical derivations agree with Sections 1-6. A113 correctly distinguishes the use of translations in the second criterion from the weak-dilation condition Hb used by the optional energy corollary. Hb alone was not substituted for uniform decay in the translation argument. Both comparisons preserve the strict c<1 damping and the strict c<2/3 energy-corollary endpoint.

The pressure-averaging step is directly proved in Section 3. The comparisons' phrase referring to LIT361 with Q=I describes the same evaluated-gradient and radial-mean mechanism; substituting Q=I into the symmetry conclusion alone would be tautological and is not the proof used here. A113's seven-item diagnostic and the C note's twenty-three-item diagnostic, including their in the team records, were not read or rerun and are not certified by this audit.

C item14 observes that a sign of the angular mean of q would give only a constant angular mean of P through the displayed projection argument, leaving other angular modes unrestricted at that step. This is a limitation of that argument alone. It is not a theorem that weaker averaged sign conditions cannot imply nonexistence by additional estimates. No such impossibility is part of the confirmed result.

The exact countertests and the named energy dependency remain as stated. These criteria supply necessary restrictions on any nonzero target profile, without producing or excluding an unrestricted rotating profile.
