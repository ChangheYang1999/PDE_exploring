"""Record the final manual review of multipoles and convergence criteria."""
from pathlib import Path
import json, sys
sys.dont_write_bytecode = True
from certificate_admission import stamp, ref, next_entry
from reconstruct_text_delta import reconstruct
base = Path("research/301_final_claim_audit")
paths = [
 "research/08_interior_multipoles/PROOF.md",
 "research/20_canonical_extension/PROOF.md",
 "research/58_free_multipole_convergence/PROOF.md",
 "research/62_analytic_multipoles/PROOF.md",
 "research/17_log_gevrey/PROOF.md",
 "research/73_improved_gevrey/PROOF.md",
 "research/41_joint_log_potential/PROOF.md",
 "research/93_stream_convergence_characterization/PROOF.md",
 "research/94_positive_measure_stream_converse/PROOF.md",
 "research/95_sharper_log_radius/PROOF.md",
 "research/98_density_stream_equivalence/PROOF.md",
 "research/99_density_pointwise_criterion/PROOF.md",
 "research/100_irrational_conditional_criterion/PROOF.md",
 "research/101_local_integral_criterion/PROOF.md",
]
for p in paths:
 assert Path(p).is_file(), p
ledger, text = next_entry(659)
now = stamp()
review = f"""# Final review of multipoles and conditional convergence criteria

Recorded {now}. This is a manual mathematical review of the fourteen complete proof texts hashed in admission_V659.json. The numerical examples and finite check counts quoted in those proofs retain their earlier admission scopes; they have not been replayed in this review.

## Interior and exterior are different conclusions

The compact-density stream moments have the negative sign in topic 08. The first harmonic stream requires a logarithmic potential; the higher stream multipoles have the stated harmonic potentials. For a different interior density, the mismatch moments are those of its difference from a reference extension whose exterior stream agrees with the prescribed series. They are not simply the moments of the new interior density.

The cutoff-potential construction in topic 20 commutes the derivatives to give the canonical whole-plane Poisson relation. Its source has growth r^(gamma-1), and the reflected Green kernel cancels its constant and linear far-field terms. The radial tail is bounded by a constant times r^(gamma-2), integrable because gamma < 1. Rescaling the near region gives stream growth O(r^(gamma+1)), hence o(r^2). The difference of two such whole-plane streams is an affine harmonic function; oddness in each coordinate makes that affine function zero. The construction therefore gives a canonical smooth extension with compact stationary residual. It does not prove that this residual vanishes inside the cutoff disk.

## Prescribed multipoles

The mixed-index linear denominator is c((n-1)delta+2k), positive at every generated index except the prescribed leading input. The sum of child indices gives the correct radial exponent. No density input has n=0, and no input has k=1, so no k=1 coefficient is generated. An independent harmonic stream changes later density coefficients even though its own density is zero.

A small divisor belongs only to a generated velocity child. Contracting interactions with independent multipoles leaves n-1 such marked nodes for a tree with n leading-density leaves; adding the output divisor gives n marks. Properly nested marks have strictly decreasing positive density mass because each marked child has a right density sibling. The continued-fraction packing estimate counts those density leaves, so arbitrary zero-mass multipole leaves do not invalidate it. The positive quadratic majorant is permitted to count extra tree shapes.

In the analytic-data extension the shrinking-strip power is n+k-1. The angular stream derivative introduces a linear weight and one existing divisor, without a new divisor. The independent multipole norm includes both its angular exponential and sigma_0^(k-1). The rescaling is x/s, y/s with s=sigma_0/2. The apparent prefactor 1/x is evaluated at the initial exterior radius through the actual monotone weights x^(n-1)y^k; it is not bounded separately as r tends to infinity. The restriction on Y gives a strict convergence margin for independent multipoles too. Early exceptional potential inverses use a smaller strip; their finite number causes no change in the all-order conclusion. Both multipole theorems remain local exterior results under a finite Brjuno sum and geometric multipole growth.

## Logarithmic growth and the common potential

The rational Gevrey estimate uses factorially weighted log coefficients and their degree bound. Its normalization controls the convolution binomial factors. The improved exponent follows from the refined degree bound and D_n! <= (n!)^sigma. Either estimate is an upper bound and does not prove divergence. A factorial inverse for an arbitrarily chosen polynomial forcing is not an example from the generated stationary sequence.

The joint potential reconstruction uses the Euler identity for Y=partial_y chi and both the density and stream coefficients. For large X=n delta the two scalar Euler factors are separated from zero by a fixed fraction of X. The downward angular primitive is uniformly bounded at negative degree. In the polynomial-log case the holomorphic resolvent estimate controls the finite derivative expansion; the ratio is strictly below one. This avoids an extra exponential loss from reconstructing the potential. Finitely many early logarithmic corrections are treated separately.

## Coefficient and pointwise criteria

Geometric stream coefficients imply geometric density coefficients through a positive convolution recurrence. The smaller root of K y=(1-y)^2 normalizes its total convolution mass to one. Conversely, at sufficiently large order, a weighted top harmonic of the nonzero finite leading profile gives a coercive estimate for the interaction of that profile with the unknown stream. Lower harmonics and the lower-frequency branch are absorbed using rho >= 4 and their normalized sum at most 1/16. The log derivative is absorbed by the degree bound. Isolating this interaction leaves only earlier stream orders and yields a convergent scalar renewal bound. This is a statement about the generated stationary sequence. It asserts neither a uniform ratio N_n/M_n nor equality of their limiting growth bases.

Positive-measure boundedness is converted first to a uniform bound on a positive-measure subset, then to angular and radial coefficient bounds. Separated interpolation nodes exist in measurable sets without interior. The angular Lagrange estimate is exponential in angular degree, and the polynomial estimate is exponential in log degree; both degrees are linear in n. Fubini supplies a positive-measure set of radial slices with a uniform lower bound on angular slice measure. These facts give a geometric coefficient bound. The argument applies separately to density, stream, radial velocity, and the stated common potential.

The contraposition gives unbounded individual terms almost everywhere and on a dense residual set if there is no geometric coefficient bound. It does not give divergence at every point: symmetry lines may have identically zero terms. For irrational parameters there are no log factors; applying the one-circle argument at countably many integer radii gives a single full-measure residual set of angles for a fixed parameter and leading profile. Radial scaling then gives unbounded terms at every positive radius on each of those rays. No common exceptional set for uncountably many parameters is asserted.

For local L^p criteria with p > 0, Chebyshev on each finite-measure rectangle produces the positive-measure bounded subset needed for interpolation. The argument does not use a norm triangle inequality when p < 1. Failure of a geometric bound forces an infinite limsup of nth roots of local term sizes; it need not force those nth roots to tend to infinity. The sharpened physical radius estimate retains the full factor A^n r^(-delta(n-1))(log r)^(kappa n) and a strict geometric margin. Its numeric examples are conditional on their explicitly stated all-order coefficient assumptions.

## Verdict

CONFIRMED for the arguments with the exact hypotheses and limits of the retained proofs. No new mathematical defect was found. In particular, the conditional logarithmic convergence criteria do not resolve convergence for the computed canonical logarithmic sequence, and the exterior theorems do not produce a whole-plane stationary solution. No new arithmetic replay, theorem, or complete reread of the assembled report is claimed.
"""
review_path = base / "sources/final_scope_chain_review_V659.md"
review_path.write_text(review)
protocol = """\n## Final exterior-scope and conditional-criteria reread protocol\n\nRead the complete current proofs of compact-density multipoles, canonical cutoff extension, prescribed multipole convergence, analytic multipoles, logarithmic Gevrey bounds, joint common-potential reconstruction, geometric coefficient equivalences, positive-measure and local-integral criteria, the sharper conditional logarithmic radius and the irrational ray criterion. Check signs, marked density mass, shrinking-strip powers, strict convergence margins, measurable-set interpolation and exact quantifiers. Preserve the distinctions between exterior and global stationarity, conditional criteria and established convergence, and limsup and limit.\n"""
with (base / "PROOF.md").open("a") as f:
 f.write(protocol + f"\nCompleted {now}, V659. All fourteen reviewed proof texts pass. No new mathematical defect was found; no new theorem or numerical certificate is introduced.\n")
