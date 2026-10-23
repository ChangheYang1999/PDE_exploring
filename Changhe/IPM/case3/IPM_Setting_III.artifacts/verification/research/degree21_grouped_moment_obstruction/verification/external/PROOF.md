Finite polynomial axis data: exclusion of d = 21
================================================

Verdict. d = 21 EXCLUDED. All 29 patterns surviving the stated preliminary
lemmas are excluded, in fact for every real n >= 1.

Statement and dependencies.

Assume the reduction and lemmas in A.3.80 of
FINAL_REPORT.d79prelim.frozen.md through "Two pairs", including (A8)-(A10),
and the scaling at the start of "Elimination". The audited x3p_text.txt
supplies types (I)-(IV) and the exclusion of smaller degrees. No other
research files are used. The exact computations below rederive their
elimination equations for the present patterns; they do not import their
old numerical certificates.

More explicitly, write a = A_0, eta = 2n+21 >= 23, T = a eta-21 > 0,
and t_0 = eta-1. An admissible configuration would have e+1 distinct nodes
zeta_j, with positive even weights A_j = 2 mu_j, a positive odd integer a,
and a+sum A_j=21. Conjugation preserves nodes and weights. No node is
0, t_0, or eta. The following necessary conditions will suffice:

    M_l = a t_0^l + sum_j A_j zeta_j^l = 0,  1 <= l <= e,
    sum_j 1/(eta-zeta_j) = 0,
    sum_j A_j/(eta-zeta_j) = -T/eta.                 (1)

At most two nodes are real. A real node is negative or greater than eta.
The configurations considered here satisfy these necessary conditions,
so excluding this larger algebraic system excludes admissible axis data.
Neither (A7) nor sufficiency of (1) is claimed or needed.

Enumeration.

For each odd a, enumerate every decreasing partition of (21-a)/2 of
length at least three. Equivalently, for s=3,...,10, subtract the
floor(s/2)+1 partitions of length at most two from the partition number
p(s). The resulting numbers are

    1, 2, 4, 7, 11, 17, 25, 36,

whose sum is 103. Apply the filters in this order: equal values; one
exceptional value, larger or smaller with a >= 3 or b-A_1 <= 2; at least
three weight classes of odd size; two pairs with a >= 3 or a weight 2.
These remove 12, 41, 18 and 3 patterns respectively. There are 29 survivors.
The question's displayed list contains 28 entries and omits

    (7; 2, 2, 1, 1, 1).

All its other entries are correct. The complete list, including its
elimination type, occurs in the table below and in enumeration.json.
The latter also records all 103 patterns and the filter assigned to each.

Exact polynomial convention.

For q(v)=v^r+c_1 v^(r-1)+...+c_r, write p_k(q) for the sum of kth powers
of its roots, counted once. Define p_0(q)=r and, for k>=1,

    p_k(q) = -sum_{i=1}^{min(k-1,r)} c_i p_{k-i}(q)
             - k c_k                    if k <= r,
    p_k(q) = -sum_{i=1}^r c_i p_{k-i}(q) if k > r.       (2)

Thus a new descending coefficient c_k enters a weighted kth moment
with coefficient -k times its weight. Equations (2), the group
polynomials and (1) specify every computation without finding roots.

Numerators are taken after cancelling a rational function over
QQ[x,y,eta]. Every polynomial called primitive has integer coefficients
with gcd 1 and positive leading coefficient, using lexicographic order
x,y,eta. In particular a univariate primitive polynomial has positive
leading coefficient. Constants are also allowed; their primitive
positive normalization is 1.

Only explicitly nonzero polynomial factors are removed. For the
singleton types these are eta, T, eta-x, and, on the regular branch,
the numerators of L_1 and L_2. For the two-value types these are eta
and T when stated. Integer content is always removable.

Every resultant is an exact resultant over the integer polynomial
ring. If both input equations vanish at the same finite root, their
resultant vanishes after specialization, including when a leading
coefficient becomes zero. This follows either from the Sylvester
matrix or its polynomial Bezout identity. All uses have positive
generic degree in the eliminated variable. For univariate equations
in eta, simultaneous vanishing implies vanishing of their polynomial
gcd, by Bezout's identity over QQ[eta].

