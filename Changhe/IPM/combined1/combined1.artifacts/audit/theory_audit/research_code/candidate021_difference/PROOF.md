# Reference compatibility and the exact021-minus020 density norm

## 1. General theorem and exact hypotheses

Fix c=4076476460239181/2251799813685248 and delta=1-1/c, so
2/5<delta<1/2. Let chi and chi' be finite real rational combinations
of the potential generators

 (1+r^2)^(2-ell delta/2) t^m tau_R^w(1-tau_R)^a
 P_N(2tau_R-1)cos(2m theta),
 t=r^2/(1+r^2), tau_R=r^2/(R^2+r^2), ell=j+1.

Here j,m,w,a,N are nonnegative integers, R is one of1,10,25,50,100,
and P_N is the Legendre polynomial normalized by P_N(1)=1. For each
ell in1,2,3,4 and each m, assume the sum of coefficients of the
terms with a=0 is identical in chi and chi'. Call this condition(P).
Define rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy), and the
primed versions by the same derivatives. Then g=rho'-rho and V=u'-u
are smooth and real, g is S1, g belongs to H^k(R2) for each integer
k>=0, X.grad g and V belong to L2, and V equals the canonical L2
velocity U[g] with Fourier symbol(xi1xi2,-xi1^2)/|xi|^2.

For the class C of all real S1 L2 functions, interpreted locally as
distributions, the stationary sets translate by

 S(rho')=S(rho)-g.

In particular the two sets are simultaneously empty. Their L2
distances d(rho)=inf{||h||2:h in S(rho)} obey both extended-real
inequalities d(rho)-||g||2<=d(rho')<=d(rho)+||g||2. We never take
an absolute difference of two infinite distances. If d(rho)>d0 and
||g||2<=tau<=d0-b, where d0>=b>=0, then d(rho')>b. For a stronger
correction class this weak-class exclusion is enough when every
candidate correction lies in C and obeys the same equation. Translation
of the stronger class itself requires a separate stability hypothesis.

## 2. Proof of smoothness, decay and the canonical identity

The factor t^m cos(2m theta) equals Re(x+iy)^(2m)/(1+r^2)^m.
All denominators are strictly positive on the plane, so each term is
smooth, with the claimed parity after differentiation. At infinity
expand in z=r^-2. Every term is r^(4-ell delta)cos(2m theta) times
a convergent analytic series in z; its constant coefficient is1 for
a=0 and0 otherwise. Condition(P) therefore cancels the leading
term for each of the first four branches, with all derivatives.
Remaining exponents are at most max(4-5delta,2-delta)=4-5delta.
The expansion is convergent beyond the largest fixed scale, so every
Cartesian derivative of orderk of the potential difference is
O(r^(4-5delta-k)), uniformly in angle. Three derivatives give

 partial^alpha g, partial^alpha V=O(r^(1-5delta-|alpha|)).

Since1-5delta<-1, their radial square integrals converge in two
dimensions; local smoothness handles every compact set. Multiplication
of grad g by X restores the same decay. This proves all Sobolev and
drift assertions. No uniform constant over all coefficient lists is
claimed. Failure of(P) is not a converse obstruction to L2 membership.

Smooth derivatives commute, giving Delta V1=partial_xy g,
Delta V2=-partial_xx g and div V=0. The bounded L2 multiplier U[g]
has the same Poisson equations and ||U[g]||2<=||g||2. Hence
V-U[g] is L2 and harmonic. Its Fourier transform is supported at the
single point0 and is L2; it must vanish. This proves the canonical
identity and excludes an unrecorded harmonic velocity correction.

For h in C define

 F_rho(h)=div((cX+u)(rho+h))+div(U[h](rho+h))-(2c+1)(rho+h).

Every product is locally integrable: smooth backgrounds and X are
bounded on compact sets, and hU[h] is locally L1 by Cauchy-Schwarz.
The formula is the intended stationary transport equation since the
velocity has divergence2c. Linearity and V=U[g] give
F_rho'(h)=F_rho(g+h). This proves the set translation. Triangle
inequality followed by infimum gives both distance inequalities when
the sets are nonempty; the empty case is immediate in the extended
reals. The strict screening implication follows directly, without
assuming an infimum is attained.

## 3. Complete norm computation for an actual pair

For this actual audit use the immutable021 and020 raw JSON copied in
data/, with hashes bound in verification/PREPARE.json. Subtract every
coefficient at the complete(j,m,spec) key exactly and check(P) before
applying the theorem. Only R=1,25,50 occur for this pair. Reconstruct
the difference density and stream by the independently audited polar
Euler derivatives of ../candidate021_weak/PROOF.md, not by the peer's
Cartesian constructor. The exact representation is

 g=r sum_(ell,n) v^(ell delta/2) A_(ell,n)(t)sin(n theta), v=1-t.

The rational denominators are powers of1+624v and1+2499v. Origin
factors are divided exactly only after their required zeros have been
checked. The low-branch density and stream coefficients at t=1 are
also checked to vanish. The stream then has the same absence of
leading velocity terms. Three physical points compare g,V with the
separately generated Cartesian reference values; these checks bind
implementations but do not replace the exact differentiation formulas.

Sine orthogonality and r dr=dt/(2v^2) give

 ||g||2^2=(pi/2) sum_L integral_0^1
             t v^(L delta/2-3) Q_L(t)dt,
 Q_L=sum_(ell+ell'=L,n) A_(ell,n) A_(ell',n).

All ordered pairs with the same angular frequency occur. Each group
may have either sign. Form Q_L exactly, write Q_L=P_L/D_L and set N(v)=(1-v)P_L(1-v), and strip its exact zero orderk at v=0. Check
b=L delta/2-3+k>-1 for every nonzero group. This is essential:
checking b before exact cancellation would reject legitimate groups.
The other endpoint and every rational denominator are nonsingular.
Thus termwise integration of this finite sum is justified.

Write the reduced rational function N/D as a polynomial plus proper
partial fractions. For each coprime factor D_i=(1+a_i v)^k_i, use
exact extended Euclidean inversion of D/D_i modulo D_i to find the
principal numerator. Replay the entire numerator identity after
recombination. Integrate the polynomial by1/(b+j+1) and each pole
by the outward Arb value

 integral_0^1 v^b/(1+a v)^k dv
     =2F1(k,b+1;b+2;-a)/(b+1), b>-1,a>0.

Euler's convergent integral proves this identity; the exact parameter
differences justify the integer-relation flags. This uses direct
hypergeometric values independently of the peer's recurrence in k.
Every nonzero moment must retain more than150 accuracy bits; the
complete sum must be strictly positive before square root. Compare
all group values and the norm to the peer only after reconstruction.
A certified rational upper tau and all strict margin comparisons are
then evaluated outward, using the separately accepted parent020 weak
distance floor. No sampled quadrature or finite radial cutoff enters.

## 4. Dependencies, verdict and limits

The general theorem above independently CONFIRMS the compatibility
lemma of N4-313. The actual021 result is accepted only on a successful
complete check, recorded separately with real time and source hashes.
The mathematical hypotheses of the parent weak-distance theorem and
the canonical fixed-c equation are retained. A failed sufficient
screen proves neither existence nor nonexistence of a nearby solution.
It gives no inverse, conditioning or norm of the residual. More
restrictive spaces, variable c, and density cancellation under weaker
prefix assumptions are outside this theorem.
