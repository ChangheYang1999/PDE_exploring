# Compatible high scalar weights and all three jet-block conditions

## Concrete spaces and statement

Use the actual normalized modal background and canonical full-plane velocity. Fix

 sigma=25/4, delta=9/5, gamma=-1/2,
 a(t)=exp(delta t) for t<=0, a(t)=exp((gamma-3)t) for t>=1,

with a fixed smooth positive interpolation. Let Gamma_H=a H^sigma(R) and B_H=A^(-1)Gamma_H with the graph norm of proof 114. The low spaces B,R,Z,Y and the scalar operator A are as in proof 44. Put p(X)=x^2 y and define

 R_base={p a(t)u(t,theta):u in H^sigma(R times S1),
             u even under both coordinate reflections,
             u(t,pi/2)=0},
 ||p a u||_(R_base)=||u||_(H^sigma).

Fix epsilon>0 and s=41/20. Let

 Q={r^3 a(t)v(t,theta):v in H^s(R times S1),
             v has even-x odd-y parity,
             supp v subset {|cos theta|>=epsilon}},
 R_H=R_base+Q,

with the infimum Hilbert product norm. The trace constraint is in the Sobolev sense. The angular Hardy estimate of proof 111 and the bulk estimate of proof 63 prove a continuous embedding R_H into R. The kernel of the sum map is closed by that embedding, so this defines a Hilbert space. Choose the sector cutoff chi_s with support in {|cos theta|<epsilon}. Then R_H embeds continuously into R_(4,s) by proof 111.

For the exact lower block and axis row

 X beta=Err beta+C_R E beta,
 Gamma_C h=axis cofactor of the normalized coupling,

the following hold:

 (J1) X:B_H->R_base, hence X:B_H->R_H, is bounded.
 (J2) Gamma_C:E B_H direct-sum R_H -> Gamma_H is compact.
 (J3) The actual bordered vector zeta belongs to E Gamma_H direct-sum R_H.

For J2 the input remainder space may be replaced by any smaller high graph domain continuously included in R_H; the target in J1 and J3 remains R_H. These statements verify the three jet-block conditions for this explicit candidate. They do not prove the high remainder conditions H1-H3, injectivity, an inverse bound or nonlinear closure.

## The transport lift

The exact scalar graph theorem gives

 beta=J chi+a v, v in H^(sigma+1),
 |J|+||v||_(H^(sigma+1))<=C||beta||_(B_H).                 (1)

