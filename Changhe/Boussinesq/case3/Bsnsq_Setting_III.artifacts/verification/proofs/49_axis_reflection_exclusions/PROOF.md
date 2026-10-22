# Independent audit of axis reflection exclusions

Date:2026-10-20. Status: CONFIRMED by independent derivation, exact symbolic checks and
checked actual Opus38 review.
These exclude additional shape subclasses of G, not G itself and not the
full B2 target. They audit lead astra/gsrc1 Sections2.1-2.3.

## Exact setting and statements

Let beta>2 and let a smooth full-plane B2 profile satisfy

    W=beta X+V, V(0)=0, div V=0, Omega=-curl V,
    W.grad Theta=(beta-2)Theta, W.grad Omega+Omega=Theta_x,
    Theta even in x, Omega odd in x, Theta(0,y)=0,
    Theta=x^2+O(r^3), Omega_x(0)=4/beta,
    DV(0)=diag(-c,c), c=1+beta/2.

Assume V is the canonical relative full-plane inverse with V=o(r), and
Omega=O(r^{-nu}), nu=1/beta. Suppose0 is the only zero of W. This is
G with the permitted a0=1 normalization. Write the smooth axis fields

    A(y)=Theta_xx(0,y)/2, q(y)=Omega_x(0,y), b(y)=W2(0,y),
    Lambda=3beta+2, M=2beta+1.

Then:

1. If at a horizontal reflection height h,

       b'(h)=beta, b'''(h)=0, q'(h)=q'''(h)=0,

   necessarily b(h)!=0 and

       b(h)b''(h)=(beta+1)(beta+2)(5beta+3)/(beta-1),      (1)
       b(h)^2 q''(h)=4(beta+1)^2(beta+2)q(h)/(beta-1)>0. (2)

2. No such profile has Omega=x g(x^2+(y-h)^2) for a smooth function g
   on[0,infinity) and any h. No positivity of g is assumed separately.

3. If Omega(s,h+eta)=Omega(s,h-eta) for every s>0 and eta, then(2)
   holds. In particular q has a strict local minimum at h. This
   excludes any such reflection whose axis quotient has a local maximum
   or nonpositive second derivative at the reflection height. Under this
   same reflection hypothesis it also excludes a common horizontal
   maximum of Omega(s,.) for every s>0 at that height.

No assertion is made that a true profile must possess these reflections
or a shifted radial quotient. Arbitrary sign-changing vorticity away
from the axis is allowed in the third statement.

## 1. Axis equations and signs

The velocity parity also follows directly from the inverse convention.
The reflected field Vtilde(x,y)=(-V1(-x,y),V2(-x,y)) is smooth, sublinear,
divergence free, zero at0, and has the same negative curl Omega. Its
difference from V is an entire sublinear harmonic field vanishing at0,
hence zero. Thus V1 is odd and V2 is even in x.

Parity and divergence give W1=x alpha(y)+O(x^3), alpha=2beta-b'.
Divide the temperature equation by x^2 and take x to0. Divide the
vorticity equation by x and do the same. Smoothness gives exactly

    b A'=(2b'-Lambda)A,
    b q'+(M-b')q=2A.                               (3)

At0, b=0, b'=mu=1+3beta/2, A=1 and q=4/beta. The assumption on zeros
of W and axis invariance imply b(y)>0 for y>0 and b(y)<0 for y<0.
The first scalar linear equation propagates A>0 on both half axes.
The second has a positive integrating factor and a positive forcing
2A/b on the positive half axis, so q stays positive there. For the
negative half axis set s=-y, B(s)=-b(-s), Q(s)=q(-s); the same two
ODEs hold with B>0 and the same positive data near0. Thus A,q>0 on
the entire axis. These facts require no global coordinate theorem.

## 2. Independent derivative elimination

Put B=b(h), J=b''(h), Q=q(h)>0, R=q''(h). At the stipulated derivative
values, the second equation in(3), its first derivative and its second
derivative respectively give

    2A=(beta+1)Q,
    2A'=BR-JQ,
    2A''=(3beta+1)R.                                (4)

For clarity, before evaluating the last derivative the exact equation is
b q'''+(M+b')q''-b''q'-b'''q=2A''.
The first equation in(3) and its first derivative give

    BA'=-(beta+2)A,
    BA''=-(2beta+2)A'+2JA.                          (5)

The first line of(4) is nonzero. Hence(5) already implies B!=0.
Substituting(4) into(5) yields

    B^2 R-BJQ=-(beta+2)(beta+1)Q,
    (5beta+3)BR=4(beta+1)JQ.                        (6)

Multiply the second identity by B and substitute the first. The
coefficient 4(beta+1)-(5beta+3) is1-beta. Solving gives(1), and then
(2). All divisions are legitimate: beta>2, Q>0 and B!=0. This proves
the first assertion without any inverse formula.

