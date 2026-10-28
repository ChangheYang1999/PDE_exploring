# Direct sharp Hilbert norms for both circle metrics

## Statement and scope

Let 0<alpha<1. On the circle R/(2pi Z), write

    d_ang(x,y) = min_(k in Z) |x-y+2pi k|,
    d_ch(x,y) = |exp(ix)-exp(iy)| = 2 sin(d_ang(x,y)/2).

For either metric d, define [f]_(alpha,d)=sup_(x!=y) |f(x)-f(y)|/d(x,y)^alpha, where the points are distinct on the circle. Let f be a continuous real or complex function of finite seminorm. Define

    Hf(x) = (1/(2pi)) pv integral_(-pi)^pi f(y) cot((x-y)/2) dy,

with the circular principal value. The proposed exact operator norm, for either metric separately, is

    sup_[f]_(alpha,d)>0 [Hf]_(alpha,d)/[f]_(alpha,d)
       = N_alpha
       = 2^(1-alpha) B((1-alpha)/2,alpha)/pi
       = Gamma(alpha/2) Gamma((1-alpha)/2)/pi^(3/2).

The supremum has the same value if inputs are restricted to smooth periodic functions. These are increment seminorms; no supremum term is included. The two metrics and seminorms differ.

This proof supplies a direct upper bound by an explicit coupling of the two difference-kernel lobes, and a lower bound by rescaling compact real-line inputs. It does not use Babenko's announced exact fixed-increment theorem or any assertion of attainment in that source. The independently proved real-line sharp constant and compact approximation in ../hilbert_exact/PROOF.md are the only sharp-norm dependency. The present result is OPEN until its independent analytic cross-read is recorded.

## Principal values and an explicit periodic pairing

For either metric, Holder continuity makes the local kernel after subtracting f(x) integrable: d_ch(x,y)<=d_ang(x,y), and the remaining integrand is bounded by a multiple of |x-y|^(alpha-1). The principal value therefore exists. Constants are killed by circular odd-kernel cancellation.

Rotation reduces every increment to the evaluation points -a,a, where 0<a<=pi/2 and h=2a is their angular distance. For y away from those points, elementary cotangent addition gives

    (1/2)[cot((a-y)/2)-cot((-a-y)/2)]
        = sin a/(cos y-cos a) = F_a(y).

The function F_a is even, positive on (0,a) and negative on (a,pi). Put b=tan(a/2). For 0<u<a define rho(u) by

    tan(rho(u)/2) tan(u/2) = b^2,
    a<rho(u)<pi.

This is a decreasing smooth bijection from (0,a) to (a,pi). Direct differentiation gives the positive-mass identity

    F_a(rho(u)) rho'(u) = F_a(u).

Thus the negative lobe is coupled to the positive one. The transform increment is

    Hf(a)-Hf(-a)
       = (1/pi) integral_0^a F_a(u)
           [f(u)-f(rho(u))+f(-u)-f(-rho(u))] du.             (1)

Here is the principal-value justification. Change variables in the negative lobe while truncating the positive interval at a-epsilon and the negative interval at rho(a-epsilon). Since rho(a)=a and rho'(a)=-1, the latter endpoint is a+epsilon+O(epsilon^2). Replacing it by the symmetric cutoff a+epsilon changes the constant part of the logarithmic singular integral by O(epsilon), and its Holder remainder by O(epsilon^alpha). These terms vanish. The same reasoning applies at -a. Excluding a vanishing neighborhood of the other pole in each original principal value changes only an integrable regular term there. Finally the paired integrand in (1) is integrable near a, bounded by a constant times (a-u)^(alpha-1), and near zero it is bounded for fixed a. This proves (1) with the stated circular principal values.

Both paired distances between u and rho(u), or between their negatives, have angular distance rho(u)-u in (0,pi). Applying the input increment bound in (1) gives

    |Hf(a)-Hf(-a)| / d(a,-a)^alpha
      <= [f]_(alpha,d) * (2/pi) integral_0^a F_a(u)
           [d(u,rho(u))/d(a,-a)]^alpha du.                 (2)

This is an upper estimate only; no claim of fixed-increment optimality is needed.

## A common upper constant

Use s=tan(u/2)/b, so 0<s<1. Then

    u=2 arctan(bs), rho=2 arctan(b/s), F_a(u)du=2ds/(1-s^2).

For the angular metric, the distance ratio in (2) is

    Q_ang(b,s) = [arctan(b/s)-arctan(bs)]/[2 arctan b].

