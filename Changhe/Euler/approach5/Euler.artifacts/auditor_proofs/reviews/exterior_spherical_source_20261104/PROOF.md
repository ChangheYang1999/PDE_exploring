# Ordered source signs and exterior rigidity

Status: independent reconstruction, confirmed in A3072 with the qualified A120 comparison in A3073. No sign is inferred from decay; the unrestricted problem remains open in A3074.

## 1. Exact statements and notation

Let U be C1 and divergence-free on R3. Set q=tr((DU)^2), where the square is matrix multiplication, E(R)=integral_(B_R)|U|^2, and Q(r)=integral_(S2)q(r theta)d sigma. Assume E(R)=o(R).

(i) If U is not zero, there exist 0<r1<r2 with Q(r1)<0<Q(r2).

(ii) If Q(r)<=0 for every r>b, where 0<=b<infinity, then U(y)=0 for |y|>b. In particular U has compact support when b>0, and is zero when b=0. This is a kinematic statement and does not itself force zero inside B_b.

(iii) Suppose additionally P is C1 and the full profile equation holds on R3,

    (1-c)U+[((cI-omega J)y+U).grad]U+omega JU+grad P=0,
    J(x1,x2,z)=(-x2,x1,0),

where c is any finite nonzero real number and omega is any finite real number. Then the premise of (ii) forces U=0 everywhere. No pressure normalization is needed.

For bounded Hb full C1/C1 profiles, the confirmed A3053 energy law supplies E=o(R) when0<c<1/2. Consequently any nonzero such profile has Q>0 at arbitrarily large radii, including at c=2/5 if such a profile exists. Neither the unrestricted critical problem nor the unrestricted target interval is settled.

## 2. Compact tests and their errors

For C1 divergence-free U,

    integral q phi=integral U.D^2 phi U

for compactly supported C2 tests phi. This follows by local C1 mollification and two integrations by parts, as in A3056. Choose a smooth radial nonincreasing chi with0<=chi<=1, equal to1 on B1 and zero outside B2, and write chi_R(y)=chi(y/R). Let K1 and K2 bound its first derivative and operator norm of its Hessian. Then

    |integral Q(r)chi(r/R)r^2 dr|<=K2 E(2R)/R^2.             (1)

For any smooth nonnegative radial psi with psi(r)<=r,0<=psi'(r)<=1 and psi''>=0, the product rule gives

    integral q psi chi_R=integral chi_R U.D^2 psi U+e_R,
    |e_R|<=(2K2+2K1)E(2R)/R.                              (2)

