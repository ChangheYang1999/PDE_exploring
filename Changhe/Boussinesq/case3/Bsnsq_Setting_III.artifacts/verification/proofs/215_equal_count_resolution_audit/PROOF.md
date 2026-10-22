# Equal-count refinement, stored-field residuals, and the limits of plateau evidence

## Exact statements and scope

Fix beta>0, a0!=0 and an external whole-plane source f. The numerical forced transport field is W_f=beta X+U_rel[Omega]+lambda U_rel[f], where U_rel[V](X)=U[V](X)-U[V](0), and U=(-Psi_y,Psi_x), -Delta Psi=V. The defining B2 problem instead has W=beta X+U_rel[Omega]. This packet compares three stored forced approximants after the same finite number of reported inner-map evaluations. Neither finite-array statistics nor a small forced residual proves a solution of B2. Every comparison below is finite and pertains to the exact named archives and the stated sampling scheme.

The following elementary conclusions determine the audit.

1. Equal evaluation count removes the specific confounder of one run receiving more map evaluations. It does not equalize arithmetic work, wall time, quadrature accuracy, or proximity to the minimum residual of a representation. A simultaneous change of angular basis and angular fit quadrature tests the combined change.
2. If obj is the sum of squared values of two envelope-weighted residual components on N sites, obj/N is the mean squared Euclidean residual vector and sqrt(obj/(2N)) is the root mean square per scalar component. It is not a physical integral without a specified physical quadrature measure. Values at different site sets are not common-point residual comparisons.
3. To say that a sequence O_j stays within epsilon of its last value O_n from evaluation k onward requires |O_j/O_n-1|<=epsilon for EVERY j in {k,...,n}. A first crossing of that threshold does not prove the suffix condition. If O_n=0, use absolute values with an explicitly chosen absolute tolerance instead; the archives here have positive objective values.
4. A finite small coefficient defect and nearly constant objective do not establish a representation-imposed residual floor, nor a distance to a fixed point. The exact origin constraints and any nonzero asymptotic residual coefficient independently disqualify literal fields regardless of that objective.

These claims are statements about inference and exact identities, not a continuum nonexistence result. No formalization is attempted. The numerical evaluator is independent of NUM: SciPy reads the saved basis, an adaptive physical-radius full-plane Green inverse supplies velocity, and seven-point Cartesian differences differentiate the saved fields. Earlier manufactured tests of these modules remain their validation evidence; new data are checked separately.

## Proof of the comparison and plateau claims

The first three claims follow from their definitions. In detail, if r_i=(r_F,i,r_G,i), then obj=sum_i(|r_F,i|^2+|r_G,i|^2). Dividing by N averages the squared vector norm, and dividing by 2N averages the 2N scalar squares. Unless the weights and sites are a quadrature for a named measure, no integral identity follows. The suffix condition in item3 is a conjunction and is tested by a reverse cumulative maximum of |O_j/O_n-1|.

For item4, take any epsilon>0 and 0<eta<1, and let a scalar fixed-point map be T(x)=(1-eta)x, with x0=1 and objective O(x)=epsilon^2 x^2. Its fixed-point defect is eta |x|, which can be arbitrarily small at x0 while the distance to its unique fixed point zero equals1. Its iterations are x_j=(1-eta)^j and O_j=epsilon^2(1-eta)^(2j). For any fixed N and tolerance delta>0, choose eta small enough that (1-eta)^(-2N)-1<delta. Then every one of the first N objectives lies within relative delta of the last, yet O_j tends to0 as j tends to infinity and the representation admits zero objective. This example is only a logical counterexample to inferring a floor from finite plateau data. It says nothing about the eventual behavior of the tested Anderson runs.

A small fixed-point defect also need not imply existence of any fixed point: T(x)=x+epsilon has defect epsilon everywhere and no fixed point. These elementary examples explain why the report must call the values finite-iteration diagnostics. They do not refute numerical improvements actually observed at equal count.

## Defining residuals, parity removal and origin tests

