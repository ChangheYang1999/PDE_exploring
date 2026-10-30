# Three remaining candidate016 weak tests

## Statement, data and hypotheses

Fix c=4076476460239181/2251799813685248 and the exact reference density R
and canonical velocity U[R] of C1-N1-016-legqs25-quot013, coefficient hash
a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42.
Write S=1+r^2, t=r^2/S, v=1/S, delta=1-1/c and
F=(cX+U[R]).grad R-R. The exact reference class and its derivative
formulas are those of ../joint_scaled_factored_weak/PROOF.md.

Suppose R+h solves the stationary equation at this same c, h is an
S1-symmetric real L2(R2) function, and its canonical velocity increment
w=U[h] is divergence-free with ||w||2<=||h||2. Require locally integrable
representatives of every product in the weak equation and the cutoff
limits justified in ../scaled_weak_backend/PROOF.md. No alternative
velocity gauge or change of c is included.

The three probes are phi=r v^2 P(t) sin(n theta): (i) the exact n=1
polynomial T4_a0.json, hash
b5b510bbabe556d2e07008473d9d92eb7098bac38cc36955cac0799bd0de425e;
(ii) the exact n=7 polynomial T4_n7_a0.json, hash
2a268c62e9e45096d2b745679a49adeee0cb9a3da532a06e4b89faaffdb3ef1f;
(iii) n=1, P=t^2048. Large coefficients stay in these exact JSON files.
Each P is divisible by t^((n-1)/2), which makes phi smooth at the
origin. Every phi and its derivative decay sufficiently at infinity.

The computational claim is that independent exact field construction
and whole-plane integration produce I=integral F phi,
M=||(2c+1)phi+(cX+U[R]).grad phi||2, C=||phi grad R||2 and a proved
Hcap>=||grad phi||infinity agreeing with the three designated rows of
source/N3_probe.json. Any containing-interval claim is accepted only
when its exact checker passes. A positive strict rational floor below

 d=2|I|/(M+C+sqrt((M+C)^2+4 Hcap |I|))                 (1)

is then a necessary lower bound for ||h||2, under the stated hypotheses.

## Weak inequality

Subtract the reference equation, pair with phi, and integrate transport
terms by parts. Since div(cX+U[R])=2c, the terms linear in h have bound
M||h||2. Cauchy-Schwarz bounds w.grad R by C||w||2 and the integrated
quadratic term by ||grad phi||infinity ||h||2 ||w||2. Thus
|I|<=(M+C)||h||2+Hcap||h||2^2. Its right side is increasing on the
nonnegative half-line; solving this quadratic gives (1). This is a
distance from the reference density to a putative exact density.

## Exact field construction and integration

For a general polynomial P, the radial derivative numerator is
B=(1-4t)P+2t(1-t)P'. The Cartesian derivative amplitudes have
frequencies n-1 and n+1, with factors (B+nP)/2 and (B-nP)/2 and the
usual sine/cosine signs. Multiplying these by every exact background
mode produces Mfield and both components of Cfield. No output angular
mode is discarded. Each field has the form
r v^2 sum v^(ell delta/2) A_(ell,kind,k)(t) trig_k(theta), where A is a
rational function with positive denominators 1+a v,
a in {99,624,2499,9999}. Only624 is active for this reference.

Angular orthogonality and r dr=-dv/(2v^2) give, for every matching
angular branch pair, pi/2 times
 integral_0^1 v^(1+(ell+ell')delta/2)(1-v) A(1-v)B(1-v) dv.
The coefficient is2 for distinct unordered branches and1 for a diagonal.
Adding every pair in every vector component yields M^2 and C^2.
An independent integration-by-parts pairing is -integral R Mfield;
its v exponent is (ell+ell')delta/2-1. A separate direct construction of
the sine-n coefficient of F gives I without that identity. All exponents
must be greater than-1, and exact partial fractions with positive poles
and outward ball moments integrate every group on the whole interval.
The two pairings must overlap, with at least150 relative accuracy bits.
The scalar moment proof is ../rational_pole_moments/PROOF.md.

For P=t^2048, keep its large power factored outside the finite field
construction. The earlier independently calibrated factored algorithm
uses localization powers2049 for I and4097 for M^2,C^2; this avoids
expanding a high-degree polynomial without changing the integrals.
Its proof is ../joint_scaled_factored_weak/PROOF.md. The general formula
above and the factored formula agree algebraically upon substitution.

## Global gradient bound

At a fixed radius the gradient square is
v^4(B^2 sin^2(n theta)+n^2 P^2 cos^2(n theta)). Hence the greater of
|v^2 B| and |n v^2 P| bounds the Euclidean gradient. For the two frozen
vectors, exact Bernstein conversion and repeated dyadic subdivision
prove both polynomial absolute values below the frozen rational cap.
Convexity of the Bernstein basis bounds every point of each closed
subinterval by the extreme control coefficients. Adjacent accepted
leaves must tile[0,1] exactly. The algorithms and their elementary
fixtures were independently checked in ../angular_probe_audit/PROOF.md
and ../optimized_probe_audit/PROOF.md; this calculation rechecks them.
For P=t^K, K=2048, n=1, |(2K+1)-(2K+4)t|<=2K+1, so the coarse exact
cap is 4(2K+1)K^K/(K+2)^(K+2), by maximizing (1-t)^2 t^K.
The derivative changes sign at K/(K+2), and both endpoint values vanish.

## Calibration, source binding and scope

Before actual016 work, compare the three exact generic field maps for
each frozen vector on007 against the independently accepted polynomial
construction, coefficient by coefficient. On016 compare their physical
values against the independently differentiated Cartesian jet at three
points. These are algebraic and local diagnostics, not substitutes for
the complete moment integration. Bind the current checker, full own
module dependency graph, exact JSON, frozen N3 record and every inherited
calibration source before execution and require their hashes unchanged
afterward. Save each completed row immutably for restart.

For the three I/M/C values require the wider N3 displays to contain the
own100-digit intervals; compare the positive roots as containing balls.
The reported H_upper is an outward endpoint, not necessarily a ball
containing the exact coarse formula. Verify its direction explicitly
or its agreement for the frozen rational cap. Do not claim to reproduce
N3's internal1024-bit endpoint digits from its30-digit norm displays.
These tests add no maximum over probes, full residual upper norm,
existence theorem or new campaign exclusion. The six requested N3 rows
are collectively covered only after these three checks and N4-353 pass.
