# Uniform tail regularity and the full image of the scattering map

Status: CONFIRMED by independent audit A533, 2026-11-03T07:22:07.096261+00:00, at the exact hypotheses below. The full existing configured-model source/comparison was read; no new model client was used.

## 1. Statement

Let 2/5<c<1/2, omega be any finite real number, A=cI-omega J, L=(1-c)I+omega J, Q_t=exp(omega tJ), and p=(1-c)/c. Here J(x1,x2,x3)=(-x2,x1,0). Suppose U in C2(R3;R3), P in C1(R3) solve

    div U=0, LU+DU(Ax+U)+grad P=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1).

No helicity assumption is made. Let B=Ax+U, Phi_t its complete flow, W=curl U, and

    u_t(x)=exp((1-c)t)Q_t U(exp(tA)x), w_t=curl u_t,
    v_t(z)=exp(-tA)Phi_t(z), M_t=Dv_t.

The actual tails from A210 give u_t->V and w_t->Wstar uniformly on compact subsets of D=R3 minus{0}. Define E to be the set of points whose positive B-orbit is unbounded. The conclusions are:

1. v_t converges uniformly on all R3 to a continuous proper surjection v. Its zero fiber is exactly the compact set of forward-bounded points, and v(E)=D.
2. For every compact K contained in E and every 0<alpha<1, M_t has a uniform C^alpha bound on K for all t>=0.
3. u_t converges to V in C^(1,alpha)loc(D) for every alpha<1. With the canonical pressure scaling p_t of A530, S_t=p_t-|u_t|^2/2 converges to S=P2-|V|^2/2 in C1loc(D).

Conclusion1 only needs bounded U and c>0, plus global completeness. The natural derivative hypotheses enter conclusions2-3. The target square-root derivative screen U->0,DU=O(sqrt r) supplies the natural bounds through A498,A476,A477. No C2 velocity limit or rate of derivative convergence is claimed.

## 2. The limiting scattering map is onto

Let C0=||U||infinity. B has at most linear growth and is locally Lipschitz, so Phi_t exists for all finite positive and negative times. Each v_t is a diffeomorphism of R3. Direct differentiation gives

    v_t(z)=z+integral_0^t exp(-sA)U(Phi_s(z))ds,
    |v_t(z)-z|<=C0/c,
    sup_z|v_t(z)-v(z)|<=C0 exp(-ct)/c.                 (1)

The last formula defines v by the absolutely and uniformly convergent integral. It is continuous and |v(z)-z|<=C0/c, so it is proper.

Fix any x in R3 and integers n tending to infinity. Since v_n is onto, choose z_n=v_n^(-1)(x). The second inequality in (1) puts all z_n in the closed ball of radius C0/c about x. Pass to z_n->z. Uniform convergence in (1) and continuity of v give v(z)=x. Thus v is onto, without an unproved proper-map degree assertion.

If the forward orbit of z is bounded, v_t(z)->0, so v(z)=0. Conversely, if that orbit is unbounded, choose t0 with r0=|Phi_(t0)(z)|>C0/c. Where r=|Phi_t(z)|>0,

    r'>=cr-C0.

Comparison for t>=t0 gives r(t)>=exp(c(t-t0))(r0-C0/c)+C0/c. Thus |v(z)|>=exp(-ct0)(r0-C0/c)>0. The inequality also shows that an unbounded orbit eventually stays outside every fixed sufficiently large sphere. In particular E is open. Its complement is bounded and closed, because every initial point outside a radius greater than C0/c escapes. The zero fiber is therefore precisely this compact set, and surjectivity implies v(E)=D.

This result does not say the local zero set of a leading Bernoulli gradient fills D. It only concerns the image of the full escaping set.

## 3. Uniform first-derivative control on an escaping compact set

Fix a compact K0 in E and rho0 in(0,1] such that K_(rho0), its closed rho0-neighborhood, is contained in E. Finite covering by open escape-time sets gives T0 such that all its trajectories lie outside a sufficiently large ball for t>=T0. The radial comparison gives a uniform positive lower bound for |v_t| there; (1) gives an upper bound. Hence their images lie in a fixed compact annulus.

The exact evolution and Cauchy formulas are

    v_t'=exp(-t)u_t(v_t),
    M_t'=exp(-t)Du_t(v_t)M_t,
    w_t(v_t)=M_t W.                                  (2)

The natural estimates bound u_t and Du_t on any fixed annulus uniformly in t. Thus Gronwall in the second equation, whose coefficient is integrable in t, bounds M_t uniformly on K_(rho0). Also det M_t=1, since div B=3c and det exp(-tA)=exp(-3ct). In dimension3 the cofactor formula bounds M_t^(-1) by a fixed multiple of |M_t|^2. Increasing a constant L covers all t>=0. The already confirmed A518 argument also gives M_t->M uniformly locally on E with det M=1, and v is locally C1 there. No Holder bound has yet been used.

## 4. A local Holder inequality without a lost power in its recursive coefficient

Write K_rho for the closed rho-neighborhood of K0 and

    m(t,rho)=[M_t]_(C^alpha(K_rho)).

