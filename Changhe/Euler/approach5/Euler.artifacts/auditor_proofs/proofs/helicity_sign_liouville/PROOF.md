# One sign of helicity on each essential basin forces a smooth decaying profile to vanish

## 1. Exact theorem

Let 2/5<=c<1/2 and omega be any finite real number. Let U in C-infinity(R3;R3) and P in C1(R3) solve

    div U=0,
    (1-c)U+[(cI-omega J)y+U].grad U+omega JU+grad P=0,
    U(y)->0 uniformly as |y|->infinity.

Set A=cI-omega J, B=Ay+U, Omega=curl U, O={Omega!=0}, a=1-2c>0, and h=U.Omega. For every compactly supported full-flow-ergodic vortical SRB probability supplied by A308, let D_nu be its invariant open essential basin from A223. If h has one sign on each such D_nu, with the sign allowed to depend on the basin, then U=0.

In particular U=0 if h>=0 everywhere or h<=0 everywhere. The hypothesis h=0 everywhere is included. No Dini strain decay, finite energy, axisymmetry, Fourier restriction, mixing or nonsingular uniformly hyperbolic support is assumed.

Equivalently, every nonzero smooth decaying profile in this range has at least one essential vortical SRB basin on which h takes both positive and negative values. Each sign then occurs on a positive-volume open subset of that basin. The associated measure gives full mass to B!=0 and Omega!=0, has spectrum (1-2c,0,-1-c), and entropy 1-2c. Its topological support may still meet either zero set.

This is a conditional Liouville theorem and a necessary sign-changing-basin condition. It does not exclude the sign-changing case and does not prove the full conjecture.

## 2. The basin data are now consequences of smoothness

A308 applies because B is smooth, complete and radially outward at infinity, div B=3c, and [B,Omega]=-(1+c)Omega, with 1+c>3c. It supplies countably many full-flow-ergodic vortical SRB measures whose continuous-time basins cover almost every point of O.

For these actual Euler fields, the one-form alpha=(B cross Omega).dy has the exact expanding covariance with rate a and is invariant under the local Omega flow. A207 gives strictly positive local unstable conditional densities, proportional to positive alpha-length. A223 therefore gives pairwise disjoint invariant open sets D_nu with Bas(nu) subset D_nu, full basin volume in D_nu, and nu(D_nu)=1. Their union covers O modulo a null set. All support, density and coverage premises used below have thus been supplied; they are not additional assumptions on the profile.

## 3. The sign hypothesis gives zero helicity on each basin

The complete Omega flow Gamma is almost everywhere recurrent for every C2 uniformly sublinear profile in this parameter range, by A048-A049. Its completeness follows from contracting its time parameter with the backward carrier flow, whose orbits are bounded. The sets D_nu are invariant under this complete flow: the exact conjugacy preserves continuous-time genericity along every finite vortex segment, and the defining full-volume property of the essential basin is preserved by the resulting C1 diffeomorphisms.

Let H0=P0+|U|^2/2+Ay.U, where P0 is the canonical pressure representative from A031. The exact Lamb and helicity identities are

    aU+grad H0=B cross Omega,
    Omega H0=-a h.

If h>=0 on D_nu, H0 is nonincreasing along each Gamma orbit there. If h were strictly positive anywhere, continuity would give a small open ball inside D_nu and a common positive vortex time on which H0 drops strictly. Almost every point of that ball is recurrent. Monotonicity prevents its H0 values from returning arbitrarily close to their initial values, contradicting recurrence and continuity. Hence h=0 on D_nu. Applying the same argument to -H0 treats h<=0. This is A283, with all invariance and completeness hypotheses checked here.

Thus the theorem's one-sign premise yields h=0 on every essential basin.

## 4. Bernoulli mean decay makes it constant on each basin

We recall the complete mechanism of A277-A278 to specify exactly which analytic information is used. Put beta=5-2/c, so 0<=beta<1. The canonical pressure and energy estimates give one fixed representative H0 with

    integral_(|y|<R)|H0|^2<=C R^(beta+2),    R>=1,
    integral_Q |H0(Phi_t y)|^2dy<=C_Q exp(-2a t)

for every bounded measurable Q, where Phi is the forward B flow. The second estimate uses det DPhi_t=exp(3ct) and |Phi_t y|<=exp(ct)(|y|+||U||_infinity/c). It assumes neither finite energy nor pointwise decay of P0.

