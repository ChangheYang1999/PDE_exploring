# Transfer of the b6 point exclusion to stationary-inverse boxes

## Statement

Use the fixed b6 reference, its fixed c, and the point X=(0,1). The independently confirmed point inequality for a stationary correction with ||h||_(H^(2+s))<=R is

    |F(X)| <= b(s,R)|V(X)|+a(s,R)(1+|D rho(X)|)+a(s,R)b(s,R),
    a(s,R)=R/[4 pi(1+s)]^(1/2),
    b(s,R)=R/[8 pi s(1+s)]^(1/2).

The hypotheses, canonical velocity, S1 normalization and Sobolev embeddings are exactly those of ../sharp_point_remainder_audit/PROOF.md. At s0=1/8192, R0=43/50000 the confirmed positive gap is greater than2.9392836795. Every pair in the seven-row exact parameter record ../transient_constant_audit/verification/results.json has a gap at least this large. Thus each of these seven fixed-c correction balls is excluded for b6. No inverse estimate or sufficient background hypothesis is needed for this necessary test.

## Proof

The factors |V| and1+|D rho| are nonnegative. The squared ratios of the two coefficients are

    a(s,R)^2/a(s0,R0)^2 = R^2(1+s0)/[R0^2(1+s)],
    b(s,R)^2/b(s0,R0)^2 = R^2 s0(1+s0)/[R0^2 s(1+s)].

If each ratio is at most1, both coefficients and their product are no larger than at the already excluded pair. Hence the new necessary right side is no larger, proving the gap comparison.

The independent verification does not copy the peer's ratios. It reads our original exact seven parameter pairs, forms the positive differences R0^2/(1+s0)-R^2/(1+s) and R0^2/[s0(1+s0)]-R^2/[s(1+s)], checks both strictly positive, and then compares the recovered ratios exactly with the peer record. The former point certificate is checked from our independently reproduced output. All arithmetic before the inherited point gap is rational. This completes the finite comparison proof.
