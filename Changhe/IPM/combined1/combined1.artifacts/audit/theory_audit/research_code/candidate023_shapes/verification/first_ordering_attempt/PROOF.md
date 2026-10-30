# Independent audit of the candidate023 dimension and recorded probe history

## Exact statement

Fix c = 4076476460239181/2251799813685248, gamma = 1/c,
delta = 1-gamma and p_j = (3+gamma-j delta)/2. Let r^2=x^2+y^2,
S=1+r^2, t=r^2/S, v=1/S and H_m=Re((x+i y)^(2m)). Let V_old be
the 1922-dimensional potential space with the selected original basis
in data/old_basis.json, already proved independent in T4-195 and
T4-230. Its elements are sums H_m S^(p_j-m) P_jm(t), where each P_jm
is polynomial and j is in {0,...,7}.

For each R in {25,100}, j in {1,2,3}, m in {9,...,15}, and
N in {0,...,11}, adjoin

    G_RjmN = H_m S^(p_j-m) [R^2/(R^2+r^2)]^4
                       P_N(2r^2/(R^2+r^2)-1),

where P_N is the Legendre polynomial normalized by P_N(1)=1.
The 2426 resulting potentials are linearly independent over the reals.
The map chi -> -partial_y Delta chi is injective on their span V.
Consequently both V and its density image have dimension 2426.
This is a theorem about the stated abstract function list, not a claim
about an unregistered candidate's shape list or coefficient rank.

## Potential independence

Separate each cos(2m theta) by angular orthogonality. The radial
relation then has the form sum_j v^(-p_j) Q_j(v)=0, where Q_j is
rational and analytic at zero. All p_j and all nonzero differences
p_j-p_k are nonintegers, as the exact check verifies. A nonzero Q_j
has some finite integer vanishing order n_j at zero. The exponents
n_j-p_j are distinct. Dividing by the smallest power and taking
v down to zero leaves one nonzero coefficient, a contradiction.
Thus each Q_j vanishes separately. The same argument separates these
branches from one additional integer Laurent-polynomial class.

For fixed (j,m) the new rational factor is

    A_RmN(v) = R^8 v^4 (1-v)^m
               P_N(2(1-v)/(1+a_R v)-1)/(1+a_R v)^4,
    a_R = R^2-1.

At v_R=-1/a_R, the factor has pole order 4+N. Its leading Laurent
coefficient is

    C_RmN = R^8 v_R^4 binom(2N,N)
                       (1-v_R)^(m+N)/a_R^(4+N) != 0.

Indeed only the leading term 2^(-N) binom(2N,N) x^N of P_N can
contribute to this order. Every old radial polynomial is analytic
there. The other scale is also analytic, since
1-a_(R')/a_R is nonzero for a_R=624 and a_(R')=9999, or conversely.
Therefore the largest N with a nonzero coefficient at either scale
would have an uncancellable pole. Descending in N removes every new
coefficient at both scales. The old independent basis removes the
remaining coefficients. There are 504 new generators, proving 2426.
The pole argument is applied only after branch separation to rational
functions; it does not analytically continue a noninteger power
through a negative pole.

## Density injectivity

Every element chi of V is smooth and separately even in x and y.
Differentiation of its explicit finite generators gives
|D^k chi|=O(r^(3+gamma-k)) for 0<=k<=4 as r tends to infinity.
The scaled rational factors improve these bounds. In particular every
fourth derivative tends to zero, since gamma<1.

Suppose partial_y Delta chi=0. Then Delta chi=f(x). For fixed x,
f''(x)=partial_xx Delta chi(x,y) tends to zero as |y| tends to infinity.
It is independent of y, so it is zero. Evenness forces f=K constant.
The function chi-Kr^2/4 is entire harmonic and grows at most like
r^(3+gamma), with 3+gamma<4. Its fourth derivatives vanish by the
interior harmonic derivative bound on disks of radius L, followed by
L tending to infinity. It is a polynomial of degree at most three.
Separate evenness leaves only a constant and even quadratics, and
harmonicity leaves the form A+B(x^2-y^2). Thus

    chi=A+B(x^2-y^2)+Kr^2/4.

Its angular coefficients are integer Laurent polynomials in v.
The branch separation already proved, including the integer class,
forces these coefficients and every branch to vanish. Hence chi=0,
and potential independence forces the entire coefficient vector to
vanish. This proves density injectivity.

## Actual candidate and analytic probes

The exact raw candidate is C1-N1-023-legqs25p100-quot013, SHA256
d67bdd9ff05917736e686af5f834a2e12afede891098ccf8f9de8a6e2d7a71df. Its ordered shapes must equal the1922 old shapes followed by252 radius25 and252 radius100 shapes above. Its first saved phase has SHA256637ae589e19d01a4bb355c2935cae1883c718b0d1e467d5151e8ce2482635ceb and starts from016, SHA256a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42. The radius100 block is added only in that phase. Both recorded phases use67 distinct analytic objective rows. These are27 first-mode exponents

    0,1,2,3,4,5,6,7,8,12,16,24,32,48,64,96,128,192,256,384,512,
    768,1024,1536,2048,3072,4096,

and40 pairs(n,(n-1)/2+s), n=3,5,...,17, s=0,8,32,128,512.
For odd n and K>=(n-1)/2 define phi_(n,K)=r(1+r^2)^(-2)t^K sin(n theta). The25 public pairs n=19,23,25,29,31 and K=600,900,1200,1800,2400, and35 diagnostic pairs n=19,21,...,31 and K=(n-1)/2+s, s=0,8,32,128,512, lie outside this real analytic span.

Indeed divide a proposed dependence by r(1+r^2)^(-2)>0 and take its full-circle sine-n coefficient. The objective contributes zero for n>=19 while the proposed probe contributes t^K>0. Each probe is smooth at zero: r^(2K+1)sin(n theta)=Im(x+iy)^n(r^2)^(K-(n-1)/2), with nonnegative integer exponent. A continuous zero distribution vanishes pointwise, so the argument applies to pointwise, almost-everywhere and distributional equality.

## Verification and limits

The checker rebinds the accepted old-basis evidence, compares every actual shape, checks all branch conditions, and independently constructs the Legendre polynomial using its three-term recurrence. Homogenizing that polynomial with L_R and evaluating its numerator at v_R reproduces every one of the168 nonzero Laurent coefficients in the displayed formula. Both cross-pole values are checked. These checks concern exact rational identities, not matrix conditioning.

The source text and saved metadata must agree on angular order180, middle order16, weights26214400,3000000 and10^12, penalty mode, and12 then28 logged iterations. A logged iteration need not be an accepted update. The parser and objective row propagation are inspected as text only. No publisher code is executed. This audit replays only the parent016 and the two023 stages; it makes no independent claim about earlier007-through013 history, actual historical source bytes, statistical independence, or blindness. The public register predates the recorded08:46Z launch; the later08:47 announcement and09:13 record do not constitute preregistration. No residual bound, inverse or existence statement follows from rank or probe separation alone.
