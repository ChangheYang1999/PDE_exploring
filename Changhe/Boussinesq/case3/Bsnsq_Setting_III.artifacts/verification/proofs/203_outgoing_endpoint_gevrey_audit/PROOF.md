# Outgoing endpoints: independent proof and scope audit

Status: CONFIRMED for the revised candidate v2 under its stated local hypotheses. The complete informal derivation preceded executable controls. Independent model review, version history and final verdict are recorded in verification/. The assertions below are conditional local obstructions, not a global nonexistence theorem. Coordinates are oriented orthonormal coordinates; a rotation does not change curl or divergence. All fields are real smooth on a full neighborhood of p=0.

## 1. Statement and dependencies

Assume div W=4 and Omega=-curl W, where curl W=partial_s W_z-partial_z W_s. Assume W(0)=0, DW(0)=diag(0,4), and every derivative of Omega vanishes at 0. The normal nullcline is z=k(s), k(0)=k'(0)=0. On it W=(f(s),0), where f is zero for negative s and strictly positive for sufficiently small positive s. Let sigma(0)=sigma'(0)=0 and O={s>sigma(z)} locally, with Omega=0 on O. These are the outgoing endpoint hypotheses from the already audited basin and chart statements. The linearization alone does not imply these hypotheses.

Then:

1. No real analytic vector field defined across 0 can agree with W on a measurable subset of O having positive area in every neighborhood of 0.
2. For no constants epsilon,C,A>0 and fixed unit direction e do the bounds |partial_e^n W|<=C A^n(n!)^2 hold at every point of O intersect B_epsilon for every integer n>=0.
3. For each fixed e and each disk B about 0 contained in the original domain, and each A>0, the supremum over n and B of |partial_e^n Omega|/[A^n(n!)^2] is infinite. These are neighborhood suprema, although the entire jet at 0 is zero.
4. Suppose in addition there is the area chart of the zero arc X(a,r), a<=0, with det(X_a,X_r)=1, W(X)=4rX_r, Theta(X)=theta(a), and the Boussinesq transport equation W.grad Omega+Omega=Theta_x in the original physical coordinates. If the physical tangent satisfies tau_x(0)!=0, then, on a sufficiently small chart rectangle, Omega(X(a,r)) is nonzero exactly for a in an open set J accumulating at 0. The directions of accumulation of nonzero Omega at 0 are exactly {v in S^1:v_s<=0}.

The chart is an explicit dependency of assertion 4, established in P188 and rechecked in P199. Its origin normalization is X_a(0,0)=tau and X_r(0,0)=n. Conclusions 1 to 3 do not use its transport formula. The global assertion that Z=gamma gives two outgoing endpoints is a separate previously audited classification hypothesis; nothing here proves it from local eigenvalues.

## 2. Analytic agreement on positive area

Take a square Q={|s|,|z|<epsilon} with |sigma(z)|<epsilon/2. The set O intersect Q is connected: every point connects horizontally to s=3epsilon/4, and that vertical segment is contained in the set. The div-curl identities show that both components of W are harmonic there, hence real analytic. For completeness, the local mean-value representation on a smaller disk gives the Poisson kernel representation; its convergent power series on every strictly smaller disk shows real analyticity.

A real analytic function zero on a positive-area subset of a connected open set vanishes throughout. Cover the open set by countably many interior rectangles; one rectangle meets that subset in positive area. Fubini supplies a positive-measure set of horizontal parameters with positive-length zero sets in the transverse variable. One-dimensional analyticity makes the function zero on those whole slices. Applying one-dimensional analyticity in the other variable now makes it zero on the rectangle. Continuation through overlapping interior disks proves the assertion on the connected set. Apply this to each component of V-W. The assumed positive-area property ensures that one can choose Q inside both domains.

