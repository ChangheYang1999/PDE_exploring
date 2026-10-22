# Homogeneous test functions, the strain identity, and their exact scope

Date:2026-10-20. Status: CONFIRMED by the independent verifier; actual Opus72 returned no audit text (provider refusal), not an endorsement. No existence or nonexistence endpoint.

## 1. Hypotheses and statement

Let beta>=2, nu=1/beta. Assume the smooth B2 equations and parity, V=U-U(0), div V=0, -curl V=Omega, W=beta X+V. Near0 assume V=O(r), Omega=O(r), Theta=O(r^2). At infinity assume

    V=O(r^(1-nu)), Omega=O(r^-nu), grad Omega=O(r^-1-nu),
    Theta=O(r^(1-2nu)), grad Theta=O(r^-2nu).

The canonical relative inverse is V(X)=integral D(X,Y)Omega(Y)dY, where

    K(Z)=(Z_2,-Z_1)/(2 pi |Z|^2),
    D(X,Y)=K(X-Y)-K(-Y)=K(X-Y)+K(Y).

Let f be smooth off0, homogeneous of degree -k, and odd under x-reflection. Put g=partial_x f. Then, with absolutely convergent integrals,

    [1-(2-k)beta] integral f Omega
       = integral Omega V.grad f - integral Theta g,             (I_k)

for 2-nu<k<3, and

    [(2-k)beta-2] integral g Theta
       = - integral Theta V.grad g,                             (J_k)

for 2-2nu<k<3. The open ranges are sufficient absolute-convergence ranges, not claims of necessity for each specially cancelling field. Both statements include beta=2: the lower endpoints are3/2 and1 respectively.

For f=K_c=xy/r^4, g=y(y^2-3x^2)/r^6, the center inverse gives integral K_c Omega=pi c with c=1+beta/2. Consequently

    pi(1+beta/2)=integral Omega V.grad K_c
                       -(1/2) integral Theta V.grad(partial_x K_c).       (S)

## 2. Proof with boundary terms

Work first on eps<r<R. Since div W=2beta and X.grad f=-kf,

    div(fW)=(2-k)beta f+V.grad f.

Multiply W.grad Omega+Omega=Theta_x by f and integrate by parts. The bulk terms give (I_k). Near0 the three integrands, including plane measure dr dtheta, are O(r^(2-k))dr. At infinity f Omega is O(r^(1-k-nu))dr, whereas Omega V.grad f and Theta g are O(r^(1-k-2nu))dr. Thus the asserted I_k range makes all terms absolutely integrable. The vorticity boundary flux f Omega W.n dS is O(eps^(3-k)) at0 and O(R^(2-k-nu)) at infinity. The boundary flux from integrating Theta_x is smaller at infinity, O(R^(2-k-2nu)), and has the same inner bound. All vanish.

Similarly div(gW)=(1-k)beta g+V.grad g. Multiplication of W.grad Theta=(beta-2)Theta by g gives

    [(beta-2)+(1-k)beta] integral g Theta=-integral Theta V.grad g.

The first integrand is O(r^(2-k))dr near0 and O(r^(1-k-2nu))dr at infinity. The second is O(r^(2-k))dr near0 and O(r^(1-k-3nu))dr at infinity. The scalar boundary flux g Theta W.n dS is O(eps^(3-k)) and O(R^(2-k-2nu)). This proves J_k and all claimed convergence statements. Taking k=2 gives integral Theta g=(1/2)integral Theta V.grad g, which substituted in I_2 proves S. No sign of either term on its right is proved.

## 3. Absolute double integrals and correct homogeneity

Define A(X)=integral |D(X,Y)||Omega(Y)|dY. For r=|X|<=1/4, split the Y-integral at2r and1. On |Y|<2r, |Omega(Y)|<=C r and integration of |K(X-Y)|+|K(Y)| gives O(r^2). On2r<|Y|<1 the mean-value estimate |D(X,Y)|<=Cr/|Y|^2, together with Omega(Y)=O(|Y|), gives O(r). On |Y|>1 the same estimate and decay give O(r). Hence A(X)<=Cr.

