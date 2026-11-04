# Positive-pressure orbit arcs of arbitrary finite vanishing order

Independent audit of Theory Agent C C59 and LIT285. C59 is the order-two instance; LIT285 additionally specifies the exact vorticity order and permits every finite order. All statements below concern the reduced local tail system, not a whole-space Euler profile.

## 1. Exact statement and local system

Fix 2/5<c<1/2, omega in R and an integer N>=2. Put

    Jx=e3 cross x, A=cI-omega J, X=Ax,
    L=(1-c)I+omega J, a=1-2c, b=2(1-c),
    q=b/a, eta=a/b>0.

There exist an open neighborhood G of e1, whose closure avoids the origin and rotation axis, and real-analytic V,P on G. Set W=curl V, E=|V|^2, k=X.V and S=P-E/2. They satisfy

    div V=0, V.W=0, X.grad V=-LV,
    -Delta P=tr((DV)^2), grad k=X cross W-aV,
    X.grad S=-bS, W.grad S=0,
    k grad S=qS grad k on supp W.                       (1)

All topology is relative to G. We can choose G so that k=0 and S>0 throughout it, P(e1)=S(e1)=1, and, for

    Gamma=G intersect{exp(tA)e1:t in R},
    Y={W!=0} intersect int{k=0},
    Fplus=(closure Y intersect{S>0}) minus Y,

one has

    {V=0}={W=0}=Fplus=Gamma,
    supp W=G, Y=G minus Gamma,

where Gamma is a single orbit arc and G minus Gamma is connected. At each z in Gamma,

    D^j V(z)=D^j W(z)=0 for 0<=j<N,
    D^N V(z)!=0, D^N W(z)!=0.                           (2)

The five pointwise laws stated in Section 6 hold everywhere. For N=2 this proves every assertion of C59 and also D^2W!=0 on its arc. The neighborhood and constants may depend on c,omega,N.

## 2. An analytic ansatz and the exact remaining equations

For x near e1 define

    r=|x|, pi(x)=exp((omega/c)log r J)x/r,
    u=pi_2(x), v=pi_3(x).

The map pi is constant along the linear X-flow, since exp(tA)=e^(ct)exp(-omega t J). At e1 the gradients of u,v,r are respectively g=(omega/c,1,0), e3 and e1. The determinant of this three-row matrix is one, so Theta=(u,v,r) is an analytic local coordinate map. The first component of pi is positive after shrinking.

For analytic phit,Ht in the two transverse coordinates, with Ht>0, set

    phi=phit(u,v), H=r^(-b/c)Ht(u,v),
    V=H^eta grad phi, S=H, P=H+|V|^2/2.                 (3)

Then X.grad phi=0 and X.grad H=-bH. Consequently k=0,

    W=eta H^(eta-1)grad H cross grad phi,                (4)

V.W=W.grad S=0 and X.grad S=-bS. Differentiating the invariant phi gives X.grad grad phi=-A^T grad phi. Since eta b=a, (3) implies X.grad V=-(aI+A^T)V=-LV. Also

    grad(X.V)-X cross curl V=A^T V+X.grad V=-aV.

This proves the contraction identity in (1). The last rank identity is zero on both sides. Because X.grad H=-bH!=0 and X.grad phi=0, a nonzero grad phi cannot be parallel to grad H. Hence

    W=0 if and only if grad phi=0 if and only if V=0.    (5)

The only unsatisfied equations are divergence and Poisson. Put

    E1=H^eta(Delta phi+eta grad(log H).grad phi),
    F0=H^(-eta)E1, H2=H^(2eta), E2=Delta P+tr((DV)^2).

The product rule and the Euclidean Bochner identity give exactly

    E2=E2s+H2 grad phi.grad F0,
    E2s=Delta H+(1/2)|grad phi|^2 Delta H2
         +2grad H2.(D^2phi grad phi)+H2|D^2phi|^2
         -eta H2 grad phi.grad(grad(log H).grad phi)
         +tr((DV)^2).                                  (6)

For verification, the only third derivative term from Delta(|V|^2/2) is H2 grad phi.grad Delta phi. Substituting Delta phi=F0-eta grad(log H).grad phi yields (6). All remaining derivatives have order at most two. The expression is affine in D^2H, since DV=H^eta D^2phi+grad phi tensor grad(H^eta) contains only first derivatives of H.

