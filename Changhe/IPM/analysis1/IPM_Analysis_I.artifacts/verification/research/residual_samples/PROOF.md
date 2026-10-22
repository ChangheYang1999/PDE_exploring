# Independently enclosed residual samples of the exact modal trial

Date: 2026-10-20. Status: CONFIRMED for the thirteen specified points, with source and independent product/output audits complete. The conclusion is a finite set of pointwise residual and angular Wiener bounds. It does not establish a global residual norm or validate the numerics lane's whole-cell Taylor arithmetic.

## Exact object and dependency

Use the exactly normalized modal trial defined in ../modal_repair/PROOF.md, with finite density expansion

rho(r,theta)=r^3 sum_{j=0}^{260} R_j(t) sin(nu_j theta), t=log r, nu_j=2j+1.

The additional R_261 slot is identically zero. All coefficients and common knots have exact binary64-input definitions; the dependent scalar correction is defined by the exact canonical normalization and enclosed independently. Reconstruct the density projection, six-jet coefficients and both canonical density moments by the procedure proved in ../modal_green/PROOF.md. No exported Green value or dependent decimal coefficient is an input.

Each comparison point is the exact rational log-midpoint of an exported numerics cell. Its endpoints are reconstructed from the original rational knots and integer parent group counts. The parent groups must cover every original span exactly once. The reported midpoint-radius boundary balls must contain all exact endpoints. This fixes the point independently of a rounded exponential. Physical radius r=exp(t) is evaluated outward.

## Residual identity

Write m_n=2n for n=1,...,261, and use the density moments i_n,j_n of ../modal_green/PROOF.md. Set

A_n=r^4[(R_{n-1}+R_n)/2-m_n i_n],
B_n=r^4[m_n j_n-(R_{n-1}+R_n)/2].

