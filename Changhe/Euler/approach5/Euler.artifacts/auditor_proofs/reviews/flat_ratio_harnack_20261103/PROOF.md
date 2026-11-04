# Pressure-ratio flux, Harnack exclusion and the period at a common flat orbit

## 1. Local class and exact statement

Let0<c<1/2, omega be any finite real number, Jx=(-x2,x1,0), X=(cI-omega J)x, q=2(1-c)/(1-2c)>2 and eta=1/q<1/2. Let x0!=0 and let Gamma be a short embedded orbit of X through x0. Work in a sufficiently small tubular flowbox B around that orbit; rho denotes the Euclidean distance to Gamma. Let V,P2 be smooth fields satisfying the local tail identities, including

    div V=0, W=curl V, -Delta P2=tr((DV)^2),
    k=X.V=0, S=P2-|V|²/2,
    curl(H^(-eta)V)=0 wherever S!=0, H=|S|.

The last identity is the already proved local normal form on the open-k-zero region; equivalently W=(eta/H)grad H cross V. It is a hypothesis of the local result here, so no global Euler momentum law is silently assigned to V.

Assume V and S are infinitely flat at x0, S<0 on B minus Gamma, and S=0 on Gamma. Put R=|V|²/H. For some delta in(0,1) and finite M, suppose rho|grad R|<=M and either

    0<=R<=1-delta,
    or 1/(1-eta)+delta<=R<=M.

Such a configuration is impossible. In particular it cannot be the neighbourhood of a supported common-flat point of an actual tail. The submitted target range2/5<c<1/2 is covered; the local proof works on the larger displayed c range. Constants depend on the fixed flowbox, q, delta and M, never on rho. This is a ratio-conditional statement only.

## 2. Exact pressure flux for both signs

On a connected open sign component of S put sigma=sign S and E=|V|²=RH. The elementary vector identity gives

    (V.grad)V=grad E/2-V cross W,
    tr((DV)^2)=Delta E/2-div(V cross W).

Since P2=sigma H+E/2, Poisson yields Delta(E+sigma H)=div(V cross W). The normal form gives

    V cross W=(eta/H)(E I-V tensor V)grad H.

Expanding grad E=R grad H+H grad R therefore proves

    div(M_R grad H+H grad R)=0,
    M_R=((1-eta)R+sigma)I+eta(V tensor V)/H.             (1)

No derivative estimate, sign of helicity beyond the normal-form premise, or original-profile momentum equation enters this calculation. At V=0 the tensor quotient is zero because H>0.

## 3. Uniform ellipticity in the stated ratio ranges

When V!=0, M_R has eigenvalue R+sigma along V and (1-eta)R+sigma in its orthogonal plane. The same conclusions hold by continuity at V=0. For sigma=+1 it is positive definite for every R>=0, and uniformly so with a finite upper ratio bound. For sigma=-1, it is negative definite when R<1 and positive definite when R>1/(1-eta).

In the first range of Section1 set A=-M_R and b=-grad R. Its eigenvalues lie between delta and1. In the second set A=M_R and b=grad R. Its smallest eigenvalue is at least(1-eta)delta and its largest is bounded in terms of M. Thus in either range

    div(A grad H+bH)=0,
    alpha I<=A<=Lambda I, |b|<=M/rho,                 (2)

with positive fixed alpha and finite Lambda. In the omitted interval1<=R<=1/(1-eta), the principal matrix is degenerate or has mixed signs; no positive ellipticity argument is available from(1).

## 4. Scaling and the exact symmetric lift

Take a ball of radius epsilon r at distance comparable to r from Gamma. Under x=xstar+r z, equation(2) becomes div_z(A_r grad_z u+b_r u)=0 with u(z)=H(xstar+r z), A_r=A(xstar+r z) and b_r=r b(xstar+r z). On a fixed scaled ball, |b_r|<=B0 independently of r, while the ellipticity constants are unchanged.

For |t|<1 define

    u_tilde(z,t)=exp(t)u(z),
    C(z,t)=exp(-t) [[A_r(z), b_r(z)], [b_r(z)^T, D]],
    D=1+2B0²/alpha.

The four-dimensional flux is exactly

    C grad u_tilde=(A_r grad u+b_r u, b_r.grad u+D u).

It is independent of t, so div_(z,t)(C grad u_tilde)=0. For vectors xi and scalars s, Young's inequality gives

    xi.A_r xi+2s b_r.xi+D s² >=(alpha/2)|xi|²+s².

The factor exp(-t) and all entries are bounded above and below on the fixed t interval. The lifted equation therefore has symmetric bounded uniformly elliptic coefficients. Its positive solution is in W1,2 on every compact scaled ball. No bound on derivatives or divergence of b is needed.

## 5. Harnack chain contradicts infinite flatness

