# Sign reversal of the rescaled flow and the hydrostatic feedback term

Result 223, independent audit of the lead's 2026-10-21T12:58Z remarks R-a and R-b. Written before the checking code. This proof concerns exact algebraic transformations and a specified frozen operator. It does not assert well posedness or ill posedness of a variable-coefficient nonlinear evolution on an unspecified space.

## The elliptic rescaled flow

Let U be the canonical full-plane linear velocity operator for smooth even-x/odd-y densities with sublinear growth and the derivatives needed below. Let S[rho]=psi_xy(0), a linear functional supplied by the independently verified [canonical inverse](../inverse/PROOF.md) and [origin calculation](../origin/PROOF.md). Fix a real C>1. Define

 w[rho]=S[rho]/(1-C), v[rho]=C*w[rho],
 F(rho)=w[rho]*rho-(v[rho]*X+U[rho]).grad rho.

For every real t, linearity gives F(t*rho)=t^2*F(rho). In particular F(-rho)=F(rho). If rho(tau) is any differentiable solution on a time interval, then r(tau)=-rho(-tau) is a solution on its reflected interval: r_tau(tau)=rho_tau(-tau)=F(rho(-tau))=F(r(tau)). This is an algebraic statement on an existing trajectory, not existence of a backward trajectory.

Differentiating F(-rho+s*h)=F(rho-s*h) at s=0 gives DF(-rho)h=-DF(rho)h. This identity holds wherever the derivative is defined, not just at a steady state. If the same domain is used for the two unbounded linear realizations, their spectra are negatives of one another. No spectral stability assertion follows without specifying such a realization. At the elementary frozen Fourier-symbol level, the feedback term -U[h].grad rho reverses sign with rho.

Suppose rho is a steady state, w=w[rho]!=0, and rho_y(0)!=0. Put q=rho/w. By linearity U[q]=U[rho]/w, and division of F(rho)=0 by w^2 gives

 (C*X+U[q]).grad q=q.

The stream function scales by 1/w as well, preserving the inverse, gauge and parities for either sign of w. Constant nonzero multiplication preserves smoothness and the growth class. Hence q is a primary profile with c_l=C and q_y(0)=rho_y(0)/w. This is not a claim that multiplication by a negative number is a symmetry of the normalized profile equation: it maps a steady state of this different rescaled flow into a profile. A nonzero affine state with these normalizations has w=0 and is excluded from the division.

The slope of a rescaled trajectory is constant. If a=rho_y(0), differentiating F at the origin gives a_tau=[w-v-S]a=0 by w(1-C)=S. In particular the slice a=-1 gives negative normalized slopes only for w>0. At w<0 its steady profiles have positive slope; it is the sign and time reversal of the corresponding a=+1 flow. No interpretation through positive physical amplitudes or forward physical time is asserted for w<0.

The cancellation-renormalized strain formula is

 S[rho]=-a/4+integral_0^infinity rho_3(r)*r^(-2) dr,

under the primary growth bound, with rho_3 the sin(3*theta) coefficient. At a=-1, w>0 is equivalent to that moment being less than -1/4. For a smooth radial function w0 with w0(0)=1 and y*w0(r) satisfying the stated growth bounds, take

 rho=-y*w0(r)+b*(3*x^2*y-y^3)*exp(-r^2).

Its slope is -1, its third mode is b*r^3*exp(-r^2), and its moment equals b/2. Thus S=1/4+b/2 and w>0 exactly when b<-1/2. For C=3,b=-2 this yields S=-3/4,w=3/8. This is a smooth manufactured start, not a steady profile.

## Hydrostatic rescaling and the missing unit-slope condition

Assume g is smooth with parities and sufficient decay of its x derivatives to define the canonical hydrostatic inverse

 V1[g](x,y)=-integral_y^infinity g_x(x,t)dt,
 V2[g](x,y)=integral_0^y t*g_xx(x,t)dt
                 +y*integral_y^infinity g_xx(x,t)dt

for y>0, with parity extension. Assume these velocities have the required sublinear growth if a hydrostatic profile class is claimed. Consider a steady rescaled equation

 w*g=(c1*x+V1[g])*g_x+(c2*y+V2[g])*g_y.

Here w,c1,c2 are constants evaluated at the steady state, w!=0, and c1=c2=c*w. For the target profile problem also require c>1; the algebraic identities below do not themselves impose that inequality. If c1 and c2 are unequal, the following vertical dilation does not make them equal. For a chosen beta>0 set

 G(x,Y)=g(x,Y/beta)/(beta*w).

