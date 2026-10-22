# A smooth beta=2 transport field with a compact equilibrium segment

Status: analytic counterexample to a transport-only closure strategy. CONFIRMED by direct algebra below; independent review requested. It deliberately does not satisfy the vorticity transport equation and is not a B2 profile.

## Exact statement

There exist globally smooth Psi, U=(-Psi_y,Psi_x), Omega=-Delta Psi and Theta on R^2 with the following properties. With W=2X+U, div W=4, U=O((1+r)^(-1)) and Omega=O((1+r)^(-1)). Psi and Omega are odd in x, Theta is even, Theta(0,y)=0 and Theta=a0 x^2 near zero, for any prescribed a0>0. The equation W.grad Theta=0 holds everywhere. The full zero set of W is exactly Z=[-1,1] times {0}. At both endpoints of Z, Theta-Theta(1,0) and Omega have every Taylor coefficient zero. The canonical ordinary full-plane velocity exists and equals U, with U(0)=0 and Psi_xy(0)=2.

The defining vorticity equation fails: in a neighborhood of zero Omega=0 and Theta=a0 x^2, so

    W.grad Omega+Omega-Theta_x = -2 a0 x.

Thus compactness of Z, flat scalar and vorticity jets at its endpoints, the exact temperature transport, positive constant divergence, and the canonical sublinear inverse do not by themselves give beta=2 nonexistence. A closure must also use the vorticity transport beyond these properties.

## 1. Smooth scalar functions used in the construction

Let b be a nonnegative C-infinity probability density on (1,2), positive throughout that interval, with all endpoint jets zero. For instance normalize exp(-1/[(s-1)(2-s)]) there and set it to zero elsewhere. Define the positive moments m1=int s b(s) ds and m2=int s^2 b(s) ds. Put

    h(y)=int_1^2 max(|y|,s) b(s) ds,
    H(y)=int_0^y h(v) dv,
    g(y)=m1/h(y),
    f(y)=4H(y)/h(y)-2y.

The flat endpoint jets of b make h smooth. It is even, equals m1 on |y|<=1, equals |y| on |y|>=2, and is nondecreasing for y>=0. Consequently g=1 and f=2y on |y|<=1. For |y|>=2, direct integration gives H(y)=sign(y)(y^2+m2)/2, so f(y)=2m2/y and g(y)=m1/|y|. For y>0, monotonicity of h gives 0<H(y)<=y h(y), hence -2y<f(y)<=2y. The corresponding absolute bound |f(y)|<=2|y| holds on the whole line. Differentiating H'=h proves

    f'(y)=2-[h'(y)/h(y)](2y+f(y)),
    g'/g=-h'/h.                                                (1)

For r>=0 define eta(r)=int_1^r b(s) ds with b zero outside (1,2), interpreted as zero for r<=1. Thus eta=0 for r<=1 and eta=1 for r>=2. Define

    q(r)=0 (r<=1), q(r)=int_1^r eta(s)/s ds (r>1),
    chi(I)=exp(-2 q(|I|)).

This is smooth and even, chi=1 on |I|<=1, and 0<chi<1 outside. For r>=2 it is Cchi/r^2, where Cchi=exp(2 int_1^2 log s b(s) ds). At all I,

    a(I):=chi(I)+I chi'(I)=chi(I)[1-2 eta(|I|)] > -1.            (2)

Indeed the bracket is at least -1, and chi<1 wherever eta can be positive. Also a<=1. The function 1+a has a strictly positive global minimum: it is continuous, strictly positive, and tends to1 at infinity.

Finally let F be smooth and even, F(I)=a0 I^2 on |I|<=1/4, strictly increasing on 0<I<1, and constant M>0 on |I|>=1, with all positive-order derivatives zero at I=1 and I=-1. Such a function is obtained by integrating F'(I)=2a0 I rho(|I|), where rho is a nonnegative smooth cutoff equal to1 near zero, positive on [0,1), zero on [1,infinity), and flat at1.

