# A posteriori closure with an L2 low metric and no negative norm

## 1. Statement, spaces and hypotheses

This is a new alternative to the baseline four-component framework. Its high norm contains weighted second derivatives, first derivatives and L². The low metric is L². It does not require the residual or correction to belong to the homogeneous negative space.

All functions are real and S1, meaning even in x and odd in y. R_j has multiplier i xi_j/|xi|, U[h]=(-R1R2 h,R1²h), J=(1-Delta)^(1/2), omega=(1+4|X|²)^(2/5), and v=omega². Let E be the completion of compact smooth S1 functions in

E(h)²=P(h)²+2^14 a(h)²+2^18 b(h)²,
P=||omega D²h||_2, a=||Dh||_2, b=||h||_2.                  (1)

For0<s<=1/1024 let X_s be the corresponding completion in X_s(h)=E(J^s h). Tensor norms are ordered Cartesian Frobenius norms. In particular both E and X_s have no H^-1 term.

Let rho be a smooth S1 reference, u=U[rho] its canonical velocity, V=cX+u, a0=rho_y(0)>0. Assume the following conditions.

(A) Structure and normalization. 9/5<c<37/20; c+partial_y u2(0)=1. The fields in Analysis II(B0) are bounded: D rho, <r>D²rho, <r>²D³rho, <r>²D⁴rho, Du, <r>D²u and <r>D³u. In addition, for some gamma<1, |D^j rho|=O(r^(gamma-j)), j=0,1,2, outside a ball. The canonical u is smooth, divergence free and at most sublinear. These assumptions specify the background at the origin and infinity and make V globally Lipschitz and complete.

(B) Signed L² margin. Put

theta=ess sup (sqrt(rho_x²+rho_y²)-rho_y)/2,
kappa²=[(log2-1/2)||D rho_x||_2²+(3log2-2)||D rho_y||_2²]/(16pi).

Require the certified inequality

c+1-theta-kappa >=2.                                     (2)

The seminorms are finite by(A). This condition replaces the baseline low negative-norm coercivity. It is a global condition, not a sampled one.

(C) First and second derivative energy conditions. Define

A=[[rho_y,-rho_x/2],[-rho_x/2,0]],
M1=I-sym Du+A,
M2=(1+c+V.D log omega)I-2sym DV+A,
S=(v_xy rho_x-v_xx rho_y-v_x rho_xy+v_y rho_xx)/2.

Require M1>=(9/10)I and M2>=(1/2)I everywhere, together with

||D²rho||_infinity<=3, ||omega D²rho||_infinity<=8,
||omega D³rho||_infinity<=10, ||omega D²u||_infinity<=3,
||D(v D rho)/omega||_infinity<=28, ||S||_infinity<=40.      (3)

These are the baseline(B4),(B5),(B7) conditions, with the same tensor convention.

(D) Fractional commutator coefficients. Component sums, with each ordered component's supremum taken separately, obey

(|c|,||Du||_S,||omega D²u||_S,||omega D³u||_S,
 ||D rho||_S,||omega D²rho||_S,||omega D³rho||_S,||omega D⁴rho||_S)
 <=(2,6,24,160,22,32,80,2048).                            (4)

For k in X_s define L=V.D-1+U[.].D rho and A_k=L+U[k].D. The maximal domain is

D_s(A_k)={h in X_s: A_k h in X_s as a distribution}.

Then A_k generates a strongly continuous semigroup on X_s with

||exp(t A_k)|| <= exp[-t(1/4-4800s-5X_s(k)/sqrt(s))].      (5)

On L² its consistent maximal-domain inverse has norm at most1/2, independent of k. Every positive rate in(5) gives an X_s inverse with norm bounded by its reciprocal.

For the a posteriori conclusion, put

s=2^-17, r=2^-14, eta=1/163840=r/10.                      (6)

If the actual stationary residual F=V.D rho-rho belongs to X_s and X_s(F)<=eta, there exists exactly one h in

B={h in X_s: X_s(h)<=r, c[h]=partial_y U2[h](0)=0}

