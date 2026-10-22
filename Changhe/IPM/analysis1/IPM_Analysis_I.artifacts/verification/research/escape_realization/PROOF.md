# Outer realization, normalization and escape-weight audit

Status at proof writing: independent mathematical derivations below are complete under their stated hypotheses; computational regression checks and actual-model review are pending. This is topic88, answering V25. No actual global inverse, escape weight, weighted commutator norm or proof endpoint is established.

## 1. Conventions and axis jets

Work on R^2, with -Delta psi=partial_x h and canonical U[h]=(-partial_y psi,partial_x psi). No harmonic polynomial is added. Let sigma[h]=partial_xy psi[h](0), and use the prompt's normalized functional c[h]=sigma[h]/3. Thus the normalization term is c[h]G, G=X.grad rho. This c is not the raw strain sigma. All Taylor expansions below concern smooth functions on a fixed open y-interval and sufficiently small x. For the coefficients through x^4, six continuous x derivatives suffice, and the displayed higher remainders can instead be read under smoothness.

Suppose h is even in x and odd in y, with its x^0,x^2,x^4 jets identically zero on that interval. Then h=O(x^6) locally, Delta U_2=-partial_xx h=O(x^4), and U_2 is even in x. Put B(y)=U_2[h](0,y). The coefficients of x^0 and x^2 in the Laplace equation give, successively,

 U_2=B-x^2 B''/2+x^4 B''''/24+O(x^6).

Divergence freeness and oddness of U_1 in x give

 U_1=-x B'+x^3 B'''/6-x^5 B'''''/120+O(x^7).

If rho=x^2 a_2(y)+x^4 a_4(y)+O(x^6), direct multiplication yields

 U[h].grad rho=x^2 T_2+x^4 T_4+O(x^6),
 T_2=a_2' B-2a_2 B',
 T_4=a_4' B-4a_4 B'-a_2' B''/2+a_2 B'''/3.             (1)

This is a nonlocal trace B. Vanishing input jets do not imply B=0. For a complete example choose a smooth nonnegative nonzero function eta(x,y), even in x and y, supported where 1<|x|<2 and |y|<1/4, and put h=y eta. It vanishes in an entire axis strip, is even in x and odd in y. The off-origin physical velocity kernel is

 K(z)=(1/(2pi))(-2xy/r^4,(x^2-y^2)/r^4),

with an additional local -h/2 in U_2. This local term is zero near the axis for our h. Differentiating K_2 at (0,0)-(u,v) gives

 B'(0)= integral v^2(3u^2-v^2) eta(u,v)/(pi(u^2+v^2)^3) du dv>0.

The integral is absolutely convergent, and its integrand is strictly positive on some open subset of the support. Oddness gives B(0)=0. Choose a smooth parity-preserving rho equal to x^2 y on a neighborhood of the origin. Then T_2=B-2yB'=-B'(0)y+o(y), which is nonzero for all sufficiently small nonzero y. Hence this class of remainder jets is not generally invariant under the IPM coupling. This example alone does not assert a nonzero T_2 for every possible h and the particular numerical trial.

On an interval of y away from zero and the source points, all nonsingular weight factors are bounded above and below. A nonzero leading x^j term belongs locally to L2(|x|^(-2a)dxdy) exactly when 2j-2a>-1, equivalently a<j+1/2. At a=25/4 an x^6 input is integrable, whereas x^4 or x^2 outputs are not. Thus a generic operator on that unprojected remainder space needs a jet correction. This does not by itself specify the correct projected operator or prove its inverse.

## 2. Far resonance and the factor of three

Let k>0 and c_l=1/k. Fix a cone separated from both coordinate axes. Suppose, in angular L2 on that cone, G(r,theta)=k r^k(Theta(theta)+o(1)), with 0<||Theta||_2<infinity. For the weight

 omega=e^phi |x|^(-2a)(1+r^2/L^2)^(a-gamma),