## 2. Fields, transport and equilibria

Set

    I(x,y)=x g(y), Psi=x f(y) chi(I), Theta=F(I).

All these are smooth, and the required x parity is immediate. On the region |I|<=1, chi=1, so

    W1=x(2-f'), W2=2y+f.

Equation(1) gives W.grad I=x g[(2-f')+(2y+f)g'/g]=0. On |I|>=1, F'=0. Thus W.grad Theta=0 everywhere, including the transition boundary by smoothness. At zero, |x|,|y| small gives Psi=2xy and Theta=a0 x^2 exactly. Thus W=(0,4y), the center strain is2, and Omega=0 in this neighborhood.

For the equilibrium set, differentiation at arbitrary I gives

    W2=2y+f(y) a(I).

By |f(y)|<=2|y| and -1<a<=1, this has the sign of y whenever y!=0. To check strictness in the possibly extreme case, if |a|<1 the inequality is strict; if a=1 then |I|<=1 and W2=4H/h has the sign of y. There is no case a=-1. Thus every equilibrium lies on y=0. There I=x, f(0)=0, f'(0)=2, so

    W1(x,0)=2x[1-chi(x)], W2(x,0)=0.

This vanishes precisely for -1<=x<=1. At either endpoint chi-1 is flat in I-1 or I+1, and F-M is flat as well. Since f=2y and g=1 near y=0, the jet of Psi at these endpoints is the jet of 2xy. Therefore every jet of Omega=-Delta Psi vanishes, and every positive-order jet of Theta vanishes there. Z is a compact interval with flat endpoints, not a closed curve.

## 3. Uniform decay and the full-plane inverse

The decay statements can be checked on two overlapping exterior regions.

For |y|>=2 and |I| bounded, f=2m2/y and g=m1/|y|, so Psi=2m2 (x/y) chi(m1 x/|y|) is a smooth angular function on a cone separated from y=0. Its first derivatives are O(r^(-1)) and its second derivatives O(r^(-2)).

For |I|>=2 use chi=Cchi/I^2 to write

    Psi=A(y)/x, A(y)=Cchi f(y) h(y)^2/m1^2.

On |y|<=2 the smooth functions A,A',A'' are bounded, giving U=O(1/|x|) and Omega=O(1/|x|). On |y|>=2, A(y) is a constant multiple of y, so U=O(r^(-1)) and Omega=O(r^(-2)) when |I|>=2. These cases cover every sufficiently large radius. Hence U=O(r^(-1)) and Omega=O(r^(-1)) uniformly; the slower Omega bound occurs only in a fixed horizontal strip.

The ordinary Biot-Savart integral is absolutely convergent at infinity. In that strip, |K(X-Y) Omega(Y)|=O(|Y1|^(-2)) for fixed X; off the strip Omega=O(r^(-2)) and the kernel contributes O(r^(-1)). Local kernel singularities are integrable against smooth Omega. Its difference from U is harmonic and sublinear, hence constant. Both decay to zero at infinity: for the integral this follows by splitting a fixed compact set, a near-X ball, and the remaining tail using the displayed strip and exterior bounds. Alternatively its relative version equals U-U(0) by research/03, and the ordinary integral at0 is zero by the additional y oddness of Omega. Since U(0)=0, it equals U everywhere. This construction adds no free strain to the inverse.

## 4. What this example does and does not disprove

It disproves an inference of smooth beta=2 nonexistence using only the temperature equation, the div-curl representation, decay, and the mere existence of flat jets at compact-zero-set endpoints. The vorticity equation fails already at the center: Omega_x(0)=0 instead of2a0. This is intentional and explicit. It does not refute the full B2 question, the center identities derived from both equations, or the circulation obstruction that uses the missing equation.

Dependencies: smooth cutoffs, elementary differentiation and ODE algebra, and the canonical inverse uniqueness in research/03. No numerical evidence is used as proof.
