# One exceptional multiplicity in the auxiliary polynomial axis problem

Result 261. Written on 2026-10-21 before its symbolic checker. This is an independent reconstruction of the new lemma in the lead's frozen referee/x3h/PROOF.md, Section 5. The proof below also checks the degree 11 and 13 enumerations and the exact noninteger counterconfiguration of its Section 7. No finite elimination scan is assumed.

## Statement, notation and scope

Use the finite auxiliary axis class of result 258: C>0, P>1, a nonzero real polynomial H(w)=w^n h(w) with integer n>=1 and h(0)!=0, and a polynomial k(w). On a nonempty open interval of positive y, set y=Ct/(1-t^2)^P, w=1-t^2 and G=y H(w), and suppose a primitive V_y=k(w) obeys (c y+V)G_y=G. The parameter c is a real constant. These are auxiliary one-dimensional identities. They are not the full-plane IPM equation or its full-plane inverse.

Result 258 proves that P=n+m/2 for an odd m>=11. Set D=2P=m+2n, z=D/(D-1)>1, and e>=2. The critical-point reduction gives distinct finite nodes u_1,...,u_d, d=e+1, different from 0,-1,u_*=-1/D, and positive integer multiplicities mu_k. Nonreal nodes are paired with their conjugates with the same multiplicity. Let A=ord_0 Psi be positive and odd, and put

    m=A+2 sum_k mu_k,
    g(u)=A/u+sum_k 2 mu_k/(u-u_k),
    v_k=1/(1+u_k),  pi(v)=prod_k(v-v_k).

The numerator of g is m(1+u)^e(u-u_*). Its denominator is u prod_k(u-u_k). Thus its only finite zeros are -1 and u_*. In particular g(u_*)=0. Its moment and residue conditions are

    M_l=A+sum_k 2 mu_k v_k^l=0,  1<=l<=e,
    pi'(z)=0,
    M_(e+1) z=(-1)^e m prod_k v_k.

Each v_k is nonzero and differs from 1,z. Also 2e+3<=m. These conclusions, with their exact dependency hashes, are established in result 258. We use only these explicit consequences below.

If all mu_k equal a common mu except a unique node a of multiplicity nu!=mu, then nu>mu is impossible. If nu<mu, necessarily

    A=1 and mu-nu>n.

Consequently every odd m<=11 is excluded, so m>=13 and P>=15/2 in this finite polynomial class. At m=13 the only multiplicity pattern not excluded by these arguments is e=3, A=1, {mu_k}={2,2,1,1}. This surviving pattern is not asserted to exist.

There is, in contrast, an exact configuration of the residue and moment equations with m=107, e=2, A=1 and multiplicities (9,22,22), with a real parameter n=eta strictly between 1 and 1001/1000. Thus a blanket exclusion for all real n>=1 would be false for these algebraic conditions. This example does not have integer n and supplies no polynomial H or full-plane profile.

## Proof of the multiplicity lemma

The exceptional node a is real. Otherwise its distinct complex conjugate would be a second exceptional node of multiplicity nu.

We first locate every real v_k. There is no nonzero real pole u_k in (u_*,0) or (0,infinity). Indeed, select consecutive real poles between such a pole and the pole at 0. Since all residues are positive, g tends to positive infinity just to the right of the left pole and negative infinity just to the left of the right pole. Between them it is real and continuous, including the contributions from conjugate nonreal poles, and therefore has a zero. Neither interval contains -1 or u_*, the only allowed zeros. This is impossible. A real u_k is consequently less than u_*. Since u_k!=-1, its transformed node is either negative, when u_k<-1, or greater than z, when -1<u_k<u_*. Hence a belongs to (-infinity,0) union (z,infinity).

Substituting u_*=1/z-1 into g(u_*)=0 and using m=A+2 sum mu_k gives

    A/(z-1)+2 sum_k mu_k/(z-v_k)=m/z.

Since pi'(z)=0 and pi(z)!=0, sum_k 1/(z-v_k)=0. With one exceptional multiplicity, the preceding equation becomes

    A/(z-1)+2(nu-mu)/(z-a)=m/z.

Let T=AD-m=(A-1)m+2An>=2n>0. Because z/(z-1)=D, the equation gives the exact identity

    a=z(1+2(nu-mu)/T).                                    (1)

All divisions here are by nonzero quantities: z, z-1, z-a and T.

Suppose nu>mu. Then a>z>0. The moment equations say

    sum_k v_k^l=-A/(2mu)-(nu-mu)a^l/mu,  1<=l<=e.

The formal series identity log prod(1-v_k t)=-sum_{l>=1}(sum_k v_k^l)t^l/l therefore gives

    prod_k(1-v_k t)
      =(1-t)^(-A/(2mu))(1-a t)^(-(nu-mu)/mu)+O(t^(e+1)).  (2)

This is an equality of coefficients through degree e; no convergence of an infinite series at t=1 or at any other point is used. Both factors have strictly positive coefficients, since their exponents are negative and A,mu,nu-mu,a are positive. Write the coefficients of the polynomial on the left as c_j, j=0,...,d. Then c_0,...,c_e>0. The identity pi(v)=sum_{j=0}^d c_j v^(d-j), with d=e+1, gives pi'(z)>0, a contradiction.

Suppose nu<mu. Equation (1) yields a<z. The real-node restriction forces a<0, so T<2(mu-nu). If A>=3, then T>=2m+6n. But mu-nu<mu<m/2, where the last inequality follows from m=A+2 sum mu_k and the presence of the common multiplicity. Hence T>2(mu-nu), a contradiction. Thus A=1. Now T=2n, giving mu-nu>n as claimed.