assume phi bounded and L>0. On that cone omega is comparable to r^(-2gamma). Consequently the G tail on this cone is in L2(omega) if and only if gamma>1+k. Indeed the radial integral is comparable to integral r^(2k-2gamma+1)dr. At equality it diverges logarithmically. Divergence on one cone proves global divergence; whole-plane convergence would require complementary angular control. Mere big-O asymptotics would not prove the divergent direction.

The specific negative far transport margin 1-c_l(gamma-1)>0 requires gamma<1+k. These inequalities are incompatible for this unmodified weighted remainder realization. If h is compactly supported, the transport and local multiplication parts vanish far away. If also rho has a globally bounded sublinear gradient asymptotic grad rho=O(r^(k-1)), then U[h].grad rho=O(r^(k-3)) off the support, by the homogeneous order-minus-two kernel and the finite L1 mass of h. It cannot cancel a nonzero c[h]G of order r^k. Thus such an h with c[h]!=0 has Lh outside the forcing space in this realization. The example in section1 has nonzero raw strain: sigma=-B'(0)<0, so nonzero c occurs even for smooth compact inputs with all axis jets zero.

The exact homogeneous identity is

 (c_l r partial_r-1)(r^k log(r)Theta)=c_l r^k Theta.

Solving the leading equation (c_l r partial_r-1)h+c[h] k r^k Theta=0 gives

 h_log=-(c[h]/c_l^2) r^k log(r)Theta
       =-(sigma[h]/(3c_l^2)) r^k log(r)Theta.                (2)

Thus a formula -c[h]/(3c_l^2) is wrong by a factor of three if c denotes the prompt functional sigma/3. It is correct with raw sigma in place of c. SPEC3.16 E2 mixes these conventions; its E5 explicitly identifies c=sigma/3. The correction changes the coefficient, not the far integrability obstruction. Equation(2) is the leading homogeneous response only, not a constructed solution of the full variable-coefficient equation.

## 3. A vanishing source cutoff and its sign

Suppose V is C1 on B_delta(P), V(P)=0, and the symmetric part of DV(P) is at least mu_P I with mu_P>0. If ||DV(X)-DV(P)||_op<=mu_P/2 there, the fundamental theorem of calculus along the segment gives

 w.V(P+w)= integral_0^1 w.DV(P+tw)w dt >=mu_P |w|^2/2.

For a C1 nondecreasing radial chi and zeta=chi(|X-P|/delta), this implies V.grad zeta>=0. The assertion includes the constant inner region of a smooth cutoff. For smooth compactly supported H and positive C1 omega, integration by parts yields

 Re integral zeta^2 omega conjugate(H) V.grad H
 =-1/2 integral zeta^2 div(omega V)|H|^2
  -integral zeta(V.grad zeta)omega|H|^2.                   (3)

For zeta>=0 the second term is nonpositive. No division by zeta is involved. Applying a fractional differentiation operator before this identity and moving it through zeta are different operations; the latter still needs commutator bounds.

For the trial's independently accepted bound M_V<743/2500 on B_(99/2000)(P), the tensor mean-value inequality proves

 sup_B ||DV(X)-DV(P)||_op <=(99/2000)M_V
 <73557/5000000 < (99/100)/2.

The Frobenius norm bounds the tensor contraction by Cauchy-Schwarz. This supplies the perturbation part of the cutoff criterion on this disc if the base-point and symmetric-matrix hypotheses hold with mu_P>=99/100. It does not silently prove those other hypotheses or extend to larger discs.

For M=R_1^2 self-adjoint and nonnegative, any real bounded multiplier m for which the expressions make sense satisfies

 Re<m(-gM f),m f>=-g||M^(1/2)(m f)||_2^2
                    +g Re<[M,m]f,mf>.

This follows by writing mMf=M(mf)-[M,m]f. The first term is favorable; the commutator must still be controlled.

## 4. Explicit unweighted Fourier estimates

