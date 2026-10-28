# Sharper compatible weighted inverse and nonlinear threshold

Status: independently audited, V081. Constants are sufficient bounds, not sharp optimal constants.

## 1. Exact setting and theorem

Use all spaces, parity, canonical inverses and background hypotheses of ROUGH_INVERSE_PROOF.md, with the same exact state131 or another reference independently satisfying those hypotheses. In particular

    R=2^35, w=(1+r2/R2)^(-11/10),
    E(h)^2=P2(h)^2+2^22 P1(h)^2+2^53 L(h)^2,
    P1=||<r>^-1/5 Dh||2, P2=||(1+4r2)^2/5 D2h||2,
    L(h)=||wh||Hdot^-1, N(h)=N_s^w(h)=E(J^s h).

For0<s<=2^-12 and k in N, the maximal-domain generator A_k=L_fix+U[k].D satisfies

    ||exp(t A_k)||_(N->N)
      <=exp[-t(1/20-2^23s-2^19N(k)/sqrt(s))].             (1)

Whenever this rate is positive the inverse is bijective with the reciprocal-rate bound. Set

    s=2^-30, r0=2^-41, eta=2^-46.                        (2)

Then on N(k)<=r0, the high rate is at least11/320>1/32, the low inverse is at most6, and the low contraction factor is3/1024. If c[k]=0, the inverse maps the forcing hyperplane f_y(0)=0 exactly onto c[h]=0. If the actual normalized reference residual has N(F)<=eta, there is a unique normalized correction h in the radius r0 ball, with F(rho+h;c)=0.

The actual state131 residual belongs to N, but N(F)>2^89 by the annular certificate V084. Thus its gap over eta is strictly greater than2^135. The earlier V079 pointwise bound remains a valid weaker check. No existence near the accepted state follows. The full leading angular function and exponent are fixed, with the same scaling exclusion as in ROUGH_INVERSE_PROOF.md.

## 2. Improved smooth commutator constant

The new ingredient is the direct negative-order estimate in SHARP_LOW_COMMUTATOR_PROOF.md. It replaces the radius conversion used in the earlier proof. The derivative components of that proof remain valid. From the V073 hierarchy,

    P0(H),P1(H)<=E(H)/2048, P2(H)<=E(H), H=J^s h.

In the top component, equations(14) of ROUGH_INVERSE_PROOF.md therefore give the coefficient

    [28*12+132*24+2*17*24*3+17*12*(9/5)*3]
      +[256*512*2+2*256*512*(3/2)*2]/2048
      +[256*16384*(8/3)*4]/2048
       =441164/15 <2^15.                                 (3)

For the first derivative component, its norm weight2048 cancels the bound on P0,P1, and the coefficient is

    28*12+132*24+17*24*2+17*12*(3/2)*2
       +256*256*(8/3)*4=2111948/3 <2^20.                 (4)

The direct low commutator norm is

    [(27/5)(312*12+5665*24)+(16/5)(1370*24)]
      +(13/2)*1370[(27/5)*12+256]
       =18581708/5.                                     (5)

Multiplying by the low norm weight2^(53/2) cancels against L(H)<=2^(-53/2)E(H); there is no large radius factor. The dilation term costs at most1644s in the low component and at most12s in each derivative component. Adding(3)-(5) and these three dilation costs gives less than2^23s E(H), proving the smooth loss in(1).

## 3. Rough loss, low inclusion and realization

The high derivative calculations(20)-(22) of ROUGH_INVERSE_PROOF.md use only the V077 multiplier estimate and remain valid for s<=2^-12. Their two coefficients are

    C_top=(14/5)2^11+2*2^15+(9/5)2^15,
    C_first=(11/5)2^11+2^15.

For the low component, write J^s(W.Dh)=W.DH+T_W H. The native transport form costs at most12d L(H)^2, where d=||DW||infinity<=2^11 N(k)/sqrt(s). The new direct commutator estimate(3) in SHARP_LOW_COMMUTATOR_PROOF.md adds at most(700416/5)(N(k)/sqrt(s))L(H)^2. Thus the total rough loss is bounded by

    [C_top+C_first+12*2^11+700416/5](N(k)/sqrt(s))E(H)^2
       =(1660928/5)(N(k)/sqrt(s))E(H)^2
       <2^19(N(k)/sqrt(s))E(H)^2.                         (6)

The earlier radius-dependent low inclusion estimate is replaced by L(J^-s H)<=6L(H). Hence L(h)<=6*2^(-53/2)N(h)<N(h). All other embeddings are unchanged.

