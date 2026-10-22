# Interior velocity from finitely many compensated exterior modes

Status: complete informal argument written before the new computation.
Decimal consequences remain conditional until the stated independent audit.
This result concerns only the explicit topic106 repair family.

## 1. Exact definitions, hypotheses and claim

Let rho0 be the exactly normalized modal trial of topic15 and let
k=1615536043799051/9007199254740992, c0=1/k, R_b=exp(tplus), with tplus
and L the original exact dyadic data. The established input has 0<k<1/4.
Use the exact family of hminus1_tail_repair/PROOF.md, with its addenda.
For i=1,2,d put a1=2k-1, a2=3k-2, ad=k-2. Its angular corrections are
H1=A1-D1, H2=A2-D2, Hd=-Dd, where the physical D rows and canonical
ordered Green products are defined there and quantitatively audited in
hminus1_tail_quantitative. These are exact real finite expressions, not
rounded coefficients. Write

 Hi(theta)=sum_(n=0)^Mi h_(i,n) sin((2n+1)theta)
          =cos^2(theta)sin(theta) sum_m q_(i,m)cos(2m theta),
 Ni=sum_m |q_(i,m)|.

The maximal sine indices are M1=521, M2=782, Md=260. Missing coefficients
are zero. Use b(s)=(s-1)^8(2-s)^8 on[1,2], zero outside,
B0=int_1^2 b(s)ds, Jb=int_1^2 s b(s)ds=1/145860, and chi equal to
B0^-1 int_1^s b on[1,2], zero below1 and one above2. Let

 Ii=h_(i,1), Ji=int_1^infinity chi(s)s^(ai-2)ds,
 h_T=sum_i [chi(r/T)r^ai Hi(theta)
           -(4 Ii Ji/Jb) T^(ai-3) x^2 y b(r/T)],
 rho_T=rho0+h_T, u_T=U[h_T], T>=max(R_b,L,1).

The canonical full-plane inverse solves -Delta psi=partial_x h_T,
U=(-psi_y,psi_x), with parity and sublinear velocity, as in topic106.
Each row has exactly zero canonical center strain. The density correction
vanishes on r<=T. Center density regularity is C4, not C5 in general;
existing joins at positive radii are C6. No fifth center derivative is used.

Fix R>0, 2R<=T, j=0,1,2,3, and q=(R/T)^2. Define

 A_(i,j)(R,T)=R^(3-j) T^(ai-3)
  sum_(n=2)^Mi [n(2n-1)_j |h_(i,n)|/(2n-ai-1)] q^(n-2),       (1)

where (v)_j is the falling factorial, with (v)_0=1. Then every velocity
component ell and Cartesian multiindex alpha of length j satisfy

 sup_(|X|<=R) |partial^alpha (u_T)_ell(X)| <=sum_i A_(i,j).    (2)

A distinct, deliberately coarser upper bound is

 B_(i,j)(R,T)=R^(3-j) T^(ai-3)
 [2(3)_j |h_(i,2)|/(3-ai)+(Ni/2)m(ai) q Zj],                  (3)
 m(a)=max(1/2,2/(3-a)),
 (Z0,Z1,Z2,Z3)=(4/3,68/9,1016/27,4600/27).

One has A_(i,j)<=B_(i,j). Thus (2) also holds with the sum of B.
The two majorants need not have overlapping numerical enclosures.

We will evaluate both independently at R=9, T=3000. This is only a
conservative comparison scale, since the admissible R_b exceeds3000.
If their independent upper bounds for j=0 and1 are each below1e-8,
then every admissible member of this family has

 |partial_y F(rho_T,c0)(P)|>3.69e-7,                         (4)

at the original trial source P=(p,0). No numerical success of this test
is asserted until the full audit. Formulae (1)-(3) remain valid if it fails.
The point P need not remain a source of the changed velocity.

## 2. Reconstructing the interior canonical Green formula

For any finite sine density sum D_n(r)sin((2n+1)theta), the sin(2n theta)
coefficient of its x derivative is

 f_n=(D'_(n-1)+D'_n)/2
       -[(2n-1)D_(n-1)-(2n+1)D_n]/(2r).

For a density vanishing on r<=T, the canonical Green formula in r<T is
psi_n(r)=r^(2n)/(4n) int_T^infinity s^(1-2n) f_n(s)ds.
Integrating the derivative terms by parts cancels the D_(n-1) integral
and leaves 2n times the D_n integral. Boundary terms vanish at T and
at infinity, since the cutoff vanishes at T and every ai<1. Hence

 psi_n(r)=(r^(2n)/2) int_T^infinity s^(-2n)D_n(s)ds.