For r>=2, split at |Y|=r/2 and2r. The inner region is bounded by integrating (C/r+C/|Y|)|Omega(Y)|, giving O(r^(1-nu)); the comparable annulus is bounded using |Omega(Y)|<=Cr^-nu and local integrability of the kernel, with the same result. The outer region gives Cr integral_(2r)^infinity s^(-1-nu)ds=O(r^(1-nu)). The intermediate compact annulus is harmless. Thus A has the same bounds used above for V, without relying on cancellation inside the outer Y-integral.

It follows that integral integral |Omega(X) D(X,Y).grad f(X) Omega(Y)|dYdX is finite for max(2-2nu,0)<k<3; the displayed lower bound0 is merely unnecessary slack when beta>=2, where2-2nu>=1. The mixed integral with Theta(X)grad g(X) instead of Omega(X)grad f(X) is finite for2-3nu<k<3. In particular both are absolutely convergent at k=2. Fubini and swapping X,Y are therefore valid for the full grouped kernels. The vorticity term equals

    (1/2) integral integral Omega(X)Omega(Y)
      { K(X-Y).[grad f(X)-grad f(Y)]
          +K(Y).grad f(X)+K(X).grad f(Y) } dXdY.                (A)

The terms within braces must remain grouped; they need not have separate absolute integrals. The mixed term is exactly

    integral integral Theta(X)Omega(Y) D(X,Y).grad g(X)dXdY.   (B)

The kernel in A has joint degree -k-2, hence degree -4 for K_c, not degree -3. The kernel in B has joint degree -k-3, hence degree -5 at k=2. Under X->l X, Omega->Omega(X/l), Theta->l Theta(X/l), l>0, both complete terms in S are invariant, as is c. This checks the powers independently. No symmetry permits dropping the K(Y),K(X) subtraction terms.

## 4. Why S alone imposes no useful sign restriction on temperature

Fix any smooth odd vorticity with the preceding bounds and nonzero c, and with canonical V satisfying DV(0)=diag(-c,c). Let g=partial_x K_c and L(X)=V.grad g. On the axis,

    g(0,y)=y^-3,   grad g(0,y)=(0,-3y^-4),
    L(0,y)=-3c y^-3+O(y^-2).

For small y>0 and y<0 this has opposite signs. By continuity, choose two small off-axis balls on which L has opposite signs, and their reflected partners. Nonnegative even-in-x smooth bumps B_+,B_- supported there satisfy integral B_+ L>0 and integral B_- L<0. They vanish near the axis and center.

Start from any smooth nonnegative Theta_0 with the required a0>0 center jet, vanishing on the axis, and the stated far-field bounds. Given any real target value for integral Theta L, add a suitable nonnegative multiple of one of these two bumps. This keeps nonnegativity, axis vanishing, center jet and far field while attaining that target. In particular S can always be imposed this way for the fixed Omega. This does not retain the temperature transport equation, J_k, or other PDE-derived integral identities. Therefore it refutes only an exclusion based on S and nonnegative temperature alone. It is not a counterexample to the B2 problem or to the simultaneous full family of identities.

## 5. The full Mellin family retains the differential equations

Assume also D^2 Theta=O(r^-1-2nu), DV=O(r^-nu) at infinity, and the corresponding smooth local jets. For arbitrary such fields, define

    Rv=W.grad Omega+Omega-Theta_x,
    Rt=W.grad Theta-(beta-2)Theta.

The same integrations by parts show that I_k for every smooth odd angular test f=r^-k phi(theta) is exactly integral f Rv=0. Here Rv=O(r) near0 and O(r^-nu) at infinity. Fix k0 inside (2-nu,3). For an angular test phi, the function

    F_phi(z)=integral r^(1-z) phi(theta) Rv(r,theta) dr dtheta

is holomorphic in this strip, by dominated differentiation on compact substrips (each logarithmic factor is absorbed by the strict endpoint margins). If I_k holds for every real k in an open interval, the identity theorem makes F_phi identically zero. On z=k0+is it is the Fourier transform in t=log r of an L1 function. Fourier uniqueness implies that this radial angular average vanishes almost everywhere, hence everywhere by smoothness. Arbitrary smooth odd angular phi and odd parity of Rv imply Rv=0 pointwise.

