# Exact angular null directions in the serialized value fits

Date: 2026-10-20. Verdict: CONFIRMED by the independent proof below.

## Statement and hypotheses

Let phi_j=pi(j+1/2)/N, j=0,...,N-1. Represent a divided field by

    H(r,phi)=E(r) sum_(k=0)^(K-1) a_k(r) rho(r)^(k mod 2) cos(k phi),

where E(r)>0 and rho(r)>0 for r>0. Each a_k is expanded in a common radial B-spline basis B_l(t(r)), with coefficients constrained to vanish only when l<floor(k/2). The sampling operator evaluates H at all pairs of any chosen positive radial nodes and the N angular nodes. Multiplication by any nonzero scalar sample weights does not change its nullspace.

For N=12 and K=16, each of the following is in that nullspace:

1. A single radial coefficient in mode12, with index l>=6.
2. Equal radial coefficients in modes13 and11, with l>=6.
3. Equal radial coefficients in modes14 and10, with l>=7.
4. Equal radial coefficients in modes15 and9, with l>=7.

If the radial basis has Nb members, these give 4 Nb-26 linearly independent null vectors when Nb>=8. They are independent because their angular supports are disjoint. They remain null for every radius, not just for the chosen radial nodes. This is a lower bound on nullity, without an assertion that all other radial directions are determined.

These functions need not vanish between the angular nodes, and their angular derivatives need not vanish at the nodes. With radial coefficients supported in a compact annulus, the perturbations preserve every center jet, all far-field coefficients, and the center strain of a vorticity Omega=xH. They also preserve the x-reflection parity required in B2. The statement applies separately to the temperature divided field F and the vorticity divided field G.

## Proof

At every node, 12 phi_j=(j+1/2)pi, so cos(12 phi_j)=0. Also 24 phi_j=(2j+1)pi, so

    cos((24-k)phi_j)=-cos(k phi_j).

The paired indices have the same parity, hence the same radial prefactor. Equal radial coefficient functions at k and24-k therefore cancel at every node and every radius. The required lower radial index is the larger of floor(k/2) and floor((24-k)/2), giving the indices in the statement. The mode12 contribution has Nb-6 free directions, the13/11 pair Nb-6, and the14/10 and15/9 pairs Nb-7 each. Their sum is4Nb-26.

None of these trigonometric polynomials is identically zero. For example the derivative of cos12phi at a sampling node is -12 sin12phi_j, with magnitude12. Thus a zero sampled value does not imply a zero derivative there. At a nearby angle phi=pi/12, cos12phi=-1, so that mode also has a nonzero unsampled value.

Choose a radial basis function whose support is a compact subinterval of0<t<1, and which is allowed by the masks. It then vanishes in neighborhoods of the center and infinity. In Cartesian coordinates the corresponding functions are smooth wherever the radial basis is smooth, and vanish near0; a smooth compact radial coefficient instead gives C-infinity perturbations with the same angular conclusion. Because cos(k phi)=T_k(-y/r) and all other radial factors depend only on r, F and G are even in x. Theta=x^2 F is even and Omega=xG is odd. The center strain is

    c=(1/pi) integral xy r^-4 Omega dxdy.

In the phi convention x=r sinphi, y=-r cosphi, its angular functional on G is proportional to the difference of coefficients of cosphi and cos3phi, by sin^2phi cosphi=(cosphi-cos3phi)/4. All four null directions involve only modes9 or higher, so their center strain is exactly zero. The fields vanish near the center and infinity, so all jets and tails there are preserved. This completes the proof.

## Scope and application

The archived driver log for a0c1hr states Nphi_res=12, while its representation has K=16 and Nphi=32. The fitting source forms separate weighted value matrices for F and G on the Nphi_res nodes and takes their pseudoinverses. The larger representation Nphi does not repair these separate value-fit nullspaces.

This theorem does not claim a nullspace of the complete nonlinear characteristic map. Changes in G can change the full-plane velocity and characteristic curves, and a fitted temperature gradient is used as a source along those curves. A pseudoinverse also selects a particular coefficient representative. The exact conclusion is that these nodal value fits alone do not determine the represented functions or control their derivatives away from the nodes. The observed worsening of true PDE residuals under this refinement remains independently established; the proportion attributable to angular aliasing is not quantified by this theorem.

When N>=K, the cosine columns0,...,K-1 are orthogonal on these nodes by the finite cosine sum identity, so this particular angular nullspace disappears. This says nothing by itself about radial conditioning, characteristic integration accuracy, center projection, or differential PDE convergence.

## Dependencies and evidence

Only elementary trigonometric identities and the stated basis are needed. The canonical center moment is independently proved in packet63. The separate implementation and read-only source provenance are in verification/angular_sampling_20261020T2044. No numerics-lane code is imported or executed, and no floating-point check is used as proof of the exact identities.
