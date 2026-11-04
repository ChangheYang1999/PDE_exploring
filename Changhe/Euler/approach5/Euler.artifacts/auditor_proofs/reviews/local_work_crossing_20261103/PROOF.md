# A complete local carrier flow with a work-sign crossing

## 1. Exact statement and scope

Fix 0<c<1/2 and finite real omega. Put a=1-2c, beta=a/(2c), m=omega+sqrt(omega²+c²)>0, so m²-2omega m=c². Cylindrical coordinates (r,theta,z) have r=sqrt(x1²+x2²), and Jx=e3 cross x. On the open domain D={r>1} define

    f=-c/r, v=m r^(-1)(r²-1)^(-beta),
    U=f e_r+v e_theta,
    P(r)=integral_(sqrt(2))^r [ac/s+c²/s³+v(s)²/s] ds.

Let A=cI-omega J, B=Ax+U, D0(r)=cr+f=c(r²-1)/r, H=P+|U|²/2+(Ax).U, Q=P-|U|²/2 and g=U.B=H-Q. All these fields are smooth on D. They solve the full rotating similarity equation

    (1-c)U+(B.grad)U+omega JU+grad P=0, div U=0.

Their helicity is zero and their vorticity is nonzero everywhere. The B flow is complete in both directions on D. Along the orbit through (sqrt(2),0,0), g changes from positive to negative through a regular critical surface of H. All claims concern this open cylindrical domain. The field is singular at its boundary and does not decay uniformly in the ambient space.

The complete current source is Theory Agent C C53, revised at 2026-11-03T15:52:56Z. Its hand derivation and revised scope are independently checked below; the source's finite symbolic samples and nested model statements are not used as proof.

## 2. Full equation and vorticity

Since rf=-c, div U=(rf)'/r=0. The radial vector f e_r is a gradient. Thus

    curl U=(v'+v/r)e_z=w e_z,
    v'/v=-1/r-(a/c)r/(r²-1),
    w=-(a/c)rv/(r²-1)=-a v/D0
      =-(am/c)(r²-1)^(-beta-1).

It is nonzero and perpendicular to U. The carrier is

    B=D0 e_r+(v-omega r)e_theta+cz e_z.

Cylindrical differentiation, including the derivatives of the basis vectors, gives

    (B.grad)U=D0 f' e_r+D0 v' e_theta
                  +((v-omega r)/r)(f e_theta-v e_r).

After adding (1-c)U+omega JU, the omega terms cancel. The radial component is

    (1-c)f+D0 f'-v²/r=-ac/r-c²/r³-v²/r=-P'(r).

The angular component is (1-c+f/r)v+D0 v', which vanishes by the displayed logarithmic derivative of v. The axial component is zero. This proves the full equation, not just the pressure Poisson equation or a tail identity.

## 3. Complete characteristics, rank and critical crossing

The carrier equations integrate to

    r(t)²-1=(r(0)²-1)exp(2ct),
    z(t)=z(0)exp(ct),
    theta(t)=theta(0)+integral_0^t[v(r(s))/r(s)-omega] ds.

On every finite time interval r stays strictly above1 and finite. The angular integral is finite on that interval. Thus these formulae define the flow for every real t, keep it in D, and give the inverse by time reversal. Every forward orbit escapes because r(t) tends to infinity. The angular speed can diverge as t tends to minus infinity, which does not prevent completeness at finite times.

The Cauchy vorticity law can also be verified directly. The flow sends e_z to exp(ct)e_z under its differential, while the explicit w satisfies w(r(t))=exp(-t)w(r(0)). Consequently

    curl U(Phi_t x)=exp(-(1+c)t)D Phi_t(x)curl U(x).

Both H and Q are radial, so their gradients are everywhere linearly dependent. The exact Bernoulli identity is

    grad H=-aU+B cross curl U, B.H=-ag.

The angular component in the first identity is -av-D0 w=0; its radial component gives H'=-ag/D0. Directly,

    g=-c²+c²/r²+v²-omega r v.

At R=sqrt(2), v=m/sqrt(2), and m²-2omega m=c² yields g(R)=0. Differentiating gives

    g'(R)=-(1-c)(c²+m²)/(sqrt(2)c)<0,
    B.g at R=-(1-c)(c²+m²)/2.

For example v'(R)=-(m/2)(1+2a/c), and the two identities m²-omega m=(m²+c²)/2 and c²+omega m=(m²+c²)/2 give the displayed derivative. On the orbit through (R,0,0), r(t)²-1=exp(2ct), so r crosses R increasingly at time0. Hence g(Phi_t x)>0 for all sufficiently small negative t and is negative for all sufficiently small positive t. The orbit remains vortical throughout.

Finally H'(R)=0 and

    H''(R)=-a g'(R)/D0(R)
           =a(1-c)(c²+m²)/c²>0.

Near this orbit point, g is a smooth radial coordinate. Thus H=F(g), with

    F'(0)=0, F''(0)=2a/[(1-c)(c²+m²)],
    F''(0) B.g=-a.

The local critical set of H is precisely the cylinder r=R, a surface of local minima. This realizes the geometry described in A1539 rather than merely an algebraic jet of that geometry.

## 4. What this exact example does and does not establish

The local equation, divergence constraint, helicity condition, rank identity, Bernoulli identities and Cauchy law do not forbid a positive-to-negative work crossing. The example establishes only that precise nonimplication. It does not prove that the regular-H premise of Theory Agent C C52 is logically necessary within its full global class or cannot be replaced by another local condition. A small ball around the crossing has neither the required forward-invariant neighborhood nor the terminal framework of that theorem.

As r decreases to1, v diverges because beta>0. At any fixed r>1, U is a nonzero vector independent of z, so there is no uniform decay as |x| tends to infinity. On z=0, |U|>=c/r, whereas the natural tail exponent is p=(1-c)/c>1. Also v=O(r^(-p)), whence

    P=ac log r+O(1), g tends to -c²,
    H=ac log r+O(1), Q=ac log r+O(1).

No additive pressure constant repairs the terminal H,Q decay. The model satisfies forward escape, but fails the spatial and pressure hypotheses used in the global argument. It is neither a global smooth profile nor a counterexample to the campaign conjecture. No numerical calculation or formal build was needed.