Restrict E1 and E2s to r=1. Their coefficients are analytic in the transverse coordinates and allowed jets. The coefficient of phit_vv in E1 is H^eta|grad v|^2>0. Solving it for phit_vv introduces no second derivatives of Ht. After this substitution the coefficient of Ht_vv in E2s is |grad v|^2+O(|grad phi|^2), and equals one at e1 when Ht=1 and grad phit=0. Thus the analytic implicit equation can also be solved for Ht_vv. This is a noncharacteristic second-order Cauchy-Kovalevskaya system.

Choose the analytic Cauchy data

    phit(u,0)=u^(N+1)/(N+1), phit_v(u,0)=0,
    Ht(u,0)=1, Ht_v(u,0)=0.                            (7)

Cauchy-Kovalevskaya gives a convergent real-analytic solution near (0,0). Positivity of Ht persists on a smaller neighborhood. E1 and E2s have respective homogeneity weights one and two along X: each derivative contributes c, each factor H^s contributes sb, and a+2c=1, b+2c=2. Their vanishing on r=1 therefore propagates along the flow to a full neighborhood. There E1=E2s=0, and (6) gives E2=0. This completes every equation in (1). The sign of Delta H here is positive; the negative-pressure C57 construction has the opposite sign, whose nonzero coefficient was checked separately in the earlier audit.

## 3. The first nonzero term is forced by the divergence equation

Fix the analytic H just obtained. Dividing E1=0 by H^eta leaves a linear homogeneous second-order equation for phit with analytic coefficients and no zeroth-order term. At (0,0) its principal part is

    s partial_uu+partial_vv,  s=|g|^2=1+(omega/c)^2>=1.  (8)

The constant and first-degree terms of phit vanish by (7). Suppose all homogeneous terms below degree d vanish. At degree d-2 in the equation, only the constant principal coefficients acting on the degree-d term Pd survive. Variable principal coefficients and first-order terms involve already vanishing lower terms at this degree. Hence Pd solves (8).

Write Pd=sum_(j=0)^d p_j u^(d-j)v^j. Its coefficients satisfy

    (j+2)(j+1)p_(j+2)=-s(d-j)(d-j-1)p_j.

The two Cauchy traces determine p_0,p_1 and then every coefficient. For d<=N both initial coefficients are zero, so Pd=0. At d=N+1 the data give

    P_(N+1)(u,v)=Re((u+i sqrt(s)v)^(N+1))/(N+1),
    phit=P_(N+1)+O(|(u,v)|^(N+2)).                     (9)

Thus this is the actual first nonzero term of the convergent solution. If zeta=u+i sqrt(s)v, then

    partial_u P_(N+1)=Re zeta^N,
    partial_v P_(N+1)=-sqrt(s) Im zeta^N,
    |grad P_(N+1)|^2
       =(Re zeta^N)^2+s(Im zeta^N)^2
       >=|zeta|^(2N)>=(u^2+v^2)^N.                    (10)

The gradient of the analytic remainder is O(|(u,v)|^(N+1)). Equations (9)-(10) therefore give |grad phit(w)|>=|w|^N-C|w|^(N+1)>0 for every sufficiently small nonzero w. The sole transverse critical point is zero.

For N=2, (9) reads phit=u^3/3-suv^2+O(|w|^4), exactly C59's cubic. Directly,

    |grad P3|^2-(u^2+v^2)^2
      =(s^2-1)v^4+2(2s+1)(s-1)u^2v^2>=0.

The general argument both recovers and checks the stated isolation estimate.

## 4. The complete zero set and support

Choose a small square Q about zero and an interval I about r=1 such that the analytic solution, coordinate inverse and preceding strict estimate hold on a neighborhood of their product closure. Let G=Theta^(-1)(Q times I). Shrink further to avoid the rotation axis. Independence of grad u and grad v gives grad phi=0 exactly when grad phit=0, hence exactly on {u=v=0}.

In this chart u=v=0 means pi=e1. Solving for x gives

    x=r exp(-(omega/c)log r J)e1=exp(tA)e1,
    t=(log r)/c.

Since r ranges over one interval and c>0, this is precisely one orbit arc Gamma. It lies in x3=0 and remains a positive distance from the axis. It is a logarithmic spiral for omega!=0 and a radial segment for omega=0.

Equation (5) identifies both zero sets with Gamma. The complement is diffeomorphic to (Q minus{0}) times I, which is connected and dense. Therefore supp W=G, Y=G minus Gamma and closure Y=G. Since S=H>0, Fplus=Gamma. At e1, H=1 and V=0, proving P(e1)=S(e1)=1.

