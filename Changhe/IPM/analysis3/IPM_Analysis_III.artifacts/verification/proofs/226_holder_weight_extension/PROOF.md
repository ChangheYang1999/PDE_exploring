# The common Holder obstruction for every residual-compatible weight

## Exact statement

Fix 0<alpha<1 and the actual joined normalized modal trial, k and ell. Let E2 be the physical-parity space used in proof 213, with bounded supremum, horizontal alpha-Holder seminorm, h(0,y)=0 and vertical alpha-Holder seminorm divided by x^2. Set p=2k-1<0. For every gamma>4k define

 Y_gamma=E2 intersect L2(w_gamma),
 w_gamma=(1+r^2)^(-gamma/2),
 ||h||Y_gamma=||h||E2+||h||L2(w_gamma).

The full normalized moving-tail coupling C0h=U[h].grad rho0+c[h]M0 is bounded E2->E2 and Y_gamma->Y_gamma for EVERY gamma>4k. The same holds for Cren with M0 replaced by H0. Both realizations A0=T+C0 and Lren=T+Cren are closed on their exact maximal transport domains, in E2 and Y_gamma respectively. The actual residual F0 belongs to E2 and to every such Y_gamma.

Let beta_R=1-chi_*(X/R), with chi_* smooth radial,1 on B1 and0 outside B2. For R sufficiently large,

 ||beta_R C0||Y_gamma->Y_gamma
 <=C_(alpha,gamma) (R^(k-1)+R^(k-gamma/2)
                        +R^p+R^(2k-gamma/2))(1+log R),   (1)

and the two weighted terms may be omitted for the E2->E2 estimate. Every exponent is strictly negative. For Cren omit the M0 terms R^p and R^(2k-gamma/2), once the compact H0 tail is zero.

For each of these realizations, T, Lren and A0 have infinite algebraic cokernel. They are not onto and are not Fredholm. The explicit family of source forcings in proof 220 already supplies linearly independent range cosets in E2 itself. It supplies the same conclusion in every Y_gamma above. No statement that the particular residual F0 is outside the range, no nonexistence of a profile, and no obstruction to the scaled space Z of proof 222 follows.

This extends the gamma<2 range stated in topics214/217/220. The restriction gamma<2 was needed for the weighted velocity theorem used there. It is not needed for the complete coupling into a residual-compatible target, because the density gradient decays. Constants here are qualitative; no numerical estimate is supplied.

## The E2 bounds and the absolute weighted coupling estimate

The global directional kernel proof of proof 214 gives, for M=||h||E2,

 ||U[h].grad rho0||E2<=C_alpha M,
 |U[h](X)|<=C_alpha M(1+log(2+r)),
 |c[h]|<=4M/pi.                                      (2)

These are E2 estimates: the proofs of the ordinary horizontal bound, U1/x bound and vertical divided-product bound use only M, not a weighted L2 input. The local normalization column H0 is E2. Proof 217 proves M0 is E2. Thus C0 and Cren are bounded E2 operators with their canonical velocity convention, including every point and divided-axis image.

For clarity the weighted part can be proved without an L2 velocity bound at all. The exact finite far formulas give |grad rho0|<=C r^(k-1) for sufficiently large r. Hence (2) implies

 |U[h].grad rho0|<=C M r^(k-1)(1+log r).

For any gamma>2k and R sufficiently large,

 integral_(r>=R) |U[h].grad rho0|^2 w_gamma dX
 <=C M^2 integral_R^infinity r^(2k-1-gamma)(1+log r)^2 dr
 <=C_gamma M^2 R^(2k-gamma)(1+log R)^2.              (3)

The last inequality follows by substituting r=R exp(s) and integrating the quadratic polynomial in log R+s against exp(-(gamma-2k)s). The denominator gamma-2k is positive. On a fixed compact disk (2)'s E2 bound supplies a finite weighted L2 norm. Since gamma>4k>2k, (3) proves U[.].grad rho0:E2->L2(w_gamma), with norm bounded independently of any input L2 norm. In particular it proves the asserted complete coupling on Y_gamma.

The same polar integral for M0=O(r^p(1+log r)) gives

 ||beta_R M0||L2(w_gamma)
      <=C_gamma R^(p+1-gamma/2)(1+log R)
       =C_gamma R^(2k-gamma/2)(1+log R),             (4)

finite precisely under the stated sufficient strict condition gamma>4k. Its compact part is controlled by E2. The scalar bound in (2) completes the full column estimate. No weight-class extrapolation of the velocity multiplier has been made.

## The entire E2 output tail, including the column

Proof 214's E2 product estimates give

 ||beta_R U[h].grad rho0||E2
       <=C M R^(k-1)(1+log R).                     (5)

They include vertical differences crossing the radial cutoff. This estimate is proved entirely from the directional kernels and bounded E2 input, and does not depend on gamma.

For M0 retain an E2 tail term that cannot be discarded when gamma>=2. The exact modal parity and axis divisions in proof 217 give, on r sufficiently large,

 |M0|<=C r^p(1+log r), |D M0|<=C r^(p-1)(1+log r),
 |M0/x^2|<=C r^(p-2)(1+log r),
 |partial_y(M0/x^2)|<=C r^(p-3)(1+log r).           (6)

