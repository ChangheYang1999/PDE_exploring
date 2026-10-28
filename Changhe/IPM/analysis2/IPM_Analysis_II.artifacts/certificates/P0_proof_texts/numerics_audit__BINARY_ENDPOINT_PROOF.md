# Independent certification of the exact binary annular endpoints

Status: CONFIRMED. The Q=4 refinement certifies all six exact binary numbers as strict lower bounds for their respective annular tests. The lower-bound comparison is independent of the producer implementation; the producer's internal machine-ball provenance is not claimed.

## Statement and test spaces

Let F be the actual unnormalized residual of exact original state131, with the canonical velocity and exponent. For C8 use the three compact tests and fixed weight of C8_PROOF.md; for C9 use the three weights and combined tests of C9_PROOF.md. Each test phi is a real compact C1 function in the homogeneous energy space, has the density parity, and its positive norm d=||grad phi||2 is given there exactly.

The producer's pair[m,e] denotes the rational number b=m 2^e. Its integer mantissa is parsed as an integer and its exponent as an integer; no floating-point conversion occurs. A claim b<=||wF||_(dot H^-1) follows if an independently certified pairing lower bound exceeds b d. Merely being an exact binary number does not establish that inequality.

## An extra exact binomial order

The original audit expands every radial potential to binomial order Q=3. Repeat the same independent reconstruction with Q=4, include every resulting residual sector of descendant degree q<=4 exactly, and bound all omitted terms by the same convergent majorant, now starting at binomial order5. The discarded finite quadratic sectors are also included in that error bound. The ratio and derivative-factor bounds in C8_PROOF.md hold for every omitted index a>=4, so in particular for every a>=5. The same proof therefore gives

    |F-F_4| <= B_4 r^(2gamma-1)

on the relevant exterior domain. No numerical approximation to the coefficient array is involved.

Use exact angular orthogonality and ball quadrature for the finite-sector pairing P_4=<wF_4,phi>. Integrate the positive radial majorant against the absolute angular test to get D_4>=|<w(F-F_4),phi>|. Thus

    (P_4-D_4)/d <= <wF,phi>/d <= (P_4+D_4)/d.          (1)

All lower comparisons are between finite Arb balls and the exact rational b. If the left side of(1) exceeds b, then the binary endpoint is independently certified. The published downward decimal and integer bounds are checked separately. As an additional consistency check, the independently retained Q=3 and Q=4 pairings obey |P_4-P_3|<=D_3+D_4, by their two proved error estimates. The exact gradient norm is unchanged.

## Provenance and limitations

The Q=4 calculations are refinements of the verifier's independent algorithm, not a third distinct implementation. Neither imports numerics code. The original read-only coefficients, producer bytes, proof files, implementation, and Q=3 audit used in the consistency check are hashed. Producer bytes are snapshotted and required not to change during computation. The output contains both ball enclosures and the exact binary pairs.

A successful lower-bound comparison certifies that number for the test and hence for the full norm. It does not prove that the stored pair is the exact machine endpoint of the producer's internal ball, since that ball is not an input here. No norm upper bound or existence conclusion follows.

## Verified comparisons

All three C8 tests, at T=2^20,2^30,2^35 with R=2^35, and all three C9 tests, at R=2^31,2^32,2^35, satisfy b<(P_4-D_4)/d. Both retained-order comparisons |P_4-P_3|<=D_3+D_4 pass in every case. The Q=3 record alone leaves these six endpoint comparisons open because its independent remainder is larger. It still confirms every published decimal and integer lower bound. The Q=4 record resolves the six open comparisons without changing any published value.

Reproduce in this directory, serially, with the permitted Python interpreter:

```sh
python3 audit_c8.py
python3 audit_c8.py 4
python3 audit_c9.py
python3 audit_c9.py 4
python3 audit_binary_summary.py
```

The default command retains the Q=3 output names used by the existing certificate collection. The explicit argument4 writes audit_c8_Q4.json or audit_c9_Q4.json. Each Q=4 record includes the exact binary pair, a strict ball comparison, original source and producer hashes, and the corresponding Q=3 dependency hash.
