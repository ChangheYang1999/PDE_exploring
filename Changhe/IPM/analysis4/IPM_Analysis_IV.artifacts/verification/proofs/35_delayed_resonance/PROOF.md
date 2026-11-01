# A compatible first resonance can be followed by an obstruction

Status: both finite independent exact calculations completed. The finite claim is separate from every all-order convergence question.

## Statement to check

Set delta=4/9 and c=9/5. With leading input sin(11 theta) or sin(13 theta), the first stream resonance at n=9, j=1 is compatible. Choose its free stream coefficient to be zero. The numerical report claims that the next stream resonance, at n=18 and j=3, is incompatible for both profiles.

At order n=18 the compatibility coefficient is the sin(5 theta) coefficient in f_18. The Cartesian x derivative forcing at sin(6 theta) must equal -6 times that coefficient. Exact nonzero forcing proves that no pure stream coefficient exists with this fixed earlier choice.

## Method and dependencies

The independent implementation uses rational Laurent polynomials with Cartesian derivatives. Every nonresonant stream is obtained by diagonal inversion of the Cartesian Poisson forcing, and its Laplacian is checked exactly. At a zero denominator it proves that the forcing is zero before assigning the free coefficient zero. The density is computed from the full ordered Cartesian transport sum.

This checks the same canonical choice as the numerical report. It does not rule out every possible nonzero free coefficient at the first resonance, and it does not settle logarithmic continuation. The dependencies are the independently derived recurrence and the first-resonance support rule in topics 01, 21 and 25.

## Exact result, 2026-10-31T03:30:04Z

Both claims of nonzero compatibility at the second resonance are confirmed under the zero first free amplitude. The exact kappa values are retained in `verification/sin11.json` and `verification/sin13.json`. Their approximate values are respectively 0.0002205515602945779 and 0.000026660748027190396. The true Cartesian forcing is -6*kappa. The numerical notes' values -0.002647 and -0.0003199 instead approximate -12*kappa, the doubled Fourier numerator before its factor 1/2, and should not be labelled as kappa itself.

All density stationary identities through order 18 and all stream Poisson identities through order 17 are exact. The first resonance is exactly compatible in both cases, and the first sine density coefficient at order 12 is nonzero. The runs took 1.334907716140151 and 1.602691981010139 seconds respectively. No result for a nonzero first free amplitude is asserted here.
