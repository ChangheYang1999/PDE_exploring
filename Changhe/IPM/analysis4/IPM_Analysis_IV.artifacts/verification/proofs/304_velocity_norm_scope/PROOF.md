# Scope of the leading-velocity minimizer

Status: complete elementary argument. This clarifies the norm in the summary; it does not refute the correctly stated Proposition8.4.

## Exact statement

For 0<gamma<1, put P=1+gamma. The cancellation polynomial of degree at most2K+1 with unit first sine coefficient uniquely minimizes

    V_0(f)=||g'||_(A_0)+P||g||_(A_0),

where g is its leading stream coefficient and A_0 is the unweighted angular Wiener norm. This is the combined norm of the two polar velocity components. The minimizer can change for a positive strip width sigma in

    V_sigma(f)=sum_(j>=1)(2j+P)exp(2j sigma)|b_j|,
    g=sum_(j>=1)b_j sin(2j theta).

The claim is not a norm-independent extremal principle. In particular, at gamma=1/2, K=1 and sigma=log4, the cancellation polynomial is not a minimizer of V_sigma among degree-at-most3 profiles with unit first coefficient.

## Proof and counterexample

The complete minimization theorem, including its equality conditions and positive-strip classification, is in topic54. Its finite unweighted conclusion follows because the positive weights W_j=A_(j-1)/2 strictly decrease with j, where A_0=1 and A_j/A_(j-1)=(2j-P)/(2j+P). Thus the unique final index j=K+1 minimizes them.

For the counterexample take

    f_c=sin(theta)+(1/7)sin(3theta),
    f_s=sin(theta).

The canceled Poisson formula from topic01 gives

    g_c=-(1/77)sin(4theta),
    g_s=-(1/7)sin(2theta).

Indeed the mode2 coefficient for f_c is -1/7+(1/7)=0, and its mode4 coefficient is -(1/7)/11=-1/77. Therefore

    V_0(f_c)=1/14 < 1/2=V_0(f_s),
    V_(log4)(f_c)=128/7 > 8=V_(log4)(f_s).

Both profiles are finite real odd sine polynomials with unit first coefficient. The strict reversed inequality proves the claimed failure at positive strip width.

## Publication wording and dependencies

In the summary's Candidate-shape paragraph, replace the unspecified phrase "leading velocity norm" by "combined unweighted Wiener norm of the leading polar velocity components". The theory already defines V_sigma explicitly and correctly distinguishes sigma=0 from positive sigma. This is a clarification of the summary's intended norm, not a new convergence result. No statement about the infinite growth rate, smallest possible exterior, or a Cartesian vector norm follows.

Dependencies: topics01,51,54. The accompanying rational calculation checks this finite example exactly. The frozen source paragraph identifies the text being clarified.
