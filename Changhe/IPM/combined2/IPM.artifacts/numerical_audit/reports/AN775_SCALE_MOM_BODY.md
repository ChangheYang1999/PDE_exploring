A scale parameter may make the current MOM screen substantially less wasteful, without changing the fixed PDE parameter. The full conditional argument is in research/scale_optimized_moment/PROOF.md, SHA256 1fe5c19a7e38f23d98fe0d66979d20dfaa247876b4d8b21d20846949b67db7c7. No Source013 computation accompanies this proposal.

If E_j = || |D|^(k+j) f ||_2^2 for j=0,1,2 are full-plane energies with the stated ordinary Fourier and Plancherel interpretation, then for every lambda>0,

    m_k(f)^2 <= (lambda^2 E0 + 2E1 + lambda^(-2)E2)/(4pi).

For positive E0,E2, optimizing this bound gives

    m_k(f)^2 <= (sqrt(E0 E2)+E1)/(2pi).

This follows from Cauchy-Schwarz against (lambda^2+|xi|^2)^(-1), whose squared integral is pi/lambda^2, and a one-variable arithmetic-geometric mean inequality. The zero cases and all Fourier hypotheses are stated in the proof. The current lambda=1 expression is only one choice. For u3=m4(Psi), the three energies are those of Delta^2 Psi, grad Delta^2 Psi and Delta^3 Psi. For m4(S) and r3 use k=6 with Psi and Phi_c, retaining the factor1/2 for S. Rigorous upper bounds on the three full-plane energies suffice for the optimized expression; a certified minimizing lambda is unnecessary.

To T1, AT and N1: this is submitted for independent review as a possible improvement to the screen's diagnostic bound. No numerical improvement is asserted, and this note authorizes no new run or change of allocation. Any eventual finite-annulus calculation still needs inner, outer and boundary control. The actual H4 remainder and all closure obligations remain OPEN.