For one tail row this equals
(h_(i,n)/2) r^(2n) T^(ai-2n+1) J_(ai,n), where
J_(a,n)=int_1^infinity chi(s)s^(a-2n)ds lies in(0,1/(2n-a-1)].
The compensator has only density sine frequencies1 and3. It therefore
changes only interior n=1. Its strain is exactly the tail strain:
Ii Ji T^(ai-1), because sigma[x^2 y b(r/T)]=T^2 Jb/4.
The complete n=1 term is strain times xy. Thus compensation removes
it identically, leaving exactly the finite modes n>=2.

Writing z=x+iy, their stream terms are
(h_(i,n)/2) T^(ai-2n+1) J_(ai,n) Im(z^(2n)). The velocity terms are
n h_(i,n) T^(ai-2n+1) J_(ai,n)
                  (-Re(z^(2n-1)), Im(z^(2n-1))).
For |alpha|=j, partial^alpha z^m=i^(alpha_y)(m)_j z^(m-j).
Since n>=2 and j<=3, these powers have nonnegative exponents, including
at the origin. Taking absolute values and factoring R^(3-j)T^(ai-3)
proves (1)-(2). Only finite harmonic polynomials are differentiated.

## 3. Bounding the higher modes by the quotient coefficient sum

The base angular factor is (sin(theta)+sin(3theta))/4. Multiplication
by cos(2m theta) and product-to-sum produce four signed sine terms,
each with coefficient of magnitude |q_m|/8. This includes m=0, where
duplicate terms combine; negative frequencies are replaced by their
negative positive-frequency sine. Combining duplicates or cancellation
cannot increase the sine coefficient absolute sum. Therefore

 sum_n |h_(i,n)| <= Ni/2, and in particular |h_(i,n)|<=Ni/2.

Separate n=2 in (1). For n>=3 and a<1,
n/(2n-a-1)<=m(a): the ratio decreases to1/2 when a+1>=0 and increases
to1/2 when a+1<0. Since q<=1/4,

 sum_(n>=3) (2n-1)_j q^(n-2)
 <=q sum_(m>=0)(2m+5)_j 4^(-m)=q Zj.

This proves (3) and A<=B. The infinite series is only a positive
majorant for a finite sum; it introduces no unknown Fourier tail.
Its exact values follow from the geometric moments at x=1/4:
sum x^m=4/3, sum m x^m=4/9, sum m^2 x^m=20/27,
sum m^3 x^m=44/27. Expanding the falling factorial gives the stated Zj.
These moment identities follow by applying x d/dx repeatedly to 1/(1-x).
An independent rational positive partial sum with a proved polynomial
geometric tail will also check them.

## 4. Uniform admissible-cutoff consequence

For fixed R, every summand of (1) decreases as T increases, since its
T power is ai-2n+1<0. Each term of (3) also decreases: its two powers
are ai-3 and ai-5, both negative. Thus a validated bound at3000 applies
at every admissible T, once exact input bounds R_b>3000 and L<=R_b
have been checked. The old source certificate gives 0<p<9 and

 D=|F_y(rho0,c0)(P)|>6.70197e-7, |g|+|g'|<30.0230,
 g=rho0_y(P), g'=rho0_xy(P).

Near P the density correction and all its derivatives vanish. The
canonical scalar remains c0. Differentiating the exact residual
change u_T dot grad rho0 on the axis, using parity, yields

 F_y(rho_T,c0)(P)-F_y(rho0,c0)(P)=g partial_y(u_T)_2(P)+g'(u_T)_1(P).

If both indicated jets have magnitude<1e-8, the triangle inequality
gives D-30.0230*1e-8>3.69e-7, proving (4). This uses local regularity
near the positive-axis point, where rho0 is C6. It needs no assertion
that P is a source of the new velocity and no global inverse estimate.

## 5. Dependencies, numerical audit and scope

The whole frozen pin map for topic113, its original NPZ and exact JSON,
normalization and leading-row certificates are rehashed. Arb constructs
H1 and Hd directly from exact JSON and uses all783 previously audited
physical H2 coefficient enclosures from its independent113 engine.
It evaluates the complete finite sum (1), including every coefficient.
A separately coded mpmath.iv computation uses the original NPZ,
independent leading-row and H2 certificates, and evaluates (3), using
its own exact projection for h_(i,2) and its own Ni enclosure.
Original binary data and exact exponents are compared independently.

Every printed strict ceiling must contain each method's corresponding
upper bound. The methods evaluate different sufficient majorants, so
agreement of output intervals is not a validation criterion. Exact
integer/rational audits check the projections, finite support, falling
factorials, denominator signs, geometric identities and polynomial-tail
remainder. Full scripts are replayed into new local output files, with
no mutation of prior frozen evidence. Actual Opus5.5 review and any
availability limitation are recorded before a final verdict.

The possible nonzero defect belongs to this one explicit repair family.
The correction may itself be changed. No surrounding neighborhood of
X3 or of rho_T is excluded, and no stationary solution, bounded inverse,
small global forcing norm, or decisive task endpoint follows.