The source proof's display corresponding to (2) omits the plus sign before O(t^(e+1)). We have repaired that typographical omission explicitly. A product by O(t^(e+1)) would be false already in its constant term.

## Complete low-degree enumeration

For each odd m, choose e>=2 with 2e+3<=m, odd A>=1, and an unordered partition of (m-A)/2 into e+1 positive integers. These are all possible multiplicity data, since they list exactly all ways to account for the degree m. Equal multiplicities are excluded by result 258.

At m=11 the complete unequal list is

| e | A | multiplicities | exclusion |
| --- | --- | --- | --- |
| 2 | 1 | 3,1,1 | unique higher multiplicity |
| 2 | 1 | 2,2,1 | unique lower multiplicity, difference 1<=n |
| 2 | 3 | 2,1,1 | unique higher multiplicity |
| 3 | 1 | 2,1,1,1 | unique higher multiplicity |

This also includes the last pattern omitted from the lead's earlier enumeration. Result 258 already excludes m<=9. Thus m>=13, and P=n+m/2>=15/2.

At m=13 the complete unequal list is

| e | A | multiplicities | exclusion or remaining status |
| --- | --- | --- | --- |
| 2 | 1 | 4,1,1 | unique higher |
| 2 | 1 | 3,2,1 | all three nodes real, impossible by M_2>0 |
| 2 | 3 | 3,1,1 | unique higher |
| 2 | 3 | 2,2,1 | unique lower with difference 1<=n |
| 2 | 5 | 2,1,1 | unique higher |
| 3 | 1 | 3,1,1,1 | unique higher |
| 3 | 1 | 2,2,1,1 | OPEN under these arguments |
| 3 | 3 | 2,1,1,1 | unique higher |
| 4 | 1 | 2,1,1,1,1 | unique higher |

When all three multiplicities differ, each node must be real, since a nonreal node requires a conjugate of the same multiplicity. Then M_2=A+sum 2mu_k v_k^2>0, contradicting M_2=0. The tables omit only equal-multiplicity cases already excluded. A separate exact partition enumeration checks completeness, including those omitted equal cases. No m>=13 elimination scan is adopted here.

## Exact noninteger counterconfiguration

Let eta be the positive root of

    f(t)=749t^4+88168t^3+2994312t^2+22061260t-25153453.

For t>=0 the derivative is strictly positive. Direct rational evaluation gives f(1)=-8964 and f(1001/1000)=19356647401164749/10^12>0. The intermediate value theorem and strict monotonicity therefore give a unique positive root and locate it strictly between these rational endpoints. In particular eta is not an integer.

Set D=107+2eta, z=D/(D-1), and

    a=z(1-13/eta),
    b=-(1+18a)/88,
    c2=b^2+(1+18a^2)/88,
    v_1=a, v_2=b+i sqrt(c2), v_3=b-i sqrt(c2).

The weights are A=1 and 2mu=(18,44,44), so m=107. Since a<0 and c2>0, the nodes are distinct and nonzero, and none equals 1 or z. They respect conjugation. The definitions give M_1=M_2=0 directly.

For pi(v)=(v-a)((v-b)^2+c2), direct rational algebra gives

    pi'(z)=9 f(eta)/(3872 eta^2(eta+53)^2)=0.              (3)

Also z/(z-a)=eta/13. The weighted sum at z is therefore

    1/(z-1)+44 pi'(z)/pi(z)-26/(z-a)
      =(D-2eta)/z=107/z.

This is precisely the transformed equation g(u_*)=0. It also gives M_3 z=107 v_1 v_2 v_3 using the established rational moment formula. The checker verifies this last identity directly modulo f, without invoking that implication a second time.

Put u_k=1/v_k-1. These nodes are finite and distinct, with none equal to 0,-1,-1/D. The real odd polynomial

    Psi(x)=x(x^2-u_1)^9(x^2-u_2)^22(x^2-u_3)^22

has degree 107 and is nonzero at x=+i and x=-i. Its logarithmic derivative is x g(x^2), with positive residues as specified. The first two vanishing moments give a double zero of g at u=-1 and (3) gives the other zero at u=-1/D. The denominator has degree four and the numerator has degree three with leading coefficient 107. The numerator is thus exactly 107(1+u)^2(u+1/D), proving

    Psi'/Psi=107(1+x^2)^2(x^2+1/D)
               /[x prod_k(x^2-u_k)].

This identity is checked without expanding a degree-107 polynomial: sum the three rational partial fractions using the real quadratic for the conjugate pair, clear its known nonzero denominators, and reduce the coefficient numerators modulo f. Exact small JSON inputs specify f and its isolating interval.

Finally eta>1 gives D>109 and hence 1<z<109/108. The counterconfiguration lies strictly inside the continuous parameter interval used in the small-degree arguments. It is compatible with the lemma's necessary gap, 22-9=13>eta. It is not compatible with integer n. It supplies no claimed polynomial H, full-plane inverse, or IPM profile.

## Verification and remaining gaps

The proof precedes its checker. The checker independently derives the weighted identity, (1), formal coefficients, exact partition lists, (3), the extra moment, and the rational logarithmic derivative. Source files and the result 258 gates are frozen with SHA256 hashes. The lead, whose actual model is Claude Opus 5.5, separately hand-checked the proposed lemma before this reconstruction. A direct follow-up review will be recorded with its actual provider model if one is obtained; it is not assumed here.

The conclusion is only a necessary condition in a finite auxiliary class. Odd degrees at least 13, nonpolynomial H, limiting sequences, and the full Setting III problem remain OPEN. These results cannot authorize a NO endpoint or an early finish.
