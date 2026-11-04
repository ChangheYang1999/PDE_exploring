# The compact Lamb gauge does not preserve the refined energy law

Status: A372 CONFIRMED. This is a scope check on a reduced-equation gauge, not a new nonexistence theorem.

## Statement and exact hypotheses

Let 2/5<c<1/2, omega be any finite real number, a=1-2c, beta=5-2/c in(0,1), A=cI-omega J. Let U in C1(R3;R3) be divergence-free, tend uniformly to0, and have the refined energy law

    E_U(R)=integral_B_R |U|2=L R^beta+O(R^(beta-1)),     (1)

where L is a finite nonnegative constant. An actual Euler profile in the campaign class has this law by A040 and its refinements. Let F in C3_c(R3) with grad F not identically zero, and put

    v=U-grad F/a.                                     (2)

Then v has the same exterior field and leading coefficient L as U, and the same coarse bound E_v(R)=O(R^beta), but it cannot satisfy (1) with any leading coefficient. Precisely, for all R containing supp F in their interior,

    E_v(R)-E_U(R)=a^-2 integral_R3 |grad F|2>0.         (3)

If U is an Euler profile with B=Ay+U, Omega=curl U and aU+grad H=B cross Omega, then holding B and Omega fixed gives

    a v+grad(H+F)=B cross Omega, curl v=Omega.          (4)

Define the pressure reconstructed from this new Lamb scalar by

    P_*=H+F-|v|2/2-Ay.v.

The abstract helicity coefficient and its physical-pressure counterpart are related by

    R_abs=H+F-v.B,
    R_phys=P_*-|v|2/2=R_abs+v.grad F/a.                (5)

Thus the repaired abstract scalar system does not in general retain its physical coefficient. The gauge also violates div v=0 unless F=0. No statement that it preserves the entire Euler integral package is justified.

## Proof of the energy assertion

Since F vanishes outside a compact subset of B_R, ordinary integration by parts gives

    integral_B_R U.grad F=-integral_B_R F div U=0.

There is no boundary term. Expanding the square in (2) proves (3). Since beta>0, dividing by R^beta shows that any new leading coefficient is still L. But the remainder in (1) tends to0 because beta<1, whereas the energy difference is the fixed strictly positive number in (3). The two refined asymptotics cannot both hold. The same constant is O(R^beta), so the coarse growth upper bound is preserved.

This argument is specific to the target interval. At c=2/5 the leading energy constant itself may change. At c>=1/2 the stated remainder need not tend to0. Neither endpoint is asserted here.

## Proof of the scalar and pressure assertions

Because curl grad F=0, the curl in (4) is unchanged, and a v+grad(H+F)=aU+grad H. If f=grad F/a, then U=v+f and B=Ay+v+f. Consequently

    P_*-|v|2/2
       =H+F-|v|2-Ay.v
       =H+F-v.B+v.f,

which proves (5). Also div v=-Delta F/a. If v were divergence-free, F would be entire harmonic and compactly supported, hence zero by the maximum principle. This contradicts the nonzero-gradient hypothesis.

If the original physical coefficient is R=H-U.B=P-|U|2/2, then

    R_abs=R+F+B.grad F/a.

That is the scalar-gauge transformation in A322. The additional term in (5) is still needed to identify the physical pressure for v. It is the same carrier-consistency distinction as A333, now applied to the gradient gauge.

## Implication for the proof campaign

The report's claim that a compact F preserves far-field bounds is correct for the coarse growth bound and for pointwise exterior fields. It should not be enlarged to preservation of the refined energy expansion, the actual pressure coefficient, or every integrated Euler identity. The exact expansion supplies one further global check on a proposed reduced countermodel.

This observation does not exclude sign-changing helicity on a basin. A gauge model already fails incompressibility and carrier consistency. The independent B27 model has different properties and must be assessed by its own verified energy and residual formulas; (3) is not a statement about that model.

## Verification

No computation or external source is required. The source passages from the current coordinator report and coord_math are hashed in the team records. Equations(3)-(5) are independently derived here from the stated hypotheses. Exact scope is the hypothetical compact gradient perturbation, all finite omega, with no claim that a nonzero decaying Euler starting profile is known to exist.
