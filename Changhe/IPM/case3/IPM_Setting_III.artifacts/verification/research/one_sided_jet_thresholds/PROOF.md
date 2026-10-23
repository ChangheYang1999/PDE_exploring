# Taylor thresholds from a one-sided affine defect

Date: 2026-10-20. Status: independent analytic audit CONFIRMED; separate exact checks will follow. This reconstructs the claims requested as FLAT1S(c),(d). The additional sign is not known for the primary admissible class.

## Statement and dependencies

Let ell>1, D=ell-1 and A=2ell-1. Suppose a smooth exact canonical profile in the primary class has a=rho_y(0) nonzero and the extra inequality y(y-rho/a)>=0 everywhere. Write H=y-rho/a. Result70, ../one_sided_flat_exclusion/PROOF.md, proves that H is not flat. Let n=2K+1>=3 be its first nonzero homogeneous degree. Then:

1. If K is odd, a>=2A+n-3.
2. If A<=n, a>=(n-1)A.
3. For n=5 the exact necessary and sufficient range for a nonnegative compatible leading jet is a>=4A when 1<A<=9. When A>9 the range is a>=4A or a<=2(A^2-18A+1)/(A-9), with a=0 omitted as in the profile hypothesis.

In particular, without a strain cap but with the extra one-sided sign, ell<=3 implies a>=(n-1)A, and ell<=5 implies a>=2A>0. These are necessary conditions. The sufficiency statements below concern finite leading jets only.

The local algebra only needs yH>=0 in a neighborhood and a nonzero first degree. The global sign is used solely to invoke the flat exclusion. No analyticity is assumed.

## Leading equations without division by a resonance

Put phi=psi+Dxy, v=(-phi_y,phi_x), and V=phi_x. Exact transport is W.grad H=H+V, where W=(Ax,y)+v. Since H=O(r^n), this identity gives V=O(r^n). The odd-in-x stream obeys phi(x,y)=int_0^x V(s,y)ds, so phi=O(r^(n+1)) and v=O(r^n). Thus

    V_n=(Ax*d_x+y*d_y-1)H_n,
    Delta phi_(n+1)=a*(H_n)_x,   (phi_(n+1))_x=V_n.

Expand H_n=sum_(j=0)^K c_j x^(2j)y^(n-2j), and put e_j=n-1+2j(A-1)>0. Differentiating the elliptic equation in x and comparing coefficients gives, for 0<=j<K,

    (n-2j)(n-2j-1)e_j c_j
      +(2j+2)(2j+1)(e_(j+1)-a)c_(j+1)=0.                 (1)

Conversely (1) implies the full leading elliptic equation: integrate V_n in x from zero, observe that the x derivative of Delta phi-a H_x vanishes, and use its odd-in-x parity to remove the integration constant. Hence no equation has been lost.

All coefficients c_j for j<K are obtained backwards from c_K by division only by the positive coefficient of c_j in (1). The solution space is one-dimensional, and a nonzero solution has c_K nonzero even when a=e_j. The sign is equivalent to

    P(t)=sum c_j t^j>=0,  t>=0,

because H_n/y=y^(2K)P(x^2/y^2) away from y=0 and by continuity on the axes. It requires c_K>0 and c_0>=0. Recurrence (1) yields c_0=C c_K prod_(j=1)^K(a-e_j), C>0. For odd K, a<e_1 makes every factor negative, contradicting c_0>=0. This proves statement1.

## Positive integral proof for every degree with A<=n

Set b=A-1, eta=K/b>0 and chi=1+(2K-a)/(2b). A polynomial spanning (1) is

    F_chi(t)=sum_(j=0)^K (-1)^j binom(2K+1,2j)
                         (eta)_j (chi+j)_(K-j) t^j,       (2)

where (z)_j is the rising factorial. To verify it, compare adjacent coefficients using (1); after canceling their common polynomial factors this is an identity, hence also holds at each zero of a canceled factor. The highest coefficient is (-1)^K(2K+1)(eta)_K and never vanishes. Thus (2) also spans at all resonances.

Suppose A<=n and a<2KA. These conditions are respectively eta>=1/2 and chi>1-K. Fix J=K-1, so u=chi+J>0. Let T have density proportional to t^(u-1)(1+t)^(-u-K-3/2) for t>0. If eta>1/2 let S, independently, have density proportional to s^(-1/2)(1-s)^(eta-3/2) on (0,1). At eta=1/2 take S=1. All moments through order K are finite. Integration by parts gives

    E T^j=(-1)^j (u)_j/(-K-1/2)_j,
    E S^j=(1/2)_j/(eta)_j,          0<=j<=K.              (3)

