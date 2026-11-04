# Scalar identities on a regular basin: exact consequences and limitations

## 1. Hypotheses and notation

Let U in C2(R3;R3), P in C1 solve the exact divergence-free rotating profile equation with U(y) tending uniformly to zero, 0<c<1/2, and arbitrary finite omega. Put A=cI-omega J, B=Ay+U, Omega=curl U, a=1-2c, kappa=1+c, d=3c, q=|U|2/2, g=U.B, h=U.Omega, and H=P+q+(Ay).U. The complete carrier flows are Phi_t and Psi_t=Phi_-t. Then

    aU+grad H=B cross Omega,
    BH=-ag, Omega H=-ah, [B,Omega]=-kappa Omega.

Let V be the full basin of a compact transitive regular backward attractor with the precise periodic-orbit and complete-vortex-line basin structure in A115/A118/A267. Every backward orbit from V stays in a compact set. No coverage of the entire vortical region by such regular basins is assumed. These are the hypotheses of the previously confirmed A310/A313 theorem.

## 2. Five equivalent conditions

The following are equivalent on V:

1. h=0.
2. H is constant on every vortex line in V.
3. g is constant on every vortex line in V.
4. There is a T>0 such that g composed Psi_T=g on V.
5. H is one constant on V.

The Lamb identities give 1 iff2. Applying the commutator to H gives

    Bh+kappa h=Omega g.                                 (1)

Thus 1 implies3. Conversely, 3 and(1) give h(Psi_t x)=exp(kappa t)h(x). The negative carrier orbit is compact and h continuous, so boundedness forces h(x)=0. This proves3 implies1 without a mixing or pressure-normalization assumption.

Condition1 implies4 by the periodic weak-stable-trace and basin argument fully proved in A310/A313; any period of a periodic orbit can be used. A313 proves4 implies5 for an arbitrary positive T: the periodic mean square of g is invariant, constant by transitivity and basin attraction, and zero by invariant-shell density and E(R)=o(R). Finally5 implies1 by Omega H=-ah. If5 holds then g=0, so4 holds for every positive T, not merely periodic-orbit periods.

This confirms the stated equivalences in SIGN_CHANGING_HELICITY Section1. It excludes periodicity of the particular observable g when h is nonzero somewhere on V. It does not classify every observable constructed from H,g,h. For example, constants are always invariant; any intended claim about nonconstant functions of those variables needs its own definition and proof. A theorem about g cannot justify the unrestricted sentence that no periodic observable built from H,g,h exists.

## 3. The pressure moment

Let mu be any compactly supported Phi-invariant probability. No SRB property is needed in this section. The profile equation gives

    BU=-[(1-c)I+omega J]U-grad P,
    BB=AB-[(1-c)I+omega J]U-grad P.

Differentiate g=U.B and cancel the skew terms:

    Bg=-ag-(1-c)|U|2-(B+U).grad P.                       (2)

All functions are continuously differentiable on the compact support. Invariance therefore permits integration of B(Hg). Since BH=-ag,

    a integral g2 dmu=integral H Bg dmu
      =-a integral Hg dmu-(1-c) integral H|U|2 dmu
        -integral H(B+U).grad P dmu.                    (3)

In fact integral Hg dmu=0 by integrating B(H2)=-2aHg. The displayed Section2.4 pressure moment is correct, with this redundant zero term retained. No term on the right has a sign supplied by the argument. The assertion that this is the only possible identity is not a mathematical conclusion of(3).

## 4. Exact scope of the scalar gauge

For any C2 scalar H and fields with div B=d, div Omega=0 and [B,Omega]=-kappa Omega, define g=-BH/a and h=-Omega H/a. Then(1), the orbit-integral identities and periodic-orbit integrals of g are kinematic consequences. Set the additional scalar R=H-g. A direct computation gives

    2ah+div(hB+R Omega)=0.                               (4)

Indeed its left side is Bh+(d+2a)h+Omega H-Omega g, which equals Bh+kappa h-Omega g because d+a=kappa.

For H'=H+F, g'=g-BF/a, h'=h-Omega F/a, the same identities hold provided

    R'=H'-g'=R+F+BF/a.                                  (5)

Thus the gauge observation is valid for this abstract scalar system. For actual Euler R=P-q. If the original P and U are held fixed, that coefficient does not change as in(5), and(4) need not be preserved. Its new residual with fixed R is

    -Omega(F+BF/a).

This is not identically zero for arbitrary F. At any point where B and Omega are linearly independent, prescribe dF=0 and a symmetric Hessian with Hess F(Omega,B) nonzero to obtain a nonzero residual. A compactly supported C2 function realizes that jet. Such regular vortical points exist on the regular basin considered here by the audited transverse structure.

Accordingly the statement that the transformed triple preserves every displayed identity with the same actual P-q is false. The correct gauge comparison transforms R too and explicitly drops g=U.B, h=U.Omega and the physical pressure relation. It shows only that the reduced abstract identities, considered separately from those definitions and the energy/normal Lamb inputs, cannot force H constant. It is not an Euler counterexample and not a theorem excluding every future scalar argument.

## 5. The little-o helicity-tail remark

Section3(a) of the submission conditionally claims an ordinary integral of h over V is zero from |U||Omega|=o(r^-3), using a cutoff flux of H Omega. Two justifications are missing as written.

First, little-o at this borderline does not by itself imply absolute integrability: the smooth-at-infinity scalar r^-3/log r has that little-o bound and infinite integral of its absolute value in R3. This scalar example does not assert it is Euler helicity; it disproves the purported integrability implication from the displayed bound alone.

Second, the cutoff contains H Omega, including P Omega. A bound on U Omega alone does not estimate this pressure contribution in the submitted proof. Tangency to an invariant rough boundary is not a replacement for estimating the flux at infinity. One may use flow invariance to remove the internal boundary rigorously, but the outer flux still needs control.

The valid alternatives already available are stronger in appropriate senses. A123 gives total cancellation whenever either signed part of h is integrable on a vortex-invariant measurable set. A283 implies directly that on every invariant open V, either h=0 or it takes both strict signs, with no tail premise. Under Dini, A302 supplies the required absolute integrability and finite cancellation. The ordinary finite-integral conclusion under the stated little-o hypothesis alone remains OPEN. This does not refute that conditional theorem if an additional Euler argument could supply the two missing bounds.

## 6. Evidence and audit scope

The entire submitted note is retained with a SHA256 hash in the team records. Sections2 and3 are independently confirmed. Section4 confirms the correctly transformed abstract scalar system while refuting preservation of the same fixed pressure coefficient. The unrestricted observable and little-o integration inferences are not established. The full nonexistence problem and the single-basin constant-H exclusion remain open.