Write Theta=x^2 F, Omega=xG, W=(x A,B), with A=beta+U_rel,1/x and B=beta y+U_rel,2 off the axis, extending A continuously on the axis by beta+partial_x U_1. Product differentiation gives

 R_Theta=x^2 R_F, R_F=A(2F+x F_x)+B F_y-(beta-2)F,
 R_Omega=x R_G, R_G=A(G+x G_x)+B G_y+G-(2F+x F_x).

These identities prove the divided-axis formulas by smooth continuity and the off-axis equality of the two normalized ratios when each normalizer is the sum of the corresponding absolute terms. Direct Cartesian finite differences give an independent numerical comparison of the factored and unfactored formulas; their floating difference is a diagnostic rather than an exact error enclosure. At the center B=0 and A=beta-c, c=Psi_xy(0). Thus

 R_F(0)=[beta+2-2c]a0,
 R_G(0)=[beta-c+1]G(0)-2a0.

For a smooth exact profile with a0!=0, R_F(0)=0 forces c=1+beta/2, and R_G(0)=0 then forces G(0)=4a0/beta. In the forced equation replace c by c+lambda c_f. Consequently a certified nonzero center mismatch or divided-center ratio rejects the literal represented field. It does not exclude another nearby field. Native source f retains its own seed exponent and geometry in the inverse; it is not retied to the unknown beta.

All pointwise normalizers use sums of absolute equation terms. Zero divided by zero is reported as0; a positive numerator divided by zero is infinite. There is no denominator floor. Samples on both sides of x=0 and on both half-axes check the stated one-axis reflection, without adding any y reflection or boundary. The physical origin is tested by exact certificates, not inferred from a nearby sample that already contains a vanishing parity factor.

## Full-plane inverse and tail rejection

The relative modal inverse used here is the once-subtracted whole-plane inverse established in research/63_adaptive_fullplane_inverse/PROOF.md and the inverse modules' manufactured tests. Its radial integrals go to infinity and keep the source in its original basis. It introduces no arbitrary harmonic strain, uniform relative drift, wall image or finite-box Dirichlet datum. Independent Cartesian Duffy quadrature in the prior inverse tests checks the same full-plane kernel by a second discretization. This packet does not turn the adaptive quadrature's reported estimates into rigorous bounds.

For tails, the exact rational archive checker derives radial expansion coefficients from the binary coefficients and regenerated knots. The relevant implication is elementary: if at a fixed angle R_Theta(r)=a r^p+o(r^p) with p>0,a!=0, then |R_Theta(r)|>=|a|r^p/2 for all sufficiently large r and its full-plane supremum is infinite. If several distinct powers occur, take the largest nonzero exponent; lower powers cannot cancel it. The archive-specific derivation, exact rational witnesses, and inverse constants are dependencies recorded in research/89_exact_serialized_tail_residuals/PROOF.md, research/101_native_source_mixed_powers/PROOF.md, research/111_higher_inverse_constant_certificate/PROOF.md, research/160_exact_center_strain/PROOF.md and research/163_exact_center_residual_lower_bounds/PROOF.md and the actual generated certificate inputs. Their paths are verified before publication. Importing an archive is not proof; each certificate must pass its separate arithmetic checker.

A finite residual table through r=1e8 is therefore only a table on its sampled set. If a checked positive-power witness exists, the global absolute thermal residual is infinite even when the tabulated normalized ratios are small. The forced and unforced witnesses are evaluated separately. Center and tail failures reject the named C4 spline approximants; they do not rule out convergence to a smooth solution after modifying the fields or their tails.

## Planned reproducible checks

Read and freeze the three run logs, shell launch text and start/end archives; parse exactly the reported map evaluations and convergence flags; independently compare the input physical fields rather than assuming transplants preserve them; recompute objective normalizations and persistent plateau indices. Then evaluate all three final archives on the same physical radius/angle rule with the independent inverse and differentiation. Archive tables distinguish self B2 and forced transport, Cartesian and divided residuals, absolute and pointwise normalized maxima, the six radial bands, both finite-difference steps and all adaptive quadrature failures. Exact center and tail inputs are registered alongside them. No numerical result is asserted in this proof before execution.
