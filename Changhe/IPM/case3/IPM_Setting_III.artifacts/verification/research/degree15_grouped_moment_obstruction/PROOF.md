# Degree15: complete grouped-moment obstruction

Result267. The initial reduction was written before exploratory code on2026-10-21 and is retained as INITIAL_REDUCTION.md. This complete informal proof, including the exact certificate argument, precedes its independent checker. Its status is pending until all stated finite arithmetic equalities pass. It uses only the independently established residue system258 and multiplicity lemma261; no producer elimination code is read or imported. The lead has proposed the same four patterns, but their enumeration and exclusion must be recomputed.

Let n>=1 be an integer, m=15, D=15+2n and z=D/(D-1). The transformed nodes are distinct, nonzero and different from1,z; conjugation preserves their integer multiplicities. A0 is positive odd, d=e+1 with e>=2, and m=A0+2 sum mu_j. They satisfy M_l=A0+sum 2mu_j v_j^l=0 for1<=l<=e, pi'(z)=0 and
 A0/(z-1)+sum 2mu_j/(z-v_j)=m/z.
Here pi(v)=product(v-v_j), and its derivative is with respect to v. Equal multiplicities are impossible. A unique higher multiplicity is impossible; a unique lower multiplicity nu below the common mu forces A0=1, mu-nu>n and the exceptional real node a=z(1+(nu-mu)/n). For e=2, either one conjugate pair shares a multiplicity or all nodes are real. The latter gives M2>0, impossible. Enumerating the positive unordered partitions leaves only:
 (i) e2,A0=1,(1,3,3);
 (ii) e3,A0=3,(2,2,1,1);
 (iii) e3,A0=1,(3,2,1,1);
 (iv) e4,A0=1,(2,2,1,1,1).
These conditions are necessary only for the finite auxiliary polynomial axis problem, not for every full-plane IPM field.

Case(i). The multiplicity gap gives n<2, hence n=1 for integer n. Then z=17/16 and the unique weight2 node is a=-17/16. Write the weight6 pair polynomial W(v)=v^2-hv+j. Moments M1=M2=0 give h=3/16 and j=37/128. Direct differentiation of (v-a)W(v) at z gives683/128>0, contrary to pi'(z)=0.

There is also a stronger real-parameter exclusion. For real n>=1, the exceptional-node identity and the first two moments give
 a=z(1-2/n), h=-(1+2a)/6, j=(1+2a^2+6h^2)/12.
Direct polynomial expansion yields
 pi'(z)=(15n^4+250n^3+1227n^2+1440n-200)/(8n^2(n+7)^2).
The numerator is at least15+250+1227+1440-200=2732>0 for n>=1. Thus this necessary pattern is impossible throughout that real range. The certificate checks the expansion by clearing its stated denominators with integer polynomial arithmetic.

Case(ii), with a useful second check for degree13. More generally let A0=A be1 or3, let m=A+12 and z=(m+2n)/(m+2n-1). Put U(v)=v^2-pv+q for the two weight4 nodes and W(v)=v^2-hv+j for the weight2 pair. Both polynomials have real coefficients. The two logarithmic derivative equations give U'(z)/U(z)=-lambda/z, W'(z)/W(z)=lambda/z where lambda=(A(m+2n)-m)/2>0. Their nonzero denominators follow from z differing from every node. Thus
 q=((lambda+1)pz-(lambda+2)z^2)/lambda,
 h=-A/2-2p,
 j=((2-lambda)z^2+(lambda-1)hz)/lambda.
Multiplying M2=0 by lambda gives the real quadratic
 12lambda p^2+(4A lambda-16z)p+lambda(A+A^2/2)+(12lambda+8)z^2+2A(lambda-1)z=0.
Its discriminant is exactly
 Delta=-8A^2 lambda^2-48A lambda^2-96A lambda^2 z-32A lambda z
       -576lambda^2 z^2+(256-384lambda)z^2.
Here A>0,z>0 and lambda>=1: for A=1,lambda=n; for A=3,lambda=15+3n. Every displayed term is strictly negative except that the last is a single combined term, which is also strictly negative since256-384lambda<0. Hence Delta<0, and no real p exists. This proof uses only M1,M2 and the two derivative equations. It independently rechecks the degree13 pattern and proves the degree15 case(ii). The simplified discriminant argument was proposed in the actual Claude Opus5.5 review and is verified coefficient by coefficient in the independent checker.