## 3. The inverse of a shifted radial quotient

Suppose Omega=x g(S), S=x^2+(y-h)^2. The axis positivity just proved
implies g(S)>0 for every S>=0. Set F(0)=0 and

    F'(S)=1/(4S^2) int_0^S t g(t)dt
         =(1/4) int_0^1 u g(Su)du.                 (7)

This gives a smooth function at S=0, with F'(0)=g(0)/8>0, and
4(2F'+S F'')=g. Use the stream with the sign required by the prompt,

    Psi=-xF(S)+F(h^2)x.

Direct differentiation gives -Delta Psi=xg(S)=Omega and

    V1=2x(y-h)F'(S),
    V2=F(h^2)-F(S)-2x^2F'(S).                     (8)

The velocity is divergence free and V(0)=0. We must check it is the
canonical inverse; a local stream alone would not suffice.

The source bound at X=(sqrt(S),h) gives
|g(S)|<=C S^{-(1+nu)/2} for large S. Let a=(1+nu)/2<1. Splitting
(7) at t=1 gives F'(S)=O((1+S)^{-a}), and integration gives
F(S)=O((1+S)^{1-a}). Thus both components of(8) are O(r^{1-nu})
plus constants. The actual canonical velocity and(8) have the same
div-curl, are smooth and sublinear, and vanish at0. Their difference
is an entire harmonic vector field. The interior harmonic gradient
estimate on arbitrarily large disks makes that difference constant;
its value at0 is zero. Therefore(8) is the actual relative velocity.

The center strain in the prompt is
c=Psi_xy(0)=2h F'(h^2). Since c>0 and F'>0, h>0, so b(h)>0. On the
axis,

    b(y)=beta y+F(h^2)-F((y-h)^2),
    q(y)=g((y-h)^2).

Consequently b'(h)=beta, b'''(h)=q'(h)=q'''(h)=0, while
b''(h)=-2F'(0)<0. This contradicts(1), proving the second assertion.

## 4. Reflection of the entire source implies reflection of axis velocity

Use the canonical kernel K(Z)=(Z2,-Z1)/(2pi|Z|^2). Pair source points
(s,h+eta) and(-s,h+eta), using odd vorticity in x. The velocity difference
between two axis target points is the absolutely convergent integral

    V2(0,h+z)-V2(0,h)
      =int_0^infinity [L_s(z)-L_s(0)]ds,             (9)

    L_s(z)=(1/pi) int_R s Omega(s,h+eta)
                           /[s^2+(z-eta)^2] d eta.

For each s>0 this one-dimensional integral converges absolutely.
At infinity the difference of the original kernels is O_z(|Y|^{-2}),
so the paired two-dimensional integral is absolutely integrable against
Omega=O(|Y|^{-nu}). Near either target, smooth oddness gives
|Omega(s,h+eta)|<=C s locally. Hence each local kernel term is bounded
in absolute value by C s^2/[s^2+(eta-z)^2]<=C, and is integrable.
This proves(9) including its subtraction and all needed Fubini steps.

If the source is even in eta, the change of variable eta->-eta proves
L_s(-z)=L_s(z). Therefore V2(0,h+z)-V2(0,h) is even in z. Smoothness of
V gives b'(h)=beta and b'''(h)=0. Differentiating source symmetry at
s=0 gives q'(h)=q'''(h)=0. Equation(2) follows from Section2. It says
q''(h)>0, whereas a local maximum would give q''(h)<=0.

If every Omega(s,.) has a maximum at h, then for s>0,
Omega(s,h+eta)/s<=Omega(s,h)/s. Let s decrease to0. Smoothness gives
q(h+eta)<=q(h), again contradicting q''(h)>0. The argument neither
assumes nor concludes a global sign for Omega off the axis.

## Dependencies and scope

All axis arguments use only the exact B2 equations, parity, smoothness,
and the unique-zero assumption. The inverse steps use the supplied
class-A source decay and the canonical relative inverse. Harmonic
Liouville uniqueness follows from an elementary interior estimate.
The global-source coordinate construction48 is not needed for these
restricted exclusions. The symbolic check in verification/ supports
only the explicit finite algebra; it is not a proof of the PDE theorem.

## Review record

Actual Opus38 (claude-opus-5-5,219.372655seconds,completed17:34:50Z)
confirmed every theorem, including the exact kernel signs. The verifier
checked its algebra and adopted an explicit velocity-parity argument
and a wording fix keeping the reflection hypothesis in the common-peak
corollary. Own symbolic algebra completed0.344782seconds and produced
exact zeros for both elimination identities and the shifted radial curl.
The reviewer also checked packet50, separately recorded there.
