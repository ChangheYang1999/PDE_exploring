# Nonanalytic strong unstable germs with the same beta-two local equations

Status: complete informal proof, independently checked by exact algebra and numerical flow controls. Actual Claude Opus 5.5 reviewed the argument conditional on dependencies156 and158; its derivative-dependency point is supplied explicitly below. This constructs nonprofiles only. The vorticity equation is not imposed on the outgoing basin.

## 1. Statement and dependencies

Fix a0>0 and R0>0. Start with the smooth whole-plane beta=2 configuration of packet156, with the endpoint geometry proved in158. Write

    J(u,v)=(-v,u), W=2X+U, U=J gradPsi, Omega=-DeltaPsi,
    gamma={(x,F(x)/4): -A<=x<=A}, M=F(A),
    p_+=(A,M/4), p_-=(-A,M/4), A>R0+1.

The two defining profile equations at beta=2 are

    (T) W.gradTheta=0,
    (V) W.gradOmega+Omega=Theta_x.

The convention is Omega=-curl U=-curl W, with curl U=partial_x U_2-partial_y U_1.

There is a compact area-preserving diffeomorphism Phi, commuting with x-reflection and equal to the identity near the core disk and near every point of the open arc, for which the fields

    W_new=Phi_*W, Theta_new=Theta o Phi^-1,
    U_new=W_new-2X, Omega_new=-curl U_new

have all of the following properties. They retain the ordinary canonical full-plane inverse, U_new(0)=0, the original exterior, nonnegative bounded temperature with zero set the axis, exact global temperature transport, both equations on the prescribed disk and near every interior point of gamma, every residual jet zero on gamma, and flat endpoint jets of Omega_new and Theta_new-M. The full equilibrium set is the same arc gamma. Both endpoints remain outgoing. The strong unstable curve at each endpoint is smooth and does not agree with any regular real analytic embedded curve germ through the endpoint.

These fields nevertheless fail the vorticity equation on a nonempty open invariant set issuing from each endpoint and in the unchanged far-field cone. Thus adding the necessary nonanalytic-germ condition of lead4.7(vi) to the properties of156 does not make those properties sufficient for a profile. This does not impose the harmonic outgoing basin that a true profile would possess and is not a broad nonexistence result.

Dependency156 supplies all global fields, decay, full-plane inverse and exact arc neighborhoods. Dependency158 supplies the local outgoing formulas and an open invariant set whose backward limit is an endpoint, with Theta=M and some nonzero Omega. The argument below rederives the new deformation and its effect on the defining equations. No computation is a premise.

## 2. A compact Hamiltonian flat at each endpoint

Near p_+ put u=x-A and Y=y-M/4. Since g=F/4 satisfies g(A)=M/4 and g'(A)=0, choose delta>0 small enough that the two endpoint neighborhoods are disjoint, avoid the prescribed core and the symmetry axis, lie within the translation band of156, and

    |g(x)-M/4| < |x-A|/4                 (0<|x-A|<delta).

Choose smooth even cutoffs chi and zeta with

    chi(q)=1 for |q|<=1/4, chi(q)=0 for |q|>=1/2,
    zeta(q)=1 for |q|<=1/2, zeta(q)=0 for |q|>=1.

Set epsilon=delta/100, and define the even positive flat function and its odd primitive

    eta(Y)=epsilon exp(-delta^2/Y^2) for Y!=0, eta(0)=0,
    H(Y)=int_0^Y eta(v)dv.

Define, for Y!=0,

    h_+(x,y)=H(Y) chi((x-A)/Y) zeta(Y/delta),

and set h_+=0 when Y=0. This is a smooth compact function flat at p_+. Indeed its support is contained in |Y|<=delta and |x-A|<=|Y|/2. Any fixed derivative away from Y=0 is a sum of bounded cutoff derivatives times a fixed negative power of |Y| times a derivative of H. Every derivative of H is flat at0, so these expressions tend to0 faster than any power of |Y|. Outside the shrinking cone they vanish. This proves smoothness and zero full jet at the cone vertex.

Put h=h_+(x,y)-h_+(-x,y), and let Phi_t be the complete flow of J grad h for 0<=t<=1. The supports are disjoint; h is compact and odd in x. The flow preserves area, commutes with x-reflection, and is the identity outside its support. Every jet of Phi_t-Id vanishes at p_+ and p_-: differentiate the flow equation successively there, using that every derivative of J grad h vanishes. In particular the endpoints are fixed.

No point of the open arc belongs to the closed support: near p_+ the arc satisfies |Y|<|u|/4 whereas support requires |u|<=|Y|/2; the reflected argument applies near p_-. The support is separated from all remaining arc points. Thus Phi_t is the identity on an open neighborhood of every interior point of gamma, and it is the identity near the prescribed core and axis.

## 3. The exact nonanalytic curve germs

For 0<|Y|<=delta/2,

    eta(Y)/|Y|=(1/100)(delta/|Y|) exp[-(delta/|Y|)^2] < 1/4.

The path (A-t eta(Y),M/4+Y) stays where chi=zeta=1 for every t in[0,1]. There J grad h=(-eta(Y),0), so uniqueness gives

    Phi(A,M/4+Y)=(A-eta(Y),M/4+Y).          (1)

