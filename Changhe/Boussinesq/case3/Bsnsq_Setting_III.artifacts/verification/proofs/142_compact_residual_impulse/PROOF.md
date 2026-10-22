# Residual impulse identities for perturbations with fixed exterior fields

Status: CONFIRMED by independent informal proof, 11 exact controls, 15 compact quadrature controls, and a written actual Claude Opus 5.5 audit, 2026-10-21. This is a conditional identity and compact-repair obstruction, not nonexistence for the broad B2 class.

## Exact statement

Fix a real beta and set k=beta-2. For j=0,1 let Psi_j and Theta_j be smooth functions on R^2. Write

    v_j=(-partial_y Psi_j,partial_x Psi_j),
    W_j=beta(x,y)+v_j, Omega_j=-Delta Psi_j,
    f_j=W_j.grad Omega_j+Omega_j-partial_x Theta_j,
    t_j=W_j.grad Theta_j-k Theta_j.

Assume chi=Psi_1-Psi_0 and tau=Theta_1-Theta_0 are compactly supported. No integral of an individual field at infinity is assumed to converge. Every difference appearing below is compactly supported, so its integral and polynomially weighted integrals are ordinary finite integrals. Put delta f=f_1-f_0 and delta t=t_1-t_0. Then

    integral delta f = integral y delta f = 0,                    (1)
    integral x delta f = integral tau,                           (2)
    integral delta t = -(3 beta-2) integral tau.                  (3)

In particular

    integral [delta t+(3 beta-2)x delta f]=0.                    (4)

If both fields satisfy exact thermal transport t_0=t_1=0 and 3 beta-2 is nonzero, (2)-(3) give integral x delta f=0 as well. For beta>2 this always applies. Thus all three first-degree moments of f are invariant under compact changes of the stream and temperature that preserve thermal transport and the complete exterior fields. If an individual residual f_j is compact, its three moments themselves are well-defined and equal for such pairs.

For the moving-center B2 interpretation, x-odd stream parity gives U_{j,1}(0)=0. Use the relative stream Psi_j=Psi_j^physical-U_{j,2}(0)x, so v_j=U_j-U_j(0) and grad Psi_j(0)=0. Without that parity the general formula also adds U_{j,1}(0)y. The compact-support assumption concerns this relative stream; a change of center velocity that introduces a nonzero exterior linear term does not satisfy this assumption. If the perturbation is supported away from the center, this normalization is preserved. The identities neither add a harmonic strain nor fit a new uniform drift. They remain valid for canonical whole-plane inverses with slow nonintegrable individual tails because only compact differences are integrated.

## Proof without integration of divergent individual terms

First delta Omega=-Delta chi. For any affine function ell, integration by parts twice, over a ball containing supp chi, gives

    integral ell delta Omega = -integral chi Delta ell=0.       (5)

This proves vanishing of the mass and both first moments of delta Omega. The gradients and all products below have compact differences, so each subsequent integration by parts can also be done over a sufficiently large ball with zero boundary difference.

For any smooth stream Psi set p=Psi_x and q=Psi_y. Direct differentiation gives the Cartesian stress identities

    v_1 Omega = partial_x(p q)+partial_y((q^2-p^2)/2),
    v_2 Omega = partial_x((q^2-p^2)/2)-partial_y(p q).            (6)

Indeed, the first right side is q Delta Psi and the second is -p Delta Psi, which are v_1 Omega and v_2 Omega under the stated signs. The differences of both stress components in (6) are compactly supported because grad Psi_1-grad Psi_0=grad chi has compact support. Hence

    integral (v_{1,i} Omega_1-v_{0,i} Omega_0)=0, i=1,2.         (7)

Here the first subscript on v labels the configuration, and i labels its Cartesian component.

Since div W_j=2 beta, write

    f_j=div(W_j Omega_j)+(1-2 beta)Omega_j-Theta_{j,x}.

Taking the difference and integrating gives (1)'s mass identity by (5). Multiplying the difference by x and integrating gives

    integral x delta f
      =-integral [W_{1,1}Omega_1-W_{0,1}Omega_0]
        +(1-2 beta)integral x delta Omega+integral tau
      =(1-3 beta)integral x delta Omega
        -integral [v_{1,1}Omega_1-v_{0,1}Omega_0]+integral tau
      =integral tau.

The same computation with y has no temperature term, and (5),(7) give integral y delta f=0. This proves (1)-(2). Finally

    t_j=div(W_j Theta_j)-(3 beta-2)Theta_j.

The difference W_1 Theta_1-W_0 Theta_0 is compact: it is (W_1-W_0)Theta_1+W_0 tau. Integrating its divergence therefore gives zero and proves (3). Equation (4) and the thermal-exact consequence follow algebraically. No individual integral of W_j Omega_j, v_j Omega_j, Theta_j, f_j or t_j was used unless its compactness was separately assumed. This completes the proof.

## Consequences for a compact correction problem

Let a smooth canonical B2 configuration with beta>2 have exact thermal transport and compact vorticity residual R. Suppose a proposed exact B2 profile has exactly the same stream and temperature outside a compact set, in the same relative gauge, so the differences satisfy the theorem. The proposed profile has zero residual. Then necessarily

    integral R=integral x R=integral y R=0.                    (8)

Under the B2 x-reflection parity, R is odd in x, so the first and third conditions follow already by parity. The x-weighted condition is potentially nontrivial. If its value for a given reference is nonzero, that reference cannot be repaired by such compact perturbations while retaining exact thermal transport and its complete exterior fields. No value for the reference of packet135 has been computed here. In particular this proof does not claim that its impulse is nonzero, nor that a compact repair is possible when the impulse vanishes.

The deformation of packet140 is a special case. Its velocity change is compact, divergence free and zero near the center. It has a smooth stream difference constant on the unbounded exterior component; choose that constant zero. The difference is compact, including any bounded holes, and its odd parity fixes the same constant. Its temperature change is compact and both temperatures solve the thermal equation. Thus these three moments are preserved by every such deformation even though packet140 proves that the singular harmonic weight xy/(x^2+y^2)^2 can change the residual moment. These are distinct weights and compatible conclusions.

For a smooth one-parameter family of compact perturbations with support in a fixed compact set, differentiating (1),(4) gives annihilating linear functionals for the coupled linearized map (dot f,dot t): weights (1,0), (y,0) and ((3 beta-2)x,1). This is an algebraic annihilator statement. In a compactly supported test-function topology these moment functionals are continuous. It does not assert a Fredholm property, closed range, dimension of a cokernel, or that these are all annihilators. For thermal-preserving variations the x-weight alone also annihilates dot f when beta>2.

## Scope and dependencies

The proof is self-contained and uses only differentiation, compact support and integration by parts. Packet140 is needed only for the named conjugacy application. Packet135 is needed only to supply a global reference with compact residual; its impulse is not evaluated here. Smoothness may be weakened to enough derivatives for the displayed identities and integration by parts, but no such extension is used. No sign of temperature or vorticity, analyticity, bounded individual norm or far-field expansion is required. Changing the complete exterior fields is permitted in the original B2 problem, so an obstruction with the exterior fixed is not a full NO endpoint.
