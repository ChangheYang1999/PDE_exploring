# Degree13 grouped-moment obstruction

Result264, reduction written on2026-10-21 before exact elimination code, with its initial version retained as INITIAL_REDUCTION.md. The exact certificate argument below was completed before the independent checker. This proof concerns only the finite auxiliary polynomial axis problem of253,258,261.

## Hypotheses and target

Assume the critical residue system of258 with integer n>=1, m=13, e=3, A0=1, and four distinct nonzero transformed nodes v1,...,v4, none equal to1 or z, whose multiplicities are (2,2,1,1). Thus the residue weights are (4,4,2,2), z=(13+2n)/(12+2n), and

M_l=1+4(v1^l+v2^l)+2(v3^l+v4^l),
M1=M2=M3=0, pi'(z)=0, M4 z+13 v1 v2 v3 v4=0,
pi(v)=product_{j=1}^4(v-vj).

Reality of the original polynomial implies that conjugation preserves each multiplicity group. Therefore both monic quadratics with these groups as roots have real coefficients:

U(v)=v^2-sv+t, W(v)=v^2-hv+j, pi=UW.

The exact target is to prove that these necessary equations have no solution for real s,t,h,j and 1<z<=15/14. This stronger range follows from integer n>=1 and m=13. The group roots need not themselves be real. No division by an individual root or discriminant will be used.

## Exact reduction, proved independently

For a quadratic with root sum s and product t the first four power sums are s, s^2-2t, s^3-3st, s^4-4s^2t+2t^2. Hence M1=M2=0 imply

h=-1/2-2s, j=3/8+s+3s^2-2t.

After substitution,

M3=24s^3+9s^2+(9/2)s+15/8-(36s+6)t.

At s=-1/6 this equals91/72, independently of t, so no solution has 6s+1=0. Thus

t=(64s^3+24s^2+12s+5)/(16(6s+1)).

Let T(s) denote this expression and put H(s)=-1/2-2s and J(s)=3/8+s+3s^2-2T(s). Define the rational expressions

A_raw(s,z)=4z^3-3(s+H)z^2+2(T+J+sH)z-(sJ+HT),
B_raw(s,z)=z[1+4(s^4-4s^2T+2T^2)+2(H^4-4H^2J+2J^2)]+13TJ.

These are exactly pi'(z) and M4 z+13tj. Let A(s,z) and B(s,z) be their integer primitive numerator polynomials after denominator clearing, choosing positive leading coefficients in lexicographic order s,z. Their denominators are nonzero whenever6s+1!=0. Therefore every solution gives A(s,z)=B(s,z)=0.

Define R(z)=Res_s(A,B) as the determinant of the Sylvester matrix. At any fixed z0 for which the two specialized polynomials share a finite root s0, this determinant vanishes: the vector of powers of s0 gives a nonzero null vector of the Sylvester evaluation system. This implication remains valid if leading coefficients vanish under specialization. Therefore a necessary condition is R(z0)=0. No converse or division by the resultant's leading coefficient is used.

## Exact coefficient certificate and nonvanishing proof

The certificate in verification/certificate.json gives the full integer coefficient lists of A,B,R and of all factors. In the following identity the sign of A is the primitive-numerator convention stated above:

R(z)=-35566624178176 f3(z) g3(z) f6(z) f10(z),

f3=128z^3+32z^2+20z+15,
g3=320z^3+80z^2+24z+5,
f6=138240z^6+69120z^5+40608z^4+19072z^3+4728z^2+1260z+245,
f10=2013265920z^10-7717519360z^9+10385620992z^8-5407899648z^7
    +693686272z^6+74287104z^5-256695072z^4+169042432z^3
    +31182528z^2+8304660z+6997445.

Here is a finite exact verification of the determinant identity that does not rely on floating-point roots or on the generating symbolic resultant. The degrees in s of A and B are4 and6, and their degrees in z are at most3 and1. Every term of their10 by10 Sylvester determinant has six A entries and four B entries, so its degree in z is at most22. The displayed product also has degree22. Evaluate the determinant and the claimed polynomial at each integer z=-11,-10,...,11. Fraction-free integer Gaussian elimination with exact divisions computes these determinants. Equality at these23 distinct points proves the polynomial identity by the degree bound. A further independent sentinel at z=12 is recorded. Each specialized determinant equality is stored in the check evidence. This is an identity certificate, not a sampled inference about the roots.

The first three factors are strictly positive for z>0 because all of their coefficients are positive. To treat f10, set z=(1+15q)/(1+14q). This is a bijection q>0 to1<z<15/14. The integer polynomial

Q(q)=(1+14q)^10 f10((1+15q)/(1+14q))

has all11 coefficients strictly positive; its exact coefficient list is in the certificate. This list is independently reconstructed by the binomial theorem: the coefficient list of the k-th summand of f10 is its coefficient times the convolution of (1+15q)^k and (1+14q)^(10-k). Thus Q(q)>0 for q>0. At the upper endpoint the certificate gives

f10(15/14)=169230287405/282475249>0.

At z=1, f10(1)=273273>0 as an additional check, though this endpoint is outside the requested interval. Therefore every factor, and hence R, is nonzero for1<z<=15/14. The necessary resultant equation is impossible.

This completes the algebraic argument once the finite integer certificate equalities are checked. Those equalities are exact and exhaust the stated polynomial identity; no real root isolation or numerical tolerance is involved. The verifier status remains pending until the independent certificate checker has run.

## Consequence for the finite auxiliary polynomial class

Result261 enumerates every m13 pattern and excludes all except the present one, and excludes all smaller odd m already not ruled out by253/258. The new obstruction excludes the final m13 pattern for all real n>=1, a fortiori for integer n. Consequently an admissible finite auxiliary polynomial identity can only have odd m>=15 and P=n+m/2>=17/2. This is only a necessary condition. It asserts no configuration at these remaining values.

## Dependencies and scope

253 supplies P=n+m/2 with odd m, 258 supplies the residue/moment reduction, and261 excludes all cases through m11 and all m13 patterns except (2,2,1,1). Those proofs are separate dependencies. This argument supplies no uniform degree bound and says nothing about nonpolynomial limits or full-plane existence. No Lean/Lake build or machine-checked proof is claimed. The full SettingIII endpoint remains OPEN regardless of the result of this finite elimination.
