# Exact recomputation of the knot-scale diagnostic

## Statement and scope

Interpret the original Analysis I trial_v2_h0.008.npz as exact dyadic data, with source SHA256 a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874. Let

 A(t)=sum_(m=0)^259 (-1)^m s_m(t)

be its vertical-axis cofactor, where s_m are the degree-seven B-splines stored in the original Phi basis. On each open knot span i its seventh derivative D_i=A^(7) is constant. The computation beside this proof independently reconstructs D_i for spans698-703 and the final31 nonzero spans, and evaluates A at the midpoint of every selected span. No sine-converted cache, Green solver or finite-section matrix is used.

For consecutive spans of comparable length define the diagnostic

 a_i=|D_i-D_(i-1)| (h_i/pi)^7/2,
 z_i=a_i/|A((t_i+t_(i+1))/2)|,
 h_i=t_(i+1)-t_i.

The computation encloses these numbers and the three-span ratios z_i/z_(i-3) when their denominators are nonzero. These are precisely defined diagnostics, not a rigorous extraction of a periodic component from a nonuniform spline, a certified inverse obstruction, or a statement about an unknown exact profile. Multiplication by (h/pi)^7 is motivated by a sinusoid of wavelength2h, but that motivation supplies no decomposition theorem. A large value alone does not refute condition(S).

## Independent exact reconstruction

Combine the original Phi control coefficients into the exact rational axis coefficients c_j=sum_m(-1)^m S_(m,j). For a spline of degree d with knot vector T, differentiation replaces its coefficients by

 c'_j=d(c_(j+1)-c_j)/(T_(j+d+1)-T_(j+1))

and deletes one endpoint knot on each side. This identity follows by differentiating the Cox-de Boor recurrence and telescoping the adjacent terms. Repeating it seven times produces the constant D_i on each nonempty span. All operations are rational, so no differentiation step has rounding error.

Independently evaluate the original undifferentiated spline by the polynomial de Boor recurrence on each selected span, with local coordinate sigma=(t-t_i)/h_i. The resulting polynomial P_i has degree at most7 and exact rational coefficients. Its seventh derivative is7! times its leading coefficient divided by h_i^7. Equality with the derivative recurrence is checked exactly. Horner evaluation at sigma=1/2 gives the exact midpoint A. Thus every raw D_i and A value is an exact rational result confirmed by two spline representations.

Directed512-bit evaluation of pi, integer powers and division encloses a_i,z_i and their three-span ratios. The output records exact rational source values as well as directed binary endpoints for the derived quantities. Arithmetic ratios use the exact stated indices and widths. Every division must have a denominator interval excluding0. The theory author's floating record is compared only after the independent values have been constructed.

## Interpretation

Alternation of D_i is an exact statement about this stored joined trial on the inspected spans. The finite diagnostic z_i can identify a scale worth investigating, but it is not the norm of a spectral projection and need not behave as a pure alternating sequence, especially at nonuniform knots or a junction. No filtering, trial modification or new inverse claim is performed here. The status of actual low injectivity and nonlinear smallness remains unchanged.

Dependencies: the original input and the independent exact de Boor evaluator of proof 04. The new derivative recurrence is also the one independently compared to de Boor in proof 194. The accompanying result file specifies the selected spans, exact values and comparison with the theory author's requested numerical diagnostic.

## Recomputed values

The exact derivative recurrence and independent polynomial checks finished at2026-10-28T13:54:27.816118+00:00 in2.63seconds. The exact rational seventh derivatives, rounded here only for readable numerical reporting, are

 span698: -97578364.7396301,
 span699:  363119169.856834,
 span700: -571051738.294454,
 span701:  580257673.024482,
 span702: -442652708.591853,
 span703:  303874912.974474.

The theory author's corresponding floating values differ relatively by between2.07e-5 and2.04e-4. The qualitative alternation is reproduced. The final-span normalized diagnostic is z_1564=4.94571041518123e-13. Across all30 requested final spans, the three-span ratios have numerical minimum1.4649274, maximum21.5438184 and median2.5142452; the central portion is about2.3-2.6 and the last ratios decline toward1.46. Thus a rough growth factor near2.5 describes part of this range, not every three-span step. The theory author's stored normalized diagnostics differ from the exact-data recomputation by up to7.81percent in this30-span range. The exact rational values and narrow512-bit enclosures, including every ratio, are in evidence/check.json. No finite-solve error model or conclusion about an exact profile is inferred.