Thus V=W on O intersect Q. Differentiating this open equality and passing to 0 shows equality of all jets. The analytic implicit function theorem gives the nullcline k_V of V_z, because partial_z V_z(0)=4. Differentiating the implicit equation recursively determines its jet uniquely from that of V, so k_V and k have identical jets. Consequently f_V(s)=V_s(s,k_V(s)) is analytic and has zero Taylor series, since f is zero on a negative interval. Hence f_V=0 near 0. For small positive s, sigma(k_V(s))=O(s^4)<s, so this nullcline lies in O. There V=W and uniqueness of the smooth nullcline implies k_V=k. This forces f(s)=0 for positive s, a contradiction.

## 3. A flat holomorphic defect on a full tangent disk

Write w=s+iz and partial_bar=(partial_s+i partial_z)/2. Define

K=W_s-iW_z+4iz, S(w)=w-K(w)/2,
Sstar(w)=conjugate(S(conjugate(w))), R(w)=conjugate(S(w)).

Direct differentiation gives partial_bar K=i Omega/2 and partial_bar S=-i Omega/4. The exact velocity identity is W_s+iW_z=2(w-R(w)). Moreover S(0)=0 and DS(0)=I. These are identities of smooth real maps, so the defect

E(w)=Sstar(S(w))-w=R(R(w))-w

is defined smoothly near 0. Its two displayed compositions agree by direct substitution, without interchanging composition order.

Choose constants B,C with |S(w)-w|<=B|w|^2 and |sigma(z)|<=C z^2. Choose M>B+4C sufficiently large that all maps below remain inside the original neighborhood and |S(w)|<=2|w|. The disk D_M={Re w>M|w|^2}, centered at 1/(2M) with radius 1/(2M), lies in O. For w in this disk,

Re S(w)>(M-B)|w|^2>4C|w|^2>=sigma(-Im S(w)).

Hence S(w) belongs to the reflected basin Ostar. S is holomorphic on O and Sstar on Ostar, so E is holomorphic on the whole D_M. This includes points arbitrarily close to the tangent boundary. Both D_M and S(D_M) can be placed in any prescribed small disk by increasing M.

Flatness of partial_bar S means that each homogeneous term of its formal real Taylor expansion solves the Cauchy-Riemann equation, hence is a complex constant times a power of w. The same is true for Sstar and their formal composition E. On the negative zero arc w=s+ik(s), the velocity identity gives R(w)=w, hence E(w)=0. If E had a first nonzero Taylor term d_m w^m, substitution would give 0=d_m s^m+o(|s|^m), impossible. Thus E has zero smooth Taylor jet. This uses finite Taylor expansions at each order, not convergence of any formal series.