Case(iii). Let a be the weight6 node and b the weight4 node, each real, and W(v)=v^2-hv+j the weight2 pair. Define t=z/(z-a) and s=z/(z-b). Both are finite and nonzero. The derivative equations imply 2t+s=-n. Hence s=-n-2t, a=z(1-1/t) and b=z(1-1/s); all divisions are permitted because t and s are nonzero. The first moments give
 h=-1/2-3a-2b,
 j=(1+6a^2+4b^2+2h^2)/4.
With pi=(v-a)(v-b)W, pi'(z)=0 is equivalent to
 z W'(z)+(t+s)W(z)=0,
since W(z)!=0. The remaining moment is
 M3=1+6a^3+4b^3+2(h^3-3hj)=0.
After clearing only the known nonzero denominators t,s,D-1, a common root t must annihilate the Sylvester determinant of these two numerator polynomials. The certificate below proves the resulting polynomial nonzero for real n>=1 using exact integer signs. A fixed-size Sylvester determinant still vanishes for a common root after leading coefficients vanish, so no assumption of degree stability is needed.

Case(iv). Let U(v)=v^2-pv+q and W(v)=v^3-hv^2+jv-k for the weight4 and weight2 groups. Both have real coefficients. The derivative equations give U'/U=-n/z, W'/W=n/z at z. Consequently
 q=((n+1)pz-(n+2)z^2)/n,
 h=-1/2-2p,
 j=1/4+p^2-2q+h^2/2,
 k=((n-3)z^3+(2-n)hz^2+(n-1)jz)/n.
These formulas are respectively the first derivative equation, M1=0, M2=0, and the second derivative equation. Define
 M3=1+4(p^3-3pq)+2(h^3-3hj+3k),
 M4=1+4(p^4-4p^2q+2q^2)+2(h^4-4h^2j+2j^2+4hk).
A common root p of the cleared numerator polynomials must annihilate their Sylvester determinant. All divisions above are by positive n or D-1. The certificate below proves this determinant nonzero for n>=1.

## Exact completeness of the four cases

For fixed e, list every odd A0>=1 with A0+2(e+1)<=15 and every partition of(15-A0)/2 into e+1 positive integers. There are11 such partitions at e2,7 at e3,4 at e4,2 at e5 and1 at e6. Larger e is impossible. At e2, all-distinct parts force all nodes real and M2>0; equal parts, unique-higher parts and unique-lower parts with A0!=1 or gap<=1 are excluded by258/261. This leaves(1,3,3) at A0=1. At e3 the unequal partitions with A0=1 are(1,1,1,4),(1,1,2,3),(1,2,2,2), with A0=3 they are(1,1,1,3),(1,1,2,2), and with A0=5 only(1,1,1,2). The equal case has A0=7. The same filters leave exactly(ii),(iii). At e4 the unequal partitions are(1,1,1,1,3),(1,1,1,2,2) at A0=1 and(1,1,1,1,2) at A0=3; A0=5 is equal. Only(iv) remains. At e5 the only unequal partition is(1,1,1,1,1,2) at A0=1, and at e6 all parts are1. Both levels are excluded. A separate recursive partition enumeration checks all25 possibilities and all filters.

## Exact determinant certificates for cases(iii),(iv)

The data file verification/certificate.json stores sparse bivariate integer coefficient lists A,B for each case. In case(iii) the primary expressions are D_raw=zW'(z)+(t+s)W(z) and B_raw=M3; the elimination variable is t. In case(iv) they are M3,M4; the elimination variable is p. A and B are the integer primitive numerators of these rational expressions, with positive leading coefficient in lexicographic order(elimination variable,n). Primitive means divide only by the greatest common divisor of the integer coefficients and possibly change sign. The independent checker reconstructs each numerator by hand-cleared common denominators using sparse integer polynomial addition and multiplication, with no symbolic rational simplifier or resultant routine. It then checks this primitive convention against the certificate. No variable or parameter factor is divided out.

For case(iii), use the common denominator D0=2(n+7)ts, Z=2n+15,
 aa=Z(t-1)s, bb=Z(s-1)t, hh=-(n+7)ts-3aa-2bb, zz=Zts,
 jj=D0^2+6aa^2+4bb^2+2hh^2.
Thus a=aa/D0,b=bb/D0,h=hh/D0,j=jj/(4D0^2),z=zz/D0. The two unnormalized numerator polynomials are
 NA=4zz(2zz-hh)+(t+s)(4zz^2-4hh zz+jj),
 NB=4D0^3+24aa^3+16bb^3+8hh^3-6hh jj,
