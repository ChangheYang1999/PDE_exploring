# Pre-execution checks

Read the standalone proof before running any numerical control. The proof establishes ideal-arithmetic exactness; numerical controls only test the chosen product-rule implementation and the degree substitutions.

Use exact normalized Cartesian monomial sphere moments, which are zero if any exponent is odd and otherwise equal the product of the three odd double factorials divided by (total degree+1)!!. Test representative monomials through degree74 on42-by-84 and48-by-96 product rules at two fixed azimuth offsets. Normalize nonzero moments by their exact values and use a2e-12 relative tolerance; use a2e-15 absolute tolerance for zero moments. Include pure powers, balanced powers, high mixed powers and odd exponents. Compare the reconstructed quadrature moments directly, without fitting to the known values.

Include an intentionally unresolved azimuthal harmonic Re((x+i y)^84) on the84-azimuth rule at zero offset. Its exact sphere average is zero, but the quadrature average is strictly positive in exact arithmetic. This control must expose failure outside the registered degree condition. Include the same harmonic on96azimuths, where the azimuth sum should vanish to numerical precision. Keep the controls small and run only when the side's single CPU computation slot is free. Save actual source hashes, timestamps, outputs and all failures.

An lead review of the mathematical argument is requested separately. Neither passing software controls nor an external review substitutes for a floating-point error enclosure or certifies a checkpoint.