The divided expressions extend continuously to x=0. The finite angular polynomials retain the x^2 factor; the parameter derivative adds only the logarithm. Multiplying by beta_R gives the same bounds with powers of R for their global suprema and first derivatives. The cutoff derivative is O(1/R) where r is comparable to R. The products extend by zero to the interior with those derivative bounds.

For a globally bounded Lipschitz function f, its alpha seminorm is at most C_alpha ||f||infinity^(1-alpha)||Df||infinity^alpha, by splitting differences at ||f||infinity/||Df||infinity (constant or zero functions cause no difficulty). Apply this to beta_R M0 in the x direction and to beta_R M0/x^2 in the y direction. Equation (6) gives horizontal bound C R^(p-alpha)(1+log R), divided vertical bound C R^(p-2-alpha)(1+log R), and supremum bound C R^p(1+log R). Since R>=1,

 ||beta_R M0||E2<=C R^p(1+log R).                   (7)

Combining (3)-(7) and the scalar bound proves (1) and its E2 version. For gamma<2 the E2 term R^p is dominated by R^(2k-gamma/2), which explains its absence from the earlier statement. For gamma>=2 it is retained. All tails tend to0.

## Maximal domains, residual and the range obstruction

Both E2 and Y_gamma are Banach and converge locally uniformly. Define D_B={h in B:V.grad h belongs to B distributionally}, for B either E2 or Y_gamma. Distributional passage to the limit shows T=V.grad-1 is closed on D_B. Boundedness of C0 or Cren makes its full maximal expression domain exactly D_B: subtract the bounded coupling in either direction. These statements do not require smooth density in the domain.

Proof 213 proves F0 in E2. Its exact nonzero far leading term is r^p S_F(theta), with faster remainder, so its weighted L2 condition is gamma>2p+2=4k. Thus all stated targets contain the actual residual. For gamma>2, boundedness of h already implies its weighted L2 norm is bounded by a constant times ||h||infinity, so Y_gamma is even equivalent to E2 as a Banach space. The argument includes gamma=2 as well without that equivalence.

We repeat the relevant range logic to specify why no weighted hypothesis is missing. Fix a large Y and 0<x sufficiently small. The exact actual forward flow satisfies x_t comparable to x exp(ell t) and y_t comparable to Y exp(ell t), with fixed comparison constants, as proved from the finite far axis quotients in proof 220. For any h in D_E2 and f=A0h, boundedness of h and the continuous distributional characteristic equation imply

 h(x,Y)=-integral_0^infinity exp(-t)f(Phi_t(x,Y))dt
          +integral_0^infinity exp(-t)(C0h)(Phi_t(x,Y))dt.

Proof 220 derives, solely from the E2 directional bounds and the actual far coefficients, the all-future estimate

 |integral exp(-t)(C0h)(Phi_t(x,Y))dt|
       <=C_Y ||h||E2 x^2(1+log(1/x)).              (8)

For the nonlocal product it combines the two envelopes min(x_t^2 r_t^(k-2),r_t^(k-1)log r_t), then splits at a constant multiple of log(1/x). The full M0 term contributes O(||h||E2 x^2), using (6), ell k=1 and ell>1. No weighted L2 bound is used in this characteristic estimate.

For b in (1/2,1), take the exact smooth odd-y far-strip forcing

 f_b=x^2 phi(x)g_b(y)-c[x^2 phi g_b]q,

where phi is even, compact in |x|<=2 and1 on |x|<=1, g_b(y)=y^(-b) for y sufficiently large and is0 near the physical origin, and q is a fixed compact smooth physical-parity c=1,J=0 correction below the tested height. Proof 220 checks c[f_b]=J(f_b)=0, f_b in E2, and Tf_b in E2. Its weighted square integral is finite for every gamma>4k, since 2b+gamma>1 on this strip; the compact correction is harmless. Thus it belongs even to every displayed transport domain.

The positive part of the forcing characteristic integral, up to leaving the x strip, is at least d_b x^(k+b)-C x^2. Since k+b<2, this cannot be reconciled with (8) and the E2 bound |h(x,Y)|<=||h||E2 x^2Y^alpha. Thus f_b is not in A0(D_E2). The same argument applies to Lren and T, omitting the relevant coupling terms. Any preimage in Y_gamma would in particular be an E2 preimage, so it is excluded too.

For any finite nonzero linear combination of distinct b values, the smallest b with nonzero coefficient dominates at sufficiently large Y. Its eventual sign fixes the same leading characteristic integral, and the identical estimate excludes a preimage. The resulting range cosets are linearly independent. This proves infinite algebraic cokernel, hence non-surjectivity and failure of Fredholmness, on every stated realization.

## Scope and dependencies

The common global weighted vertical Holder norm, including E2 alone, cannot be the onto target of these full maximal realizations. The scaled far norm Z imposes different annular control and is not covered by this conclusion. The exact residual could still belong to the range of a non-surjective operator. The local inverses, possible stronger normalized domains and the separate Sobolev construction remain unaffected.

Dependencies: topics213/214 for E2 mapping, actual coefficient estimates and residual membership; proof 217 for M0 divisions; topics117/220 for the exact far powers and fully checked range packets. The new weight range, complete tail norm and transfer to E2 are proved above. No numerical computation or unconditional existence/nonexistence claim is used.