The canonical stream coefficients are psi_n=(A_n+B_n)/(2m_n). Their log derivative is (B_n-A_n)/2, because A_n'=-m_n A_n+G_n and B_n'=m_n B_n-G_n. In polar coordinates U_r=-r^{-1}psi_theta and U_theta=r^{-1}psi_t. Also rho_r=r^2 sum_j(3R_j+R_j')sin(nu_j theta) and rho_theta=r^3 sum_j nu_j R_j cos(nu_j theta). Therefore the residual is the finite sine polynomial

E(r,theta)=c_l X.grad rho+U.grad rho-rho
 =r^3 sum_j[c_l(3R_j+R_j')-R_j]sin(nu_j theta)
 +(r/4)sum_{n,j}{-(A_n+B_n)(3R_j+R_j')
       [sin((nu_j+m_n)theta)+sin((nu_j-m_n)theta)]
      +(B_n-A_n)nu_j R_j
       [sin((m_n+nu_j)theta)+sin((m_n-nu_j)theta)]}.

This follows by the exact product identities 2sin(a)cos(b)=sin(a+b)+sin(a-b). Negative frequencies are converted using sin(-a)=-sin(a); no frequency is zero because m_n is even and nu_j is odd. The largest frequency is1043, so all coefficients E_N for frequencies2N+1, 0<=N<=521, are included. The identity includes both radial and tangential signs and the canonical c_l=1/k.

## Point enclosures and comparisons

At each exact log point, integrate all i_n from the center endpoint and all j_n from infinity. Every polynomial integral is enclosed using the proved exponential-moment Taylor bound and a checked |lambda h|<129. Evaluate R_j and its derivatives from exact Cox polynomials. Outward Arb arithmetic in the finite identity above encloses every E_N. Then

W_point=sum_N |E_N|,
W_point/m(r),
pi sum_N |E_N|^2

are respectively the pointwise angular Wiener sum, its weighted value, and the exact angular L2 integral over0<=theta<=2pi. Absolute values are interval operations, giving both lower and upper bounds on the first two quantities. Parseval here is just integration of a finite trigonometric polynomial: the sine functions of distinct positive integer frequencies are orthogonal and have squared integral pi.

The numerics whole-cell value W_cell is only comparison data. If the independent point upper bound is <= W_cell, that sample is consistent with the claim, but the rest of the cell is not verified. If the independent lower bound exceeds W_cell, the corresponding cell claim is refuted. Overlap alone proves neither conclusion. All comparison files, selected cell indices, exact points, code and input hashes must be recorded. The finite-point calculation supplies no upper bound for any untested point or global integral.

## Independent Laurent-polynomial output audit

The task's conventions are explicitly (IPM-SS), PROMPT.md section1: U=(-psi_y,psi_x), -Delta psi=partial_x rho, and epsilon=(c_l X+U).grad rho-rho. Section2's reported numerical residual has the same sign. The exact modal repair separately enforces c_l=1/k through3c_l-c=1. The comparison weight is the numerics artifact's chosen m(r)=u^3(1+u^2)^((k-3)/2), u=r/L, with L the exact dyadic modal input; it is not claimed to be the only weight allowed by PROMPT.md. SPEC section4.1 uses that base weight and an additional far factor, which is not included in this finite-point W/m comparison.

The num source cert_resid.py constructs real sine coefficients at frequencies2N+1, bounds each over a cell using its claimed Bernstein Taylor model, and sets W to the sum of those upper bounds. Its W_over_m divides by a claimed lower bound for m on the cell. The comparison is therefore of the same scalar functionals; this audit does not accept the arithmetic that produced those whole-cell bounds. The num array includes a few additional identically zero frequencies, which do not alter the mathematical Wiener sum.

For a second reconstruction of the finite product, put z=exp(i theta). A real sine sum sum f_n sin(n theta) has imaginary Laurent coefficients -f_n/2 at+n and+f_n/2 at-n. A real cosine sum has real Laurent coefficients f_n/2 at both signs. The imaginary Laurent coefficients of the residual are obtained by two polynomial multiplications:

E=r^3 linear_sine +(r/2)[-cos(A+B) sin(D)+sin(B-A) cos(nu R)].

Shifting density Laurent polynomials by521 and velocity polynomials by522 turns these into ordinary polynomial products centered at1043. The sine coefficient for positive nu is the negative twice-imaginary coefficient at+nu, equivalently the difference of the imaginary coefficients at-nu and+nu. This reconstructs every residual coefficient without using the original nested sine-index scatter. All polynomial multiplication and imported moment balls use outward arithmetic. Direct mpmath.iv angular substitutions provide additional sign checks, without replacing the algebraic proof.

The output audit must parse the immutable published JSON numbers as exact decimals, compare them again with the new enclosures, verify all pinned dependencies and boundary widths, and record these corrected comparisons. The first-run comparison fields, which converted a JSON number through binary64, are provisional. Reading one immutable byte string before calculation and writing that same byte string later is not a race: the byte hash fixes the complete input independently of any later changes to the external file. The pre-completion hash was independently recorded as439df9893cf99ee0389e04358ff79146e7a95e71a061d1d09d025879ddacc331 on2026-10-20 at15:52:47Z.

Completed2026-10-20T16:00:14Z in927.23seconds. The independent Laurent product and mpmath.iv audit finished16:00:48Z in17.70seconds, checking6786coefficients and65angularsubstitutions. Actual Claude Opus5.5 accepted the finite-point certificate at16:05:20Z, conditional on the separately confirmed moment, reconstruction, canonical inverse and ball-transport dependencies. The product audit shares the independently computed moments with the first computation; it is not a second integration. The authoritative exact-decimal comparison file is evidence/laurent_output_audit.json. All13samples are consistent for W and W/m; no full-cell conclusion follows from these point data.

Functional provenance is separately checked in evidence/functional_provenance.json: exact k and L agree with the hashed trial NPZ and the archived residual source identifies W and division by m. Its arithmetic is not accepted.
