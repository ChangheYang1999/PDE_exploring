# Independent finite-kernel audit

Verdict: **PASS for the mathematical and numerical kernels in the bound snapshots below.** This review does not assert complete radial coverage or a final whole-plane norm before every regional certificate is assembled.

The review inspected both angular encodings, the complete Arb Taylor construction, the source-derived complex majorant, the L2 integrand polynomial, its analytic remainder, and the positive high-order modal energies. It uses no inherited residual norm endpoint.

## Bound program and evidence snapshots

| File | SHA256 |
|---|---|
| `finite.py` | `2af2484dd24a29af8ab623eb06514076dd41466c4ad58da7948163e35ce9d77a` |
| `finite_fast.py` | `71d83b6868df9723c91e5486f7bcb59904c20c117e393c703d9c73d89642b912` |
| `run_finite.py` | `afec6d19687fbdb8ff8c155f5b0235c1fb7b675ddffd370d9c156405488f6abb` |
| `run_finite_legacy.py` | `8dbcce218e5e34191a3c388f3b728a9b0a907154b23e7dfcbfd797ab42e016f7` |
| `high_order.py` | `79924a482cb8d68f387f817fe45d8f0f8e1fea69ccab8f432e232e0d1e41651c` |
| `FINITE_METHOD.md` | `3dba5e244bf88561db4ac4a8d6d63513c61e26cba02167aaf89be4c077e49c86` |
| `audit_fast_encoding.py` | `e227b04f303790fdc6f7480e6b62f061f190c05786f6303d4499a34b69aa918b` |
| `fast_encoding_exact_audit.json` | `4caa884012ea3f60edc4c67a362465bea0ad059daf7169f5d507e9dc842364d8` |
| `convolution_crosscheck.json` | `6f5b5aab7906c85a4e324c6e700dc401e43069752e5771b473a266d9f7a4907c` |
| `fast_convolution_crosscheck.json` | `f444b115af46526ff6d150292fcf5e006579495cf349e58a37f8afc2ba4c8e98` |
| `independent_modal_check.py` | `2bc5653fd1d9faf7c46cae19162fc48b7f180b2ca7d4bf5ceea1dcb3cc6b9136` |
| `independent_modal_check.json` | `33fd1defdcd1b8a04cda0c37c6a637dee5f167c39a0707629e251d698f5b86b2` |

## Mathematical checks

1. For the outer disk of radius c/4, minimizing Re(z²) on its boundary gives 9c²/16. Every t+z² stays in the open right half-plane. The polynomial Mobius displacement and both A_t/its-reciprocal displacement estimates in FINITE_METHOD.md have the correct denominators.

2. With n=2k+eps and alpha=b+k−v, the joint factor identity z^n(1+z²)^b(t+z²)^(−v)=z^eps Z_1^k(1+z²)^alpha A_t^v holds exactly. The noninteger power has one analytic branch; all other introduced powers are integer. The negative-alpha and negative-v branches use the appropriate lower modulus and reciprocal bounds. No factor was dropped.

3. Direct inspection of the exact source specifications gives maximal polynomial degree25 for Candidate007 and24 for Candidate013. The global series cap≥30 therefore suffices to compute the complete finite shift P(z0+w) in improved_majorant; no high polynomial coefficient is silently truncated.

4. Cauchy differentiation on the nested disks gives a! M/(D−R)^a, and polar inverse powers use |z|≥c−R. Summing absolute rational polar coefficients gives a genuine angular coefficient l1 majorant. Applying Cauchy coefficientwise and summing inside the contour integral establishes the common l1 residual Taylor tail H q^(K+1)/(1−q). There is no missing angular-mode multiplicity.

5. Every nonlinear product is cosine×sine. The suppressed 1/i convention for sine Laurent coefficients is therefore consistent. The legacy angular shift and stride2K+1 encode every degree≤2K product without carry. For the compressed layout, input exponents have one fixed parity, so (shift+n)/2 is an integer. Their sums have index (odd_shift+even_shift+n)/2, exactly the extraction index in finite_fast.py. Both angular endpoints and every radial product slot are included.

6. An additional independent Fraction Laurent/radial multiplication checked640 coefficient slots, including all radial degrees through2K, both permitted parity products, and degree0,1,4,9 with dyadic scaling. All exact coefficients belong to the Arb product enclosures. This is recorded by audit_fast_encoding.py and fast_encoding_exact_audit.json. The five-radius source checks and the independent Acb layout cross-check supply additional diagnostics; the proof of containment does not rely on sampling.

7. On a real panel, angular orthogonality gives pi∫r sum_n f_n² dr. The producer integrates the complete degree2K+1 polynomial, including all even coefficients and the correct factor2h pi/(k+1). The remainder estimate 2h pi(c+h)(2B delta+delta²) follows from absolute coefficient l1 bounds. Containing nondyadic centers and halfwidths introduce only extra Arb enclosure width. The validated degree-selection inequality, rather than floating logarithms used to guess K, controls the tail.

8. The positive local integer energies use actual (1−Delta)G and its gradient; they do not use a regional integration-by-parts identity. The n=1 zero angular harmonic has the correct factor through the sum of the two coordinate components. The supplied exact Cartesian polynomial test checks those modal identities independently.

## Provenance and assembly scope

run_finite.py labels new compressed panels with convolution_layout=parity_compressed. The preserved run_finite_legacy.py describes the older layout. Both snapshots must remain in the archive. A cached panel is read without a new source/code check by the worker, so the cache-hit path is not itself a provenance proof. The final assembly must check every exact panel index and endpoint and bind all raw bytes plus both producer versions in the final manifest. A missing panel prevents any whole-plane PASS. The portable manifest verifier checks byte integrity and source bindings; it is explicitly not a replacement for the numerical replay.

No mathematical containment error was found in the reviewed finite kernels. Later code changes fall outside these listed hashes and require an explicit diff review.
