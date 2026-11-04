# A fixed vortical component accumulating at a common flat point

## 1. Statement, notation and dependencies

Fix 2/5<c<1/2 and any finite real omega. Set Jx=e3 cross x, A=cI-omega J, X(x)=Ax, L=(1-c)I+omega J, a=1-2c, b=2(1-c), q=b/a>6 and p=(1-c)/c. On an open neighborhood G of x0!=0 let V,P be smooth. Put W=curl V, M=DV, E=sym M, T=curl W, k=X.V and S=P-|V|²/2. Assume

    div V=0, V.W=0, X.grad V=-LV,
    -Delta P=tr(M²), grad k=X cross W-aV,
    X.grad S=-bS, W.grad S=0,
    k grad S=qS grad k on supp W.                       (1)

Let C be one component of {W!=0,k!=0}, with x0 in its closure and with V,S infinitely flat at x0. The rank relation gives S=D|k|^q on C for one finite D. After shrinking G near x0, every nonflat boundary point of C has either k=0,W!=0, or W=0,V!=0,T!=0. In the latter case W has a nonzero first jet. Points with V=W=0 are common flat. More detailed conclusions are proved below. They do not exclude such accumulation.

The interface dichotomy used below is A1519-A1522, proved in the team records: at a contact with the boundary of int{W=0}, either V,k are nonzero, D<0 and |D||k|^(q-2)>=3(1-c)/(2|X|²), or V,S are common flat. That proof, including the no-cone projection argument, was reread. The pressure identity and component access estimates in A1471-A1479 were also reread.

There is a crucial scope correction to the submitted question. A1471 proves curl(V/k)=0 and a potential on simply connected patches. It expressly does not prove a potential on an arbitrary whole component. Global exactness is an extra assumption wherever a loop integral is used below. The actual-profile status of that extra assumption remains unproved here.

## 2. Pressure identity and order lemma

Divergence freedom gives Delta V=-T. Therefore

    Delta S=-2|E|²+V.T.                                 (2)

Indeed Delta(|V|²/2)=|M|²-V.T, and tr(M²)+|M|²=2|E|². If z is in closure C and k(z)=0, all derivatives of S of order at most six vanish at z: the globally C6 function D|k|^q agrees with S on C and has these zero derivatives at k=0. Derivatives of the difference vanish on C and hence at its closure.

Here is an order lemma independent of the rank and homogeneity conditions. Suppose div V=0 and -Delta P=tr((DV)²) near z, the first nonzero velocity polynomial V_m at z has degree m>=1, and S=P-|V|²/2 has zero jets through degree 2m. Then m=1 and V_1(n).n=0 for all unit n.

To prove it, set K(r)=average |V(z+rn)|², N(r)=average (V(z+rn).n)² and H(r)=average P(z+rn)+N(r). The double-divergence-free stress V tensor V+PI gives

    integral_Br (|V|²+3P)
       =r integral_dBr ((V.n)²+P),
    r H'(r)=K(r)-3N(r).                                 (3)

The compactly supported test (r²-|x-z|²)_+/2 is Lipschitz, not C1 as written in the submission. Formula (3) follows either by smooth approximation, including its boundary Hessian measure, or by two integrations by parts on the ball, where the polynomial test is smooth and vanishes on the boundary. This repairs the regularity description without changing the identity.

Write K0=average |V_m(n)|²>0 and N0=average (V_m(n).n)²>=0. Since P has leading term |V_m|²/2, the coefficients of r^(2m) in (3) give

    2m(K0/2+N0)=K0-3N0,
    (m-1)K0+(2m+3)N0=0.                                (4)

Thus m=1,N0=0. Continuity makes the normal component zero at every n. No nondegeneracy along a selected direction is needed.

## 3. Smooth irrational powers at arbitrary boundaries

Let B be open in U, with its relative boundary in {f=g=0}. Suppose f,g are smooth, f has one strict sign on B, and g=D|f|^lambda there, where D!=0 and lambda>0 is irrational. Then f and g are infinitely flat at every relative boundary point.

