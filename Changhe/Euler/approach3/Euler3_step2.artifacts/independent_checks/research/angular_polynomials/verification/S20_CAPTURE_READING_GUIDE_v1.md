# S20 captured all-order angular tables


## V320. Complete captured S20 primal closure tables

Date: 2026-10-29T13:53:36.608614+00:00.

Claim: the two remaining S20 closure value/gradient/Hessian tables satisfy the registered finite G5(c) comparison.
Method: independently generate all361real modes through18 on the exact924captured nodes from rational Cartesian harmonic polynomials at70Decimal digits with80-digit normalization, checking three full-node jets against a separate normalized recurrence at1e-55. Store high/low reference words and measured serialization remainders. Compare all13components entrywise, with directed numerical triangle bounds and degree/order floor1e-13 of the largest reference magnitude. These finite computations are not rigorous interval enclosures.
Result: 116 controls PASS. call01: 2918916 entries, 0 failures, largest normalized error bound 1.10937505391e-16.
call06: 4336332 entries, 0 failures, largest normalized error bound 1.10937505391e-16. Reference NPZ RUN_ROOT/verifier/artifacts/allm_closure_reference_v1/closure_all361.npz SHA256 f97c5d80e0e4611c2471ca08ce16c8c91aeadda5281537d11437d041941b9968; reference record SHA256 958629db8bc5fcab7d49e1eca60f8322774624992678d59b8fa777bc19bcf5a2. Comparison SHA256 3e15b68760452c0e5e12773488bf0619e4d5b926369a1ab2b426331701b98121. Reference program78.49980348s; comparison10.238231681s, completed2026-10-29T13:53:00.046896+00:00. All reference mixed partials are equal. Production mixed partials have maximum absolute asymmetry7.70371977755e-34; both orientations independently satisfy G5(c). The earlier extra bitwise-symmetry assertion failed and was replaced by this explicit diagnostic, preserving all registered comparisons.
Verdict: **CONFIRMED** for both finite primal closure sets. Together with V317 this covers all seven captured primal table sets. Counts overlap across sets. Exact bitwise Hessian symmetry is **REFUTED** for this capture and is not a G5(c) requirement.

## V321. Captured S20 Jacobian angular-table argument reuse

Date: 2026-10-29T13:53:36.608614+00:00.

Claim: the three unconverted angular-table calls during the captured physical-c_l JVP reuse independently checked primal arguments with sufficient derivative order.
Method: source-review recorder v2, bind every producer source and indirect DD harmonic module, check identical v1/v2 primal NPZ SHA256, match call metadata and source-reviewed torch.equal witnesses, and require each recorded covering derivative order to be at least the requested order. Eight negative fixtures reject incomplete coverage.
Result: 96 controls PASS. The JVP calls map to call01(L15,243modes,order2), call05(L18,361modes,order0), call06(L18,361modes,order2). The12primal calls deduplicate into seven sets; all three JVP calls have sufficient recorded matches. Audit SHA256 8cf31d13d55a936bef8eddaebd18a0a6f1b13492f7eac6e89ff1a611c8662c8a; elapsed1.359964348s, completed2026-10-29T13:53:01.474248+00:00.
Verdict: **CONFIRMED** for the source-reviewed argument-coverage claim on this CPU S20 capture. Wrapped tensor bytes and JVP tangent values were not independently measured. This is not an assertion about unobserved GPU coordinates, other configurations or branches. Code-level all-m table accuracy at the captured nodes is complete.

Read the angular_polynomials/PROOF.md first, then the reference and capture plans. These verdicts check finite table arithmetic, not an Euler solution.

## V325. Transfer to the recorded CUDA capture

At 2026-10-29T14:06:51.005252Z, 484 controls confirmed that the complete GPU NPZ has the identical SHA256 to the CPU NPZ: 8ccb35cb6d296a48af8c71e4dbf07f43b5b882e77a18a076d16a0a980309c3e3. The seven primal sets are therefore bitwise identical; three recorded GPU JVP calls also match covered arguments with sufficient derivative order. V317/V320/V321 apply to this recorded CUDA S20 configuration. Audit: ../../../artifacts/allm_gpu_capture_audit_v1/audit.json, SHA256 22b6876d02b7cdbab32db225755fb17fba288dede65edaa2b16cabce9b528a8e. JVP tangent values and wrapped tensor bytes were not measured independently, and other branches remain outside this finite capture.
