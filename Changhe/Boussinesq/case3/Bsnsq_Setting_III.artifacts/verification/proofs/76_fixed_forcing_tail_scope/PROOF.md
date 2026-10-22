# A fixed forcing tail and a changing exponent basis

Date:2026-10-20. Status: proved elementary approximation and residual identities. No profile result.

## Statement and hypotheses

Let f_S be a fixed continuous full-plane scalar source with uniform angular asymptotic

    f_S(r,theta)=r^(-nu_S)[a_S(theta)+o(1)],

where nu_S>0 and a_S is continuous and not identically zero. Let f_N be any finite representation with f_N=O(r^-nu) uniformly in angle for some nu>nu_S. Then

    r^(nu_S)(f_N-f_S) -> -a_S uniformly,
    sup_(r>=1,theta) r^nu |f_N-f_S| = infinity.

In particular, convergence of finite-grid weighted errors or convergence on all compact subsets does not supply convergence in this global weighted norm. This does not prevent local or unweighted convergence, and does not rule out a separately verified zero-forcing endpoint.

For r2 splines, every fixed finite coefficient vector with basis exponent b has nu=1/b. Thus retie from a seed beta_S to beta<beta_S has this obstruction whenever the original fixed source has a nonzero leading r^(-1/beta_S) coefficient. The nonzero coefficient must be checked on the actual source; it is not assumed merely because both terms defining it separately have that envelope.

## Proof of the tail statement

The uniform size bound gives r^(nu_S) f_N=O(r^(-(nu-nu_S))) ->0. Subtract the assumed expansion of f_S. Choose an angle theta0 with |a_S(theta0)|>0. For all sufficiently large r, |f_N-f_S|(r,theta0)>=(|a_S(theta0)|/2)r^(-nu_S), whose product with r^nu diverges. This proves both assertions.

No finite collection of nodes constrains this limiting value. Even a sequence converging on every compact set can have this obstruction at every finite index: take smooth radial cutoffs chi(r/N) equal to1 for r<=N and0 for r>=2N, and f_N=chi(r/N)f_S. Each compactly supported f_N has any prescribed decay bound, but the stated weighted error remains infinite. This example concerns function approximation, not a specific spline solver.

In the r2 basis, the bounded endpoint spline and bounded odd-mode factor multiply G by (1-t)^(b+1), with1-t~(L/r)^(1/b); Omega=xG is O(r^-1/b). This verifies the claimed exponent for every finite coefficient vector. Endpoint cancellation can only make it decay faster, so it cannot defeat the obstruction when nu>nu_S.

## Conditional exact seed and the stored residual

Let B be the linear centered full-plane inverse. For fields Omega,Theta and exponent beta define

    Rv(W)=W.gradOmega+Omega-Theta_x,
    Rt(W)=W.gradTheta-(beta-2)Theta.

Suppose a seed Omega_S,Theta_S uses W_S=beta_S X+B[E]. Define f_S=E-Omega_S and the additive path W_lambda=beta X+B[Omega+lambda f_S]. At the same seed and lambda1, beta=beta_S, linearity gives W_lambda=W_S exactly. Therefore both residuals are exactly the original seed residuals. They vanish if and only if those seed residuals vanish. A stored approximate seed does not become an exact root merely by this algebra.

If the code instead uses an approximation f_tilde, then at a fixed state the exact residual changes are

    delta Rv=lambda B[f_tilde-f_S].gradOmega,
    delta Rt=lambda B[f_tilde-f_S].gradTheta.

Likewise the center-strain change is lambda c[f_tilde-f_S]. A small weighted nodal value error alone is not a bound on any of these full-plane inverse quantities. At lambda0 the forcing drops out, so none of this obstructs verifying a zero-forcing candidate by its own PDE residuals.

## Scope and evidence

The source asymptotic and inverse convergence must be established for each actual representation. The result does not say that no approximate fixed-source path can work: retaining the original basis for the fixed source, or explicitly evaluating that source independently of the unknown-field basis, avoids this particular exponent mismatch. It supplies no beta or profile exclusion.

The actual seed is the immutable lambda_seed_snapshot.npz in verification/additive_driver_20261020T2128, SHA256483d3af008fa13ece17ad735c59e7c2d9de75e03f7dc615b91eb99aa06ff04c0. It has beta_S=3,L=1.5. On the positive x ray (phi=pi/2), all odd cosine modes vanish and each even mode is exactly(-1)^(k/2). The endpoint source coefficient divided by L^(4/3) is the rational number

    -350452483136245083625327 / 75557863725914323419136

when the stored binary64 E and Omega_S coefficients are interpreted as exact dyadic rationals and subtracted exactly. If subtraction is instead rounded mode by mode first, the coefficient is

    -668435064575662787 / 144115188075855872.

Both are strictly negative. Thus a_S is not identically zero for either represented source interpretation. This is exact finite rational arithmetic on the archived binary input, not a certificate about an unknown continuum seed. The uniform angular expansion follows from the finite r2 representation. Packet76 therefore applies to that actual fixed source for every beta<3.

Reproduction: code_independent/check_forcing_schema.py and verification/forcing_schema_20261020T2142/exact_source_coefficient.json. The new archive schema distinguishes original seed-basis cG_f,beta_seed from lambda-scaled stage-basis cG_f_effective. The independent reader uses the latter for the actual stage velocity, refuses nonzero-lambda seed-only archives unless explicitly reconstructed, and ignores forcing at lambda0. Four regression cases passed at at most1.12e-16 error.

Actual claude-opus-5-5 request77b returned a written review confirming the fixed-source obstruction and conditional seed algebra; its qualifications about consistent projection/rounding are included above. Request77 had supplied no written audit. The same review's unrelated unmasked-origin objection to packet75 was refuted against the actual index mask, and the attempted followup78 returned no text. No endpoint.
