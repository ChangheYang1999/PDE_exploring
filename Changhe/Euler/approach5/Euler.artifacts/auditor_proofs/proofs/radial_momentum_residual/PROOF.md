# The radial momentum mean follows from the Poisson equation

Auditor verdict: A396, CONFIRMED at the exact hypotheses below.

## Statement

Let u in C2(R3;R3) satisfy div u=0. Let p in C2(R3) satisfy

    -Delta p=partial_i partial_j(u_i u_j)

on all of R3, with repeated indices summed. Let c and omega be any real constants, and let J(y1,y2,y3)=(-y2,y1,0). Define A=cI-omega J and the C1 momentum residual

    E=(1-c)u+(Ay).grad u+omega Ju+(u.grad)u+grad p.

Then div E=0. Consequently, for every R>0,

    integral_S2 E(R theta).theta dtheta=0.

More generally E annihilates every compactly supported C1 gradient test, and the flux across the boundary of every bounded C1 domain is zero. No decay, pressure normalization, profile equation E=0, or tail expansion is assumed.

## Proof

The divergence of (1-c)u is zero. Differentiation of the linear drift gives

    div[(Ay).grad u]
      =A_ji partial_j u_i+(Ay).grad(div u)
      =-omega J_ji partial_j u_i.

On the other hand, relabeling the two indices gives

    div(omega Ju)=omega J_ij partial_i u_j
                =omega J_ji partial_j u_i.

These two terms cancel exactly, for every omega. Incompressibility also gives (u.grad)u=div(u tensor u). Its divergence is the right side of the Poisson equation, which cancels Delta p. Thus div E=0 pointwise.

Apply the divergence theorem to the radius-R ball. Its outer normal is theta and its area element is R^2 dtheta, so the flux identity is R^2 times the asserted spherical mean. Divide by R^2. Integration by parts against a compact gradient yields the test-function statement. The same divergence theorem proves the domain version. All integrations are on compact sets, so no condition at infinity or discarded boundary term is involved.

## Why this is only a necessary scalar test

These identities do not imply E=0. For example, let u=b be a nonzero constant, p=0, and 0<c<1. The Poisson equation holds while

    E=((1-c)I+omega J)b

is a nonzero constant vector. Its spherical radial means and compact gradient tests vanish. This example is a countertest for the implication, not a decaying Euler profile.

The canonical-pressure means in A351-A352 therefore cannot become an additional whole-sphere radial momentum obstruction solely by imposing the Poisson equation. Testing against u, or using a basin-dependent vector weight, involves different information. No sign of such a test or nonexistence conclusion is established here.

## Verification

Read all of the submitted LIT73 Section6, independently expanded both rotation divergences, and checked finite-radius fluxes and arbitrary pressure constants. The argument is elementary and uses no source theorem beyond divergence and integration by parts. The retained submission and its hash are in the team records. No numerical computation or formal build was used.