such that F(rho+h;c)=0. Its origin slope remains positive. Picard iteration of T(k)=-A_k^-1F converges in L² with ratio less than0.00312. A fixed leading profile of rho, if specified, is preserved because h tends to zero at infinity.

These are conditional claims. The original state131 has all background hypotheses, using the new seminorm certificate, but its residual is not in L². No reference has yet been shown to satisfy all hypotheses including(6).

## 2. Signed L2 estimate and inverse

Write a=rho_x, b=rho_y and Q=-aR1R2+bR1². Direct expansion gives

Sym Q=P0+K,
P0=R1 b R1-(R1 a R2+R2 a R1)/2,
K=(1/2)[R1,[R1,b]]-(1/2)[R1,[R2,a]].

Skew-adjointness of R_j gives

<P0 h,h>=integral[-b|R1 h|²+a(R1 h)(R2 h)]<=theta||h||_2².

Here sum_j||R_jh||²=||h||² and the largest eigenvalue of the two-by-two integrand matrix is theta pointwise. The independently audited gradient-structured identity gives ||K||<=||K||_HS=kappa. Its cutoff extension applies by(A).

The field V+U[k] has divergence2c, is globally Lipschitz and has at most linear growth: X_s controls H^(2+s), hence U[k] and DU[k] are bounded. Therefore, on compact smooth tests,

Re<A_k h,h> <= -(c+1-theta-kappa)||h||² <=-2||h||².        (7)

The complete Lipschitz transport flow defines a strongly continuous L² group. Its generator is maximal distributional transport, by mollification and radial cutoff. Q is a bounded L² operator because D rho is bounded. Bounded perturbation defines A_k on the same maximal domain. The core estimate(7) extends to that domain and gives semigroup norm at most exp(-2t). The integral -integral_0^infinity exp(tA_k)f dt is therefore in the generator domain and is the inverse with norm at most1/2. A kernel element has a constant, exponentially decaying orbit and is zero. This proves both onto and one-to-one statements, without a trace assumption on general L² inputs.

## 3. Base high estimate

The exact gradient and weighted-Hessian identities of Analysis II P7.5 use only(C), not its negative-norm estimate. On smooth tests they give

Re<D Lh,Dh> <=-(9/10)a²+6ab,
Re<D²Lh,omega²D²h> <=-(1/2)P²+(347/5)Pa+10Pb+40a².       (8)

For clarity, the Hessian Pa coefficient is28(9/5)+3+16=347/5. The weighted Riesz constant9/5 applies to the centrally odd second derivatives; the three terms are respectively the exact gradient identity remainder, D²u.Dh, and the two differentiated coefficient terms. The last two terms in(8) are the U[h].D³rho term and S term. Thus neither H nor a negative norm appears in this step.

Combine(7) at k=0 with(8), with weights1,2^14,2^18. The claim

-Re<Lh,h>_E >=(1/4)E(h)²                               (9)

is equivalent to nonnegativity of the quadratic form on(P,a,b) with matrix

G=[[1/4,-347/10,-5],
   [-347/10,53048/5,-49152],
   [-5,-49152,458752]].

Its three leading principal minors are1/4,144831/100 and1077858728/25, all positive. This proves(9) without separate Young relaxations. The smooth complete background flow acts strongly continuously on E by the weighted chain rule and(A); Q is bounded on E by product rules, the same weighted Riesz estimate and(C). Hence its generator has the maximal distributional realization and(9) extends by its graph core.

## 4. Fractional and rough losses do not use a negative norm

Use e=(P,128a,512b), for the derivatives of J^s g. The first three output rows of the smooth commutator calculation in Analysis II P8.4 yield the energy bound s e^T K3 e with

K3=[[4708,85/2,68],[0,4290,340],[0,0,3882]].

The symmetric row sums are19053/4,17925/4 and4086, all less than4800. Therefore

|Re<[J^s,L]J^-s f,f>_E|<=4800s E(f)².                   (10)

The fourth H row of that calculation is not needed. Its first three rows follow from the explicit Bessel-kernel multiplication and transport bounds and the coefficient sums(4). They depend only on weighted Hessians, gradients and L² inputs. Thus deleting H does not invalidate the input norm in(10).

