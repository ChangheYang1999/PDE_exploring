# Local reverse-ratio unique continuation

## 1. Exact claims and notation

Let 0<c<1/2, omega be any real number, Jx=e3 cross x, A=cI-omega J, X(x)=Ax, L=(1-c)I+omega J, a=1-2c, and b=2(1-c). For a smooth real vector field V use DV=(partial_j V_i), W=curl V, M=sym DV, and Frobenius matrix norms. Then tr((DV)^2)=|M|^2-|W|^2/2. Flatness at a point means that all derivatives vanish there, equivalently |V(x)|=O(|x-x0|^N) for every integer N.

**Local theorem.** Suppose x0 is nonzero, V is smooth on an open neighborhood U of x0, div V=0, X dot V=0, and (DV)X=-LV throughout U. Suppose V is flat at x0. If constants 0<=kappa<sqrt(2) and C0>=0 satisfy

    |W| <= kappa |M| + C0 |V| on U,

then V vanishes on a neighborhood of x0. The theorem is local and has no pressure, decay, energy, helicity or global-flow assumption.

For the carrier consequence define **F** as follows. G is a smooth X-flowbox about an orbit segment Gamma containing x0. V,S are smooth on G, satisfy div V=0, k=X dot V=0, (DV)X=-LV, X dot grad S=-bS, grad k=X cross W-aV, W dot grad S=0, P=S+|V|^2/2, and -Delta P=tr((DV)^2). Further S<0 on G minus Gamma, S=0 on Gamma, and V,S are flat at x0. In F the displayed ratio bound cannot hold on any neighborhood of x0. These are precisely local hypotheses, not a conclusion that the campaign's general decaying profiles satisfy F.

## 2. Reduction to a transverse first-order inequality

Since det A=c(c^2+omega^2)>0, X(x0) is nonzero. Translate x0 to 0 and apply a proper orthogonal change of coordinates O so X(0)=|X(x0)|e3. Divergence, curl, matrix norms, the two constraints and flatness transform correctly. L is conjugated by the same rotation. On a small closed ball X3>0. Set xi=(X1,X2)/X3, so xi(0)=0, and set Q to be the 3 by 2 matrix with first two rows I2 and last row -xi^T. On the transverse disc y3=0 put v=(V1,V2), B=Dv and S_B=sym B.

The constraint X dot V=0 gives V=Qv. The first two derivative columns are Q partial_j v+(partial_j Q)v. The transport constraint gives

    partial_3 V = -xi1 partial_1 V-xi2 partial_2 V-LQv/X3.

Consequently

    DV = Q B Q^T + K,
    K = [(partial_1 Q)v, (partial_2 Q)v,
         -(xi1 partial_1 Q+xi2 partial_2 Q)v-LQv/X3].

All coefficients of K are bounded on a smaller closed disc, hence |K|<=C1|v|. Since Q^T Q=I2+xi xi^T, taking traces and symmetric parts yields

    div v = -xi^T S_B xi-tr K,
    |M| <= (1+|xi|^2)|S_B|+|K|,
    W3 = partial_1 v2-partial_2 v1.

Let f=v1+i v2, with f_z=(partial_1 f-i partial_2 f)/2 and f_barz=(partial_1 f+i partial_2 f)/2. Direct expansion gives

    2 f_z = div v+i curl v,
    |S_B|^2 = 2|f_barz|^2+(div v)^2/2.

Shrink the disc so |xi|<=delta. Write s=|S_B| and phi=|f_barz|. The assumed bound on |W|, the preceding identities and |V|<=sqrt(1+delta^2)|v| give a finite constant C3 with

    |div v| <= delta^2 s+C3|v|,
    |curl v| <= kappa(1+delta^2)s+C3|v|,
    (1-delta^2/sqrt(2))s <= sqrt(2)phi+C3|v|/sqrt(2).

The Euclidean triangle inequality for the first two estimates now gives

    |f_z| <= k_delta |f_barz|+C4|f|,
    k_delta = sqrt(delta^4+kappa^2(1+delta^2)^2)
              /[sqrt(2)(1-delta^2/sqrt(2))].

As delta tends to zero, k_delta tends to kappa/sqrt(2)<1. Choose a positive delta for which the denominator is positive and k=k_delta<1. For g=conjugate(f) this is

    |g_barz| <= k |g_z|+C4|g|.                 (UC)

Every constant is local and finite. No uniform bound in omega is needed: for each real omega the same strict threshold sqrt(2) works after choosing the disc.

## 3. Why (UC) rules out a nonzero flat solution

Here are the classical inputs in the form used. For bounded measurable compactly supported mu with ||mu||infinity<1 and bounded compactly supported alpha, the equation s_barz-mu s_z=alpha has a continuous W^{1,p}_loc solution for some p>2. The homogeneous Beltrami equation has the representation h=F composed with chi, with F holomorphic and chi a quasiconformal homeomorphism whose inverse is locally Hölder. A primary source is B. V. Bojarski, *Generalized solutions of a system of differential equations of the first order and elliptic type with discontinuous coefficients*, Jyväskylä Report 118 (2009), the translation of the 1957 paper: Theorem 4.1, pp.31-32; Theorem 3.3, p.26; Theorem 3.1, pp.17-19. These precise passages were read from the retained PDF. The first result follows there from the Cauchy-transform derivative formulas and the invertibility of I-mu S on L^p for p close to 2, as in equation (3.7).

