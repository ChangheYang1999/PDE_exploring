# Derivative restrictions for the frozen vorticity field

## Statement

Let c>0, omega be finite, and let U,P be C^2 exact rotating Euler profiles with div U=0 and uniform U=o(|y|). Set B=(cI-omega J)y+U, Omega=curl U, and b=1+c.

1. At every zero p of Omega, the matrix A=DOmega(p) is nilpotent: A^3=0.
2. If K is any compact invariant set of the full frozen Omega-flow psi_t, then for every epsilon>0 there is a finite C_epsilon such that

\[
 \sup_{x\in K}\|D\psi_t(x)\|\le C_\epsilon e^{\epsilon |t|}
                  \quad(t\in\mathbb R).
\]

These are independently checked versions of approach3 item 35(b,c). They concern the frozen vorticity field. They do not assert subexponential growth of the B-flow. Hypothesis tags: H0, H1-prime.

## 1. Transport and the derivative at a zero

The B-flow Phi_s is complete and maps any fixed compact set into one common ball for all negative s. Its Cauchy relation is

\[
 D\Phi_s(x)\Omega(x)=e^{bs}\Omega(\Phi_s x).        \tag{1}
\]

Thus the zero set of Omega is B-invariant. Differentiate (1) at a zero p. The term containing the spatial derivative of DPhi_s is multiplied by Omega(p)=0, so

\[
 D\Omega(\Phi_s p)=e^{-bs}D\Phi_s(p)
                  D\Omega(p)D\Phi_s(p)^{-1}.             \tag{2}
\]

All derivatives exist under the stated C^2 hypotheses. For s=-nL with L>0, the matrices on the left stay bounded because Phi_{-nL}(p) stays in one compact ball and DOmega is continuous. The eigenvalues on the right are e^{bnL} times the eigenvalues of DOmega(p), by similarity. As b>0, boundedness forces each eigenvalue of DOmega(p) to be zero. Cayley-Hamilton in dimension three then gives DOmega(p)^3=0. In particular det DOmega(p)=0 and trace(DOmega(p)^2)=0.

This is a degeneracy condition, not a proof that zeros are absent or nonisolated. Degenerate isolated zeros remain possible.

## 2. Uniform subexponential derivative growth on an invariant set

The local Omega-flow obeys

\[
 \Phi_s\psi_t=\psi_{e^{bs}t}\Phi_s.                 \tag{3}
\]

On a compact invariant set it is complete. Fix L>0 and put K_n=Phi_{-nL}(K), eta_n=e^{-bnL}. All K_n are compact Omega-invariant sets in one fixed ball D. Let M=sup_D||DOmega||. The variational equation along trajectories in K_n yields ||Dpsi_t(q)||<=e^{M|t|} for q in K_n, for positive and negative t.

Differentiating (3) and rearranging gives, with q=Phi_{-nL}(x),

\[
 D\psi_t(x)=D\Phi_{nL}(\psi_{\eta_n t}q)
                 D\psi_{\eta_n t}(q)D\Phi_{-nL}(x).
\]

The two outer factors are uniformly bounded for x in K and all t: their arguments belong to the compact sets K_n and K. Denote their product bound by C_n, which need not be uniform in n. Then

\[
 \sup_{x\in K}\|D\psi_t(x)\|\le C_n e^{M\eta_n|t|}.
\]

For any epsilon>0, choose n with M eta_n<=epsilon and put C_epsilon=C_n. This proves the assertion. No exchange of the large-time and large-n limits is used; n is fixed after epsilon is chosen.

## Dependencies and scope

The proof uses only complete B-flow, its backward compactness, the Cauchy formula, matrix similarity, the elementary variational bound, and Cayley-Hamilton. It does not require completeness of the Omega-flow away from the compact invariant sets. The result supplements the zero-entropy statement in the team records.