Use the unitary Fourier transform with factor(2pi)^(-1) in dimension2. Define

 M_t(b)=integral <p>^t |bhat(p)|dp,
 N_s(b)=integral |p|<p>^(s-1)|bhat(p)|dp,
 D_s(b)=s 2^((s-1)/2) N_s(b)/(2pi).

Constants can be separated off b before computing commutators. Assume all displayed integrals finite. Peetre's inequality <eta+p><=sqrt(2)<p><eta> and Young's convolution inequality imply

 ||bf||_Ht <= 2^(t/2) M_t(b)/(2pi) ||f||_Ht, t>=0.        (4)

For s>=1, the mean-value formula along eta+tp gives

 |<eta+p>^s-<eta>^s|
 <=s|p| sup_(0<=t<=1)<eta+tp>^(s-1)
 <=s2^((s-1)/2)|p|<p>^(s-1)<eta>^(s-1).

Thus ||[J^s,b]f||_2<=D_s(b)||f||_(H^(s-1)). The velocity symbol is m=(n_1n_2,-n_1^2), n=xi/|xi|. Its vector difference has magnitude |sin(angle(xi,eta))|. The elementary direction bound and min inequality proved in topic87 give |m(xi)-m(eta)|<eta><=2<p>, so the looser stated coefficient2sqrt(2) also gives

 ||[U,b]f||_2 <=2sqrt(2)M_1(b)/(2pi)||f||_(H^-1).

Since U commutes with J^s, the exact identity

 J^s[U,b]f=[U,b]J^s f+U[J^s,b]f-[J^s,b]Uf

and the vector bound ||U||_(Hr to Hr)<=1 yield

 ||[U,b]f||_Hs
 <=(2sqrt(2)M_1(b)/(2pi)+2D_s(b))||f||_(H^(s-1)).          (5)

These are global unweighted norms. None is automatically a weighted or degenerate-conormal commutator estimate.

Cauchy-Schwarz and Plancherel give

 M_1(b)<=sqrt(pi)||b||_H3,
 N_s(b)<=M_s(b)<=sqrt(pi/(4-s))||b||_H5, 0<=s<4.

Indeed integral_R2 <p>^(-4)dp=pi and integral_R2 <p>^(2s-10)dp=pi/(4-s), by substituting u=1+r^2 in polar coordinates.

The off-origin velocity kernel above is a rotation and sign change of z^(-2)/(2pi), z=x+iy. Differentiating any multi-index alpha gives complex modulus (|alpha|+1)!/(2pi r^(|alpha|+2)); the same is the Euclidean norm of the two kernel components. Local distributions do not enter separated-support estimates.

For 2<s<4 set q=s/2. Two integrations by parts in the absolutely convergent scalar integral show, for lambda>0,

 lambda^q=1/Gamma(-q) integral_0^infinity (exp(-lambda t)-1+lambda t)t^(-q-1)dt.

The boundary terms vanish at zero and infinity since1<q<2; the resulting factor is Gamma(2-q)/(q(q-1))=Gamma(-q)>0. With lambda=1+|xi|^2, the subtraction terms have kernels supported at zero. The heat kernel gives, for z!=0,

 K_s(z)=1/(4pi Gamma(-s/2))
   integral_0^infinity t^(-2-s/2) exp(-t-|z|^2/(4t))dt.

Dropping exp(-t)<=1 and substituting u=|z|^2/(4t) proves

 |K_s(z)|<=2^s Gamma(1+s/2)/(pi|Gamma(-s/2)|)|z|^(-2-s).   (6)

This proves the cited homogeneous constant is also a valid off-diagonal upper bound for the inhomogeneous operator. It does not bound local singular integrals without cancellation.

## 5. The weighted canonical strain bound

For smooth compact h with h_y(0)=0, the physical convention is

 sigma[h]=-h_y(0)/4-PV integral K_sigma(-X)h(X)dX,
 K_sigma(X)=y(3x^2-y^2)/(pi r^6).

