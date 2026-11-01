# Other compatible Candidate-shaped profiles

Status: roots1,2,4,5,6,7 are PROVED by the reviewed theorem145 and certificate construction158. Root3 is proved separately in158. All seven branches are proved.

## Exact statement to be checked

Let the normalized leading profile and the degree-nine obstruction
polynomial be exactly those of156. Number the seven real roots
in increasing order. Topic158 treats root3. This topic tests
roots2,4,1,5,6,7, in that order, at delta=4/9 and c=9/5.
Only the coefficient of sin(3 theta) changes. Every other normalized
Candidate007 coefficient remains its exact value.

For a specified root b, suppose the retained certificate establishes
|sigma_k(b)|>s for every integer k>=1, where s is its recorded positive
rational number. Then theorem145 gives a unique tuned pure density and
stream expansion with this leading profile. Its common potential is
reconstructed by the same theorem, including its finite exceptional
logarithm. If the exact rational majorant test below also passes, the
series and all appropriately weighted derivatives converge absolutely
and uniformly on the stated exterior domains.

## Proof of the certificate implication

Use the signed Cartesian recurrence and its linear response as derived
in145,149 and158. The response from the free stream harmonic at order9k
to the next obstruction depends only on the fixed density prefix1..9
and stream prefix1..8. Compute these prefixes from the exact leading
profile. At the first resonance the obstruction is zero by the
definition of b. The interval implementation encloses the exact
algebraic root using rational bisection and propagates outward-rounded
balls through the polynomial recurrence.

Compute sigma_k separately for1<=k<=52. Check nonvanishing and retain
its exact dyadic enclosure. For k>=46 the positive carrier frequency
q=4k-2 is at least182>BQ=180. The compact recurrence149 is therefore
valid with t=1/q. Its full and compact implementations are compared at
46<=k<=52, and its sparse and dense implementations at three rational
t values including zero.

Cover [0,1/182] by the retained finite binary tree. At every leaf,
either interval arithmetic gives |sigma(t)|>s on the whole leaf or
exact rational inequalities show that the leaf contains no point
1/(4k-2) with integer k>=46. Reconstruct the dyadic endpoints from
their binary addresses and verify adjacency and every lower bound
independently using exact fractions. This proves the tail estimate,
including arbitrarily large k. The finite enclosures prove the
remaining estimates.

Bound the leading Fourier norm strictly above by a rational number a
using the rational root endpoints and the exact fixed coefficients.
Use h=2,Q=9,B=20,L=9/2 and kappa=1150/9 in145. Write
Phi(0,Y)=c0+JY, where J is strictly lower triangular and nonnegative,
T=(I-J)^-1, Y0=T c0 and

    G(z,Y)=Y0+T(Phi(z,Y)-Phi(0,Y)).

The program retains the exact fractions c0,J,Y0,2Y0 and
G(2^-q,2Y0). If every image component is strictly smaller than the
corresponding box component, the nonnegative majorant converges at
z=2^-q. Thus every radius

    R > 2^(9q/4) |epsilon|^(9/4)

suffices for leading profile epsilon*f1. The strict radius absorbs
every fixed polynomial derivative factor. The adjacent failed box
test establishes only failure of this particular box, not an optimal
convergence radius.

For epsilon equal to the original positive Candidate007 coefficient
a1, the exact inequality a1^9<2^38 from158 gives the sufficient bound
R>2^((9q+38)/4). The recorded integer power of two is chosen strictly
larger than this number.

## Scope and failure reporting

The argument proves a local exterior stationary solution generated
by a common potential. It does not prove convergence at the original
stored Candidate007 exponent, a smooth whole-plane stationary
extension, or an optimal radius. A finite unresolved response or a
failed interval cover is reported as an open certificate attempt;
neither establishes divergence. Each root is checked independently.

Dependencies:02,145,149,156,158. Verification evidence and exact source
snapshots are stored alongside this proof.

## Completed root2 certificate

