# Candidate022: complete generator space and recorded probe history

## Exact statement

Fix c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma,
S=1+x^2+y^2, H_m=Re(x+iy)^(2m), p_j=(3+gamma-j delta)/2 and
v=1/S. The candidate is C1-N1-022-legqs25-m16to23 with raw SHA256
85c7e4e2c060f1124f2f1d77a2b7f07cd67b32849bd849c1e0a2ec8aa85ce75f.
Its immediate parent is the phase-one raw JSON with SHA256
2a13c07969eb37af27c68a0336fa7f28a9f1747119e1f7ad4623302f58d5fd4f.
That phase started from candidate016, raw SHA256
a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42.

The complete shape list is the accepted1922-function quotient basis
of013 plus492 functions

 H_m S^(p_j-m) [625/(625+r^2)]^4
       P_N(2r^2/(625+r^2)-1),

where P_N is the Legendre polynomial with P_N(1)=1, N=0,...,11,
j=1,m=9,...,19 or j=2,3,m=9,...,23. This is41 blocks of12 functions.
The240 functions added to016 are j=1,m=16,...,19 and j=2,3,m=16,...,23.
The potential dimension is2414 and the density map
chi -> -partial_y Delta chi is injective on this space. This conclusion
uses the accepted rank and density-injectivity hypotheses of013 and the
exact nonintegrality checks in N4-306. It is a statement about the whole
function space, not the rank of a sampled matrix or a conditioning bound.

The added density functions have Fourier frequencies contained in
{31,33,...,47}; mode31 actually occurs among those functions. Thus the
immutable manifest's statement that this whole support lies outside the
N4-160 sweep through31 is false. Its intersection with that sweep is31.
No assertion that every such frequency has a nonzero fitted coefficient
or survives in the residual is made.

For odd n>0 and integer K>=(n-1)/2, set

 phi_(n,K)=r(1+r^2)^(-2) t^K sin(n theta), t=r^2/(1+r^2).

The two recorded stages use the same67 analytic objective rows as016:
27 first-mode exponents

 0,1,2,3,4,5,6,7,8,12,16,24,32,48,64,96,128,192,256,384,512,
 768,1024,1536,2048,3072,4096,

and40 pairs with n=3,5,...,17 and K=(n-1)/2+s, s=0,8,32,128,512.
Each of the25 public registered pairs n in{19,23,25,29,31} and
K in{600,900,1200,1800,2400}, and each of the35 diagnostic pairs
n=19,21,...,31, K=(n-1)/2+s, s=0,8,32,128,512, lies outside their
real analytic span. This holds throughout the recorded history
007 ->013 ->exact quotient ->016 ->022 phase1 ->022 phase2. It says
nothing about unrecorded experiments, statistical independence,
blindness or independence from sampled residual values.

## Proof of potential independence

Angular orthogonality separates cos(2m theta). At fixed m a finite
relation is a sum of v^(-p_j)Q_j(v), with rational Q_j analytic near0.
The exact p_j are nonintegers and p_j-p_k are nonintegers for j!=k.
If Q_j is nonzero it has a finite integer order e_j at0. Thus the
leading exponents e_j-p_j are distinct. Divide by the unique smallest
power and take the positive v->0 limit. Its nonzero coefficient cannot
vanish, a contradiction. All branches therefore separate.

Put a=624, L(v)=1+av and v0=-1/a. Within a separated branch the scaled
radial function is

 A_mN(v)=625^4 v^4(1-v)^m P_N(2(1-v)/L(v)-1)/L(v)^4.

The leading Legendre coefficient is 2^(-N) binom(2N,N), by Rodrigues'
formula. Consequently A_mN has pole order4+N at v0 and nonzero leading
Laurent coefficient

 625^4 v0^4 binom(2N,N)(1-v0)^(m+N)/a^(4+N).

All quotient radial polynomials are analytic at v0. In a relation
choose the greatest N with a nonzero scaled coefficient. Its highest
pole cannot cancel. Descending induction removes every scaled term;
accepted quotient independence removes the rest. There are1922+492
independent functions. The negative pole is used only in rational
identities after fractional branch separation, not as a value of the
physical noninteger power S^p.

