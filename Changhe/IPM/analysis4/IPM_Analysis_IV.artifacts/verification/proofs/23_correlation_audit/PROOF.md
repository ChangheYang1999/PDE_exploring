# What short-lag coefficient correlations do not establish

Status: the claimed fixed two-dimensional rotation is refuted for the tested checkpoint; singularity location remains open. The checkpoint calculation is supplemented below by interval checks.

## Claim under review

The numerical report infers that normalized density coefficient vectors rotate in a fixed two-dimensional subspace because their first two lag correlations are approximately `cos(phi)` and `cos(2phi)`. It then locates the dominant singularities at `exp(+-i phi)/L` and excludes a positive-real singularity at the same radius.

The statements are stronger than the reported measurements. They need either an all-order asymptotic theorem or further evidence explicitly labelled as conjectural. Multiplying different coefficient vectors by the signs of their largest coefficients also changes the original power series. Its singularity phase cannot be read from that altered sequence without tracking the signs.

## A finite-dimensional test

Use the actual coefficient vectors, normalized by their positive Euclidean norms. For three such vectors `v_0,v_1,v`, set

\[
 a=\langle v_0,v_1\rangle,\quad b=\langle v_0,v\rangle,
 d=\langle v_1,v\rangle.
\]

If `|a|<1`, the squared distance of `v` from their initial two-dimensional span is exactly

\[
 D^2=1-\frac{b^2-2abd+d^2}{1-a^2}.
\tag{1}
\]

This follows by solving the two-by-two Gram system for the orthogonal projection. In particular `D>0` proves that these three vectors do not lie in a common two-dimensional space. A fixed rotation would further require, for every lag `k`,

\[
 \langle v_0,v_k\rangle=\cos(k\phi),\qquad
 v_{n+2}-2\cos(\phi)v_{n+1}+v_n=0.
\tag{2}
\]

The numerical checkpoint for `delta=1/sqrt(5)`, `f_1=sin(theta)`, through order 700 fails both tests by amounts far larger than numerical rounding. With orders 572 and 573 as the initial span, the distance at order 574 is about 0.08126, at order 636 about 0.999465, and at order 700 about 0.9999999983. The lag-64 correlation is about -0.03038, whereas the rotation inferred from lag one predicts about -0.97654. The 128 vectors at orders 573 through 700 have about 56.6 percent of their squared norm outside their best common two-dimensional subspace, according to the floating-point Gram eigenvalue calculation.

These are finite checkpoint statements. They do not themselves determine the true large-order asymptotic structure, and do not refute every possible two-singularity model in a different topology.

## A counterexample to the inference from approximate local correlations

Let `e_1,e_2,...` be an orthonormal basis of a real Hilbert space, choose `0<epsilon<1` and `0<phi<pi`, and define

\[
 v_n=\sqrt{1-\epsilon^2}
       (\cos(n\phi)e_1+\sin(n\phi)e_2)+\epsilon e_{n+2},
 \qquad n\ge1.
\]

Then every vector has norm one and every distinct-lag correlation is

\[
 \langle v_n,v_{n+k}\rangle=(1-\epsilon^2)\cos(k\phi),\qquad k\ge1.
\]

These can be arbitrarily close to the correlations of a fixed rotation, while the vectors span an infinite-dimensional space.

More strongly, fix `L>0` and let `F(z)=sum_{n>=1}L^n v_n z^n/n^2`. The Hilbert-valued series has radius `1/L`. Its coordinate in direction `e_{n+2}` is exactly `epsilon (Lz)^n/n^2`. There is no Hilbert-valued analytic continuation through any point of the circle `|z|=1/L`: if such a continuation existed on a neighborhood crossing the circle, scalar coordinate uniqueness would force the same coordinate formula on that neighborhood, but for `|z|>1/L` those coordinates are not square summable. Thus approximate rotation correlations and a norm law `L^n/n^2` are compatible with a full boundary of singularities, including the positive-real point.

This is a counterexample to the statistical inference, not an IPM solution or an IPM divergence result. The IPM recurrence may impose further structure, but that structure must be proved or tested separately.

## Dependencies and evidence

Only elementary Gram projection, orthogonal coordinates and uniqueness of scalar analytic continuation are used. The original checkpoint is read without modifying it. Selected coefficient triples, file hashes, float diagnostics and the separate Arb interval projection check are retained under `sources` and `verification`. This topic does not claim any certified singularity location for the stationary IPM series.

## Interval projection certificate

Arb 2048-bit calculations from the retained 1024-bit coefficient balls give strict distances from the span of orders 572 and 573 greater than `0.0812` at order 574, `0.9994` at order 636, and `0.99999999` at order 700. These enclosures account for the checkpoint coefficient radii; they are conditional only on those source balls enclosing the recursion coefficients. The certificate is `verification/interval_projection.json`. This definitively excludes an exact common two-dimensional span for these finite vectors. It does not exclude an asymptotic model whose vectors or topology vary with order.
