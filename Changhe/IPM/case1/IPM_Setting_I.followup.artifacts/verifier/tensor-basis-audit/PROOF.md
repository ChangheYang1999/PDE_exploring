# Exact binary tensor basis and center-moment checks

Date: 2026-10-20. Status: complete informal argument before implementation. This is a manufactured finite-formula audit, not a PDE existence proof.

## Statement

Let the ideal radial grid be z_j=-cos(pi*j/N), j=0,...,N, so q_j=(1+z_j)/2 is increasing from0to1. Let c_a=cos(pi*(2a+1)/(2M)), a=0,...,M-1. The tensor interpolant of nodal data b_(j,a) has coefficients C_(n,m) in T_n(z)T_m(c). The implementation reverses the radial rows and applies the ordinary Lobatto cosine transform, with both input and output endpoint weights1/2, and the angular Gauss transform, with output factor1/M for m=0 and2/M otherwise.

The following exact binary nodal tests recover the indicated single coefficient exactly, in the sense that the rigorous interval coefficient contains the exact target and all other coefficients contain zero:

1. N=2,M=3, b=1, coefficient(0,0)=1.
2. N=2,M=3, radial column(-1,0,1) constant in a, coefficient(1,0)=1.
3. N=2,M=3, radial column(1,-1,1) constant in a, coefficient(2,0)=1.
4. N=2,M=3, angular row(1/2,-1,1/2) repeated in j, coefficient(0,2)=1.
5. Products of radial columns in2or3 with row4 give coefficients(1,2)or(2,2).
6. N=4,M=3, radial column(1,-1,1,-1,1), with or without row4, gives coefficient(4,0)or(4,2).

All stated samples are exact binary64 values, although some ideal coordinates are irrational. Tests2and5check orientation. Tests3and6check the radial top-degree normalization, and tests4to6check the angular top-degree normalization.

For the canonical density convention of ../center-moment/PROOF.md, set L=2,c_l=6,k=1/6,beta=0 and eta=1/8. Each of the following satisfies b(0,s)=1:

    b=1+eta*(T2(z)-1)*T2(c): c=13/10,
    b=1+eta*(T1(z)+1)*T2(c): c=9/8,
    b=1+eta*(T4(z)-1)*T2(c): c=32/25.           (1)

The first two can be represented on N=2,M=3, the last on N=4,M=3. This provides end-to-end tests of exact samples, transform, radial moment and angular signs, distinct from constant-nodal-data tests.

## Proof

For reversed index j'=N-j, z_j=cos(pi*j'/N). Lobatto discrete cosine orthogonality gives

    sum_(j'=0)^N w_(j') cos(n*pi*j'/N)cos(k*pi*j'/N)
       =N/(2*w_n) if n=k, and0 otherwise,

where w_j=1/2 for j=0,N and1 otherwise. Thus the radial transform multiplier is2*w_n*w_(j')/N. The angular midpoint cosine sum is M for n=m=0, M/2 for n=m>0 and0 for distinct n,m in0,...,M-1. Its inverse multiplier is1/M at m=0 and2/M otherwise. The tensor product therefore recovers each polynomial of degrees at most N and M-1 exactly.

At N=2, the ascending z nodes are(-1,0,1). Their T1 and T2 values are respectively(-1,0,1) and(1,-1,1). At M=3, the angular arguments are pi/6,pi/2,5pi/6, so T2(c)=cos twice those arguments is(1/2,-1,1/2). At N=4, T4(-cos(pi*j/4))=(-1)^j. These exact identities prove every coefficient target above.

For beta=0, the angular moments are Omega0=1/4 and Omega2=-1/8. The radial moments of T0,T1,T2,T4 are1,0,-1/3,-1/15. The common factor L^2/(1-k) is24/5. The three values in(1) follow by linearity:

    (24/5)[1/4+(1/8)(-1/3-1)(-1/8)]=13/10,
    (24/5)[1/4+(1/8)(0+1)(-1/8)]=9/8,
    (24/5)[1/4+(1/8)(-1/15-1)(-1/8)]=32/25.

Their center row is identically1 because T2(-1)=T4(-1)=1 and T1(-1)=-1. The center-moment theorem therefore applies. Its canonical inverse and integral derivation are dependencies, not claims established by these tests.

## Verification and scope

Run the separately written code under code/. It imports the pinned verifier transform and moment implementation, never numerical-lane code. The expected nodal tables and rational outputs are generated from these small exact identities. A second diagnostic differentiates a nonzero-warp manufactured scalar density with arbitrary-precision implicit inversion, independently of the Cartesian chain-rule implementation. That diagnostic is not an interval proof. The two analytic formulas and the original interval arithmetic argument remain the soundness basis.

Candidate dtype inspection records the input parameters and shape metadata without changing the shared certificate interface during running jobs. Tests cannot prove an implementation correct on all inputs; they resolve specific unexercised basis and orientation cases raised in the external code review. No numerical result here is a PDE proof or an error bound for the off-center full-plane inverse.


## Additional nonzero angular first mode

For M=2, c=(1/sqrt2,-1/sqrt2). The exact binary samples(1,-1) interpolate sqrt2*T1(c). Repeating this row at N=2 gives coefficient C_(0,1)=sqrt2 and zero for every other coefficient. This tests a nonzero angular first mode, including its normalization.

For L=2,c_l=6,beta=0, the nodal samples of

    b=1+(1/8)(T2(z)-1)*sqrt2*T1(c)

are exact dyadic numbers and the center row is1. Since Omega1=1/8, its canonical center moment is

    (24/5)[1/4+(1/8)(-1/3-1)*sqrt2*(1/8)]
       =6/5-sqrt2/10.

These are exact algebraic targets enclosed by Arb sqrt2. This additional check uses the same soundness dependencies and does not strengthen the scope beyond those stated above.
