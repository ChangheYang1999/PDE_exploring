# The axis row from a slightly lower-order remainder space

## Statement

Use the actual background, weights and smooth order s of topics123 and130. Put sigma=25/4 and, for 0<=epsilon<=1/4, let X_(s-epsilon) have the same weights, parity and zero cofactor trace as X_s, with both Sobolev orders lowered by epsilon. Let Gamma_C be the canonical complete axis row of C_ren. Then

 h -> Gamma_C[h]/a

is bounded from X_(s-epsilon) to H^(51/8)(R), and compact from X_(s-epsilon) to H^(25/4)(R). Its operator norm is finite and may be chosen uniformly for epsilon in [0,1/4]. No numerical value is asserted.

Consequently E Gamma_C maps X_(s-epsilon) compactly into the trace-unrestricted space Xhat_s of proof 138, whose largest target order is25/4. The image generally has nonzero cofactor trace and is not separately asserted to lie in X_s. This is an improvement specific to the factored high space. It does not follow merely by reusing the critical four-dilation-derivative embedding into R_(4,sector).

## A direct trace estimate

First work on a fixed Cartesian patch about the vertical axis, away from the origin. Let h(x,y)=x^2 w(x,y), where w has compact support in a fixed strip |x|<=L and belongs to ordinary H^q(R^2), q>=0. The canonical second velocity component is U_2=-M, M with multiplier xi^2/(xi^2+eta^2). Fourier transform only in y, unitarily. Since h(0,y)=0, the local negative identity contribution has zero trace. Solving the one-dimensional resolvent in x gives

 T_hat(eta)=(|eta|/2) integral_R exp(-|eta||x|)x^2 w_hat(x,eta) dx,
 T(y)=U_2[h](0,y).                                     (1)

For |eta|>=1, Cauchy-Schwarz and an exact gamma integral give

 |T_hat(eta)|^2
 <=(3/8)|eta|^(-3) integral_R |w_hat(x,eta)|^2 dx,       (2)

because

 (|eta|^2/4) integral_R exp(-2|eta||x|)x^4 dx
 =(eta^2/4) 2(4!)/(2|eta|)^5=(3/8)|eta|^(-3).

For |eta|<=1 use the compact x support in (1); the bound is a fixed constant times integral |w_hat|^2. Multiplying by <eta>^(2q+3) and integrating proves

 ||T||_H(q+3/2)(R)<=C_(q,L)||w||_Hq(R^2).               (3)

The right side could even be the weaker L2_x H^q_y norm. Formula (1) and the estimate first hold on a smooth core. Approximation proves the trace and its continuity for all stated w and identifies it with the canonical trace. No trace of an arbitrary L2 density was assumed.

## The complete local row

Let y be bounded above and below by positive constants on the patch. Write alpha(t)=rho(x,y)/(x^2 y) at x=0, t=log y, and V_h(t)=T(exp(t))/exp(t). The exact row is

 Gamma_C[h]=(alpha'-alpha)V_h-2alpha V_h'
                      +c[h]chi_0(alpha+alpha'/3).      (4)

The change y<->t is a smooth diffeomorphism on this patch. Thus (3) gives V_h in H^(q+3/2) and V_h' in H^(q+1/2). The actual coefficients alpha, alpha' and the cutoff products belong locally to H^(51/8), with uniform normalized annular bounds. This follows from the C6 joined degree-seven trial: alpha' has sixth weak derivative with finitely many jumps and belongs to every H^r with r<13/2. The value51/8 is strictly below13/2.

For the input space in the theorem q=sigma-epsilon lies in[6,25/4]. Hence

 q+1/2>=13/2>51/8.

The one-dimensional H^(51/8) algebra estimate applied to (4) proves the local H^(51/8) row bound. The strain term is finite rank and its functional is bounded: X_(s-epsilon) embeds continuously into the physical R space because its cofactor order is at least6, above the required angular Hardy order9/4, and its bulk order is at least9/5>1. Endpoint weights are unchanged. Thus the previously accepted R-dual strain bound applies.

On a comparable input annulus in the vertical sector, h=x^2 times a smooth multiple of the local cofactor u, so (3) applies after the fixed annular rescaling. Input outside a slightly larger vertical sector has positive distance from the output axis and is handled by a smooth kernel. Its required output derivatives are bounded by the input L2 norm and the same geometric scale factors. This checks both angular pieces without assuming the lower-order input still has four R-valued dilation derivatives.

## Uniform radial summation and the normalization cancellation

Use logarithmically spaced annuli as in proof 123 and normalize every output row by a(t). For a comparable input annulus of radius R, the physical amplitude b(R)=R^3 a(R), the velocity trace division by y and the derivative in (4) yield a factor R^2 a(R). After division by a(R), its inner same-scale factor is R^2. At the outer end the background cofactor contributes the additional R^(k-3), so the factor is R^(k-1). The H^q-to-H^(51/8) estimate just proved is uniform on unit rescaled annuli; its constants for q in[6,25/4] are uniformly bounded.

For separated input and output radii all required rescaled output derivatives fall on a smooth kernel. The parity moment bounds and the exact linear-strain cancellation are exactly those of proof 123, before axis subtraction. Taking the output axis trace does not change a scale power when the separated kernel is already smooth. Near the origin the full expression (4), or equivalently its cancellation form

 Gamma_C=(alpha'-alpha)(V_h-c[h])-2alpha V_h'
                                      +(4/3)c[h]alpha',

must be used before summing the distant input. This removes the uncancelled constant strain and gives the same six matrix estimates, now for the normalized scalar H^(51/8) output:

 s<=r<=1: C r^2(s/r)^(delta+2),
 r<=s<=1: C r^(2-delta)s^delta,
 1<=s<=r: C r^(k-1)(s/r)^(gamma+3),
 1<=r<=s: C r^(k-1)(s/r)^(gamma-1),
 r<=1<=s: C r^(2-delta)s^(gamma-1),
 s<=1<=r: C r^(k-4-gamma)s^(delta+2).                  (5)

Here s in (5) is an input radius, not the Sobolev order function. These bounds require only the annular L2 norm for separated inputs. The input X_(s-epsilon) annular norm is stronger. The background H^(51/8) coefficient multiplication is uniform after extracting its indicated scale power, by the exact finite endpoint expansions and the finite knot interval.

The row and column sums in proof 138 therefore apply unchanged. They give the global H^(51/8) bound and uniform output tails bounded by

 C exp(-R/5) at the inner end,
 C exp(-(1-k)R) at the outer end.

The local annular H^(51/8) square sum is equivalent to the ordinary global H^(51/8) norm, since the output has already been divided by a. The finite transition region only changes the constant.

## Compactness and the target trace

On any fixed compact t interval, bounded H^(51/8) sets are precompact in H^(25/4), with an order gap1/8. The uniform tail estimates above make the complement of a sufficiently large interval uniformly small. Combining the local compactness and tail control proves compactness into H^(25/4).

The lift E satisfies E Gamma_C/b=p Gamma_C/a, while its cofactor is Gamma_C/a times the fixed sector cutoff. Smooth angular multiplication gives the asserted Xhat_s mapping. Its axis trace is precisely Gamma_C/a, so omitting the target zero-trace condition for this separate term is essential.

The theorem resolves this particular lower-order remainder in a possible high-frequency estimate. It does not prove the transport commutator or positive-quantization estimates, and it makes no global H3 assertion.
