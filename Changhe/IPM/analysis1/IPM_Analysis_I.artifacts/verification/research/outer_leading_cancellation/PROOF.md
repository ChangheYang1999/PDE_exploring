# Retaining the leading exterior residual cancellation

Date: 2026-10-20. Status: analytic derivation independently reviewed; the two numerical constructions passed, with final source and proof pins recorded in evidence/verdict.json. The exact normalized modal density, common radius R=exp(t_b), exponent k, polynomial Green coefficients and the coarse exterior majorant are the audited dependencies in ../outer_majorant/PROOF.md and its evidence/verdict.json. This note sharpens one coefficient of that majorant. It does not certify outer Taylor cells or any inverse theorem.

## The coefficient that may be replaced

Let tau=log(r/R)>=0. Write the exact exterior density coefficients as in outer_majorant:

rho_j(tau)=R^3 sum_b exp(beta_b tau)c_(j,b)(tau),   j=0,...,260.

There are ten degree-zero bases beta_b=k-j_b(1-k)-2l_b and the degree-six correction beta_c=3-b_o. The ten pairs are (0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(0,2). Set gamma_*=2k-1 and nu_j=2j+1. Since 0<k<1/2 and b_o>120, beta_0=k is strictly the largest exponent, beta_1=gamma_* is the next largest, and every other beta is strictly smaller than gamma_*.

The linear part (k^-1 partial_t-1)rho has coefficient R^3(beta_1/k-1)c_(j,1) at exp(gamma_* tau). The beta_0 linear term vanishes exactly. A product of two particular terms has exponent beta_b+beta_c-1; equality to gamma_* occurs only when b=c=0. A transient product has exponent -2n-2+beta_b<=k-4<gamma_*. These are strict exact inequalities and are also enumerated with rational arithmetic in the computation. Therefore the only sources of the gamma_* coefficient are the single linear basis and the leading-leading particular product. Its polynomial degree is zero.

Write a=k+1 and m=2n. Put d_j=c_(j,0), with d_261=0, and

F_n=[(a-m)d_(n-1)+(a+m)d_n]/2,
q_n^+=F_n/(a+m),   q_n^-=-F_n/(a-m).

The normalized coefficients of U_r/r and U_theta/r in their leading particular term are

v_n=-(q_n^++q_n^-)/2,   w_n=(q_n^--q_n^+)/2.

Thus that velocity contribution is R^2 exp((k-1)tau) times sum_n v_n cos(m theta), sum_n w_n sin(m theta), respectively. These expressions follow from the previously proved canonical Green formulas; no exterior homogeneous velocity is omitted, since it remains among the transient terms of the coarse majorant.

Let e_q be the real sine coefficients of the following finite trigonometric polynomial:

sum_(q=0)^521 e_q sin((2q+1)theta)
 =R^3 sum_j (beta_1/k-1)c_(j,1)sin(nu_j theta)
 +R^5[(sum_n v_n cos(m theta))(sum_j k d_j sin(nu_j theta))
      +(sum_n w_n sin(m theta))(sum_j nu_j d_j cos(nu_j theta))].

This is precisely the coefficient of exp(gamma_* tau) in the true residual. There are522possible sine frequencies, with maximum1043. Define C_*=sum_q |e_q|. The exact normalization correction is retained through the full audited scalar interval for z; d_j is affine in z, so each e_q has degree at most two in z, apart from the exact scalar factors R^3 and R^5.

## Two independent angular constructions

For the primary construction introduce a formal variable zeta for the compressed angular indices. This zeta is unrelated to the normalization scalar z. Even frequency2n has index n; odd frequency2j+1 has index j. The cosine velocity has Laurent coefficients v_n/2 at indices+n and-n. The sine velocity has coefficients w_n and-w_n at those indices after removing the common factor1/(2i). The radial density sine has coefficients k d_j and-k d_j at indices j and-j-1. The angular density cosine has coefficients nu_j d_j/2 at indices j and-j-1.

Consequently ordinary Laurent multiplication gives both products in the preceding display, with the common sine factor1/(2i) removed. Shifting the even index range[-261,261] and odd range[-261,260] to nonnegative arrays gives lengths523 and522. The product has length1044 and output position q+522 represents the positive sine frequency2q+1. This is an exact convolution identity, without sampling, angular truncation or aliasing. Arb polynomial multiplication encloses its coefficients.

The independent construction derives the stream coefficient directly from the radial Poisson equation. Since -(partial_r^2+r^-1 partial_r-m^2r^-2)r^a=(m^2-a^2)r^(a-2), the leading stream coefficient is R^4 F_n/(m^2-a^2). Hence

v_n=-m F_n/(m^2-a^2),   w_n=a F_n/(m^2-a^2).

These equal the Green expressions by elementary fraction addition. The independent code reconstructs d_j and c_(j,1) from the exact raw cosine data by signed trigonometric projection, using the audited z interval. It then expands the products directly with

cos(m theta)sin(nu theta)=[sin((nu+m)theta)+sin((nu-m)theta)]/2,
sin(m theta)cos(nu theta)=[sin((m+nu)theta)+sin((m-nu)theta)]/2.

Negative sine frequencies change sign, and none of these odd frequencies is zero. The direct sum includes every261by261pair. This uses mpmath.iv and does not import the primary convolution coefficients. Every one of the522primary coefficient intervals and their absolute sum is compared to the independent result. The audit requires the entire independent iv interval to lie inside the primary Arb interval. All1070such comparisons passed at Arb384bits and iv160decimal digits. This criterion is stronger than necessary and could fail for valid differently associated computations; any such failure remains an unaccepted audit until explicitly resolved. No containment was weakened to mere intersection.

## Replacement without subtraction from a bound

The coarse majorant is a finite sum sum_(gamma,l) C_(gamma,l) tau^l exp(gamma tau), with nonnegative coefficients. Its gamma_* row contains only l=0. Replace that whole row by C_*, leaving every other row at its audited exact rational upper endpoint. Call the resulting coefficients D_(gamma,l). This gives another valid majorant for W(tau), because the exact residual coefficient at gamma_* is the e vector just reconstructed. This argument does not subtract an estimated cancellation from an absolute residual upper bound. It replaces one complete, identified trigonometric coefficient before taking absolute values. No omitted angular or radial degree contributes to this row.

The scalar maximum, weighted estimates and L2 consequence in outer_majorant now apply with D in place of C:

sup_(tau>=T) W <= sum D_(gamma,l) M_(-gamma,l,T),
sup_(tau>=T) (1+r/L)^delta W/m <= K_delta(T) sum D_(gamma,l) M_(k-delta-gamma,l,T),
N_ext <= sqrt(pi)L K_0(0) sum D_(gamma,l) sqrt((2l)!/[2(k-gamma)]^(2l+1)).

Here m(r)=(r/L)^3[1+(r/L)^2]^((k-3)/2), u_0=R/L,

M(a,l,T)=x^l exp(-a x), x=max(T,l/a),
K_delta(T)=u_0^(delta-k)[1+u_0^(-2)exp(-2T)]^((3-k)/2)[1+u_0^(-1)exp(-T)]^delta,
N_ext^2=integral_(r>=R) |epsilon/m|^2 dX/[1+(r/L)^2].

The maximum formula follows by differentiating tau^l exp(-a tau). The factors in K decrease with tau, leaving the exponential with rate k-delta-gamma. The angular identity integral |epsilon|^2 dtheta<=pi W^2, r^2/[1+(r/L)^2]<=L^2 and Minkowski's inequality give the L2 display, using integral_0^infty tau^(2l)exp(-2(k-gamma)tau)dtau=(2l)!/[2(k-gamma)]^(2l+1). These steps agree with the proof in outer_majorant. For delta=0,1/2,1/2-k the smallest weighted rates are respectively1-k,1/2-k,1/2, which are positive. The smallest L2 rate is1-k. The scalar sums are independently recomputed with interval arithmetic. The shared nonleading coefficient upper endpoints are explicit already-audited dependencies, not a new independent integration of those modes.

## Verified numerical consequences

For every tau>=T, the strict bounds below hold for the exact normalized modal trial. Each decimal is interpreted as an exact rational upper bound and checked against both interval results in code/finalize_verdict.py.

| T | W | W/m | (1+r/L)^(1/2) W/m | (1+r/L)^(1/2-k) W/m |
|---|---|---|---|---|
| 0 | 17145004 | 5740429 | 121374223 | 40621479 |
| 9 | 0.000020450600 | 0.000001362864 | 0.002591031 | 0.000172670851 |
| 10 | 0.000008067437 | 0.000000449353 | 0.001408491 | 0.000078452209 |
| 17 | 0.000000066848357 | 0.000000001060902 | 0.000110121685 | 0.000001747661 |

Also C_*<0.003623778, replacing the old gamma_* coefficient upper bound160.153387682903..., and N_ext<4949188. The original coefficient is the unique gamma_* row of the pinned outer_result.json, and its exact rational upper endpoint is recorded as old_C_star_upper_exact. The final verification includes1048exact raw projection scalar equalities and68121direct trigonometric pairs. Actual Claude Opus5.5 reviewed the theorem and sources, corrected its overstrong general rate claim after challenge, and accepted the exact row isolation argument. Its degree and length checks were added before the final rerun.

## Scope

This method retains the leading linear/nonlinear angular cancellation at gamma_*. It still discards cancellations between different exponentials, particularly near the matching boundary. Its usefulness for a far-tail bound does not imply a small whole-exterior bound. No derivative norm, X3 distance, global inverse or decisive endpoint follows from this calculation alone.
