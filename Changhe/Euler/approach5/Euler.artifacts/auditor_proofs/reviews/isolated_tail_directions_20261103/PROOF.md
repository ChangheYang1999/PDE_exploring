# Singleton components of the leading Bernoulli-gradient zero set

Status: CONFIRMED in A512 after complete independent reconstruction and full postread of Theory Agent C C36.

## 1. Exact statement and previously checked inputs

Let U in C2(R3;R3),P in C1(R3) solve the full incompressible rotating profile equation

    ((1-c)I+omega J)U+DU(Ay+U)+grad P=0, div U=0,
    A=cI-omega J, J(y1,y2,y3)=(-y2,y1,0), 1/3<c<1/2,

for any finite real omega. Assume global U.curl U=0, uniform U(y)->0, and |DU(y)|<=C0(1+|y|)^(1/2). All constants may depend on the profile and parameters. Set B=Ay+U,W=curl U,a=1-2c,kappa=1+c,H=P+|U|^2/2+(Ay).U.

Use the A210 continuous tails V,W_* and the A509 quantities

    k(y)=(Ay).V(y), E(y)=-aV(y)+Ay cross W_*(y),
    pi(y)=exp(-(log|y|/c)A)y, Z_E={w in S2:E(w)=0}.

A509 gives k in C1, grad k=E, grad H=E+o(r^(1-1/c)), U=V+o(r^(1-1/c)), W=W_*+o(r^(-1/c)), all uniformly. The exact twisted homogeneities are

    W_*(exp(sA)z)=exp(-s)exp(-omega sJ)W_*(z),
    |E(y)|=|y|^(1-1/c)|E(pi(y))|.

Let p be a vortical carrier equilibrium with the A468 parameter rho<-a. Let Sigma be the regular vortical H-level component through p, and q in Sigma with f(q)!=0, where

    f=(B cross W).grad H/|grad H|^2,
    Wf=0, Bf=mu f, mu=-a-rho>0,
    aU=(f-1)grad H.                                      (1)

By A509, either q_t=Phi_t q escapes and pi(q_t) tends to a direction w in Z_E, or its bounded forward orbit has a compact critical limit set with unbounded full W-saturation N contained in Crit(H), from which one can choose x_n with |x_n|->infinity and pi(x_n)->w in Z_E.

For any such limiting direction w, if {w} is a connected component of Z_E, then

    V(w)=0, Aw cross W_*(w)=0.                           (2)

Consequently, if Z_E is totally disconnected and the two fields V(w),Aw cross W_*(w) have no common zero on S2, every vortical carrier equilibrium has rho=-a. This is a conditional restriction; neither extra hypothesis is deduced from the PDE. A singleton component need not be isolated in the zero set.

## 2. Small normalized gradient along entire vortex lines

In the escaping case take any sequence t_n->infinity and put x_n=q_(t_n). Its complete W orbit l_n stays in Sigma and has constant f_n=f(x_n). By (1), |f_n|=exp(mu t_n)|f(q)| tends to infinity. The A210 velocity bound yields, for z in l_n outside a fixed ball,

    |grad H(z)|/|z|^(1-1/c) <= aC/(|f_n|-1).              (3)

Here n is large enough that |f_n|>1. The constant C and the exterior radius are independent of n. In the bounded-orbit case take the sequence x_n in N from the statement, and l_n its complete W orbit. It stays in N, where grad H=0, so the left side of (3) vanishes. In either case there is epsilon_n->0 and one uniform error modulus eta(R)->0 such that

    |E(pi(z))| <= epsilon_n+eta(|z|), z in l_n, |z|>=R0.  (4)

The uniformity follows from the actual A509 far-field estimate; no modulus may depend on the vortex line. It is sufficient to replace eta by its nonincreasing exterior supremum.

## 3. Rescaling and compactness of short vortex arcs

Let r_n=|x_n|, s_n=(log r_n)/c and T_n=exp(-s_n A). Define on the fixed annulus 1/2<=|z|<=2

    W_n(z)=exp(kappa s_n)T_n W(exp(s_n A)z).

The rescaled field tends uniformly to W_* there. Indeed |exp(s_n A)z|=r_n|z|, and the physical error o((r_n|z|)^(-1/c)) is multiplied by the norm exp(kappa s_n)exp(-c s_n)=exp(s_n)=r_n^(1/c). This tends uniformly to zero on the annulus. The leading term is exactly W_*(z) by homogeneity.

Choose a finite M>=1 bounding all W_n on that annulus after discarding finitely many n. For each n the rescaled full vortex curve through T_n x_n=pi(x_n) solves gamma_n'=W_n(gamma_n), with initial radius one. On the common interval [-tau,tau], tau=1/(4M), a first-exit estimate shows its displacement is at most1/4, so its image stays in the annulus. The curves are uniformly M-Lipschitz. Arzela-Ascoli supplies a uniformly convergent subsequence gamma_n->gamma. Their integral equations and uniform convergence W_n->W_* show

    gamma(t)=w+integral_0^t W_*(gamma(v)) dv.

Thus gamma is C1, gamma(0)=w and gamma'=W_*(gamma). No uniqueness of solutions to the continuous limiting field is required.

For each t, gamma_n(t)=T_n z_n(t) for a point z_n(t) in l_n, and |z_n(t)|>=r_n/2. Moreover pi(gamma_n(t))=pi(z_n(t)), by invariance of pi under exp(sA). From (4), uniform convergence of the curves and continuity of E and pi on the annulus, we obtain

    E(pi(gamma(t)))=0, -tau<=t<=tau.                     (5)

The continuous image pi(gamma([-tau,tau])) is therefore a connected subset of Z_E containing w. If {w} is a connected component, that image equals {w}. This uses connected components, not isolatedness or local uniqueness.

## 4. Tangency to the spiral ray and the conditional exclusion

The fiber pi^-1({w}) is exactly {exp(sA)w:s in R}, since |exp(sA)w|=exp(cs). It is a smooth embedded curve with tangent Aw at w, and Aw is nonzero because c>0. Equation (5) and the singleton-component assumption force gamma to lie on that curve. Differentiating at zero gives W_*(w)=gamma'(0) parallel to Aw. As w lies in Z_E and a>0,

    0=E(w)=-aV(w)+Aw cross W_*(w)

then implies V(w)=0. This proves (2).

If Z_E is totally disconnected, all its connected components are singletons. Suppose a vortical equilibrium had rho<-a. A509 supplies at least one limiting direction of the kind above, and (2) gives a common zero, contradicting the additional hypothesis. The remaining inequality rho<=-a is A496, so necessarily rho=-a. When Z_E is empty, A509 already gives the contradiction without any curve limit. None of this constrains a nonzero irrotational equilibrium or a flat periodic witness.

## 5. Scope and verification

The short rescaled-arc argument proves a necessary condition even when Z_E has accumulating singleton components. It assumes no smoothness of the angular tails beyond the continuous A210 fields and the C1 scalar k already checked in A509. It does not assert that a zero of E is impossible or that the leading tail extends to an exact global profile.

Dependencies: A048/A509 flow completeness and level invariance, A210 uniform tails, A496 equilibrium inequality and A509 dichotomy. The entire new C36 Proposition9 and its proof, exact scope, notation and concluding remarks were read and compared to the independent reconstruction. The configured-model Theory Agent C source is the existing model collaboration. No computation or external model client was used.
