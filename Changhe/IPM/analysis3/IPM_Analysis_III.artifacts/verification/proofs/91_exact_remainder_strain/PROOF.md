# Exact norm of the strain functional on the strong remainder space

## Statement

Let R be the real parity subspace of L2(w dX) on R2, where

 w(X)=|x|^(-17/2)max(1,|X|)^(29/4),
 h(-x,y)=h(x,y), h(x,-y)=-h(x,y).

Then the absolutely convergent functional

 c_R[h]=(1/pi) integral_R2 sin(3theta) r^(-3) h(X)dX

has exact operator norm

 C_R=[(58/99)(6618/725) B(3/2,19/4)/pi^2]^(1/2),

where B is Euler's beta function. In particular C_R<20757/100000=0.20757. This also bounds c_R on the maximal transport domain D_R equipped with its Hilbert graph norm. It is the norm of the functional, not the norm of the similarly named remainder coupling operator.

## Proof and sharpness

Weighted Cauchy-Schwarz gives the squared norm as the integral of the squared kernel divided by w. In polar coordinates,

 integral_0^1 r^(-6)r^(17/2)r dr=2/9,
 integral_1^infinity r^(-6)r^(5/4)r dr=4/11.

Their sum is58/99. This proves integrability at both ends. The angular factor is integrable at both axes and equals

 I=integral_0^(2pi) sin^2(3theta)|cos theta|^(17/2)dtheta
  =2[16B(3/2,27/4)-8B(3/2,23/4)+B(3/2,19/4)].

Indeed sin(3theta)=sin(theta)(4cos^2(theta)-1), and quadrant symmetry followed by the substitution z=sin^2(theta) gives the displayed beta integrals. The recurrence B(a,b+1)=b B(a,b)/(a+b) gives

 B(3/2,23/4)=(19/25)B(3/2,19/4),
 B(3/2,27/4)=(19/25)(23/29)B(3/2,19/4).

Thus I=(6618/725)B(3/2,19/4), proving the formula. The weighted Riesz representative is the kernel divided by w. It belongs to R and has the required even-x, odd-y parity, so Cauchy-Schwarz is sharp within this parity subspace. Smooth compact parity functions supported away from the axes are dense in R, so restricting the functional to this dense class does not change its R norm. The graph norm dominates the R norm, giving the stated graph bound without asserting sharpness for that stronger norm.

The finite decimal bound is checked by directed Arb gamma-function evaluation of B(a,b)=Gamma(a)Gamma(b)/Gamma(a+b) at256 and384 bits, including an independent evaluation of the three-term beta expression. There is no truncation of a numerical integral or modal sum. The estimate depends only on the exact weight and kernel convention, already fixed by the actual strong realization.
