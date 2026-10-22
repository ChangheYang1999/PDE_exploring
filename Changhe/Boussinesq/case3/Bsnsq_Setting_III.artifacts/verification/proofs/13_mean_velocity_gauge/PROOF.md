# An explicit averaged-velocity convention for a power-decaying vorticity class

Status: proposed canonical observer convention, with complete mathematical derivation. It is not yet the lead's selected convention. It changes no relative transport equation. It is not an existence result.

## Statement

Let Omega be smooth, odd in x, and uniformly O((1+r)^(-delta)) for some delta>0. Let V be the canonical relative whole-plane inverse from research/03_inverse, with V(0)=0. Fix ell>0 and the radial probability density

    eta_ell(Z) = exp(-|Z|^2/ell^2)/(pi ell^2).

Define

    C_ell(Omega) = integral eta_ell(Z) V(Z) dZ,
    U_ell(X) = V(X)-C_ell(Omega).

Then U_ell is a well-defined sublinear whole-plane div-curl velocity, unique among such velocities satisfying integral eta_ell U_ell=0. It has the required parity and generally nonzero center velocity

    v0_ell = U_ell(0) = -C_ell(Omega).

This is a prescribed spatial-average convention, not the condition U(0)=0 and not a fitted drift. Its vertical value must be computed from the density and convention. The relative field U_ell-U_ell(0) remains exactly V.

## Proof of existence and uniqueness

The relative-inverse theorem gives smooth V of at most sublinear growth, so its Gaussian average converges absolutely. Subtracting its average preserves div U=0, curl U=-Omega, and sublinear growth, and gives the stated zero average. By parity V_1 is odd in x while V_2 is even; hence C_ell has zero horizontal component. All required velocity parity follows.

Any other whole-plane sublinear velocity with the same div-curl data differs from U_ell by a constant vector, by the harmonic Liouville argument in research/03. If its same weighted average vanishes, this constant is zero. Thus the convention fixes the complete velocity without an extra harmonic strain or arbitrary fitted parameter.

## Relation to the ordinary convergent inverse

If the ordinary Biot-Savart velocity U_BS is defined, then V=U_BS-U_BS(0), and

    U_ell = U_BS - integral eta_ell U_BS.

Thus this convention is generally a different observer representative even when the ordinary integral converges. The positive-vorticity ordinary-center sign formula must not be silently transferred to this representative. One may select the ordinary inverse on its convergent subclass and use a declared averaged convention on a divergent-tail subclass, but that piecewise selection would itself need to be specified. The physical reconstruction with any selected constant requires translating theta and omega along with the observer velocity, as proved in research/07. It is incorrect to add a uniform velocity to unchanged physical scalar fields.

As a simple example, take Psi=x(1+y)exp(-r^2), whose ordinary center velocity is (0,1). Direct Gaussian integration gives

    integral eta_ell U_BS = (0,(1+ell^2)^(-2)),
    v0_ell = (0,1-(1+ell^2)^(-2)).

The horizontal mean and odd-y part of the vertical mean vanish by parity. For the remaining integral, set a=1+ell^(-2) and use integral exp(-a r^2)=pi/a and integral x^2 exp(-a r^2)=pi/(2a^2). This verifies a nonzero center velocity in the averaged convention. This manufactured field is not a B2 solution.

## Scaling and a choice without an independent length parameter

Under the exact signed scaling Omega_lambda(X)=Omega(X/lambda), the canonical relative velocity obeys V_lambda(X)=lambda V(X/lambda). If ell_lambda=|lambda| ell, change variables Z=lambda Y in the Gaussian average to obtain

    C_(ell_lambda)(Omega_lambda)=lambda C_ell(Omega),
    U_(ell_lambda)[Omega_lambda](X)=lambda U_ell[Omega](X/lambda),
    v0_(ell_lambda)=lambda v0_ell.

A fixed numerical ell would not remain the same convention under spatial scaling; this transformation must be recorded. In the B2 class b0=Omega_x(0)=4a0/beta is nonzero. Choosing ell(Omega)=1/|b0| gives ell(Omega_lambda)=|lambda|ell(Omega), so the resulting convention respects the exact scaling without an extra fitted length. This last selection is nonlinear in Omega because its averaging radius depends on the center derivative. It is a gauge-fixing rule, not a claim that the linear div-curl inverse itself is nonlinear.

## Scope and acceptance question

The prompt permits an advertised regularization and demands that no unannounced uniform velocity be appended. This construction makes the constant explicit, computable and unique under its stated average condition. Whether to adopt this observer convention is a specification choice owned by the lead. No current candidate is accepted with it, and it does not resolve the broad-class inverse for polynomially growing densities lacking uniform decay. In all cases the difference between observer choice and the physical B1 condition must remain explicit.
