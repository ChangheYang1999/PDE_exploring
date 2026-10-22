# Actual finite composition checks

Written 2026-10-21T19:56:22.784625+00:00. Final acceptance still requires a completed actual review and a later independent adjudication.

The first checker finished19:52:29.841173Z. It compared all135723 exact saved scalars against19389 coherent cells, in counts2632 inner,7809 middle and8948 outer, checked the two exact parameters, every exact join, both endpoints, every width slack, and the maximal start displacement1677/629659522901737472. It rechecked all pins of accepted152 and160.

The independent checker finished19:55:25.532780Z. It manually decoded IEEE binary64 values to fmpq, traversed the source rows in reverse region and index order, repeated all135723 scalar comparisons, verified the parameter dyadics, and traversed the exact cover backwards. It independently obtained positive cross-multiplied rational slacks for the proposed ceilings. Arb at320 bits and mpmath.iv at100 decimal digits gave overlapping corrected-ceiling enclosures strictly below0.385656 and585.874. Neither engine uses binary floating approximations to establish these two strict comparisons.

The first independent attempt failed at the conversion of an mpmath endpoint mantissa of type gmpy2.mpz to fmpq. It produced no audit output. Its source and traceback are preserved as code/audit_attempt1.py and evidence/audit_attempt1.log. The repaired checker converts the exact integer mantissa and exponent with int and also adds independent parameter and reverse-cover checks.

The conclusion, if accepted, is precisely the conditional theorem in PROOF.md, read with REGULARITY_AND_REVIEW_SCOPE.md. It is not a proof that the physical IPM residual satisfies the majorants or weak regularity. Both tails, the scaling-vector numerator and the global inverse remain open.
