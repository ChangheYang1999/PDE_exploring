# Retain both components through finite-difference division

Statement. Let binary64 arithmetic use round-to-nearest with ties to even. Set H = 1, L = 2^(-53), and h equal to the binary64 value of the decimal literal 0.001. Let d be the binary64 product 2h, which is exact because multiplication by two changes only the exponent here. Then

    fl(fl(H + L) / d) != fl((H + L) / d),

where the addition and division inside the outer fl on the right are interpreted as exact rational operations. This is a scalar counterexample to the claim that rounding a double-double numerator before division implements a single final rounding of the quotient. It is not a claim about the size of an error on an Euler residual.

Proof. The exact sum H + L is halfway between 1 and the next binary64 number above 1. The even-significand tie rule gives fl(H + L) = 1. The binary64 literal h has the exact rational value 1152921504606847 / 1152921504606846976, so d = 1152921504606847 / 576460752303423488. Exact rational comparison puts 1/d inside the rounding interval of 500. Hence the left side equals 500.

Around 500 the binary64 spacing is 2^(-44). Exact rational comparison gives

    500 + 2^(-45) < (1 + 2^(-53))/d < 500 + 3*2^(-45).

Both inequalities are strict. The right side therefore rounds to 500 + 2^(-44), the successor of 500, proving the inequality. The attached verification checks the rational inequalities directly and the relevant binary64 bit patterns.

Application and limits. The draft residual ladder rounds a double-double numerator as H + L and then divides by 2h or 12h. General division by those non-power-of-two divisors is another rounded operation. Keeping the numerator pair through a double-double division and rounding the resulting quotient pair closes this particular premature-rounding gap. The production helper dd_div_f is a possible implementation and is checked only on the displayed counterexample here. No theorem of correct rounding for that helper, no derivative acceptance result, and no pressure accuracy claim follows from this scalar argument. Multiplication by 12 can also round the divisor itself; a specification using exact real 12h must distinguish that from using its binary64 value.

Dependencies. Binary64 spacing and ties-to-even rounding; exact rational arithmetic. The verifier is Python-only. No formal proof build is part of this result.
