# Interior affine limits, lost tails and stationary shear rigidity

Date: 2026-10-20. Status: independent audit of lead near1 P2, P3 and P5. The statements below constrain possible limits and provide explicit non-profile tests. They do not classify every endpoint limit or exclude the primary class.

## 1. Gradient distance and a conditional exact-profile gap

Let rho be globally C¹ and strictly sublinear, |rho(X)|<=C(1+|X|)^gamma with gamma<1. For every nonzero constant a,

    sup_X |grad rho(X)-a e_y|>=|a|.                       (1)

Indeed, a strict smaller upper bound would force rho_y to have the sign of a and magnitude bounded below on the entire vertical axis. Integrating along that axis contradicts strict sublinear growth. If the symbol derivative bounds hold, (1) also follows by taking a sequence to infinity, where grad rho tends tozero. Thus convergence to a nonzero affine density on compact sets cannot be upgraded to global uniform gradient convergence.

For an exact primary profile, put D=ell-1>0, a0=rho_y(0), R=||grad rho||_infinity and V=||DU||_(infinity,Frob). Suppose a proved energy gap has the form

    1+2D<=C(R+V),

where C can be the independently proved Lambda in ../sharper_energy_strain_cap/PROOF.md. For fixed M,K>0 impose the additional bounds R+V<=M|a0| and |a0|<=KD. Then1<=(CMK-2)D. If CMK<=2 there is no such exact profile. If CMK>2 there is none for0<D<1/(CMK-2). In particular an exact family with D tending tozero cannot have R+V=O(D). The uniform global estimates are essential; small center slope and local compact convergence alone do not imply them.

## 2. An explicit family with exact transport on an expanding disk

Choose smooth radial functions chi,eta on[0,infinity), with chi=1 on[0,1], chi=0 on[2,infinity), eta>=0 supported in(2,3), eta not identically zero. Put

    J=integral_0^infinity eta(t)dt/t>0,
    b=(a/4-D)/J,
    q_L(X)=a y chi(r/L)+b r sin(3theta)eta(r/L),            (2)

for arbitrary a!=0,D>=0,L>0. Each q_L is a smooth compactly supported Cartesian function: the potentially nonsmooth r sin(3theta) is multiplied by a function identically zero near the origin. Let v_L be its canonical full-plane IPM inverse.

Then on the entire disk r<L,

    q_L=a y, v_L=D(x,-y).                                 (3)

Consequently at ell=1+D the residual is exactly zero on that disk, and all its fixed compact derivatives are eventually zero as L tends toinfinity. At the center the slope is exactlya and the strain is exactlydiag(D,-D). The global derivative norms of q_L and v_L are independent of L. Yet no member with a!=0 is an exact full-plane profile, and the limiting affine density violates strict sublinear growth. For D>0 the limiting velocity also violates U=o(r).

## 3. Independent inversion proof of the interior identity

For smooth compact data define phi=(-Delta)^(-1)q_L using the planar Newtonian potential, and psi=partial_x phi. Then -Delta psi=partial_x q_L and the resulting velocity has the canonical decay and parity. The radial Newtonian kernel preserves angular Fourier modes.

In r<L, the first angular density is a r sin(theta)=a y. The regular first angular potential has form

    phi_1=-a y r²/8+C1 y,

because Delta(y r²)=8y. It contributes psi_1=-a xy/4. The third angular density is zero in the disk, so its regular interior potential is C3 r³sin(3theta)=C3(3x²y-y³); it contributes psi_3=6C3 xy. There are no other angular modes. Hence the entire interior stream is a constant multiple of xy, and the interior velocity is exactly linear.

Its coefficient follows from the canonical center identity

    c=psi_xy(0)=-q_y(0)/4+integral_0^infinity q_3(r)dr/r².

This identity, including its origin term, is independently proved in ../inverse/PROOF.md. For(2), q_y(0)=a, q_3(r)=b r eta(r/L), and the integral is bJ. Thus c=-a/4+bJ=-D, proving(3). This fixes the global inverse coefficient; no free linear strain is added.

The order-zero inverse commutes with genuine dilation, so q_L(X)=L q_1(X/L) and v_L(X)=L v_1(X/L). Taking one derivative proves the global norm invariance. Equation(3) gives W_y=(1+D)y-Dy=y, hence W.grad q_L=q_L throughout the disk.

## 4. Why the compact fields are not profiles

A nonzero smooth compact density with canonical velocity cannot solve W.grad q=q with ell>0. Its velocity is globally smooth with bounded derivatives and decays at infinity, so the flow of W=ell X+v exists for all real times. On any orbit, an exact solution would obey q(Phi_t X)=e^t q(X). Since q is globally bounded, letting t tend toinfinity gives q(X)=0 at every X, a contradiction. This argument proves nonexactness of(2) without numerical sampling or a condition on whether the trajectory crosses the support boundary.

The family therefore supplies a rigorous test of finite-domain verification. Exact residual on arbitrarily large finite disks, canonical inversion and the exact center identity still do not establish a full-plane profile. The missing tail is not a free gauge choice. In this example the affine local limit comes with its specific harmonic strain D(x,-y); only atD=0 is that velocity zero. No claim here identifies the limit of the numerics lane's actual states.

## 5. Local stationary shear rigidity

Let q,v be C¹ on a neighborhood of the origin, with the IPM parities, div v=0, curl v=-q_x and stationary transport v.grad q=0. Assume q_y(0)!=0. Then in a possibly smaller neighborhood,

    v=0, q=f(y).                                         (4)

To prove this, v_1(0,y)=0 by parity and

    psi(x,y)=integral_0^x v_2(t,y)dt

satisfies psi_x=v_2, psi_y=-v_1 by divergence. In particular psi(0,y)=0. By the inverse function theorem, (x,y)->(x,q(x,y)) is a C¹ coordinate map on a smaller neighborhood, with an inverse y=y(x,t) on a product rectangle containing x=0. At fixedt,

    partial_x psi(x,y(x,t))=psi_x-psi_y q_x/q_y
                             =(v_2 q_y+v_1 q_x)/q_y=0.

The value atx=0 is zero, so psi vanishes throughout the coordinate rectangle. Thusv=0 there; curl then givesq_x=0. This is a local rigidity statement, with no analyticity requirement. Extending it globally would need additional hypotheses, such as analyticity or a global connected graph foliation of level sets meeting the vertical axis. Neither is assumed for the primary class.

Smooth odd shears q=f(y),v=0 supply stationary examples, including f=tanh(y), which is nonlinear. They do not solve the original self-similar equation with ell>1 and nonzero center slope: differentiating ell y f'=f atzero gives(ell-1)f'(0)=0. Thus the stationary limiting problem cannot silently be identified with the original profile problem.

## 6. Scope and verification

The gradient and energy statements are exact mathematical consequences with the displayed hypotheses. The compact family and local shear proof were independently reconstructed from their defining equations. Separate direct-kernel computations check(3) for two scales and both signs ofa; these manufactured checks test the evaluator, not the theorem or existence of a profile. The limit ell->1 remains open without additional compactness, a specified dilation, nontriviality and control of the global inverse and tail.
