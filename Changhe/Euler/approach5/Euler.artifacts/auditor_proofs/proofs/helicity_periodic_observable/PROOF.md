# Periodic carrier observables and the corrected Bernoulli normalization

## 1. Exact setting and claims

Let U in C2(R3;R3), P in C1(R3) solve

    (1-c)U+(B.grad)U+omega J U+grad P=0, div U=0,
    B=Ay+U, A=cI-omega J,

where 0<c<1/2, omega is any finite real number, J(y1,y2,y3)=(-y2,y1,0), and U(y)->0 uniformly at infinity. Let Phi be the complete B flow, Psi_t=Phi_-t, a=1-2c, Omega=curl U, h=U.Omega,

    H=P+|U|2/2+(Ay).U, g=U.B, E(R)=integral_(|y|<R)|U|2.

The exact Lamb identity is aU+grad H=B cross Omega, hence BH=-a g and Omega H=-a h. The pressure in H may differ from the canonical pressure by a constant. The energy theorem applies because boundedness and distributionally vanishing dilates Hb follow from uniform decay. For 2/5<=c<1/2 it gives E(R)=o(R), with E(R)=O(R^(5-2/c)) above2/5 and E(R)=O(1) at2/5. Below2/5 it already gives U=0.

For every open Phi-invariant V of positive volume and every fixed T>0,

    average_(V intersect {R<|y|<2R}) integral_0^T |g(Psi_t y)|2 dt
        <=C_(T,V) E(2R)/R ->0.                            (1)

If, in addition, V is the basin of a transitive compact regular backward attractor Lambda and g composed Psi_T=g on V, then g=0 and H is constant on V. This is B26-v2 Proposition HF-per. The regular-attractor hypotheses and supplied stable-leaf basin structure are those of A115/A118, not merely the almost-everywhere support properties of A308.

## 2. Mean-square estimate

Put M=sup|U| and d=3c. A092 gives constants delta>0 and R0 such that F_R=V intersect {R<|y|<2R} has volume at least delta R3 for R>=R0. Its hypotheses are bounded U and invariance of a positive-volume set. For R also sufficiently large, the ball of radius2R is forward invariant under Psi, since on its boundary

    (-B).y/|y|=-c|y|-U.y/|y|<=-2cR+M<0.

Liouville's formula gives det D Psi_t=exp(-dt). Thus

    integral_(F_R) integral_0^T |g(Psi_t y)|2 dt dy
      =integral_0^T exp(dt) integral_(Psi_t F_R)|g(z)|2 dz dt
      <=T exp(dT)(2||A||R+M)2 E(2R).

Divide by delta R3 and take R>=max(1,M). This proves(1), including both endpoint rates. No helicity assumption or pressure boundary integration occurs in this step. The finite constant depends on omega through ||A||, which is harmless for each arbitrary finite omega.

## 3. Periodicity and constancy

Set Q(y)=integral_0^T |g(Psi_t y)|2 dt. The periodicity hypothesis makes Q invariant under every Psi time by a change of integration interval. Q is continuous in a neighbourhood of Lambda. On the transitive compact set Lambda, continuity and a dense orbit make Q a constant q0>=0. If y is in its basin, dist(Psi_t y,Lambda)->0; invariance and uniform continuity near Lambda give Q(y)=q0. Equation(1) therefore implies q0=0. The nonnegative continuous integrand defining Q is identically zero, so g=0 on V.

Consequently BH=0 on V. The same transitivity, continuity and basin argument gives one constant H on V. This proof needs no mixing alternative, no synchronized arithmetic phase, no SRB measure and no integrability of H. Alternatively A290 applies directly to the discrete-invariant g and already gives its vanishing on any such invariant open set without the attractor hypothesis; the attractor is still used to obtain one H value on all of V.

If h=0 on V, H is constant on every complete vortex line. A267 supplies density of the weak stable trace of any periodic orbit in Lambda. For its period T, H composed Psi_T=H first on that trace, then on Lambda by continuity, then on all V by the supplied complete-vortex-line basin representation. Differentiating along Psi gives g composed Psi_T=g. Section3 proves B26's main theorem. Separate almost-everywhere coverage by these regular basins then gives U=0 through A265. This is the already confirmed A310/A291 conclusion.

## 4. Two scope repairs in the submitted prose

The reduced H used throughout the proof is correct. Its comparison with the original unreduced Bernoulli function is not. With X=cy+U, the original definition in EXACT_IDENTITIES is

    H_old=P+|X|2/2+c(c-1)|y|2/2-omega(Jy).X.

Expanding the squares and using (Jy).y=0 gives

    H_old=H-c(1-2c)|y|2/2.                                (2)

Thus the difference is not c|y|2/2. Nor is a nonconstant quadratic term irrelevant when differentiating a Bernoulli function: the corresponding identities are aX+grad H_old=B cross Omega and aU+grad H=B cross Omega. Equation(2) exactly transforms one into the other. The displayed reduced identity and all arguments in Sections1-3 remain valid.

B26-v2 Remark1 also says that a constant-roof regular attractor of a profile must fail h=0 on its basin. The theorem proved here gives only H constant on that one basin. It does not give U=0 on the basin, or exclude the attractor, without a further argument. A265 requires covering almost every vortical point by constant-H open sets. No such coverage follows from the existence of one regular basin, and A308's possibly singular supports cannot be silently replaced by regular attractors. The asserted single-basin exclusion remains OPEN. Remove it or state the additional global coverage premise.

The appendix's phase argument remains conditional on its unverified arithmetic/phase input. The new main proof avoids that input completely. Its success does not certify the original Bowen/Plante formulation.

## 5. Evidence and limitations

The complete B26-v2 submission is retained with its hash in the team records. Dependencies A092, A267, A290, A265 and the canonical-pressure energy theorem have already been independently audited. This check fixes the missing Hb citation flagged in A311. It supplies no new unrestricted nonexistence theorem, no automatic helicity condition and no regular-attractor coverage theorem.