This is topic80's corrected convention. Here |K_sigma|<=1/(pi r^3). For a>2, gamma<2 and phi bounded below, Cauchy-Schwarz gives

 |sigma[h]|<= C_sigma ||h||_L2(omega),
 C_sigma=e^(-inf(phi)/2)L^(a-2)/pi
          sqrt(Beta(a-2,2-gamma)Beta(a+1/2,1/2)),
 |c[h]|<=C_sigma/3 ||h||_L2(omega).                        (7)

To prove the constant, the squared dual-kernel norm is at most

 e^(-inf phi)/pi^2
 [integral_0^infinity r^(2a-5)(1+r^2/L^2)^(-(a-gamma))dr]
 [integral_0^(2pi)|cos theta|^(2a)dtheta].

The substitution u=r^2/L^2 gives the first bracket L^(2a-4)Beta(a-2,2-gamma)/2; substituting v=sin^2(theta) on a quadrant gives the second2Beta(a+1/2,1/2). Their product proves(7). It also proves absolute integrability of the kernel times h in this weighted class. The local derivative term is zero by the stated jet hypothesis; vanishing h(0) alone would not imply h_y(0)=0. For less regular remainders this defines the bounded extension of the strain integral, with identification with the canonical distribution requiring the zero-jet approximation/domain premise.

At a=25/4,gamma=1129/1000,L=1/2,inf phi=0 the constant is a definite positive real. Its numerical directed enclosure is left to the accompanying computation. The larger coefficient C_sigma for c is conservative by3, not false. It bounds the input functional only; it does not place the output G in the forcing space.

## 6. Signed orbit cost, positive cost and compatibility

For an integrable scalar rate g(t), define C=sup_(a<=b)integral_a^b g and C_+=integral g^+. Take g=1 on[0,1] and[2,3], g=-2 on[1,2], and zero elsewhere. Its cumulative primitive has values0,1,-1,0 at0,1,2,3. The largest rise between ordered times is1, so C=1; C_+=2. With N separated unit positive pulses and intervening negative pulses of mass2, the same argument gives C=1,C_+=N. Smooth nonnegative compactly supported bumps with these masses and disjoint ordered supports give the same conclusion, since the primitive is monotone on each pulse. Thus no finite bound on C_+ follows from C alone, even for smooth rates.

Let Phi_t be a complete C1 flow and f>=0 smooth. If the backward integral phi(X)=integral_(-infinity)^0 f(Phi_t X)dt converges and its derivatives can be passed under the integral, then shifting the integration variable gives V.grad phi=f. Any uniform bound by a positive-part orbit integral is a bound on that integral, not on the signed cost without a separate comparison theorem. The derivative assumption is substantive; qualitative flow diagrams do not provide it.

If an orbit joins equilibria P at t=-infinity and O at t=+infinity and A=integral_R f(Phi_t X)dt is finite and positive, then every continuous phi with integrable along-orbit derivative V.grad phi>=f must satisfy phi(O)-phi(P)>=A. Integrate between finite times and take both endpoint limits. If f vanishes at both equilibria, the literal backward integral is zero at O but tends to A along this orbit approaching O. Therefore that literal definition is not continuous at O. Independent zero endpoint normalizations cannot work.

For the linear saddle V=(-alpha x,beta y), alpha,beta>0, the characteristic through the incoming section x=epsilon has label v=y(x/epsilon)^(beta/alpha). Direct differentiation proves V.grad v=0. A transported datum F(v)=v gives phi=y(x/epsilon)^p, p=beta/alpha. If2<p<3 it fails to be C3 at x=0 for nonzero fixed y. An even datum F(v)=v^2 instead has exponent2p in(4,6); for the particular2<p<5/2 it is not C5. Applying(x partial_x)^j multiplies x^p by p^j, so conormal regularity can hold despite this Cartesian obstruction. This is a normal-model example, not a regularity theorem for the actual flow or every datum F.

