# Chae's weighted boundary step and its stationary rotating consequence

Status: the complete existing A, C and literature comparisons agree after independent checks. The same-exponent implication is refuted; the strict-exponent repair and the exact stationary theorem below are confirmed. This adds no new nonexistence class and does not resolve the unrestricted target conjecture.

## 1. Exact claims and source limits

In Dongho Chae, *Euler's equations and the maximum principle*, arXiv:1308.1051v3, the alpha>-1 branch of Theorem 1.1 and the (a+b)b>0 branch of Theorem 1.2 require strict vorticity exponents. The retained primary PDF and independently regenerated text are the sources. Printed pages 7-8, equations (2.16)-(2.24), contain the weighted boundary argument. Printed pages 9-10 contain the compact-support argument. The entire paper has not been freshly read for this check.

The same-exponent inference after (2.21), from |Omega|=O(r^(-k)) to r^(2k)|Omega|^2 tending to zero, is false as an implication between bounds. For k>0, g(y)=(1+|y|^2)^(-k/2) is smooth and satisfies the first bound, while r^(2k)g(y)^2 tends to one. This is a scalar test of the inference, not an Euler counterexample or a refutation of Chae's theorem.

In the source's case C, b<0 and a+b<=0. Put rho=(a+b)/b. Its hypothesis is k>rho. Choose rho<theta<k. The needed coefficient is

    a+b-b theta = (-b)(theta-rho) > 0.

Replacing the proof's weight exponent by theta preserves every strict sign in (2.16)-(2.21), and the weighted square is O(r^(-2(k-theta))), which tends to zero. Uniform decay over the time period gives uniform weighted decay. The second occurrence of Gamma2 in the sentence after (2.21) refers instead to the cutoff's inner boundary Gamma1. The rendered page 8 verifies these two printed steps.

The source writes the spatial bounds for every time in one period; its proof uses uniform bounds over that period. This review does not infer uniformity from pointwise-in-time bounds plus periodicity. No verdict about the full general periodic theorem under a merely pointwise interpretation is made. The stationary rotation conversion in Section 5 supplies the needed uniformity directly.

## 2. Stationary theorem and notation

Let c>0 and omega be any finite real number. Let J(y1,y2,y3)=(-y2,y1,0). Suppose U in C^2(R^3;R^3) and P in C^1(R^3) satisfy div U=0 and

    (1-c)U + B dot grad U + omega J U + grad P = 0,
    B(y) = c y - omega J y + U(y).

Assume DU(y) tends to zero uniformly as |y| tends to infinity. Assume constants C,R1>0 and k>1/c satisfy |curl U(y)|<=C |y|^(-k) for |y|>=R1. Then U is constant. If U(y) tends to zero, that constant is zero.

There is no pressure normalization, velocity-integrability or energy hypothesis. Constants in the argument may depend on the fixed solution, c and omega. The result holds separately for every finite omega. Both decay assumptions are additional to the campaign's velocity decay hypothesis.

Write Omega=curl U, S=(DU+DU^T)/2, r=|y| and q=|Omega|^2. DU is bounded. Given epsilon>0, choose R0 with |DU|<=epsilon outside R0. For r>R0 the segment formula gives

    |U(y)| <= |U(0)| + R0 sup|DU| + epsilon r.

Thus U=o(r), uniformly in direction. Taking curl first in distributions cancels grad P. Since all remaining terms are continuous, the resulting identity is classical:

    B dot grad Omega = (DU - omega J - I) Omega,
    B dot grad q = 2 Omega dot S Omega - 2q,
    div B = 3c,
    B dot grad r = cr + U dot y/r  (r>0).

The skew matrix is orthogonal to Omega in the first scalar contraction and to y in the radial identity. This is the entire dependence on rotation in the proof.

## 3. A cutoff maximum forces compact vorticity support

Choose `1/c<theta<k` and let `d=c theta-1>0`. Choose epsilon>0 with epsilon<c/2 and (1+theta)epsilon<d/2. Choose R>=R1 sufficiently large that |S|_op<=epsilon and |U|/r<=epsilon for r>=R. Direct differentiation gives, with no division by q,

    B dot grad (r^(2theta)q)
      = 2(c theta-1)r^(2theta)q + 2r^(2theta) Omega dot S Omega
        + 2theta r^(2theta-2)(U dot y)q
      >= d r^(2theta)q.

