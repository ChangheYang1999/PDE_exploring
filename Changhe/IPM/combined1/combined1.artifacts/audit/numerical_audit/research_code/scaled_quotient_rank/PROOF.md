# Independence of the radius25 extension of the exact quotient basis

## Exact statement

Fix c=4076476460239181/2251799813685248, gamma=1/c,
delta=1-gamma and p_j=(3+gamma-j delta)/2. Put
S=1+r^2,t=r^2/S,v=1/S,H_m=Re(x+iy)^(2m).
Let V_old be the1922-dimensional real potential space with basis in
../optimizer_quotient_audit/source/N1_013_quot_exact.json. Its exact
independence and original2982-generator span were proved in that topic.
In particular its elements are finite sums H_m S^(p_j-m)P_jm(t), where
P_jm is a polynomial and the actual j belong to{0,...,7}.

For R=25, j in{1,2,3},m in{9,...,15},N in{0,...,11}, adjoin

 G_jmN=H_m S^(p_j-m) [R^2/(R^2+r^2)]^4
                              P_N(2r^2/(R^2+r^2)-1),

where P_N is the Legendre polynomial with P_N(1)=1. These252 potentials
are independent modulo V_old. Thus their union with the old basis has
real dimension2174. This is a statement about potential functions. No
rank of their densities, coercivity, condition number, objective minimum,
stationarity or inverse is asserted. The checker compares actual shapes
in immutable016 with this exact list, disregarding current coefficients.

## Proof of independence

After angular separation write H_m S^(p_j-m)=S^p_j t^m cos(2m theta).
Set a=R^2-1=624 and L=1+a v. The new radial numerator is

 A_mN(v)=R^8 t^m v^4 P_N(2t/L-1)/L^4.

Its rational continuation has a pole at v0=-1/a. The Legendre leading
coefficient is2^(-N) binom(2N,N), from Rodrigues' formula. At that pole,
t0=1-v0=R^2/a is nonzero, and the coefficient of(v-v0)^(-4-N) is

 C_mN=R^8 v0^4 binom(2N,N)t0^(m+N)/a^(4+N),

which is nonzero. All remaining terms have smaller pole order. For a
fixed(j,m), take the largestN whose coefficient in a proposed linear
relation is nonzero. Its pole order4+N cannot be canceled by the other
new terms or the polynomial old terms. This is impossible. Hence all
new coefficients in that block vanish, and old block independence
finishes that block.

To justify block separation, angular orthogonality first separatesm.
For each fixedm a potential relation is sum_j v^(-p_j)Q_j(v)=0,
where every rationalQ_j is analytic atv=0. IfQ_j is nonzero, its Taylor
series has a finite least integer exponentk_j and nonzero coefficient.
The exponent classes of-p_j are distinct modulo integers: their
differences are(j-j')delta/2, verified to be nonintegers for the actual
j=0,...,7. Thus among the finitely many nonzeroQ_j there is a unique
least real exponentk_j-p_j. Divide byv to that exponent and letv tend
to0 from above. The unique nonzero leading coefficient cannot vanish.
This contradiction separatesj, and the preceding pole argument applies.
Counting3*7*12 new independent classes gives2174 total. The use of a
negative auxiliary pole is an exact rational identity argument, not an
analytic continuation of the noninteger prefactor to a physical radius.

## Density frequencies and an explicit lowest-mode witness

The polar Laplacian preserves thecos(2m theta) frequency, and
-partial_y maps it into sine frequencies2m-1 and2m+1. Thus these
new generators have density frequencies contained in{17,19,...,31}.
The lower endpoint17 actually occurs in the family. Forj=1,m=9,N=0,
expand the radial envelope at the origin as

 S^(p_1-9)[R^2/(R^2+r^2)]^4
     =1+(p_1-9-4/R^2)r^2+O(r^4).

The leading harmonicH_9 has zero Laplacian. Using
Delta(r^2 H_m)=4(2m+1)H_m and
-partial_y H_m=2m Im(x+iy)^(2m-1), the leading density term is

 4*19*18*(p_1-9-4/625) Im(x+iy)^17,

with a nonzero exact coefficient. The checker also derives this term
from the accepted Cartesian rational-field code. Therefore describing
the full density support of the new basis as only modes19 to31 omits
mode17. This correction does not affect the separate exact Fourier proof
that probes n>=19 lie outside the declared weak objective withn<=17.

## Verification and scope

Compare all1922 initial generator shapes against the confirmed old basis,
then compare the remaining252 exact tuples with the stated Cartesian
product. Verify the old rank artifact and raw SHA256 bindings. Independently
build each Legendre polynomial by its three-term recurrence, substitute
its rational argument, and evaluate the highest numerator atv0 exactly.
Require the displayed Laurent coefficient for every(m,N), repeat the
branch-class checks and verify the single explicit density witness.
Store finite rational witnesses in exact JSON; no generated Lean file.
This proof precedes computation. The new rank theorem remains OPEN for
independent theoretical review until a separate lane accepts it.