For the first identity integrate the derivative of t^(u+j)(1+t)^(-u-K-1/2), for j<K. Its endpoint terms vanish and its two terms give successive ratio (u+j)/(K+1/2-j). For the second integrate the derivative of s^(j+1/2)(1-s)^(eta-1/2), obtaining (j+1/2)/(j+eta). Normalizing the zeroth moment proves (3); the endpoint eta=1/2 is immediate.

The elementary factorial identity

    binom(2K+1,2j)=(-K)_j(-K-1/2)_j/((1/2)_j*j!)

now gives

    E F_chi(TS)
       =sum_(j=0)^K (-1)^j binom(K,j)
                         (chi+j)_(K-j)(chi+J)_j=0.        (4)

Here is a proof of the last equality that covers every resonance. For parameters where division is allowed, the product in the summand is

    ((chi)_K/(chi)_J)*(chi+j)_J.

The alternating binomial sum vanishes since the K-th finite difference annihilates the degree-J polynomial in j, with J=K-1<K. Before this rewrite the entire sum is polynomial in chi, so the vanishing extends to all chi. Equation (4) is consequently valid for the chosen positive distribution even if some coefficients in (2) vanish.

The law of TS has positive mass on every nonempty open subinterval of (0,infinity). A nonzero polynomial nonnegative on this interval has a strictly positive integral against that law, since its K-th moment is finite. The same argument applies to every nonzero scalar multiple of F_chi. Thus (4) contradicts P>=0. This proves a>=2KA.

For the threshold a=2KA=e_K, recurrence permits P(t)=t^K, corresponding to H_n=x^(2K)y. For a>e_K choose c_K>0; the backward recurrence makes every coefficient positive. The necessary threshold is therefore sharp for compatible leading jets. It does not construct an exact profile.

## Complete quintic calculation

For K=2, set e_1=2A+2 and e_2=4A, and normalize c_2=1. Recurrence gives

    P(t)=t^2+2(a-e_2)t/e_1+(a-e_1)(a-e_2)/(20e_1),
    disc(P)=(a-e_2)*[(20-e_1)a+e_1^2-20e_2]/(5e_1^2).   (5)

If a>=e_2, coefficients are nonnegative. If e_1<a<e_2 the constant is negative. If a=e_1<e_2 the linear coefficient is negative. If a<e_1, the constant is positive and the vertex is in t>0, so nonnegativity is equivalent to disc(P)<=0. Since a-e_2<0, this is equivalent to the bracket in (5) being nonnegative.

When A<=9, 20-e_1>=0 and the bracket at a<e_1 is less than its value 20(e_1-e_2)<0 at e_1. No lower branch exists. When A>9, solving the reversed linear inequality gives

    a<=a_*(A)=2(A^2-18A+1)/(A-9).

This upper endpoint lies strictly below e_1, since a_*-e_1=-20(e_2-e_1)/(e_1-20)<0. This proves the claimed exact classification without discarding resonances or double roots.

At ell=6, A=11, a=-76, one example is

    H_5=y*(y^2-x^2/5)^2,
    V_5=4y^5-(48/5)x^2y^3+(44/25)x^4y,
    phi_6=4xy^5-(16/5)x^3y^3+(44/125)x^5y.

Direct differentiation gives V_5=(11x*d_x+y*d_y-1)H_5, phi_x=V_5 and Delta phi=-76H_x. The classification supplies a nonnegative compatible jet for every a<=-76 at this fixed ell. For a=-100, another normalization is H_5=y^5-(10/31)x^2y^3+(5/186)x^4y; the quadratic discriminant is -10/2883, so H_5/y is strictly positive away from the origin. Neither example is a profile. For rho=a(y-H_5) and psi=-Dxy+phi_6 the nonlinear transport residual is -a*v.grad H_5, a nonzero degree-nine polynomial, and the fields violate sublinear growth.

## Consequences and limits

If ell<=3 then A<=5. Cubics obey a>=2A by statement1, and all n>=5 satisfy A<=n, so statement2 covers the remaining degrees. If ell<=5 then A<=9. Cubics and quintics are covered by their classifications; for n=7, odd K gives a>=2A+4; for n>=9 statement2 applies. This proves the stated exact-profile consequences once the global sign excludes flatness.

For larger ell, negative leading jets show that sign-compatible local algebra alone cannot imply positive a or a universal lower bound. They do not settle whether any global exact profile realizes such jets. Without the one-sided sign, none of these new exclusions is a theorem about the full primary class. The team's principal endpoint remains UNRESOLVED.

Verification sources: lead referee/flat1s/PROOF.md Sections6-8, read as a claim to audit; the recurrence, positive integral and classification were separately reconstructed here. No source implementation was imported. Supporting exact identities are stored in verification after their independent checker runs. The actual Claude Opus5.5 lead is the available collaborating model; no external Bedrock review is claimed.
