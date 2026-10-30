# Independent audit of the two sharpened L2 closure frameworks

## Exact statement and hypotheses

This note audits the frozen T2-R3 proposal in `source/T2_T4L2_sharp.md`. All functions are real on R² and S1, meaning even in x and odd in y. Use the Fourier transform fhat(xi)=integral f(x)exp(-ix.xi)dx, R_j with symbol i xi_j/|xi|, U=(-R1R2,R1²), J=(1-Delta)^(1/2) and omega=(1+4|x|²)^(2/5).

For fixed w1>=2,w2>=1 put

E_w(f)²=P²+w1 a²+w2 b²,
P=||omega D²f||_2, a=||Df||_2, b=||f||_2,
X_(s,w)(f)=E_w(J^s f), 0<s<=1/1024.

The spaces are completions of compact smooth S1 functions. Derivative tensors have all ordered Cartesian components and Euclidean norms. Different finite positive component weights give equivalent spaces. The changing weights do not change the tail membership condition.

Let rho be a smooth S1 reference, u=U[rho] its canonical velocity, V=cx+u, a0=rho_y(0)>0, and L=V.D-1+U[.].D rho. Require all of the following.

(A) 9/5<c<37/20, c+partial_y u2(0)=1. The fields D rho, <r>D²rho, <r>²D³rho, <r>²D⁴rho, Du, <r>D²u, <r>D³u are bounded. The canonical velocity is smooth, divergence free and sublinear; for some gamma<1, |D^j rho|=O(r^(gamma-j)), j=0,1,2.

(B) With theta=ess sup (|D rho|-rho_y)/2 and

kappa²=[(log2-1/2)||D rho_x||_2²+(3log2-2)||D rho_y||_2²]/(16pi),

one has c+1-theta-kappa>=2.

(C) Set A=[[rho_y,-rho_x/2],[-rho_x/2,0]], v=omega²,
M1=I-sym Du+A,
M2=(1+c+V.Dlogomega)I-2sym DV+A,
S=(v_xy rho_x-v_xx rho_y-v_x rho_xy+v_y rho_xx)/2.
Require M1>=(9/10)I, M2>=(1/2)I and the six suprema

(||D²rho||,||omega D²rho||,||omega D³rho||,||omega D²u||,||D(v D rho)/omega||,||S||)
<=(3,8,10,3,28,40).

(D) The separate component-supremum sums for

(|c|,Du,omega D²u,omega D³u,D rho,omega D²rho,omega D³rho,omega D⁴rho)

are at most (2,6,24,160,22,32,80,2048), respectively.

Under these hypotheses the proposed linear rate is valid, and each of the following parameter sets gives a conditional nonlinear existence and uniqueness theorem:

| name | w1 | w2 | s | r | eta | certified rate |
| --- | --- | --- | --- | --- | --- | --- |
| sharp | 16384 | 262144 | 1/7744 | 147/200000 | 76219/1000000000 | at least1037/10000 |
| sharpw | 32768 | 1048576 | 1/5184 | 1351/1000000 | 4207/20000000 | at least1557/10000 |

More precisely, if the actual residual F=V.D rho-rho belongs to X_(s,w) and X_(s,w)(F)<=eta, there is exactly one h in the ball X_(s,w)(h)<=r, c[h]=partial_y U2[h](0)=0, satisfying the stationary equation F(rho+h;c)=0. Its origin slope is positive and its fixed leading r^(1/c) profile agrees with rho. This is conditional on every stated hypothesis. No existing candidate is certified by this note.

## 1. Base rate and component scaling

The independently audited derivative identities in T4-019 give

-Re<D²Lh,omega²D²h> >= P²/2-(347/5)Pa-10Pb-40a²,
-Re<DLh,Dh> >= (9/10)a²-6ab,
-Re<Lh,h> >=2b².

The last line remains valid with any divergence-free rough transport U[k].D. Adding the three lines with weights1,w1,w2, and subtracting mu E_w(h)², gives a lower bound by the quadratic form of

G_w(mu)=[[1/2-mu,-347/10,-5],
 [-347/10,w1(9/10-mu)-40,-3w1],
 [-5,-3w1,w2(2-mu)]].

Thus G_w(mu)>=0 is sufficient. The equality sign in step1 of the frozen T2 draft should be >=: the displayed quadratic form already uses lower estimates for the exact energy. It is not a necessary condition for the actual operator to have that rate.

Our exact LDU elimination verifies positive pivots at mu=259/1000 for sharp and97/250 for sharpw; the next grid values13/50 and389/1000 have negative determinant. This verifies the proposed sufficient rates, not an optimal rate of the differential operator.

