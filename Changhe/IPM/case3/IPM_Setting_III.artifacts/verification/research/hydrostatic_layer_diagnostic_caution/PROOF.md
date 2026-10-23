# Residual collapse caused by a homogeneous inverse, without a density layer

Result218. This is a diagnostic theorem for arbitrary smooth hydrostatic trial densities. It does not concern a solution of the full elliptic IPM problem, and does not prove that a true nonlinear inner layer exists. Written before its verification code.

## Precise statement

Fix0<p<1, c=1/p, alpha=(1+p)/2, n=alpha*p, d=2p-1 and D=max(d,0). Let f_p be homogeneous of degreep, even inx, odd iny, with a smooth angular trace and f_p(0,y)=K*y^p for y>0, whereK>0. Let g be a smooth even-x/odd-y density on the whole plane such that outside a fixed ball

 |partial^j(g-f_p)(X)|<=C_j*|X|^(d-j), 0<=j<=3.                  (1)

Here partial^j denotes each Cartesian derivative of total orderj. Put w=g-f_p away from zero. Use the canonical hydrostatic velocities

 V1[g](x,y)=-int_y^infinity g_x(x,t)dt,
 V2[g](x,y)=int_0^y t*g_xx(x,t)dt+y*int_y^infinity g_xx(x,t)dt.    (2)

The formulas extend by parity and are used fory>0. The corresponding homogeneous density has, for|x|/y sufficiently small,

 V2[f_p](x,y)=a*y^p+Cp*|x|^p+O(x^2*y^(p-2)),
 V1[f_p](x,y)=O(|x|*y^(p-1)), a=Q/[p*(1-p)],                    (3)

where Q is its axis curvature coefficient. These canonical formulas and expansions are proved in [the independent hydrostatic inverse](../independent_hydrostatic_evaluator/PROOF.md) and [the trace compatibility audit](../hydrostatic_trace_compatibility_diagnostic/PROOF.md). They can also be obtained directly by expanding f_p at the axis in (2), with the scale-homogeneous integration constantCp.

Define the signed transport residual and the first normalization exactly as in the task:

 R=(cx+V1)g_x+(cy+V2)g_y-g,
 Nf=|(cx+V1)g_x|+|(cy+V2)g_y|+|g|, H=R/Nf.                     (4)

Then, uniformly forz in each fixed bounded real interval,

 y^(1-n)*[H(y^alpha*z,y)-H(0,y)]
       -> (p*Cp/2)*|z|^p, asy->infinity.                       (5)

More precisely the error is O(y^(D-n)*log(2+y)). SinceD<n, it tends tozero. Thus an apparent collapse under this rescaling can be an automatic property of a fixed smooth trial with an ordinary homogeneous far field. It is not by itself evidence for the nontrivial smooth inner density correction of result215. This theorem also does not assert that any finite data range has reached its asymptotic regime.

## Proof: canonical velocity of the remainder

The functionw may be singular atzero becausef_p is homogeneous there. Its singularity is O(r^p), with derivativesO(r^(p-j)). Its contribution to the first integral inV2 is uniformly bounded nearzero: the local absolute bound is a constant times int_0^1 t*(x^2+t^2)^((p-2)/2)dt, which is bounded forp>0. Away from the core (1) applies.

Uniformly for|x|<=y and largey, splitting the first integral into core and exterior parts gives

 |V2[w](x,y)|<=C*(1+y^D*log(2+y)).                             (6)

For the exterior part use int t*(x^2+t^2)^((d-2)/2)dt; when d<0 it is bounded away from the fixed core, when d=0 it is logarithmic, and when d>0 it is O(y^d). The tail integral multiplied byy is O(y^d), since d<1. ForV1 only t>=y occurs, and

 |V1[w](x,y)|<=C*|x|*y^(d-1)<=C*y^d.                         (7)

For the stronger first bound in (7), evenness and (1) give |w_x(x,t)|<=C*|x|*t^(d-2) for t>=y and |x|<=y. Both bounds are sufficient; no missing core constant is assumed to vanish.

## Proof: the unnormalized difference

Write T=c*X.dot(gradient)-1. Euler's identity gives Tf_p=0. For|x|<=Z*y^alpha and largey, smooth angular parity implies

 f_p=K*y^p+O(x^2*y^(p-2)),
 (f_p)_y=p*K*y^(p-1)+O(x^2*y^(p-3)),
 (f_p)_x=O(|x|*y^(p-2)).                                      (8)

By (1), evenness and Taylor's theorem inx, with derivatives through order3,

 Tw(x,y)-Tw(0,y)=O(x^2*y^(d-2)).                              (9)

Expand R=Tw+V[f_p].grad f_p+V[f_p].grad w+V[w].grad g. Equations (3),(8) give

 [V[f_p].grad f_p](x,y)-[V[f_p].grad f_p](0,y)
   =p*K*Cp*|x|^p*y^(p-1)+O(x^2*y^(2p-3)).                    (10)

