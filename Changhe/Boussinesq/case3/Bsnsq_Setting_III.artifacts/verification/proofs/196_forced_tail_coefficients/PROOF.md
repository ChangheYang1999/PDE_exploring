# Distinct mixed powers and own-ladder coefficient defects

## Statement and hypotheses

Use X=(r sin(phi),-r cos(phi)), r>0, and beta>2. The equations are W.grad Omega+Omega=partial_x Theta and W.grad Theta=(beta-2)Theta, with U=(-Psi_y,Psi_x), -Delta Psi=Omega. The asserted leading velocity excludes linear or faster harmonic additions; this is required by sublinear velocity at infinity. Set alpha=1/beta, q=1-2alpha. Suppose a formal asymptotic expansion has leading Omega=r^(-alpha)a(phi), Theta=r^q b(phi). A source with beta_s>2 has leading velocity lambda r^(1-1/beta_s)u_s(phi); the unknown leading velocity is r^(1-alpha)u(phi), multiplied by e in the transport. The formulas below identify individual homogeneous contributions. A claim that they are the complete coefficients additionally requires that no other present exponent contributes at the same power. Such noncollision and controlled differentiation assumptions cannot be inferred from a finite-window fit.

The own-velocity predictions for the next coefficients are

 A2=e[-alpha u_r a+u_phi a']-[q sin(phi)b+cos(phi)b'],
 B2=e[q u_r b+u_phi b'].

The leading source interaction has powers -alpha-1/beta_s and q-1/beta_s, and its predicted coefficients are

 Am=(beta_s/beta)lambda[-alpha u_sr a+u_sphi a'],
 Bm=(beta_s/beta)lambda[q u_sr b+u_sphi b'].

Absence of a required nonzero mixed coefficient is a residual obstruction at that distinct power. It does not imply any nonzero lower bound on the error in the own coefficients A2,B2, let alone a near100percent error. The report's observed near100percent own-coefficient differences are numerical measurements, not consequences of the absent mixed power.

## Derivation

In these polar coordinates grad H=e_r partial_r H+e_phi r^(-1)partial_phi H, e_r=(sin(phi),-cos(phi)), e_phi=(cos(phi),sin(phi)). Thus partial_x(r^q b)=r^(q-1)[q sin(phi)b+cos(phi)b']. The diagonal dilation multipliers are beta*s+1 for Omega and beta*s-beta+2 for Theta. At s=-2alpha and s=1-3alpha both equal-1. The displayed transport products have precisely these degrees, giving A2 and B2 with the stated signs. At the mixed powers both multipliers equal-beta/beta_s, giving the factor beta_s/beta. A constant velocity contributes at Omega power-1-alpha and Theta power-2alpha, whose multipliers both equal-beta. These degree identities are exact.

For a sine mode a_n sin(n phi), put p=2-alpha. The polar Laplacian gives Delta(r^p sin(n phi))=(p^2-n^2)r^(p-2)sin(n phi). Since1<p<2, no positive integer resonance occurs. Therefore Psi=-a_n r^p sin(n phi)/(p^2-n^2) has -Delta Psi=Omega. Its velocity components are u_r=-partial_phi Psi/r and u_phi=partial_r Psi. This is the homogeneous particular contribution. It does not define an entire-plane smooth source at the origin, nor does it alone fix all constant/multipole terms of the full inverse.

## Endpoint coefficients of the represented fields

Assume the fitted exponent equals beta. Let z=1-t=(1+(r/L)^2)^(-1/(2beta)), and G=z^(beta+1)S_G(t,phi), F=z^(beta+2)S_F(t,phi), Omega=r sin(phi)G and Theta=r^2 sin(phi)^2 F. Suppose S_F,S_G have a one-sided C2 extension to t=1. Then z=L^alpha r^(-alpha)(1+O(r^-2)). Taylor expansion S(1-z)=S(1)-z S_t(1)+O(z^2) gives

 a=L^(1+alpha)sin(phi)S_G(1,phi),
 a2=-L^(1+2alpha)sin(phi)S_G,t(1,phi),
 b=L^(1+2alpha)sin(phi)^2 S_F(1,phi),
 b2=-L^(1+3alpha)sin(phi)^2 S_F,t(1,phi).

The extra factor r/sqrt(r^2+L^2) in odd angular modes is1+O(r^-2), hence cannot alter these first two powers when beta>2. Endpoint formulas specify exact mathematical coefficients of the stored spline representation; their floating evaluation is not an exact arithmetic certificate. Their own-ladder comparison must distinguish any same-power artificial tail of a represented external source.

## Explicit counterexample to forced own-coefficient mismatch

Take beta=4, beta_s=3, e=lambda=L=1, a=sin(phi), b=sin(phi)^2. The unknown leading stream-function coefficient is -16sin(phi)/33, so u_r=16cos(phi)/33, u_phi=-28sin(phi)/33. Thus

 A2=-(32/33)sin(phi)cos(phi)-(1/2)sin(phi)^3-2sin(phi)cos(phi)^2,
 B2=-(16/11)sin(phi)^2 cos(phi).

Choose endpoint functions S_G(1)=S_F(1)=1 and

 S_G,t(1)=(32/33)cos(phi)+(1/2)sin(phi)^2+2cos(phi)^2,
 S_F,t(1)=(16/11)cos(phi).

These are finite cosine polynomials, realized by S(t)=1+(t-1)S_t(1), or any cubic spline with the same endpoint jet. The representation then has a2=A2 and b2=B2 exactly. Its own-coefficient discrepancy is zero.

For the source leading vorticity r^(-1/3)sin(phi), u_sr=9cos(phi)/16 and u_sphi=-15sin(phi)/16. Hence

 Am=-(207/256)sin(phi)cos(phi),
 Bm=-(153/128)sin(phi)^2 cos(phi),

both nonzero. Their powers are-7/12 and1/6. The represented own ladder has Omega powers-1/4-j/4 and Theta powers1/2-j/4, j nonnegative integers, with additional radial corrections of integer multiples of2; neither mixed power occurs. At these powers no own interaction, temperature forcing or constant velocity term collides. Thus the mixed residual is nonzero despite exact agreement with both own next-order coefficient relations. This example concerns tail consistency, not a smooth normalized B2 profile. It suffices to refute the claimed logical necessity of the observed near100percent mismatch.

## Scope and dependencies

All coefficient deductions are formal homogeneous algebra, or actual asymptotic deductions conditional on differentiable expansions with the stated absence of colliding powers. The explicit tail example is smooth on r>0; no global profile is asserted. Finite angular quadratures below check saved field coefficients using independent endpoint extraction and a different angular grid. They do not validate window regressions, exact equation solvability, certified error bounds or the full nonlinear forced problem. Dependencies: elementary polar calculus, one-sided Taylor expansion and finite trigonometric product identities.
