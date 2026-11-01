# Agreement of floating twins does not certify the canonical recurrence

Status: CONFIRMED finite counterexample (V314). Agreement of these floating twins as an accuracy certificate is REFUTED.

## Exact objects and claim

Set delta=2/3, c=3, and f1=sin(theta). Use the canonical polynomial-in-log recurrence with zero constant in every newly resonant stream harmonic. Write M_n and N_n for the sums of the absolute Fourier coefficients over all logarithmic columns of the density and stream, respectively. Their interval enclosures through330 are retained in82.

Compare two floating computations, with initial amplitudes1 and1.0000000001, against those enclosures at common computed orders. Normalize the second computation by its amplitude to the nth power. The initially retained comparison used the printed decimal amplitude; the refinement below uses the exact binary64 input. The purpose is to decide whether close agreement of these floating outputs guarantees proximity to the exact canonical coefficient norms.

## Scaling and comparison argument

At order1 both fields depend linearly on the leading amplitude. If all lower fields at order i are homogeneous of amplitude degree i, every ordered product contributing to order n has degree n. The linear radial and angular inverses preserve that degree. Setting each new free constant to zero preserves it as well. Induction therefore gives degree n for every density and stream coefficient, including each logarithmic column. Positive amplitude a multiplies M_n and N_n by a^n. Their base-ten logarithms change by n log10(a).

For each retained floating logarithm x and certified exact logarithm interval I, interval subtraction x-I encloses the error of the displayed floating value. An interval bounded away from zero certifies a discrepancy. Likewise the difference between the two normalized displayed floating logarithms can be enclosed using exact decimal input and outward-rounded arithmetic.

If the floating pair agrees closely while either value is many decades from its exact interval, the agreement is a counterexample to using this amplitude perturbation as an accuracy certificate. The exact intervals remain valid. This comparison does not prove a particular causal mechanism, distinguish underflow from cancellation, or describe orders that were not computed.

## Dependencies and evidence

Topic82 supplies the independently verified canonical interval norms. Topic127 gives the earlier logical limitation of the amplitude probe. Source snapshots and hashes identify the actual floating records. This topic compares existing files and launches no new recurrence. It does not certify the reset329 continuation relative to the original exact initial data.

## Certified finite counterexample

At order300, the full density and stream plain norms from the unperturbed binary64 run differ from the retained exact-input interval logarithms by6.2855560876415897948 and7.78978226332986700 decades. The normalized amplitude-perturbed run differs from its unperturbed twin by only9.13180765543554e-7 and7.61637445543554e-7 decades. Both twin differences are strictly below1e-6.

Among the retained common orders, the density error first exceeds1e-6,0.01,1,5 decades at267,276,282,296. The corresponding stream orders are262,271,277,289. These concern the whole plain norms, not only the constant logarithmic column. The source logs were frozen and fingerprinted; all comparisons use the previously certified interval norm data. Arithmetic elapsed time was0.4244332890957594 seconds. The calculation identifies a shared discrepancy without proving which floating point operation caused it.

## Actual binary64 input normalization

The source converts the string `1.0000000001` through Python `float`.
Its exact initial amplitude is therefore
562949953477607/562949953421312. Relative to the printed decimal, the
base-ten logarithmic normalization changes by
3.5933686551939427759871881928221488592963e-18 per order.

At order 300, subtracting this correction gives normalized twin
differences of 9.131807644655433e-7 for density and
7.616374444655433e-7 for stream. Both remain strictly below 1e-6.
The exact-input norm errors of the unperturbed run are unchanged.
The earlier decimal-normalized values are retained and explicitly
distinguished in `actual_binary_normalization.json`. This refinement
took 0.02680832426995039 seconds and is recorded in V316.
