# Exact Sobolev energy for the frozen source operator

Status: CONFIRMED after independent derivation/checking and completed Opus 5.5 review 11. Date: 2026-10-20. The actual returned model was claude-opus-5-5; the review is in ../../evidence/opus_review_11/answer.md. Its suggestions were independently checked.

## Statement

Let A>1 and a0 be real. On Schwartz functions h on R^2 whose Fourier transforms have compact support away from zero, define

    L_A h = (A x partial_x+y partial_y-1)h
                 +a0 partial_x(-Delta)^(-1)partial_x h.

Use the unitary Fourier transform, Lambda^s with multiplier |k|^s, k=(xi,zeta), and w=k/|k|. For every real s,

    Re <Lambda^s L_A h,Lambda^s h>
      = integral_R2 [s(A w1^2+w2^2)-(A+3)/2-a0 w1^2]
                       |k|^(2s) |hat h(k)|^2 dk.                 (1)

The identity also holds within the even-x/odd-y parity class. In particular, uniform strict positivity of this quadratic form with a constant times the homogeneous H^s seminorm is equivalent to

    s > (A+3)/2,
    s > [a0+(A+3)/2]/A.                                      (2)

The coefficient at horizontal frequency is sA-a0-(A+3)/2. Its zero differs by (A+1)/(2A) from the pointwise derivative threshold (1+a0)/A. This is the L2 volume contribution. Identity (1) is not a global inverse or Fredholm theorem, and does not classify nonlinear profiles.

Dependencies: Fourier differentiation, Plancherel and ordinary integration by parts on compact Fourier support. The relation with IPM uses the linearization in ../indicial_fourier/PROOF.md: its velocity contribution at the source is a0 times the second velocity component, with multiplier -a0 xi^2/|k|^2.

## Derivation

Write H=hat h, b(k)=(A xi,zeta) and Q=A w1^2+w2^2. Direct transformation gives

    hat(L_A h)=-b dot grad_k H-(A+2+a0 w1^2)H.

For the weight v=|k|^(2s), div_k b=A+1 and b dot grad_k v=2s Q v. Compact Fourier support away from zero removes both boundary terms. Therefore

    Re integral v (-b dot grad H) conjugate(H)
      = (1/2) integral div(v b) |H|^2
      = integral [(A+1)/2+s Q] v |H|^2.

Subtracting A+2+a0 w1^2 proves (1). The coefficient is affine in w1^2 in [0,1], so its minimum is the smaller of

    s-(A+3)/2,  sA-a0-(A+3)/2.

Strict positivity is exactly (2). Necessity remains true under the required parity: choose smooth Fourier bumps in narrow cones near either axis, reflect them evenly in xi and oddly in zeta, and multiply by i to enforce the reality condition H(-k)=conjugate(H(k)). The bumps can approach either axis without touching it. Thus failure of strict positivity cannot be repaired by the symmetry restriction.

## Scope of the correction

A derivative measured pointwise along a characteristic does not include a spatial volume factor. An L2 packet norm does. For the dilation flow X -> exp(t diag(A,1))X, the square root of its Jacobian is exp((A+1)t/2). Omitting this factor conflates a pointwise/Hölder heuristic with an H^s estimate. The exact identity above corrects that omission without asserting that either local criterion supplies the weighted full-plane estimates needed for the research endpoint.

Verification: verification/exact_gaussian_moments.json contains 24 exact rational Gaussian-moment examples and negative controls for the omitted volume term. The examples use positive integer s and hat h=i*zeta times an anisotropic Gaussian. They are not compactly supported in Fourier space, but the same integration by parts is justified directly: exponential tails vanish, and the inner-circle term vanishes for these positive s. No domain extension beyond these test functions is used.
