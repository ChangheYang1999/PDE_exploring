# Audit of local velocity regularity and propagation to the open axis

Date: 2026-10-20. Verdict: CONFIRMED, for the exact hypotheses stated in the source. This is an independent mathematical audit of the lead's proof, not a formal or numerical certification.

Source: lead-run-records/verifier/fred27/answer.md, parts (2), (1), especially the one-derivative lemma and its iteration. The report's C1 conclusion is smoothness near each point of the open axis segment (0,x*), not a uniform derivative bound at P.

## Canonical inverse localization

For a compact cutoff eta equal to one on a neighborhood of a compact set K, U[rho]=U[eta rho]+H there, with H smooth. One must define the far part by subtracting the compactly supported canonical velocity from the already normalized full-plane velocity; eta need not preserve parity. For k>=1, far derivatives of the kernel have magnitude O(|z|^{-2-k}), so the far density growth O(|z|^gamma), gamma<1, gives radial integrability at infinity. Local separation from K removes the kernel singularity. The value of the far constant is fixed by the original normalization. Thus differentiating a non-absolutely convergent zeroth-order integral has not been assumed.

The compact inverse is a bounded order-zero multiplier. Its bounded symbol gives the local H^k assertion by Plancherel after this decomposition. Its annular zero-mean kernels give C^alpha bounds: for a dyadic annulus of radius 2^{-j}, subtract rho(X) and use the alpha-Hoelder increment; the contribution is O(2^{-j alpha}), and its first derivative is O(2^{j(1-alpha)}). Splitting at 2^{-j} comparable to |X-X'| proves the C^alpha increment estimate. Apply the same argument to derivatives of a compactly supported C^{k,alpha} density, commuting constant multipliers with derivatives. This supplies the needed C^{2,alpha} velocity and smoothness where the density is smooth.

## One-derivative propagation lemma

The source proves the following finite-system assertion. For

    P u = W.grad u + sum B_nu R_nu u + C u,

assume W is real C_b^{2,alpha}, B_nu,C are C_b^{1,alpha}, the R_nu are constant order-zero multipliers with bounded symbols and |grad m|<=C/|xi|, u in L^2, and Pu in H^{-1} globally. If Pu is H^1 near a compact nonstationary trajectory tube and u is H^1 near its forward end, then u is H^1 at the earlier end. Coefficients may be extended from a larger compact neighborhood. No positivity of the B_nu terms is needed.

I checked the following steps directly.

1. The inequality |eta||m(eta)-m(xi)|<=C|xi-eta| follows by splitting |eta|<=2|xi-eta| and its complement. Fourier convolution then gives ||[chi,R] partial_j v||_2<=C_chi||v||_2. The required first Fourier moment of chi is finite for chi in C_c^{2,alpha}: choose 0<eta<alpha, use chi in H^{2+eta}, and Cauchy-Schwarz. The radial exponent at infinity is -1-2eta. There is no endpoint alpha=0 assertion.
2. A flow cutoff chi=eta_transverse exp(lambda t/2)theta(t) has D(chi^2)>=lambda chi^2-K_e e^2. The negative derivative of theta is supported in the known regular region. The flow is C^{2,alpha}, sufficient for step 1. Choose lambda only after fixing the coefficient-bound constant in the energy estimate, and before choosing chi.
3. For J_epsilon=(1-epsilon^2 Delta)^{-1}, the exact identity is P J_epsilon u=J_epsilon Pu-epsilon^2 J_epsilon[Delta,P]J_epsilon u. The sign is correct. The formulas [Delta,W.grad]z=2 partial_i((partial_i W_j)partial_j z)-(Delta W_j)partial_j z and [Delta,B]z=partial_i((partial_iB)z)+(partial_iB)partial_i z avoid differentiating the rough coefficients beyond the stated orders.
4. L=epsilon^2 partial J_epsilon partial has norm <=1, and M=epsilon^2 partial J_epsilon has norm O(epsilon). Their cutoff commutators have norms O(epsilon)||grad chi||_infty and O(epsilon^2)||grad chi||_infty. The heat-kernel representation of J_epsilon proves these from the first absolute moments of the differentiated Gaussian. The possible delta term commutes with chi. Since ||grad J_epsilon u||_2<=C epsilon^{-1}||u||_2, all cutoff errors are uniform.
5. Moving chi through L,M and then through R gives ||chi grad E_epsilon u_epsilon||_2<=K_0||chi grad u_epsilon||_2+C_chi||u||_2, with K_0 independent of chi and lambda. Terms containing Delta W use M and require only a bounded Delta W. Terms containing partial B use L on R u_epsilon or M on R grad u_epsilon; no second derivative of B is needed.
6. Separated resolvent kernels have uniform derivatives for epsilon<=1. Inserting cutoffs proves the local bounds on chi grad J_epsilon Pu and e grad J_epsilon u from the stated local H^1 assumptions and global H^{-1}/L^2 bounds. The separated kernel and one derivative in its input variable have uniformly bounded L^2 norms on compact output sets. This is the needed H^{-1} to L^2 estimate.
7. Pair the differentiated regularized equation with chi^2 grad u_epsilon, take its real part, and integrate transport by parts. The result is lambda/2 ||chi grad u_epsilon||_2^2 <= K_1||chi grad u_epsilon||_2^2+C_chi||chi grad u_epsilon||_2+C_chi. The order-zero terms need only boundedness plus the commutator from step 1. Choose lambda>2K_1+2. Weak compactness proves the desired H^1 regularity.

These seven steps prove the lemma from the stated hypotheses. In particular the proof does not silently replace the order-zero nonlocal term by a local multiplier or assume it is self-adjoint.

## Iteration and the source limitation

Let O be the open set of points whose forward nonstationary trajectories enter the smooth center neighborhood in finite time. Assuming rho in H^k_loc(O), k>=2, local inverse regularity gives U in H^k_loc(O). Differentiate the transport equation k times on a compact tube in O, using u_I=partial^I(eta rho), |I|=k. The single derivative on W contributes a matrix with C^{1,alpha} entries. All k derivatives on U give grad rho . R u_I plus a smooth separated-tail term times grad rho. The remaining products have derivative orders between 2 and k after one extra derivative, and total order k+2.

They belong to H^1 by the product estimate for bounded H^{k-2} functions, applied to D^2U and D^2rho. The estimate follows from ||D^a v||_{2m/a}<=C||v||_infty^{1-a/m}||D^m v||_2^{a/m}, Holder, and weighted arithmetic-geometric mean, with m=k-2; k=2 has no middle products. The source provides a valid dyadic-kernel proof of this interpolation inequality and the needed maximal-function L^2 bound. Local cutoffs supply bounded supports. Therefore the differentiated system has an H^1 right side and precisely the coefficient regularity of the lemma.

The differentiations can be justified by local mollification in H^k and C^2, with the highest transport derivative interpreted in H^{-1}. They do not presuppose H^{k+1}. Terminal smoothness supplies u_I in H^1 there. Applying the lemma gives H^{k+1} near each earlier point. The same open set O works for every k; tubes and finite constants may depend on k and the point. Sobolev embedding yields smoothness.

Every point of (0,x*) reaches a smaller positive-axis point inside the smooth center neighborhood in finite forward time, because w<0 is bounded away from zero on the intervening compact segment. This proves the C1 assertion used by the higher trace proof. It gives no uniform bound as x approaches x*, and cannot supply missing C^{4,alpha} regularity at P. That distinction is maintained in the report and in ../PROOF.md.
