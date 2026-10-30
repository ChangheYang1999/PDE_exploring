# Candidate 016 production: peer imports and independent numerical routines

## Exact scope and claim

This audit concerns the unchanged running source
../scaled_product_norms/code/production.py and the frozen first completed
checkpoint ../candidate016_scaled_norm_peer/source/N4_norms_partial_v01.json.
It clarifies software provenance; it proves no additional numerical norm.
The completed G0 and rF mathematical enclosures remain those of N4-341.

The production uses its own packed residual, derivative, squared-field
and positive-pole integration routines. Its point-calibration helper is
the own module ../n3_synthetic_field_audit/code/check.py. That helper also
imports frozen local N3 modules at initialization. Thus the literal claim
that no peer source is executed at all is false. The narrower statement
that no peer candidate field or norm routine is used in this production
has the source justification below. Execution from the original peer
lane is not involved: these modules are copied local audit inputs.

## Source-level argument

The production's P alias resolves to own packed.py, which loads the own
joint_scaled_factored_weak/code/fields_joint.py by explicit filename.
Its M alias loads the own rational_pole_moments/code/moments.py. Its C
alias loads the own Cartesian generator-jet module. Its H alias loads
the own synthetic helper by explicit filename and under a name different
from __main__. Inspect all H attribute uses in the complete production;
they must consist only of evaluate and direct_derivative. These two
functions have no references to N, LS or E and no dynamic module loading.
Their conversion ar is J.ar from the own rational-field module. Their
arguments are the own rational field objects and own Cartesian jet.
Their displayed finite sums, products, trigonometric powers and Leibniz
formula are the independently derived field-calibration formulas.

The synthetic helper's N and LS imports load local legqs_norms.py and
legqs_e2norms.py. These also initialize local e2norms.py and
legqs_integrals.py. Python executes their top-level imports, constant
assignments and definitions, even though their guarded main blocks are
not taken. This is already enough to disprove a literal no-peer-execution
reading. In particular legqs_integrals.py sets ctx.prec=512 at import;
the own helper later sets it to1536. Production's main sets ctx.prec to
the requested2048 after all these imports and before candidate assembly.
The invoked own arithmetic files do not subsequently change ctx.prec.
Consequently these initial defaults do not reduce the production's
working precision. The completed checkpoint independently records2048
and the passed1931-bit minimum Cartesian accuracy.

The own production computes F by P.residual, its derivatives by
P.all_derivatives, complete squared groups by its own normgroups and
all radial moments by M.integral. Its point comparisons use only the two
own H functions above and C.GeneratorJet. No peer field builder, peer
integral function, peer norm routine or saved peer numerical value enters
these candidate calculations. Peer source and fixture records are
hashed to bind the earlier calibration; reading their hashes and prior
fixture metadata is not using their numerical routines for this candidate.
The production's norm comparison with N3 is a later separate operation.

## Finite inspection and limitations

The checker parses the actual files without importing them. It records
all load calls, H attribute accesses, the selected helper function ASTs,
peer import edges, top-level initialization statements and all precision
assignments. It verifies the exact source hashes against the immutable
completed checkpoint and its fixture dependencies, checks the main guards
and rejects dynamic eval/exec/getattr/import calls in the selected helper
functions. These finite syntactic checks support the explicit source
inspection above. They are not a general Python program verification,
a runtime trace, or independent validation of the FLINT/Arb libraries.

Read the output flags together. frozen_peer_modules_imported_for_own_fixture_helpers
is true and peer_field_or_norm_routines_called is false. The flag
foreign_code_executed=false must not be quoted as absence of peer module
initialization. The correction is kept in this separate bound record;
neither the running source nor previously accepted checkpoints is edited.
This clarification changes no mathematical enclosure or peer-review status.
