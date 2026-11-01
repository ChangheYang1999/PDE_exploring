# Certified longer prefixes for the other four-ninths profiles

Status: PROVED for all eight completed branches listed below. Each Candidate-shaped branch uses the separately proved all-index response certificate.

## Statement and hypotheses

Fix delta=4/9, c=9/5, and p_n=1-4n/9. A profile here is either f1=sin(theta)+b sin(3theta), with b one of the five exact algebraic roots isolated in146, or the normalized Candidate-shaped ten-mode polynomial156, with its sin(3theta) coefficient replaced by one of the seven isolated roots in156. Its even carrier bound is B=4 or B=20 respectively. A Candidate-shaped branch is admitted only after158 or163 proves a positive uniform response bound s. For the two-mode profiles the exact lower bounds in164 apply.

For any admitted branch, suppose the algorithm below succeeds through N, a positive multiple of9. Let d_j be its exact rational upper bound for j||f_j||_1, and e_a its upper bound for 9a|H_(9a)|, a<N/9. Form the explicit polynomial map of172 with these inputs, L=243/104 and

    kappa_N=B(19/9)(5/4)(N+1)/N.

If a nonnegative rational vector b0 satisfies b0>=Y0 and G(2^(-q),b0)<=b0, then the exact tuned density, stream and common potential, with every appropriately weighted spatial derivative, converge absolutely and uniformly on every closed exterior r>=R>2^(q/4). For amplitude epsilon, replace the radius by |epsilon|^(9/4)2^(q/4). This is a sufficient exterior radius, not an optimal radius or a whole-plane existence statement.

## Enclosure construction and proof

The polynomial defining b and its isolating interval are exact rational data. Sign-preserving rational bisection refines the interval; the resulting Arb interval contains the same unique algebraic root. Every initial coefficient is enclosed using this interval and the exact fixed rational coefficients. This interval is propagated through every operation; no midpoint reset is allowed.

Represent a homogeneous field using signed Cartesian Laurent coefficients. Differentiation, multiplication and addition are finite exact algebraic operations enclosed by directed ball arithmetic. The recurrence comes from the independently checked Cartesian advection g_x f_y-g_y f_x with multiplier (1-delta)/[(n-1)delta]. The S1 symmetry and carrier projections delete only coefficients known to vanish by symmetry or the previously proved carrier bounds. Every deleted interval must contain zero. The Poisson equation is checked independently by Cartesian second differentiation after inversion.

At n=9a, the obstruction in f_n vanishes: for a=1 this follows from the exact root polynomial; for a>1 it follows from tuning H_(n-9). Its interval must contain zero before projection. To tune H_n, compute two provisional continuations to n+9, with H_n=0 and H_n=1, keeping all earlier data fixed. Their obstruction values R and R1 enclose the exact values. The affine response is S=R1-R. The proof145 shows the dependence is affine, since no product contains two factors depending on H_n before n+9, and the response is nonzero. If the computed interval S excludes zero, division H_n=-R/S encloses the unique exact harmonic. Inserting that interval in the Poisson solution and continuing therefore preserves the induction. An interval containing zero causes a reported computational failure, never a division or a claim of incompatibility.

At the final order N the density obstruction is projected, but H_N need not be computed: it first affects f_(N+1). The known harmonic input in172 ends at H_(N-9). Thus all required d_j and e_a are enclosed without needing an extra final lookahead.

For each norm, the exact dyadic midpoint plus radius is evaluated rationally and rounded strictly upward to a positive rational number. Absolute values and sums are interval operations, so d_j and e_a have precisely the hypotheses required by172. The exact scalar identities and supersolution inequality are then checked with rational arithmetic. Approximate component iteration may propose a box; the complete rational inequality alone admits it. Theorem172 supplies the asserted convergence and the common-potential statement. A finite prefix alone does not prove convergence; the uniform response certificate and the infinite majorant remain indispensable.

## Evidence

Each branch records the root interval, source hashes, exact dyadic norm and harmonic enclosures, Poisson and Cartesian operation counts, complete initial rational bounds, and each exact majorant box. Optional comparisons with previously certified prefixes are consistency checks only. Large external checkpoints are not needed to define or reproduce these certificates.

## Two-mode certificates completed at 2026-10-31T13:07:44+00:00

The four prefixes through36 pass all checks, including comparison of the density norms through27 with153. Each gives14989Poisson coefficient checks and1818ordered products. All16prefix boxes pass864exact scalar coefficient identities in total. The best q values for roots1..4 are129,125,129,121. The sufficient radius is2^(q/4) for unit amplitude. The exact boxes and norm enclosures are inverification; V334 records their audit.

## Candidate-shaped certificates completed at 2026-10-31T13:10:21+00:00

All four prefixes through27 pass. Each has39550Poisson coefficient checks,981ordered products,four provisional continuations and three compatibility projections. The12prefix boxes pass648exact scalar coefficient identities. Best q values for roots1,2,3,4 are161,166,174,171; their normalized radii are2^(q/4). Restoring the exact original first-harmonic amplitude gives sufficient radii2^50,2^51,2^53,2^53, respectively. The exact inequalities a^225<2^949 and a^9<2^38 certify the conversion. The stored per-box integer bounds were sometimes rounded more conservatively; restored_radii.json gives these sharper valid bounds without changing the boxes. The complete eight-profile batch took190.94635112816468seconds.
