# A full growing profile with two expanding carrier directions

Status: independent reconstruction and existing coordinator comparison complete. The example is a full profile, but it is not bounded or decaying.

## 1. Exact claim

Let J(y1,y2,y3)=(-y2,y1,0), and consider the entire profile equation

    (1-c)U+DU[(cI-omega J)y+U]+omega JU+grad P=0,
    div U=0.

For the fixed omega=2sqrt(5), the analytic fields below solve this equation for every real c. Their pressure has a strict global minimum at zero and positive definite Hessian. For every 0<c<1/2, the carrier B=(cI-omega J)y+U has a two-dimensional forward unstable subspace and a one-dimensional forward stable subspace at zero. Thus pressure positivity and the complete equation alone do not force at most one expanding carrier direction.

No decay, boundedness, sublinearity or arbitrary-omega family is asserted. The final interval can include every c in the campaign, but that does not make the example a counterexample to the campaign conjecture.

## 2. Frame and full equation

Put e=(1,0,2)/sqrt(5), f=(0,1,0), g=(-2,0,1)/sqrt(5), E=[e f g] and x=E^T y. These unit vectors are orthogonal and e cross f=g, so E is orthogonal and orientation preserving. Since omega Je=2f, omega Jf=-2e+4g and omega Jg=-4f, the rotation generator in this frame is

    R=E^T(omega J)E=[[0,-2,0],[2,0,-4],[0,4,0]].

Define

    M=[[1,2,0],[2,-7/2,-53/8],[0,51/8,5/2]],
    U(y)=E M x,
    H=[[2,-6,-8],[-6,1311/64,24],[-8,24,2207/64]],
    P(y)=(1/2)x^T Hx.

The trace of M is zero. In the frame the full velocity residual without grad P equals

    [(1-c)M+M(cI-R+M)+RM]x=[M+M^2+[R,M]]x.

All c terms cancel. To check the remaining multiplication explicitly,

    M^2=[[5,-5,-53/4],[-5,-1663/64,53/8],
         [51/4,-51/8,-2303/64]],
    [R,M]=[[-8,9,85/4],[9,9,-24],[-19/4,-24,-1]].

These give -M-M^2-[R,M]=H entry by entry. Thus the full equation, not merely its divergence or curl, holds. The curl in this oriented frame is (M32-M23,M13-M31,M21-M12)=(13,0,0), so curl U=13e.

## 3. Strict pressure minimum

With v=(1,-3,-4) and d=159/64,

    H=2vv^T+d diag(0,1,1),
    P=(x1-3x2-4x3)^2+(159/128)(x2^2+x3^2).

If P vanishes, x2=x3=0 and then x1=0. Hence P is positive away from zero. This proves a strict global minimum and positive definite Hessian without an eigenvalue approximation. The leading principal minors are 2, 2d=159/32 and 2d^2=25281/2048. Adding a pressure constant does not affect these conclusions; the displayed normalization has P(0)=0.

## 4. Carrier spectrum and complete linear flow

In the frame, the carrier matrix is

    C=cI-R+M=[[1+c,4,0],[0,c-7/2,-21/8],
             [0,19/8,c+5/2]].

The lower block has scalar center c-1/2. Subtracting that center gives a trace-zero matrix whose square is (177/64)I, since 9-399/64=177/64. Thus the three eigenvalues are

    1+c, c-1/2+sqrt(177)/8, c-1/2-sqrt(177)/8.

For 0<c<1/2 the first two are positive and the third is negative. The middle sign uses sqrt(177)/8>1/2; the last is immediate. The first eigenvalue differs from the second since sqrt(177)/8 differs from3/2, and differs from the third since their difference is3/2+sqrt(177)/8. The lower two are distinct. The matrix is therefore diagonalizable over R.

The exact flow x(t)=exp(tC)x(0) exists for all real t. Expansion in this real eigenbasis shows that the points converging to zero as t tends to minus infinity form exactly the span of the two positive-eigenvalue vectors. Forward convergence occurs exactly on the negative-eigenvalue line. In particular the backward-captured set is a proper plane and has three-dimensional Lebesgue measure zero. There is no conflict with an equilibrium-capture nullity theorem.

## 5. Additional comparison checks and scope

The center curl relation is MW=W+RW because W=13e1 and Me1=e1+Re1. The strict angular quantity is omega^2|Je|^2=20/5=4>2. The vorticity norm13 is above the independently proved uniform threshold: 169>59+24sqrt(6), for instance because sqrt(6)<5/2.

The coordinator's optional larger sign interval is also correct. The three necessary inequalities are c>-1, c>1/2-sqrt(177)/8 and c<1/2+sqrt(177)/8. Since sqrt(177)/8>3/2, the second lower endpoint is below-1, so the exact interval for this sign pattern is

    -1<c<1/2+sqrt(177)/8.

The optional construction history agrees with the previously checked central matrix family. At k=2, v=4, eta=-3, xi=-1/8, its Schur data are h=(-1,24), tau/2=31, and y=(-1/8,3)=h/(2v). Thus K_min=31+577/64=2561/64, in the second branch because |h|=sqrt(577)<32=2v^2. Raising K to (1+13^2)/4 adds159/64 to the lower diagonal block and gives the displayed positive definite H. This historical identification is not a dependency of Sections2-4.

The field U is nonzero and linear, so it grows linearly on every ray not contained in ker M. No claim about the original decaying class follows. The counterexample excludes only the universal local implication from a pressure minimum to at most one expanding carrier direction. No existing confirmed theorem asserting that implication was identified.

## 6. Verification boundary

All six source sections, all four coordinator comparison items and W1-W4 were read. The source's fourteen exact checks and the coordinator's eighteen exact checks were inspected, not rerun. The full matrix multiplication, pressure positivity, spectral signs and flow interpretation were independently reconstructed above. Source hashes and retained comparisons are in verification.

The only source revision suggested by the comparison is status: LIT328 is already confirmed, so calling it pending is outdated. That result is not used to prove the example. Existing configured model collaboration was through the coordinator's files; actual provider execution was not independently attested. No mathematical computation, formal build, server or external publication was performed by this audit.


## 7. Source status revision

The complete delta from the archived submission to current source SHA256 7c96935d2692cec3395c4cf6da8c6020d2286aadbdef4cd68031850bb101b42c was read. The revision changes status and adds Section7. The optional interval and second-branch construction history reproduce Section5 above exactly; the fixed rotation rate and growing character are retained. It adds no pressure or decay implication.

All added reading-scope statements distinguish this audit from the submitting agent's own reading. The retained delta and hashes are in the team records and in the team records. This revision needs no new mathematical computation.