J_k is exactly integral (partial_x f)Rt=0, hence integral f partial_x Rt=0 after another integration by parts. The inner boundary is O(eps^(3-k)); the outer is O(R^(2-k-2nu)). The derivative partial_x Rt is O(r) near0 and O(r^-2nu) at infinity, so the same Mellin argument on (2-2nu,3) gives partial_x Rt=0. Thus Rt is independent of x. Since Theta(0,y)=0, Theta_y(0,y)=0 and W_1(0,y)=0, Rt(0,y)=0, so Rt=0.

Accordingly all I_k and J_k for all odd angular tests are equivalent to the two transport PDEs in these classes. They are not a finite set of weaker algebraic obstructions. This does not rule out obtaining a useful estimate from a selected test.

## 6. Left-edge residue and dependence

If the stronger known expansion Omega=r^-nu a(theta)+O(r^-2nu) holds, its Mellin transform in Section5 has residue integral phi a at k*=2-nu. Indeed subtract the leading term for r>=1; the remainder integral is holomorphic for Re k>2-2nu, and integral_1^infinity r^(1-k-nu)dr=1/(k-k*). The I_k prefactor is beta(k-k*). Both right-hand integrals converge at k*, by their O(r^(1-k-2nu)) bounds and k*<3 at0. Taking the real limit yields

    beta integral phi(theta)a(theta)dtheta
      = integral Omega V.grad(r^-k* phi)
          -integral Theta partial_x(r^-k* phi).

This is the retained outer critical flux, not a zero boundary term at the endpoint. No further sign or exclusion follows from taking the residue. The canonical inverse and center moment inputs are proved in packets34,40,50,63. The new algebra, absolute Fubini estimate, Mellin equivalence and scope argument are complete above; no numerical evidence is used as proof.

## 7. Independent smooth-blob sign construction

Here beta>2. Write N(Omega)=integral Omega V.grad K_c. Choose a nonnegative radial smooth function eta supported in the unit disk with unit mass. At A=(a,b), A*=(-a,b), a,b>0, put

    Omega_e=Gamma e^-2 [eta((X-A)/e)-eta((X-A*)/e)],

with e small enough that the two supports are disjoint and avoid the axis. The field is positive on its support in x>0 and has the required x parity. Its own velocity around either individual blob is tangent to concentric circles. Since the individual vorticity is radial, div(Omega_blob U_self)=0. Compact support away from the singular point of K_c therefore gives integral Omega_blob U_self.grad K_c=0 exactly, by integration by parts. Every cross-blob and center-evaluation kernel is smooth on the separated supports, so ordinary weak convergence to their masses applies to all remaining terms as e tends to0. This avoids interpreting point vortices as smooth fields.

The limiting other-blob velocity at A is (0,Gamma/(4 pi a)). The center velocity is (0,Gamma a/(pi(a^2+b^2))). Also

    partial_y K_c(A)=a(a^2-3b^2)/(a^2+b^2)^3.

The reflected blob contributes equally to N, because both Omega and this component of grad K_c change sign while the vertical velocity does not. Thus

    c_pair=2 Gamma ab/[pi(a^2+b^2)^2],
    N_pair=Gamma^2(b^2-3a^2)(a^2-3b^2)/[2 pi(a^2+b^2)^4].

At b=a, N_pair=pi c_pair^2/2>0. At b=a/2 it is negative, with positive c_pair in both cases. These strict signs persist for small positive e. Omitting the center subtraction instead gives Gamma^2(a^2-3b^2)/[2 pi(a^2+b^2)^3], which has the opposite sign at b=a. This independently verifies the significance of the gauge subtraction.

For the prescribed c*=1+beta/2>2, choose b=a and normalize the smooth blobs by a positive constant to have c=c* exactly. The limit of N is pi c*^2/2>pi c*, so e can be fixed such that N>pi c*. Supply the local jet and a positive algebraic tail using q=(1-nu)/2 and

    Psi_t=-x(1+r^2)^q,
    Omega_t=-Delta Psi_t=4q x(1+r^2)^(q-2)[2+(q+1)r^2].

Here Omega_t>0 for x>0, Omega_t,x(0)=8q, and its leading tail is4q(q+1)r^-nu cos(theta). Its relative velocity has zero derivative at0, center strain0, and growthO(r^(1-nu)). It is the canonical relative inverse: both fields have the same divergence and curl, both are sublinear, and their difference is an entire harmonic vector field vanishing at0. The interior harmonic gradient bound and sublinear growth make that difference constant, hence zero.