The construction of the maximal high generator, smooth-velocity approximation in the common P0 topology, consistent low semigroups, and low domain inclusion for nonlinear differences is exactly the proof of section6 of ROUGH_INVERSE_PROOF.md, now with(1),(6) and the new low inclusion. That proof uses only these estimates and the same coefficient hypotheses; it does not require the older restriction s<=2^-96 once its radius-dependent commutator is replaced. Its inverse integral proves surjectivity, and strict decay proves injectivity.

### Item-by-item audit of the reused realization argument, V085

No step of section6 of ROUGH_INVERSE_PROOF.md requires s<=2^-96 after its estimates are replaced as above. The precise dependencies are as follows.

1. The onto isometry J^s:N->E and compact smooth approximation in N are proved for0<s<=1/2 in PROOF.md. The uniform gradient convergence of U[k_m] uses the same range. Neither assertion involves the low radius.
2. For each smooth velocity, conjugation gives a bounded perturbation of the E generator. The only s-dependent input is boundedness of the commutator. Sections2-3 above supply it for0<s<=2^-12. Bounds on higher derivatives of a particular smooth approximant may depend on that approximant; uniform semigroup bounds instead come from(1).
3. The common P0 transport realization uses global Lipschitz velocity, linear growth, the logarithmic derivative of omega0 and the fixed coupling bound16*(8/3). These are independent of s and R. The estimate for the approximating difference uses P1(h)<=2N(h), valid for0<s<=1/2. Gronwall, weak high compactness, the limsup norm argument and the semigroup law introduce no new smallness restriction.
4. The radial cutoff and local Friedrichs proof identifies the maximal distributional P0 domain using only linear growth and local Lipschitz continuity. If h and A_kh are in N, the P0 Duhamel identity equals the high semigroup identity; its high Bochner integral proves the asserted maximal high domain. This uses continuity of the embedding N into P0, with no radius-dependent conversion.
5. The high inverse integral requires the positive rate in(1), not any separately fixed upper bound on s. Strict decay gives injectivity, and the closed-generator integral identity gives surjectivity.
6. Low/P0 consistency uses parity Hardy for radial cutoffs, compact-core density in the intersection, convergence of the smooth flows in C1 on compact sets and uniform boundedness of the respective coupling Duhamel series. The new inclusion is L(h)<=6*2^(-53/2)N(h), valid for0<s<=2^-12. The positive high rate implies d<=2^11 N(k)/sqrt(s)<1/5120, so1/5-12d remains positive. Thus both inverse integrals converge and agree.
7. The nonlinear difference-domain step uses h in N and A_kh in L intersect P0. Its P0 integral identity, low/P0 consistency and strong continuity in L imply membership in the low generator domain. The extra forcing has its P0 bound from the Lipschitz velocity difference and its L bound from(26) of the earlier proof, which is valid for0<s<=1/2. No claim about arbitrary maximal distributional negative-order domains is needed.

The only old radius-dependent inclusion in these seven steps has therefore been explicitly replaced. The remaining domain construction is unchanged. All reference coefficient bounds and their state131 certificate sources are listed individually in REFERENCE_AUDIT.md (V082).

## 4. Nonlinear closure and all four output quantities

At(2), both smooth and rough losses equal1/128, giving11/320. Also d<=2^-15, so the low rate is at least8177/40960>1/6. The low bilinear estimate remains

    L(U[h].Dg)<=2^15 s^-1/2 N(g)L(h).

The high inverse32 maps the residual ball eta into the correction ball r0 because32eta=r0. The low Lipschitz factor is6*2^15 r0/sqrt(s)=3/1024. Completeness of the high ball in the low metric, weak continuity of c, the origin identity, and uniqueness are proved exactly as in section8 of the earlier theorem. The center slope stays positive since its change is at most2^-15.

With alpha=s/2, p0=8/s and kappa=p0+4, use the same adapted Holder norm C_ad and moment M as section9 of ROUGH_INVERSE_PROOF.md. Since s<=2^-12, their annular growth exponents remain below1/4, and

    L(h)+C_ad(h)+M(h)+|c[h]|
      <=2^18s^-3/2 N(h)<=2^23s^-3/2 N(A_kh).              (7)

Thus all parts of the requested estimate use the same space and realization. At(2), the last constant is2^68. This remains a sufficient theorem with a failed actual smallness test; no numerical residual proxy is substituted for N(F).

## General-rate qualification, V086

The four-output estimate with numerical inverse factor2^23 is asserted on the specified parameter ball (2), whose high inverse is at most32. For an arbitrary positive decay rate beta supplied by the general semigroup bound, the corresponding estimate is

    L(h)+C_ad(h)+M(h)+|c[h]|
             <=2^18 s^(-3/2) beta^(-1) N(A_k h).

No uniform bound on beta^(-1) is claimed when beta tends to zero. The embeddings themselves retain their stated constants.
