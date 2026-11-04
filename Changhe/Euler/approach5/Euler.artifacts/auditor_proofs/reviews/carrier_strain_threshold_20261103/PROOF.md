# Carrier identity and the local strain threshold

## 1. Exact theorem and hypotheses

Let 0<c<1/2 and omega be real. On Euclidean R3 put Jx=e3 cross x, A=cI-omega J, X(x)=Ax, L=(1-c)I+omega J, a=1-2c, b=2(1-c) and eta=a/b. Thus b-a=1 and 1/eta-1=1/a. Let x0!=0 and let G be a smooth X-flowbox about a central orbit segment Gamma through x0. Suppose V,S are smooth on G and satisfy

    div V=0, W=curl V, k=X dot V=0,
    (X dot grad)V=-LV, X dot grad S=-bS,
    grad k=X cross W-aV, W dot grad S=0,
    P=S+|V|^2/2, -Delta P=tr((DV)^2).

Assume S<0 on G minus Gamma, S=0 on Gamma, and V,S vanish to infinite order at x0. Matrix norms are Frobenius norms. For every mu>=0 satisfying

    2 mu a^2<1,

each neighborhood of x0 contains a point at which |sym DV|^2>mu|W|^2. Equivalently, for every kappa>sqrt(2)a, each neighborhood contains |W|<kappa|sym DV|.

This is the precise local setting of C60-C61. The proof uses all the displayed structural equations, a single central pressure zero orbit and infinite-order flatness. No global profile conclusion, arbitrary-zero-set conclusion or endpoint assertion is included. The complete four-section C62 source and complete eight-section earlier C61 audit were read. Their pinned copies are listed in the team records. No source numerical checker is used or executed.

## 2. The carrier identity and trace-free matrix estimate

Write D=DV and M=(D+D^T)/2. Since grad(X dot V)=A^T V+D^T X=0 and DX=-LV,

    2MX=-(L+A^T)V=-(I+2omega J)V,
    X dot MV=-|V|^2/2.                                      (1)

The second equality uses V dot JV=0. Also tr M=0 and X dot V=0.

For a symmetric trace-free matrix M and arbitrary real vectors p,q, define

    N=(p q^T+q p^T)/2-(p dot q)I/3.

Then p dot Mq=<M,N> and

    |N|^2=|p|^2|q|^2/2+(p dot q)^2/6.

Cauchy-Schwarz therefore gives the absolute-value bound

    |p dot Mq| <= |M| sqrt(|p|^2|q|^2/2+(p dot q)^2/6).       (2)

Applying (2) to p=-X,q=V and using (1) shows sqrt(2)|M||X|>=|V|. In particular a nonzero V has nonzero strain, without using the strain-ratio hypothesis.

Put E=|V|^2, H=-S, and u=grad log H off Gamma. The scalar transports give XE=-bE, XH=-bH and u dot X=-b. From X cross W=aV, W dot grad H=0 and X dot grad H=-bH, the vector triple-product identity gives

    W=eta u cross V.

Since D^T=M-(W cross)/2, it follows that

    grad E=2MV+eta(Eu-(u dot V)V),
    |W|^2=eta^2(E|u|^2-(u dot V)^2).                         (3)

Every division here is by H, which is strictly positive off Gamma. No division by E has yet been made.

## 3. Positivity before logarithms

Assume for contradiction that |M|^2<=mu|W|^2 on a neighborhood of x0 with 2mu a^2<1. If mu=0, enlarge it slightly while preserving the strict inequality. Henceforth mu>0.

Choose the plane through x0 normal to n0=X(x0)/|X(x0)|. Since det A=c(c^2+omega^2)>0, X(x0)!=0. A small transverse disc and the map Phi(sigma,t)=exp(tA)sigma give a flowbox inside the neighborhood on which the strain assumption holds. The disc meets Gamma only at its center. Its punctured part D' is connected.

Equation (3) and the strain assumption imply

    |grad E| <= eta(1+2sqrt(mu)) |u| E.                      (4)

The constant is finite, even though it need not be less than one. Along any compact piecewise smooth path in D', |u| is bounded. Gronwall in both directions shows that E is either positive throughout D' or identically zero there.