For completeness the rough estimate has the same property. Put n=X_s(k), W=U[k], f=J^s g and E=E(f). The Fourier embedding gives ||W||_(H^(2+s))<=n and ||DW||_infinity<=c_s n, where c_s=[2sqrt(pi s(1+s))]^-1 and c_s sqrt(s)<3/10. The exact top derivative expansion is

D²J^s(W.Dg)=W.D D²f+[J^s,W.D]D²g+2J^s(DW D²g)+J^s(D²W Dg).

The first three terms cost at most (n/sqrt(s))A_s P², where A_s=127/50+(653/5)s. The last costs at most (n/sqrt(s))B_s E P, B_s=(9/5)(1+44s). This follows from

||omega J^s(vf)||_2<=(1+44s)s^-1/2||v||_(H^(1+s))||omega J^s f||_2,
||omega J^s D²W||_2<=(9/5)n,

and ||Dg||_(H^(1+s))<=E. These input bounds use no negative norm. The first-derivative and L² energy costs are at most(13/10)(n/sqrt(s))(128a)² and(3/10)(n/sqrt(s))(512b)². Setting x=P/E in[0,1], the total divided by n E²/sqrt(s) is at most

A_s x²+B_s x+(13/10)(1-x²)<=A_s+B_s<5,

for s<=1/1024. The statement is trivial if E=0. Hence the rough energy loss is at most5 n E²/sqrt(s). Combined with(9)-(10), this proves the smooth form of(5). It is an energy estimate on the graph core, not a high-to-high bound for the transport nonlinearity.

## 5. Rough realization and maximal domain

The map J^s is an isometric bijection from X_s onto E. Its range is dense because J^-s maps compact smooth functions into Schwartz functions, and smooth cutoffs approximate those functions in all the required weighted norms. Completion then gives the assertion. Also X_s continuously injects into L² and H^(2+s).

Choose smooth compact S1 k_m converging to k in X_s. Then W_m=U[k_m] converges in W^(1,infinity). Each smooth A_(k_m) has an X_s semigroup by the flow construction, bounded perturbation and smooth conjugation by J^s. Its bound(5) is uniform on bounded k_m sequences and converges to the displayed rate. On any finite time interval the difference of two such solutions has forcing(W_m-W_l).D S_l(t)f. Uniform high bounds control its L² norm, and W_m-W_l tends uniformly to zero. The common L² energy estimate and Duhamel formula show convergence in C_t L².

Weak compactness in X_s, uniqueness of the L² limit and lower semicontinuity give an X_s limit S(t) with(5). L² uniqueness proves its semigroup law. At t=0 the same convergence and boundedness imply weak X_s convergence to f, while(5) gives limsup X_s(S(t)f)<=X_s(f). The Hilbert norm identity gives strong continuity.

This semigroup is the restriction of the L² semigroup from Section2. To identify its domain, if h and A_k h belong to X_s distributionally, they belong to L² and the maximal L² characterization applies. Its Duhamel identity is

S(t)h-h=integral_0^t S(v)A_k h dv.

The right side is an X_s integral by strong continuity. Dividing by t proves h is in the high generator domain. The reverse inclusion follows from the L² restriction. This proves the asserted maximal domain, not just a subdomain obtained by completion. Integrating the positive-rate semigroup establishes high surjectivity and injectivity. The inverses agree on common inputs by L² uniqueness.

## 6. Trace, complete ball and nonlinear fixed point

The Fourier embedding gives X_s subset H^(2+s) subset C^(1,alpha) for every0<alpha<s. It also gives |c[h]|<=c_s X_s(h), so c is a continuous functional on X_s. Its contact formula is

c[h]=-h_y(0)/4+(1/pi)PV integral sin(3theta)h(X)|X|^-3 dX.

The local integral converges after the linear Taylor cancellation; the exterior is controlled by L². This formula is not imposed on the low space itself.

If k has c[k]=0 and h in D_s(A_k) solves A_k h=f, first-order expansion at the origin yields

f_y(0)=(c+c[rho]-1+c[k])h_y(0)+a0c[h]=a0c[h].            (11)

