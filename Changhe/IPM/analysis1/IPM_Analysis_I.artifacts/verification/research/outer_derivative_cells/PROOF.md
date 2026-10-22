# Physical derivative norm bounds from exterior Taylor cells

Written 2026-10-22 before implementation. Status: analytic theorem with numerical application OPEN. This result concerns the distinguished exact normalized finite modal trial, its canonical velocity and c_l=1/k, not the stored X3 ansatz. It does not assert an inverse, existence or exclusion.

## Statement and fixed inputs

Use the exact exterior density and Green representation of outer_cells/PROOF.md, with its constants k=1615536043799051/9007199254740992, L=8614738245908811/1125899906842624 and b=2289893859708677/281474976710656. Put R=exp(b), tau=log(r/R), D=partial_tau. For the density sine modes j=0,...,260 and velocity modes n=1,...,261, define E_j=(D/k-1)rho_j, D_j=D rho_j and H_j=(2j+1)rho_j. Let p_n=U_r/r cosine coefficients and s_n=U_theta/r sine coefficients, including every canonical transient. The exact residual is

    eps = E + P D_rho + S H,
    E=sum E_j sin((2j+1)theta), D_rho=sum D_j sin((2j+1)theta),
    H=sum H_j cos((2j+1)theta), P=sum p_n cos(2n theta),
    S=sum s_n sin(2n theta).

These functions are finite sums of exp(lambda tau)c(tau), with c a polynomial of degree at most6 whose coefficients are exact affine functions of the same enclosed canonical normalization scalar. The scalar is not replaced by its midpoint. Canonical transient coefficients are enclosed by the accepted moment certificates. Identification with the distinguished canonical trial is a separate explicit dependency, requiring the accepted canonical linkage. Merely satisfying interval inequalities for arbitrary independent coefficients is insufficient to identify a canonical field.

We prove whole-cell upper bounds B_p>=||D^p eps||_W for p=0,1,2 and C_p>=||partial_theta D^p eps||_W for p=0,1. Here ||.||_W is the sum of the physical real sine or cosine coefficient magnitudes. All residual frequencies are odd and at most Omega=1043. Given complete cells covering 0<=tau<=17, the inequalities below bound the exterior contribution to

    ||f||_X^2 = integral_R2 (f^2+r^2|grad f|^2) w(r)dX,
    w(r)=L^6 r^-6(1+r^2/L^2)^(3/2-k),

for f=eps and f=eps-D eps, after joining the accepted derivative tail at tau=17. The numerical result requires every input, convolution, enclosure, coverage and tail check below and an actual subsequent independent review. No old zeroth-order bound is differentiated.

## Analytic derivative remainder

Fix exact 0<=a<c, t_c=(a+c)/2 and h=(c-a)/2>0. Write v=(tau-t_c)/h. Choose Q>=8, so Q-d+1>2 for d<=6. For one analytic term exp(lambda tau)c(tau), let

    A_l=h^l sum_(j=l)^d binom(j,l)c_j t_c^(j-l), ell=lambda h,
    P_q=exp(lambda t_c) sum_(l=0)^min(q,d) A_l ell^(q-l)/(q-l)!, 0<=q<=Q.

Let P(v)=sum P_q v^q be this exact Taylor polynomial, with its coefficients enclosed by interval arithmetic. For p=0,1,2, its physical derivative polynomial is h^-p partial_v^p P. Define (z)_s=z(z-1)...(z-s+1), (z)_0=1, with (l)_s=0 when s>l for nonnegative integer l. Put x=|ell| and N_l=Q-l+1. Then a valid derivative remainder bound is

    e_p = exp(lambda t_c) h^-p exp(x)
          sum_(l=0)^d |A_l| x^N_l
              sum_(q=0)^p binom(p,q)(l)_(p-q)/(N_l-q)! .       (1)

All denominators are factorials of nonnegative integers. At x=0 the tails vanish since N_l>p. Formula (1) is proved from the convergent analytic series, not by differentiating a real inequality. The omitted series for the l term starts at j=N_l. Its p-th v derivative has coefficient (l+j)_p ell^j/j!, and

    (l+j)_p=sum_(q=0)^p binom(p,q)(l)_(p-q)(j)_q.

For each q, the absolute omitted sum is bounded by

    sum_(j=N_l)^infinity (j)_q x^j/j!
       = x^q sum_(i=N_l-q)^infinity x^i/i!
       <= exp(x) x^N_l/(N_l-q)!.

Uniform absolute convergence on a slightly larger compact interval justifies differentiating each entire series. This proves (1) for exact coefficients; enclosing coefficient magnitudes and positive arithmetic only enlarge it.

An independent second method first differentiates the analytic input: set c^(0)=c and c^(p+1)=lambda c^(p)+(c^(p))'. Expand exp(lambda tau)c^(p)(tau) at t_c to degree Q-p using its own interval arithmetic, and apply the ordinary exponential tail formula at that degree. Its exact Taylor polynomial is h^-p partial_v^p P because Taylor coefficients are derivatives of the same entire function. For every input coefficient and every p, the independently computed derivative Taylor coefficient enclosure must overlap the differentiated original coefficient enclosure. This is a consistency test; the soundness of each enclosure comes from its analytic construction. These two derivative remainder methods have different coefficient operations and may give different upper bounds.

