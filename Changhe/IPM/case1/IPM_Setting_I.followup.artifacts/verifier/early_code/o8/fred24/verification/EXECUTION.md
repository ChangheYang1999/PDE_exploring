# Verification and execution record

The work was an analytic audit of the supplied local proofs. We checked the differential, the finite-part subtraction, source quotients, reconstruction constants, tail constants, Cauchy bounds, counterexamples, reference supremum bounds, parameter-integral majorants, and the logical use of the supplied PDE implication.

The only substantive local numerical computation needed for the conclusion was an exact-rational recalculation after correcting the norm convention. The script in `../02-remainder/verification/norm_repair.py` reads the original scalar certificate, removes its `__main__` block, replaces exactly the three origin perturbation constants, and evaluates the resulting certificate. It does not write into the original workspace. Its `Fraction` assertions check the strict exclusion budget for all three simple radii. The output is `../02-remainder/verification/norm_repair.json`.

This is a reuse of audited scalar arithmetic, not a second independently implemented quadrature or numerical reconstruction. The final decimal values of B and its directional derivatives were outside the requested arithmetic audit and were not recomputed.

Reproduction command, from this workspace:

```sh
timeout 540 env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 answer/02-remainder/verification/norm_repair.py
```

The process imposes a 1.9-billion-byte address-space limit. Computation was local and single-threaded. No GPU, JavaScript/TypeScript tooling, server, listener, or RLScience-cluster access was used. All created files are under this workspace's `answer/` directory. The original report and original answer were not modified.

## Requested Claude collaboration

We attempted the permitted Python client using the existing boto3/Bedrock configuration. The active profile was `cline-profile`, region `us-west-2`. Credential retrieval failed before model discovery:

```text
CredentialRetrievalError: Error when retrieving credentials from Ec2InstanceMetadata: No credentials found in credential_source referenced in profile cline-profile
```

No inference model was invoked. Claude Opus 5.5 availability could not be confirmed. No substitute model was used. The analysis and repaired bounds should not be described as having received an Opus review.

## External reference check

A primary-source search on finite-part analytic continuation was made as a background check. No external theorem from that search is needed for the result: the finite-part definition, differentiation rule, integrable majorants, and absence of boundary constants are proved explicitly in this answer. The supplied local PDE implication remains the only unproved PDE input.
