# Exact rational endpoint checks for the finite angular tree

Status: analytic proof before implementation. The numerical membership claim remains conditional on complete execution.

## Statement and notation

For z in(0,1), define S(z)=sum_{k=0}^{99} (-1)^k z^{2k+1}/(2k+1) and T(z)=z^{201}/201. Set L=16S(1/5)-4(S(1/239)+T(1/239)) and U=16(S(1/5)+T(1/5))-4S(1/239). Then L<pi<U. These are exact rational numbers.

For the finite cells with integers0<=l<r<=25600, width r-l in{1,2,4,8,16,32,64,128} and l divisible by r-l, let a=l*pi/51200, b=r*pi/51200 and h=(r-l)*pi/102400. Suppose each recorded endpoint ball is represented exactly by dyadic midpoint m and nonnegative dyadic radius q. If m-q<=l*L/51200 and l*U/51200<=m+q, it contains a. The corresponding two inequalities with r certify b. If a positive exact binary64 d satisfies d>=(r-l)*U/102400, then h<=d. The same argument works when l=0, with equality permitted. These are sufficient tests, with no floating conversion of rational comparison endpoints.

## Proof

Write A=arctan(1/5), B=arctan(1/239). Since0<A<pi/4 and tan(2A)=5/12<1, one has0<2A<pi/4 and hence0<4A<pi/2. Also0<B<A, so0<4A-B<pi/2. The tangent double-angle formula gives tan(4A)=120/119. Subtracting B gives tan(4A-B)=(120/119-1/239)/(1+(120/119)/239)=1. Tangent is strictly increasing on(-pi/2,pi/2), so4A-B=pi/4. Thus pi=16A-4B.

Integrating the finite geometric-series identity for1/(1+t^2) from0 to z yields the alternating arctangent expansion with a remainder of the sign of the first omitted term and magnitude less than that term. There are100 terms in S, ending with the negative term of degree199. Therefore S(z)<arctan(z)<S(z)+T(z). Multiplying the1/5 bounds by16 and the1/239 bounds by-4 gives L<pi<U. All arithmetic in the definitions is rational and can be done exactly.

Multiplication by a nonnegative rational preserves the interval order. Thus l*pi/51200 lies between l*L/51200 and l*U/51200. If the entire latter interval belongs to[m-q,m+q], so does the exact endpoint. The r endpoint and positive half-width follow in the same way. This proves the sufficient tests.

## Remainder-table use and scope

For the functions c_n,C_n,S_n of research/flow_angular_full/PROOF.md and1<=n<=261, the third derivative majorants are8n^3 for c_n and4n^2(n+1)^2 for C_n,S_n. The source uses the larger integer4n^4+8n^3+6n^2+2n for the latter. Taylor's theorem gives a remainder bound M*d^3/6 whenever h<=d. Exact rational comparisons against each of the8 by2 by261 stored binary64 remainder entries therefore certify all4176 distinct sufficient inequalities, provided the actual regenerated arrays match these tables. That last linkage is checked for every row by the existing full source replay and the additional saved-record audit.

This proof certifies the meaning of the rational pi and remainder tests. It does not itself establish that any saved ball passes them. Complete acceptance additionally requires every actual endpoint, width and table comparison, all three existing angular numerical engines and the actual output review. No historical numerics-lane run, radial field, physical derivative, inverse or IPM endpoint is certified here. Dependence on the angular majorant proof and the exact binary64 source meanings is explicit. Python exact integers and Fraction arithmetic are trusted computational dependencies; no formal verification is claimed.