If f were not flat at z, some directional derivative partial_e^n f(z) would be nonzero. It remains nonzero on a small cylinder about z. On any line parallel to e, an interior endpoint of a B interval is a zero of f of some finite order m<=n. Taylor expansion on its B side makes g have nonzero leading order m lambda, which is nonintegral, contradicting smoothness. Hence a line that meets B occupies the full cylinder interval of that line. Lines through B approaching z give, by continuity, g=D|f|^lambda on the entire central interval through z. There f again has a finite-order zero, giving the same contradiction. Applying the argument with f and g interchanged and exponent 1/lambda proves that g is flat as well. This proof requires no cone, thickness or regularity of the boundary.

## 4. Boundaries with zero vorticity

Shrink the neighborhood so that

    |D||k|^(q-2)<3(1-c)/(2|X|²).                         (5)

This is possible because D is fixed, k(x0)=0 and X has no zero near x0. The interface dichotomy excludes every nonflat contact with boundary int{W=0} there.

Now suppose z in boundary C has W(z)=0 but z is not in closure int{W=0}. On a neighborhood U of z, W!=0 is dense, so supp W contains U. On {k!=0} in U the rank law makes S/|k|^q locally constant, even across lower-dimensional zeros of W. If k(z)!=0, this constant is D throughout a smaller neighborhood.

If V(z)=0, then k(z)=0. Equation (2) and the vanishing second jets of S imply E(z)=0. Since W(z)=0, M(z) is symmetric, hence M(z)=0. Let epsilon be the sign of k on C and put B={epsilon k>0,S/|k|^q=D} in U. This set is open, contains C intersect U and has relative boundary in {k=S=0}. If D=0, S is flat at z by smoothness from B. If D!=0 and q is irrational, Section 3 makes k,S flat. If q=r/s is rational in lowest terms, the identity

    S^s=D^s epsilon^r k^r

on B holds to every Taylor order at z. Thus if k has finite order ell, S has order q ell; if k is flat, S is flat. If V had finite order m, then m>=2 because M(z)=0, and ell>=m, giving order(S)>2m. Equation (4) is a contradiction. Therefore V is flat. Then k is flat and the same alternatives make S flat. W and all its jets are also flat.

If V(z)!=0, put d=(D|k|^q)' and e=(D|k|^q)'' at k(z), using the limiting derivatives from C when k(z)=0. Since M is symmetric trace free and MX=-LV, (2) gives

    (V+dX).T=2|M|²+e a²|V|².                            (6)

Here Delta k=-X.T at W=0. For a symmetric trace-free matrix,

    |M|² >= (3/2)|MX|²/|X|²,
    |LV| >= (1-c)|V|,
    q(q-1)a²=2(1-c).

Combining these inequalities with (5) makes the right side of (6) strictly positive. Hence T(z)!=0. In particular DW(z)!=0, so W has a first-order zero. If also k(z)=0, grad k=-aV!=0, and the two local constants satisfy D+=D-=0 for nonintegral q, or D-=(-1)^q D+ for integral q. This follows from smoothness across the regular coordinate k=0. These conclusions prove the stated boundary classification.

## 5. Vortical nodes with nonzero velocity

