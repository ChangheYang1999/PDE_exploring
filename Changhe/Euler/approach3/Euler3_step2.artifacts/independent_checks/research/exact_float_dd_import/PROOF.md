# Exact float imports and double-double splitting

## Statement and notation

All arithmetic in the statements below is real arithmetic unless explicitly described as binary64 rounding. Let fl be IEEE 754 binary64 round-to-nearest, ties-to-even, and assume the particular numbers below are normal and finite. A double-double pair (h,l) denotes the real sum of its two binary64 entries. Let dec(f) denote the real number represented by the shortest round-tripping decimal string of a binary64 number f. In general dec(f) is not the exact real value f.

For f = fl(1/10), the following claims hold.

1. f = 3602879701896397/36028797018963968 and f - 1/10 = 1/180143985094819840.
2. Since the shortest decimal string for f is "0.1", importing that string produces 1/10, not f.
3. Consider the splitting operation h = fl(x), l = fl(x - dec(h)). At x = 1/10 this gives (f,0), so the represented sum has error 1/180143985094819840. Thus this operation does not, even in this simple case, supply an approximation with relative error 10^-30 or smaller.
4. If the splitting operation instead subtracts the exact binary64 value h, the same example gives l = fl(-1/180143985094819840). Its remaining absolute error is at most 2^-110, and its remaining relative error is at most 10*2^-110 < 10^-31.

These are claims about input conversion and splitting, not about the correctness of any Euler residual or derivative.

## Proof

The adjacent binary64 grid near 1/10 has spacing 2^-56. Multiplying 1/10 by 2^56 gives 7205759403792793.6. The nearest integer is 7205759403792794, so the rounded value is 7205759403792794/2^56 = 3602879701896397/2^55. Subtracting 1/10 gives

    (10*3602879701896397 - 2^55)/(10*2^55)
    = 2/(10*2^55) = 1/(5*2^55).

The shortest round-tripping decimal representation is 0.1. Its exact real value is 1/10, which differs from f by the positive quantity just computed. This proves claims 1 and 2.

For claim 3, take x=1/10. The high entry h is f, while dec(h)=1/10. The residual used for the low entry is therefore zero, giving l=0. The error is f-x=1/(5*2^55). Its relative value is 2^-54, larger than 10^-30.

For claim 4, subtracting the exact h instead gives the nonzero residual -1/(5*2^55). Its magnitude lies between 2^-58 and 2^-57. The binary64 grid in this binade has spacing 2^-110, and nearest rounding has error at most half a spacing, hence at most 2^-111. The stated looser bound 2^-110 follows. Adding h exactly to the rounded low entry leaves precisely that low-rounding error. Division by x=1/10 gives a relative bound 10*2^-110 < 10^-31.

## Dependencies and scope

The proof uses only binary64 spacing, nearest rounding, the explicit round-tripping string 0.1, and exact rational arithmetic. An implementation may use higher precision internally; it must still import binary64 inputs through their exact binary value if that is its stated convention. An exact integer ratio or a verified exact float constructor provides that convention. Decimal-string import can be correct under a different, explicitly decimal input convention, but does not satisfy the convention considered here.

For arbitrary inputs, a two-stage split additionally needs enough working precision, finite values, and control of overflow and underflow. No unrestricted error theorem for a whole numerical pipeline is claimed here. The attached checks execute the captured conversion and splitting functions on selected finite examples, and verify the rational counterexample. Formal verification has not been performed.
