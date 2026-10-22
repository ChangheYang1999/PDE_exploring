# A compact stream with a positive core must change vorticity sign

Written UTC 2026-10-21T08:28:40.944788+00:00 before computation. This result audits the scope of the lead's impulse434 construction. It does not exclude the broad B2 class, which permits sign-changing vorticity.

## Statement, conventions and dependencies

Let Psi be a real C2 function of compact support on R2, odd in x, and let Omega=-Delta Psi. Assume that Omega is strictly positive on some nonempty open subset of {x>0}. Then Omega is strictly negative at some point of {x>0}. The same conclusion holds for any new stream that equals Psi on a disk containing its support. The only dependencies are integration by parts against the harmonic function x, reflection symmetry, continuity and compact support.

## Complete proof

Choose a disk D containing the support of Psi in its interior. Since Psi and its first derivatives vanish near its boundary, Green's identity gives

    integral_R2 x Omega = -integral_D x Delta Psi
                        = -integral_D Psi Delta x = 0.

The oddness of Psi implies that Omega is odd in x. Therefore x Omega is even in x, and

    0=integral_R2 x Omega=2 integral_{x>0} x Omega.

All integrals are absolutely finite because Omega is continuous and compactly supported. If Omega were nonnegative throughout {x>0}, the nonempty positive open subset would make the rightmost integral strictly positive: shrink that subset to a closed ball staying away from x=0, on which both x and Omega have positive lower bounds. This contradiction proves existence of a point with Omega<0. Continuity gives a whole negative open neighborhood. The negative point lies in the support of Omega, hence within the chosen disk containing supp Psi. If another C2 stream equals Psi throughout that disk, its Laplacian agrees at that point. Its vorticity is also negative there. This proves every assertion.

## Application to the specific reference construction

The lead's impulse434 proof, sections5.2-5.3, constructs a smooth compact odd stream Psi_f whose drift is conjugate to a globally outgoing reference and which agrees with the original stream near the center. The intended center has Omega(x,y)=q x+O(|X|^2), q=4a0/beta>0. In particular Omega(x,0)>0 for sufficiently small positive x, and continuity supplies a positive open subset. The theorem forces Omega_f<0 somewhere in the right half-plane. This conclusion is independent of which angular diffeomorphism was used; it applies even to the first radial truncation.

Section5.5 restores the prescribed tail by setting Psi_{f,N}=Psi_f+chi_N Psi_ext, with chi_N=0 on B_N and B_N containing supp Psi_f. The negative point just proved remains inside B_N and is unchanged. Thus every stream constructed in this way has some negative vorticity on the right. It also has a nonempty open annulus of zero vorticity if N is taken strictly beyond the support before restoration begins. No estimate on the remote tail can repair the retained negative point.

## Audit verdict and exact scope

CONFIRMED: the compact truncation and remote restoration construction necessarily leaves the subclass Omega>=0 on {x>0}, and therefore also leaves the strictly positive-vorticity family of126 and the positive-vorticity conclusion of135/lead4.34. Claiming that this construction preserves that sign condition would be REFUTED by the theorem above.

The actual impulse434 question and its section5.1 define a wider reference class: smooth parity, exact thermal transport, the same center, whole-plane backward basin and fixed exterior. They do not impose a vorticity sign condition. Accordingly this is a scope distinction, not a refutation of the stated realization theorem in that wider class. The broad PROMPT also allows sign changes. Preservation of smoothness, basin, tail and canonical relative inverse must be audited separately before endorsing the wider realization theorem. No arbitrary compact modification of a true full profile is asserted here; only the stated stream construction is considered.