The Hessian of psi(|y|), away from0, is psi'' e_r tensor e_r+(psi'/r)(I-e_r tensor e_r), so it is positive semidefinite. The tests used below vanish near0. All integrals before taking limits have compact support. Formula (2) needs no global integrability of q or DU.

For f(r)=sqrt(1+r^2), the same formula holds with a fixed error constant depending only on chi, for R>=1. Its Hessian has strictly positive eigenvalues f^-3 radially and f^-1 tangentially.

## 3. Ordered signs

Suppose no pair r1<r2 has Q(r1)<0<Q(r2). If Q has no positive value, A3056 gives U=0. Otherwise let r0=sup{r>0:Q(r)>0}. For every r<r0 there is a positive value at a larger radius, so the assumed absence of the pair forces Q(r)>=0. For every r>r0, Q(r)<=0 by definition. If r0=infinity, Q>=0 everywhere and again A3056 applies.

It remains to consider0<r0<infinity. Write M_R for the integral in (1). The sign order implies pointwise

    Q(r)[f(r)-f(r0)]<=0.

Multiplication by chi(r/R)r^2 and integration therefore give

    integral chi_R U.D^2 f U
       <=f(r0)|M_R|+C E(2R)/R ->0.

For every fixed L and R>=L, the left side is at least (1+L^2)^(-3/2)E(L). Hence E(L)=0 for all L, a contradiction to nonzero U. This proves (i). Continuity at0 ensures that a negative value at0 also gives negative values at positive radii; no special radius0 case is needed.

## 4. Exterior nonpositive mean gives zero exterior velocity

Fix epsilon>0. Choose a smooth nonnegative eta supported in (b+epsilon/2,b+epsilon), with integral1, and define

    psi'(r)=integral_0^r eta(s)ds,
    psi(r)=integral_0^r psi'(s)ds.

Then psi vanishes for r<=b+epsilon/2,0<=psi'<=1,psi''=eta>=0,psi<=r, and psi'=1 for r>=b+epsilon. By the sign assumption the left side of (2) is nonpositive. The right side's main term is nonnegative, so for every fixed exterior compact set its integral tends to zero as R tends to infinity. Equivalently, Fatou's lemma and E=o(R) give

    integral U.D^2 psi U=0.

For r>b+epsilon the integrand is |U_tan|^2/r. Continuity implies U_tan=0 there. Letting epsilon decrease gives U=u(r,theta)e_r on r>b. Divergence now gives partial_r(r^2 u)=0, hence

    U(r theta)=g(theta)theta/r^2,

with g in C1(S2). This is A117's exterior conclusion. The source sign forces a further restriction that is not needed in A117's energy argument. Put e=theta and h=grad_(S2)g. Direct differentiation gives

    DU=r^-3[g I-3g e tensor e+e tensor h].

Here h.e=0. The square of e tensor h has trace0, and its cross terms with gI-3g e tensor e also have trace0. The latter symmetric matrix has eigenvalues -2g,g,g. Therefore

    q(r theta)=6g(theta)^2/r^6,
    Q(r)=6r^-6 integral_(S2)g^2>=0.                       (3)

Since Q<=0 in the same exterior, g=0. This proves (ii). No angular regularity beyond C1 was used. The flux identity integral g=0 also follows from global divergence, but is not needed to conclude g=0.

## 5. Compact-support exclusion from C1 circulation

We give the full implication used in (iii). For a compactly supported C1 U the carrier B=(cI-omega J)y+U has at most linear growth, hence a complete C1 flow Phi_t for all real t. Since div B=3c,

    det D Phi_t=exp(3ct).                                  (4)

Let alpha=U.dy and G=|U|^2/2-P. Direct substitution of the full equation and (DB)^T U gives

    L_B alpha=(2c-1)alpha+dG.

Integrating along the flow and then taking the exterior derivative in distributions yields

    Phi_t^* d alpha=exp((2c-1)t)d alpha.                   (5)

For completeness, the integrated one-form identity has a C1 scalar primitive. Locally smooth approximations to Phi_t converge in C1; their pulled-back one-forms and pulled-back continuous two-forms converge uniformly on compact sets. Thus exterior differentiation commutes with pullback after passage to distributions. Both sides of (5) are continuous, so (5) holds everywhere. This is the C1 transport proof also verified in A3047 and A3059.

The open set O={y:d alpha(y)!=0} is invariant under every Phi_t, since the derivative of Phi_t is invertible and the scalar factor in (5) is nonzero. Compact support of U makes O bounded. The change-of-variables formula and (4) give

    |O|=|Phi_t(O)|=exp(3ct)|O|.

For c!=0 choose any nonzero t. Finiteness of |O| forces |O|=0, and openness forces O empty. Hence curl U=0 everywhere. Along with div U=0, this gives Delta U=0 in distributions. Each component is harmonic and compactly supported, so U=0. This proves (iii) without a pressure estimate or any special sign of c.

The same argument excludes a finite-volume nonzero-vorticity set whenever the C1 carrier flow is complete and c!=0. To conclude constant U from zero curl, one may use global uniform sublinearity instead of compact support. This last generalization is recorded only with those explicit hypotheses.

## 6. Actual pressure interpretation and limitations

For a full C1/C1 profile, -Delta P=q in distributions. Let pbar(r)=(4pi)^-1 integral_(S2)P(r theta)d sigma. Local mollification and the divergence theorem give

    4pi r^2 pbar'(r)=-integral_0^r s^2 Q(s)ds,
    (r^2 pbar')'=-r^2 Q/(4pi), r>0.                       (6)

Although only C1 P is assumed, the first identity shows r^2 pbar' is continuously differentiable on (0,infinity). The constant at0 is zero since grad P is locally bounded. Thus the ordered signs in(i) correspond to a region where r^2 pbar' increases and a later region where it decreases. Exterior Q<=0 would make this weighted pressure derivative nondecreasing there and forces zero for the full profiles in(iii).

There is no conclusion that Q<0 occurs at arbitrarily large radii. Compactly supported kinematic divergence-free fields are consistent with(ii), since their Q is zero outside. The full Euler equation is indispensable in Section5. No finite support or sign is inferred for an arbitrary target profile, and no c=1/2 energy premise is supplied by A3053. These results do not close the unrestricted rotating conjecture.

## 7. Sources and verification status

A117's complete comparison and optional R1-R3 were read. Sections2-3 rederive its sign-order argument; Section4 rederives its radial exterior conclusion and adds the exact nonnegative source calculation. Section5 supplies the compact-support exclusion needed to include the critical exponent in the stated conditional Euler consequence. These proofs use exact calculus only. No mathematical computation, diagnostic script or formal build was run. Existing configured model comparison is requested, with actual provider execution independently unattested.


## 8. All fixed centers and a strictly convex exterior test

The statements above hold about every fixed center a. In the kinematic statements replace Q by Q_a(r)=integral_(S2)q(a+r theta)d sigma and replace B_b by B_b(a). The original energy E remains centered at0: the only needed translated bound is

    integral_(B_(2R)(a)) |U|^2 <= E(2R+|a|)=o(R).

The equality on the right denotes its asymptotic order, not equality of the two integrals. The center a is fixed before R tends to infinity. The sign-order proof in Section3 uses the translated test sqrt(1+|y-a|^2) and the same estimates. The full equation is not claimed invariant under arbitrary spatial translation; it is used in its original coordinates only after compact support has been obtained.

Here is a second, direct proof of the exterior conclusion. For beta>b let eta(t)=exp(-1/t-t) for t>0 and0 otherwise, and M=integral_0^infinity eta(t)dt. Then0<M<infinity, eta is smooth and flat at0. Put

    h_beta(r)=M^-1 integral_0^r (r-s)eta(s-beta)ds.

For r<=beta, h_beta=0. For r>beta, h_beta''=eta(r-beta)/M>0 and h_beta'=M^-1 integral_0^r eta(s-beta)ds>0; everywhere0<=h_beta'<=1 and0<=h_beta<=r. Therefore f_beta(y)=h_beta(|y-a|) is smooth, vanishes near a, has positive semidefinite Hessian everywhere and positive definite Hessian outside B_beta(a). Its eigenvalues there are h_beta'' and h_beta'/r.

Use the centered cutoff chi_R(y)=chi((y-a)/R). The integral of q f_beta chi_R is nonpositive because Q_a<=0 on the entire support of f_beta. Its Hessian expansion has main term integral chi_R U.D^2 f_beta U and error bounded by (2K2+2K1)E(2R+|a|)/R. Thus that nonnegative main term tends to zero. For each fixed compact annulus beta+epsilon<=|y-a|<=L, the minimum Hessian eigenvalue is strictly positive, so the energy on that annulus is zero. Continuity and arbitrary epsilon,L give U=0 outside B_beta(a). Let beta decrease to b. This proves the all-center version with no uniform lower Hessian bound at infinity.

A118 supplies another equivalent argument using compactly supported eta: choose it positive at any desired radius r1>b. The zero integrand then contains both eta(r1)|U_rad|^2 and psi'(r1)|U_tan|^2/r1 with strictly positive coefficients, so both components vanish on that sphere. This avoids the intermediate radial remainder in Section4. All three arguments agree.

Consequently, for every nonzero bounded Hb full C1/C1 profile with0<c<1/2 and finite omega, every fixed center a and radius b admit r>b with Q_a(r)>0. A compactly supported q is impossible in that class, including c=2/5, because Q_a then vanishes for all sufficiently large r. This is conditional critical exclusion, not general critical nonexistence. The all-center pressure identity is

    (r^2 pbar_a'(r))'=-r^2 Q_a(r)/(4pi),
    pbar_a(r)=(4pi)^-1 integral_(S2)P(a+r theta)d sigma.

Thus the excluded eventual condition is nondecrease of r^2 pbar_a', distinct from eventual nonincrease of pbar_a itself in the cumulative-source criterion. The proof uses the actual pressure and no choice of its additive constant. The order-R shear from Section6 of LIT369 has q=0 and is not compactly supported; it shows why E=o(R) cannot simply be replaced by E=O(R) in this kinematic theorem.

The complete seven-section LIT369 proof and its25manual checks have been read and independently reconstructed here. Its exact source pin and support files are retained in verification. The invariant-volume mechanism is already known in this campaign as A067; no novelty is asserted for it. The analytical comparison completed as A120 and is checked in Section9. No diagnostic, external referee execution or formal build is certified.

## 9. Completed A120 comparison

The complete in the team records, all eight analytical
items, two optional remarks and the correction to A117, was read. It
agrees with Sections1-8. In particular the three exterior arguments,
using a radial remainder, a test with positive radial second derivative
at a prescribed radius, or the strictly convex exterior test, give the
same conclusion.

Its compact-support energy observation is correct. Dotting the full
equation with U and using div B=3c gives

    (1-5c/2)|U|^2+div(B|U|^2/2+PU)=0.

When U has compact support the vector inside the divergence does too,
even if P has no prescribed growth. Integration gives
(1-5c/2) integral |U|^2=0. This already proves zero for c!=2/5.
The circulation-volume argument of Section5 handles the remaining
critical value and also gives one uniform proof for every c!=0.
This says which step is needed in the present proof, not that every
possible proof must use circulation at the critical value.

The optional kinematic swirl U=(-y2,y1,0)/(1+|y|^2) has

    Q(r)=8pi(1+r^2)^(-2)[4r^2/(3(1+r^2))-1].

Thus Q is negative below sqrt(3) and positive above it. Its energy
grows linearly, so this illustration does not strengthen the theorem
under E=o(R) or prove that distant negative means are impossible
for a full profile. The comparison's smooth columnar shear control
has q=0 and E(R)/(2R) tending to integral_R2 g^2, as direct slicing
of the ball shows.

The A117 historical sentence overlooking the earlier compact-vorticity
result is correctly withdrawn. The original A067 Section5 was also
read independently and captured in the team records; the present
argument uses the same invariant-volume mechanism with its C1
transport justification made explicit. No novelty is asserted.
The described diagnostic script, both execution times and the
separate earlier referee execution are not certified here.
