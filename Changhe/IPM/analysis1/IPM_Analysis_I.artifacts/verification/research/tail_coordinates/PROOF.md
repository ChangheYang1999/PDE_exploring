# Full tail coordinates, trace moments and the reduced matching column

Status: standalone argument written before its checking code. These results audit the elementary tail and block algebra in Design D_b'. They do not establish its analytic mapping, Fredholm property or inverse.

## Setting and exact tail jets

Let X=(x,y), r=|X|, E=x partial_x+y partial_y, c_l>1 and k=1/c_l in(0,1). In the upper half-plane put cos(theta)=x/r and sin(theta)=y/r. A smooth angular function with the density parity is even under x reflection and odd under y reflection. Near the positive y-axis suppose

Theta(theta)=theta_2 cos(theta)^2+theta_4 cos(theta)^4+O(cos(theta)^6).

The coefficients here are angular Taylor coefficients at this axis. They are not the Cartesian x jets. Expanding r=y(1+x^2/y^2)^(1/2) at fixed positive y gives

[x^2](r^k Theta)=theta_2 y^(k-2),
[x^4](r^k Theta)=[theta_4+(k-2)theta_2/2]y^(k-4).  (1)

Multiplication by log r=log y+x^2/(2y^2)+O(x^4/y^4) gives

[x^2](r^k log r Theta)=theta_2 y^(k-2)log y,
[x^4](r^k log r Theta)=[theta_4+(k-2)theta_2/2]y^(k-4)log y
                         +(theta_2/2)y^(k-4).  (2)

These identities hold where a radial tail cutoff equals1. Derivatives of the cutoff contribute only on its compact transition annulus.

For a concrete angular direction choose

Theta_1=sin(theta)cos(theta)^2[1+(3-k)cos(theta)^2/2].  (3)

It has the required parity. Since sin(theta)=(1-cos(theta)^2)^(1/2) near the positive y-axis, theta_2=1 and theta_4=(2-k)/2, which is nonzero. Its Cartesian fourth jet in(1) is zero. More explicitly, setting z=x/y and p=(k-3)/2 gives

r^k Theta_1=y^k z^2 (1+z^2)^p[1-p z^2/(1+z^2)]
           =y^k[z^2-((k-3)(k-5)/8)z^6+O(z^8)].  (4)

Thus a nonzero angular fourth coefficient does not ensure a nonzero Cartesian fourth jet. This refutes that proposed proxy. It does not determine the value of any full coupled adjoint functional.

## Why removing the jets does not remove the tail

Fix a>0, 1<gamma<1+k, a bounded scalar weight phi, and use the remainder weight

omega=|x|^(-2a)(1+r^2)^(a-gamma)exp(phi).

On the corner y>R, 0<z=x/y<z_0, the change of variables (x,y)=(zy,y) has Jacobian y. Boundedness of phi and comparison of1+r^2 with r^2 imply that the squared norm of a homogeneous remainder y^beta b(z) is comparable, with fixed positive constants, to

[integral_0^z0 z^(-2a)(1+z^2)^(a-gamma)|b(z)|^2 dz]
[integral_R^infinity y^(2beta+1-2gamma)dy].  (5)

If b is nonzero on a subinterval, the angular factor is strictly positive, or infinite. If b=O(z^6), it is finite for a<13/2. At a=6 the example(4), after subtracting its second and fourth Cartesian jets using a cutoff equal to1 for0<z<z_0, has a nonzero z^6 remainder. Its angular integral is finite, while its radial integral diverges because beta=k and gamma<1+k. The same conclusion applies to any nonzero such angular remainder. The exceptional case of an identically zero remainder is excluded explicitly.

Each nonzero pure tail jet itself also has divergent far jet norm: for a_{2j}=C y^(k-2j), its prescribed integral of y^(4j+1-2gamma)|a_{2j}|^2 equals C^2 integral y^(2k+1-2gamma). Hence external tail directions must be full spatial functions, including their jets and remainders, if that is the intended enlarged domain. This is a statement about the specified norms, not a proof that the enlarged operator is well defined.

For the homogeneous far transport, E=y partial_y at fixed z. Its weighted L2 rate can be computed without an angular estimate. For a smooth compactly supported test function in this corner, integration by parts in y gives