Thus the high inverse maps the zero-forcing-jet hyperplane into ker c, and conversely. The actual normalized residual satisfies F_y(0)=0 by the same expansion of V.D rho-rho. Parity makes U[h](0)=0, so no constant term was omitted.

The ball B is complete in L²: an L² Cauchy sequence in B has a weak X_s convergent subsequence, whose image in distributions is the given L² limit. Lower semicontinuity preserves the radius and continuity of c preserves the constraint. This also proves uniqueness of the high limit as a distribution.

Let beta=1/4-4800s-5r/sqrt(s). Under(6), beta>1/10 by the exact/Arb calculation supplied separately. Therefore T(k)=-A_k^-1F maps B into itself by(5),(11) and X_s(F)<=r/10. For k,l in B, common L² domains give

A_k(T(k)-T(l))=U[l-k].D T(l).

Since U is an L² vector contraction and ||D T(l)||_infinity<=c_s r,

||T(k)-T(l)||_2 <=(c_s r/2)||k-l||_2.                    (12)

The right side is an L² product; no unbounded high nonlinear map is invoked. With(6), c_s r<0.006234, so the ratio is less than0.00312. The contraction theorem on B gives the unique fixed point and hence the exact stationary equation. Conversely, any stationary h in B belongs to D_s(A_h), because A_h h=-F is in X_s, and high inverse uniqueness makes it a fixed point.

At the origin, M1>=.9I and normalization imply a0>=c-11/10>7/10. Since |h_y(0)|<=c_s r<.006234, the corrected slope is positive. Fourier integrability gives h and Dh tending to zero at infinity, preserving any specified leading r^gamma profile. The scaling direction with a nonzero r^gamma leading term is outside X_s.

## 7. Forcing data and the changed tail threshold

If E(f)<infinity and Q3=||omega D³f||_2<infinity, the same weighted Bessel-kernel interpolation argument, now with only three components, gives

X_s(f)<=E(f)^(1-s)(2Q3²+16410 E(f)²)^(s/2)+34s E(f).      (13)

To see the constants without introducing H, apply ordinary Fourier interpolation to the vector(omega D²f,128Df,512f). Its L² norm is E, and its H¹ norm squared is at most2Q3²+16410 E² by |D omega|/omega<=4/5 and the product rule. Commuting J^s across omega costs at most34sE, as in the explicit Bessel-kernel estimate. The reverse comparison X_s(f)>=(1-34s)E(f) also uses only this weighted commutator and unweighted contraction, for0<s<1/34.

For a smooth nonzero exterior power r^q times a finite angular profile, E and Q3 are finite at infinity if q<-1. The L² component is decisive: integral r^(2q+1)dr converges exactly for q<-1. The weighted Hessian and third derivative have weaker thresholds q<1/5 and q<6/5. Thus this framework permits tails strictly between powers-2 and-1 that the baseline H component excludes. At q=-1 a logarithmic factor must be considered separately; no claim of membership is made there.

In the principal hierarchy p_n=1-n delta, canceling the first three residual sectors leaves p5=1-5delta<-1 for the case4 exponent. The potential then includes four stationary principal density branches. The first descendant gamma-2 is also below-1. Exact sector algebra and full remainder control are still required for a concrete candidate; this count is not a convergence theorem for an infinite asymptotic series. Conditions(A)-(D) and the residual bound must be certified anew for that candidate.

## Dependencies and audit status

The inputs from Analysis II are the exact first/second derivative energy identities of P7.5, the centrally odd weighted Riesz bound of P7.2, and the explicitly proved Bessel-kernel/product estimates of P8.1 and their component accounting in P8.4. Each use above shows that its first three rows do not require H. The additional analytic input is the independently audited exact gradient-structured Hilbert-Schmidt identity in ../gradient_commutator_audit/PROOF.md. State131's new seminorms were independently reproduced in ../background_norm_reproduction/.

This is a new T4 conditional theorem. It remains CLAIMED until an independent Opus theory lane checks the deletion of H, the maximal domains, the normalization step and the numerical parameter box. No candidate existence claim is implied by the framework alone.
