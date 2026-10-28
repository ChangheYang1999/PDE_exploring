# The low/high nonlinear estimate for the decoupled family

## Exact spaces and claims

Fix a in [18/5,4]. Use X_a=B direct-sum R_a and Y_a=G direct-sum R_a from topics168 and171. In particular the radial exponents are beta_0=17/2 and eta=37/20, independently of a, and the scalar target weight is e^(-t/2) on t<0 and e^(123t/20) on t>=0. The scalar domain B is the fixed integrating-factor space, equivalently R chi_0 plus H1(G). Its origin coordinate J is continuous.

Use the actual high space H_full=B_H direct-sum X_s of proof 171, with fixed sigma=25/4, delta=9/5, gamma=-1/2 and s_0=41/20. The high target is Y_H=Gamma_H direct-sum X_s. All densities are even in x and odd in y. The velocity U is the canonical full-plane IPM operator, and

 W[d]=U[d]+c[d]X/3.

There is a finite constant C_a such that

 ||W[d].grad f||Y_a<=C_a||d||X_a||f||H_full.             (1)

Every product in (1) has its canonical distributional meaning and its exact axis decomposition. No derivative of the low input d is required. The constants may depend on the fixed high cutoffs and weights and on a.

For the exact moving-tail operators A_h of proof 167, on a sufficiently small fixed H_full ball whose parameters lie in I,

 ||(A_h1-A_h0)f||Y_a
       <=C'_a||h1-h0||X_a||f||H_full.                  (2)

The exact fixed-forcing identity F_ell(h)(rho_ell(h)+h)=F_ell0(rho_0)+A_h h holds in Y_a. Combined with proof 171, the conditional two-norm iteration is valid with these weaker low spaces. This result does not prove injectivity, compute a high forcing norm, or verify the iteration's numerical smallness conditions.

## Reducing the high space to two elementary pieces

Let p(X)=x^2 y, p_theta=cos(theta)^2 sin(theta), b(t)=e^(3t)a_H(t). A bounded decomposition of any f in H_full is

 f=f_base+f_bulk,
 f_base=p[J chi_0+a_H u], u in H^sigma(R times S1),
 f_bulk=b v, v in H^(s_0)(R times S1),
                 supp v subset {|cos(theta)|>=epsilon}, (3)

with |J|+||u||Hsigma+||v||Hs0<=C||f||H_full for one fixed epsilon>0. To construct it, write the scalar coordinate as J chi_0+a_H beta_1 and the remainder as b v_0. Choose a smooth angular cutoff eta_0 equal to one on a smaller vertical sector and supported where the cofactor norm in X_s is available. Set u=beta_1+eta_0 v_0/p_theta and v=(1-eta_0)v_0. Multiplication by the cutoffs is bounded in the fixed Sobolev spaces. The cofactor has H^sigma regularity on this support by definition, beta_1 is in H^(sigma+1), and H^{s(.)} embeds into H^(s_0). This proves (3), with the required parity. The division never meets the horizontal axis.

Fourier Cauchy-Schwarz on the two-dimensional cylinder bounds five continuous derivatives of u because sigma>6. Thus f_base has cofactor

 B_f=J+O(r^delta) at0,
 B_f=O(r^(gamma-3)) at infinity,                        (4)

with every cylinder derivative needed below through order five. The constants are bounded by its norm in (3). The bulk function has the annular C1,alpha bounds

 |f_bulk|<=C b(log R), |grad f_bulk|<=C b(log R)/R
                                                       (r comparable to R),

for any 0<alpha<s_0-2=1/20, with the corresponding scaled seminorm. It vanishes on a fixed angular neighborhood of the vertical axis.

The exact high-to-low norm comparison follows either from proof 168 or directly from (3). The two radial logarithmic powers for f and its bounded-tangent-field transport image are

 2delta+8-beta_0=31/10>0 at0,
 2gamma+2-eta=-17/20<0 at infinity.                     (5)

Evenness gives the additional cos(theta)^2 in the base remainder after subtracting its axis cofactor. Its angular integral is I_a=2 Beta((9-2a)/2,3/2), which is finite for every a under consideration. The scalar coordinate belongs to B by (4),(5). These arguments also show that every H_full element belongs to the low graph domain of each normalized transport field in proof 171.

## Axis trace of the low input

Write d=E beta_d+u_d. Proof 168 proves for the R_a component, and its explicit two-mode moment formulas prove for the B component,

 |T_d(r)/r-c[d]|+|T_d'(r)-c[d]|<=C_a r^2||d||X_a,
                                                       0<r<=1,
 |T_d(r)/r|+|T_d'(r)|<=C_a r^(-43/40)||d||X_a,
                                                       r>=1,             (6)

where T_d(y)=U_2[d](0,y). For the jet part, the B norm bounds beta_d at the inner end and gives beta_d=O(r^(-123/40)) at the outer end. Inserting these bounds in P,Q,S of proof 168 proves (6) directly. The derivatives involved contain the moment integrals and r^2 beta_d, not an uncontrolled second derivative of beta_d.