The old strong unstable curve is the vertical segment x=A, on which W=(0,4Y). Flow conjugacy and preservation of the endpoint carry it to the strong unstable curve of W_new. Its germ is therefore the regular graph x=A-eta(Y). It has the Taylor jet of the vertical line but is not that line on either punctured branch. If a regular analytic embedded curve agreed with this germ, its tangent would be vertical, so the analytic implicit-function theorem would express it as an analytic graph x=f(Y). All derivatives of f-A at0 would vanish, forcing f=A near0 and contradicting eta(Y)>0. Thus there is no such analytic curve germ. Reflection gives x=-A+eta(Y) near p_-.

The endpoint's reduced outward dynamics is unchanged on the old outgoing center segment Y=0, where the deformation is the identity. Equivalently, the existence and outward orientation of the center branch are preserved by the diffeomorphism. Both endpoints remain outgoing, and zeros are carried bijectively by Phi. Since Phi fixes gamma pointwise, the entire zero set remains gamma.

## 4. Canonical inverse and preservation of the equations

Divergence is preserved by an area-preserving pushforward, so div W_new=4 and div U_new=0. Global temperature transport follows by the chain rule. A compact stream correction is given explicitly by

    Psi_new-Psi=int_0^1 (W_t.grad h-4h)dt,
    W_t=(Phi_t)_*W.                         (2)

In fact dW_t/dt=D(J grad h)W_t-DW_t(J grad h)=J grad(W_t.grad h-4h), using div W_t=4. The correction is compact and odd. Its vorticity is -Delta of a compact smooth function, whose ordinary full-plane Biot-Savart inverse is its stream gradient. Adding this to the canonical old inverse proves that U_new is the canonical inverse, with no added constant or harmonic strain. It has the same O(1/r) exterior and U_new(0)=0.

On a neighborhood of each interior arc point and on the core the map is the identity, so W,Theta,U,Omega and their defining residuals remain unchanged there. The integrand in(2) is identically zero near the core because h and its gradient vanish there. The exact core stream formula of156 therefore remains valid.

At the endpoints the map is flat relative to identity, so all full jets of W_new,Theta_new coincide with the old jets. The flatness of Omega_new,Theta_new-M and of every residual jet follows. Nonnegativity, boundedness and the exact temperature zero set follow from pullback and the fact that Phi fixes the axis and maps its complement onto itself. The original far-field residual formula and its sign-changing vorticity witnesses are untouched.

## 5. Explicit failure on the curved strong unstable germ

In the inner cone, Phi is the horizontal shear (x,Y)->(x-eta(Y),Y). For every fixed Y in this small band, the old fields on x>=A are exactly W=(v(x),2Y(1+a(x))) and Theta=M, with v=2x(1-chi_old), a=chi_old+x chi_old′. Every derivative of chi_old-1 at A vanishes, so all positive x derivatives of W vanish at (A,Y), its value is (0,4Y), and every positive derivative of Theta vanishes there. Smoothness of the156 construction makes these the common two-sided jets. This is stronger than flatness at the single endpoint: it holds for every Y in the band, as required when differentiating the vorticity residual. Therefore along the image curve (1),

    W_new=(-4Y eta'(Y),4Y),
    Omega_new=-4[eta'(Y)+Y eta''(Y)]
             =-16 epsilon delta^2 exp(-delta^2/Y^2)
                    (delta^2-Y^2)/Y^5.               (3)

Here Omega=-curl W by the stated convention. For 0<Y<delta/2 this is strictly negative. Theta_new=M and grad Theta_new=0 on this curve because the old temperature gradient vanishes at x=A. Along the curve, W_new differentiates as 4Y d/dY. Thus

    R_Omega,new=-4 eta' -36Y eta'' -16Y^2 eta'''
       =-16 epsilon delta^2 exp(-delta^2/Y^2)
           [8delta^4/Y^7-27delta^2/Y^5+11/Y^3].       (4)

For 0<Y<=delta/2 the bracket is positive: with z=delta^2/Y^2>=4 its numerator is8z^2-27z+11, positive at4 and increasing thereafter. Hence (V) fails even on each sufficiently short upper branch of the curved strong unstable germ, although its complete endpoint jet vanishes. On the lower branch the same formula is nonzero with the opposite sign, since eta is even and the residual in(4) is odd in Y.

An open invariant failure region also follows without relying on(4). Shrink the outgoing wedge of158 to satisfy |Y|<c v(x)<(x-A)/4, where v(x)=2x(1-chi_old(x)) is flat at A. It lies outside the support of h and contains a point with old Omega nonzero, as proved in158. The map is the identity near that point, so Omega_new is nonzero there. Map the old open invariant region by Phi. It remains open and invariant, every backward orbit tends to p_+, and Theta_new=M there. If(V) held throughout it, Omega_new(phi_{-t}X)=exp(t)Omega_new(X), contradicting boundedness near the endpoint. Reflection gives the second endpoint.

## 6. Scope

This construction preserves the local equations and all arc jets while giving nonanalytic strong unstable germs. It does not create a harmonic outgoing basin, repair the exterior residual, produce a candidate, or rule out a different global profile. It isolates another insufficient collection of necessary local conditions. The nonanalyticity is an exact C-infinity germ property, not a visual claim from finite samples.

Written UTC 2026-10-21T11:14:04.110756+00:00, before code or controls.

Revision UTC 2026-10-21T11:21:09.418087+00:00: explicit equations and transverse-jet dependency added after the247 review; the proof’s construction and formulas are unchanged.
