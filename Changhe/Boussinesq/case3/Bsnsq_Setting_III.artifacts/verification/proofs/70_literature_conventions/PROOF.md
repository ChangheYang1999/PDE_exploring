# Coordinate translation and the B2 center jet

Date:2026-10-20. Status: independent proof complete. This is a convention and scope lemma, not a nonexistence theorem for the full target.

## Exact statement

Suppose fields in coordinates(a,b) satisfy

    u=(psi_b,-psi_a), Delta psi=omega,
    omega_t+u.grad omega=rho_b, rho_t+u.grad rho=0.

Set (x,y)=(b,a) and

    Psi(t,x,y)=psi(t,y,x), Omega(t,x,y)=-omega(t,y,x),
    Theta(t,x,y)=-rho(t,y,x),
    U(t,x,y)=(u_b(t,y,x),u_a(t,y,x)).

Then U=(-Psi_y,Psi_x), -Delta Psi=Omega, and

    Omega_t+U.grad Omega=Theta_x,
    Theta_t+U.grad Theta=0.

If omega is odd separately in a and b, and rho is odd in a and even in b, then Omega is odd separately in x and y, and Theta is even in x and odd in y. Consequently, at the symmetric center, no rescaled temperature retaining these parities can have

    Theta(x,y)=a0 x^2+O((x^2+y^2)^(3/2)), a0!=0.

The obstruction concerns this specified center and parity. A material center with constant position is not, by itself, excluded by the moving-center formulation.

## Complete proof

The chain rule gives Psi_x=psi_b and Psi_y=psi_a. Since the coordinate swap preserves the Laplacian, -Delta Psi=-omega=Omega. The reordered velocity is U=(-psi_a,psi_b)=(-Psi_y,Psi_x), with the arguments composed as stated. For any scalar f and its swapped scalar F, direct differentiation gives U.grad_(x,y)F=u.grad_(a,b)f. Therefore the vorticity equation, multiplied by minus one and evaluated at(a,b)=(y,x), has right side -rho_b=Theta_x. The temperature equation follows by the same multiplication and coordinate change.

Changing the new x sign changes the old b sign, while changing the new y sign changes the old a sign. The two asserted transformed parities follow immediately. In particular Theta(x,0)=0 for all x for which the field is defined. If the proposed center expansion held, restricting it to y=0 would yield 0=a0 x^2+O(|x|^3). Dividing by x^2 and sending x to0 gives a0=0, a contradiction. This argument needs only the displayed expansion and parity, not any additional decay or integrability assumption. The same parities persist under dilations and nonzero scalar multiplication, so the argument also applies to their similarity profiles centered at that point.

Finally, a moving material center is a trajectory z0'(t)=u(t,z0(t)). The constant path is a valid special case when its velocity is zero. The relative field subtracts u(t,z0(t)) in either case. Thus constant position supplies no separate obstruction; the specific center-jet contradiction above does.

## Application and limits

Section2 of Elgindi and Pasqualotto, arXiv:2310.19780v1, PDF page9, states precisely the convention and parities used in this lemma. Their Theorem1.1, PDF page2, concerns finite-energy initial data of C^(1,alpha*) regularity, smooth away from the origin, with finite-time singularity. The theorem is not a claim of the exact smooth B2 profile in the present prompt. Merely belonging to C^(1,alpha*) would not logically prove nonmembership in C-infinity. The exact parity/jet obstruction above avoids that invalid inference and distinguishes their particular construction from all possible whole-plane constructions.

The source identification and the separate wall-setting audit of arXiv:2604.01868v1 are recorded in verification/literature_20261020T2031/AUDIT.md. No theorem or computer-assisted component of either paper has been fully reproved here. The confirmed verdict concerns their applicability to the precise B2 target.
