# A real response zero between two admissible integers

Status: Existence PROVED in V499 and uniqueness on the stated interval PROVED in V518, after the1024/1536-bit derivative certificates and the independent theory-part review of18:06Z.

## Statement

For the sin(11 theta) profile at delta=4/9, let S(t) be the compact response of149 and227, with S(1/(4k-2))=sigma_k for integer k>=28. The directed endpoint checks establish

    S(1/2050)<0<S(1/2054).

Consequently S has a real zero in (1/2054,1/2050). In the real index coordinate k=(1/t+2)/4 this zero lies strictly between513 and514. In particular, a uniform nonzero bound on all integer responses does not require a nonzero bound for every real parameter in the compact interval.

If the directed interval derivative check also establishes S'(t)<0 throughout [1/2054,1/2050], the zero in this interval is unique. Existence does not depend on this additional derivative check.

## Continuity

The low coefficients f_1,...,f_9 and g_1,...,g_8 are fixed rational numbers. The compact formula is a finite rational expression in t. Its transport denominators have form1+(2+4(r-1)/9)t, strictly positive for t>=0. Its first Poisson factors are2(v+1-4r/9), nonzero for integer v and1<=r<=8. The remaining factors are2(2+(v-1+4r/9)t).

A direct bound on the compact expression is |v|<=14r-1 at stage r. For r=1 the unit shift of a low derivative gives |v|<=13. Inductively, U_s has bound14s-1, V_s has bound14s, and one further high derivative increases each by at most one. Low density derivatives have bound12(r-s), and low stream derivatives have bound12(r-s)+1. Every product therefore has bound12r+2s+1<=14r-1 for s<=r-1. This bound needs no cancellation of endpoint coefficients. Consequently |v-1+4r/9|<=14r+4r/9<=1040/9 for r<=8. On the stated interval, t<=1/2050, so

    2+(v-1+4r/9)t >= 2-1040/(9*2050)>0.

Every intermediate denominator is nonzero there, hence S is continuous. A successful interval jet evaluation also checks each denominator directly and independently certifies this premise.

## Existence and optional uniqueness

The endpoint signs and the intermediate value theorem give a zero strictly inside the interval. The reciprocal change of coordinates is continuous and strictly decreasing, so its real index lies in(513,514). A strictly negative derivative, when separately certified, gives strict monotonicity and at most one zero there.

Topic227 proves |sigma_k|>2^-29 for every integer k. That bound and the real zero coexist. The root is not an integer response and is not an obstruction to the tuned integer recurrence. A cover that demanded separation on every real subinterval containing the root would therefore impose an unnecessary condition; the singleton and integer-exclusion alternatives in232 avoid it.

Dependencies: compact identity149, support bound197, directed jet inclusion234, elementary continuity and the intermediate value theorem. No statement about other real zeros or the true radius of convergence follows.

## Completed endpoint check

The1024-bit directed values have signs S(1/2054)>0 and S(1/2050)<0, with approximate values8.0772047862e-9 and-1.3355326218e-8. Every interval denominator is separated. The derivative enclosure from one interval contains zero and does not prove uniqueness. The existence proof is complete independently of that attempted derivative check.

## A sharper derivative certificate

The first interval derivative calculation was inconclusive. The following refinement does not infer a sign from that calculation. On a rational subinterval I=[a,b], let m=(a+b)/2 and r=(b-a)/2. A degree-three interval jet at m encloses S'(m) and S''(m)/2 in its coefficients c_1(m),c_2(m); a jet whose constant input ranges over I encloses S'''(x)/6 for every x in I in c_3(I). Taylor's theorem applied to S' gives, for t=m+x in I,

    S'(t) in c_1(m)+2c_2(m)[-r,r]+3c_3(I)[0,r^2].

All intermediate denominators must exclude zero on I. A finite rational partition whose derivative enclosures are all strictly negative proves strict decrease over the full interval. Combined with the previously proved endpoint signs, this certifies uniqueness of the zero. The partition and sign bounds have been replayed at higher precision, as recorded below.

The refined certificate has completed: one interval gives S'(t) in -0.022561 +/-6.48e-7, strictly negative, and all denominators are separated. A fresh1536-bit replay confirms the1024-bit construction. The initial inconclusive calculation is retained as historical evidence. The theory part independently accepted the derivative argument at18:06Z. Together these checks prove that the zero in this interval is unique (V518).
