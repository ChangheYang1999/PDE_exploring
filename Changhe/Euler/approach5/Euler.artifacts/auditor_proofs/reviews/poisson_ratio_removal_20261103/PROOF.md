# Pressure-based removal at natural tail regularity

## 1. Exact local and global theorems

Fix 2/5<c<1/2 and put

    eta=(1-2c)/(2-2c), rho=1/2-eta=c/[2(1-c)],
    gamma=2rho=c/(1-c), theta0=1/rho-2=2/c-4.

Thus 1/3<rho<1/2, 2/3<gamma<1 and 0<theta0<1. Let theta0<alpha<1. On an open G in R3 suppose V is locally C^(1,alpha), P is continuous and

    Delta P=-tr((DV)^2) in distributions,
    E=|V|^2, S=P-E/2,
    r_-|S|<=E<=r_+|S|.                              (1)

The comparison constants satisfy0<r_-<=r_+<infinity on each relatively compact neighborhood where the assertion is made. Define beta=|S|^(-eta)V on S!=0 and beta=0 on S=0. Then beta is continuous and locally W^(1,t) for every1<=t<1/(1-rho). Its weak derivative is zero almost everywhere on S=0. Therefore zero classical curl off S=0 extends to zero distributional curl on G, with no assumption on the zero set.

For the global consequence take G=D=R3 minus{0}, omega any finite real number, Jx=e_3 cross x, A=cI-omega J, X=Ax, L=(1-c)I+omega J and W=curl V. Assume additionally

    div V=0, DV X=-LV, X.grad S=-2(1-c)S,
    X.V=0, W.grad S=0,                              (2)

and assume fixed constants in(1) on the unit sphere. Then V=S=P=0 on D. The pressure in(1) is the actual scalar used to define S; it cannot be shifted arbitrarily while preserving these premises. This is a conditional global result, not a local continuation theorem from bounded ratios alone.

## 2. Pressure regularity and exact root inputs

The source tr((DV)^2) is locally C^alpha. Interior Poisson Schauder regularity gives P locally C^(2,alpha). One may localize its Holder source, form a Newtonian potential, and apply harmonic distribution regularity to the difference from P on a smaller ball. These are named external elliptic inputs. In particular S is C^(1,alpha) and

    DS=DP-(DV)^T V,
    |P|<=|S|+E/2<=(1/r_-+1/2)E.                     (3)

P can vanish where E>0; no lower bound on |P| is asserted.

The scalar input is the actual Ghisi-Gobbino arXiv1107.2694v2 Theorem2.3. Its statement and complete printed15-16 slicing proof were reread in the retained primary text, together with the A1541 reconstruction. For 0<sigma<1, a real f in C^(k,delta), with k>=1, 0<delta<=1 and k+delta=1/sigma, has continuous signed root sign(f)|f|^sigma with weak gradient locally in weak L^(1/(1-sigma)). The theorem gives strong L^t for every strictly smaller exponent. The erroneous last displayed exponent in the slicing proof is not used; its correct exponent is in the theorem statement and follows from(3.24).

Apply the theorem to P with sigma=rho. Its needed regularity is C^(2,theta0), which P has on compact smaller sets. Apply it to each V_i with sigma=gamma. Its needed regularity is C^(1,theta1), where theta1=1/gamma-1=theta0/2<alpha. Thus, assigning zero on the relevant zero sets,

    H_P=|P|^(rho-1)|DP|, H_i=|V_i|^(gamma-1)|DV_i|

belong locally to L^t for t<1/(1-rho); the H_i also have the larger exponent range t<1/(1-gamma). The chain rule off zeros and the Sobolev level-set property identify these quantities with absolute root derivatives up to fixed factors. No root theorem is applied to S, whose available regularity is lower.

## 3. Uniform estimates through both kinds of zero

For epsilon>0 define beta_e=(S^2+epsilon^2)^(-eta/2)V. This is C1. On S!=0, direct differentiation gives

    |D beta_e|<=|S|^(-eta)|DV|
                  +eta |S|^(-eta-1)|V||DS|
               <=C E^(-eta)|DV|+C E^(rho-1)|DP|.     (4)

The second inequality uses both sides of the comparison and(3). The contribution of (DV)^T V is C E^(-eta)|DV|, and -eta-1/2=rho-1. Since E^(-eta)=|V|^(gamma-1), the negative exponent gives

    E^(-eta)|DV|<=sum_i |V_i|^(gamma-1)|DV_i|

almost everywhere: it holds componentwise wherever V_i!=0, while DV_i=0 almost everywhere on its zero level set.

Set C0=1/r_-+1/2. Where P!=0, (3) and rho-1<0 give

    E^(rho-1)|DP|<=C0^(1-rho)|P|^(rho-1)|DP|.

Where P=0 and E>0, DP=0 almost everywhere on that level set, so the same bound with H_P=0 remains valid almost everywhere. At S=0, comparison gives V=0 and DV=0 almost everywhere; the other exact regularized derivative term contains S V and is zero there. Therefore, on the full neighborhood,

    |D beta_e|<=C(sum_i H_i+H_P)                    (5)

almost everywhere, independently of epsilon. No negative power is evaluated at a zero before this level-set argument is applied.

Also |beta|<=sqrt(r_+)|S|^rho. Thus beta is continuous, including every zero. Splitting |S|<=epsilon and |S|>epsilon proves uniform local convergence beta_e->beta with error C epsilon^rho. In the latter region use1-(1+epsilon^2/S^2)^(-eta/2)<=C epsilon^2/S^2; in the former both terms are bounded by C epsilon^rho.

