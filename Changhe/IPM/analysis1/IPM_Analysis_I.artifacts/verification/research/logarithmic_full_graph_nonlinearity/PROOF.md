# Quadratic IPM discontinuity in the full logarithmic graph norm

This standalone argument precedes its finite checks. Status OPEN until independent checking, actual Claude Opus5.5 review, resolution of objections and later own adjudication. It applies the transverse mechanism of topic36 to the actual canonical trial with exact compact potentials. It is distinct from topic177, which used an equilibrium and a weaker first-order weighted norm.

## Statement and notation

Let rho be the exactly joined and canonically normalized modal_v2 density, k its exact exponent, ell=1/k, and V=ell X+U[rho]. The full-plane canonical velocity is U[f]=(-psi_y,psi_x), where -Delta psi=partial_xf and U=o(r) at infinity with the prescribed parity. Set Sigma(f)=psi[f]_xy(0), J(f)=a_f(0) when f=x²y a_f, and

 Lh=V.grad h-h+U[h].grad rho+(Sigma(h)/3)X.grad rho,
 Q(h)=U[h].grad h+(Sigma(h)/3)X.grad h.

For every fixed real b and every finite s>=0 define

 ||h||Y=||exp((1/2-b)z)h(exp z,y)||H^s(R²_(z,y)),
 ||h||graph=||h||Y+||Lh||Y.

The Sobolev norm uses the unitary Fourier transform and multiplier (1+|xi|²)^(s/2). D_cp below is a linear space of smooth compact densities h=-Delta f, with smooth compact even-x/odd-y potentials f supported in a fixed finite union of patches away from both axes. Every element satisfies J=Sigma=0, has a smooth compact x²y factor and compact canonical velocity. The patches are chosen inside a region where the actual background is smooth. Thus h,Lh,Q(h) belong toY for everyh inD_cp.

For each b,s there exist g and a sequenceh_n inD_cp, and constantsC,c>0, such that

 ||g||graph+sup_n||h_n||graph<=C,
 ||U[g].grad h_n+U[h_n].grad g||Y>=cn-C.              (1)

More strongly, put v_n^+=n^(-1/2)(g+h_n) and v_n^-=n^(-1/2)(g-h_n). Then

 max(||v_n^+||graph,||v_n^-||graph)->0,
 liminf_n max(||Q(v_n^+)||Y,||Q(v_n^-)||Y)>=c>0.      (2)

Hence Q has no continuous extension at0 from this full linearized graph topology toY. In particular no finite quadratic bound ||Q(h)||Y<=C0||h||graph² holds on any positive-radius graph ball containingD_cp. The same conclusion holds on any larger domain whose norm on this class is bounded above by a constant times the stated graph norm. It does not hold by this argument for an arbitrarily stronger domain norm.

All perturbations preserve every center jet, the scalar scaling normalization and every exterior coefficient exactly. This obstruction is local and has no tail-estimate premise. It does not show that L is closed or lacks an inverse, nor exclude any exact IPM profile, stronger topology, weaker target or scale-of-spaces method. No numerical value ofc orC is claimed.

## A smooth patch and an exact transverse velocity

The accepted exact background has DV(0)=diag(-A,D), with A=2/k-1>0 and D=4/k-1, and V(0)=0. Its finite inner power and logarithm formulas are smooth on the punctured inner disk. These assertions concern the exactly joined, normalized trial, not its literal unjoined coefficient formula. AlongP_t=(t,t), differentiability gives V1(P_t)=-At+o(t). Choose t>0 sufficiently small thatP=P_t is in the inner disk andV1(P)!=0. This is an existence choice justified byA>0, not an asserted numerical location or quantitative bound.

There are nested open disks B0 with closure insideB1, closureB1 insideB2, all in the positive quadrant and in that punctured inner disk, and all four reflections ofB2 are disjoint. Shrink them further below as needed. The density, canonical velocity andV are smooth near their closures. For the velocity this follows directly from its finite angular Green formulas on any open positive-radius region of the inner representation; powers and logarithms are smooth there.

Construct flow coordinates (tau,v) by flowing the vertical curve (p,q+v) throughP=(p,q) underV. At(tau,v)=(0,0), the two columns of the coordinate map areV(P) ande_y, whose determinant isV1(P)!=0. Smooth local ODE existence and the inverse function theorem give a smooth coordinate diffeomorphism after shrinking the disks. Let phi(X)=v be its second inverse coordinate. Then

 V.grad phi=0, phi_y(P)=1.

Continuity permits shrinkingB1 so phi_y>1/2 there. In particular gradphi is nonzero onB1. Choose a real nonzero smooth amplitudea supported compactly inB0. All derivatives ofa vanish near the boundary ofB0.

Choose a smooth cutoffeta supported inB2 and equal to1 on a neighborhood ofclosureB1. Set on the positive patch

 F(X)=eta(X)(x-p)²/2.