Let prem_y(f,g) denote polynomial pseudo-division with respect to y:
it uses only polynomial arithmetic and gives an identity

    lc_y(g)^k f = h g + prem_y(f,g).

It follows that f=g=0 implies prem_y(f,g)=0. This implication remains
valid if lc_y(g) vanishes at the specialization. No pseudo-division
step below divides by a coefficient of a remainder or by a leading
coefficient. Normalizing its integer content does not affect this
implication.

The two exceptional-value patterns.

For (1;4,4,2) and (1;3,3,3,1), (A8) and the unweighted relation in (1)
give the single exceptional node

    x = eta (1-4/T),  T=eta-21.

The other nodes have a common weight, so their monic polynomial is
determined by the moments using (2). For the product pi of the node
polynomials the exact results are

    (1;4,4,2):       pi'(eta) = 3 P_4(eta)/(128 T^2),
    (1;3,3,3,1):     pi'(eta) = 7 P_6(eta)/(48 T^3),

where the coefficient lists, in ascending powers of m, are

    P_4(23+m):
        [382640, 342880, 75528, 4760, 91],
    P_6(23+m):
        [4537920, 6105600, 2794320, 479680, 35724, 1200, 15].

These are strictly positive for m>=0, whereas (1) requires pi'(eta)=0.
At n=1 the scaled derivatives are 71745/32 and 165445/2 respectively.
The one-exception lemma alone already restricts integer n to 1, but
the displayed calculation proves exclusion for every real n>=1.

The two-pairs pattern.

For (1;3,3,2,2), use the accepted discriminant formula with weights
6 and 4 and z=eta/(eta-1). Its K is exactly

    K = 3 P_K(eta)/(eta-1)^2,
    P_K(23+m) = 153072 + 204592 m + 57392 m^2 + 3892 m^3 + 77 m^4.

Thus K>0 for every eta>=23, and the discriminant -4*6*4*K is negative.
The relevant pair sum must be real because its class is preserved by
conjugation. This is a contradiction. In particular K(23)=114804/121.
The stronger sufficient inequality T(6+4)>6*4 is not needed.

Previously defined types, recomputed here.

Type (I). One class is a pair of weight w and the other has m=e-1
nodes of weight b != w. Set

    p(v)=v^2-xv+c,
    c=((T+w-b)x eta-(T+2w-2b)eta^2)/T.

The first relation (A9) gives c, with nonzero pivot T. The first
m-1 moments give the first m-1 descending coefficients of the monic
polynomial q of the other class, with pivots -l b. The second (A9)
gives its constant coefficient, with pivot -T. The numerators of
M_m and M_(m+1) have a common x at a solution. Their resultant in x,
normalized as above, is Lambda. There are no other pivots.

Type (II). Let x and u be the singleton nodes, with distinct weights
A and B, and let the remaining m=e-1 nodes have weight b. Set

    S=(T+A-b)eta-Tx,
    u=eta+(B-b)eta(eta-x)/S.

(A10) gives this formula. If S=0, its original polynomial relation
would give (A-b)(B-b)eta^2/T=0; this is impossible, since the three
weights are distinct, eta>0 and T>0. Moments 1,...,m determine the
descending coefficients of the repeated class, with pivots -l b.
The numerators of M_(m+1) and pi'(eta) have a common x. Their
resultant is Lambda. This treats the possible S=0 branch rather
than discarding it.

Type (III). The only present pattern is (3;2,2,2,1,1,1), with weights
4 and 2 each taken three times. Use p=v^3-xv^2+yv+c and a monic
cubic q. The two relations (A9) determine the constants of p and q,
and M_1,M_2 determine the other coefficients of q. The pivots are
T,-2,-4,-T. The primitive numerator of M_3 is C_1 y+C_0. For C_1!=0,
substitute y=-C_0/C_1 and eliminate x between the numerators of M_4
and M_5. This gives degree 81. For C_1=0 one must also have C_0=0;
Res_x(C_1,C_0) has degree 7, with shifted coefficient list

    [8577317003264, 3265385573888, 530358338304, 47632749424,
     2554592800, 81805896, 1448280, 10935].