Terms with the cusp times the derivative remainder also obey the stated bound for|x|<=y. Since2alpha=p+1, (9) and the error in (10) are O(y^(3p-2)) on the inner scale. The interactionV[f_p].gradw is O(y^(p+d-1))=O(y^(3p-2)); no cancellation betweenx andzero is needed to bound it. Equations(6),(7) imply

 V[w].gradg=O(y^(D+p-1)*log(2+y))+O(y^(d+alpha+p-2)),

and the second term is smaller than the first foralpha<1. Consequently

 R(y^alpha*z,y)-R(0,y)
   =p*K*Cp*y^(n+p-1)*|z|^p
      +O(y^(3p-2)+y^(D+p-1)*log(2+y)).                        (11)

The estimates are uniform on every boundedz interval, includingzero.

## Proof: the absolute-value denominator

Individually R(x,y)=O(y^d) on this scale. Indeed Tw=O(y^d), the main homogeneous product is O(y^(2p-1))=O(y^d), and the other terms just bounded are smaller. In particular the remainder velocity bound does not change this estimate, sinceD+p-1<d forp>0 whenD=0, and likewise whenD=d.

The densityg and vertical transport(cy+V2)g_y are positive for largey, uniformly on the inner scale: their leading terms areK*y^p andc*p*K*y^p=K*y^p. The horizontal transport has magnitudeO(x^2*y^(p-2)), using (8) and the derivative bounds onw. Therefore

 Nf=2*K*y^p*(1+O(y^(p-1))).                                  (12)

This conclusion does not assume a sign for the horizontal transport. Combining R=O(y^d) with (12) gives

 H(x,y)=R(x,y)/(2*K*y^p)+O(y^(2p-2)).                          (13)

Substitute(11) into the difference of(13), multiply byy^(1-n), and use

 n-d=(1-p)*(2-p)/2>0, n>0.

The error is O(y^(d-n)+y^(D-n)*log(2+y)), proving(5).

## An explicit smooth manufacture with no density layer

For any0<p<1 take

 g(x,y)=y*(1+x^2+y^2)^((p-1)/2), f_p(x,y)=y*(x^2+y^2)^((p-1)/2). (14)

Thisg is C-infinity, has the required parities andg_y(0)=1, and has a conventional expansiong=f_p+O(r^(p-2)) with corresponding derivative bounds. Sincep-2<2p-1, it satisfies(1). It is used only as a manufacture, not as a PDE solution. Let beta0=(p-1)/2 and B=1+x^2. Then

 V1=x*(B+y^2)^beta0,
 V2=-int_0^y (B+t^2)^beta0 dt
       -2*beta0*x^2*int_0^y (B+t^2)^(beta0-1)dt.                   (15)

The first identity follows by integratingg_x. Differentiating the second iny gives the correct sign d_yV2=int_y^infinity g_xx; more explicitly it is -[(B+y^2)^beta0+2*beta0*x^2*(B+y^2)^(beta0-1)], which is that tail integral. AlsoV2(x,0)=0, so (15) equals(2).

Put

 B0=sqrt(pi)*Gamma(-p/2)/(2*Gamma((1-p)/2)),
 B1=sqrt(pi)*Gamma(1-p/2)/(2*Gamma((3-p)/2)).

The finite part of int_0^Y(1+t^2)^beta0 dt isB0. It can be derived by integrating the convergent subtraction fromt^(p-1), or by the beta recurrence; it is negative. The second integral toinfinity is the ordinary convergent beta integralB1. The homogeneous velocity therefore hasa=-1/p and

 Cp=-B0-(p-1)*B1=-(1+p)*B0>0.                                (16)

For stable independent high-precision evaluations, for beta=beta0 orbeta0-1 use the exact antiderivative continuation

 int_0^y(B+t^2)^beta dt
  =sqrt(pi)*Gamma(-beta-1/2)/(2*Gamma(-beta))*B^(beta+1/2)
    +y^(2beta+1)/(2beta+1)
       *2F1(-beta-1/2,-beta;1/2-beta;-B/y^2).                  (17)

Its derivative is(B+y^2)^beta. Its additive constant is fixed by the convergent second case and the subtracted first case. Direct physical quadrature at moderatepoints independently tests(17) and(15). Equation(5) predicts a nonzero collapsed curve(p*Cp/2)|z|^p even though(14) contains no inner correction. The true density defect on the inner scale is O(y^(p-2)), strictly belowy^q becauseq-(p-2)=n+1>0.

## Scope

The theorem requires the derivative-controlled asymptotic expansion(1) andcp=1 exactly. It need not apply to a floating storedmap whose true exponent differs from1/c. It concerns the hydrostatic auxiliary inverse and signed normalized residual, not the full elliptic PDE residual. Arbitrary visual collapse under another normalization is not asserted. A genuine nonlinear layer must be tested in the density correction and in the coupled inner equations, with far-field and inverse errors separated. Conversely failure to see collapse at finitey does not exclude such a layer.
