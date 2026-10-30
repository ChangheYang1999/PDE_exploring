# Independent pointwise exclusion for two published parameter boxes

## Statement

Use the fixed-c stationary IPM residual F(rho;c)=(cX+U[rho]).grad rho-rho, the S1 parity class, the canonical velocity U=(-R1R2,R1²), and J=(1-Delta)^(1/2). Let V=cX+U[rho]. Fix0<s<1 and suppose a correction h satisfies ||h||_(H^(2+s))<=R. If rho+h solves the stationary equation, then at every point X

|F(X)| <= [C1 |V(X)|+C0(1+|grad rho(X)|)] R+C0 C1 R²,     (1)
C0=[4pi(1+s)]^(-1/2), C1=[8pi s(1+s)]^(-1/2).

For each of the exact references d2, Mpen2 and b6 specified by the canonical hashes in source/N4_cartesian_witnesses.json, the already independently confirmed field intervals violate(1) at the indicated axis point for both parameter boxes:

1. Rebalanced scalar ball: s=1/65536, R=3/32768.
2. T4 graded ball: s=1/50000, component bounds(P,a,b)=(1/5000,1/3000000,1/50000000), and R=sqrt(P²+2a²+b²).

Thus no stationary correction exists in either specific ball around any of these three references. This is a necessary-condition exclusion independent of whether the background satisfies a sufficient inverse theorem. It makes no assertion about other graded boxes or corrections outside these radii.

## Proof of the necessary condition

With Fourier inverse normalization(2pi)^-2, Cauchy-Schwarz gives

|h(X)|, |U[h](X)| <=C0 ||h||_(H^(2+s)),
|grad h(X)|<=C1 ||h||_(H^(2+s)).

For the velocity inequality, every unit projection of its vector symbol has modulus at most one. For the gradient inequality use any unit directional derivative. The exact squared kernel integrals are(2pi)^-2 integral <xi>^(-4-2s)d xi=1/[4pi(1+s)] and(2pi)^-2 integral |e.xi|²<xi>^(-4-2s)d xi=1/[8pi s(1+s)]. Radial integration and angular isotropy evaluate them directly. Taking the supremum over unit e controls the Euclidean gradient.

Expanding the corrected stationary equation gives

0=F+V.grad h-h+U[h].grad rho+U[h].grad h.

Apply the preceding bounds to each term to obtain(1). Equivalently every such correction must have radius at least2|F|/(A+sqrt(A²+4B|F|)), where A=C1|V|+C0(1+|grad rho|) and B=C0C1.

For the scalar ball, its weighted high norm dominates H^(2+s), because omega>=1 and its Fourier quadratic terms dominate |xi|^4+2|xi|²+1. Thus R=3/32768 is a valid upper bound. For the graded ball, Plancherel gives

||h||_(H^(2+s))²=||D²J^s h||²+2||DJ^s h||²+||J^s h||²<=P²+2a²+b².

The negative-norm component is unnecessary for this implication.

## Arithmetic and evidence

The code independently constructs C0,C1,R and both sides of(1) at512-bit Arb precision from the exact radii and the saved confirmed field intervals. It does not import N4's postprocessing code. It confirms strict positive gaps, approximately

| reference | rebalanced scalar ball | specified graded ball |
|---|---:|---:|
| d2 at(0,1) |0.00620093765682|0.00109819662480|
| Mpen2 at(0,2) |0.0622984673420|0.0512891303099|
| b6 at(0,1) |2.95295824689|2.94809688558|

The full intervals and overlap checks against N4's independently produced postprocessing are in verification/reproduction.json. The underlying fields were calculated twice previously, with different radial and Cartesian evaluators; this audit reuses those certified enclosures and does not count as a third field evaluation. The analytic inequality was independently confirmed by both Opus theory lanes as T4-007. The only new work here is its application to these two boxes and independent scalar arithmetic.
