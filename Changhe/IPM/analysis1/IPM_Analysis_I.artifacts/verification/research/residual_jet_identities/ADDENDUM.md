# Conventions and the first independent review

Date: 2026-10-21. Mandatory with PROOF.md.

The source writes f_n(e^t) as a radial function evaluated at r=e^t;
PROOF.md writes that same value as f_n(t). No factor changes. The module
header's formula called psi_n' includes e^(-t) and is actually partial_r
psi_n. The derivative path uses partial_t and the exact identities in
PROOF.md. This documentation ambiguity must not be used to infer a sign
or missing radial factor.

The source obtains M and Nf independently from T and A array shapes. The
application here requires the actual source-file shapes M=260,Nf=261,
T degree7, and the matching nder=4 call that creates _last_eps. These
must be checked from current pinned input headers and caller AST. The
constructor does not impose Nf=M+1 for arbitrary inputs. We make no
universal statement for mismatched source dimensions.

The first actual Opus5.5 review confirmed the exact identities and asked
for these dimension/caller checks, all scatter multiplicities, and the
value/derivative path convention. It also proposed a full exact-surrogate
execution. The final scope will state precisely which expressions and
execution paths were checked; an AST comparison is not a full numerical
execution. A small rational example is diagnostic unless a complete
basis or algebraic structural argument establishes universality.

The derivative-algebra check differentiates abstract smooth functions and
uses A'=-2nA+g and B'=2nB-g. It never differentiates a uniform remainder.
Finite Taylor coefficients in an exact formal-power-series surrogate, if
used, are exact derivatives at zero by definition and have no C0 remainder.
Such a surrogate does not certify the floating coefficient/remainder
arithmetic of the numerical producer.

The complete Chebyshev test forms products by an independent recurrence
in the even angular frequency a. For fixed odd b=2j+1 set

    V_0=2U_(b-1), V_1=2x U_(b-1), V_(a+1)=2x V_a-V_(a-1),
    W_0=0, W_1=2T_b,             W_(a+1)=2x W_a-W_(a-1).

Induction gives V_a=2T_a U_(b-1), W_a=2U_(a-1)T_b, with U_-1=0.
For every a=2,4,...,522, exact integer polynomial comparison to
U_(a+b-1) plus or minus sign(b-a) U_(|b-a|-1) checks both products.
The common factor sin(theta) can first be canceled where nonzero; equality
at its zeros follows by continuity. The test makes no trigonometric
sampling or modular zero inference.
