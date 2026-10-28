# A certified neighborhood of the exact modal source

Status: analytic construction proved; numerical bounds pending independent audit.

## Statement and dependencies

The background is the exactly joined, exactly normalized modal density of
`../04_modal_scalar/PROOF.md`. The point P=(p,0) is its unique velocity zero in
[a,b], where a=4841405518533377/562949953421312 and
b=4841405518533711/562949953421312, certified in
`../15_modal_source/PROOF.md`. Put delta=33/2000 and V=X/k+U[rho].
This note specifies a reproducible certificate for

M_V = sup_{B_{3 delta}(P)} ||D^2 V||_F,
M_rho = sup_{B_{3 delta}(P)} ||D^2 rho||_F.

The Frobenius norm here sums over both derivative indices and, for V, the
vector component. Thus ||D^2 rho||_F^2=rho_xx^2+2rho_xy^2+rho_yy^2 and
||D^2 V||_F^2=psi_xxx^2+3psi_xxy^2+3psi_xyy^2+psi_yyy^2 because
U=(-psi_y,psi_x). Numerical upper bounds will only be asserted after the
interval output and its algebra are audited.

## Enclosing the physical ball

The positive-radius rectangle

r_min=a-3delta, r_max=sqrt((b+3delta)^2+(3delta)^2),
|theta| <= arctan(3delta/(a-3delta))

contains B_{3delta}(P) for every p in [a,b]. It suffices to enclose each
Cartesian derivative on its logarithmic radial and angular rectangle.
Parity permits theta>=0: rho and psi are odd in y, so every derivative's
absolute value is invariant under y reflection. Split the logarithmic
interval at every modal spline knot and then into finitely many closed
subintervals; split the angular interval likewise. This is a finite cover,
including every shared boundary.

## Radial functions and their derivatives

Use the sine coefficients H_j(t) in
rho=e^{3t} sum_{j=0}^{261} H_j(t) sin((2j+1)theta).
Their exact polynomial pieces are obtained from the original NPZ's dyadic
B-spline coefficients by the signed sine projection proved in proof 15.
There is no use of the archived Green tables.
For m=2n, 1<=n<=261, let

I_n(t)=exp(-(m+4)t) integral_{-infinity}^t exp((m+4)s) H_{n-1}(s) ds,
J_n(t)=exp((m-4)t) integral_t^infinity exp((4-m)s) H_n(s) ds.

Then psi=e^{4t} sum_n (J_n-I_n)sin(mtheta)/2. The defining tails converge
by the exact exponents and the source reconstruction in proof 15. Boundary
values are independently propagated across every radial span with exact
polynomial/exponential moments. In a local span [t0,t1], the partial
integrals use the uniformly convergent exponential series with its explicit
remainder, also proved in proof 15. Ball arithmetic encloses their values
on a whole subinterval, not merely at its midpoint.

For j>=1, differentiation of the defining integrals gives

I_n^(j)=(-(m+4))^j I_n
       + sum_{l=0}^{j-1} (-(m+4))^(j-1-l) H_{n-1}^(l),
J_n^(j)=(m-4)^j J_n
       - sum_{l=0}^{j-1} (m-4)^(j-1-l) H_n^(l).

The needed H derivatives are derivatives of the exact degree7 polynomial.
All endpoint jets through order6 agree, so either adjacent piece is valid
at a shared knot. There is no differentiation of numerical point samples.

## Cartesian differentiation

Write D=d/dt. For e^{qt} f(t) sin(mtheta), an x derivative produces

(e^{(q-1)t}/2)[((D+q-m)f)sin((m+1)theta)
                        +((D+q+m)f)sin((m-1)theta)],

and a y derivative produces

(e^{(q-1)t}/2)[-((D+q-m)f)cos((m+1)theta)
                         +((D+q+m)f)cos((m-1)theta)].

For cosine replace sine by cosine in the x formula; the y formula is

(e^{(q-1)t}/2)[((D+q-m)f)sin((m+1)theta)
                        -((D+q+m)f)sin((m-1)theta)].

These identities follow directly from d_x=e^{-t}(cos(theta)D-sin(theta)d_theta)
and d_y=e^{-t}(sin(theta)D+cos(theta)d_theta). Repeated application, retaining
signed frequencies, supplies the second density and third stream derivatives.
Every sum is finite. Interval evaluation followed by the displayed Frobenius
formulas therefore provides rigorous upper bounds on the physical ball.

