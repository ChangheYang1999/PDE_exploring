# Nonzero formal velocity tails with zero Bernoulli coefficient

## Exact statement

For every 2/5<c<1/2 and finite omega, let k=(1-c)/c, a=1-2c, A=cI-omega J, and b=omega/c. There is a nonzero smooth vector field V on R3 minus {0}, with W=curl V smooth there, such that

    div V=0,
    (1-c)V+(Ay.grad)V+omega JV=0,
    (Ay).V=0,
    a V=Ay cross W,
    V.W=0.

V and W extend as locally integrable distributions on all R3, where div V=div W=0 and curl V=W. They have the exact velocity and vorticity homogeneities of A210. V is the Biot-Savart reconstruction of W. Thus these leading-field constraints, including zero scalar coefficient (Ay).V, do not force the tail to vanish.

This is a formal linear-tail example, singular at zero. It is not claimed to solve the full nonlinear Euler profile equation, and is not an example in the decaying smooth class of the prompt.

## Construction

Use spherical coordinates (r,theta,phi), with theta the polar angle, and their orthonormal basis (e_r,e_theta,e_phi). Write s=sin(theta), z=cos(theta), and m=2-k. Define on S2

    F_r=b s^2 z,
    F_theta=-(m b/4)s^3,
    F_phi=s z,

and V(rw)=r^-k F(w). These components define a smooth Cartesian vector field at the poles. Indeed, for w=(w1,w2,w3), with z=w3 and s^2=w1^2+w2^2,

    F(w)=b s^2 z w
         -(m b/4)s^2(z w1,z w2,-s^2)
         +z Jw.

This expression is polynomial in w. It also shows rotation covariance F(exp(tJ)w)=exp(tJ)F(w). The azimuthal component is nonzero at theta=pi/4, so V is not zero, including when omega=0.

## Divergence, transport and scalar coefficient

For a degree-minus-k field with axisymmetric spherical components,

    div V=r^(-k-1)[(2-k)F_r+(1/s)partial_theta(s F_theta)].

The phi derivative vanishes. Direct differentiation gives

    (1/s)partial_theta(s F_theta)
       =-(m b/4)(1/s)partial_theta(s^4)
       =-m b s^2 z=-(2-k)F_r.

Hence div V=0 pointwise off zero. Homogeneity gives (y.grad)V=-k V, while rotational covariance gives (Jy.grad)V=JV. Therefore the linear profile operator is

    [(1-c)-ck]V-omega JV+omega JV=0.

On each radius sphere,

    (Ay).V=r^(1-k)[c F_r-omega s F_phi]
          =r^(1-k)[c b s^2 z-omega s^2 z]=0.

The standard linear Lamb identity now gives aV=Ay cross W-grad[(Ay).V]=Ay cross W. Dotting with W yields V.W=0. This step does not impose the omitted nonlinear convective term.

## Distributional extension and Biot-Savart

Since 1<k<3/2, V=O(r^-k) and W=O(r^(-k-1)) are locally integrable at zero. When integrating by parts on the complement of a radius-epsilon ball, the boundary terms for div V and curl V are bounded by C epsilon^(2-k), which tends to zero. Thus div V=0 and curl V=W globally in distributions. Distributional div curl gives div W=0. In particular no hidden point source or curl defect has been introduced.

Curling the linear equation, or differentiating its exact rotation-dilation covariance, gives

    W(exp(tA)y)=exp(-t)exp(-omega tJ)W(y).

The velocity covariance has factor exp(-(1-c)t). The Biot-Savart integral of W is absolutely convergent off zero: W is locally bounded there, integrable near zero, and its degree k+1 lies strictly between 1 and 3. The same global div-curl argument as A210 shows curl(TW)=W and div(TW)=0. Both TW and V lie in finite-exponent sum spaces on R3. Their difference is an entire distributionally harmonic field in those spaces, hence zero. Equivalently its Fourier transform is supported at zero, so it is a polynomial, and no nonzero polynomial lies in the indicated finite-exponent sum spaces. Therefore V=TW.

The nontriviality of W also follows: if W=0, the linear Lamb relation with a>0 would force V=0, contradicting the displayed azimuthal component.

## What this does and does not rule out

The construction refutes only the algebraic implication that a nonzero admissible linear tail must have a nonzero scalar (Ay).V. It satisfies the actual curl relation and every leading relation explicitly listed above. It does not verify the full nonlinear equation, a smooth core, an energy remainder identity, a periodic-orbit condition on a regular attractor, or realizability as the tail of any global profile. A future use of K=0 to prove U=0 would have to use additional information from that full problem. No numerical calculation was needed.