In the latter case transport gives V=0 on the punctured flowbox and continuity gives V=0 on its central orbit. The Poisson equation reduces to Delta S=0 on the entire smaller flowbox. A harmonic function with all derivatives zero at an interior point is identically zero in a connected neighborhood, contrary to S<0 off Gamma. Thus E>0 on D' and throughout its smaller flowbox. The gradients e=grad log E and w=grad log(E/H)=e-u are now defined, with

    e dot X=u dot X=-b, w dot X=0.

## 4. Directional logarithmic estimates

Let t=(u dot V)/(|u||V|), so -1<=t<=1. Equation (3), followed by (2) and the exact expression for |W|, gives

    e dot u <= eta |u|^2 f(t^2),
    f(s)=1-s+2sqrt(mu) sqrt((1-s)(1/2+s/6)).

For 0<=s<=1, the product under the square root has derivative -(1+s)/3. Both terms in f are decreasing, so f(s)<=f(0)=1+sqrt(2mu). Define

    theta=eta(1+sqrt(2mu)), theta1=a sqrt(2mu).

The strict hypothesis says theta1<1. Since b=a+1, it also gives theta<1. Both constants are positive.

Using (1), then (2), and then the strain bound gives

    E/2 <= |M||X||V|/sqrt(2)
         <= sqrt(mu) eta |u||X| E/sqrt(2).

After cancellation and multiplication by b/|X|, the two needed estimates are

    e dot u <= theta |u|^2,
    b/|X| <= theta1 |u|.                                    (5)

The second estimate uses the carrier identity and is the extra information beyond the matrix-gradient bound of LIT294. No upper bound for |e| with constant less than one is required.

## 5. Oblique projection and a bounded-ratio sequence

Let n be a unit vector with epsilon=|n-X/|X|| satisfying

    epsilon<=min(1/2,(1-theta1^2)/(6theta1)).

Set beta=b/|X|, nu=(1-epsilon^2/2)^(-1), and

    Z=u-[(u dot n)/(X dot n)]X.

Then X dot n>0, Z dot n=0, and direct expansion gives

    u dot Z=|u|^2-nu beta^2+nu beta u dot(n-X/|X|).

Because beta<=theta1|u|, 1<=nu<=1+epsilon^2<=2 and epsilon theta1<=1, this implies

    (1-theta1^2)|u|^2/2 <= u dot Z <= 2|u|^2.

The lower error is at most epsilon^2 theta1^2+2epsilon theta1<=3epsilon theta1. Since w dot X=0, (5) gives w dot Z=w dot u<=(theta-1)|u|^2. With gamma=(1-theta)/4>0, we obtain

    (w+gamma u) dot Z <= -(1-theta)|u|^2/2.                  (6)

We also need a sequence with R=E/H bounded. Here is the pressure argument including its center boundary term. If liminf R>2 off Gamma at x0, shrink the ball to have R>=R0>2. The symmetric tensor

    T=V tensor V+P I

satisfies div div T=0 by incompressibility and the Poisson equation. Also

    (1/2-1/R0)E I <= T <= (3/2)E I.

These inequalities extend across Gamma since V=P=0 there by transport. The tensor is smooth and infinitely flat at x0.

For a positive tensor with alpha E I<=T<=beta0 E I, integrate n dot T(rn)n over the unit sphere centered at x0 to obtain A0(r), and integrate tr T-n dot Tn to obtain B0(r). The integrated radial divergence identity is

    A0'(r)=[B0(r)-2A0(r)]/r.

The omitted flux is zero: div div T=0 makes the flux of div T constant, and bounded div T makes its flux at a vanishing sphere tend to zero. The tensor comparison gives B0<=2(beta0/alpha)A0, hence A0'<=K A0/r with K=2(beta0/alpha-1). Integrating backwards gives A0(r)>=(r/r1)^K A0(r1). Infinite-order flatness forces A0(r1)=0 for every small r1, and positivity forces E=P=S=0. This contradicts the pressure sign. Thus liminf R<=2.

