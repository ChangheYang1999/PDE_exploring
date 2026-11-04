# Axisymmetric polar zeros: pressure, endpoint uniqueness and swirl

Status: independent proofs of LIT224-LIT226 and the stronger zero-vorticity criterion in Section9. The conclusions concern precisely specified local homogeneous fields. They do not impose axisymmetry on an arbitrary Euler tail.

## 1. Common hypotheses and exact conclusions

Let 0<c<1/2, p=(1-c)/c>1, a=1-2c, omega in R, Jx=(-x2,x1,0), A=cI-omega J and x0=(0,0,1). Let

    G={x=r n: r_-<r<r_+, n in S2, n3>z_*},
    0<r_-<1<r_+, -1<z_*<1.

Suppose V is a smooth real vector field on G, including the north ray, axisymmetric in the vector sense, ordinarily homogeneous of degree -p wherever scaling stays in G, and div V=0. Suppose P2 is a smooth real scalar, with the local twisted homogeneity P2(exp(tA)x)=exp(-2(1-c)t)P2(x). Put W=curl V and S=P2-|V|2/2 and assume

    W.grad S=0, -Delta P2=tr((DV)^2).

The following statements are proved below.

1. If V is purely azimuthal and flat to infinite order at x0, then V=0 on G. This is LIT224.
2. If (Ax).V=0 on G and V is flat to infinite order at x0, then V=0 on G. This is LIT225, with its range strengthened from 1/3<c<1/2 to 0<c<1/2.
3. If V.W=0 on G and V is flat to infinite order at x0, then V_phi=0 on G. This is LIT226, with the same range strengthening. Without (Ax).V=0 it does not force the remaining meridional velocity to vanish.
4. In each of these three statements, infinite-order flatness can be replaced by the single condition W(x0)=0. The last section proves this stronger conclusion.

All smoothness and pressure identities are hypotheses. P2 need not be axisymmetric. No rank relation between grad((Ax).V) and grad S is used. The original source statements for225 and226 have 1/3<c<1/2; the proof below shows explicitly why p<2 is unnecessary.

## 2. Averaging the pressure is legitimate

Let R_alpha=exp(alpha J) and Pbar(x)=(2pi)^(-1) integral P2(R_alpha x) d alpha. The full cap G is invariant under every such rotation. V and W are equivariant, so the source tr((DV)^2) is axisymmetric. Rotation commutes with Delta. Also

    W(x).grad[P2(R_alpha x)]
       =W(R_alpha x).grad P2(R_alpha x).

Thus Pbar and Sbar=Pbar-|V|2/2 satisfy the same two pressure and transport identities. Since A and J commute, shifting the angle in the twisted homogeneity gives ordinary homogeneity Pbar(rn)=r^(-2p)u(n). It is axisymmetric, so u=u(z), z=n3. This step keeps every pressure mode in the original problem; it uses only their average. Averaging a general nonaxisymmetric velocity would not preserve its quadratic source, and is not done here.

## 3. Direct pure-swirl proof and arbitrary zero circles

