# Larger compatible shape disks from exact response polynomials

Status: PROVED. The independent Cartesian certificates and the theory part's separate Fourier and rational computations agree. The independent review dated 2026-10-31T11:06Z is recorded in V284. All conclusions retain the exact hypotheses and scope stated below.

## Exact hypotheses and statement

Let c=3 and let O(b,tau) be the exact sixth-order compatibility polynomial for f_1=sin(theta)+b sin(3theta)+tau sin(5theta). Let I=[l,u] be an exact interval isolating either sextic root from119, and put m=(l+u)/2. Choose positive rationals h,t0,s. Expand

    O(m+x,tau)=sum c_ij x^i tau^j,              A=c_10.

Suppose

    (u-l)/2<h,
    sum_((i,j)!=(1,0)) |c_ij| h^i t0^j < |A|h.             (1)

For each finite response2<=k<=9, expand sigma_k(m+x,tau)=sum d_(k,i,j)x^i tau^j. Suppose

    |d_(k,0,0)|-sum_((i,j)!=(0,0)) |d_(k,i,j)|h^i t0^j > s. (2)

Use the exact rational response sigma_k=N(k,b,tau)/D(k) valid for every integer k>=10 from136. After putting k=10+w, write

    N(10+w,m+x,tau)=sum_(ell,i,j) n_(ell,i,j) w^ell x^i tau^j,
    D(10+w)=sum_ell D_ell w^ell.

Require D_ell>=0 for every ell, D_0>0, and

    -n_(ell,0,0)-sum_((i,j)!=(0,0)) |n_(ell,i,j)|h^i t0^j
                        -s D_ell >=0                     (3)

for every ell, with strict inequality for ell=0. Missing coefficients are zero. The sign convention may be arranged by multiplying both N and D by-1, but it must be checked explicitly.

Then there is a unique holomorphic b(tau), defined on a neighborhood of |tau|<=t0, with |b(tau)-m|<h, O(b(tau),tau)=0 and b(0) equal to the selected exact sextic root. It is real for real tau. Every such real profile has the uniquely tuned convergent pure density and stream series, with all weighted derivatives and the common potential. A common sufficient radius follows from the component certificate134 with Q3, B6, kappa14, leading norm bound a>=1+|m|+h+t0, and response lower bound s.

## Proof of the shape branch

On the circle |x|=h and the closed parameter disk |tau|<=t0, (1) gives |O(m+x,tau)-Ax|<|Ax|. The homotopy from Ax to O has no zero on the circle. Its winding number is one, so the argument principle gives exactly one zero inside, counted with multiplicity. It is therefore simple. The strict inequality persists for a slightly larger parameter disk. Local holomorphic implicit branches patch uniquely on that disk. At tau0 the selected algebraic root lies inside the circle, so it is the branch value. Complex conjugation and uniqueness make b(tau) real for real tau.

## Uniform control of every response

For complex |x|<=h and |tau|<=t0, let epsilon_k be the sign of the real nonzero constant d_(k,0,0). The triangle inequality gives

    Re[epsilon_k sigma_k(m+x,tau)]
       >= |d_(k,0,0)|-sum_((i,j)!=(0,0)) |d_(k,i,j)|h^i t0^j.

Condition(2) therefore gives |sigma_k|>s for every finite k under consideration. Each finite response may have its own sign; they are not assumed all negative.

For real w>=0, apply the same estimate to each coefficient polynomial of N. Condition(3) implies

    Re[-N(10+w,m+x,tau)] >= s D(10+w).

The denominator is strictly positive because D_0>0 and its coefficients are nonnegative. Dividing shows Re sigma_k<=-s for every real k>=10, in particular every remaining integer. Thus |sigma_k|>=s uniformly throughout the entire complex bidisk, including the compatible root branch. This proof controls complex perturbations directly; positivity of coefficients for real b and tau alone would not suffice.

The branch has exact compatibility and a uniform positive response bound. Theorem119 therefore supplies its unique tuned pure series. Its norm is at most1+|m|+h+t0. Applying the exact positive majorant with B6, kappa14 and this common norm/response bound yields the stated uniform exterior convergence and all weighted derivative bounds. Topic121 reconstructs the common potential with the same strict radius and logarithms only at orders3and6. Normal convergence of the rational coefficient construction proves holomorphic dependence on tau on a smaller common exterior disk.

## Finite implementation and scope

The exact computation tests t0=2^(-q), h=2t0 for nonnegative integers q. It retains failed trials and the first successful inequalities for each root, including every finite response margin and every shifted tail coefficient margin. The circle condition uses the exact O polynomial; the response conditions use the exact bivariate formulas136. A rounded-up rational a is independently compared with1+|m|+h+t0 before the component radius is calculated.

This method does not impose the much smaller sufficient perturbation ball from122. It establishes the required uniform response lower bound directly. An unsuccessful trial does not prove that a larger compatible branch or a better convergence radius is impossible. Every numerical disk size, response bound and exterior radius must have a complete exact certificate before publication.

Dependencies:119for the base sextic roots and tuned convergence,121for the potential,125for O,136for the exact three-mode responses,134for the component radius, and the elementary argument principle. No empirical high-order data are used.

## Completed exact disks

For the first sextic root, the certificate gives t0=1/512, h=1/256, response lower bound s=1/100000, leading norm bound a=1287/1000, and common exterior R>2^63. For the second root it gives t0=1/128, h=1/64, s=1/2000, a=167/100, and R>2^57. Each radius is multiplied by |epsilon|^(3/2) when scaling the complete leading profile by epsilon.

The exact circle ratios are approximately0.5288219757900406 and0.9982967994175486; both are strictly below1. Every finite response margin and every tail coefficient margin is strictly positive. The first implementation incorrectly required all finite central responses to be negative and therefore rejected the second root: sigma2 is positive there. That failed attempt is retained. The corrected certificate uses the separate sign of each finite response, as required by the proof above. All later checks pass.
