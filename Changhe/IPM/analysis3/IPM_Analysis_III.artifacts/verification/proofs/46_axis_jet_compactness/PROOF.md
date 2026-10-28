# Compactness of the complete axis coupling

## Statement, spaces and scope

Use the spaces of proof 44 with a=17/4, eta=5/4, ell>1, k=1/ell and the positive-axis hypothesis (A). Thus R=L2_P(w dX), where

 w=|x|^(-2a) for r<1,
 w=|cos(theta)|^(-2a) r^(-eta) for r>=1.

The parity P is even in x and odd in y. Let B be the Hilbert space of beta=H z defined in proof 44, with z' in L2(omega), z(+infinity)=0 and continuous coordinate J=z(-infinity). Set E beta=x^2 y beta(log r), X0=E B direct-sum R, and

 G=L2(g(t)dt),  g(t)=exp(-t/2) for t<0,
                       exp(27t/4) for t>=0.

Assume the background has a classical axis expansion rho(x,y)=x^2 rho2(y)+O(x^4) on compact annuli, and write rho2(y)=y A(log y), y>0. Assume A is C1, bounded on compact intervals, and

 |A(t)|<=A0,  |A'(t)|<=A1 exp(2t) for t<=0,
 |A(t)|+|A'(t)|<=Aplus exp((k-3)t) for t>=0.                (B)