For the remainder part, the first line of (6) uses the split |Z|<=2r and |Z|>2r. The local scaled dual norms are O(r^(9/4)), while the separated odd-kernel remainder is O(r^2) because beta_0>8. Local first and second axis traces are bounded because a>3. No uniform third trace is used; that assertion is false by V173.

Let A_f(t)=B_f(t,pi/2). The exact scalar coordinate of W[d].grad f_base is

 Gamma=(A_f+A_f')T_d/r-2A_f T_d'
                                  +c[d](A_f+A_f'/3)
      =(A_f'-A_f)(T_d/r-c[d])
         -2A_f(T_d'-T_d/r)+(4/3)c[d]A_f'.               (7)

This follows by expanding f_base=x^2 rho_2(y)+O(x^4), using partial_x U_1=-partial_y U_2 and rho_2(y)=y A_f(log y), and including the normalization term. Equations (4),(6) make (7) O(r^delta) at0 and O(r^(gamma-3)) at infinity. The squared G integrals are exactly (5), so its norm is bounded by the product of the two input norms. For f_bulk the scalar coordinate is zero because the product vanishes near every nonzero vertical-axis point.

## The base remainder estimate

First retain the cutoff normalization [U[d]+chi_0 c[d]X/3].grad f_base and subtract (7) with the same cutoff. For d=E beta_d, the explicit angular-polynomial formulas for its velocity give a linear strain plus O(r^3) at0. The normalized linear strain annihilates p. The output cofactor after its axis subtraction therefore has an extra cos(theta)^2 and physical size O(r^(3+delta))+O(r^5) at0. At infinity the velocity is O(r^(-3/40)), so the output has size O(r^(gamma-43/40)). Its squared outer radial logarithmic exponent is 2gamma-2<0. These bounds are linear in ||beta_d||B and the base high norm. This proves the jet-input part.

For d=u_d in R_a, decompose input and output into dyadic radial annuli. Write w_a=|x|^(-2a)W_a(r), where W_a=r^(2a-beta_0) inside and r^(2a-eta) outside. On comparable annuli, W_a is comparable to its central value with constants independent of radius. The local vertical-strip theorem of proof 23 applies because 5/2<a<9/2. The radial-versus-vertical lift correction uses only the first derivative of the scalar row, hence at most T_d'' and three derivatives of f_base. The bounded scaled C5 norm established above is sufficient. The resulting same-scale operator norm is at most

 C_a R^2 at the inner end, C_a R^(gamma-1) at infinity,

times the high norm. These factors are bounded, and the enlarged input annuli have finite overlap. This proves the comparable-scale part.

For smaller separated inputs, the weight-independent, parity-reflected kernel after the axis subtraction has bound

 C Q(theta)d_f(r)r^(-3),
 Q(theta)=|cos(theta)|^4|sin(theta)|,
 d_f(r)=r^3 (r<=1), d_f(r)=r^gamma (r>=1).

The input inverse-weight volumes are bounded by C r^(beta_0+2) or C r^(eta+2), respectively. The resulting squared Hilbert-Schmidt radial integrals are

 integral_0^1 r^3 dr + integral_1^infinity r^(2gamma-3)dr. (8)

The compactly supported normalization term may be kept separately as a bounded rank-one map; its remainder has the same inner cancellation.

For larger separated inputs |Z|>4r and r<=1, the kernel bound is

 C Q(theta)[r^(3+delta)|Z|^(-3)+r^5|Z|^(-5)].            (9)

To obtain it, subtract the exact axis value of the linear source-free velocity. Its action on Jp is constant in the cofactor and disappears in the subtraction. The high cofactor error contributes r^(3+delta); the next odd velocity Taylor term contributes r^5. Every kernel differentiation here is on a separated region. The worst squared input radial exponent near0 is beta_0-9=-1/2>-1; at infinity the weaker kernel has exponent eta-5=-63/20<-1. Hence the input integrals are uniformly bounded for r<=1. The output integrals in dr are

 integral_0^1 [r^(7+2delta-beta_0)+r^(11-beta_0)]dr,
                                                       (10)

whose powers are 21/10 and 5/2. For r>=1, the bound C Q(theta)r^gamma |Z|^(-3) gives the outer integral in (8). The angular square integral of Q against w_a is I_a throughout. This proves the separated-scale estimates.

Finally the omitted full-strain term is (c[d]/3)(1-chi_0)X.grad f_base. It vanishes near0, its remainder has the extra cos(theta)^2, and its outer squared logarithmic exponent is the second one in (5). Its scalar coordinate has the same exponent. This completes (1) for the base piece.

## The bulk remainder estimate

There is no axis row for f_bulk. The jet-input velocity satisfies |U[E beta_d]|<=Cr inside and <=Cr^(-3/40) outside, and the full strain is bounded by Cr everywhere. The annular derivative envelope from (3) and the two powers in (5) prove its product estimate.

For u_d in R_a, the full scalar strain is again treated with (5). On comparable annuli the input weight is bounded below by C r^(-beta_0) or C r^(-eta); on the bulk output it is also bounded above by a fixed multiple of that radial weight. The ordinary unweighted L2 multiplier bound for the localized U therefore gives a weighted L2 estimate there. Multiplication by grad f_bulk costs at most C r^(2+delta) inside and C r^(gamma-1) outside. Finite annular overlap proves the same-scale bound.

For smaller input radii, oddness in source y permits subtraction of the kernel at Z=0. The product kernel is bounded by C b(log r)r^(-4)|Z|. Integrating |Z|^2 against the inverse input weight gives C r^(beta_0+4) inside and C r^(eta+4) outside. The squared Hilbert-Schmidt radial integrals are

 integral_0^1 r^(3+2delta)dr
                    +integral_1^infinity r^(2gamma-3)dr. (11)

For larger input radii, parity makes the velocity at X=0 vanish. Subtracting that kernel value gives product bound C b(log r)|Z|^(-3). The source integral is bounded for r<=1 and is O(r^(eta-4)) for r>=1. The resulting radial integrals are

 integral_0^1 r^(7+2delta-beta_0)dr
                    +integral_1^infinity r^(2gamma-3)dr. (12)

They all converge. No singular weight theorem or A2 property was assumed. Combining (7)-(12) with (3) proves (1).

The estimates extend from smooth parity-preserving approximants by density. Low velocities converge in local L2 and in the trace pairings (6). The high base converges in local C5 and the bulk in local C1. Thus the limit is the canonical locally integrable product, with scalar row (7), and no axis-supported distribution. The weighted bounds give its Y_a membership.

## Moving-tail difference and conditional iteration

The scalar inverse n(ell(h))=c[h], n'>=3 gives

 |ell(h1)-ell(h0)|<=||c||_(X_a*)||h1-h0||X_a/3.          (13)

Set d=h1-h0 and z=rho_ell(h1)-rho_ell(h0). The exact identity is

 (A_h1-A_h0)f=W[d].grad f+W[z].grad f
                     +U[f].grad z+c[f](m(ell(h1))-m(ell(h0))). (14)

The first term is (1). The direct finite-band coefficient estimates of proof 171 bound the second as H_full->Y_a by C|ell(h1)-ell(h0)|; its central strain annihilates p and its far normalized coefficient is bounded. For the third, (12) of proof 171 bounds the cutoff-normalized coupling on X_a. Removing the cutoff term gives only a compactly supported smooth vector times c[f], because z vanishes near0; hence it has the same bound. The last term uses the smooth Y_a-valued m family. Equations (13),(14) and H_full->X_a prove (2).

Let eta_H=||F_ell0(rho_0)||Y_H. Suppose base low injectivity is certified and let K_H,K_L be uniform high and low inverse constants from proof 171 on an H_full ball of radius r. Let C'_a be the constant in (2). If

 K_H eta_H<=r, K_L C'_a K_H eta_H<1,                    (15)

and the ball stays inside the scalar interval and the inverse radius, then the exact iteration

 h_0=0, h_(j+1)=-A_hj^(-1)F_ell0(rho_0)

stays in the high ball and contracts successive differences in X_a. Subtract the two consecutive equations, apply the low inverse and (2), and use ||h_j||H_full<=K_H eta_H. This gives the contraction factor in (15). Strong convergence in X_a and weak subsequential compactness of the high Hilbert ball identify a common limit in H_full. Equation (2) passes the operators to the limit in H_full->Y_a, and weak continuity of the fixed A_h:H_full->Y_a passes the equation. Thus the limit solves the exact profile equation. If K_L C'_a r<1, the same difference argument proves uniqueness within this fixed-tail high ball.

To restore the unit cubic coefficient, also require ||J||_(H_full*)K_H eta_H<1. The high regularity gives a classical coefficient 1+J(h)>0. The exact scaling lambda=sqrt(1+J(h)) then yields rho_norm(X)=lambda(rho_ell(h)+h)(X/lambda). It preserves c and ell and changes the leading tail amplitude by lambda^(1-1/ell). The conclusion does not keep that amplitude fixed after this final normalization.

## What is and is not certified

The new low spaces support the product estimate, the moving-tail difference, the exact normalization and the conditional iteration. Their low residual upper bound is V174: ||F||Y_a<485.632. It is not eta_H in (15). The high norm eta_H is finite by proof 167 but has not been quantitatively certified. Actual base injectivity, K_H, K_L, C'_a, the coefficient radius and every inequality in (15) remain open. Reducing a low residual bound does not on its own reduce the high forcing norm or prove closure.

Dependencies: exact spaces and mappings in topics168 and171; the local strip theorem23; moment formulas46-47; the explicit separated-kernel construction48; actual high space123; the smooth moving-tail algebra167. All endpoint powers affected by the new weights have been recomputed in this proof. The accompanying exact-rational audit checks these powers and the condition ranges, not the analytical estimates themselves.

Verdict: CONFIRMED as a low/high mapping theorem and a conditional nonlinear implication. No exact profile existence is established here.
