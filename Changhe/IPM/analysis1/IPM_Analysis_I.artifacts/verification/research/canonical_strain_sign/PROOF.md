# Canonical stream-function sign correction to topics 77 and 78

## Exact statement

PROMPT.md fixes -Delta psi[h]=partial_x h, U[h]=(-partial_y psi[h],partial_x psi[h]), sigma[h]=partial_xy psi[h](0), and c[h]=sigma[h]/3. Topics 77 and 78 instead identified the stream function solving Delta psi_minus=partial_x h with this same raw strain. This identification is REFUTED. They are related by psi_minus=-psi, sigma_minus=-sigma. Reversing the velocity convention at the same time preserves U, but does not preserve the strain functional. The normalized linearization in the prompt uses +ell sigma, ell=X dot grad rho/3.

Let G=(2pi)^(-1)log|X|, so Delta G=delta_0. For a smooth compactly supported h,

 psi=-partial_x G*h,
 U=(partial_xy G*h,-partial_xx G*h),
 sigma[h]=-partial_xxy G*h(0).

With circular principal values, put

 K=(y^2-x^2)/(2pi r^4),
 K_s=y(3x^2-y^2)/(pi r^6).

Then

 partial_xx G=delta_0/2+PV K,
 partial_xxy G=partial_y delta_0/4+PV K_s,
 sigma[h]=-h_y(0)/4-PV(K_s*h)(0).                    (1)

For h(0)=grad h(0)=0 the last convolution is absolutely convergent and sigma[h]=-integral K_s(-Y)h(Y)dY. This correction changes a sign, not the factor 1/4. The velocity symbols and kernels in topics 77 and 78 remain exactly those of the prompt.

## Proof of the local distribution identity

Differentiate G away from 0 to obtain K and K_s. The usual circular integration by parts gives partial_xx G=delta_0/2+PV K: the boundary coefficient is (2pi)^(-1)integral cos^2 theta dtheta=1/2. To differentiate PV K in y, integrate by parts on the complement of a disk. The additional boundary pairing is integral K phi omega_y dS. Its constant and x-linear terms have zero angular integrals. Its y-linear term is phi_y(0)/(2pi) times integral (sin^2 theta-cos^2 theta)sin^2 theta dtheta=phi_y(0)/4. As a distribution this is -partial_y delta_0/4. Hence

 partial_y PV K=PV K_s-partial_y delta_0/4,
 partial_xxy G=partial_y delta_0/2+partial_y PV K
              =partial_y delta_0/4+PV K_s.

Multiplication by the canonical minus sign proves (1). The angular moments of K_s against constants and linear functions vanish, making the circular PV meaningful. When h has zero value and gradient, its Taylor remainder is O(r^2), and r^-3*r^2 times the area measure is integrable at zero. Compact support ensures convergence at infinity. The convolution uses K_s(-Y), not K_s(Y).

Fourier transformation gives psi_hat=i xi h_hat/(xi^2+eta^2), hence U_hat=(xi eta,-xi^2)h_hat/(xi^2+eta^2) and sigma's evaluation multiplier is -i xi^2 eta/(xi^2+eta^2). The opposite stream convention has the negative strain multiplier and the same velocity only after reversing the rotation.

## Consequences for the verified local estimates

Topic 77's Aop, frozen Fourier energy, commutators, remote velocity bounds, E, R, kappa, and K1 do not contain sigma. All other displayed K_i use sigma only through absolute estimates |sigma h|, absolute cutoff norms involving ell, or an exact localization identity valid for either chosen scalar functional. Since |sigma|=|sigma_minus|, each proof step and each numeric bound transfers verbatim to the prompt's linearization L=V dot grad-1+a dot U+ell sigma. In particular its local estimate with K1-K4 remains valid after sigma is corrected to the canonical definition (1). This is a sign-invariance deduction from the completed proof; it is not a new actual coefficient certificate.

Topic 78's maximal transport domain, generator, auxiliary inverse Aop^-1, semigroup estimate, and norm bound likewise contain no strain and are unchanged. The strain bound |sigma h|<=beta_s ||h||Hs remains valid. The bounded rank-one statement is algebraic for any functional: for the canonical operator Aop+ell_delta sigma it reads

 Delta_can=1+sigma[Aop^-1 ell_delta],
 (Aop+ell_delta sigma)^-1 f
   =Aop^-1 f-Aop^-1 ell_delta sigma[Aop^-1 f]/Delta_can,

provided Delta_can!=0. In terms of the wrongly named old functional sigma_minus, the physical denominator is

 Delta_can=1-sigma_minus[Aop^-1 ell_delta].             (2)

It is not 1+sigma_minus[Aop^-1 ell_delta]. If Delta_can=0, v=Aop^-1 ell_delta has sigma[v]=-1 and is a nonzero null vector; conversely the formula gives both inverse identities when the denominator is nonzero. The norm estimate is unchanged after using |Delta_can|. No actual denominator had been numerically enclosed, so no claimed numerical nonvanishing is being retained or reversed.

## Scope and evidentiary record

The original finalized files for topics 77 and 78 are preserved without alteration. This correction supersedes their identification of the alternative strain with PROMPT.md, the sign of their canonical distribution formula, and use of an old-convention plus denominator for the physical operator. It preserves the sign-independent estimates by the proof above. The first N7 proof repeated the mistake; its rejected version and Opus5.5 review are preserved in research/n7_center/evidence/rejected_proof_v1.md and notes/reviews/n7_center_proof_*; its current proof uses the prompt convention.

Both the verifier's direct prompt check and actual Opus5.5 found the N7 velocity inconsistency. This topic's proof and explicit sign algebra are subject to a separate review. No decisive endpoint follows.
