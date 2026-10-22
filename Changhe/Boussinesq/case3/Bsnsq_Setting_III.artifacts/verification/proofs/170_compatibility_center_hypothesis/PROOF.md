# A center hypothesis in the compatibility converse

Written 2026-10-21, shift6, before the new exact controls. This extends the local argument of packet139 and independently checks the counterexample proposed in the lead's referee12 review. It is a local statement about the two transport equations, not a B2 existence or nonexistence result.

## 1. Statement

Fix beta>2 and k=beta-2. Let Psi be smooth near the origin and odd in x. Define

    U=(-Psi_y,Psi_x), Omega=-Delta Psi,
    W=beta(x,y)+U-U(0), F=W.grad Omega+Omega,
    J=partial_x W_2,
    D=(k-partial_x W_1)F-W.grad F,
    Z=W_1 F J+W_2 D,
    E=J partial_y Z-Z partial_y J-k D J,
    Theta(x,y)=integral_0^x F(s,y) ds,
    t=W.grad Theta-k Theta.

Assume Psi_xxx(0) is nonzero and put c=Psi_xy(0).

(a) If c>-2, then E=0 on a neighborhood of the origin if and only if the two equations

    W.grad Theta=k Theta,  W.grad Omega+Omega=Theta_x

hold on a possibly smaller neighborhood. This sufficient hypothesis includes the B2 normalization c=1+beta/2. No global inverse or tail assertion is included.

(b) The inequality cannot be extended uniformly to c=-2. For any q nonzero, the polynomial

    Psi=-2xy-q x^3/6

is smooth and odd in x, has Psi_xxx(0)=-q nonzero, and satisfies E=0 identically, while the normalized primitive Theta has a nonzero thermal residual. Thus the unqualified local converse, with no condition on the center strain, is false. This counterexample has quadratic velocity growth and the wrong B2 center strain, and is not in the profile class.

## 2. The compatibility identity

All functions below are defined on a sufficiently small rectangle. By parity, F is odd in x, Theta is even in x and vanishes at x=0, and t is even in x and divisible by x^2. Direct differentiation of t gives

    t_x = J Theta_y - D,
    k J Theta = Z-Jt+W_2 t_x.

Differentiate the second identity in y, multiply by J, and use the first identity to eliminate J Theta_y. After canceling equal terms one obtains

    E = J^2 t_y - J W_2 t_xy
        +[W_2 J_y+J(k-W_{2,y})]t_x.                 (1)

This calculation uses no division. It also proves necessity when t=0. The vorticity equation already holds by the definition of Theta.

For the converse, J=xj with j smooth and j(0)=Psi_xxx(0) nonzero. Shrink the rectangle so j never vanishes. Since t_x is divisible by x, the quotient

    mu=t_x/J

extends smoothly through x=0. Set nu=t-W_2 mu. Then

    nu_x=-W_2 mu_x,
    E=J^2(nu_y+k mu).                              (2)

If E=0, the second equality gives nu_y=-k mu off x=0 and also on that line by continuity. Equality of mixed derivatives now gives, at every point,

    W_2 (mu_x)_y+(W_{2,y}-k)mu_x=0.                (3)

## 3. The bounded-solution argument

Let v be smooth near a point y0 with v(y0)=0 and delta=v'(y0)>k>0. A solution of

    v f'+(v'-k)f=0

on either punctured side is either zero or a nonzero constant times

    |y-y0|^(k/delta-1) exp(g(y)),

where g stays bounded near y0. Indeed, v(y)=delta(y-y0)+O((y-y0)^2), so (k-v')/v=(k/delta-1)/(y-y0)+O(1), and integration gives the formula. The power k/delta-1 is negative. A bounded solution must therefore vanish on both sides and at the point; ordinary uniqueness extends that vanishing along the connected interval on each side.

In our setting W_2(0,0)=0 and W_{2,y}(0,0)=beta+c>beta-2=k. First choose a sufficiently small positive height h and horizontal width a0 so that W_{2,y}>k and j is nonzero on the closed rectangle. At x=0 the endpoint values W_2(0,-h) and W_2(0,h) have opposite strict signs. By continuity, shrink the horizontal width to a>0 so the same signs hold at both horizontal edges for every |x|<=a. Strict monotonicity in y then gives exactly one zero of W_2(x,.) in each vertical segment. Apply the preceding bounded-solution argument to (3), with x fixed. Smoothness makes mu_x bounded, so mu_x=0. Thus mu=mu0(y).

Writing b(y)=W_2(0,y), integrate t_x=J mu0 and use t(0,y)=0 to get

    t=(W_2-b)mu0,   nu=-b mu0.

The equality nu_y=-k mu0 becomes

    b mu0'+(b'-k)mu0=0.

Here b(0)=0 and b'(0)=beta+c>k. The same bounded-solution argument gives mu0=0. Hence t=0 and both transports hold. This proves (a).

## 4. Exact polynomial family and the counterexample

For the larger family Psi=cxy-q x^3/6, direct differentiation gives

    Omega=qx,
    W_1=(beta-c)x, W_2=(beta+c)y-qx^2/2,
    F=q(beta-c+1)x,
    Theta=q(beta-c+1)x^2/2,
    t=q(beta-c+1)(beta+2-2c)x^2/2,
    E=q^2(c+2)(beta-c+1)(beta+2-2c)x^2.             (4)

To check the last equality without expanding Z, note that J=-qx, J_y=0, t_y=t_xy=0 and W_{2,y}=beta+c. Substitution in (1) leaves J(-c-2)t_x, exactly the displayed formula. At c=-2 one has E=0 but

    Theta=q(beta+3)x^2/2,
    t=q(beta+3)(beta+6)x^2/2,

which is nonzero for q nonzero and beta>2. Also c=-2 violates c=1+beta/2, and U_2=-2y-qx^2/2 is not sublinear. These exclusions prevent any interpretation as a B2 counterexample or profile. The conclusion is only that a stated strain or equivalent spectral hypothesis cannot simply be dropped from the local converse.

## 5. Dependencies and scope

The proof uses elementary differentiation, parity division by x, the intermediate value theorem and strict monotonicity at a simple vertical zero, and a scalar ordinary differential equation. Packet139 contains the same two-ODE mechanism at the normalized B2 strain. This proof states a sufficient open strain range explicitly and checks the excluded boundary. It does not claim that c>-2 is necessary for every individual stream, or that a local solution extends to the plane. The origin of the boundary example is the lead's referee12 note; all formulas above were recomputed independently. Exact controls and review records belong in verification/. No Lean or Lake build is authorized.

Verified UTC 2026-10-21T13:28:11.352424+00:00. The first draft had a minus sign in the second intermediate identity of section2; actual Opus5.5 review281 found it. Direct algebra and exact mixed-polynomial controls confirm the corrected plus sign. The final compatibility identity and conclusions are unchanged. Follow-up282 reviewed the corrected proof with no remaining mathematical error found.