proof = base / "sources/PROOF_at_V659.md"
proof.write_bytes((base / "PROOF.md").read_bytes())
algorithm = base / "sources/admit_final_scope_chain_review.py"
algorithm.write_bytes(Path(__file__).read_bytes())
snapshot = base / "verification/post_freeze_20261031T235941Z/theory.json"
assert reconstruct(snapshot) == Path("../a4-lead/FARFIELD_CONVERGENCE_THEORY.md").read_bytes()
result = "Fourteen complete proof texts were reread. The multipole signs and tree marks, canonical extension and compact residual, shrinking-strip and common-potential bounds, Gevrey upper estimates, density/stream equivalence, measurable-set interpolation, local Lp and irrational ray criteria retain their stated scopes. No new mathematical defect was found. The lead theory remains identical to the reviewed 23:59:41Z snapshot."
scope = "CONFIRMED for this manual mathematical review under the exact hypotheses of the retained proofs. No fresh numerical replay, new theorem or complete assembled-report reread is claimed."
p = base / "verification/admission_V659.json"
p.write_text(json.dumps(dict(at=now, entry=659, verdict="CONFIRMED", review_kind="manual mathematical reread, not a numerical replay", reviewed_proofs=[ref(p) for p in paths], review=ref(review_path), proof=ref(proof), algorithm=ref(algorithm), theory_snapshot=ref(snapshot), result=result, scope=scope), indent=2) + "\n")
ledger.write_text(text + f"\n## V659 | {now} | Final reread of exterior scope and conditional convergence criteria\n\n**Claim.** The multipole and conditional convergence proofs retain their exact hypotheses, quantifiers and limits.\n\n**Method.** Complete manual reread of fourteen proof texts with a written account of the delicate estimates; compare the lead theory by exact reconstruction.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {p}.\n")
n = Path("NOTES_FOR_TEAM.md")
n.write_text(f"## {now} VERIFIER -> LEAD: V659 exterior-scope and conditional-criteria reread passes\n\n{result}\n\n{scope}\n\nThe additional rereads in V657-V659 now cover forty-one proof texts. No new report correction is requested. The logarithmic all-order hypotheses and whole-plane stationary extension remain open exactly as stated.\n\n" + n.read_text())
with Path("WORKLOG.md").open("a") as f:
 f.write(f"\n{now}: V659 records the final manual reread of fourteen multipole, exterior-scope and conditional-criterion proof texts. No new defect found; no arithmetic replay claimed.\n")
print(now, result)
