# Optimized rational weak probe for candidate 007

Status: analytic weak-test consequence of audited T4-172; new candidate arithmetic OPEN until completed and independently reproduced. No existence claim.

## Statement and spaces

Let w=(1+|X|^2)^(-a/2), 0<=a<2, and let rho be the exact canonical candidate C1-N1-007-d2w-j7-e2bal at the fixed exponent c. Suppose a real S1 correction h satisfies the full distributional equation F(rho+h;c)=0, h and canonical U[h] belong to L2(w^2 dX), and ||w U[h]||_2<=C_U||w h||_2. All integrals below must be absolutely integrable or justified by the cutoff limit. The displayed polynomial probes have the required decay for this candidate and these weights.

For a real polynomial P put t=r^2/(1+r^2), W=1-t and phi=y W^2 P(t). Set

    I=int F(rho;c) phi,
    M=||((2c+1)phi+(cX+U[rho]).grad phi)/w||_2,
    C=||phi grad rho/w||_2,
    H=||grad phi/w^2||_infinity,
    D=M+C_U C.

Then m=||w h||_2 satisfies |I|<=Dm+C_U Hm^2, and hence

    m >= 2|I|/(D+sqrt(D^2+4 C_U H |I|)).

The zero probe is omitted. This is a necessary distance, with the exponent and leading tail fixed as in the campaign.

## Proof

Expand F(rho+h)=F(rho)+(cX+U[rho]).grad h-h+U[h].grad rho+U[h].grad h. The divergence of cX+U[rho] is 2c and div U[h]=0. Test with phi and integrate the transport and the quadratic term by parts. Cauchy-Schwarz with w gives the two linear bounds Mm and C C_U m. The quadratic term is bounded by H||w h||_2||w U[h]||_2. The positive quadratic root gives the formula. These are the same hypotheses and argument as T4-172; no inverse or differentiability gain is assumed.

The polar gradient is

    grad phi=W^2[sin(theta) Q(t)e_r+cos(theta)P(t)e_theta],
    Q=(1-4t)P+2tW P'.

Thus H=sup_(0<=t<=1) W^(2-a) max(|P|,|Q|). Candidate density and stream are represented independently from their exact potential by

    rho=r sum W^aj R_jn(t) sin(n theta),
    psi=r^2 sum W^aj S_jm(t) sin(m theta), aj=(j+1)(1-1/c)/2.

The transport form is affine in k for P=t^k. If M_k denotes its unsquared function, the Gram entry <M_k/w,M_l/w> is obtained by integrating t^(k+l+1) times the polynomial products of its constant and linear coefficients. The gradient form uses the exact angular integrals of sin^2(theta) sin(n theta)sin(m theta) and sin^2(theta) cos(n theta)cos(m theta). No angular triangle inequality is substituted.

## Numerical method and proof separation

The Gram matrices and pairings use outward Arb arithmetic on exact rational fields. Polynomial coefficients are expanded in W, and the moments are B(K+2,b+j+1). Their seeds and recurrences use only rational arithmetic and outward ball operations because K is a nonnegative integer and b is rational greater than -1. Finite sums retain every term, including cross terms.

A high-precision floating solve proposes a rational vector P. Only its later interval quadratic forms and the directly certified H enter the distance bound. No claim that the proposed vector is optimal is needed. A subdivision of [0,1] bounds each polynomial by its midpoint value plus interval derivative times half width, then multiplies by the largest W^(2-a) on the interval. The largest upper bound controls the entire interval. The last scalar is floored below the lower endpoint; decimal rounding to nearest is not used as a certificate.

The code and frozen input hashes accompany the output. Candidate arithmetic is not independently audited merely because the scalar inequalities are rigorous.