For kappa(s)=s+ik(s), s>0, the identity gives R(kappa)=kappa-f(s)/2. Since f=o(s) and k=O(s^2), the horizontal segment from kappa-f/2 to kappa lies in O. On that segment partial_s R=conjugate(S'). The fundamental theorem of calculus yields

E(kappa(s))=-f(s)/2 [1+integral_0^1 conjugate(S'(kappa(s)-t f(s)/2)) dt]
            =-f(s)(1+O(s)).

The bracket tends to 2, so E is nonzero there. For the contradiction on D_M it is necessary that these evaluation points lie in D_M, not only in O. This holds for each fixed M and sufficiently small s>0: Re kappa=s and |kappa|^2=s^2+O(s^4), so s>M|kappa|^2. This explicit observation completes the otherwise implicit last domain step in the candidate outline.

## 4. Directional Gevrey bounds and the critical uniqueness argument

Suppose the bound in assertion 2 holds. The affine correction in K can be absorbed in constants. On O, for n>=1,

partial_e^n K=(e_s+i e_z)^n K^(n),

and the prefactor has absolute value one. Thus the holomorphic derivatives of K, S and Sstar satisfy uniform bounds C A^n(n!)^2 on the required basin and reflected basin pieces.

Here is an explicit composition estimate. Suppose |b^(k)|<=C_b A_b^k(k!)^2 and |h^(j)|<=C_h A_h^j(j!)^2 at the relevant points. Taylor substitution gives for n>=1

|(b compose h)^(n)|/n! <= C_b A_h^n sum_{k=1}^n (A_b C_h)^k sum_{j_1+...+j_k=n, j_i>=1} k! product_i j_i!.

For every ordered composition, product j_i! is largest at (n-k+1,1,...,1), by transferring units to a largest entry. Therefore k! product j_i!<=n!, since n!/(n-k+1)!>=k!. There are binomial(n-1,k-1) ordered compositions. With x=A_b C_h this proves

|(b compose h)^(n)|<=C_b A_h^n(n!)^2 x(1+x)^(n-1).

Consequently E obeys a uniform bound C_1 A_1^n(n!)^2 on D_M. No estimate is assumed on the arc side.

We now prove the needed critical uniqueness fact. Let G be holomorphic on D_M, extend smoothly and flatly to 0, and satisfy that derivative bound. The radial segment tw, 0<t<=1, remains in D_M. Taylor's integral remainder along it gives

|G(w)|<=C_1 A_1^n n! |w|^n

for every n>=1. For sufficiently small |w| choose n=floor(1/(2A_1|w|)); then n!<=(n)^n, and the right side is at most C_1 2^(-n)<=C_2 exp(-c/|w|). On the remaining region |w|>=r_0>0, exp(-c/|w|)>=exp(-c/r_0), so increase C_2 using the n=0 bound. The inequality |w|<1/M alone gives the opposite exponential comparison and must not be used for this absorption. Thus this exponential estimate holds uniformly on D_M.

The inversion zeta=1/w maps D_M exactly onto Re zeta>M. Put P(zeta)=G(1/zeta); it satisfies |P(zeta)|<=C_2 exp(-c|zeta|). If P is not identically zero, there is a real x_0>M with P(x_0)!=0, by the identity theorem. Put d=x_0-M>0 and g(u)=P(M+d(1+u)/(1-u)). This is holomorphic on the unit disk and g(0)!=0. The submean inequality for log|g| gives

log|g(0)|<=log C_2 - c/(2pi) integral_{-pi}^{pi}|M+d(1+r exp(it))/(1-r exp(it))| dt.

One can first take radii avoiding zeros on the circle, or use the subharmonic mean inequality directly; interior zeros do not reverse this bound. For 1-r<=t<=1/4 and r sufficiently close to one, |1+r exp(it)|>=1 and |1-r exp(it)|<=2t. The integrand is therefore at least d/(2t)-M. Its integral tends to infinity logarithmically as r increases to one; the integrand is nonnegative elsewhere. This contradicts the finite left side. Hence G=0. Applying this result to E contradicts its nonzero values inside D_M. Assertion 2 follows, including the critical order 2. The division by n! in Taylor's remainder is essential.

## 5. Transfer from directional vorticity regularity

Suppose |partial_e^n Omega|<=C A^n(n!)^2 on a disk about 0. Construct a cutoff chi supported inside that disk, equal to one near 0, with the same type of bounds in direction e. A complete one-dimensional construction is as follows. For |t|<1 put b_0(t)=exp(-1/(1-t^2)), and put b_0=0 outside. With d=1-|t|, choose a fixed sufficiently small c_0>0. For |z-t|<=c_0 d, the complex number 1-z^2 differs from 1-t^2, which lies in [d,2d], by at most a fixed small fraction. Thus Re (1-z^2)^(-1)>=c_1/d. Cauchy's estimate gives

|b_0^(n)(t)|<=n!(c_0d)^(-n) exp(-c_1/d)<=C_0^n(n!)^2,

by maximizing v^n exp(-v) at v=n and using (n/e)^n<=n!. Fixed-order derivatives vanish at the endpoints by the same estimates, so the zero extension is smooth. Normalize a rescaled copy to have integral one and convolve with an interval indicator to obtain a compact cutoff equal to one on a smaller interval. Take its product with any compact smooth transverse cutoff. Only the first factor is differentiated by partial_e. This yields chi in an arbitrarily small rectangle inside the original disk.

Leibniz's rule gives the desired bound for q=i chi Omega/2. Indeed binomial(n,j)(j!)^2((n-j)!)^2=n!j!(n-j)!<=(n!)^2, and summing the geometric factors increases A at most by a constant factor.

Define Tq(w)=pi^(-1) integral_C q(zeta)/(w-zeta) dA(zeta). Its locally integrable kernel obeys partial_bar(1/(pi w))=delta_0, checked by integration by parts on an annulus and the inner circular boundary integral. Consequently partial_bar Tq=q. Because q is compact and smooth, directional derivatives transfer to the source distributionally and hence classically: partial_e^n Tq=T(partial_e^n q). This avoids differentiating a nonintegrable kernel absolutely. For w in a fixed smaller disk, all support differences lie in B_R, so pi^(-1) integral_support |w-zeta|^(-1)dA<=2R. Thus Tq has the same directional Gevrey bound.

Near 0, K-Tq is holomorphic since chi=1 there; its derivatives on a smaller disk have ordinary Cauchy bounds C B^n n!. Hence K and W have directional Gevrey-2 bounds on that smaller full disk, contrary to assertion 2. This proves assertion 3 for small disks, and therefore for any larger disk in the domain. Since each finite-order supremum on a compact smaller disk is finite, the equivalent limsup of [sup|partial_e^n Omega|/(n!)^2]^(1/n) is infinite. No statement of divergence of pointwise derivatives at p is intended.

## 6. Whole fibers and the exact direction set

In the assumed area chart, det(X_a,X_r)=1 implies a_x=y_r in the physical coordinates. Boussinesq transport becomes

(4r partial_r+1) omega(a,r)=theta'(a)y_r(a,r), where omega=Omega compose X.

Multiply the orbit equation by exp(t), integrate from t=-infinity to zero with r(t)=r exp(4t), and use boundedness at r=0. Substitution u=exp(4t) gives

omega(a,r)=theta'(a) mu(a,r),
mu(a,r)=1/4 integral_0^1 u^(-3/4)y_r(a,ur) du.

The weight is integrable and all derivatives on the compact chart are bounded, so mu is smooth. At (0,0), mu=y_r=n_y=tau_x in a positively oriented frame. Under the nonvertical physical tangent hypothesis this is nonzero; shrink the closed chart rectangle so mu remains nonzero throughout. Thus omega!=0 exactly when a belongs to J={a<0:theta'(a)!=0}, which is open.

If J did not accumulate at 0, omega would vanish on a terminal arc-side chart neighborhood. It already vanishes on O and, by continuity, on their common boundary. Together these sets contain a disk about 0. The div-curl identities would make W harmonic on that disk, contradicting assertion 1 with V=W. Thus J accumulates at 0. This proof does not need to assume theta monotone or that J contains a terminal interval.

In endpoint coordinates DX(0,0)=I. For a unit vector v with v_s<0, choose a_j in J tending to zero, set t_j=a_j/v_s>0 and r_j=t_j v_z. Then X(a_j,r_j)=t_j v+O(t_j^2) and omega there is nonzero. For the two vertical unit vectors instead put r_j=plus or minus sqrt(|a_j|). The leading vector is vertical and the error is O(|a_j|), giving both vertical limits. Conversely, nonzero omega lies on the arc side s<sigma(z)=O(z^2). Dividing by |(s,z)| and taking a limit forces v_s<=0. This proves both inclusions. It asserts intersections with every open sector containing such a direction, not positivity or nonvanishing throughout any sector. If tau_x=0, the nonzero-factor argument fails and this support conclusion is not proved.

## 7. Scope checks and counterexamples to stronger readings

Orders between 1 and 2 are excluded because (n!)^rho<=(n!)^2. W differs from physical U by an affine function when beta=2, so local directional regularity transfers between them. The proof does not exclude all smooth fields or orders greater than 2, and no existence is established in the remaining class.

The scalar example b(w)=integral_0^infinity exp(-t)/(1+tw) dt, Re w>0, has |b^(n)|<=(n!)^2 even up to Re w=0, by dominated differentiation and |1+tw|>=1. Its limiting derivatives at 0 are (-1)^n(n!)^2, so its Taylor coefficients (-1)^n n! have zero convergence radius. It is not flat and is not asserted to satisfy the endpoint geometry. It proves that uniform Gevrey-2 bounds for holomorphic basin germs are weaker than analytic continuation. Here smooth up to the closed half-plane means all one-sided derivatives extend continuously; no holomorphic extension is asserted.

The proof in fact needs W bounds only on D_M together with R(D_M), not the entire basin. If the same bounds hold on one tangent disk D_L contained in O, choose M>B+4L sufficiently large. Then D_M is contained in D_L, and Re R(w)=Re S(w)>(M-B)|w|^2>4L|w|^2>=L|R(w)|^2, so R(D_M) is also contained in D_L. The same proof applies. Therefore a blanket statement that bounds on any smaller part of O give no exclusion is false; such tangent disks are sufficient. The candidate v1 Scope has this overbroad wording and requires correction.

The tangent-disk domain is indispensable to the critical argument as given. For example exp(-1/w) is flat and holomorphic with Gevrey-2 estimates on every fixed proper closed sector in the right half-plane, by Cauchy estimates on disks of radius a|w| contained in a slightly wider sector and the bound exp(-c/|w|). It is not continuously zero at the tangency point uniformly on D_M: along 1/w=M+1+it its absolute value is exp(-(M+1)). Thus a proof using only proper sectors cannot substitute for the domain step above. This control is a scalar example, not a Boussinesq solution.

Gevrey order 2 is not quasianalytic, as the explicit compact cutoff above proves. Therefore the new exclusion is not merely an application of a quasianalyticity criterion. The previously proved global classification, when its full assumptions including Z=gamma hold, supplies outgoing endpoints at both ends; local obstructions may then be applied separately. If those assumptions are absent, the present proof supplies no outgoing endpoint on its own.

## 8. Audit coverage

The frozen candidate is work/enter_xix/text_v1.md, SHA256 b583c237ca61627c231d1e8e373cfbb3cf11090e2d4f6cb93de1a358e1e225c3. Its source proof SHA256 is 2f915eab80c38417e8322ffe342c809561f9d7c45b6b2c7994e0ec457af73b39. This derivation confirms the core assertions G1 to G6. G7 requires replacing its blanket statement about smaller parts of O by the specific proper-sector or individual-line limitation. X8 should specify endpoint uniformity, since W is analytic on every compact subset of the open basin. X11 should name U and Omega; the preceding criterion also discusses Theta, whose Gevrey-2 exclusion is not proved here. X12 should say general obstruction and should not say the consultations obtained only exclusions, since they also obtained necessary conditions and continuation statements. These are scope repairs, not changes to the proved local obstructions. Bookkeeping of the actual report insertion must be checked after insertion; a preview is not an entered report. The explicit inclusion kappa(s) in D_M is an explanatory completion, not an added hypothesis. No numerical evidence is used to prove the analytic theorem, and no formal proof is claimed.

## 9. Revised candidate adjudication

The candidate v2, SHA256 c7972a0175d4666b945e6adffbe5c2f9bd0dc2045ecf8667b887bad7c085eee3, was read together with an independently generated complete v1-to-v2 diff. It adds the reflected derivative evaluation and positive-nullcline disk placement, replaces the blanket smaller-region non-exclusion by the proper-sector or individual-line limitation, states the stronger sufficient tangent-disk assumption, names U and Omega in the local regularity summaries, and qualifies the general obstruction. The core assertions are unchanged. These repairs resolve the scope issues identified above, so G1 to G8 are CONFIRMED for v2. They do not provide a full B2 YES or NO endpoint. Actual insertion remains a separate audit.
