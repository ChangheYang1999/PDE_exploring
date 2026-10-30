# Independent complete-plane Hessian check

## Statement, hypotheses and scope

Fix one of the immutable S1 references007,016,017 listed in data/manifest.json. Let c>1 be its exact parameter, delta=1-1/c, and let rho=-partial_y Delta chi for its finite raw potential. The accepted structural checks give smoothness at the origin and D^k rho=O(r^(1/c-k)) at infinity for k<=2. This check computes the three exact full-plane energies E_xx, E_xy, E_yy and encloses them using rational algebra and outward Arb arithmetic. Set X^2=E_xx+E_xy, Y^2=E_xy+E_yy and H^2=E_xx+2E_xy+E_yy.

Under the already audited gradient-commutator theorem, with Fourier multiplier R_j=i xi_j/|xi|, the operator K=1/2[R1,[R1,rho_y]]-1/2[R1,[R2,rho_x]] has squared Hilbert-Schmidt norm

    kappa^2=((log2-1/2)X^2+(3log2-2)Y^2)/(16pi).

Consequently ||K||<=kappa. This is no lower bound for ||K|| and supplies neither a global bound for theta=sup(|grad rho|-rho_y)/2 nor a high-space inverse or existence proof.

## Polar differentiation

Write t=r^2/(1+r^2), v=1-t. The independently reconstructed density has the exact finite representation

    rho=r sum_(j,n) v^a_j A_(j,n)(t) sin(n theta), a_j=(j+1)delta/2.

Every A is rational with positive denominators (1+624v)^p(1+2499v)^q. For any component r^d v^a A(t) trig(n theta), put B=(d-2at)A+2tv A'. Radial differentiation gives r^(d-1)v^a B. Cartesian differentiation and elementary sine/cosine product identities give the following coefficients, with the common factor r^(d-1)v^a:

- partial_x has (B-nA)/2 at n+1 and (B+nA)/2 at n-1, with the same trigonometric kind.
- partial_y of a cosine has (B-nA)/2 at sine(n+1) and -(B+nA)/2 at sine(n-1).
- partial_y of a sine has (nA-B)/2 at cosine(n+1) and (B+nA)/2 at cosine(n-1).

Negative sine indices change sign, negative cosine indices do not, and sine0 vanishes. Apply this identity twice, first d=1 and then d=0, retaining the zero cosine when it arises. Compare the two constructions of partial_xy rho exactly. In each resulting grouped second derivative the rational numerator is divisible by t. Since r^-1 t = r v, division by t gives

    rho_ab=r sum_(j,n) v^(1+a_j) B_ab,(j,n)(t) trig(n theta).

The division is checked exactly, so no artificial polar singularity remains. The xx,yy fields are odd sine series and xy is an odd cosine series. Compare nine physical values per candidate with the separate Cartesian fifth-order Taylor-jet results. These point comparisons are regression checks, not an integration proof.

## Whole-plane energies

Orthogonality on the circle gives integral pi for the square of each positive sine or cosine, and zero across frequencies. For a pair of branches j,j' at the same frequency, put ell=j+j'+2. Accumulate every product, doubling off-diagonal pairs, into W_ell. Since r dr=-dv/(2v^2) and r^2=(1-v)/v, each energy is

    E_ab=(pi/2) sum_ell integral_0^1 v^(ell delta/2-1)(1-v) W_ell(1-v) dv.

Here ell>=2 and ell delta/2-1>-1, so every separate integral converges. No cancellation is needed for convergence. The denominators remain positive. The finite sum equals the spatial energy by the exact change of variables.

Use the independent rational-field and CRT moment backend previously checked on020. Decompose the numerator (1-v)W_ell(1-v) by exact polynomial division and Chinese remainders; replay the decomposition exactly. For each pole, evaluate integral_0^1 v^b/(1+av)^k dv = 2F1(k,b+1;b+2;-a)/(b+1), b>-1, a>0. Its Euler integral establishes the identity. Direct outward Arb evaluation differs from the peer recurrence evaluation. All groups must have at least150 bits of accuracy at2048-bit working precision. Compare every grouped moment and the resulting energies, not only rounded norms.

Calibrate007 against its previously accepted exact rational energy sums pi*S/2. A saved directed upper endpoint is not a containing ball for the exact norm; compare the exact S or the saved containing norm ball. Record the two tests separately if needed. No tolerance change is involved.

## Dependencies and evidence

The accepted gradient-commutator theorem is in ../gradient_commutator_audit/PROOF.md; the polar construction and exact rational moments are in ../candidate020_weak and ../weak_probe_audit. Frozen raw files, peer records and code hashes are registered in data/manifest.json. All executed code is local. No formal build is attempted. This proof was written and checked before the new checker was executed. The result is numerical certificate reproduction and uses only the stated, already audited analytic identities.