This also holds at vorticity zeros. Moreover B dot grad r>=(c-epsilon)r>=cr/2 on the exterior region.

Take psi in C-infinity([0,infinity)), nondecreasing, zero on [0,R], one on [2R,infinity), with 0<=psi<=1. The function F(y)=psi(r)r^(2theta)q(y), extended by zero near the origin, is nonnegative and C^1 on all of R^3. The product rule, psi'>=0 and the positive radial derivative give

    B dot grad F >= d F  on R^3.

Because theta<k, F tends to zero at infinity. If F is positive at one point, choose a ball outside which F is below half that value. Continuity then gives a positive global maximum inside the ball. At that point grad F=0, contradicting dF>0. Hence F=0 and Omega=0 on r>=2R. No characteristic escape or global flow hypothesis has entered this argument.

## 4. A small power eliminates compactly supported vorticity

Let M=sup |S|_op<infinity and choose 0<p<min(2,3c/(1+M)). For delta>0 define

    f_delta = (delta+q)^(p/2)-delta^(p/2).

It is C^1 and compactly supported in the same fixed ball as Omega. Its transport derivative is

    B dot grad f_delta = p(delta+q)^(p/2-1)(Omega dot S Omega-q).

Integrating div(B f_delta) over a ball strictly containing its support gives, without boundary terms,

    0 = 3c integral f_delta
        + p integral (delta+q)^(p/2-1)(Omega dot S Omega-q).

Concavity for 0<p<2 gives 0<=f_delta<=q^(p/2). Also q(delta+q)^(p/2-1)<=q^(p/2). These bounds give fixed integrable majorants, including at q=0. Define sigma=(Omega dot S Omega)/q for q>0 and sigma=0 for q=0. Dominated convergence as delta decreases to zero yields

    0 = integral (3c-p+p sigma)|Omega|^p
      >= [3c-p(1+M)] integral |Omega|^p.

The coefficient is strictly positive, so continuity gives Omega=0 everywhere. Since div U=curl U=0, the distributional identity Delta U=grad div U-curl curl U makes U harmonic and smooth. Every entry of DU is then an entire bounded harmonic function tending to zero at infinity. Harmonic Liouville gives DU=0. Thus U is constant. Substitution into the full equation gives

    P(y)=P(0)-([(1-c)I+omega J]U) dot y.

Linear pressure is allowed. Uniform velocity decay makes the constant velocity zero.

## 5. Rotation conversion and independent integrability check

Put Q_s=exp(omega s J), V(y,s)=Q_s U(Q_s^(-1)y), and Pi(y,s)=P(Q_s^(-1)y). Differentiation gives

    partial_s V = omega(JV - DV J y),
    partial_s V + (1-c)V + c(y dot grad)V
      + (V dot grad)V + grad Pi = 0,
    div V=0.

Here Q_s commutes with J and preserves the Euclidean norm. Furthermore

    DV(y,s)=Q_s DU(Q_s^(-1)y) Q_s^(-1),
    curl V(y,s)=Q_s Omega(Q_s^(-1)y).

Consequently the stationary derivative and vorticity bounds become bounds uniform over all s. For omega!=0 the period 2pi/|omega| is valid; for omega=0 every positive period is valid. Chae's parameter is alpha=1/c-1>-1, so alpha+1=1/c. This explains the strict exponent without using a pointwise-to-uniform inference.

There is also an independent short proof from A029. Choose 3/k<p<3c. The strict tail then gives Omega in L^p(R^3), and DU tending to zero implies S tending to zero. The complete retained A029 argument uses outward radial flux to obtain compact support and then the same small-power integration. It even requires only strain decay, not full derivative decay. The present theorem is within that already confirmed class.

## 6. Dependencies and boundaries of the verdict

The direct stationary proof uses the curl identity, a segment integral, a smooth radial cutoff, the elementary maximum argument, the divergence theorem, dominated convergence and harmonic Liouville. Section 5's alternative uses A029. There is no numerical test, formal proof, new model call or claim of novelty.

At k=1/c neither 1/c<theta<k nor 3/k<p<3c is possible. These arguments make no endpoint claim. Velocity decay alone supplies neither derivative decay nor the strict vorticity exponent. The campaign's nonexistence conjecture for 2/5<c<1/2 and arbitrary omega remains OPEN. Only the defective scalar implication, its strict-exponent repair, and the exact conditional stationary theorem are under review here.