It has no zero for eta>=23. Both branches are therefore covered.

Type (IV). Let x be the singleton of weight A; the two pairs have
distinct weights w,b. With L_0=1/(eta-x), set

    L_1=(-T/eta-(A-b)L_0)/(w-b),  L_2=-L_0-L_1.       (3)

On L_1 L_2!=0 the relations p_i'(eta)=L_i p_i(eta) determine the
pair products, with pivots -L_1,-L_2. M_1 determines the second
pair sum with a nonzero constant pivot. The primitive numerator
N_0 of M_2 is quadratic in the first pair sum y. Pseudo-reduce the
numerators of M_3,M_4 to R_1=a_1 y+a_0 and R_2=b_1 y+b_0. A solution
annuls U=a_1 b_0-a_0 b_1 and V=Res_y(N_0,R_1). After removing factors
of the two logarithmic-derivative numerators, Res_x(U,V) has degree
234 and is strictly positive after the shift eta=23+m, for each of
the three patterns of this type.

If the pair of weight w has L_1=0, its sum is 2 eta and
x=eta(1+(A-b)/T). Hence L_2=-L_0!=0. M_1 gives the other pair sum;
its logarithmic relation gives its product; M_2 gives the product
of the zero-derivative pair, with coefficient -2w. The remaining
numerators of M_3 and M_4 have gcd 1. The same argument with the
pairs exchanged covers L_2=0. Each of these six gcd computations
is recorded. The two L_i cannot both vanish since L_0!=0.

New type (V): a triple and a quartet.

This is (1;2,2,2,1,1,1,1), with weights w=4 and b=2. Let

    p(v)=v^3-xv^2+yv+c,
    q(v)=v^4+c_1 v^3+c_2 v^2+c_3 v+c_4.

The first (A9) determines c, with pivot T. Moments M_1,M_2,M_3
determine c_1,c_2,c_3, with respective pivots -2,-4,-6. The second
(A9) determines c_4, with pivot -T. Thus all these pivots are
nonzero for eta>=23.

Let N_0,F_1,F_2 be the primitive numerators of M_4,M_5,M_6. N_0 is
quadratic in y and its leading coefficient is 384 T^2. Put

    R_1=prem_y(F_1,N_0)=a_1 y+a_0,
    R_2=prem_y(F_2,N_0)=b_1 y+b_0,
    U=a_1 b_0-a_0 b_1,
    V_1=Res_y(N_0,R_1),  V_2=Res_y(N_0,R_2).          (4)

Remove their powers of eta and T and take primitive parts. A
solution annuls all three polynomials U,V_1,V_2. Therefore it
annuls H_1=Res_x(U,V_1) and H_2=Res_x(U,V_2), and hence their
primitive gcd Lambda.

The degrees of H_1,H_2,Lambda are 165,198,102. Every coefficient of
Lambda(23+m) is positive. In particular the first eliminant alone
does not have this property; taking the gcd is part of this proof.
No coefficient a_i or b_i has been divided out, so their possible
vanishing gives no omitted branch. The only actual divisions
were by nonzero constants and T.

New type (VI): a singleton, a pair and a triple.

This is (1;3,2,2,1,1,1). The weights are A=6,w=4,b=2, and T=eta-21.
Write the singleton as x, and use

    p(v)=v^2-yv+c,
    q(v)=v^3+c_1 v^2+c_2 v+c_3.

Use (3), so that

    L_1=[Tx-(T+4)eta]/[2eta(eta-x)],
    L_2=[(T+2)eta-Tx]/[2eta(eta-x)].                 (5)

On the regular branch L_1 L_2!=0, p'(eta)=L_1 p(eta) determines c,
with pivot -L_1. M_1 and M_2 determine c_1,c_2, with pivots -2,-4,
and q'(eta)=L_2 q(eta) determines c_3, with pivot -L_2. Equivalently,

    c=(2eta-y)/L_1-eta^2+y eta,
    c_1=(eta-1+6x+4y)/2,
    c_2=((eta-1)^2+6x^2+4(y^2-2c)+2c_1^2)/4,
    c_3=(3eta^2+2c_1 eta+c_2)/L_2
          -(eta^3+c_1 eta^2+c_2 eta).

