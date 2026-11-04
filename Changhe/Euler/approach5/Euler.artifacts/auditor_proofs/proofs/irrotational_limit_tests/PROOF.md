# Two tests for approach to the irrotational set

## Nonrotating C2 profiles

Let U in C2(R3;R3), P in C1(R3), div U=0 and U=o(|y|) uniformly. Assume the nonrotating Euler profile equation

    (1-c)U+(cy+U).grad U+grad P=0,  0<c<1/2.

Set B=cy+U, Omega=curl U, k=1-2c, d=3c, and Psi_t=Phi_{-t} for the complete B-flow. Let K(x) be its compact backward limit. If K(x) is contained in {Omega=0}, then K(x) is contained in {B=0}.

This is an auxiliary C2 statement. The previously audited nonrotating Liouville theorem is stronger under these global profile hypotheses.

### Bernoulli function and its critical values

The equation makes grad P C1, so P is C2. Define

    H=P+|B|^2/2+c(c-1)|y|^2/2.

The verified Lamb identity gives grad H=-k B-Omega cross B. Let E={Omega=0, B=0}. At q in E, grad H(q)=0 and

    Hess H(q)=-k DB(q),    trace Hess H(q)=-kd!=0.

The derivative of Omega cross B vanishes because both factors vanish at q.

We need that H(E intersect K(x)) has one-dimensional Lebesgue measure zero, not a false general C2 Sard theorem in dimension three. At any q in E some diagonal entry H_ii is nonzero. Relabel so i=3. The C1 implicit-function theorem puts the nearby set {H_3=0} on a C1 graph y3=g(y1,y2). Define h(y1,y2)=H(y1,y2,g(y1,y2)). On that graph H_3=0, hence h_j=H_j composed with the graph for j=1,2. These derivatives are C1, so h is C2. Points of E on the graph give critical points of h. The two-dimensional C2 Morse-Sard theorem shows their H-values form a null set. A finite chart cover of compact E intersect K(x) proves the assertion.

### Chain-transitivity argument

A compact omega-limit set of a precompact continuous flow trajectory is connected and internally chain transitive. To verify the latter, fix p,q in K, an error epsilon and a minimum time T. Take a sufficiently late visit near p and a later visit near q. Partition their time separation into intervals between T and 2T. The tail is uniformly close to K. Approximate its partition points by points in K, use p and q at the ends, and use uniform continuity of the flow for times in [T,2T]. This produces an epsilon-chain in K from p to q.

On K subset {Omega=0}, the function L=-H satisfies

    d/dt L(Psi_t y)=-k |B(Psi_t y)|^2<=0.

If L were nonconstant on connected K, its range would contain an interval. Since L(E intersect K) is null and compact, choose an interior value r of that range and delta>0 so that [r-2delta,r+2delta] avoids L(E intersect K). The compact part of K with values in this strip contains no zero of B, so k|B|^2 has a positive minimum there.

There is eta>0 such that every y in K with L(y)<=r satisfies L(Psi_t y)<=r-eta for all t>=1. Indeed points with L(y)<=r-delta already have this property; points above that threshold either cross below r-2delta during the first unit of time or spend the entire unit in a strip with a uniform strictly negative derivative. Nonincrease handles all later times. Choose chain errors so each jump changes L by less than eta/2. A chain with flight times at least one starting below r can never cross r. This contradicts internal chain transitivity between points on opposite sides of r. Therefore L is constant on K, and its derivative forces B=0 on K.

## Flat zeros and exponential approach

Let B be a C1 complete field and Psi its backward flow. Suppose |DB(Psi_t x)|<=A for t>=0. Let W be smooth on a neighborhood of a compact set K and on the trajectory, obeying

    W(Psi_t x)=exp(kappa t)D Psi_t(x)W(x).

Assume every derivative of W vanishes at every point of K and dist(Psi_t x,K)<=C exp(-delta t), delta>0. Then W(x)=0.

The inverse variational equation and Gronwall give the smallest singular value of D Psi_t(x) at least exp(-At). Thus

    |W(Psi_t x)|>=exp((kappa-A)t)|W(x)|.

For each integer N>=1, Taylor's formula and compactness give a uniform bound |W(y)|<=C_N dist(y,K)^N near K. Choose a nearest point of K; the segment to y lies in a fixed compact neighborhood for y sufficiently near K, and the order-N derivatives there are bounded. Combining the two estimates yields

    |W(x)|<=C'_N exp((A-kappa-N delta)t).

Choose N delta>A-kappa and let t tend to infinity.

## Dependencies and limits

These arguments verify Sections 2 and 4 of in the team records. The nonrotating statement uses the exact Euler Lamb identity; the flat-zero statement uses only transport, a derivative bound, flatness on the WHOLE approached set, and exponential approach. A089 does not supply either of the latter two global properties for arbitrary smooth backward limits. No rotating smooth exclusion is inferred. Verdict: A187 CONFIRMED with the hypotheses above.