The modal transport lift is

 Err beta=p cos(theta)^2[a_1 beta'+a_0 beta],
 a_1=(q-d)/cos(theta)^2,
 a_0=(2V_1/x+V_2/y-1-b)/cos(theta)^2.                     (2)

Both coefficients have finite angular expansions. Division by cos(theta)^2 is exact: the numerator is reflection-even and vanishes at the vertical axis. Their radial coefficients are at least C5, piecewise analytic with finitely many knots, so locally in H^sigma. At the endpoints, with all fixed t derivatives needed,

 a_1=-(A+D)+O(r^2), a_0=O(r^2) at0,
 a_1,a_0=O(r^(k-1)) at infinity.                         (3)

The finite angular dimension makes all these algebraic division maps bounded, with constants depending only on the fixed background degree.

After division by p a, (2) becomes

 cos(theta)^2{a_1[v'+(a'/a)v]+a_0 v
                 +J[a_1 chi'/a+a_0 chi/a]}.             (4)

The fixed J coefficient belongs to the cylinder H^sigma space: at0 it is O(r^(2-delta)), at infinity it vanishes, and its compact-interval regularity was just checked. All the other coefficients are smooth endpoint limits plus H^sigma radial coefficients. The one-dimensional H^sigma multiplication inequality and the finite angular expansion prove the H^sigma bound for (4). It vanishes at the vertical axis. Hence Err maps B_H boundedly into R_base.

## The complete finite-mode velocity of a jet input

The canonical stream function of h=E beta has only angular modes2 and4. Direct differentiation gives

 partial_x h=r^2[(beta+beta'/4)sin(2theta)+(beta'/8)sin(4theta)].

Integrating the whole-plane Green formula by parts gives

 psi=r^2[(P-Q)sin(2theta)-S sin(4theta)]/8,                (5)

where

 P=int_t^infinity exp(2u)beta(u)du,
 Q=int_(-infinity)^t exp(-4(t-u))exp(2u)beta(u)du,
 S=int_(-infinity)^t exp(-6(t-u))exp(2u)beta(u)du,
 c=P(-infinity)/4.                                      (6)

The boundary terms vanish because beta is bounded at0 and decays faster than r^(-2) at infinity. Formula (5) is the canonical Green solution; no homogeneous velocity is added. In polar coordinates it gives

 U_r/r=-(P-Q)cos(2theta)/4+S cos(4theta)/2,
 U_theta/r=(P+Q-r^2 beta)sin(2theta)/4
                          +(4S-r^2 beta)sin(4theta)/8.   (7)

These formulas use beta but no derivative of beta. They are also valid for (1) by Sobolev approximation and the absolutely convergent moment integrals.

The moment operators have the following elementary weighted bounds. Put b_1(t)=exp(2t)a(t). For the input beta=a v, each of Q/b_1, S/b_1 and (P-4c chi)/b_1 belongs to H^(sigma+1), bounded by C||v||_(H^(sigma+1)). To check this, the inner rates of b_1 are delta+2 and its outer rate is gamma-1. On either half-line the quotient kernels are exponential convolutions. The positive decay rates are

 delta+6 and gamma+3 for Q,
 delta+8 and gamma+5 for S,
 delta+2 for the inner integral of P-4c,
 1-gamma for the outer integral of P.                    (8)

Every rate in (8) is positive at the displayed parameters. Differentiation commutes with those half-line convolution formulas after a smooth cutoff; the cutoff terms have compact support. Across the fixed transition interval ordinary integration and the first-order moment equations give the same bound. The scalar c is bounded because b_1 belongs to L2 and c is its pairing with v, up to fixed cutoff terms.

The input J chi produces fixed smooth moment profiles. After subtraction of the strain part 4c chi from P, those profiles are O(r^2) at0 and O(r^(-4)) or faster at infinity. Thus (7) has the exact decomposition

 U[E beta]/r=c chi u_lin(theta)+J U_J(t,theta)
                                      +b_1(t)U_v(t,theta), (9)

where u_lin corresponds to the Cartesian field (-x,y)/r, U_J is fixed with the endpoint bounds just stated, and U_v has finitely many angular modes with radial H^(sigma+1) norm bounded by C||v||_(H^(sigma+1)). Different fixed cutoffs in (9) and in the normalization change only compactly supported finite-rank terms.

## The normalized coupling and its remainder

Write the actual density as rho=p A_bg(t,theta). Its cofactor has finitely many angular modes, satisfies A_bg=1+O(r^2) at0 and A_bg=O(r^(k-3)) at infinity, and has C6 piecewise-analytic radial coefficients. Its first t and angular derivatives have local H^sigma regularity. Angular division in the following expressions is exact and finite-dimensional, by the parity and the x^2 factor of rho.

The coupling divided by p is a finite linear combination of the radial coefficients in (7), c chi_0, and the coefficients of A_bg and its first derivatives. The leading strain cancels exactly. Indeed near0 the normalized strain field is c(-2x/3,4y/3), and

 (-2x/3,4y/3).grad p=0.

Therefore its action on rho is p times its action on A_bg, which is O(r^2). After division by a, this fixed strain contribution belongs to H^sigma because2-delta>0. The fixed J term in (9) has the same inner order and, at infinity, its product with the background divided by a decays at least as r^(k-gamma-4).

For the U_v term, b_1/a=r^2. Multiplication by A_bg and its first derivatives produces coefficients that are O(r^2) at0 and O(r^(k-1)) at infinity. These coefficients have the checked local H^sigma regularity and their fixed-order endpoint derivatives decay. They therefore multiply H^(sigma+1) functions boundedly into H^sigma. This proves that the full normalized coupling divided by p a belongs to the cylinder H^sigma space, with norm bounded by C||beta||_(B_H).

It remains to remove its axis row. The full coupling has a fixed finite angular degree, independent of beta. Evaluation at the axis and subtraction of that scalar coefficient are bounded linear maps on this finite angular coefficient space, including in its radial H^sigma norm. The resulting cofactor vanishes at the vertical axis. This proves C_R E:B_H->R_base and completes J1.

## Compactness with the stronger scalar weights

Theorem113 supplies local H^(51/8) control and the following uniform endpoint bounds for the full axis row on E B_6 plus R_(4,s):

 ||Gamma_C h||_(H^(51/8)(I_n))<=C||h|| times
       exp(2n) at negative infinity,
       exp((k-35/8)n) at positive infinity.              (10)

The present B_H is continuously included in B_6, because Gamma_H is continuously included in the old G^6. Multiplying (10) by a(n)^(-1) changes its exponents to

 2-delta=1/5 at negative infinity,
 k-gamma-11/8=k-7/8<0 at positive infinity.               (11)

The smooth quotient a(t)/a(n) and all its needed logarithmic derivatives are uniformly bounded on each I_n. Thus (10)-(11) prove boundedness into a H^(51/8), with uniformly small tails. Local compactness from order51/8 to25/4, followed by the same tail argument as in proof 113, proves J2. The remainder embedding required here is exactly proof 111.

## Membership of the bordered vector

Proof 83 proved from the actual all-mode Green formulas that zeta/p is a finite angular polynomial with local H^sigma radial coefficients for every sigma<13/2. At the endpoints, including all fixed t derivatives there,

 zeta/p=O(r^2) at0,
 zeta/p=O(r^(2k-4)(1+|log r|)) at infinity.               (12)

After division by a, the powers are2-delta>0 at0 and2k-1-gamma=2k-1/2<0 at infinity. Hence zeta/(p a) belongs to H^sigma on the cylinder. Because the angular degree is finite, axis evaluation preserves this same radial order, without the generic half-derivative trace loss. Its axis coefficient belongs to Gamma_H, and its remainder belongs to R_base. This proves J3.

## What remains outside this theorem

The three jet-block hypotheses are now valid for one explicit choice of scalar and remainder spaces. The high remainder coupling bound H1, the transport resolvent H2, the compact high estimate H3 and low injectivity have not been proved by this argument. The fixed cone-bulk space is used here only to state and verify the block mappings; no invariance under the actual flow is asserted. No nonlinear existence theorem follows until those separate obligations and the quantitative closure conditions are met.