Re <(c_l E-1)h,h> =-[1-c_l(gamma-1)]||h||^2  (6)

in the exactly homogeneous measure z^(-2a)(1+z^2)^(a-gamma)y^(1-2gamma) dz dy. The gap is positive because gamma<1+k. Neither variable phi nor a nonlocal coupling is included in(6). No corner matching or surjectivity theorem for the full operator follows.

## Exact scalar extraction and its sufficient zeroth-order far bounds

Use the canonical inverse -Delta psi[h]=partial_x h and U[h]=(-psi_y,psi_x). Let ell[h]=psi[h]_{xy}(0), so the variation of c_l is ell[h]/3. Assume this linear functional and all velocities below exist in the canonical sense. Let rho be a sufficiently smooth background and define

V=c_l X+U[rho],
Lh=(V dot grad-1)h+U[h] dot grad rho+(ell[h]/3)E rho.

Choose a smooth radial cutoff chi_infinity equal to0 near0 and1 for r>=R. Put

e=chi_infinity r^k Theta_0,
q=chi_infinity r^k log r Theta_0,
t=chi_infinity r^k Theta_1,
w=(E rho-k e)/3,
d(h)=k ell[h]/3,
Ah=(V dot grad-1)h+U[h] dot grad rho+ell[h]w.

Then the algebraic identities

Lh=Ah+d(h)e,
m=c_l+k ell[q]/3, n=k ell[t]/3,
a=Lq-m e, b_tau=Lt-n e  (7)

are exact. In particular, ell[q] and ell[t] belong in the scalar row. For any h,kappa,tau for which the expressions make sense,

L(h+kappa q+tau t)
 =Ah+a kappa+b_tau tau+[d(h)+m kappa+n tau]e.  (8)

A sufficient hypothesis for zeroth-order far bounds is that, uniformly in angle, with enough angular smoothness for the displayed first derivatives,

rho-e=O(r^(2k-1)), E(rho-e)=O(r^(2k-1)),
U[rho]=O(r^k), grad rho=O(r^(k-1)),
U[q]=O(r^k log r), U[t]=O(r^k).

The smooth angular tails have grad q=O(r^(k-1)log r) and grad t=O(r^(k-1)). Outside the cutoff annulus,

(c_l E-1)q=c_l e, (c_l E-1)t=0.

Inserting these identities in(7) proves

w=O(r^(2k-1)), a=O(r^(2k-1)log r), b_tau=O(r^(2k-1)).  (9)

For a function bounded by C r^beta(log r)^m uniformly in angle, the far H_gamma norm with measure (1+r^2)^(-gamma)dX is finite if beta<gamma-1, by the convergent radial integral of r^(2beta+1-2gamma)(log r)^(2m). Thus (9) is sufficient for these zeroth-order far norms when2k-1<gamma-1. It does not prove the stronger projected conormal norm, its derivative bounds, or behavior at an interior corner. Those require separate estimates; a radial O bound alone is insufficient.

For an exact profile, one part of the preceding hypothesis follows from a uniform angular trace. Suppose (c_l E-1)rho=-G, |G|<=C r^(2k-1), and r^(-k)rho tends uniformly to Theta_0. Direct integration gives

rho-r^k Theta_0=k r^k integral_r^infinity s^(-k-1)G(s,theta)ds,
|rho-r^k Theta_0|<=k C r^(2k-1)/(1-k).  (10)

The radial differentiated remainder obeys the same upper constant, since E rho=k rho-kG. Differentiated angular bounds need the corresponding differentiated G and trace hypotheses. Equation(10) proves no velocity estimate or angular trace existence.

If Y embeds into H_gamma and Theta_0 is nonzero, e is outside Y. Whenever the remainders in(8) have been proved to lie in Y, the decomposition into Y plus the one-dimensional span of e is unique. The existence of these mappings is a hypothesis here. The natural domain for the unbounded first-order transport also needs a graph norm; a bounded X-to-X map is not inferred.

## Axis moment asymptotics and the strain functional

For a compact smooth h even in x, odd in y and zero on x=0, the partial Fourier transform in y gives, with nu=|eta|,

