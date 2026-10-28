# Exact radial-power seminorm and a stronger complex lower bound

## Statements and notation

Let H be a nonzero real Hilbert space and 0<alpha<1. Define

    R_alpha(x)=||x||^(alpha-1)x for x!=0, and R_alpha(0)=0.

Use the Euclidean Holder seminorm

    [F]_alpha=sup_(x!=y) ||F(x)-F(y)||/||x-y||^alpha.

Then the exact identity is

    [R_alpha]_alpha=2^(1-alpha).                         (1)

In particular (1) holds on C identified with R^2. Let S=T_xx+iT_xy
have circular principal-value kernel 1/(2pi conjugate(z)^2), defined
by convergent increments modulo complex constants on the homogeneous
complex Holder space. Write M_alpha for its norm using the complex
modulus seminorm. With the conventions of ../PROOF.md, the conventional
complex-input Beurling norm is 2M_alpha. Then

    M_alpha >= (alpha+3)/[2(1-alpha)3^alpha].             (2)

This is a finite-exponent lower bound. No exact finite-exponent norm
of S, of the Beurling transform, or of the cubic input below is claimed.
The same lower bound holds for the supremum over compact smooth inputs.

## Proof of the exact radial-power identity

Fix x,y and put r=||x||, s=||y||. If either radius is zero, the quotient
is one and the asserted upper bound follows. Suppose r,s>0. Let

    u=||x-y||^2, a=(r-s)^2, b=(r+s)^2.

Then a<=u<=b. The Hilbert-space inner-product identity gives

    ||R_alpha(x)-R_alpha(y)||^2
       =r^(2alpha)+s^(2alpha)
          -(rs)^(alpha-1)(r^2+s^2-u)=:L(u).

Thus L is affine in u. The function

    Q(u)=2^(2-2alpha)u^alpha

is concave on [a,b], including when a=0. At the left endpoint,

    L(a)=(r^alpha-s^alpha)^2 <= |r-s|^(2alpha) <= Q(a).

Here the first inequality is the elementary subadditivity consequence
|(s+t)^alpha-s^alpha|<=t^alpha for s,t>=0. It follows, for instance,
by differentiating (s+t)^alpha-s^alpha with respect to s for s>0 and
then taking the limit at zero. At the right endpoint, concavity of the
power function gives

    L(b)=(r^alpha+s^alpha)^2
         <=[2((r+s)/2)^alpha]^2=Q(b).

For every u between a and b, the chord joining (a,Q(a)) and (b,Q(b))
lies above the affine function L and below the concave graph Q.
Consequently L(u)<=Q(u). Taking square roots proves the upper bound
in (1). For any nonzero x choose y=-x. The quotient equals
2||x||^alpha/(2||x||)^alpha=2^(1-alpha). This proves equality.

## Application to the cubic angular input

Define g(0)=0 and g(z)=|z|exp(-3i arg z) otherwise. Its differential
in orthonormal radial and tangential frames has singular values 1 and
3. Thus it is globally 3-Lipschitz by integrating along a segment;
if the segment meets zero, split there and use continuity. Hence

    f_alpha(z)=R_alpha(g(z))=|z|^alpha exp(-3i arg z)

has seminorm at most 2^(1-alpha)3^alpha by (1).

The complete potential calculation in ../large_alpha/PROOF.md gives

    S f_alpha(z) = c_alpha |z|^alpha exp(-i arg z)
                     modulo a complex constant,
    c_alpha=(alpha+3)/[2(1-alpha)].

For clarity, that calculation solves -Delta U=f_alpha with
U=-r^(alpha+2)exp(-3i theta)/[(alpha+2)^2-9] and applies
(1/2)(partial_x+i partial_y)^2. The cancellation of the alpha+5 factor
gives c_alpha. Both expressions are globally alpha-Holder; their
harmonic difference has sublinear growth and is constant. This also
justifies the formula at zero and for the prescribed increment
normalization at infinity, as detailed in the cited proof.

Complex conjugation is an isometry, so (1) gives the exact output
seminorm c_alpha 2^(1-alpha). Dividing by the established input
seminorm upper bound 2^(1-alpha)3^alpha proves (2). Equivalently,
one can use the output increment between 1 and -1. Both factors
2^(1-alpha) must be retained until they cancel. Using only the
increment between 1 and zero would lose this factor unnecessarily.

The compact smooth approximation theorem in ../PROOF.md approximates
any fixed input increment and its transform increment with arbitrarily
small seminorm loss. Applied to the pair 1,-1 and f_alpha, it transfers
the lower bound to the original compact smooth test-function supremum.

## Dependencies and scope

Identity (1) is an elementary standalone proof on any real Hilbert
space. Bound (2) additionally uses the already established homogeneous
kernel definition, the cubic potential calculation and the complex
compact smooth approximation. It strengthens the finite-alpha lower
bound in ../large_alpha/PROOF.md; it leaves both endpoint limits in
that proof unchanged. No numerical or external literature assertion
is used.