ExtendF by even reflection inx and odd reflection iny, using the four disjoint supports. It is a globally smooth compact potential. Put g=-DeltaF. OnB1,

 g=-1, gradg=0, U[g]=(0,1).                           (3)

The same gradient vanishing holds on the other three reflected copies ofB1. ThusU[g] is exactly transverse toV atP. The cutoff does not create a nonlocal tail: the canonical stream isF_x and U[g]=(-F_xy,F_xx) everywhere.

Here is the canonical identification for any smooth compact potentialf of this parity. Ifh=-Deltaf, thenpsi=f_x solves -Deltapsi=partial_xh and gives U=(-f_xy,f_xx), compact and of the required component parity. The difference from any other sublinear canonical velocity is a harmonic vector field witho(r) growth. The mean-value derivative estimate for each component on a circle of radiusR about an arbitrary pointP0 is at most2sup_boundary|H|/R. The boundary radii are betweenR-|P0| andR+|P0|, so this tends to0. Every derivative is zero and the difference is constant; parity kills that constant. This proves uniqueness in the full o(r) gauge. Sincef vanishes near0, Sigma=f_xxy(0)=0. The density also vanishes there, soJ and all its center jets vanish. Division byx²y on the compact support gives a smooth compact even-even factor, extended by0 off that support.

## The Sobolev estimates used on fixed patches

For any fixed smooth compact amplitudeB(tau,v),

 n^(-s)||B(tau,v) exp(i n v)||H^s -> ||B||2.

Indeed, after Fourier translation its squared left side is

 integral [n^(-2)(1+xi_tau²+(xi_v+n)²)]^s |Bhat(xi)|² dxi.

The bracket tends to1 and is bounded forn>=1 byC_s(1+|xi|²)^s. Dominated convergence applies. For sine or cosine, the limit is||B||2/sqrt2. To check the mixed term between opposite translations, first truncateBhat to|xi|<=R. The translated truncations are disjoint forn>R. The remaining weighted Fourier tails are uniformly bounded byC_s times theH^s tail ofB, using the same bracket inequality and Cauchy-Schwarz. Letn increase and thenR increase. This proves both lower and upper bounds for nonzero real amplitudes without a stationary-phase assumption.

Smooth coordinate changes and smooth nonvanishing weights give equivalentH^s norms on fixed compactly contained patches. For clarity, for0<theta<1 the difference seminorm has kernel |X-Y|^(-2-2theta). Plancherel and rotation/scaling of integral|exp(i xi.W)-1|²|W|^(-2-2theta)dW give the positive finite Fourier symbolC_theta|xi|^(2theta). A bi-Lipschitz coordinate map with bounded Jacobian compares the local double integrals in both directions. Pairs with one point outside a larger chart are bounded by theL2norm because the support is separated from its boundary. A smooth multiplier is bounded by splitting its product difference; the coefficient difference isO(min(|X-Y|,1)), whose squared kernel is integrable. For s=m+theta use the chain and product rules throughm and these fractional estimates for each term. Lower derivatives are bounded by theH^s norm. The inverse coordinate map supplies the reverse estimate. Integer orders follow from the chain rule. These arguments apply to the flow chart, x=exp z and the weight exp((1/2-b)z) because all supports remain inside a fixed positive-x compact patch.

To pass from one positive patch to the wholeYnorm, use a smooth cutoff supported in that patch. Its multiplication is bounded onY by the preceding estimates. This supplies a lower bound on the full norm from the selected patch. For upper bounds use the triangle inequality over the finite reflected pieces. No orthogonality between disjoint physical supports is presumed for fractional orders. Constants can depend onb,s and the fixed patches.

## Compact oscillating potentials and their full graph bound

OnB0 set

 f_n=n^(-s-2) a(X) cos(n phi(X)), h_n=-Delta f_n,

and extendf_n with the same even-x/odd-y four-patch reflection before taking the Laplacian. These are inD_cp. Their velocities are exact compact derivatives of their potentials. On the positive patch put

 A0=a|gradphi|², A1=2grada.gradphi+aDeltaphi, A2=Deltaa.

Direct differentiation gives

 h_n=n^(-s)A0cos(nphi)+n^(-s-1)A1sin(nphi)
     -n^(-s-2)A2cos(nphi).                            (4)

Since V.gradphi=0,

 V.grad h_n=n^(-s)(V.grad A0)cos(nphi)
     +n^(-s-1)(V.grad A1)sin(nphi)
     -n^(-s-2)(V.grad A2)cos(nphi).                    (5)

Each velocity component has the same three amplitude orders n^(-s), n^(-s-1), n^(-s-2). More explicitly,

 U1[h_n]=n^(-s)a phi_x phi_y cos(nphi)
  +n^(-s-1)(a_x phi_y+a_y phi_x+a phi_xy)sin(nphi)
  -n^(-s-2)a_xy cos(nphi),
 U2[h_n]=-n^(-s)a phi_x² cos(nphi)
  -n^(-s-1)(2a_x phi_x+a phi_xx)sin(nphi)
  +n^(-s-2)a_xx cos(nphi).                             (6)