with denominators4D0^2,4D0^3. These formulas are direct multiplication of the displayed rational expressions. Since n>=1,t!=0,s!=0, every denominator is nonzero. Any extraneous common root introduced by clearing is harmless: a genuine solution is still a common numerator root, and we prove that no common numerator root exists at all for the admissible n.

For case(iv), let l=n+7,Z=2n+15 and define
 qq=2l(n+1)pZ-(n+2)Z^2, hh=-1-4p,
 jj=2nl^2+8nl^2p^2-4qq+nl^2hh^2,
 kk=2n(n-3)Z^3+2n(2-n)hh Z^2 l+(n-1)jj Z.
These give q=qq/(4nl^2),h=hh/2,j=jj/(8nl^2),k=kk/(16n^2l^3). The unnormalized numerators of M3 and M4 are respectively
 NA=16n^2l^3(1+4p^3)-48nl p qq+4n^2l^3hh^3-6nl hh jj+6kk,
 NB=16n^2l^4(1+4p^4)-64nl^2p^2qq+8qq^2+2n^2l^4hh^4
    -4nl^2hh^2jj+jj^2+4l hh kk,
with denominators16n^2l^3 and16n^2l^4. All are nonzero for n>=1. Every equality in these clearings is checked with integer polynomial arithmetic.

The exact resultant identities are
 Res_t(A_iii,B_iii)=409600 n^9(2n+15)^12 F24(n),
 Res_p(A_iv,B_iv)=-13107200 n^6(n+7)^12 F20(n).
The integer coefficient lists of F24 and F20, and their products, are in the same certificate. All25 coefficients of F24 are strictly positive. All21 coefficients of F20(1+x) are strictly positive. The latter list is checked by the binomial identity coeff_x^j=sum_{k>=j}coeff_n^k binom(k,j); no numerical root computation is used. Consequently F24(n)>0 for n>=1, and F20(n)>0 for n>=1, including n=1 because its transformed constant coefficient is positive. All other factors are nonzero there.

Here is a finite exact proof of the two determinant identities. In case(iii), deg_t A=5,deg_t B=6,deg_n A=5,deg_n B=6. The11 by11 Sylvester determinant has six A rows and five B rows, so its degree in n is at most60. The claimed product has degree45. Equality at61 distinct integer values n=1,...,61 therefore proves the identity. A further value n=62 is a sentinel. In case(iv), the corresponding degrees are3,4,5,6. Its7 by7 determinant has four A rows and three B rows, so the degree bound is38. The claimed product has degree38. Equality at39 distinct values n=1,...,39 proves the identity; n=40 is a sentinel. Integer Bareiss elimination, with every division checked for zero remainder, evaluates these determinants. The checker also evaluates each determinant by ordinary rational Gaussian elimination at n=1,2,3/2. The latter cross-check uses a different elimination algorithm but shares the Sylvester construction, and is not described as independent matrix construction.

For completeness, the specialized resultant must vanish if the specialized polynomials have a common finite root: the vector of consecutive powers of that root is nonzero and annihilated by the Sylvester coefficient rows, equivalently by its transpose under the other coefficient convention. This implication does not require the leading coefficients to stay nonzero under specialization. Thus the exact nonvanishing just established excludes both cases(iii),(iv).

## Conclusion, dependencies and scope

Each of the four necessary m15 patterns is excluded. The individual algebraic exclusions hold for real n>=1; the underlying finite-polynomial problem requires integer n. Together with253/258/261 and264, an exact nonzero finite auxiliary polynomial axis identity can only have odd m>=17 and P=n+m/2>=19/2. This is a necessary condition; no example at these remaining degrees is asserted.

The frozen proof and gate hashes of258,261,264 are in verification/DEPENDENCIES.json. The gate must check the complete partition enumeration, all algebraic clearings, the discriminant and real-n case(i), primitive conventions, factor multiplicities/degrees, determinant identities, coefficient signs and file hashes. Exploratory symbolic resultants are discovery artifacts only; the independent certificate checker does not import Sympy or the generator. The actual Opus5.5 reduction review and its follow-up are recorded separately and do not substitute for exact checks.

No uniform degree bound, residual lower bound, nonpolynomial exclusion, convergence theorem or full-plane IPM existence/nonexistence result follows. The full SettingIII problem remains OPEN, the team remains UNRESOLVED, and no early finish is authorized by this result.
