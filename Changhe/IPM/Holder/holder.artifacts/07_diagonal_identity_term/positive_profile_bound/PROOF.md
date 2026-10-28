# A cancellation-free bound for the projection-profile constant

Use the notation and hypotheses of `../refined_profile_constant/PROOF.md`.
For 0<alpha<=1/2, k=1/(1-alpha), R=u^alpha, define

$$\widetilde B(u)=1+\frac{k-1}{8R}(1-R)^2
 +\frac{1-R}{2}((1-u)^{-\alpha}-1).$$

Then B(u)<=Btilde(u), so replacing B by the minimum of B and Btilde
in the finite enclosure procedure preserves a rigorous upper bound for
K_alpha. The new expression avoids cancellation between its first two
terms when alpha is small.

For completeness, let M=((1+R^k)/2)^(1/k) and m=(1+R)/2.
The second derivative of t^k on [R,1] is at most k(k-1)R^(k-2)
for 1<k<=2. The midpoint Taylor estimate gives

$$M^k-m^k\le k(k-1)R^{k-2}(1-R)^2/8.$$

The mean value theorem and m>=R give
M^k-m^k>=k R^(k-1)(M-m). Combining these inequalities proves
M-m<=(k-1)(1-R)^2/(8R). Finally,

$$B=1+(M-m)+\frac{1-R}{2}((1-u)^{-\alpha}-1).$$

This proves the claimed bound. Both correction terms in Btilde are
nonnegative. The endpoint enclosures from the preceding note apply
unchanged. This is an upper bound for a sufficient seminorm constant,
not an assertion of the exact seminorm of the local profile.