For the smooth commutator use the already audited T2-R2 constants

m=(sqrt(pi)/2)Gamma(1023/2048), z=(8sqrt5/5)6^(-3/5),
k_u=m, k_w=m+8/5, t_u=3m/2, t_w=3m/2+32/15,
b=1+3pi z/4, d=1+pi z/2.

The unscaled output bounds depend only on P,a,b; no Hdot^-1 input occurs. In the scaled vector (P,sqrt(w1)a,sqrt(w2)b), the six nonzero entries are

K00=2d+6b+24(t_w+2k_w)+32k_w,
K01=320k_w/sqrt(w1), K02=2048k_w/sqrt(w2),
K11=8+24(t_u+k_u)+32k_u,
K12=80k_u sqrt(w1/w2), K22=8+24t_u+32k_u.

This scaling follows by dividing each input coefficient by its input weight and multiplying by its output weight. In particular K12 increases with sqrt(w1) and decreases with sqrt(w2). The symmetric row sums give a valid energy upper bound. Our separate rational certificate proves that all sums are below401 and397, respectively. No floating eigenvalue is used.

## 2. Rough transport and realization

Since omega>=1 and w1>=2,w2>=1,

||f||_(H^(2+s))² <= X_(s,w)(f)².

Let n=X_(s,w)(k), W=U[k], f=J^s g, E=E_w(f), x=P(f)/E. The vector Fourier multiplier of U has modulus |xi1|/|xi|<=1. Thus ||W||_(H^(2+s))<=n, ||DW||_infinity<=c_s n, c_s=1/[2sqrt(pi s(1+s))]. The weighted odd Riesz estimate also gives ||omega J^s D²W||<=9n/5. Moreover ||Dg||_(H^(1+s))²<=a(f)²+P(f)²<=E².

At s0=1/1024 define q=1/(2sqrt(pi)), p=2^s0 sqrt(1+s0)/(2sqrt(pi)), L=z m s0,
P_w=p(1+L)+qL,
A=(4/5)q+q(1+4L)+2P_w,
B=(9/5)P_w.

The differentiated rough transport identity and the independently audited T2-R2 product estimates give top energy cost (n/sqrt(s))[A P(f)²+B E P(f)]. The first-derivative energy costs at most(q+p)(n/sqrt(s))w1 a(f)², and the L2 energy at most q(n/sqrt(s))w2 b(f)². These are multiples of the corresponding squares regardless of the weights. The additional p/2 cost in the old L2 line was half of the cross-term from the H energy. Since there is no H energy here, that cost disappears.

As A>=q+p, the full normalized cost is bounded by A x²+B x+(q+p)(1-x²)<=A+B<8/5. The last strict bound follows from the rational certificate; the frozen draft's more accurate1.5871175 is not needed.

Consequently for A_k=L+U[k].D the high rate is

mu-C'(w)s-(8/5)X_(s,w)(k)/sqrt(s).

The maximal-domain and consistency proof of T4-019 applies with these equivalent Hilbert norms. For clarity, smooth k_m converges to k in X_(s,w), hence W_m converges in W^(1,infinity). The high energy estimates are uniform on finite time intervals. The L2 Duhamel difference is bounded using ||D S_m(t)f||_2<=X_(s,w)(S_m(t)f)/sqrt(w1). Thus the smooth semigroups converge in C_t L2 on high inputs; low-input convergence follows by L2 density and the uniform exp(-2t) estimate. Weak high compactness and the energy estimate give a strongly continuous high restriction. If h and A_kh are in X_(s,w) distributionally, the low Duhamel identity is a high-space integral and identifies the full maximal domain. A positive high rate gives its inverse by the convergent negative time integral. On L2 the inverse bound remains1/2 independently of k.

The weight changes introduce no extra differentiation, normalization condition or derivative loss in this construction.

## 3. Nonlinear ball, trace and uniqueness

For each parameter row let beta=mu-C's-(8/5)r/sqrt(s). The exact certificate verifies beta is at least the displayed positive lower rate and eta<=r times that lower rate. Therefore T(k)=-A_k^-1 F maps the high ball into itself.

Every high input is C^(1,alpha) for0<alpha<s. The audited contact formula is

c[h]=-h_y(0)/4+(1/pi)PV integral sin(3theta)h(x)|x|^-3 dx.

The contact term is retained. At normalized k, the origin identity (A_kh)_y(0)=a0 c[h] and F_y(0)=0 show c[T(k)]=0. The normalized high ball is complete in the L2 metric: an L2-Cauchy sequence has a weakly convergent high subsequence, whose limit is its L2 limit; the norm bound and the continuous linear trace pass to that limit.

