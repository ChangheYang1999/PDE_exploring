# Clarifications after the independent audit

Date: 2026-10-28T14:31:36.699585+00:00. The bound PROOF.md SHA256 is unchanged.

Choose the source extension cutoff chi radial, as already used in the proof's parity paragraph. This is needed for the odd-y restriction. The whole-space inverse without a parity restriction does not require this extra symmetry.

The radius1/1000 check certifies containment in a single original knot annulus. Analyticity on that annulus follows from the finite angular log-polynomial density formula and the modal Green constant-coefficient ODEs in proof 15, not from numerical testing of derivatives. The backward-flow proof itself needs smoothness, and retains the vanishing powers of the order12 remainder when differentiating to every order.

The Riesz conjugation proof uses an exact weak projection identity and an a priori membership estimate. A Neumann series for the elliptic metric perturbation is possible but is not needed for that step. The final coupled inverse does use a Neumann series on the exact maximal domain.

The auxiliary velocity is the whole-plane L2 Fourier multiplier velocity. Equality with the canonical physical-origin far-subtracted velocity holds on globally even-x, odd-y inputs. On an odd-y source input without global evenness, the possible horizontal constant is bounded by C||h||2; its product with the localized rho_x coefficient is an additional rank-one term of size O(delta^(1-alpha)). This observation does not itself patch the source inverse into the global problem.

Every uniformity in delta is for a fixed alpha<1. No uniform estimate as alpha tends to1 is claimed.