Sum term polynomials before coefficient absolute values, retaining cancellations between all radial exponentials. Sum their nonnegative derivative remainder bounds. Multiplication by the scalar R^2 or R^3 is enclosed, including its coefficient uncertainty. For every input family A in {E,P,D_rho,S,H}, write A_c for its degree-Q Taylor polynomial and set

    N_(A,p)=sum_modes sum_(l=p)^Q (l)_p |(A_c)_l| h^-p,
    e_(A,p)=sum_modes e_(mode,p).

Both bound the indicated physical derivative polynomial or remainder on the whole cell. Interval coefficient dependence can be forgotten because this enlarges the set. Each actual coefficient is fixed; the proof differentiates its exact polynomial, not a choice of interval values varying with tau.

## Residual polynomial and errors

Construct the complete degree at most2Q residual polynomial

    Z(v,theta)=E_c+P_c D_c+S_c H_c

before taking any absolute values. Retain all522 physical sine modes. The primary method uses the full signed Fourier encoding and interval polynomial convolution; the independent method uses compressed even/odd angular indices and exact integer center-radius convolution, as derived in outer_cells/PROOF.md. The radial stride2Q+1 prevents aliasing. Every resulting real sine coefficient at every degree must have overlapping enclosures in the two independent methods.

For p<=2, the retained physical derivative polynomial is Z_p=h^-p partial_v^p Z. This derivative is computed algebraically from the full polynomial coefficients. Its error is bounded in Wiener norm by

    delta_p=e_(E,p)+sum_(l=0)^p binom(p,l) [
      N_(P,l)e_(D,p-l)+N_(D,p-l)e_(P,l)+e_(P,l)e_(D,p-l)
      +N_(S,l)e_(H,p-l)+N_(H,p-l)e_(S,l)+e_(S,l)e_(H,p-l)].   (2)

To prove (2), apply Leibniz to the exact analytic factors, substitute each exact derivative polynomial plus its separately proved derivative remainder, and use the Wiener algebra inequality. Each product has one sine factor. Product-to-sum shows submultiplicativity of the physical coefficient sums here; no zero angular mode occurs. The same argument applied term by term gives (2) with no omitted mixed product. Since exact and polynomial residuals have frequencies at most1043, the angular derivative error is at most1043 delta_p. This last estimate differentiates a finite Fourier series with known support, not a radial majorant.

For each sine mode of Z_p, retain radial degrees0,...,Q (padding missing coefficients by zero) and convert to degree-Q Bernstein coefficients on v=2x-1. The basis is nonnegative and sums to1 on0<=x<=1. Let b_(nu,p) be the maximum absolute Bernstein coefficient plus the absolute sum of coefficients of degrees greater thanQ. Then

    B_p=sum_nu b_(nu,p)+delta_p,
    C_p=sum_nu nu b_(nu,p)+1043 delta_p.                     (3)

This preserves cancellation in the differentiated polynomial, including between its linear and nonlinear terms. The high-degree sum controls the entire discarded polynomial, not a sampled value. The independent integer method differentiates centers and radii by exact nonnegative falling factorials, applies the exact Q!-scaled Bernstein matrix and finally divides by h^p. For each mode and p, it retains an exact outward rational upper bound. Interval overlap alone is never treated as a proof of an upper bound; publish an exact ceiling above both sound engines.

## Radial integrals, joins and scope

In logarithmic radius t=b+tau, write

    v_w(t)=exp(2t)w(exp(t))
          =L^6 exp(-4t)(1+exp(2t)/L^2)^(3/2-k).

Its logarithmic derivative is -4+(3-2k)exp(2t)/(L^2+exp(2t))<0. Hence the exact physical cell tau in[a,c] contributes at most

    pi(c-a)v_w(b+a)[B0^2+B1^2+C0^2],
    pi(c-a)v_w(b+a)[(B0+B1)^2+(B1+B2)^2+(C0+C1)^2]           (4)

to the two norm squares. The factor pi follows from full-circle orthogonality of the nonzero real sine and cosine modes. The identity r^2|grad f|^2=|D f|^2+|partial_theta f|^2 gives (4). All powers, weights and sums use independent outward interval arithmetic. Use exact true cell widths and verify the consecutive rational endpoints, beginning0 and ending17.

For tau>=17, derivative_end_tails/PROOF.md gives a coefficientwise analytic derivative bound, with independently checked exponentials, polynomial weights and integrals. Join its norm-square upper bounds at exactly17 to the sum of (4); this has only measure-zero overlap. The finite cell formulas also match the middle model at tau=0 through the accepted canonical piecewise regularity and linkage. This statement itself concerns only the exterior. A whole-plane theorem needs a separately certified middle annulus and inner disk, with the same canonical trial, normalization, norm and cutoffs. Such a later composition may improve the coarse exterior term in topic179; it may not replace or silently rewrite the accepted179 output.

## Verification obligations

Before accepting a numerical instance: preserve the proof-before-code record and exact source inputs; verify the canonical identification; rehash all inherited accepted content (using any historical source replacement only through an explicit proved same-byte map); check the independent exact Green recurrence; check all derivative-input coefficients; compare every residual polynomial coefficient; validate every finite-cell enclosure and complete exact covering; recompute the tail join and final scalar sums in a different method; retain complete compact output with stream hashes; replay selected cells including the smallest, endpoint, broad exterior and largest contributions; obtain actual Opus5.5 review of the implemented proof and actual output, and a later independent adjudication. Missing coverage or an invalid source pin leaves the instance OPEN. No numerical existence, exclusion or X3-distance follows from this derivative norm bound alone.