Fix nu and its essential basin D_nu, now with h=0. Positive unstable conditional density gives a local unstable arc with a full-arclength set T of two-sided generic support points. At a regular point the unstable tangent, -B and Omega are independent. The map C(s,r,tau)=Gamma_tau Psi_r gamma(s) is a local C1 coordinate map in D_nu. The image E of T times a smaller rectangle has full volume in a small open box V.

Since Omega H0=0 on D_nu and the basin is invariant under the complete vortex flow, exact conjugacy gives, for all real t and y=C(s,r,tau) with s in T,

    H0(Phi_t y)=H0(Phi_(t-r) gamma(s)).

The right side stays on the compact invariant support. Its positive-time square average tends to integral H0^2 dnu, using the two-sided generic points. Dominated convergence over E, followed by the exponentially decaying spatial estimate above, gives

    Leb(E) integral H0^2 dnu=0.

Therefore H0 vanishes on supp(nu), by continuity. The same identity makes it vanish on every carrier translate of E and hence on every translate of V. Their invariant open union contains a support point and has positive nu measure. A nonnegative compactly supported observable inside that union has positive nu integral, so every basin point eventually enters it. Invariance places the whole basin in it. Since the basin has full volume in D_nu, continuity yields H0=0 on D_nu.

This step uses no integration by parts against a measure singular in the vortex direction. It does not presume backward genericity of arbitrary physical-basin points.

## 5. Localization and the global positive-stress argument

The essential basins cover O modulo a null set. Hence grad H0=0 everywhere on O by continuity. Let Z={Omega=0}. At every boundary point of O, the Lamb identity and continuity imply U=0.

On D=int(Z), extend U by zero outside D. The extension is locally Lipschitz: near a boundary point, use U=0 there and the local bound on DU to estimate by distance to the boundary. Its weak derivative equals 1_D DU almost everywhere; on its zero set the weak derivative vanishes almost everywhere. Therefore its distributional divergence and curl both vanish. It is entire harmonic and vanishes on the nonempty open set O, so it vanishes everywhere by unique continuation. If O was empty, the original U was already entire harmonic and decaying, and hence zero. Thus U=0 on D and on all remaining points of Z as well.

The Lamb identity now gives grad H0=0 on Z, so H0 is globally constant. Its normalized quadratic mean tends to zero by beta<1, forcing that constant to be zero. Dotting the Lamb identity with B gives U.B=0. Since H0=P0-|U|^2/2+U.B, it follows that P0=q=|U|^2/2.

The pressure equation is therefore

    partial_i partial_j(U_i U_j)+Delta q=0.

Test it against chi(y/R) sqrt(1+|y|^2), where chi is a nonnegative smooth cutoff equal to one on the unit ball. All terms differentiating chi are bounded in absolute value by C R^(-1) integral_(|y|<2R)|U|^2<=C R^(beta-1), which tends to zero. The remaining integrand is

    chi(y/R)[U^T D2 sqrt(1+|y|^2) U
                       +q Delta sqrt(1+|y|^2)].

It is nonnegative and strictly positive wherever U!=0. On each fixed ball its integral is bounded by the vanishing cutoff error for sufficiently large R. Thus U=0 everywhere.

## 6. Contrapositive and scope

If a nonzero profile existed, some essential basin would violate the one-sign condition. Since h is a continuous real function, that means it takes both signs there. Its strict-sign sets are nonempty and open, hence have positive volume; removing the null nongeneric set leaves positive-volume sets of physical-basin points of both signs.

No claim is made that every essential basin must have both signs. No statement about the sign or values of h on the entire singular support is inferred from its Lebesgue basin. The theorem remains limited to smooth profiles because the new measure construction uses C-infinity regularity. The analytic mean-decay and given-measure parts only need C2, but their regularity does not by itself extend the coverage theorem.

## Dependencies and verification

A308 supplies smooth coverage; A207 and A223 supply positive local densities and essential basin domains; A048-A049 and A283 supply complete recurrent vortex flow and sign rigidity; A277-A278 supply the fixed-pressure mean estimate and basin-to-global conclusion. The relevant proofs were reread in full, including the pressure normalization and boundary localization formulas. The focused coordinator review independently identified this corollary conditional on coverage; that premise is now provided by A308. Its received text and model configuration are retained as evidence. No computation, finite truncation or formal asymptotic assertion enters the proof.