To apply them, choose measurable mu,alpha with |mu|<=k, |alpha|<=C4 and g_barz=mu g_z+alpha g. Where |g_barz|<=k|g_z|, set alpha=0 and mu=g_barz/g_z, taking mu=0 if g_z=0. On the remaining set g is nonzero by (UC); choose mu g_z to have the phase of g_barz and modulus k|g_z|, and set alpha=(g_barz-mu g_z)/g. If g_z=0, use mu=0. Extend both coefficients by zero off the disc. Let s solve the inhomogeneous equation and put h=e^{-s}g. The W^{1,p} product rule gives h_barz=mu h_z, so h=F composed with chi.

On a compact smaller disc e^{-s} is bounded. Therefore h(y)=O(|y|^N) for every N. With zeta0=chi(0), local Hölder continuity of chi^{-1} gives |chi^{-1}(zeta)|<=C|zeta-zeta0|^beta for some beta>0. Thus F(zeta)=O(|zeta-zeta0|^{beta N}) for every N. A nonzero holomorphic function has a finite vanishing order, which contradicts these estimates. Hence F, h, g and v vanish on a disc. This uses no claim that a composition of flat functions is smooth: only the quantitative upper bounds and the positive Hölder exponent are needed.

Finally the map (y1,y2,t) to exp(tA)(x0+O(y1,y2,0)) has invertible differential at 0, since its third derivative column is X(x0), transverse to the disc. It is a diffeomorphism from a smaller product onto a neighborhood. Along each of these short orbit segments,

    V(exp(tA)x) = exp(-tL)V(x).

Zero disc data therefore give V=0 on that neighborhood. This proves the local theorem. Only local characteristic existence is used.

## 4. Carrier consequence and all four corollaries

If the ratio bound held in F, the local theorem would give V=0 on a ball about x0. There P=S, DV=0, and the pressure equation says Delta S=0. Since S<=0 and S(x0)=0, the strong maximum principle gives S=0 on the ball. The ball contains points outside the smooth arc Gamma, where F requires S<0. This contradiction proves the carrier consequence. No pressure normalization is used; the stated value and sign of S are hypotheses.

It follows that every neighborhood of x0 contains a point with |W|>kappa|M| for every 0<=kappa<sqrt(2). Such a point has W nonzero. For 0<epsilon<1 choose kappa=sqrt(2(1-epsilon)); this gives

    tr((DV)^2) < epsilon |M|^2.

For epsilon>=1 use kappa=0. At those points the same conclusion follows from W nonzero.

Combining this with the separately audited C62 theorem, every neighborhood contains a point with |W|<kappa1|M| for any kappa1>sqrt(2)a and a point with |W|>kappa2|M| for any kappa2<sqrt(2). The points need not coincide. For negative kappa2 the second assertion follows already from a point with W nonzero. This is oscillation of relative size, not exclusion of a flat carrier.

There is also the stronger component version. In F, X cross W=aV. On a neighborhood with |X|>=m>0,

    |W| <= |W dot X|/|X|+a|V|/|X|.

If |W dot X|<=kappa|X||M|+C0|V| held there, then |W|<=kappa|M|+(C0+a)|V|/m, contradicting the carrier consequence. Thus each neighborhood contains a point with

    |W dot X| > kappa |X| |M|+C0 |V|.

All statements hold for every fixed real omega and every 0<c<1/2. Only this last corollary uses X cross W=aV; the local theorem does not.

## 5. Endpoint, necessity of flatness and unresolved scope

At kappa=sqrt(2), k_delta>1 for delta>0 and the elliptic argument stops. This is a real limitation of the planar inequality. Put rho(t)=exp(-1/t^2) for t nonzero and rho(0)=0, F(t)=integral_0^t rho(s) ds, and v(y1,y2)=(F(y2),F(y1)). Repeated differentiation of rho gives a polynomial in 1/t times exp(-1/t^2), so every derivative tends to zero at 0. The same is true for derivatives of F. F(t) has the sign of t and is zero only at 0, so v is smooth, flat at 0 and nonzero at every other point. Direct differentiation gives

    div v=0, curl v=rho(y1)-rho(y2),
    |sym Dv|^2=(rho(y1)+rho(y2))^2/2,
    tr((Dv)^2)=2rho(y1)rho(y2)>=0.

Thus |curl v|<=sqrt(2)|sym Dv|. This is a planar counterexample to endpoint unique continuation for the reduced inequality. It is not a field in F and does not establish compatibility of tr((DV)^2)>=0 with F.

Flatness cannot simply be omitted: the nonzero local fields in C63 satisfy the carrier linear constraints and |W|/|M|=sqrt(2)a/sqrt(1+4omega^2)<sqrt(2). Their lack of a common flat zero is essential.

The existence or exclusion of a full carrier in F, the endpoint reverse bound, extensions beyond the strict threshold, and the unrestricted smooth decaying rotating-profile conjecture remain OPEN. C62's opposite endpoint also remains OPEN. There is no new global nonexistence result here.

## 6. Evidence and verdict scope

The complete C64 source, both source check scripts and their current logs were read. The planar script uses high precision residual evaluation at finitely many points and random algebra samples. Its passing log is diagnostic only. The endpoint script checks exact identities and seven one-sided derivative limits; the all-orders argument above supplies the actual flatness proof. Neither script was rerun because the symbolic derivation already checks every required identity and no new computational question remains.

The source and primary paper are pinned in the team records with SHA256 hashes. The primary PDF text extraction has the same source and is retained for inspection. The downloaded manuscript's theorem numbers above are taken from the manuscript itself, not a search snippet. No Lean or other formal proof was produced. The proof covers the local theorem and the stated conditional carrier consequences only.
