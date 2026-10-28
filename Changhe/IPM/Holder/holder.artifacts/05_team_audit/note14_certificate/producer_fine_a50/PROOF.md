# Audit of the finer half-exponent producer certificate

## Exact statement and operators

Use the real homogeneous seminorm [f]_(1/2)=sup_(z!=w)|f(z)-f(w)|/|z-w|^(1/2). Define T_xx by circular principal values with kernel (z_1^2-z_2^2)/(2pi|z|^4), and by convergent increments modulo constants for nondecaying inputs. Put R_1^2=T_xx-I/2 and D_(1/2)=||R_1^2||. The exact witness is the polygon-plus-projection function from ../pole_profile/PROOF.md, with alpha=1/2, b=3/4, c=-3/20 and lambda=1000/1021. The accepted global profile certificate gives [f]_(1/2)<=1, f(0)=1/2 and f(e_1)=-1/2. The compact approximation theorem transfers every fixed increment lower bound to the supremum over real C_c^infinity inputs.

The lower endpoint obtained by the finite interval and analytic remainder contract below, plus the exact identity gain1/2, is therefore a lower bound for D_(1/2). It is admitted only after all checks are complete. This is an audit of producer task records with selected independent task replays, not a full independent fine-mesh replay. V164 supplies the separate complete coarser replay for this exponent.

## Source, coverage and interval contract

The producer uses delta=.0035, 80-bit directed arithmetic, near-pole radii10^(-8) through1/2, midpoint radii1/100 through10^8, and subdivision depth3. Its4019 tasks contain24900260 cells. The frozen source hashes must equal the producer's start and end hashes and the sidecar's start hashes. An abstract-syntax comparison with the already audited source snapshot must show that only the provenance-recording main routine changed; both imported geometry modules must match byte for byte.

Each task midpoint is itself a printed ball, and its printed radius is also a ball. Import them conservatively as [mid_lower-radius_upper, mid_upper+radius_upper]. Check finite values, nonnegative radii and error bounds, exact witness parameters, increasing radial edges, exact matching at every boundary, even angular counts and the complete cell total. The audited full-circle angular loop ensures angular coverage. The radial systems and exclusion rules are exactly those of the accepted cell proof; mixed and partial cells retain their absolute fallback errors.

Independently re-evaluate selected complete tasks, including endpoints of both systems, twelfths of their task lists, both sides of every angular-count transition, and the largest two contributions in each recorded error category. Match the full printed midpoint/radius tuple, cell count and error tuple exactly. A mismatch blocks acceptance. These checks corroborate the producer computation; they do not establish that unsampled cells were independently replayed.

## Original recombination

Sum all task intervals as exact rational endpoints. Let r0=10^(-8), eta=1/100, R=10^8. With alpha=1/2 the absolute bound per omitted pole disk is

    E_p=r0^alpha/alpha+r0^2(1/2+r0^alpha)/(2(1-r0)^2).

The midpoint sliver and original exterior bounds are

    E_0=2^(alpha+3)eta^(alpha+3)/(pi(alpha+3)sqrt(1-eta^2)),
    E_R=2^alpha(R/(R-1/2))^3 R^(alpha-1)/(1-alpha).

For the one-pole near sum N and midpoint sum W, the original complete trace-free increment is enclosed by 2N+W+[-2E_p-E_0-E_R,2E_p+E_0+E_R]. Compare this independent recombination with the printed producer summary, without using that printed lower decimal as input.

## Improved pole and exterior bounds

The accepted general quadratic pole and homogeneous exterior proofs apply to this same witness and exponent. A finite initial set of near tasks may be replaced by the analytic pole interval at its exact outer endpoint epsilon. Require (lambda+2^(alpha-1))epsilon^alpha<=c+1/2, lambda epsilon^alpha<=1/2 and0<epsilon<1/2. The lower pole bound is M-E_c-E_s, where

    C_e=(1-2epsilon)^(alpha-1),
    A=Gamma(1+alpha/2)/(2sqrt(pi)Gamma(3/2+alpha/2)),
    M=lambda A epsilon^alpha/alpha+epsilon^2/4,
    E_c=alpha C_e^3 epsilon^(3-2alpha)/(6pi lambda^2(3-2alpha)),
    E_s=epsilon^(alpha+2)/((alpha+2)(1-epsilon)^2).

The upper bound is M+E_s+U_c, with U_c=0 if alpha C_e epsilon^(1-alpha)<=lambda/2, and U_c=alpha C_e epsilon/pi otherwise. The proof controls the possibly negative clamp contribution by a positive quadratic integral; the pure projection and opposite-pole constant terms are exact. The original principal-value convention is unchanged.

For the exterior require lambda(1+2^(-alpha))>=1. Put H=sqrt((b+1/2)^2+b^2), B=max(H^alpha+|c|,1/2+2^(-alpha)), q=1/(4R^2). Its main term is T=2a_3(alpha)R^(alpha-1)/(1-alpha), with absolute error

    E_T=4B/(pi R)+B/(3R^3(1-q)^2)
                         +R^(alpha-3)/(2(3-alpha)(1-q)^2).

The accepted explicit angular formula defines a_3. Since alpha<1, the exterior dipole integral converges. Keep the midpoint sliver unchanged.

## Final endpoint and evidence

For retained near sum [N_-,N_+] and complete midpoint sum [W_-,W_+], the lower trace-free endpoint is

    L=2N_-+W_-+T_-+2M_--2(E_c)_+-2(E_s)_+-(E_T)_+-(E_0)_+.

The upper endpoint U uses the opposite directed endpoints and adds2U_c instead of subtracting2E_c. Then D_(1/2)>=1/2+max(0,L,-U). Every admissible choice of epsilon proves a bound, so selecting the largest among finitely many candidates is valid without a global optimization claim. The acceptance record binds sources, all imported tasks, selected replays, exact parameters, every analytic dependency and exact arithmetic. Final decimals are rounded downward.