There are points y_j off Gamma tending to x0 with R(y_j)<3. Pull them back through the same flowbox to sigma_j in D'. Transport makes R invariant under X, so R(sigma_j)<3, sigma_j tends to x0 and H(sigma_j) tends to zero.

## 6. Compact flow continuation and contradiction

Shrink the transverse disc so that its fixed normal n0 satisfies the epsilon bound throughout. The projection Z in Section5 is then a smooth vector field tangent to D'. Let Xmax bound |X| on the surrounding closed ball. Since |u|>=b/|X|,

    Z(log H) >= (1-theta1^2)b^2/(2Xmax^2)>0,
    Z(log R+gamma log H)<=0.                                (7)

Choose a fixed smaller circle C around x0 in the transverse disc. For large j the initial point sigma_j is inside it. Along its forward Z-trajectory, H increases and is at least H(sigma_j)>0, so the trajectory cannot approach the puncture. If it never reaches C, it stays in the compact subset inside C where H>=H(sigma_j). This is contained in the smooth vector field's domain, giving continuation for all positive time. The positive uniform rate in (7) then contradicts the boundedness of log H on that compact set. Therefore the trajectory reaches C at some z_j.

For F=log R+gamma log H, (7) gives

    F(z_j)<=log 3+gamma log H(sigma_j),

which tends to minus infinity. On C both H and E are positive and F is continuous, so F has a finite lower bound there. This contradiction proves the theorem. Completeness on the punctured domain was never assumed; each trajectory was continued only on its own compact subset.

## 7. Constants, comparison and the pointwise method limit

For mu=1/2 the strict condition is a^2<1, valid for all 0<c<1/2. Thus tr((DV)^2)=|M|^2-|W|^2/2 is positive arbitrarily close to x0. For 2/5<c<1/2, a<1/5 and mu=25/2 is admissible. For any kappa0>0, the kappa form holds for c>max(0,1/2-kappa0/2^(3/2)).

Write q=1/eta>2. The new threshold is mu<(q-1)^2/2. It exceeds C61's threshold by (q-2)^2/4. It agrees with LIT294 for q<=4; for q>=4 its improvement over LIT294 is (q-4)^2/8. These are comparisons of sufficient criteria.

The source's method limitation is also valid as a pointwise statement. At a fixed point choose an orthonormal basis e0=X/ell, e1=V, e2, where ell=|X|, |V|=1 and X dot V=0. Write j0=(JV) dot e0 and j2=(JV) dot e2. Take u=-(b/ell)e0+s e2 and choose the symmetric trace-free matrix M with entries

    M00=-omega j0/ell, M01=-1/(2ell), M02=-omega j2/ell,
    M11=0, M12=s/(2b), M22=omega j0/ell.

Set W=eta u cross V and D=M+(W cross)/2. Then MX=-(V+2omega JV)/2, DX=-LV and D^T X=-A^T V. Formula (3) gives e=2MV+eta u=u. Directly,

    |W|^2=a^2/ell^2+a^2 s^2/b^2,
    |M|^2=(1+4omega^2|JV|^2)/(2ell^2)+s^2/(2b^2).

Consequently |M|^2/|W|^2 tends to 1/(2a^2) as s tends to infinity. For any mu above that threshold, these algebraic data obey |M|^2<mu|W|^2 and w=e-u=0. No direction can then increase log H while decreasing log R+gamma log H for gamma>0. These are pointwise data, without a Poisson equation or a field extension; they are not counterexamples to a stronger theorem.

## 8. Scope and verification

The argument is analytic and uses no random sampling. The C62 source matrix identities, the trace-free estimate, both strict constants, positivity before logarithms, the center flux and every continuation step were checked independently. The proof also verifies the comparisons with the already confirmed C61 and LIT294 results.

The equality 2mu a^2=1, optimality among fields satisfying all the equations, common flat-point exclusion, nonnegative trace on a neighborhood, general pressure zero sets and the unrestricted profile conjecture remain open. Pressure is the specified P=S+E/2; no additive normalization is inserted.

Findings are exchanged with the existing configured model C and coordinator agents and the external referee (a second model) literature agent. Actual provider execution remains independently unattested.
