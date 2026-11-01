# A real response zero for the seventeenth harmonic

Status: PROVED. The1024-bit construction,1536-bit replay and independent theory-part review at18:19Z confirm existence and uniqueness on the stated bracket. Admitted in V525.

## Statement

Let S be the unit-amplitude compact response for delta=6/13 and f_1(theta)=sin(17theta), as defined in149 and242. For integer k>=40, S(1/(6k-2))=sigma_k. Set a=1/14278, b=1/14272. If S(a)>0>S(b), S has a zero in(a,b), corresponding to a real index k=(1/t+2)/6 in(2379,2380). If in addition S'(t)<0 throughout[a,b], this zero is unique in that interval. No assertion of uniqueness elsewhere is made.

## Smoothness on the interval

The compact response is a finite rational expression in t with fixed rational low-order coefficients. At stage r, 1<=r<=12, the transport denominators are 1+(2+6(r-1)/13)t and are positive. The first Poisson factors are 2(v+1-6r/13), which are nonzero because v is integral and13 does not divide r. The remaining factors are 2(2+(v-1+6r/13)t).

A support bound that does not require cancellation is |v|<=20r-1. At r=1 the carrier derivative times a low density derivative has bound19. Inductively U_s has bound20s-1 and V_s has bound20s. Differentiation adds at most one. The low density derivative at r-s has bound18(r-s), and the low stream derivative has bound18(r-s)+1. Every product has bound18r+2s+1<=20r-1 for s<=r-1. Hence |v-1+6r/13|<=20r+6r/13<=3192/13. For t in[a,b],

    2+(v-1+6r/13)t >= 2-3192/(13*14272)>0.

All denominators are nonzero on the closed interval, so S is smooth there. A successful interval-jet evaluation checks these denominators directly as well.

## Existence and uniqueness

The endpoint signs imply existence by the intermediate value theorem. For a subinterval I=[x,y], let m=(x+y)/2 and r=(y-x)/2. A degree-three jet at m encloses S'(m) and S''(m)/2 by c_1(m),c_2(m), and an interval-input jet encloses S'''(xi)/6 for all xi in I by c_3(I). Taylor's theorem gives

    S'(I) subset c_1(m)+2c_2(m)[-r,r]+3c_3(I)[0,r^2].

A finite exact partition of[a,b] on which all these enclosures are negative proves strict monotonicity and uniqueness. Each denominator must be separated, and each leaf is to be checked again at higher precision. The reciprocal index map is continuous and strictly decreasing, so the unique root maps to(2379,2380).

This real root is not an integer response and does not obstruct a positive lower bound for all integer responses. The all-index convergence certificate is a separate task in242.

Dependencies:01,149,232,234,236,242.

## Completed directed checks

The endpoint values are S(a)=2.7706188235585353467544e-12 and S(b)=-1.1291632150099695593217e-11 to the displayed digits. One Taylor interval encloses S'(t) in -0.000477591 +/-4.65e-10, strictly negative. The higher-precision replay confirms the signs, all denominator separations and this complete one-leaf partition. Exact dyadic ball encodings are in verification/uniqueness_checks.json, and verification/uniqueness_replay.json identifies the replayed source hash. The decimal displays are not the proof inputs.