For completeness, for smooth vector fields Z_i and a word w suppose

 Z_w(f(Phi_t X))=sum_beta A_(w,beta)(t,X)(partial^beta f)(Phi_t X).

The chain and product rules give

 A_(iw,beta)=Z_i A_(w,beta)+sum_j(Z_i Phi_t^j)A_(w,beta-e_j),

with negative indices zero and the empty-word coefficient1. If the absolute sum on the right of the differentiated integrand has a common integrable-in-t bound uniformly in X, dominated convergence proves differentiability and ||Z_w phi||_infinity no larger than its integrated bound. This is an explicit sufficient condition, not data supplied by a trajectory plot.

The reflected scalar construction phi(t)=sup_(a<=t)integral_a^t g, including a=t, satisfies0<=phi<=C whenever C is finite. For continuous g on bounded intervals it is locally Lipschitz: write phi=G(t)-inf_(a<=t)G(a), with the lower envelope finite; the envelope can only decrease while G itself is at its running minimum. Consequently phi'>=g almost everywhere. This does not give transverse differentiability of a family of characteristics or smoothness across separatrices.

If phi is already C1, V.grad phi=0 in a far annulus, V.grad r>0 there, chi(r) is nondecreasing between0 and1, and A>=sup phi, then phi_new=(1-chi)phi+chi A satisfies V.grad phi_new=(V.grad chi)(A-phi)>=0 in that annulus. This conditional algebra does not construct phi or certify the annular hypotheses.

## 7. Noncompactness: exact model spaces and scope

The lead has not fixed the fractional operator A_s. It is therefore necessary to distinguish exact model counterexamples from a claim in an unspecified norm. Let s>=1. On a far cone use t=log r and a smooth angular coordinate theta in a compact subcone, with weighted measure r^(-2gamma)dX=exp((2-2gamma)t)dt dtheta. Define the model norm of h to be the standard H^s(dt dtheta) norm of v=exp((1-gamma)t)h, extending compact angular support by zero to R^2. For a nonzero smooth compactly supported v_0(t,theta), let v_n=v_0(t-T_n,theta) with T_n separated sufficiently. H^s norms are identical by translation. In physical coordinates these are h_n=R_n^(gamma-1)f(X/R_n), R_n=exp(T_n), for fixed f. Their weighted L2 supports are disjoint and their norms equal a positive constant. Thus no subsequence is Cauchy in the H^(s-1) model norm, which dominates L2.

Near the y-axis away from the origin choose a compact y-interval and t=-log x on x>0. The singular measure x^(-2a)dxdy=exp((2a-1)t)dt dy. Conjugate by v=exp((a-1/2)t)h and define the exact model H^s norm of v. For fixed smooth compact f(t,y), choose integer translations N_n with disjoint supports and put

 h_n(t,y)=exp(-(a-1/2)N_n) f(t-N_n,y).

Then v_n(t,y)=v_0(t-N_n,y), with v_0=exp((a-1/2)t)f. Again the high norm is constant and disjoint weighted L2 masses forbid a convergent lower-norm subsequence. Each h_n vanishes on some neighborhood of the axis, so imposing any finite number of zero axis jets does not remove the example. Reflection supplies the required parity with disjoint copies, changing only a fixed norm factor.

For an actual norm uniformly equivalent to these model norms in their ends, both counterexamples transfer immediately: uniform high-norm bounds and a fixed positive lower L2 separation persist. If all smooth residual weight factors and their necessary derivatives are uniformly bounded above and below after conjugation, such equivalence is a sufficient separately checkable premise. A proof of equivalence for the unspecified A_s is not supplied here. Thus a blanket compactness claim on these model ends is false, while an unconditional statement about every possible definition of the lead's X is not justified. Adding compact local terms or finitely many bounded scalar functionals cannot repair noncompactness of a lower norm which already includes the separated weighted L2 mass.

These results identify defects and conditional estimates of a proposed proof framework. They do not imply nonexistence of the X3 solution or any decisive endpoint in PROMPT.md.