For1<t<1/(1-rho), (5) and weak compactness identify beta as a local W1,t field. Finite local measure gives t=1. Its weak derivative is zero almost everywhere on S=0 by the Sobolev level-set property, componentwise. Off that set it is the classical derivative. This proves the full local theorem and removal of classical closedness, including arbitrary scalar sign changes and arbitrary zero sets.

## 4. Global closedness, exactness and the maximum

The complete linear flow F_t=exp(tA) obeys |F_t x|=exp(ct)|x|. Integrating(2) gives

    V(F_t x)=exp(-(1-c)t)exp(-omega tJ)V(x),
    S(F_t x)=exp(-2(1-c)t)S(x).

The sphere comparison thus holds everywhere on D. Put a=1-2c and b=2-2c. For k=X.V, direct differentiation gives grad k=X cross W-aV. Since k=0,

    X cross W=aV,
    grad S cross V=(b/a)S W,

where the second formula uses W.grad S=0 and X.grad S=-bS in the triple-product identity. Since eta=a/b, these give curl beta=0 on S!=0. Section3 extends this to D in distributions.

A continuous distributionally closed form has local C1 primitives: mollify on balls, integrate the smooth closed forms and pass uniformly after fixing additive constants. As D is simply connected, the local primitives join to a global C1 function phi with grad phi=beta. There is no remaining period hypothesis.

The contraction gives X.grad phi=0 everywhere, including S=0. Every complete linear orbit crosses the unit sphere exactly once, so the maximum M of phi on that compact sphere is a global maximum on D attained at an interior point. No completeness of the V or W characteristic flow is used.

## 5. The physical-space weak equation and Harnack

Set m=1/c and tau=(m-2)/2=eta/gamma. On S!=0 put R=E/|S|. Algebra gives

    |grad phi|^2=R|S|^gamma,
    V=q|grad phi|^(m-2)grad phi, q=R^(-tau),
    0<r_+^(-tau)<=q<=r_-^(-tau)<infinity.             (6)

Give q the value r_+^(-tau) on S=0. Both vector sides are zero there, so (6) holds on the full domain. Since div V=0,

    div(q|grad phi|^(m-2)grad phi)=0                 (7)

in distributions on D. The potential is C1 and hence Wloc^(1,m). No derivative of q, interface integral or deleted-domain limit occurs.

Here2<m<5/2<3. The actual Serrin1964 Theorem5 gives local Harnack for nonnegative weak solutions of(7). The structural mapping is rechecked here against the complete source audit in A1822-A1826; that earlier audit read the full Theorem5 proof. Divide the flux by lambda=r_+^(-tau); A=(q/lambda)|p|^(m-2)p satisfies |A|<=(sup q/lambda)|p|^(m-1), p.A>=|p|^m, and all lower-order terms in structural condition(6) are zero. Thus the additive Harnack constant is zero. The bounded measurable coefficient is allowed; continuity or differentiability of q is not required.

Apply this to u=M-phi. It is nonnegative and solves the same weak equation by oddness of the flux. Harnack on compactly contained balls makes the nonempty zero set of u open. Continuity makes it closed; D is connected. Hence u=0 throughout D. Equation(6) gives V=0, the lower comparison gives S=0, and P=S+E/2 gives P=0. This completes the global theorem for every finite omega.

## 6. Actual natural tails and the countertest distinction

For the actual-profile application retain a full whole-space C2 velocity/C1 pressure rotating profile in the target c interval and the explicit natural bounds

    |U(y)|<=C(1+|y|)^(-p), |DU(y)|<=C(1+|y|)^(-p-1),
    p=(1-c)/c.

The complete A538 proof was reread: local physical Euler estimates give uniform W2,q bounds on compact sets avoiding0, for every finite q>3, hence V in C^(1,alpha)loc for every alpha<1. The alternative A533 and the A539 pressure regularity are consistent with this. The tail pressure P2 is defined after subtracting the finite profile pressure limit, satisfies Poisson, and has the required scalar homogeneity. For globally zero-helicity profiles A531 supplies W.grad S=0. Because S is C1 here, its earlier distributional transport identity is also a pointwise identity.

Therefore this theorem needs no extra C2 velocity-tail or C3 scalar-tail premise beyond those natural full-profile hypotheses, once global k=0 and the global positive finite comparison are separately supplied. This statement concludes V=S=P2=0. Passing from V=0 to U=0 additionally uses a faithful-tail theorem with its exact hypotheses; no such passage is implicit here.

LIT266 does not contradict the local theorem. For its shear tr((DV)^2)=0, whereas P=S+E/2 is a nonzero flat function of x alone and is not affine. Thus Delta P=P'' is not identically zero. Its prescribed scalar fails precisely the Poisson premise used to obtain the smoother pressure root. Its other missing tail equations were separately checked in A1845.

## 7. Audit verdict and limits

LIT267's local pressure-based removal and conditional global rigidity are CONFIRMED. Both the lower and upper scalar comparisons are retained, as are global k=0 and the actual Poisson equation. None follows here from bare decay. The theorem is not a local strong-continuation conclusion from merely bounded ratios: it uses a global maximum obtained from the compact sphere and the complete linear spiral flow.

All seven submitted and independent sections were read. The actual root statement and slicing proof, the complete natural-tail regularity proof and the complete earlier global bounded-ratio proof were compared. External scalar-root, elliptic, Harnack and basic Sobolev inputs are explicitly named. No computation, formal build or new client was needed. The full arbitrary-helicity bare-decay conjecture and missing local ratio-energy control remain OPEN.