Put c=(1-s^2)/s. Arctangent subtraction is on the branch (0,pi/2), and

    arctan(b/s)-arctan(bs)
      = arctan(cb/(1+b^2)) <= cb/(1+b^2) <= c arctan b.

The last step follows from arctan b>=b/(1+b^2), whose difference has nonnegative derivative and vanishes at zero. Hence Q_ang<=(1-s^2)/(2s).

For the chordal metric the distance ratio is instead

    Q_ch(b,s) = (1+b^2)(1-s^2)
                 / [2 sqrt((s^2+b^2)(1+b^2s^2))].

The exact algebraic identity

    (s^2+b^2)(1+b^2s^2)-s^2(1+b^2)^2=b^2(1-s^2)^2>=0

gives the same bound Q_ch<=(1-s^2)/(2s). Both ratios are nonnegative. Consequently (2), in either metric, is at most

    [f]_(alpha,d) * (2^(2-alpha)/pi)
        integral_0^1 s^(-alpha)(1-s^2)^(alpha-1) ds
      = N_alpha [f]_(alpha,d).

The integral converges precisely for 0<alpha<1. Substitution t=s^2 evaluates it as half the beta integral B((1-alpha)/2,alpha). Gamma duplication gives the alternative expression for N_alpha. This proves the operator upper bound for all inputs, including complex inputs since only absolute-value increment bounds were used.

## Local rescaling proves sharpness

The real-line theorem in ../hilbert_exact/PROOF.md proves that the supremum over real g in C_c^infinity(R) with [g]_alpha<=1 of their normalized Hilbert output increments is N_alpha. Fix one such nonzero g, supported in [-M,M], and fixed distinct real evaluation points x,y.

For sufficiently small epsilon>0 define a smooth periodic function by

    f_epsilon(theta)=epsilon^alpha g(theta/epsilon),  -pi<=theta<=pi,

and periodic extension. Its support lies strictly inside (-pi,pi), so the extension is smooth. Put delta=sqrt(epsilon).

If an angular pair distance d is at most delta and at least one input value is nonzero, lift the supported point to [-M epsilon,M epsilon] and the other to distance d from it. For small epsilon both lifts lie in (-pi,pi), and the line Holder inequality gives |f_epsilon(theta)-f_epsilon(phi)|<=d^alpha. If both values vanish the same inequality is immediate. For chordal distances this yields an input quotient at most

    [delta/(2 sin(delta/2))]^alpha = 1+o(1),

because d/(2 sin(d/2)) is increasing on [0,pi]. For angular distances greater than delta, the quotient is at most 2 epsilon^alpha ||g||_infinity/delta^alpha, which tends to zero. For chordal distances at such pairs, replace the denominator by (2 sin(delta/2))^alpha and obtain the same conclusion. Therefore

    [f_epsilon]_(alpha,ang)<=1,  for sufficiently small epsilon,
    [f_epsilon]_(alpha,ch)<=1+o(1).

The transform also has the correct local limit. For any fixed real x,

    epsilon^(-alpha) Hf_epsilon(epsilon x)
      = (epsilon/(2pi)) pv integral_(-M)^M g(v) cot(epsilon(x-v)/2) dv
      -> (1/pi) pv integral_R g(v)/(x-v) dv = H_R g(x).

Indeed cot t-1/t extends continuously through zero and is O(t) on a fixed neighborhood, so the error in this expression is O(epsilon^2) for fixed x and g. No interchange of a nonintegrable error with a principal value is involved. The same limit holds at y. The angular output distance is epsilon|x-y| for small epsilon, and its chordal distance divided by epsilon tends to |x-y|. It follows that the limiting normalized periodic output increment is

    |H_R g(x)-H_R g(y)|/|x-y|^alpha.

The input seminorms are bounded by 1+o(1), so each periodic operator norm is at least this quantity. Taking the real-line supremum proves the lower bound N_alpha. The lower construction uses smooth real functions; it therefore proves sharpness for smooth inputs and also for complex inputs. Together with the direct upper bound, this proves the stated exact norms without any announced-theorem dependency.

## Relation to the literature audit

The reciprocal tangent pairing agrees with the one explicitly appearing in the retained Babenko source, but every identity and inequality needed here has been proved above. The proof does not assert Babenko's more general exact increment formula or its extremizers. The earlier periodic and chordal notes remain accurate deductions from that stated theorem; the present proof supplies a separate complete argument for these two specific operator norms. No planar Riesz or Beurling bound follows from this auxiliary one-dimensional result.