## Proof of density injectivity

Every potential is smooth, even separately in x and y, and satisfies
|D^k chi|=O(r^(3+gamma-k)) for0<=k<=4. The scaled terms decay eight
powers faster. Since3+gamma<4, D^4 chi tends to zero. Suppose
partial_y Delta chi=0. Then Delta chi=f(x). For fixed x, send |y| to
infinity in f''(x)=partial_xx Delta chi(x,y). This gives f''=0, and
evenness gives f=K constant. The function h=chi-Kr^2/4 is entire
harmonic, separately even and grows at most like r^(3+gamma).
The interior harmonic derivative estimate on a radius-L disk about
any fixed point gives |D^4h|<=C L^-4 sup|h|=O(L^(gamma-1)). Taking
L->infinity proves D^4h=0. Thus h is a polynomial of degree at most3;
evenness and harmonicity reduce it to A+B(x^2-y^2).

Therefore chi is a separately even quadratic polynomial. Its angular
radial coefficients are integer Laurent polynomials in v. The original
potential is a sum of distinct noninteger fractional branches. The
same least-exponent argument, including the integer class, forces
both sides to vanish. Hence chi=0 and the density dimension is2414.

## Density frequencies and the endpoint31

The Laplacian preserves angular frequency2m. Differentiating in y
produces only sine frequencies2m-1 and2m+1. The new range16<=m<=23
therefore gives containment in31,...,47. For j=1,m=16,N=0, the radial
envelope at the origin is

 S^(p_1-16)[625/(625+r^2)]^4
       =1+(p_1-16-4/625)r^2+O(r^4).

Since Delta H_16=0, Delta(r^2H_16)=4*33 H_16 and
-partial_y H_16=32 Im(x+iy)^31, the leading density coefficient at
mode31 is4*33*32*(p_1-16-4/625), a nonzero exact rational. This
establishes an actual endpoint of the function-space support.

## Probe-span proof

For r>0 divide a proposed relation by the positive factor
r(1+r^2)^(-2), and take a full-circle sine-n coefficient at the proposed
probe's n>=19. Every objective row vanishes because its mode is<=17.
The proposed probe gives a nonzero multiple of t^K for0<t<1, a
contradiction. This proves every stated separation. The argument also
applies to the earlier recorded stages, whose objective rows form a
subset of the same67 rows.

Each probe is smooth at the origin: r^(2K+1)sin(n theta) equals the
harmonic polynomial Im(x+iy)^n times the nonnegative integer power
(r^2)^(K-(n-1)/2). Multiplication by the smooth positive denominator
preserves smoothness. A continuous function vanishing a.e. vanishes
everywhere; a nonzero continuous function pairs nontrivially with a
smooth test supported where its sign is constant. Thus pointwise,
a.e. and distributional equality give the same span conclusion.

## Verification and scope

The checker must compare all actual2414 shapes, including order,
with phase1, parent016 plus the240 declared shapes, and the accepted
abstract list. It rehashes the complete N4-306 dependency graph and
its independent T4-369 source records. It also checks the rational
mode31 witness, c and every original013 quotient shape.

The saved JSON metadata, two completed logs and copied launch command
bind12 steps then28 more, angular180, MID16, uniform probe weight10^12
and the identical67 rows. Counts mean logged iterations, including
rejected trial steps; they do not mean40 accepted updates. The
manifest's generic d2 parent is broad lineage, not immediate input.
Its description is truncated; the copied exact JSON and complete
logs supply the missing phase information. The public25-pair register
predates the08:32Z launch. The08:33Z note and09:13:13Z held-out
record postdate launch and are not called preregistration.

Current publisher source bytes may differ from historical bytes due
to subsequent025 weighting changes. Source is inspected as text,
never executed here. The unchanged row parser and explicit passage
to Problem3 are checked, but no claim of exact historical source
identity is substituted for the completed logs and immutable metadata.
The whole-plane weak-correction hypotheses, including canonical
velocity and distributional stationary equations, remain those of
joint_scaled_factored_weak/PROOF.md. No whole-plane norm, exclusion,
optimizer minimum, inverse or existence conclusion is proved here.