The first estimate may use a larger finite constant when necessary. Let chi0 be any smooth radial cutoff equal to1 near0 and zero outside a compact set. Define U by the canonical full-plane inverse with no harmonic velocity. For the dense smooth inputs considered below, put

 T_h(y)=U2[h](0,y), c[h]=T_h'(0),
 Gamma_h(t)=(A+A') T_h(y)/y - 2 A T_h'(y)
                 +c[h] chi0(y)(A+A'/3),  y=exp(t).        (1)

Then Gamma extends to a Hilbert-Schmidt map X0->G. In particular it is compact on Z=E B direct-sum D_R with its graph norm. Formula (1) is precisely the x^2 y axis coefficient of

 C h=[U[h]+chi0(c[h]/3)X].grad rho.

Consequently, once the separate mapping hypothesis (E0), C:Z->Y=E G direct-sum R, is established by an extension agreeing with the smooth core, its jet coordinate is Gamma and hypothesis (E-J) follows. No boundedness of the remainder part of C, and no Garding estimate, is asserted here.

The modal background used by the team satisfies (B) qualitatively: its verified inner expansion has A=1+O(exp(2t)), A'=O(exp(2t)); its finite angular expansion and outer powers give A,A'=O(exp((k-3)t)). This result does not provide numerical values of A0, A1, Aplus or the Hilbert-Schmidt norm.

## The exact axis row and its cancellation

Incompressibility gives partial_x U1(0,y)=-T_h'(y). Since rho_x=2x rho2+O(x^3), rho_y=x^2 rho2'+O(x^4), the x^2 coefficient of U.grad rho is -2 rho2 T_h'+rho2' T_h. Dividing by y and adding the radial strain term gives (1). No derivative of chi0 appears, because chi0 multiplies the velocity rather than being differentiated.

Write V_h(t)=T_h(y)/y and B_h(t)=V_h(t)-c[h]. A prime on V_h or A below means differentiation in t. Where chi0=1, (1) becomes

 Gamma_h=(A'-A) B_h -2 A V_h' +(4/3)c[h] A'.               (2)

This identity exhibits the required cancellation. The constant c[h] part of V_h cancels when A=1. Retaining the complete velocity does not make the entire coupling vanish.

## Remainder inputs: trace kernels and explicit bounds

Let

 K(s,z)=(s^2-z^2)/(2 pi (s^2+z^2)^2).

For h in R define the axis traces by the absolutely convergent pairings

 T_h^(j)(y)=integral_R2 partial_y^j K(-s,y-v) h(s,v) ds dv,
                         0<=j<=3.                        (3)

The point mass in the full multiplier U2=R1^2 does not contribute to the trace for smooth inputs vanishing on the axis. Formula (3), by continuous extension from those inputs, defines the trace for general h in R; it is not an assertion that every h has a classical pointwise representative on the axis.

Set q_j=(j+1)!/(2 pi). The complex kernel formula gives

 |partial_y^j K(-s,y-v)|<=q_j (s^2+(v-y)^2)^(-(j+2)/2).    (4)

Also, globally,

 w^(-1)<=|s|^(2a),
 w^(-1)<=|s|^(2a)(s^2+v^2)^((eta-2a)/2)<=r^eta.           (5)

For |y|<=1 split the input into r<=4 and r>4. In the first part R_y=|(s,v)-(0,y)|<=5 and |s|<=R_y. In the second R_y>=3r/4. Cauchy-Schwarz, polar integration, (4) and (5) give

 ||T^(3)(y)||_(R*)^2 <= M3^2,
 M3^2=(12/pi)^2 2 pi [5^(2a-8)/(2a-8)
                  +(4/3)^10 4^(eta-8)/(8-eta)].           (6)

The first integral converges because a>4; the second because eta<8. The same argument works for j=0,1,2 with their corresponding powers. It proves uniformly bounded trace maps into C3([-1,1]). More explicitly, approximate h in R by smooth parity-preserving functions supported away from the axis and origin. Their traces converge with all three derivatives uniformly on compact y intervals. This proves the differentiability claimed in (3), including at0, without assuming derivatives of h.

Parity gives T(0)=T''(0)=0. Direct differentiation of the kernel gives

 partial_y K(-s,-v)=v(3s^2-v^2)/(pi(s^2+v^2)^3),

so T'(0) is exactly the strain functional c of proof 44. In particular |c[h]|<=c_R ||h||_R with c_R<0.207570. Taylor's integral formula now yields, for 0<y<=1,

 |T_h(y)/y-c[h]| <= (M3/6)y^2 ||h||_R,
 |V_h'(log y)| <= (M3/3)y^2 ||h||_R.                      (7)

For the second inequality use V'=T'-T/y=(1/y) integral_0^y s T''(s)ds and |T''(s)|<=M3 s ||h||_R. Hence (2), for y small enough that chi0=1, gives a finite constant Cminus,R with

 ||Gamma_.(log y)||_(R*)<=Cminus,R y^2.                  (8)

For example, when chi0=1 on [0,1], one may take

 Cminus,R=(5 A0+A1)M3/6 +(4/3)c_R A1.

We also need a bound uniform at infinity, not just a compact-strip trace theorem. For j=0,1 put

 F_j^2=q_j^2 integral_R2 |Y-(0,1)|^(-4-2j)
                     |Y1|^(2a)|Y|^(eta-2a) dY.

These integrals are finite: near (0,1) the condition is a>j+1, near0 it is eta>-2, and at infinity it is eta<2+2j. A change of variables in (3), using (5), gives for all y>0

 ||T_h^(j)(y)||_(R*) <= F_j y^(eta/2-1-j).                (9)

The following fully explicit upper bound is useful if a numerical trace constant is later needed:

 F_j^2 <= q_j^2 2 pi [2^(2+2j-eta)/(2a-2-2j)
                    +2^(2+2j-eta)/(eta+2)
                    +2^(eta+5+2j)
                    +2^(eta+2)/(2+2j-eta)].              (10)

To verify (10), partition into the half-radius disks about0 and (0,1), the remaining subset of |Y|<=2, and |Y|>2. On the first two disks use respectively |Y-(0,1)|>=1/2 and |Y|>=1/2. On the remaining bounded set use |Y-(0,1)|>=1/2, |Y|^eta<=2^eta and area<=4 pi. On the last set use |Y-(0,1)|>=|Y|/2. All four terms are nonnegative upper bounds; no cancellation is used.

Outside the support of chi0, (1), (B) and (9) give

 ||Gamma_.(t)||_(R*) <= Aplus(F0+2F1) exp((k-35/8)t),     (11)

since eta/2-2=-11/8. On each intervening compact t interval the functional norm is bounded by (3) and the boundedness of A,A',chi0 and c.

## Jet inputs: a direct modal computation

For beta in B the pointwise bounds from the scalar Hardy space are

 |beta(t)|<=Bminus ||beta||_B for t<=0,
 |beta(t)|<=Bplus exp(-27t/8)||beta||_B for t>=0,           (12)

where one can take Bminus=sqrt(3) sup_(t<=0)|H(t)| and
Bplus=(2 kappa)^(-1/2) sup_(t>=0) exp((3-k)t)|H(t)|,
kappa=3/8+k. Indeed z(t)=J+integral_-infinity^t z' on the left and z(t)=-integral_t^infinity z' on the right; Cauchy-Schwarz with omega gives (12). In particular beta is continuous and locally H1.

For h=E beta, angular differentiation gives

 partial_x h=r^2[(beta+beta'/4)sin(2theta)+(beta'/8)sin(4theta)].

Here beta' is d/dt. Define

 I2(r)=integral_r^infinity s beta(log s)ds,
 I6(r)=integral_0^r s^5 beta(log s)ds,
 I8(r)=integral_0^r s^7 beta(log s)ds.

All integrals exist by (12). Solving the two radial Poisson equations with the canonical end conditions gives

 psi2=(r^2 I2-r^(-2)I6)/8,
 psi4=-r^(-4)I8/8.

The integrations by parts used here have vanishing end terms: r^6 beta and r^8 beta vanish at0, while beta and r^2 beta vanish at infinity. The velocity and its radial derivative on the axis are therefore

 V_beta(t)=T_(E beta)(r)/r=I2/4-r^(-4)I6/4+r^(-6)I8/2,
 V_beta'(t)=r^(-4)I6-3r^(-6)I8,
 c[E beta]=(1/4)integral_0^infinity s beta(log s)ds.        (13)

These identities first follow for smooth beta with the end bounds and then by local H1 approximation and (12). They also follow from the absolutely integrable axis kernel and its first derivative. Thus they agree with the canonical trace, not a separately chosen radial inverse.

For t<=0, (13) implies

 |V_beta-c[E beta]| <= (11/48)Bminus exp(2t)||beta||_B,
 |V_beta'| <= (13/24)Bminus exp(2t)||beta||_B,
 |c[E beta]| <= (Bminus/8+2Bplus/11)||beta||_B.            (14)

The first two bounds use absolute values on the three past integrals. For example

 V_beta-c[E beta]=exp(2t) integral_0^infinity
   [-exp(-2u)/4-exp(-6u)/4+exp(-8u)/2] beta(t-u)du.

Formula (2) and (14) prove a finite constant Cminus,B such that

 ||Gamma_(E .)(t)||_(B*)<=Cminus,B exp(2t)                 (15)

for sufficiently negative t. If chi0=1 on [0,1], a valid explicit constant is

 Cminus,B=(63 A0+11 A1)Bminus/48
                  +(4/3)A1(Bminus/8+2Bplus/11).

For t>=0 let q=27/8 and

 D6=Bminus/6+Bplus/(6-q),
 D8=Bminus/8+Bplus/(8-q),
 CV=Bplus/[4(q-2)]+D6/4+D8/2,
 CVprime=D6+3D8.

Splitting the moments in (13) at0 gives

 |V_beta(t)|<=CV exp(-11t/8)||beta||_B,
 |V_beta'(t)|<=CVprime exp(-11t/8)||beta||_B.               (16)

For instance r^(-4)I6<=D6 exp(-(q-2)t)||beta||_B; the contribution of s<1 has the faster decay exp(-4t). Outside the support of chi0, (1) or (2) without the c terms, (B) and (16) yield

 ||Gamma_(E .)(t)||_(B*)
       <=Aplus(CV+2CVprime)exp((k-35/8)t).                (17)

Again the functional norms are bounded on compact t intervals. This proof does not require classical angular derivatives of arbitrary remainder inputs or an additional derivative of beta.

## Hilbert-Schmidt conclusion and its meaning

For either Hilbert input space Q=R or Q=B, evaluation of Gamma at each t is a bounded linear functional. The preceding estimates give a measurable upper bound D_Q(t) with

 integral D_Q(t)^2 g(t)dt < infinity.

At the left end the integrand is O(exp((7/2)t)). At the right end it is O(exp(2(k-1)t)), which is integrable because k<1. On compact intervals it is bounded. Let (e_n) be an orthonormal basis of Q. Tonelli and Parseval for the Riesz representer of the evaluation functional give

 sum_n ||Gamma(e_n)||_G^2
   =integral sum_n |Gamma(e_n)(t)|^2 g(t)dt
   =integral ||Gamma_.(t)||_(Q*)^2 g(t)dt < infinity.

Thus both components are Hilbert-Schmidt. Their direct sum is Hilbert-Schmidt X0->G, and composition with the bounded inclusion Z->X0 is compact (indeed Hilbert-Schmidt).

To identify this map with P_J C under (E0), work first on the smooth core. The remainder in the decomposition C h=E gamma+f_R cannot have a nonzero smooth x^2 coefficient on an axis segment: its squared R norm would contain the divergent integral of |x|^(4-2a). Hence gamma equals (1) almost everywhere on that segment. Exhaust the positive axis and pass to the Z->Y extension by density. The compact map constructed here is therefore the only possible jet coordinate of that extension.

The result establishes the complete axis compactness hypothesis, including both endpoints and jet inputs. It does not establish that C h-E Gamma_h lies in R, its boundedness, the Garding inequality for that remainder, a positive numerical margin, or injectivity. Those are separate requirements of the conditional Fredholm theorem.

## Verification evidence

The accompanying script checks the two radial Poisson identities, the axis formulas, the strain kernel and all rational exponents symbolically. It encloses the explicit universal constants M3 and the right side of (10) with independent Arb calculations at384 and768 bits. These constants are upper bounds for trace operators, not measured values for the modal background.

Dependencies: proof 01 (canonical signs), proof 38 (B and its Hardy estimates), proof 44 (spaces, bounded strain and the conditional Fredholm theorem), and the independently checked modal endpoint expansions. The computed universal upper bounds are M3<20.3, F0<4 and F1<15; the smaller values recorded in evidence/check.json are bounds from (6) and (10), not sharp operator norms.

Verdict: CONFIRMED with hypotheses (A) and (B) as explicitly stated; identification with the jet coordinate of C is conditional only on its separately required Y-valued extension (E0).