Add mu Omega_t to the normalized blob field with small mu>0. The center strain remains c*, and N remains larger than pi c* by continuity of its absolutely convergent quadratic expression. Set a0=2 beta q mu and Theta_0=a0 x^2(1+r^2)^(-(1+2nu)/2). Then Omega_x(0)=4a0/beta, the temperature jet is a0x^2, Theta_0 and Omega are strictly positive on x>0, and Theta_0,xx(0,y), Omega_x(0,y) are positive for every y. The fields obey the stated polynomial tail and derivative bounds. The mixed functional B(Theta_0)=integral Theta_0 V.grad g tends to0 as mu tends to0. Reduce mu until 2(N-pi c*)-B(Theta_0)>0.

Section4 supplies a nonnegative even bump H, supported away from the axis and center, with B(H)>0. Choose its positive multiplier to make

    B(Theta_0+tH)=2(N-pi c*).

This proves (S) exactly while retaining all the local, tail and positivity properties just listed. No transport equation is asserted. In particular this does not assert either I_2 or J_2 separately, absence of other equilibria, or simultaneous validity of the quotient identities. It proves that (S), the inverse, these jets, and these positivity and tail conditions alone have no inconsistency. The beta=2 limiting margin vanishes in this construction, so this paragraph asserts the construction only for beta>2.

## 8. Direct quantitative strain bound

If Q=Omega/x, Lx=sup|Q| and Ax=sup r^(1+nu)|Q| are finite, then

    |c| <= [4(beta+1)/(3pi)] Lx^(1/(beta+1)) Ax^(beta/(beta+1)).

Indeed |Omega(r,theta)|<=|cos(theta)| min(Lx r,Ax r^-nu). Substitute into the absolute center moment and use integral_0^(2pi) cos^2(theta)|sin(theta)|dtheta=4/3. The radial integral is bounded by Lx R+(Ax/nu)R^-nu. With R=(Ax/Lx)^(1/(1+nu)) this is (beta+1)Lx^(1/(beta+1))Ax^(beta/(beta+1)). The zero-field case is immediate. The product on the right is invariant under the allowed spatial scaling, since Lx scales by |l|^-1 and Ax by |l|^nu. No upper estimate for this invariant product has been derived from the profile PDE; the inequality is a necessary size lower bound once c=1+beta/2 is imposed, not a full exclusion.

## 9. Shape dependence of concentration and explicit failure of both PDEs

The radial qualification in Section7 cannot be omitted. More generally let eta be any nonnegative smooth unit-mass function supported in the unit disk and let omega_e(X)=Gamma e^-2 eta((X-A)/e), with A away from0. Its own uncentered velocity is u_e=K*omega_e. For every C2 function f near A, antisymmetry of K gives

    integral omega_e u_e.grad f
      = (Gamma^2/2) integral integral eta(z)eta(w) K(z-w).
          [grad f(A+ez)-grad f(A+ew)]/e dzdw.

Taylor's integral formula bounds the bracket by C|z-w|, and |K(z-w)|=1/(2pi|z-w|). Dominated convergence therefore gives the generally nonzero limit

    (Gamma^2/2) integral integral eta(z)eta(w)
          K(z-w).D^2f(A)(z-w) dzdw.                         (C)

For a radial eta the law of z-w is rotation invariant. The angular average of K(v).Hv is zero for every symmetric matrix H, so (C)=0, in agreement with the exact radial cancellation. General shapes need not have that cancellation. If H has entries h11,h12,h22, the integrand without its mass weights is

    [(h11-h22)v1 v2+h12(v2^2-v1^2)]/(2pi|v|^2).

It is bounded by sqrt(((h11-h22)/2)^2+h12^2)/(2pi), but has either sign as the separation direction changes. This supplies a direct bound for the concentration defect and explains why weak convergence of the masses alone is insufficient for this quadratic functional.