Suppose k(z)=0 and V(z),W(z) are nonzero. The form alpha=V.dx is nonzero and alpha wedge d alpha=0 by helicity zero. Frobenius gives alpha=h df with h>0. Since W=grad h cross grad f is nonzero, h,f are independent coordinates. The identity Lie_X alpha=-a alpha gives

    Xf=F(f), Xh=-(a+F'(f))h, k=hF(f).

Because W.grad S=0, S is a function of h,f. Where F!=0 the rank law gives h S_h=qS. On the interior of {F=0}, also F'=0, and X.grad S=-bS gives the same equation. Continuity supplies it on the remaining zero points. Thus, including the edge cases not checked in the submitted derivation,

    S=h^q G(f), F G'=qF'G.                              (7)

At f=f0 with F(f0)=0, grad k=F'(f0)V. If F has finite order m and D!=0 on the component side, smoothness of G=D|F|^q implies mq is an integer. Matching to the other side gives D-=(-1)^(mq)D+, with the side constants indexed by f-f0. If F is flat, k is flat; smoothness and the component sequence make every one-dimensional G jet zero, hence S is flat as well. V,W need not be flat in this case.

## 6. Vortical nodes with zero velocity

Suppose k(z)=V(z)=0 and W(z)!=0. Equations (2) and the zero second jets of S give E(z)=0, hence M(z)=(1/2)W(z) cross. Homogeneity MX=-LV gives W(z) parallel to X(z), and grad k(z)=0.

In a flow box of W, alpha and k descend to a transverse disk: alpha(W)=0, i_W d alpha=0 and W.grad k=0. Denote the descended form by eta; its exterior derivative is a nonzero area form. The identity grad k cross V=kW becomes

    dk wedge eta=k d eta.

Define Z by i_Z d eta=eta. Then Zk=k. On a Euclidean transverse disk at z, eta(z)=0 and its first derivative is the skew form from M, so DZ(z)=I/2. The backward flow of Z stays in a small disk and converges exponentially to z, with |z(t)-z|<=C exp(lambda t), t<=0, for some lambda>0.

If k were flat, k(z(t))=exp(t)k(y) together with arbitrarily high power estimates would force k(y)=0 for every sufficiently near y. This contradicts z in closure C. Comparing lowest Taylor degrees in Zk=k therefore shows that k has exactly degree 2. This argument imposes no global exactness hypothesis.

On C, ZS=qS. If D=0, S is zero on C and every jet at z is zero. If D!=0, backward Z-orbits starting in C preserve k!=0 and remain in that component. Flatness of S would contradict S(z(t))=exp(qt)S(y) by choosing a power N with N lambda>q. Hence S has finite order n. All jets of ZS-qS at z vanish because this smooth expression vanishes on the open set C. Its leading term is (n/2-q)S_n, so n=2q, which must be an integer. These degree conclusions hold under (1) alone.

## 7. The loop conclusion requires a global potential

If V.dx/k is exact on the whole relevant component, the quadratic form Q of k in Section 6 cannot be definite. Indeed a sufficiently small punctured transverse disk then lies in C. With eta=(Omega0/2)(-y dx+x dy)+O(r²) and k=r²Q(theta)+O(r³), its circle integral tends to

    (Omega0/2) integral_0^(2pi) 1/Q(theta) dtheta !=0,

contradicting exactness. This proves only nondefiniteness; a nonzero rank-one semidefinite Q is not excluded.

The global exactness premise is not A1471. A concrete counterexample to deriving it from the listed local identities is the swirl in Section 9(a), on a full annular cylindrical neighborhood. There V.dx/k=-(1/omega)dtheta, with period -2pi/omega. It satisfies all local equations but has only local potentials.

The quotient identities alone permit even a definite quadratic form: take eta=(Omega0/2)(-y dx+x dy), k=x²+y². Then dk wedge eta=k d eta and Z=(x partial_x+y partial_y)/2, while eta/k has the nonzero circle period. A semidefinite form is also allowed by those identities: take k=x², for which eta/k=(Omega0/2)d(y/x) on each half-plane. If desired both examples satisfy Lie_Y eta=-a eta and eta(Y)=k with Y=-(a/2)(x partial_x+y partial_y)+(2/Omega0)k r^-2(-y partial_x+x partial_y) in the definite case, or Y=-(a/2)(x partial_x+y partial_y)+(2/Omega0)x partial_y in the rank-one case; the definite expression simplifies to a linear field. These are quotient tests, not full Euclidean Euler tails. Nondefiniteness under (1) without an extra zero-period input remains OPEN. The earlier stronger word 'indefinite' is also unsupported.

## 8. Conditional exclusion from complementary sphere means

On C, |S|<=|D||X|^q |V|^q. Hence for every epsilon>0, after shrinking,

    P>=(1/2-epsilon)|V|² on C.

Suppose for some delta>0 and epsilon>0 with delta+epsilon<1/2, all sufficiently small spheres about x0 satisfy

    average (1_(C complement) S_-)
        <=(1/2-delta-epsilon) average |V|².              (8)

Then average P>=delta K, H=average P+N>=delta K>=0, and (3) gives rH'<=K<=H/delta. Therefore r^(-1/delta)H is nonincreasing. Common flatness makes its limit at zero equal to zero; nonnegativity then forces H=K=0 at every small radius. Thus V vanishes on a neighborhood, contradicting x0 in closure C. The equivalent formulation with a bound (1/2-delta0)K for some delta0>0 follows by taking epsilon<delta0 and replacing delta by delta0-epsilon.

Condition (8) has not been derived from (1). A bound only on the negative pressure off C does not by itself give the needed positive sphere mean without control of the fraction of velocity energy on C. This is an algebraic limitation of this estimate, not a counterexample proving that no other Euler argument can use such a bound. Nor is it proved that every possible exclusion must proceed by controlling these means.

## 9. Model checks and exact limits

(a) For omega!=0, V=A0 rho^-p e_theta, P=-A0² rho^-2p/(2p) is divergence free, helicity free and stationary Euler away from the axis. Its linear similarity part vanishes for every c and omega. Direct cylindrical differentiation gives

    k=-omega A0 rho^(1-p),
    S=-(p+1)A0² rho^-2p/(2p),
    q(p-1)=2p,
    D=-(p+1)|A0|^(2-q)/(2p |omega|^q).

Thus D tends to minus infinity while the field and its derivatives tend to zero with A0 on fixed compact sets. The Poisson equation is satisfied. This is a family of local solutions, not an accumulation of components inside one actual profile, and there is no common flat point. On an annular component its nonzero potential period is the exact obstruction in Section 7.

(b) In cylindrical coordinates near x0=(1,0,0), put beta=omega/c, u=theta+beta log rho and h(u)=exp(-1/u²) for u>0, zero otherwise. Let F=rho^-p h(u), V=F e3, P=F²/2, S=0 and k=c x3 F. Then X u=0 and XF=-(1-c)F. Direct differentiation gives

    div V=0, W=(F_y,-F_x,0), V.W=0,
    grad k=X cross W-aV, (DV)²=0.

All scalar homogeneity, vorticity transport and rank identities in (1) hold. On a small positive-u patch, W!=0 because h'>0. The component {u>0,x3>0} has D=0, and x0 is common flat. Points (cos u_j,sin u_j,0), u_j decreasing to zero, have k=0 and V,W nonzero, so they are accumulating nonflat boundary points. On C a potential is phi=(1/c)log x3. Poisson would require Delta F²=0, which fails: a nonnegative harmonic F² with a zero would vanish locally. Thus this is an exact countermodel only after deleting Poisson, and cannot be an actual tail.

(c) Replace h² by g(u)=exp(gamma u)cos(nu u) on a sector where it is positive, with gamma=2p beta/(1+beta²), nu=2p/(1+beta²). Then

    Delta(rho^-2p g(u))
       =rho^(-2p-2)[(1+beta²)g''-4p beta g'+4p²g]=0.

All listed identities, including Poisson, now hold. There is a regular k=0 boundary at x3=0, but no velocity zero and no common flat point. This construction need not satisfy the full stationary momentum equation and is not claimed to arise from an actual profile.

## 10. Verdict

The order lemma, irrational-power lemma, boundary classification, completed Frobenius calculation, exact orders at a vortical velocity zero, conditional mean criterion and models are confirmed at the precise scopes above. The question's attribution of a globally exact component potential to A1471 is refuted. The nondefinite quadratic conclusion is confirmed only with that additional zero-period hypothesis; without it the conclusion remains OPEN, as does the stronger indefinite claim. No actual common-flat tail satisfying all hypotheses or exclusion of every such tail has been obtained.

The complete submitted note and its question were read, and both are pinned with real capture time and hashes. No numerical or symbolic computation was used. Continued file exchange with the configured model coordinator supplies the model comparison; runtime provider identity remains unattested and no new model client was launched.
