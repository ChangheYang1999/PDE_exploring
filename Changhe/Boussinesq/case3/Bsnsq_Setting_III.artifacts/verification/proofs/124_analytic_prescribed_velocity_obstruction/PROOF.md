# A prescribed analytic velocity can fail on every open set

Written 2026-10-21T04:43:19.645847+00:00, before packet124 computations. Status: CONFIRMED after independent exact controls and actual Opus163/164 written audits, finalized 2026-10-21T04:51:17.459905+00:00. This is a restricted obstruction for the explicit base field, not a full B2 nonexistence theorem.

## Exact statement

Fix beta>2 and a0>0. Put k=beta-2, c=1+beta/2, mu=1+3beta/2, q0=4a0/beta, p=(beta-1)/(2beta),

    L=3c sqrt(beta)/(4a0), h=sqrt(beta)L, S=L^2+x^2+(y-h)^2,
    S0=L^2+h^2, B=c/(2ph S0^(p-1)), Psi_e=-BxS^p.

Set U_e=(-Psi_e,y,Psi_e,x), W_e=beta X+U_e-U_e(0), and Omega_e=-Delta Psi_e. There is no nonempty open set O in R^2 and no C2 function Theta on O such that both

    W_e.grad Theta=k Theta,
    Theta_x=W_e.grad Omega_e+Omega_e

hold on O. No parity or axis condition on this local Theta is assumed.

Consequently, no smooth global B2 solution can agree with BOTH this relative velocity and this vorticity on any nonempty open set. In particular the stream modifications in packets119,121,122,123, whose vorticity and relative-velocity changes vanish outside a compact set or a fixed vertical strip, cannot be full profiles. The exact-disk and all-axis-jet conclusions of those packets are unaffected.

This theorem does not cover arbitrary compact vorticity perturbations with a nonzero harmonic velocity change outside their support. It does not exclude other analytic velocities, arbitrary profiles, or a convergent sequence whose exterior agreement is lost in the limit.

## A necessary analytic compatibility identity

First work with any smooth prescribed W and Omega, with any constant k, and define

    F=W.grad Omega+Omega,
    J=partial_x W2,
    D=(k-partial_x W1)F-W.grad F,
    Z=W1 F J+W2 D,
    E=J partial_y Z-Z partial_y J-k D J.                 (1)

These definitions involve only W and Omega. If a C2 temperature satisfies both PDEs, differentiate its transport equation in x and use Theta_x=F:

    J Theta_y=D.

Multiplying the original temperature equation by J then gives

    k J Theta=Z.

Differentiate this identity in y, multiply by J, and substitute the two preceding identities. The result is E=0. No division by J or by a component of W is involved. The identity holds also at zeros of J and W. The regularity stated is sufficient because F is smooth independently and all derivatives of Theta used are of order at most two.

For the explicit base, W_e,Omega_e,F,J,D,Z,E are real analytic on all of R^2: S is strictly positive and every real power of S is analytic there. If both PDEs held on a nonempty open set, E would vanish on that set. The identity theorem for a real analytic function on the connected plane would imply E identically zero. We next compute one nonzero Taylor coefficient.

## Computation at the center

Write the smooth parity expansions

    Psi_e=x g1(y)+x^3 g3(y)+O(x^5),
    Omega_e=x q(y)+O(x^3),
    b(y)=W_e,2(0,y), A(y)=2beta-bprime(y), C(y)=6g3(y).

They imply

    W1=x A(y)+O(x^3), W2=b(y)+O(x^2), J=x C(y)+O(x^3).

Let M=2beta+1 and Lambda=2mu=3beta+2. The coefficient of x in F is

    H=b qprime+(M-bprime)q.

The coefficient of x in D is -G, where

    G=b Hprime-(2bprime-Lambda)H.                       (2)

Indeed k-2A=2bprime-Lambda. Therefore

    D=-xG+O(x^3), Z=-x bG+O(x^3).

The coefficient of x^2 in E is the exact smooth function

    E2(y)=-C(bG)prime+bG Cprime+kCG.                   (3)

The explicit base has

    b(0)=0, bprime(0)=mu, bsecond(0)=0,
    q(0)=q0, C(0)=-q0, G(0)=0,
    Gprime(0)=mu M qprime(0).                         (4)

For the last equality, differentiate (2), use 2bprime(0)=Lambda and bsecond(0)=0, and compute Hprime(0)=M qprime(0). All terms with b(0) vanish. The identities bsecond(0)=0 and C(0)=-q0 follow either directly or from the cubic polynomial

    Psi_e=ell x+cxy-q0x^3/6+O(|X|^4), ell=Psi_e,x(0).

Differentiate (3) at y=0. Using b(0)=G(0)=0 gives

    E2prime(0)=C(0)(k-2mu)Gprime(0)
               =q0(2beta+4)mu M qprime(0).             (5)

This is the ordinary monomial coefficient [x^2 y]E, not the derivative partial_x^2 partial_y E (which is twice it).

For completeness positivity of qprime(0) is explicit. With t=y-h,

    q(y)=4Bp(L^2+t^2)^(p-2)[2L^2+(p+1)t^2],
    qprime(y)=8Bp(p-1)t(L^2+t^2)^(p-3)[3L^2+(p+1)t^2].

At y=0, t=-h<0 and p-1<0, so qprime(0)>0. Substituting the chosen L,h,B gives

    qprime(0)=32a0^2(3beta+5)/[9beta^2(beta+1)(beta+2)].

To check the closed form without fractional powers, substitute Bp S0^(p-3)=c/(2h S0^2), h^2=beta L^2 and L^2=9c^2 beta/(16a0^2). The preceding formula reduces first to c(3beta+5)/[beta(beta+1)L^2], then to the displayed value.

Every factor in (5) is positive. At beta=4,a0=1 the coefficient is 476/5. Thus E is not identically zero. Analytic continuation contradicts its vanishing on any nonempty open set, proving the statement.

## Consequences and dependencies

The compatibility identity (1) is a local necessary identity for ANY prescribed field. Its zero is not sufficient for a temperature or a B2 solution. The analytic identity theorem is used only for the particular globally analytic base W_e,Omega_e. The modified configurations themselves need not be analytic. If a modified configuration solved both PDEs globally, restricting to an exterior open region of exact agreement with the base would already contradict the theorem.

A constant linear term in Psi has no effect on the relative velocity. The compact stream perturbations in packet119 start at total degree four; thus they leave the center velocity unchanged in any fixed representative. For packet123 the strip and weighted Borel corrections, and the compact disk correction, all vanish for sufficiently large |x|; their gradients at0 vanish. For the infinite sum this follows by its already proved local C-infinity convergence, hence by termwise first differentiation. The same beta is used in both fields, W is exactly beta X+U-U(0), and the vorticity operator is the Cartesian -Delta throughout. Hence their RELATIVE velocity, as well as vorticity, is exactly the base on either exterior half-plane. This is enough. It follows that the constructed full-plane fields are nonprofiles, even though both PDEs hold on a small disk and all vorticity residual jets vanish on the entire axis. The previously open question for these fixed-exterior constructions is therefore answered negatively by a restriction absent from the full B2 target.

Dependencies: elementary differentiation, real analytic identity theorem, and the explicit base formula. Packets119/121/122/123 are used only to identify which constructions have an open region of exact agreement. No numerical sign, far-field integration by parts, inverse approximation, or imported theorem about Boussinesq is used.