At b=0.042005686153258142714011962278366589..., all responses satisfy |sigma_k|>2^-21. The exact tail tree has108 accepted leaves,19 empty leaves and126 splits. All52 finite checks, seven compact comparisons, three dense/sparse comparisons, and the exact tree replay pass. The old majorant gives q=244, normalized radius2^549 and restored-amplitude sufficient radius2^559. Every strict larger closed exterior has the convergence properties stated above. The finite and tail computation took822.9564047767781 seconds. The sharper initial-coefficient certificate in168 is separately subject to its analytic review.

## Completed root4 certificate (2026-10-31T12:49:22+00:00)

The fourth ordered real root of the exact compatibility polynomial in156 has uniform response lower bound2^-23. The finite checks through52 and compact tail cover starting46 all pass, with108 accepted leaves and19 empty leaves. The exact replay verifies the full cover. The limiting response is positive, enclosed around1.38692306842117379519450813519e-6. The already reviewed158 argument therefore proves convergence for this additional root. The original145 box gives q251, normalized sufficient radius2^(2259/4), restored sufficient radius2^575. The root run took694.8394661648199 seconds. The remaining roots retain their pending status until their own certificates pass.

## Root1 completion at 2026-10-31T13:05:12+00:00

The smallest real root b=-0.15263500056179827656... also satisfies every response hypothesis. The uniform lower bound1/16384 follows from52 finite interval checks and a complete compact tail cover beginning at46. Exact rational replay confirms260 accepted,146 empty and405 split cells. The limiting response is+.00143813290655637254.... The same proof above therefore applies with a=601/500 and s=1/16384. The original majorant gives q232, normalized sufficient radius2^522 and restored-amplitude sufficient radius2^532. This branch is PROVED by V333.

## Root5 completion at 2026-10-31T13:19:15+00:00

The fifth real root is b=0.293187687845006959464311289885522594.... All52 finite responses and the compact infinite tail satisfy |sigma_k|>2^-21. The retained tree has317 accepted leaves,279 empty leaves and595 splits; exact rational replay passes. The limiting response is positive, around6.64045874452995963966e-5. The original majorant with a=1343/1000 passes at q249, giving normalized sufficient radius2^(2241/4) and restored-amplitude sufficient radius2^570. Actual root computation903.5937683857046seconds. This fifth admitted Candidate-shaped branch is PROVED by V339.

## Root6 completion at 2026-10-31T13:41:52+00:00

Root6, b=[0.46749215425279362216756691599237685133429773452353608778774121799 +/- 4.76e-66], satisfies |sigma_k|>1/8192 for every integer k>=1. All52finite checks, seven full/compact comparisons and three sparse/dense comparisons pass. The exact compact cover has818accepted leaves,720empty leaves and1537splits. An independent address-based rational replay confirms every endpoint, integer exclusion and retained lower bound. The limiting response is[-0.0015637488427909991565594871655472448596619770698721588220135008214 +/- 4.05e-68]. The original145majorant with a=1517/1000 passes at q=237, giving normalized R>2^(2133/4)|epsilon|^(9/4) and restored original-amplitude R>2^543. Actual root computation1334.5814285790548seconds. PROVED by V349.

## Root7 completion at 2026-10-31T13:54:27+00:00

Root7, b=[2.3744614453077789911040451573798899463092036197452182976683696007 +/- 3.25e-65], satisfies |sigma_k|>1 for every integer k>=1. All52finite checks, seven full/compact comparisons and three sparse/dense comparisons pass. The exact compact cover has260accepted leaves,146empty leaves and405splits. An independent address-based rational replay confirms every endpoint, integer exclusion and retained lower bound. The limiting response is[61454.218201912264486592578180886153471909657102942468517926275871 +/- 3.07e-61]. The original145majorant with a=428/125 passes at q=233, giving normalized R>2^(2097/4)|epsilon|^(9/4) and restored original-amplitude R>2^534. Actual root computation810.304421194829seconds. PROVED by V361.