Here is a concrete smooth counterexample to a shape-independent version of Section7. Put A=(a,a). Replace the right macro-blob by two radial blobs of masses Gamma/2 at A plus or minus (e/2,0), each of radius e^3, and reflect them with negative sign across x=0. Each own self term is exactly zero. The mutual term within the right cluster tends to

    (Gamma^2/4) K(e,0).[grad K_c(A+(e/2,0))-grad K_c(A-(e/2,0))]
      -> -Gamma^2 (K_c)_{xy}(A)/(8pi)
       = -3Gamma^2/(32pi a^4).

Replacing these two small blobs by their centers in this mutual expression has error tending to0: after symmetrization its local kernel is bounded and its derivative at separation e is O(1/e), so displacements O(e^3) cause O(e^2) error. Reflection gives the same limit for the left cluster. Cross-cluster and center-subtraction kernels remain smooth and retain the Section7 limits. The full N therefore tends to

    Gamma^2/(8pi a^4)-3Gamma^2/(16pi a^4)
      = -Gamma^2/(16pi a^4),

whereas the single radial macro-blobs gave +Gamma^2/(8pi a^4). Both sequences converge weakly to the same signed point masses, with the same limiting strain. This refutes only the assertion that arbitrary smooth concentration has the radial limit.

The structural construction in Section7 also fails both transport PDEs, as can be shown without a numerical test. All compact perturbations vanish at (x,0) for sufficiently large x>0. The tail stream is odd in x and even in y, so its horizontal relative velocity is zero there, as are Theta_{0,y} and Omega_{t,y}. The compact odd blob field has total mass zero, hence its horizontal velocity is O(x^-2); subtracting its center velocity changes only the vertical component. Set s=(1+2nu)/2. Direct differentiation yields

    beta X.grad Theta_0-(beta-2)Theta_0
       =(beta+2)Theta_0/(1+r^2).

Thus at (x,0),

    R_Theta/Theta_0=(beta+2)/(1+x^2)
          +V_{b,1}(x,0)[2/x-(1+2nu)x/(1+x^2)]
       =(beta+2)x^-2+O(x^-3)>0.

Likewise Omega=mu Omega_t there has expansion C x^-nu+O(x^-nu-2). The dilation-vorticity terms cancel at leading order, so beta x Omega_x+Omega=O(x^-nu-2). Its advective correction is O(x^-nu-3). On the other hand Theta_x=a0(1-2nu)x^-2nu+O(x^-2nu-2). Since beta>2,

    R_Omega=-a0(1-2nu)x^-2nu+o(x^-2nu) !=0.

These facts strengthen the earlier careful statement that transport was not asserted. They do not strengthen feasibility beyond the single strain identity.

## 10. The singular horizontal test and its boundary orientation

Assume beta>2 and, in addition to the earlier bounds, P=Theta/x^2=O((1+r)^-1-2nu) and v=V1/x=O((1+r)^-nu). These are the quotient estimates already proved for the full class. Put m=2-nu and g=-m x^-m-1 on D={x>0}. The smooth-angular assertion in Section1 does not directly include this singular test. Integrate the temperature equation on D_{e,R}={x>e,r<R}. The same finite-domain integration gives

    [(2-m)beta-2] integral Theta g
       =-integral Theta V.grad g + integral_boundary Theta g W.n.

The coefficient is -1. With the outward normal (-1,0) on x=e, the axis flux has the positive sign

    +m e^(2-m) integral_{|y|<sqrt(R^2-e^2)} P(e,y)[beta+v(e,y)]dy.

Its absolute value is O(e^nu), uniformly in R, because P decays integrably in y and v is bounded. In polar coordinates x=r cos(theta), theta in(-pi/2,pi/2), the two absolute bulk densities at infinity are bounded respectively by

    C r^-2-nu (cos theta)^(1-m),
    C r^-2-2nu (cos theta)^(1-m).

The angular factor is unbounded and must be retained. It is integrable because 1-m=-1+nu>-1. Including plane measure proves integrability at infinity. Boundedness of P,v and the same exponent prove local integrability at the axis and origin. The absolute circular flux is bounded by C R^-nu times that finite angular integral. All boundary terms vanish, in either sequential limit. Substituting Theta g=-m x^(1-m)P and Theta V.grad g=m(m+1)x^(1-m)vP proves

    integral_D x^(1-m)[1+(m+1)v]P=0.

No pointwise uniform angular estimate is used. This section asserts the result only where the quotient bounds are available; it does not introduce them at beta=2 without proof.
