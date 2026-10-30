# Smooth probes in higher angular modes

Date: 2026-10-29T02:54:32.607666+00:00.
Status: explicit extension of the audited weak-test identity. New angular formulas and candidate values remain OPEN until independently reviewed.

## Exact statement and hypotheses

Let c>1 and 0<=a<2. On R2 set w=(1+|X|^2)^(-a/2). Let rho be a smooth real S1 function, even in x and odd in y, with canonical IPM velocity u=(-R1R2 rho,R1^2 rho), using Rj=partial_j(-Delta)^(-1/2). Assume |rho|+|u|=O((1+r)^gamma) and |grad rho|=O((1+r)^(gamma-1)) for some 0<gamma<1. Let h be a real S1 distributional stationary correction at the same c, with h,U[h] in L2(w^2 dX), and ||wU[h]||2<=C_U||wh||2. Its equation means

    F(rho;c)+div((cX+u)h)-(2c+1)h
                 +U[h].grad rho+div(hU[h])=0.

All products are locally integrable. For any nonzero probe below define

    I=int F(rho;c) phi_n,
    M=||[(2c+1)phi_n+(cX+u).grad phi_n]/w||2,
    C=||phi_n grad rho/w||2, H=||grad phi_n/w^2||infinity,
    D=M+C_U C.

Every quantity is finite, and m=||wh||2 obeys

    |I|<=Dm+C_U Hm^2,
    m>=2|I|/[D+sqrt(D^2+4 C_U H|I|)].

When I=0 the lower bound is zero. For a=0 one may take C_U=1 by the vector Fourier multiplier norm. Weighted choices require the separately audited velocity bound. The statement needs neither a linear inverse nor any derivative of h. It is a necessary correction distance, not an existence theorem.

Proof of the inequality. Test the distributional equation with a compact radial cutoff times phi_n. Integrate the two divergence terms by parts. Weighted Cauchy-Schwarz bounds the transport, coupling and quadratic terms by Mm, C_U Cm and C_U Hm^2. The probe is O(r^-3) with gradient O(r^-4). Therefore its transport dual coefficient is O(r^(a-3)), both background dual coefficients are O(r^(a+gamma-4)), and its nonlinear coefficient is O(r^(2a-4)). These give integrability and vanishing cutoff errors for a<2 and gamma<1, using the L2 tails of wh and wU[h]. Also F=O(r^gamma), so its probe pairing converges absolutely. Solving the scalar quadratic proves the claim.

## Polar identities and exact integration

Let n be a positive odd integer and let P(t) be a real polynomial divisible by t^k0, where k0=(n-1)/2. Put

    phi_n(r,theta)=r(1-t)^2 P(t) sin(n theta), t=r^2/(1+r^2).

This is smooth on the whole plane: each monomial r^(2k+1) sin(n theta) is the polynomial Im(x+iy)^n times (x^2+y^2)^(k-k0), and the remaining radial denominator is smooth and positive. The probe is O(r^-3) at infinity, with differentiated decay. It belongs to S1, since n is odd.

Its polar gradient is

    grad phi_n=W^2[Q(t) sin(n theta)e_r+nP(t) cos(n theta)e_theta],
    Q=(1-4t)P+2tW P'.

Thus the exact gradient supremum in the weak test is

    H=sup_(0<=t<=1) W^(2-a) max(|Q|,n|P|).

For a stream mode psi_m=r^2 W^aj S(t) sin(m theta), write T_S=2S+2tW S'-2aj t S. Its velocity is rW^aj[-mS cos(m theta)e_r+T_S sin(m theta)e_theta]. Its contribution to u.grad phi_n, divided by rW^(aj+2), is

    (nT_S P-mS Q) sin((n+m)theta)/2
      +(-nT_S P-mS Q) sin((n-m)theta)/2.

Negative angular indices are replaced by positive indices with the opposite coefficient; the zero index vanishes. The dilation and zeroth-order contribution has angular index n and coefficient A=(2c+1)P+cQ. These rules give the exact transport form M, and hence its Gram matrices, for arbitrary n.

The pairing can be obtained without a separate nonlinear trigonometric formula:

    int F(rho;c) phi_n = -int rho M,
    M=(2c+1)phi_n+(cX+U[rho]).grad phi_n.

Indeed integrate div(cX+U[rho])=2c by parts. The candidate and probe decay give vanishing cutoff errors. Only equal positive sine indices survive, each with angular integral pi. With rho=rW^ai R and M=rW^(aj+2) A, their radial factor is tW^(ai+aj-1)dt/2. This proves the pairing rule used in the generalized code.

For positive density indices l,m, the exact gradient angular factors are

    int sin^2(n theta) sin(l theta)sin(m theta) dtheta
       =pi/4 [2 delta_lm-delta_|l-m|,2n+delta_l+m,2n],
    int sin^2(n theta) cos(l theta)cos(m theta) dtheta
       =pi/4 [2 delta_lm-delta_|l-m|,2n-delta_l+m,2n].

These follow from sin^2(n theta)=(1-cos(2n theta))/2 and the product-to-sum identities. The radial factor in C^2 is tW^(1-a+ai+aj)dt/2, giving the overall pi/8 coefficient. The transport square has pi/2 times tW^(1-a+ai+aj). All cross terms are retained.

The weak necessary quadratic inequality is unchanged. Each generated rational polynomial is a single admissible test, not an inverse approximation or a solution certificate. No optimality of the finite span is asserted.

## Verification artifacts

Canonical candidate007 computations are in ../optimized_probe_007/code/angular.py and ../optimized_probe_007/verification/n*_a0.json. The generalized n=1 formula reproduces the original Gram and direct-polynomial calculations. Each rational coefficient vector is frozen in JSON; all coefficient, input, helper and code hashes are recorded there. Candidate values remain OPEN pending another lane's reproduction.