Let N_0,F_1,F_2 be the primitive numerators of M_3,M_4,M_5. Their
degrees in y are 3,4,4. First form

    U=Res_y(N_0,F_1),  V=Res_y(N_0,F_2),  H=Res_x(U,V).

For a second necessary eliminant form

    Q_1=prem_y(F_1,N_0),  Q_2=prem_y(F_2,N_0),
    R=prem_y(N_0,Q_1),  W=Res_y(Q_2,R),  J=Res_x(U,W).  (6)

The degrees in y of Q_1,Q_2,R are 2,2,1. After each indicated
operation, powers of eta,T,eta-x and the numerators of L_1,L_2
may be removed. These are nonzero on this branch. The exact
removed factors and their exponents are saved in the certificate.
Every equation used in (6) is necessary even when a specialized
leading coefficient vanishes, by the pseudo-division identity.
There is no division by a coefficient of Q_1,Q_2 or R.

The degrees of H and J are 946 and 1322. Let Lambda be their
primitive gcd after removing powers of eta and T. It has degree
160, and every coefficient of Lambda(23+m) is positive. The
second eliminant J itself also has all shifted coefficients
positive, providing a redundant exclusion of the regular branch.

For L_1=0, (5) gives x=eta(1+4/T) and p'(eta)=0 gives y=2eta.
The pair product c is now the remaining variable. Moments M_1,M_2
give c_1,c_2, and the nonzero logarithmic relation for q gives c_3.
The remaining numerators M_3,M_4,M_5 have degrees 1,2,2 in c.
The two resultants of the first with the other two have degrees
16 and 18; their primitive gcd is T^4. This cannot vanish.

For L_2=0, (5) gives x=eta(1+2/T), and L_1=-L_0!=0 determines the
pair product from its sum y. M_1 determines c_1; q'(eta)=0
determines c_2 with pivot 1; M_3 determines c_3 with pivot -6.
The remaining numerators M_2,M_4,M_5 have degrees 2,4,5 in y.
The two resultants of the first with the other two have degrees
24 and 30; their primitive gcd is T^8. This also cannot vanish.
All other pivots are nonzero constants or L_1,L_2 on their stated
branches. Both L_i cannot vanish together since L_0!=0.

Computation and verification.

certificate.py carries out the recurrences, rational cancellations,
pseudo-divisions, resultants, gcds and shifts directly over the
integer polynomial ring, using Python-FLINT 0.9.0. It uses neither
floating point nor interpolation. Thus no guessed degree bound
or numerical root exclusion is used. Every rational group coefficient,
residual polynomial, needed remainder, removed factor, resultant and
final coefficient list is saved in certificate_01.json through
certificate_29.json. Each list explicitly includes zero coefficients.

verify.py independently derives the power sums as minus k times the
coefficient of u^k in the truncated formal logarithm

    log(1+c_1 u+...+c_r u^r).

This checks the saved eliminations and moment identities using a
different formula from (2). It independently recomputes all shifted
coefficient lists by the integer binomial theorem. There are 168 exact
formal-logarithm identity checks and 42 binomial shift checks.
Exploratory eliminants whose shifted coefficients are not all positive
are retained and explicitly marked as such; they are never individually
claimed to exclude a pattern.

All computations are single-threaded, with an address-space cap below
2 GB. The scripts use no JavaScript, GPU, server or RLScience resource.
The two prescribed input files are not modified.

The requested Claude Opus 5.5 consultation was attempted through the
existing Bedrock profile, requesting us.anthropic.claude-opus-5-5.
Credential retrieval failed before model invocation. No model answered,
no substitute model was used, and no second-model endorsement is claimed.
The exact limitation is recorded in opus_unavailable.json.

Conclusion and scope.