## An explicit cutoff of sufficient regularity

Let S(v)=126v^5-420v^6+540v^7-315v^8+70v^9 on [0,1].
Then S'(v)=630v^4(1-v)^4, S(0)=0, S(1)=1, S(1-v)=1-S(v), and
its first four derivatives vanish at both endpoints. Set epsilon=1/8 and

 d(t)=S(t/epsilon) for 0<=t<=epsilon,
 d(t)=1 for epsilon<=t<=1-epsilon,
 d(t)=S((1-t)/epsilon) for 1-epsilon<=t<=1,
 d(t)=0 outside [0,1].

The function d is C^4, 0<=d<=1, and integral d=1-epsilon=7/8.
Define Theta(t)=1-(8/7) integral_0^t d(v)dv on [0,1], extended by1 on
t<=0 and by0 on t>=1. Thus Theta is C^5, 0<=Theta<=1, and
||Theta'||_infinity=8/7. Finally set

 theta_delta(X)=Theta((|X-P|-2delta)/(7delta/8)).

It is constant near P and hence C^5 everywhere, equals1 on B_{2delta}(P),
and has support in the closed ball of radius23delta/8, which is contained
in B_{3delta}(P). Its derivative obeys delta||grad theta_delta||<=64/49.
All higher derivatives required by proof 18 are bounded on their compact
annular support.

## Consequence for the auxiliary inverse

Let D0=DV(P), g=rho_y(P),
w=theta_delta(V-D0(X-P)), and
q=theta_delta(grad rho-(0,g)). The Taylor theorem with integral remainder
and the Frobenius norm imply, throughout the support,

|V-D0(X-P)| <= (9/2)delta^2 M_V,
||DV-D0||_F <= 3delta M_V,
|grad rho-(0,g)| <= 3delta M_rho.

Moreover div(V-D0(X-P))=0 exactly: div V=2/k=tr D0. Hence
||div w||<= (9/2)(64/49)delta M_V,
||Dw||_F<=delta(3+(9/2)(64/49))M_V,
||q||<=3delta M_rho.
For s=31/10 the perturbation E of proof 18 therefore satisfies

E <= delta{[3s+(9/2)(s+1/2)(64/49)]M_V+3M_rho}.

If the certified right side is less than1687/500, proof 18 supplies the
closed maximal-domain auxiliary inverse. Its full norm additionally
requires the explicitly defined higher coefficient norm R. This note does
not certify R, the rank-one denominator, a localized boundary inverse,
or a full-plane IPM inverse.

## Taylor enclosure used by the implementation

For stability the code evaluates I and J at the exact midpoint t_c of a
radial subinterval, then encloses their derivatives by Taylor polynomials
there. Let H(t_c+v)=sum_{j=0}^7 h_j v^j. If I'+aI=H, a=m+4,
its Taylor coefficients obey i_0=I(t_c) and
j i_j=h_{j-1}-a i_{j-1}, with h_l=0 for l>7. The exact polynomial
particular solution S has s_7=h_7/a and
s_j=(h_j-(j+1)s_{j+1})/a. Consequently
I(t_c+v)=S(v)+(i_0-s_0)exp(-av).
For J'=bJ-H, b=m-4 nonzero, use
j j_j=b j_{j-1}-h_{j-1}, s_7=h_7/b,
s_j=(h_j+(j+1)s_{j+1})/b and the exponential exp(bv).
When b=0, J is a polynomial of degree8 exactly.

With a Taylor polynomial through degree N=20 and |v|<=eta, the error in
its j-th derivative, 0<=j<=3, is at most

|i_0-s_0| a^j exp(a eta) (a eta)^{N-j+1}/(N-j+1)!

for I, and the analogous expression with |b| for J. This is the exponential
Taylor remainder, differentiated j times; the polynomial particular part
has degree7 and is represented exactly. The J error is0 if b=0. These
bounds are added in ball arithmetic before Cartesian differentiation.
The implementation combines exact derivative polynomials and equal angular
frequencies before interval evaluation. This finite rearrangement changes
no function and reduces interval dependency. All Taylor coefficients,
midpoint integrals, remainders and trigonometric ranges are enclosed.