The only external analytic input is interior Harnack for nonnegative weak solutions of a homogeneous uniformly elliptic symmetric divergence-form equation with bounded measurable coefficients. Precisely, sup on an inner ball is at most a constant times inf there if the concentric fourfold ball lies in the domain; the constant depends only on dimension, ellipticity and the fixed radius ratio. This is Theorem4, page6, of the Princeton-hosted notes "Boundedness, Harnack inequality and Holder continuity for weak solutions". Its assumptions and preceding pure-equation argument on pages1-6 were read and the PDF is pinned. Only the pure divergence-form case in dimension4 is used.

Fix a unit normal n to Gamma at x0 and let x_r=x0+r n for small r. Tubular coordinates make rho(x_r)=r. A fixed number of balls of radius epsilon r at distances comparable to r join x_r to x_(r/2) in the punctured flowbox. Apply the scaled lifted Harnack inequality on that chain at t=0. The number of balls and their ellipticity constants are independent of r. Thus for one C0>=1,

    H(x_(r/2))>=C0^(-1)H(x_r)>0.

Iterating from a fixed r0 gives H(x_(2^(-j)r0))>=H(x_r0)C0^(-j). Put N0=log(C0)/log2. Smooth infinite flatness of S at x0 gives H(x_r)<=C_N r^N for every integer N. Choosing N>N0 contradicts the preceding positive lower bound as j tends to infinity. This proves the claimed impossibility. No flow completeness, global boundary integral or pressure normalization at infinity is used by this local argument.

## 6. Constant ratio and removable orbit

For a constant ratio R=lambda in either elliptic range, b=0. If H is smooth, nonnegative, zero on Gamma and positive off it, then grad H=0 on Gamma and |grad H|=O(rho) locally. The bounded flux A grad H across a tube of radius epsilon has integral O(epsilon²), since a compact tube segment has area O(epsilon). Testing away from the tube and letting epsilon tend to zero shows div(A grad H)=0 weakly across Gamma. Extend A by any bounded elliptic value on the measure-zero curve.

Interior Harnack in a ball meeting Gamma now forces H=0 there because H(x0)=0. Thus in the constant-ratio elliptic ranges, infinite-order flatness is not needed: nonnegative smooth H vanishing on the orbit already contradicts strict positivity off it. This verifies the source's weak-extension remark and states its stronger consequence precisely.

## 7. The potential is single-valued on the punctured flowbox

Let alpha=H^(-eta)V.dx, a smooth closed one-form on B minus Gamma. This punctured tubular flowbox retracts to a transverse circle, so its first homology is generated by any small circle gamma_r in a transverse disk. Stokes on the annulus between two such circles makes the period P=int_gamma_r alpha independent of r.

If R<=M and H->0 at x0, then on that circle

    |P|<=C r (sup_gamma_r R)^(1/2)
                 (sup_gamma_r H)^(1/2-eta) ->0.

Here the Euclidean circle has length2pi r; a smooth equivalent transverse coordinate changes only C. Because eta<1/2, the limit holds. Therefore P=0. Every closed loop has zero integral and path integration defines one single-valued potential phi with dphi=alpha. No assertion is made for arbitrary multiply punctured sign domains or for domains cut by additional zeros of S.

## 8. Stronger period consequence under a polynomial ratio bound

When H is infinitely flat at x0, boundedness of R can be weakened to any fixed polynomial bound R<=C rho^(-m), m finite, on the punctured flowbox. Indeed, the circle estimate in Section7 becomes

    |P|<=C r^(1-m/2)(sup_gamma_r H)^(1/2-eta).

Since1/2-eta>0, flatness makes the last factor smaller than every prescribed positive power of r. The period is again zero. Conversely, a nonzero period would force

    sup_gamma_r R >= |P|² / [C² r²(sup_gamma_r H)^(1-2eta)].       (3)

As r tends to zero this lower bound grows faster than every inverse power of r. This exact necessary growth statement does not bound R in an actual profile and does not resolve the common-flat branch.

## 9. Scope and comparison with the earlier pressure lemma

The proof of Sections2-8 only needs0<eta<1/2, hence every0<c<1/2 and every finite omega. The source's target interval is not an analytic restriction here. S>0 off the orbit is already ruled out at a supported common flat point by the confirmed local pressure-deficit lemma; the new useful Harnack ranges have S<0. The source's description of a "new" ratio range below2 must not be read as a proof throughout that range without rho|grad R| bounded.

Uncovered cases include ratios in the degenerate interval, unbounded ratios, uncontrolled ratio derivatives and sign-changing S with accumulating nodal components. Formula(3) is only a necessary condition for nonzero period. An example satisfying scalar transport alone with nodal circles is not a solution of the full local tail system.

## 10. Verification and model collaboration

The full four-section configured coordinator source was read, pinned and independently reconstructed. The tensor algebra, sign ranges, scaling, four-dimensional lift, tube flux and period calculation were checked by hand. The primary Harnack notes were fetched and read at the indicated scope; the original Moser1961 publisher page was unavailable and is not claimed read. No symbolic test was needed or rerun.

The configured model coordinator's explicit hand check is the received collaboration; runtime is unattested and its nested source reports that its requested second-model consultation did not run. The all-c scope, constant-ratio consequence and polynomial-period extension are returned for further comparison through the existing agents. No new agent or model client was used.