Every amplitude in(4)--(6), including those differentiated byV, is fixed smooth and compact. The modulation estimates and coordinate equivalence therefore give uniformYbounds for h_n,V.grad h_n,U[h_n].grad rho. The background gradient is smooth on the fixed support and can be multiplied by a compact cutoff before applying the multiplier bound. The reflected pieces obey the same estimates: V is equivariant under coordinate reflections, so the reflected phases are still first integrals. The rank-one term vanishes becauseSigma(h_n)=0. Thus||h_n||graph<=C.

The same support and smoothness argument shows g,Lg inY. Every element ofD_cp has compact canonical velocity; multiplying it by the smooth background gradient keeps the support in those fixed patches. Consequently no behavior ofrho at0, at a join or at infinity enters the graph estimates beyond the proved existence of the chosen smooth patch.

## The cross term grows linearly

BecauseU[h_n] is supported in the same compact subset of the reflected copies ofB0 asf_n, (3) gives exactly

 U[h_n].grad g=0 onR².

On the positive patch the other cross term is U[g].grad h_n=partial_yh_n. From(4),

 partial_yh_n=-n^(1-s)A0 phi_y sin(nphi)+R_n,
 ||R_n||Y<=C on that fixed patch.                     (7)

The remainder bound follows by differentiation of the three terms: after the displayed leading term, the largest amplitude order is n^(-s). The leading fixed amplitudeA0phi_y is nonzero, becausea is nonzero, |gradphi|>0 andphi_y>1/2. Pull back to the flow chart and apply the sine lower bound. Coordinate equivalence and bounded localization then give

 ||U[g].grad h_n+U[h_n].grad g||Y>=cn-C.

This proves(1). The exact cancellation of the second cross term uses compact potentials and the quadratic plateau inF. It does not assume a global order-zero multiplier estimate in the weighted space.

## Quadratic discontinuity and the normalized residual difference

OnD_cp, Sigma=0 and the canonical velocity map is linear. Thus the exact polarization identity is

 Q(g+h)-Q(g-h)=2(U[g].grad h+U[h].grad g).

Forv_n^+ andv_n^- in(2), this gives

 ||Q(v_n^+)||Y+||Q(v_n^-)||Y
 >=(2/n)||U[g].grad h_n+U[h_n].grad g||Y
 >=2c-2C/n.

Their graph norms areO(n^(-1/2)). Taking the larger output gives(2). If a single sequence is desired, choose the plus sign when itsYnorm is at least the minus norm and the minus sign otherwise. This is a well-defined mathematical selection from two smooth compact tests, not a numerical sign-selection algorithm. A continuous extension at0 would force both output norms to0, a contradiction. The quadratic bound is therefore impossible on every positive-radius graph ball containing the class.

There is also a residual-difference conclusion, with its convention explicit. For the canonically normalized background define c_l(rho+h)=(1+Sigma(rho)+Sigma(h))/3 and F(rho+h)=(c_l(rho+h)X+U[rho+h]).grad(rho+h)-(rho+h). The canonical uniqueness argument gives U[rho+h]=U[rho]+U[h]. Exact expansion gives

 F(rho+h)-F(rho)=Lh+Q(h).

Along the selected sequence from(2), the norm of this difference has positive lower limit, because||Lh||Y tends to0. The difference is compactly supported and inY; no assertion thatF(rho) itself belongs toY for everyb,s is required. Allh here satisfySigma=0, so the scalar scaling parameter actually remainsell.

The result rules out this ordinary quadratic closing estimate in the indicated full logarithmic graph topology. It makes no assertion about the existence of a closed realization ofL, a linear inverse in a different domain, the endpoint of any other estimate, or a decisive PDE YES orNO. Adding finitely many center-jet conditions cannot remove these packets, since they vanish near0 identically. A stronger norm controlling transverse derivatives, a weaker image norm, or a scale of spaces remains possible.

## Verification plan and dependencies

The exact joined-normalized modal trial and its origin derivative and smooth inner formulas are inherited from the accepted parent chain. Both new codes will reread the exact k and relevant data by rawNPZ/Fraction and manualintegerhex/fmpq routes and rehash the parent pins. The primary symbolic route and an independent rational differential-jet algebra will reconstruct(3)--(7), the compact canonical identity, reflection covariance and polarization. They will factor out the common spatially constant n^(-s) when checking the finite wave identities; the analytic modulation proof handles arbitrary real s.

No new interval enclosure or numerical norm constant is proposed. The local flow-box, all-order Sobolev estimates, compact support and discontinuity arguments must be reviewed mathematically. Topic36 is a conceptual predecessor, not an assumption that its conditional IPM application was already verified. Topic177 concerns a different norm and is not used in this proof. Actual Opus5.5 must review the full proof and executed evidence, and a later independent adjudication must resolve objections before any FINAL verdict.
