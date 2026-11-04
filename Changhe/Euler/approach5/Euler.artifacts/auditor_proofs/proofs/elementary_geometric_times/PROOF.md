# Positive density of large expanding times in an interval tree

## Exact finite-time statement

Let D be one large initial curve in an A305 tree, with normalized arclength lambda and scale epsilon. Each image curve has length at most 2epsilon; each large image has length at least epsilon/2. Suppose every parent has at most A>=1 small children. Every restricted iterate between two levels has arclength distortion at most two. For x outside partition boundaries, write l_i(x)=floor(log J_g(g^i x)), using the tangent to the image of D. On each depth-j atom the l_i, 0<=i<j, oscillate by at most one. Assume they have at most q possible integer values and are bounded above by L.

Choose 0<h<alpha<=L with h>log A. Put theta=(alpha-h)/(L-h), and choose 0<beta<theta. A time j is hyperbolic if sum_(i=s)^(j-1) l_i(x)>=h(j-s) for all 0<=s<j. Let G_n(x) count hyperbolic times j<=n for which the depth-j image is large. Then

    lambda{sum_(i<n)l_i>=alpha n, G_n<beta n}
      <=2 exp(n[log(32q)-(h-log A)(theta-beta)]).

If j is such a time, the tangent expansion from time s to j at every point y of its entire depth-j atom is at least exp((h-1)(j-s)), for all s<j.

## Proof of the finite-time estimate

Fix a derivative word l_0,...,l_(n-1) whose sum is at least alpha n. Let S_j=sum_(i<j)(l_i-h). Every strict record maximum of S_j is a hyperbolic time. The running maximum increases in increments at most L-h, while its total increase is at least (alpha-h)n. Thus there are at least theta n hyperbolic times. Ties can only enlarge this collection.

Fix also a large/small color word u_1,...,u_n, with u_0=large, and let E be the set realizing both words. Its hyperbolic-time set H depends only on l. Partition the small times into maximal consecutive runs after a large time. Whenever a run contains hyperbolic times, retain the interval (s,t] from its preceding large time s to its last hyperbolic time t. These intervals are disjoint, all their depths after s are small, and their total length T is at least the number of hyperbolic small times.

Let R_j be the supremum over depth-j atoms P meeting E of the fraction of the image g^jP occupied by g^j(E intersect P). For arbitrary s<t, subdividing a depth-s atom into depth-t descendants and applying the distortion bound on each gives R_s<=2R_t. This is a weighted average of image fractions; the weights sum to one.

For a retained interval (s,t], every relevant depth-s image is large and has at most A^(t-s) relevant descendants, because all intermediate colors are small. On each descendant Q meeting E, hyperbolicity at a witness gives J_(g^(t-s))>=exp(h(t-s)); distortion gives that lower bound divided by two everywhere on Q. Consequently

    length(g^s Q)<=2exp(-h(t-s))length(g^t Q).

Using the final length upper bound 2epsilon, the initial large length lower bound epsilon/2, and the definition of R_t, summing over these descendants gives

    R_s<=8(A exp(-h))^(t-s)R_t.

Use this stronger bound across retained intervals and R_s<=2R_t across the gaps. With at most n retained intervals and at most one more gap, R_n<=1 and R_0=lambda(E) give

    lambda(E)<=2*16^n exp(-(h-log A)T).

For a bad word, T>=(theta-beta)n. There are at most q^n derivative words and 2^n color words. Summing proves the displayed estimate. This argument uses no count of large children and no lower length bound for small children.

Finally, on a depth-j atom l_i(y)>=l_i(x)-1 for every i<j. Actual logarithmic expansion is at least its floor. Summing from s to j-1 gives the stated whole-atom tangent expansion.

## Consequence for a smooth map and an arbitrary original target

Let f:R^m->R^m be C-infinity, a diffeomorphism with bounded derivatives of every positive order and bounded first derivative of its inverse. Set M_f=max(2,||Df||_infinity,||Df^(-1)||_infinity). Suppose a straight embedded arc contains a positive-length measurable set F such that

    limsup_(N->infinity) N^(-1)log J_(f^N)(x)>=lambda_0>0

at every x in F. Then, after restriction to a straight subarc retaining positive F measure, there exist r>=3, p>=1, epsilon>0, beta>0, and infinitely many n with subsets E_n of that original F, satisfying lambda(E_n)>=1/(2n^2), such that every x in E_n has at least beta n large hyperbolic times for g=f^p, at one threshold h>1. The underlying tree is A305. Parameters may be fixed before any later positive-length restriction of F; the selection argument then works for that restricted set in the same tree.

Choose 0<chi<chi'<lambda_0. Necessarily lambda_0<=log M_f. Choose r>=3 with 3log M_f/(r-1)<chi/2. For g=f^p, A305 allows A=C_r M_g^(3/(r-1)), so

    log A<=log C_r+3p log M_f/(r-1).

Take h=p chi+2, alpha=p chi'-1, L=p log M_f, theta_0=(chi'-chi)/(2log M_f), beta=theta_0/2, and q=2ceil(p log M_f)+3. For sufficiently large p, alpha>h>1, alpha<=L and theta>=theta_0. Moreover h-log A grows at least linearly in p with a positive coefficient, while log(32q) grows logarithmically. Fix p such that

    (h-log A)(theta_0-beta)-log(32q)>1.

The finite-time bad-set bound is then at most 2exp(-n).

Choose epsilon for the derivatives of this fixed g, decreasing it if necessary. Cover the interior of the original straight arc by finitely or countably many length-2epsilon subarcs contained in it. One retains positive F measure. Parametrize it at speed epsilon. It is a small bounded large initial curve. Use normalized arclength on this restriction.

Writing N=np+j with 0<=j<p shows that the logarithms of J_(f^N) and J_(f^(np)) differ by at most p log M_f. Hence the same positive limsup holds on multiples of p. Every point of F lies in infinitely many sets F_n={x in F:J_(g^n)(x)>=exp(np chi')}. If lambda(F_n)<1/n^2 eventually, the first Borel-Cantelli lemma contradicts positive measure of their limsup. Thus infinitely many n have lambda(F_n)>=1/n^2. On F_n the sum of logarithmic floors is at least alpha n. Delete the bad set; for all sufficiently large such n the retained E_n has measure at least 1/(2n^2) and the asserted density of times.

This last selection uses only positive measure and the pointwise limsup. It therefore remains valid for any subsequent positive-length subset of the fixed original target, without changing the parameters or tree. In particular a uniform original-density subset can be chosen first.

## Dependencies and scope

This independently proves LIT66 from A305. The elementary inputs are record maxima, interval-tree counting, arclength distortion and the first Borel-Cantelli lemma. No external entropy or reparametrization theorem is used. This result supplies time selection and original-set retention, not an invariant measure or basin coverage. No computation or formalization was used. The immutable input and its hash are in the team records.