For each finite t this is finite and locally bounded in time, because Phi_t is C2. Let 0<=rho<rho'<=rho0 and delta=rho'-rho. By the inverse bound in Section3,

    B(v_t(z),delta/L) is contained in v_t(K_(rho')),

for z in K_rho. To justify this, lift a straight segment from v_t(z) through the global inverse v_t^(-1). Until the lift could leave K_(rho'), its derivative is bounded by L, so a segment of length less than delta/L cannot travel the distance delta needed to leave. The inverse is L-Lipschitz on this ball. The forward map is L-Lipschitz on B(z,delta), by integration along segments there.

Take r=delta/(2L). The interior div-curl estimate on B(x,2r), x=v_t(z), is

    [Du_t]_(alpha,B(x,r))
      <=C_alpha([w_t]_(alpha,B(x,2r))
                   +r^(-alpha)||w_t||infinity
                   +r^(-1-alpha)||u_t||infinity).     (3)

It is the usual unweighted local Schauder estimate for div u_t=0,curl u_t=w_t, obtained from the Newton representation of curl w_t with a cutoff and the harmonic interior estimate. All norms are on the displayed larger ball. There is no coefficient depending on r in front of [w_t]_alpha.

The third equation in (2) and the inverse Lipschitz bound give

    [w_t]_(alpha,B(x,2r))
      <=L^alpha(m(t,rho')||W||infinity+L[W]_(alpha,K_(rho0))).

Here W is C1 on the fixed initial compact set. For pairs of initial points at distance less than r/L, (3) and the forward Lipschitz estimate control the composition Du_t o v_t. For farther pairs use its uniform sup norm and divide by (r/L)^alpha. Consequently

    [Du_t o v_t]_(alpha,K_rho)
          <=C1 m(t,rho')+C2 delta^(-1-alpha).         (4)

Constants are uniform in t>=T0 and in rho,rho'. Taking the seminorm in the integral equation for M_t and using the product rule for Holder seminorms yields

    m(t,rho)<=m(T0,rho0)
       +C integral_(T0)^t exp(-s)
                     [m(s,rho')+delta^(-1-alpha)]ds. (5)

The power of delta appears only in the inhomogeneous term. Moving it to the recursive coefficient would destroy the following argument.

## 5. Nested neighborhoods close the estimate

Fix rho<rho0 and put rho_j=rho+(rho0-rho)(1-2^(-j)), j>=0. Let tau(t)=exp(-T0)-exp(-t), so 0<=tau<=1. Iterate (5) n times using rho_j<rho_(j+1). The ordered time integrals equal tau^j/j!, and the jth spatial gap contributes at most

    (rho0-rho)^(-1-alpha) 2^(j(1+alpha)).

The resulting bound is the sum of m(T0,rho0)exp(C), an absolutely convergent exponential series with these gap factors, and the remainder

    (C tau)^n/n! sup_(T0<=s<=t)m(s,rho0).

For each fixed finite t the supremum is finite, so the remainder tends to zero as n increases. The remaining exponential series is bounded independently of t. This proves a uniform bound for m(t,rho) for t>=T0, and finite-time smoothness covers [0,T0]. Taking rho=0 proves conclusion2 for arbitrary K0.

The argument first fixes t, removes the recursive remainder, and only then observes that the resulting bound is uniform in t. It does not assume a bound on m(t,rho0) as t tends to infinity.

## 6. Velocity and deficit convergence on every punctured compact set

Fix z in E. The preceding estimate with two nested initial neighborhoods and (3) gives a ball B(v_t(z),r) with uniform Holder control of Du_t. Since v_t(z)->v(z), a smaller fixed ball about v(z) is contained in those balls for all sufficiently large t. Arzela-Ascoli and the known C0 limit u_t->V imply V is C1 on that ball and Du_t->DV uniformly there. The same Holder bound gives convergence in every strictly smaller Holder exponent, by interpolation or compact embedding. Choose the original exponent arbitrarily close to1 to obtain C^(1,alpha) convergence for every alpha<1.

By Section2 every x!=0 equals v(z) for some z in E. The preceding balls therefore cover D, and finitely many cover any compact subset. This proves the global punctured conclusion3. A530 supplies C1 convergence of p_t, so ordinary products give C1 convergence of S_t. No higher velocity derivative is inferred from this proof.

## 7. Comparison and limits

Sections3-6 reconstruct all essential steps of the actual configured-model Theory Agent C C37 Lemma16 proof, including its nonuniform outer seminorm and factorial iteration. Section2 removes the unnecessary restriction to the unspecified image cone by a separate elementary compactness argument. The moving-cutoff W2q argument in the neighboring natural_tail_c1 topic, LIT136, is a different route to stronger local Sobolev bounds and is not needed for the result here.

The pressure part is A530. The geometric consequences for a limiting Bernoulli sheet are proved separately in the neighboring limiting_bernoulli_sheet topic and retain global zero helicity. This regularity theorem imposes neither that helicity condition nor symmetry, but retains the full natural derivative bound or its confirmed square-root sufficient condition. No computation or new model client was used.