B_hat(eta)=nu integral_0^infinity exp(-nu x)h_hat(x,eta)dx,
B(y)=U_2[h](0,y), ell[h]=B'(0).  (11)

This follows from the Green kernel exp(-nu|x-z|)/(2nu) of -partial_x^2+nu^2 and the identity U2_hat=-h_hat+nu^2(-partial_x^2+nu^2)^(-1)h_hat. Evenness reduces the whole-line integral to(11). The value at nu=0 is its limit. This also reconstructs topic66's trace convention.

For a fixed bounded compact cutoff chi equal to1 on[0,delta], consider h=x^(2j)chi(x)a_{2j}(y), j=1,2. Formula(11) has multiplier

M_j(nu)=nu integral_0^infinity exp(-nu x)x^(2j)chi(x)dx.

Let C_chi=sup_{x>=delta}|chi(x)-1|. Repeated integration by parts of the exponential moment gives

|M_j(nu)-(2j)!nu^(-2j)|
 <=C_chi (2j)!nu^(-2j) exp(-nu delta)
       sum_{m=0}^{2j}(nu delta)^m/m!.  (12)

The estimate holds for nu>0. Its right side decays faster than any inverse power at high frequency. The leading multipliers are therefore2nu^(-2) and24nu^(-4). These are fixed-cutoff assertions; variable-width extensions need another analysis. For the second-jet extension, the leading terms cancel in u2=-a2-B''/2 and u3=a2'/3+B'''/6. The fourth-jet contribution similarly cancels the leading -a4 in u4=-a4+a2''/12+B''''/24. These cancellations follow by multiplying by i eta and eta^2, without estimating the summands separately.

There is also a flat weighted remainder bound. Cauchy-Schwarz in(11) yields for a>-1/2

|B_hat|^2 <=[Gamma(2a+1)/2^(2a+1)]nu^(1-2a)
             integral_0^infinity x^(-2a)|h_hat(x,eta)|^2 dx.  (13)

The factor is the exact integral nu^2 integral_0^infinity exp(-2nu x)x^(2a)dx. Multiplying by nu^(2(s+a-1/2)) and integrating over|eta|>=1 proves the indicated high-frequency gain a-1/2 from the corresponding weighted tangential Sobolev norm. Low frequencies and variable coefficients are not controlled by this assertion.

The strain kernel can be checked directly from G(Z)=-(1/(2pi))log|Z|, psi=partial_x G*h, evaluated at X=0. For compact h vanishing sufficiently at0, its integral is absolutely convergent and

ell[h]=integral_{x>0,y in R} [2y(3x^2-y^2)/(pi r^6)]h(x,y) dxdy.  (14)

Evenness in x accounts for the factor2. For the remainder weight omega_0=x^(-2a)(1+r^2)^(a-gamma) on the half-plane, a>2 and gamma<2, the kernel is in the dual L2 weight. Its exact squared norm is

C_ell^2=(2/pi^2) B(a-2,2-gamma) B(3/2,a+1/2)
             [3(3a^2+3a+2)/((a+2)(a+3))].  (15)

To verify(15), square the kernel, use polar coordinates theta in(-pi/2,pi/2), and substitute u=r^2 in the radial integral. It equals B(a-2,2-gamma)/2. The angular integral of cos(theta)^(2a) sin(theta)^2(3cos(theta)^2-sin(theta)^2)^2 is

9B(3/2,a+1/2)-24B(5/2,a+1/2)+16B(7/2,a+1/2).

The Beta recurrence reduces it to the second and third factors in(15). These integrals converge exactly under the stated radial conditions and a>-1/2 angularly. Cauchy-Schwarz proves |ell[h]|<=C_ell||h||_{L2(omega_0)} on the test core, hence a unique continuous extension of this moment functional to its completion. This does not construct a canonical velocity on that completion. A bounded phi changes the bound by exp(-inf(phi)/2).

## Eliminating the far scalar and testing transversality

Let X,Y be Banach spaces, A:X->Y and d:X->R bounded linear maps, a,b_tau in Y, and m,n real. Here X can be an established graph domain. Assume m!=0. For the block in(8), the equation with target(f,s) gives

kappa=[s-d(h)-n tau]/m,
Th+b tau=f-a s/m,
T=A-a d/m, b=b_tau-(n/m)a.  (16)

Now assume T is injective, its range is closed of codimension one, and ell_0 is a nonzero continuous functional whose kernel is range(T). These are substantive hypotheses. The operator(h,tau)->Th+b tau is a bijection if and only if ell_0(b)!=0. In that case applying ell_0 gives tau=ell_0(f-a s/m)/ell_0(b), and the remaining right side lies in range(T), where h is uniquely obtained. Since T is a bounded bijection X->range(T) between Banach spaces, its inverse is bounded by the bounded inverse theorem. The displayed formulas then give a bounded inverse for the full block. If ell_0(b)=0 the output is contained in the proper subspace ker ell_0, so surjectivity fails.

For the base block containing only h,kappa, its cokernel functional is

widehat ell_0(f,s)=ell_0(f)-ell_0(a)s/m.  (17)

Indeed (17) annihilates(Ah,d(h)) because ell_0(Th)=0, and annihilates(a,m) identically. Its evaluation on the tau column is precisely ell_0(b). If m=0, no division is permitted; the dual equations are instead A*ell_0+d*nu=0 and ell_0(a)+m nu=0, and the tau evaluation is ell_0(b_tau)+n nu. No actual cokernel, adjoint approximation or lower bound for this pairing is provided here.

A continuous nonzero linear functional on a real normed angular space is nonzero on an open dense set. Openness is continuity. Density follows by adding arbitrarily small multiples of one vector on which it is nonzero; at most one multiple can make a given affine value zero. Applying this statement to the tail pairing requires that the tail-to-column map and the cokernel have already been constructed and that their composition is nonzero.

For the exact scaling K=(E-1)rho, topic65 proves LK=0 whenever differentiation of the canonical scaling is justified. If the stronger membership K-(k-1)t in X is separately established for t with Theta_1=Theta_0, the enlarged unnormalized domain contains the vector (K-(k-1)t,0,k-1) in its kernel. Zeroth-order decay O(r^(2k-1)) alone does not establish that membership in the proposed conormal graph domain. Under local C3 normalization, K has cubic coefficient2; imposing the normalized cubic condition excludes this particular vector. This yields no dimension count.

## Conditional two-block closure with onto hypotheses retained

Suppose J0:X_J->Y_J and R0:X_R->Y_R are bounded bijections between Banach spaces with inverse bounds C_J,C_R. Suppose the actual diagonal blocks J=J0+E_J and R=R0+E_R have bounded errors epsilon_J,epsilon_R, and bounded off-diagonal blocks C:X_R->Y_J and D:X_J->Y_R have norms at most C_JR,C_RJ. If

mu_J=1-C_J epsilon_J>0, mu_R=1-C_R epsilon_R>0,
Gamma_J=C_J/mu_J, Gamma_R=C_R/mu_R,
theta=Gamma_J Gamma_R C_JR C_RJ<1,

then Neumann series first invert J and R with bounds Gamma_J,Gamma_R. Eliminating r from Jj+Cr=f_J, Dj+Rr=f_R gives (I-J^(-1)C R^(-1)D)j=J^(-1)f_J-J^(-1)C R^(-1)f_R. Its operator norm perturbation is at most theta<1, so it is onto and invertible. The corresponding elimination for r gives

||H^(-1)|| <= max{Gamma_J(1+C_JR Gamma_R),
                  Gamma_R(1+C_RJ Gamma_J)}/(1-theta)=C_H  (18)

in maximum product norms. This proof uses actual reference isomorphisms; inequalities on solutions alone do not supply them.

For an additional bounded finite-dimensional border [H B; C_b D_f], let S=D_f-C_b H^(-1)B. If S is invertible with bound C_S, solving the two equations gives the valid maximum-product bound

||[H B; C_b D_f]^(-1)||
 <= C_H+(1+C_H||B||)C_S(1+||C_b||C_H).  (19)

For completeness, the scalar block solution obeys ||z||<=C_S(1+||C_b||C_H)||(f,g)||, and the vector part obeys ||x||<=C_H||f||+C_H||B||||z||. Their maximum is no larger than the sum used in(19). No block or error constant for the actual profile is certified here.

## Explicit numerical illustrations specified before code

The multiplier test uses a fixed C7 cutoff, not an unspecified smooth cutoff. Let chi(x)=1 for0<=x<=1/2, chi(x)=sum_{m=0}^7 binom(15,m)t^m(1-t)^(15-m) for t=2x-1 in[0,1], and chi(x)=0 for x>=1, with even extension. The middle polynomial has derivative -[15!/(7!7!)]t^7(1-t)^7; it lies between0 and1 and matches the endpoint constants to order7. Formula(12) therefore applies with delta=1/2 and C_chi=1.

One integration method expands this polynomial in powers of x and uses the exact exponential antiderivative on the two intervals. A second method expands the exponential positively after changing variables to the unit interval. For N=2j, its two terms are

M_left=nu 2^(-N-1) exp(-nu/2) sum_{q>=0}(nu/2)^q B(N+1,q+1)/q!,
M_right=nu 2^(-N-1) exp(-nu) sum_{q>=0}(nu/2)^q/q!
          times sum_{l=0}^N sum_{m=0}^7 binom(N,l)binom(15,m)B(l+m+1,16-m+q).  (20)

All summands are nonnegative. The Beta ratio when q increases is less than1, so the successive total q-term ratio is at most nu/[2(q+1)]. The tail after Q is at most the next term divided by1-nu/[2(Q+2)], when this denominator is positive. An independent high-precision check uses the layer representation chi(x)=integral_x^infinity p(z)dz, where p=-chi' is supported on[1/2,1], p>=0 and integral p=1. Interchanging positive integrals gives

M_j=(2j)!nu^(-2j)[1-integral_{1/2}^1 p(z)exp(-nu z)
                                     sum_{m=0}^{2j}(nu z)^m/m! dz].  (21)

After z=(1+t)/2, p(z)dz=[15!/(7!7!)]t^7(1-t)^7dt. This supplies a third finite exponential-moment formula. These tests check multiplier values at nu=4,16,64 for j=1,2 and their error bounds, not global extension estimates.

For(15) at a=6, the radial Beta factor is B(4,b)=6/[b(b+1)(b+2)(b+3)], b=2-gamma. The angular Beta factor equals pi times (12)!/[2*4^6*6!*7!]. Thus C_ell^2 is an exact positive rational multiple of1/pi. This identity allows an independent evaluation using exact factorials and an alternating Machin enclosure of pi, rather than repeating a Gamma-library call.

For the finite block illustration of(16), use X=R,Y=R^2, A=(2,3), d=5, a=(1,-2), m=4, b_tau=(-1,7), n=6. Then T=(3/4,11/2), b=(-5/2,10), and ell_0=(22,-3) gives ell_0(T)=0, ell_0(b)=-85. The full3by3matrix with columns(A,d),(a,m),(b_tau,n) has determinant -85, so this is an invertible illustrative block.

For(18), choose J0=1/2,R0=1/3,E_J=-1/20,E_R=-1/30,C=1/5,D=1/10. Then mu_J=mu_R=9/10, theta=4/27 and C_H=110/23. The actual matrix H=[9/20,1/5;1/10,3/10] has inverse maximum row-sum norm exactly110/23, so the stated bound is attained in this scalar two-block example. An optional border B=(1/7,-1/11), C_b=(1/13,1/17), D_f=2 tests(19) by exact inversion. None of these matrices represents a discretized IPM operator.

## Dependencies and planned verification

The canonical convention and scaling identity agree with the standalone proofs in ../y_axis_matching/PROOF.md and ../far_domain/PROOF.md; the relevant trace and kernel formulas have been rederived here. Elementary integration, Cauchy-Schwarz, Banach inverse and Neumann-series arguments are supplied above. No compactness theorem is invoked.

Independent symbolic expansion will check the tail coefficients, scalar extraction, multiplier cancellations, Beta simplification and finite block algebra. Exact rational parameters k=1615536043799051/9007199254740992, gamma=1129/1000 and a=6 will illustrate the strict inequalities and(15). Arb balls and independently evaluated interval formulas will enclose the constants and fixed-cutoff error bound; a higher-precision audit will check the output intervals. These computations will not replace the hypotheses of(16)-(19) by trial measurements. Full conormal mapping, actual coupled matching and every decisive PDE endpoint remain open.
