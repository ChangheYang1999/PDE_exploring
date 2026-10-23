# Why the proved far-field limits do not yet control derivatives

Status: independently derived and checked; external review unavailable. Date: 2026-10-20. Review 12 returned actual claude-opus-5-5 with stop_reason=refusal and no mathematical answer. No model acceptance is inferred. Metadata is in ../../evidence/opus_review_12/metadata.json.

## Statement and exact scope

Fix 0<p<gamma<1 and c_l=1/p. There is a real C-infinity density rho on R^2 with the required even-x/odd-y parities, a0=rho_y(0)>0, canonical U=o(r), and

    |rho|+(1+r)|grad rho| <= C(1+r)^gamma,
    c_l+psi_xy(0)=1,
    R^(-p)rho(RX) -> a |X|^p sin(arg X),  a>0,

locally on punctured annuli in C^alpha for every alpha<1. Its canonical velocity has the corresponding homogeneous leading limit and satisfies U=O(r^p). Nevertheless grad rho is not O(r^(p-1)), and DU is unbounded along a sequence tending to infinity.

This is NOT a profile: the transport equation is not imposed or claimed. It disproves an inference from the stated growth, canonical inverse, origin relation and far-field estimates alone. The derivative conclusion might still follow from additional use of the exact nonlinear transport equation; that remains OPEN.

Dependencies: the strain formula, translation invariance and uniqueness of the canonical inverse in ../inverse/PROOF.md and ../origin/PROOF.md. All constructed auxiliary fields are explicitly smooth; no distributional singularities occur in the final density.

## A small-gradient patch with a large strain

Let chi be a smooth radial cutoff, equal to one for r<=1/2 and zero for r>=1. Let kappa be smooth, zero for s<=1 and one for s>=2. For 0<delta<1/8 define

    q_delta(r,theta)=r sin(3theta) chi(r) kappa(r/delta).

The function vanishes on a neighborhood of zero and is smooth everywhere. Its supremum, L1 norm and supremum of its gradient are bounded by constants independent of delta. For the gradient bound, differentiating the inner cutoff contributes at most C*r/delta on delta<r<2delta. The other terms are bounded homogeneous angular derivatives of r sin(3theta).

The density is even in its first coordinate and odd in its second, and its center derivative is zero. Its canonical center strain is exactly

    c_delta=integral_0^infinity chi(r) kappa(r/delta) dr/r
           =log(1/delta)+O(1),                               (1)

with a constant independent of delta. This is the b3 strain formula; on 2delta<r<1/2 the integrand is 1/r and the two transition regions contribute uniformly bounded quantities. Thus a bounded gradient of the density does not give a bounded pointwise strain of its canonical velocity.

## Separated patches and reflection parity

Choose R_n=2^(n+N), where N will be sufficiently large, and set

    epsilon_n=R_n^(p-1) log R_n,
    delta_n=exp(-epsilon_n^(-2)).

Increase N so every delta_n<1/8 and the four unit disks centered at (+/-R_n,+/-R_n) are disjoint from one another and from every other group. Put

    F_n(x,y)=epsilon_n sum_(sigma,tau in {+1,-1})
                       tau q_delta_n(sigma x-R_n,tau y-R_n),
    F=sum_(n>=1) F_n.

This sum is locally finite, hence C-infinity. It is even in x and odd in y. Its L1 norm, supremum and global Lipschitz norm are finite because sum epsilon_n<infinity. Near its n-th group, |F|+|grad F|<=C epsilon_n. Therefore it satisfies the stated density/gradient growth bound for every gamma>p. It vanishes near the origin.

The canonical velocity U[F] is uniformly bounded. Indeed, for the singular integral over |z|<1 subtract F(X) and use the uniform Lipschitz bound, giving a uniform integral of C/|z|. Over |z|>=1 the kernel is bounded and the L1 norm of F controls the integral. The contact term is bounded too.

At C_n=(R_n,R_n), the local patch contributes

    partial_y U2[F_n](C_n)=epsilon_n c_delta_n
                           =epsilon_n^(-1)+O(epsilon_n).     (2)

The other reflected patches and all other groups are a distance at least a fixed multiple of max(R_n,R_m) away. Outside their supports a derivative of the velocity kernel is O(distance^(-3)). Their total contribution at C_n is O(R_n^(-3)), using sum epsilon_m<infinity and geometric separation. Hence this derivative of U[F] tends to positive infinity.

At C_n+(0,1/4), the local density has derivative F_y=-epsilon_n, since r sin(3theta)=-y on the positive local y-axis and both cutoffs are constant there. Thus the gradient exceeds a fixed multiple of R_n^(p-1) log R_n at these points.

## Adding a nonzero homogeneous leading term and the center relation

Let rho_0=y(1+r^2)^((p-1)/2). Its canonical strain at zero is -1/4. Its canonical velocity and derivatives have their usual smooth homogeneous leading terms, in particular U[rho_0]=O(r^p) and DU[rho_0]=O(r^(p-1)). For example, its only stream mode is h2(r)=-(1/2)r^(-2) integral_0^r s^3(1+s^2)^((p-1)/2) ds, multiplying sin(2theta). Differentiating this explicit formula proves the stated rates.

Let c_F=partial_y U2[F](0). It is finite. It tends to zero as N tends to infinity: all supports are distant, and the derivative-kernel bound gives a convergent O(sum epsilon_n R_n^(-3)) estimate. Choose N large enough that |c_F|<1 and

    a=4(c_l-1+c_F)>0,
    rho=a rho_0+F.

Then rho_y(0)=a and its canonical strain is -a/4+c_F=1-c_l. The center relation is exact. The background derivative at C_n is O(R_n^(p-1)), so it cannot cancel either the logarithmically larger density-gradient patches or the divergent velocity derivative in (2).

## The strong leading limit still holds

On a fixed punctured scaled annulus, only a bounded number of patch groups can occur. Their scaled support radii are O(R^(-1)), their scaled density amplitudes are O(R^(-1)log R), and their scaled Lipschitz bounds are O(log R). The elementary interpolation bound

    [f]_(C^alpha) <= C ||f||_infinity^(1-alpha) Lip(f)^alpha

therefore gives a C^alpha norm O(R^(alpha-1)log R), tending to zero for every alpha<1. The background has smooth homogeneous convergence on such annuli. This proves the asserted density limit, including all the Holder estimates actually used in the established far-field theorem.

The boundedness of U[F] gives R^(-p)U[F](RX)->0 uniformly. For the background the canonical homogeneous limit follows from its explicit radial modes or from local subtraction, compact convergence and the convergent sublinear tail. Thus the constructed field also has the stated velocity leading limit. The example isolates the missing derivative information without purporting to violate any theorem for exact coupled profiles.

The failure of transport is also explicit. Near zero F=0, so the density cubic coefficients are b=e=a(p-1)/2, nonzero. The necessary cubic identity 6e=(a-2A)b with A=2c_l-1 would require a=2A+6=4c_l+4. Our value a=4(c_l-1+c_F), with |c_F|<1, cannot satisfy this. Thus this example actually violates the transport equation, rather than leaving that fact untested.