The difference equation is A_k(T(k)-T(l))=U[l-k].D T(l). The L2 inverse and the gradient embedding give contraction factor at most c_s r/2. Our rational certificate gives factors below0.009123 and0.01372. Thus the contraction theorem applies. Any stationary h in the ball is in the maximal domain because A_hh=-F, so inverse uniqueness makes it a fixed point. This proves uniqueness within the stated ball.

At the origin M1>=.9I and c+u2_y(0)=1 imply a0>=c-1.1>.7. The certificate verifies c_s r<.028, so a0+h_y(0)>0. The correction and its first derivative vanish at infinity by Fourier integrability. A nonzero scaling mode changing the prescribed leading r^gamma profile is not in this high space.

## 4. Raw-norm conversion

Let E=E_w(F)<infinity and Q3=||omega D³F||_2<infinity. Set Z=(omega D²F,sqrt(w1)DF,sqrt(w2)F). Since |Dlogomega|<=4/5, the product rule gives

||Z||_(H1)² <=2Q3²+(1+32/25+w1)P²+(w1+w2)a²+w2 b²
 <=2Q3²+C_w E²,
C_w=max(1+32/25+w1,1+w2/w1).

Interpolation of this Hilbert-valued Fourier norm gives ||J^s Z||_2<=E^(1-s)(2Q3²+C_w E²)^(s/2). Commuting only the top weight costs at most s z m ||D²F||_2<=1.92s E. Thus

X_(s,w)(F)<=E^(1-s)(2Q3²+C_w E²)^(s/2)+1.92s E.

Here C_w=16386.28 and32770.28 exactly for the two rows. The reverse top estimate is P(J^s F)>=(1-1.92s)P(F), obtained from ||J^s(omega D²F)||>=P(F) and the same commutator. The unweighted lower components satisfy a(J^s F)>=a(F), b(J^s F)>=b(F).

Component bounds should be stated as the exact quantities eta, eta/sqrt(w1), eta/sqrt(w2), not decimals rounded downward. They are individually necessary, while their weighted square sum is required for closure. The two different values of s prevent reading a same-s norm comparison as inclusion of the actual two balls.

## 5. Weak necessary test

Independently of the sufficient inverse conditions, let h in H^(2+s) solve F(rho+h;c)=0 distributionally, with ||h||_2<=m and ||Dh||_infinity<=D. For every real compact smooth phi,

|<F,phi>| <= m[||V.Dphi+(2c+1)phi||_2+||phi D rho||_2+D||phi||_2].

Indeed integration by parts in V.Dh-h uses div V=2c. The remaining terms are bounded by Cauchy-Schwarz, ||U[h]||_2<=||h||_2 and the gradient bound. The actual vector symbol is (xi1 xi2,-xi1²)/|xi|²; the frozen draft prints its negative, which has the same modulus and does not affect this estimate. No point evaluation, trace restriction or negative norm is used. For the two high balls, take m=r/sqrt(w2) and D=c_s r. The theorem is valid, but its numerical use requires certified integrals or other rigorous test-function bounds.

## 6. Finite-family and point arithmetic

The audited finite-family L2 theorem T4-025, with precisely four stationary branches and indices0<=m<=k<=K, gives the full-residual floor in `verification/FAMILY_SCOPE.md`. Since X_(s,w)(F)>=sqrt(w2)||F||_2 directly, its new cutoffs are K<=6886 for sharp and K<=5814 for sharpw. The following K is inconclusive. The exact family, distance product and arithmetic method are stated in that file; no guessed asymptotic onset is used. These new cutoff numbers await independent cross-lane arithmetic reproduction.

Using the already independently confirmed Cartesian point fields and the audited S1 point inequality, the old point test at (0,1) remains inconclusive for d2 in both new balls. It excludes Mpen2 at (0,2) and b6 at (0,1). Independent Arb512 arithmetic agrees with T2's signs and values. This limited test does not establish that d2 is within either ball.

## Scope

This independent audit confirms the two conditional frameworks, the raw-norm comparison and the weak necessary inequality. It does not verify the floating weight optimization, a universal upper limit for every weight choice, or any numerical weak-test evaluation. The statement that all these inequalities can never accept G0 above3e-7 is not proved by a finite floating scan. The absolute operator base rate is also not determined by failure of the sufficient Gram matrix at the next grid point.

Dependencies are the exact A2 derivative identities, the audited T2-R2 kernel/product estimates with their independent derivation in `../sharp_kernel_audit/PROOF.md`, the contact and maximal-domain proof of `../l2_closure/PROOF.md` and its addendum, and the elementary Fourier interpolation above. All numerical checks are separate in `verification/`; no proof assistant or server is run.