Each survivor contradicts a necessary condition for every eta>=23.
Therefore no d=21 admissible configuration exists for any real n>=1;
in particular none exists for integer n>=1. Combined with the
accepted exclusion of all smaller odd d, this gives d>=23 and
P=n+d/2>=25/2. This is an exclusion in the finite polynomial axis-data
class, not a nonexistence theorem for more general hydrostatic profiles.
There is consequently no real or integer configuration to report in
part (e).

The following table records the positive polynomial used for each
pattern. For the exceptional patterns it is P_4 or P_6; for the two
pairs it is P_K; otherwise it is Lambda. The last column is the exact
least coefficient of its expansion in ascending powers of eta-23.


| No. | Pattern (A_0; mu) | Type | Degree | Least shifted coefficient |
|---:|---|---|---:|---:|
| 1 | (1; 6, 2, 1, 1) | II | 54 | 5649508565353275 |
| 2 | (1; 5, 3, 1, 1) | II | 54 | 10590692191252173 |
| 3 | (1; 5, 2, 2, 1) | II | 54 | 9370886559077043 |
| 4 | (1; 4, 4, 2) | exception | 4 | 91 |
| 5 | (1; 4, 2, 2, 1, 1) | IV | 234 | 12589824224106242877960644905582320036624386955702852391724787531217152941162109375 |
| 6 | (1; 4, 2, 1, 1, 1, 1) | II | 150 | 1030606926392491685834653114644776361171 |
| 7 | (1; 3, 3, 3, 1) | exception | 6 | 15 |
| 8 | (1; 3, 3, 2, 2) | two_pairs | 4 | 77 |
| 9 | (1; 3, 3, 2, 1, 1) | IV | 234 | 118950341479372232985740909521600862840219189616819493288881936769599609375 |
| 10 | (1; 3, 3, 1, 1, 1, 1) | I | 38 | 1769719778467641 |
| 11 | (1; 3, 2, 2, 1, 1, 1) | VI | 160 | 926910390972025085770986163454028685545140676868998420479567880381895463677521 |
| 12 | (1; 2, 2, 2, 2, 1, 1) | I | 38 | 2470320857621617 |
| 13 | (1; 2, 2, 2, 1, 1, 1, 1) | V | 102 | 1667317721197146097465612035138116195970034473 |
| 14 | (1; 2, 2, 1, 1, 1, 1, 1, 1) | I | 81 | 14023747963387634772347454273867 |
| 15 | (3; 5, 2, 1, 1) | II | 54 | 11554350540972247701 |
| 16 | (3; 4, 3, 1, 1) | II | 54 | 473163380940627976599 |
| 17 | (3; 4, 2, 2, 1) | II | 54 | 20427395532780538575 |
| 18 | (3; 3, 3, 2, 1) | II | 54 | 30347547047692875 |
| 19 | (3; 3, 3, 1, 1, 1) | I | 26 | 49311077418603 |
| 20 | (3; 3, 2, 2, 1, 1) | IV | 234 | 1534197374141597781641255338394620081334550580399047600375550311284686606942929976849248245269775390625 |
| 21 | (3; 3, 2, 1, 1, 1, 1) | II | 150 | 22289047872611682771558844708955564349435722103891 |
| 22 | (3; 2, 2, 2, 1, 1, 1) | III | 81 | 4309127019076973520475204608011906086516400625 |
| 23 | (3; 2, 2, 1, 1, 1, 1, 1) | I | 63 | 80985058811060297734118783327823 |
| 24 | (5; 4, 2, 1, 1) | II | 54 | 5082879486128871917724609375 |
| 25 | (5; 3, 2, 2, 1) | II | 54 | 2080518776017597198486328125 |
| 26 | (5; 2, 2, 2, 1, 1) | I | 26 | 28415087139892578125 |
| 27 | (5; 2, 2, 1, 1, 1, 1) | I | 38 | 28944528713965274810791015625 |
| 28 | (7; 3, 2, 1, 1) | II | 54 | 187212294352811365217125 |
| 29 | (7; 2, 2, 1, 1, 1) | I | 26 | 1618659536891685925 |