## 5. Exact velocity and vorticity orders on the entire arc

At every z in Gamma, the same transverse point (u,v)=(0,0) is used. All derivatives of phit through order N vanish there. The chain rule gives D^j grad phi(z)=0 for j<N. At the next order, for M_z h=(grad u(z).h,grad v(z).h),

    D^(N+1)phi(z)[h,...,h]=(N+1)!P_(N+1)(M_z h).         (11)

The map M_z is onto R^2 and P_(N+1) is a nonzero polynomial, so D^N grad phi(z)!=0. Product differentiation of (3) shows D^j V(z)=0 for j<N and D^N V(z)=H(z)^eta D^N grad phi(z)!=0.

Differentiating (4) shows that all derivatives of W below order N vanish, and

    D^N W(z)=eta H(z)^(eta-1)
               grad H(z) cross D^N grad phi(z).          (12)

Every output vector of the last tensor lies in X(z)^perp. Indeed, differentiate X.grad phi=0 N times: terms involving derivatives of X contain a lower derivative of grad phi and vanish. The linear map p maps to grad H(z) cross p is injective on X(z)^perp, because grad H(z).X(z)=-bH(z)!=0. Thus the nonzero tensor in (11) remains nonzero in (12). This proves both exact orders in (2). In particular taking curl does not lower the first nonzero order in this special ansatz.

## 6. All five pointwise laws are satisfied

The laws checked are precisely the following implications.

1. If z is in supp W and V(z)=W(z)=0, then S(z)>=0; if additionally DW(z)!=0, then S(z)=0.
2. If V=W=0 and DW!=0 at z, then DV(z)=0 and DW(z)=X(z) tensor ell for a nonzero covector ell with ell(X(z))=0.
3. At every zero of W, DW is nilpotent.
4. At a common zero of V,W in int{k=0}, DV=0.
5. If z is in supp W, W(z)=0 and range DW(z) is contained in R X(z), then k(z)<=0 and S(z)>=0 when k(z)=0. If z is in supp W, W(z)=0 and either k(z)>0 or k(z)=0,S(z)<0, then V(z)!=0 and DW(z) has rank one.

Off Gamma the zero premises fail. On Gamma, V=W=DV=DW=0, k=0 and S>0, since N>=2. Thus the sign, nilpotence, zero-derivative and nonpositive-contraction conclusions hold. Every premise involving DW!=0, positive k or negative S fails. This verifies all five laws at every point, without using them to construct the solution.

## 7. Consequences and precise limits

C59's off-axis Fplus alternative is realized by (1) together with all five laws. The implication that these inputs alone exclude Fplus is therefore false. Given any fixed finite integer M, choose N>M. The same construction also satisfies vanishing of every velocity and vorticity derivative through order M on Gamma. Consequently adding that finite vanishing requirement still cannot exclude this local alternative.

This does not refute restrictions on a specified nonzero higher jet, infinite-order conditions, additional original-profile transport information, or global matching conditions. The analytic functions here are nontrivial and have a specified finite order. There is no analytic infinite-flatness example, no uniform domain in N, no passage to an N=infinity limit, and no globally decaying Euler profile. The pressure equation in (1) is enforced exactly, but the full original-profile momentum equation is not part of this local construction.

C59 Remark 1 calls X nonradial on the constructed arc without qualifying omega. That is true only for omega!=0. For omega=0, X=cx is radial everywhere. Its main theorem has the correct orbit formula and is unaffected. LIT285 explicitly states both cases correctly. The heuristic discussion of higher-jet conjugation in C59 is not needed for the theorem or included as a general obstruction verdict.

## 8. Dependencies and verification

The full C59 and LIT285 sources, every construction step of C57(c), the earlier positive-sign C58 audit, and the complete independent the literature agent review of C59 were read. The Cauchy reduction, induction, isolation bound, topology, tensor injectivity and law-by-law implications were checked directly above. No source numerical script was executed. The earlier confirmations of the analytic reduction are A1927-A1928 and A2016; the present proof spells out its equations and verifies the changed data.

The only external classical tools are the analytic inverse function theorem, Cauchy-Kovalevskaya for the explicitly noncharacteristic analytic system, and Taylor's theorem. There is no global flow-completeness claim or boundary integral in this local argument. Every real finite omega is covered; bounds and neighborhoods can depend on it. Source hashes and a final reading record accompany this proof. No new computation or formal build is required.