For V=r^(-p)f(theta)e_phi, put d=p-1, q=2p/d>2, g=f2 and Pi(theta)=u(cos theta). Direct curl and differentiation give

    W=r^(-p-1)[(f'+cot(theta)f)e_r+d f e_theta],
    d f h'=2p(f'+cot(theta)f)h,
    Pi''+cot(theta)Pi'+2p(2p-1)Pi=-2p g+cot(theta)g',

where Sbar=r^(-2p)h and Pi=h+g/2. The pressure source follows from (V.grad)V=-r^(-2p-1)g(e_r+cot(theta)e_theta); its radial and tangential divergences sum to r^(-2p-2)(2p g-cot(theta)g').

On every nonzero-f component I,

    h=C_I sin(theta)^q g^(q/2).

C_I is finite at any interior point, with no uniform bound across components. At an interior endpoint f=0, hence g=g'=h=h'=Pi=Pi'=0. Since q/2>1, differentiating Pi=g/2+C_I sin(theta)^q g^(q/2) shows, on a sufficiently short one-sided interval,

    g+|g'|<=C(|Pi|+|Pi'|).

The pressure equation then gives |Pi''|<=C(|Pi|+|Pi'|). Its zero Cauchy data and elementary one-sided Gronwall force Pi=g=0 there, a contradiction. Therefore a nonempty component of {f!=0} cannot have an interior endpoint. Either f=0 on the entire interval or f has one sign everywhere on the punctured cap.

In the latter case a single finite C satisfies

    |Sbar|/|V|2=|C|sin(theta)^q|f|^(q-2) ->0

at the pole. Infinite flatness and the full-ball pressure argument of Section8 exclude this case. The same argument with Section9 gives the stronger zero-vorticity version. This proves LIT224 independently of the more general component calculation below.

## 4. General axisymmetric geometry and the two reductions

Write w=1-z2, s=sqrt(w), and

    V=r^(-p)[R(z)e_r+H(z)e_theta/s+F(z)e_phi/s].

Smoothness at the pole implies F,H=O(w); R has a finite limit. Incompressibility and curl give

    H'=(2-p)R,
    r^(p+1)W=(-F', (p-1)F/s, -(p-1)H/s+sR').

For the open condition (Ax).V=0, one has R=tF with t=omega/c throughout the cap. In particular V(x0)=0. Alternatively zero helicity gives, by canceling the two H F terms,

    r^(2p+1)V.W=F R'-R F'=0.

On every component I of {F!=0}, this implies R=t_I F for a single finite real constant t_I. Its value need not equal omega/c. These are the only uses of the respective extra hypotheses.

On such a component fix its t and put kappa=(2-p)t. Then H'=kappa F and

    e=|r^pV|2/2=[t2F2+(F2+H2)/w]/2, u=e+h.

Scalar transport becomes 2p F'h-(p-1)Fh'=0, so

    h=C_I|F|^nu, nu=2p/(p-1)>2.

The constants t and C are fixed only for this one component. All following endpoint estimates are local to that component.

## 5. Independent endpoint matrix and positive quadratic

In the orthonormal spherical frame M=r^(p+1)DV is

    [ -ptF,  -tsF'-H/s,           -F/s;
      -pH/s, (p-1)tF-zH/w,        -zF/w;
      -pF/s, -F'-zF/w,            tF+zH/w ].

This follows by differentiating each spherical component and its moving basis. The pressure equation is (w u')'+lambda u=-tr(M2), lambda=2p(2p-1).

At an interior endpoint z0 of I, F=0. Smoothness and nu>2 give h=h'=h''=0 there. Put d=F'(z0), H0=H(z0), w0=1-z0^2. Differentiating e gives

    e=H0^2/(2w0), e'=z0 H0^2/w0^2,
    e''=(t2+1/w0)d2+kappa H0 d/w0
          +H0^2(1/w0^2+4z0^2/w0^3).

At this endpoint the diagonal part of tr(M2) is 2z0^2 H0^2/w0^2. Its only nonzero off-diagonal pair is 2p t H0 d+2p H0^2/w0. Substitution into the pressure equation therefore gives exactly

    (1+t2 w0)d2+(p+2)t H0 d
       +[(2p2+p+1)/w0+4z0^2/w0^2]H0^2=0.

The first coefficient is positive. Four times the determinant is

    4(2p2+p+1)/w0+16z0^2/w0^2
        +t2[7p2+16z0^2/w0]>0.

This is positive for every p>1 and every real t. Consequently d=H0=0. No assumption p<2, sign of t or finite vanishing order has been used.

## 6. One-sided uniqueness on each component

A further direct multiplication gives tr(M2)=T'+R0, where

    T=2pt HF+zF2/w,
    R0=(2p-1)[2(p-1)t2+1/w]F2
         +[2p/w+2z2/w2]H2+2kappa zFH/w.

For a check of all derivative terms, tr(M2) contains 2pt HF'+2zFF'/w. Differentiating T removes those terms and 2pt kappa F2+(1/w+2z2/w2)F2; the remaining t2 coefficient is 2(p2-p+1)-2p(2-p)=2(2p-1)(p-1), as displayed.

Hence (w u'+T)'=-lambda u-R0. Near the fixed interior endpoint, u=e+C|F|^nu and nu>2 imply

    u>=b(F2+H2)>=0, |T|+|R0|<=C1u

for finite b>0,C1, after shrinking within that component. All coefficients are bounded because w stays positive there. The endpoint values are u=u'=T=0. Integrating the last differential equation gives

    |u'(z)|<=C2[u(z)+integral_from_endpoint_to_z u].

For a left endpoint, Y=u+integral u is nonnegative, starts at0 and satisfies Y'<=C3Y. Multiplication by the decaying integrating factor gives Y=0, a contradiction. Reverse z at a right endpoint. Every nonempty component must therefore be the entire connected punctured interval. The conclusion is either F=0 everywhere or F never vanishes there and R=tF, h=C|F|^nu use one finite pair of constants.

This argument does not take a supremum over components. Arbitrarily many hypothetical zero circles and unbounded families of component constants are permitted at the start and ruled out one component at a time.

## 7. Pole pressure bound and the original flatness conclusions

If F never vanishes, the pole limit F=0 and R=tF imply V(x0)=0. Since |r^pV|2>=F2/w,

    |Sbar|/|V|2<=|C|w|F|^(nu-2) ->0.

This limit is uniform in azimuth and on compact radial subintervals. Also Pbar(x0)=0. Thus for every fixed epsilon>0, on a sufficiently small full Euclidean ball about x0,

    Sbar>=-epsilon|V|2.

If V is infinitely flat there, Section8 with epsilon=1/4 forces V=0 near x0, contradicting the nonzero-F alternative. Hence F=0 on the entire angular interval. This proves the zero-helicity swirl conclusion of226. If the open condition (Ax).V=0 holds, it now gives R=0; incompressibility makes H constant and its pole limit makes H=0. Therefore V=0 on G, proving225. Pure swirl is the special case R=H=0, giving224 as well.

## 8. Local pressure lemma with a second-order velocity zero

Let v,pi be smooth on a ball centered at0, div v=0 and -Delta pi=partial_i partial_j(v_i v_j). Define spherical averages

    E(r)=average |v|2, A0(r)=average(v.n)^2,
    Y(r)=average[pi-pi(0)]+A0(r).

The spherical mean of div div(v tensor v) equals

    r^(-2)partial_r{r2[A0'+(3A0-E)/r]}.

The pressure equation and smoothness at0 remove the radial integration constant and give Y'=(E-3A0)/r. Suppose v(0)=Dv(0)=0, so E,A0=O(r4), Y(0)=0 and integration gives Y=O(r4). If

    pi-pi(0)-|v|2/2>=-|v|2/8

on the ball, then Y>=3E/8+A0>=0, and

    Y'<=8Y/(3r), (r^(-8/3)Y)'<=0.

The nonnegative quantity r^(-8/3)Y tends to0 at the origin, so it is identically zero. Then E=0 on every smaller sphere and v=0 near0. This proves the lemma without assuming that pi itself has a flat Taylor series or fixing a global pressure normalization.

For the original infinite-flat argument, the same calculation uses Y>=E/4+A0, Y'<=4Y/r and Y=o(r4). Both forms are valid. The second-order version is what improves the source hypotheses.

## 9. Zero vorticity at the pole suffices

Assume W(x0)=0 in place of infinite flatness. If F=0 on the whole interval, the swirl conclusion is already proved. Otherwise Section6 gives one nonzero-F component covering the punctured cap, R=tF, and hence V(x0)=0. Let M0=DV(x0). Axisymmetry implies M0 commutes with all rotations about e3. Its real matrix form is therefore

    M0=[lambda,-beta,0; beta,lambda,0; 0,0,gamma].

Ordinary homogeneity gives M0 e3=-pV(x0)=0, so gamma=0. Incompressibility gives lambda=0. Thus M0=beta J and W(x0)=2beta e3. The assumed W(x0)=0 implies M0=0.

The smooth velocity consequently has a second-order zero. Section7 supplies the pressure deficit with epsilon=1/8, and the local lemma in Section8 forces V=0 near x0. This contradicts the nonzero-F alternative. Thus F=0 on G for every axisymmetric zero-helicity pair satisfying the common hypotheses and W(x0)=0. In the open-k-zero case the additional R=H=0 argument gives full vanishing. The pure-swirl case is also included.

The entire proof requires only p>1, equivalent to 0<c<1/2. This confirms both improvements together: no infinite-order premise and no c>1/3 restriction. There is no claim that an arbitrary nonaxisymmetric point can be put into this polar axisymmetric configuration.

## 10. Verification and limits

All seven sections of224, seven of225 and six of226 were read in full. The exact curl, helicity cancellation, matrix, endpoint quadratic and derivative decomposition were independently derived above, without numerical algebra or a formal build. The pressure identity is the independently confirmed A1200-A1207 identity, with its integration and improved exponent spelled out here.

These theorems do not remove the symmetry assumption or imply the global rotating conjecture. A purely meridional field in the zero-helicity case can survive the present argument if open (Ax).V=0 is absent. In that branch F=0, so the scalar formula h=C|F|^nu must not be continued into it; W.grad Sbar is automatically zero. The actual-tail rank relation is separate information there. No general meridional or common-flat exclusion is certified by this proof.
