# The scalar transverse-zero kernel is not realized by its cubic-x stream family

Status: independently derived informal proof, 2026-10-21. Own21 exact checks and four polynomial controls passed. Actual claude-opus-5-5 review203 confirms the algebra and contradiction; its requested compatibility dependencies are derived explicitly below. This is a local exclusion for one prescribed stream form at beta=2. It does not settle general compatibility sufficiency or either global B2 branch.

## Exact statement

Let b be smooth on an interval around0, with b(0)=0, b'(0)=4 and b''(0)=-q, q nonzero. Let d be a nonzero real constant. Define the odd-in-x stream on a rectangle around0 by

    Psi(x,y)=x[b(y)-2y]+(d/6)x^3 y.

Use the prompt's beta=2 relative transport field, whose center velocity is zero for this expression:

    W=(2x-Psi_y,2y+Psi_x), Omega=-Delta Psi,
    F=W.grad Omega+Omega, T(x,y)=integral_0^x F(s,y) ds,
    t=W.grad T, J=partial_x W2.

The center strain is Psi_xy(0)=2, the vorticity slope is q, and T=q x^2/2+terms of degree at least3. Thus a0=q/2 is nonzero and both required center relations hold. Define the compatibility expression, equivalently by packet137,

    E=J^2 t_y-J W2 t_xy+(W2 J_y-J partial_y W2)t_x.       (1)

Then E cannot vanish identically on any neighborhood of0. In particular no smooth temperature can solve both B2 transport equations near0 for this prescribed stream while obeying the axis normalization. In fact the necessary compatibility equation is independent of the temperature, so its failure also excludes any C2 temperature solving both equations near0, with or without the axis normalization, by packet124. No full-plane inverse or tail is assumed or proved for this local statement.

## Why the compatibility expression is necessary

Here is a self-contained derivation of the packet124/137 identity at k=0. For any prescribed smooth W and Omega define F as above and

    D=-(partial_x W1)F-W.grad F,
    Z=W1 F J+W2 D,
    E0=J partial_y Z-Z partial_y J.

If a C2 function Theta solves Theta_x=F and W.gradTheta=0, differentiating the latter equation in x gives D=J Theta_y. Thus Z=J(W.gradTheta)=0, so E0=0. No axis normalization or division is used. For the normalized primitive T_x=F and t=W.grad T, differentiating t in x instead gives D=J T_y-t_x, hence Z=Jt-W2 t_x. Substituting this last formula into E0 and canceling the two J J_y t terms yields exactly(1). This proves both the identity and the necessity used here for any prescribed smooth stream, without assuming beta>2. The temperature derivatives used in the necessity calculation have order at most2.

## Stream and primitive calculation

Put Q=-b''-d y and use a prime for differentiation in y. Direct differentiation gives

    W1=(4-b')x-d x^3/6, W2=b+d x^2 y/2,
    Omega=x Q, J=dxy.

Set

    A=(5-b')Q+b Q', C=d(-Q/6+y Q'/2).

Then F=xA+x^3 C and its exact normalized primitive is

    T=x^2 A/2+x^4 C/4.

Its thermal residual is a polynomial in x with smooth coefficients:

    t=x^2 t1+x^4 t2+x^6 t3,
    t1=(4-b')A+b A'/2,
    t2=(4-b')C-d A/6+b C'/4+d y A'/4,
    t3=-d C/6+d y C'/8.                              (2)

At y=0 these have the fixed values

    t1(0)=0, t2(0)=-d q/6, t3(0)=d^2 q/36.           (3)

These values use b(0)=0, b'(0)=4 and Q(0)=q only; no higher derivative of b is prescribed.

## Compatibility contradiction

Suppose E=0 near0. Substituting J=dxy and W2=b+d x^2 y/2 into(1) gives

    E/d=x(b-yb')t_x-xyb t_xy
          +d x^2 y^2 t_y-(d/2)x^3 y^2 t_xy.          (4)

Since d is nonzero and t is a polynomial in x, every x coefficient in(4) vanishes. With t0=t4=0, its coefficient of x^(2n), n=1,2,3,4, is

    -2n y b t_n'+2n(b-yb')t_n
          +d(2-n)y^2 t_(n-1)'=0.                   (5)

The n=2 equation is

    -y b t2'+(b-yb')t2=0.

On a sufficiently small punctured half interval, b/y is smooth and nonzero, and the general solution is t2=C_* y/b. Continuity at0 fixes the same constant on both sides: from(3), C_*=4t2(0)=-2d q/3. Since

    b=4y-qy^2/2+O(y^3),
    y/b=1/4+q y/32+O(y^2),

we obtain

    t2'(0)=-d q^2/48.                               (6)

The n=3 equation is

    -6 y b t3'+6(b-yb')t3-d y^2 t2'=0.              (7)

The n=4 equation is -2d y^2 t3'=0, so t3'=0 throughout the punctured interval and at0 by continuity. Divide(7) by y^2 off0 and pass to0. Since (b-yb')/y^2 tends to q/2, (3) and(6) force

    0=3q t3(0)-d t2'(0)
      =d^2 q^2/12+d^2 q^2/48
      =5d^2 q^2/48>0.

This contradiction proves the statement. All divisions occur on a punctured interval where their denominators are explicitly nonzero, followed by smooth limits.

## Dependencies and scope

The displayed stream and polynomial calculation are local and elementary. The identification(1) and its necessity are the packet124/137 identities specialized to k=0, derived self-containedly above. The informal proof above precedes its symbolic controls.

This family has J=dxy, so it lies outside the uniform-order hypothesis of packet139. That packet's freely prescribed scalar kernel does solve M t=0 for suitable V of this form, but (2)-(3) show why it cannot be the actual primitive residual here. A general Psi with additional powers of x, a variable coefficient replacing d y, or a smooth flat J is not covered. No global profile or class-wide nonexistence result follows.
