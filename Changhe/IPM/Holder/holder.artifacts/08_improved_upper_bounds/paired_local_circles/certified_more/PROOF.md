# Three further paired-local-circle upper bounds

For the real Euclidean homogeneous Holder seminorm on R^2, with operators
and compact smooth test supremum as defined in ../../../01_setup/PROOF.md,

    C_(3/10) <= 2.7748077123,
    C_(3/4)  <= 2.6442935978,
    C_(9/10) <= 5.0137426873.

The same constants bound T_xx and T_xy. These are certified upper bounds,
not asserted exact norms. No new bound for R_1^2 is claimed here.

## Proof

Apply the paired local-circle theorem ../PROOF.md with delta=1/64,
512 angular cells per circle, 256 radial intervals, and the 17 phases
j*pi/32, 0<=j<=16. Use the already audited middle-circle and exterior-circle
bounds on the same phase grid. Their sum covers the whole plane. The two
small disks are bounded by

    S=2*a_2(alpha)*delta^alpha/alpha
      +(1+2*delta)^alpha*delta^2/(2*(1-delta)^2),
    a_2(alpha)=2^(1+alpha/2)/(pi*(alpha+2)).

The remaining phase-grid maximum is multiplied by sec(pi/64), as in the
local theorem. No extra cross-disk term is added: it is already present in
the exact paired local-circle density.

The new implementation shares the exact integer flow plans across the
three exponents. This is legitimate because an admissible transport plan
does not have to be optimal. Every flow is nonnegative and every marginal
is checked with exact integer arithmetic. The plan's ordering uses only
Euclidean distance, whose order agrees with its positive alpha powers.
Same-circle edges with the same circular index distance k have the same
certified chord bound 2*sin(pi*min(k+1,256)/512). Summing their integer
masses before multiplication by this cost leaves the exact cost unchanged.
Opposite-circle distances are separately enclosed on each angular product
and at both radial endpoints. The unassigned variation is transported to
its antipodal copy as in the original proof.

The two radial chunks for each alpha cover rows 0 through 255 exactly
once at every phase. The merger checks this coverage and all source
hashes. An independent 90-decimal computation of adverse input endpoints
gives, respectively,

    2.7748077122371975546310730905897626754969584265...,
    2.6442935977670703615149429514531714778975101186...,
    5.0137426872952893321797759044826610065403189972....

Each is below the stated upward-rounded decimal. Independent checks of
96 grouped costs against the original edge-by-edge formula pass, and a
whole alpha=1/2 phase agrees with the earlier implementation. The exact
marginal checks, analytical cost bounds and outward arithmetic supply the
certificate; floating candidate ordering is not used as mathematical
proof of optimality. All inputs are hashed in verification/manifest.json.