Direct changes of variables in the two integrals give

 V1[G](x,Y)=V1[g](x,Y/beta)/w,
 V2[G](x,Y)=beta*V2[g](x,Y/beta)/w.

Since G_x=g_x/(beta*w) and G_Y=g_y/(beta^2*w), substitution yields

 (c*x+V1[G])*G_x+(c*Y+V2[G])*G_Y=G.

This is valid for every beta>0 at the level of the transport and inverse equations. However, the full problem (3) of Section3.72 also imposes G_Y(0)=1. Its actual value is

 G_Y(0)=g_y(0)/(beta^2*w).

Thus the unit-slope condition requires g_y(0)/w>0 and the specific choice beta=sqrt(g_y(0)/w). Arbitrary beta does not suffice. If that ratio is negative, this positive-sign hydrostatic operator cannot be made to have slope +1 by this transformation; one must state a different signed formulation explicitly. The leading vertical coefficient also changes: g(0,y)~K*y^p gives G(0,Y)~K*beta^(-p-1)*Y^p/w. It must not silently be normalized to 1. The construction alone does not establish the center relation, a steady state, or existence of a nonzero admissible profile.

## Exact feedback on a horizontal mode

For a smooth compactly supported vertical test phi on the positive half-line define

 (K phi)(y)=integral_0^infinity min(t,y)*phi(t)dt,
 (J phi)(y)=integral_y^infinity phi(t)dt.

Then -(K phi)''=phi, (K phi)(0)=0 and (K phi)'(infinity)=0. The first boundary value is inherited from odd-y stream parity. It is not a physical wall or an independent extra boundary condition. The inverse K is not asserted to be a bounded inverse of -d_y^2 on all half-line L2. For example, a compact phi with a nonzero first moment produces a nonzero constant tail in K phi. If phi=-psi'' for a compactly supported smooth psi away from zero, both integrations show K phi=psi exactly, so there is no constant tail.

For the complex mode h(x,y)=exp(i*k*x)*phi(y), direct differentiation of the hydrostatic formulas gives

 V1[h]=-i*k*exp(i*k*x)*J phi,
 V2[h]=-k^2*exp(i*k*x)*K phi.

Consequently the perturbation-velocity part of the linearized rescaled transport is

 -V[h].grad g=exp(i*k*x)*[i*k*g_x*J phi+k^2*g_y*K phi].

Taking real and imaginary parts, or reflecting wave packets, enforces the required x parity. A single complex mode is a diagnostic, not a sublinear-density candidate. Terms from variations of the rates, from transport of h by the base velocity and from w*h are distinct terms. The displayed identity alone does not dispose of them.

If the base gradient is frozen with g_y=a and g_x=0, the displayed feedback operator is a*k^2*K. Its coefficient grows quadratically in horizontal frequency on any fixed nonzero vertical test. On the full line, restricting vertical Fourier support to frequencies bounded away from zero makes K the multiplier 1/eta^2. The exact constant-gradient feedback equation then has multiplier exp(a*k^2*tau/eta^2). For a>0, fixed tau>0 and a fixed compact interval of nonzero eta, this multiplier is unbounded in every Sobolev norm as |k| tends to infinity: multiplying the initial Fourier packet by any power of k cannot offset exp(c*k^2*tau). There is no bounded forward Sobolev solution operator for this specified frozen feedback equation. For a<0 the same multiplier has modulus at most1. This last fact is a semigroup statement about that isolated frozen operator only.

The lead's R-b term and its destabilizing sign are therefore correct as frozen diagnostics. A theorem that the complete variable-coefficient nonlinear rescaled flow is ill posed wherever g_y>0 needs a stated function space and an additional argument transferring this growth to that flow, respecting nonlocal tails, rate variations, localization and parities. Conversely a negative frozen sign is not a proof of nonlinear well posedness. Neither conclusion is proved here. Suggested wording: "The frozen hydrostatic feedback has an unbounded positive horizontal-frequency growth term when g_y>0; a nonlinear well-posedness theorem is not supplied." This is stronger evidence of derivative loss than the bounded elliptic feedback symbol, but not a substitute for that missing theorem.

## Verification and scope

Independent symbolic tests will check the quadratic sign identity, linearization sign, steady-state division for both signs, the anisotropic inverse factors, the transformed slope, the Gaussian strain moment and the mode signs with a concrete decaying vertical function. The test program will not execute producer code, instantiate a server or run an evolution solver. The proof is the argument above, not a test count. R-a is confirmed under its explicit nonzero-rate and trajectory hypotheses. R-b's algebra is confirmed after the slope repair; its complete nonlinear well-posedness conclusions remain open. Full SettingIII remains unresolved.
