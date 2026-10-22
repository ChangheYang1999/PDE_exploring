# Endpoint refinement execution conventions

This supplements PROOF.md section8, without changing its analytic claim.

1. Each exact Fraction is passed to Arb through fmpq(numerator,denominator),
   and each fmpq directly to Arb. No rational endpoint passes through float.
   Arb rounds its rational point input outward; lower().man_exp() and
   upper().man_exp() give exact dyadic endpoints used in integer comparisons.
   The earlier phrase "point ball" allows the outward radius needed when a
   rational is not dyadic. Nonfinite values or unordered intervals fail.
2. The iv180 engine has no refinement or increased precision fallback.
   Every original coefficient and remainder must pass independently.
3. The seed's two drawn distinct indices are [1955, 3510]. Distinctness is
   among the drawn indices only, without excluding0,2955,7808. The actual
   fixed union is [0, 1955, 2955, 3510, 7808]. Its complete exact list is in the header.
   Actual restart neighbors are added and compared with completed replay.
4. For every first-method refinement, the independent auditor directly
   recomputes its particular-solution endpoint bound and then includes that
   whole mode's26 tests in the third method. Every such check must pass.
   Any third-method failure stops OPEN, even on a supplementary index.
   The saved selection is explicitly tested to contain every refined mode.
   All refinement indices, original failures and passing new bounds are
   logged; final extraction will count them by engine, mode and degree.
5. The exact rational forcing image must be a subset of the unchanged F
   candidate interval. It is checked for all2088 values on every cell.
6. Topic161 diagnoses a sufficient-test width failure for one j=0 value.
   No internal Arb mechanism has been proved. The review's speculative
   explanation involving large powers of lambda is not adopted; lambda^0
   is1 at that failed coefficient. Topics98 and99 are separately FINAL as
   scoped there, with canonical archive membership still conditional until
   its independent full check closes. This new topic does not inherit a
   full radial conclusion from them or from the partial failed topic101.
