# Frozen full-nonlocal source inverse on the Hölder scale

Topic74, written before its checking code, 2026-10-20. This is an independent proof audit of lead V21. The statements below concern a specified constant-coefficient dilation operator on the full plane. They are not a variable-coefficient IPM inverse theorem or a profile exclusion. Status remains OPEN until the recorded reviews and checks are complete.

## 1. Exact statement and realization

Use coordinates z=(s,y) centered at a source. Let A>1, a=g/(A-1), and assume 1<a<A+1. Define

 T=A s partial_s+y partial_y,
 M=partial_s^2 Delta^{-1}, with Fourier symbol xi^2/(xi^2+eta^2),
 L=T-1-gM,
 b=(A-1)/A, p=A/(A-1), q=(1+g)/A=a-(a-1)/A,
 r(sigma)=b sigma+1/A.

The Fourier convention is fhat(zeta)=integral exp(-i z.zeta)f(z)dz, inverse factor(2pi)^-2. M is the bounded L2 multiplier with any value at frequency zero. T is the closed generator of D_t f(z)=f(exp(tB)z), B=diag(A,1), on L2. L is the bounded perturbation T-1-gM, with domain D(T). Thus the domain and inverse selection are part of the statement.

Let C_*^sigma=B^sigma_{infinity,infinity} be the inhomogeneous isotropic Besov space, using a fixed smooth annular dyadic decomposition and a low block. For noninteger positive sigma it equals the usual bounded Hölder space with equivalent norms. Local norms mean restriction norms on an open ball. Fix any compact K in the plane. The following statements hold with finite constants depending on A,a,K, the decomposition and the indicated exponents:

(i) R=L^-1 on L2 exists, ||R||<=2/(A+3).

(ii) For supp f subset K and 1<sigma<a,

 ||Rf||_{C_*^{r(sigma)}}<=C||f||_{C_*^sigma}.             (1)

The exact output exponent is attained. No larger exponent admits a uniform estimate of this form, even for smooth inputs supported in any fixed small source neighborhood, even in s and odd in y.

(iii) If 1<sigma<q, there are such smooth packets with uniformly bounded input C_*^sigma norm and

 ||Rf_N||_{C_*^sigma(B_r)} comparable to N^{(sigma-1)/(A-1)}. (2)

Both constants in comparability are independent of N=2^n; r>0 is fixed.

(iv) For 0<sigma<1, the same compact-input inverse is bounded into C_*^sigma. At sigma=1 its dyadic upper bound loses one logarithm; this logarithm is necessary for C_*^1 inputs. A separate single-packet sequence has bounded classical C1 input norm and

 partial_y Rf_N(0)=-phi(0)psi(0) log N/(A-1)+O(1).       (3)

(v) For sigma>a, the output is bounded in C_*^q. No exponent greater than q works uniformly, and there is one fixed smooth compactly supported parity-compatible forcing whose selected solution fails to belong locally to any C_*^beta with beta>q. At sigma=a, we prove only a logarithmically weakened q upper bound; necessity of this endpoint logarithm in the odd class is OPEN.

Constants denoted C below are finite existence constants derived from fixed Schwartz kernels and geometric integrals. None is a numerical a posteriori inverse constant. This result cannot close the nonlinear PDE error theorem.

## 2. Semigroup and inverse

Direct Fourier transport gives the combined operator

 S_t=e^{(a-1)t} Lambda^{-a}D_t Lambda^a=e^{-t}D_t Q_t,
 Q_t(xi,eta)=[(xi^2+eta^2)/(e^{2(A-1)t}xi^2+eta^2)]^{a/2},             (4)

or equivalently

 (S_t f)^hat(zeta)=e^{(a-A-2)t}|zeta|^{-a}
       |e^{-tB}zeta|^a fhat(e^{-tB}zeta).                           (5)

No separate low-frequency definition of Lambda^{-a} is needed. The product in(5), or Q_t in(4), defines S_t on L2. Its symbols satisfy the cocycle relation, so S_{t+u}=S_tS_u. It is strongly continuous at0 by dominated convergence and strong continuity of D_t. Since 0<=Q_t<=1,

 ||S_t||_{2->2}<=e^{-t}e^{-(A+1)t/2}=e^{-(A+3)t/2}.                (6)

Differentiating(4) at0 gives T-1-a(A-1)M=L on functions with smooth Fourier transform compactly supported away from0. This set is a core for T: truncate frequency first near0 and infinity with smooth cutoffs whose logarithmic radial derivative is uniformly bounded, then approximate smoothly on the resulting annuli. The cutoff commutators with the first-order Fourier transport vanish in L2 by absolute continuity of its integral; ordinary local smooth approximation converges in its first-order graph norm. Bounded perturbation preserves this core and determines L uniquely. Hence S_t is its semigroup.

The Bochner integral R=-integral_0^infinity S_t dt converges on L2 by(6). For finite H, L integral_0^H S_t f dt=S_Hf-f, first on the core and then by the closed-generator identity. Letting H tend to infinity and using closedness gives LRf=f. The analogous identity for f in D(L) gives RLf=f. Integration of(6) gives the norm in(i). Parity in s and y is preserved.

## 3. Dyadic estimate with compact-support gain

Write Delta_N for a homogeneous smooth annular block, N dyadic. The high-frequency inhomogeneous blocks have N>=1. For such N and compactly supported f,

 ||Delta_N f||_infinity+||Delta_N f||_{L_s^1 L_y^infinity}
       <=C_K N^{-sigma}||f||_{C_*^sigma}.                         (7)

On a fixed enlargement of the s-projection of K, the second norm follows from the first times the strip width. Outside this strip, convolving the compact input with the Schwartz kernel gives a bound C_M N^{-M}(1+dist(s,K))^{-M}||f||_infinity, integrable in s. Choose M>sigma+2. Applying Lambda^a to an annular function costs at most C N^a in both norms, because its localized multiplier has an L1 convolution kernel with that scaling.

For lambda>=1 the kernel K_lambda of Delta_lambda Lambda^{-a} satisfies

 ||K_lambda||_1<=C lambda^{-a},
 integral sup_s |K_lambda(s,y)|dy<=C lambda^{1-a}.                (8)

These follow by dilation from a fixed Schwartz kernel. D_t preserves the supremum norm and multiplies the mixed norm in(7) by e^{-At}. Convolution, using either line of(8), gives

 ||Delta_lambda S_t Delta_N f||_infinity
 <=C e^{(a-1)t}(N/lambda)^a N^{-sigma}
               min(1,lambda e^{-At})||f||_{C_*^sigma}.            (9)

Frequency support forces N e^t lesssim lambda lesssim N e^{At}. Fixed overlap constants merely shift the time endpoints by bounded constants and alter C. With idealized endpoints l=log(lambda/N)/A and u=log(lambda/N), integrate over [l,u] intersect[0,infinity). Split also at t*=log(lambda)/A. The exponents before and after the split are a-1>0 and a-A-1<0. Each full exponential integral is bounded by its extreme endpoint divided by the respective positive gap. Using just the first branch gives a bound C N/lambda; using both branches at t* gives C N^a/lambda^q. Consequently

 ||Delta_lambda R Delta_N f||_infinity
 <=C N^{-sigma}min(N/lambda,N^a/lambda^q)||f||_{C_*^sigma}.         (10)

The crossover is N=lambda^b, since (a-1)b=q-1. Inputs N above a fixed multiple of lambda have no overlap. The fixed constants around N~lambda and around the crossover do not affect dyadic exponents or summability.

For low inputs use homogeneous N<=1 and |fhat|<=||f||_1. The input annulus intersected with the output condition |e^{tB}zeta|~lambda has area at most C N lambda e^{-At}: its xi width is bounded by C lambda e^{-At} and its eta width by C N. Fourier inversion in(4), with multiplier size at most C e^{(a-1)t}(N/lambda)^a, gives

 ||Delta_lambda S_t Delta_N f||_infinity
 <=C||f||_1 lambda^{1-a}N^{a+1}e^{(a-A-1)t}.

Integrating from t at least A^{-1}log(lambda/N) minus a fixed constant yields

 ||Delta_lambda R Delta_N f||_infinity
 <=C||f||_1 lambda^{-q}N^{q+2}.                             (11)

Here q>1, so the low input series converges. Homogeneous decomposition of the low block is legitimate in L2; the estimates then give absolute uniform convergence after the output projection. The low output block is bounded by the L2 inverse and its L2 convolution kernel, with ||f||_2<=C_K||f||_infinity.

For lambda>=2, (10)-(11) reduce the proof to

 ||Delta_lambda Rf||_infinity<=C||f||_{C_*^sigma}[
 lambda^{-q}+lambda^{-q} sum_{1<=N<=lambda^b}N^{a-sigma}
              +lambda^{-1} sum_{lambda^b<=N lesssim lambda}N^{1-sigma}]. (12)

All sums are over dyadic N. For 1<sigma<a the two sums are bounded respectively by constants times lambda^{b(a-sigma)} and lambda^{b(1-sigma)}, and both terms equal the order lambda^{-r(sigma)}. This proves(1), including its endpoint output exponent. For 0<sigma<1 the final sum instead gives lambda^{1-sigma}, and the result is lambda^{-sigma}. For sigma=1 it gives lambda^{-1}(1+log lambda). For sigma=a the first sum gives lambda^{-q}(1+log lambda). For sigma>a both sums are bounded by C lambda^{-q}. This proves all claimed upper bounds.

## 4. Packet lower bound and exact transformed integral

Choose real even phi,psi in C_c^infinity on arbitrarily small intervals, with psi(0)>0 and phihat(kappa0) nonzero at some kappa0>0. Put

 f_N(s,y)=N^{-sigma}phi(s)psi(y)sin(Ny),
 t_N=log N/(A-1), lambda_N=N^p,
 H_N(Z)=N^{sigma+1/(A-1)}Rf_N(Z/lambda_N).                       (13)

Modulation and fixed smooth multiplication give ||f_N||_{C_*^tau}<=C_tau N^{tau-sigma} for tau>0. Their L2 norms are at most C N^{-sigma}.

We prove the Fourier limit on compact sets where kappa>0 and nu>0, keeping kappa bounded away from0. Substitute t=t_N+tau into(5), then v=e^{-tau}nu. A direct cancellation of every N power gives

 Hhat_N(kappa,nu)= (i N/2)|(kappa,nu)|^{-a} nu^{a-A-2}
 integral_0^{nu N^{1/(A-1)}} v^{A+1}
 [1+kappa^2 v^{2A-2}/(N^2 nu^{2A})]^{a/2}
 phihat(kappa(v/nu)^A)
 [psihat(N(v-1))-psihat(N(v+1))]dv.                              (14)

This formula makes the delta limit precise. Its multiplier of the square bracket in the last line has a uniform integrable polynomial-decay majorant at infinity, since kappa stays positive and phihat is Schwartz. At0 it is bounded by C v^{A+1}, which is integrable. Near v=1 it converges uniformly to phihat(kappa/nu^A), times the displayed powers. The approximate identity N psihat(N(v-1)) has integral tending to integral psihat=2pi psi(0). Its absolute L1 norm is uniformly bounded, and its mass outside any fixed neighborhood of1 tends to0 faster than any inverse power. The negative carrier has no positive root, so its integral tends to0 by the same decay bounds. The upper endpoint tends uniformly to infinity. Thus locally uniformly on these frequency compacts,

 Hhat_N -> i pi psi(0)|(kappa,nu)|^{-a}nu^{a-A-2}
                         phihat(kappa/nu^A).                    (15)

In particular the limit is nonzero near(kappa0,1). Choose a Schwartz test W with compact Fourier support there, with phase arranged so its pairing with the limit is nonzero. Real and imaginary parts can be used if desired. Every polynomial moment of W vanishes. Then

 |<Rf_N,lambda_N^2 W(lambda_N .)>|>=c N^{-sigma-1/(A-1)}.         (16)

For any beta>0 and fixed ball B_r, frequency localization and the Besov norm give

 |<h,lambda^2 W(lambda .)>|<=C lambda^{-beta}||h||_{C_*^beta(B_r)}
                                      +C_M lambda^{-M}||h||_2.   (17)

To see the local assertion, choose an extension realizing the restriction norm up to a factor2, multiply it by a fixed smooth cutoff supported in B_r and equal to1 near0, and use the usual whole-space dyadic pairing for that cutoff function. The difference from h is supported away from0, where the rescaled Schwartz test has L2 norm smaller than any prescribed inverse power. The cutoff extension is L2-controlled by the local norm; this extra term is absorbed in the first term by taking a sufficiently large power. No support or smoothness of Rf_N is assumed in this argument.

Using(6) to control the last term of(17), we obtain

 ||Rf_N||_{C_*^beta(B_r)}>=c N^{p beta-sigma-1/(A-1)}.            (18)

The exponent is positive exactly when beta>r(sigma). For beta=sigma>1 it equals(sigma-1)/(A-1). If sigma<q, apply(1) at input order tau=(A sigma-1)/(A-1), which lies in(1,a), and use the packet norm at that order. This gives the matching upper bound in(2). Claims for classical noninteger Hölder spaces follow by norm equivalence. No assertion about classical integer C^m is needed for(2).

These packets are even in s and odd in y. If parity about a distinct original x-origin is wanted, replace phi(s) by phi(s)+phi(s+2x_*). Its Fourier transform is phihat(xi)(1+e^{2i x_*xi}), nonzero on a suitable smaller test set. The same frozen-operator proof works. This does not make the frozen operator a global reflection-invariant variable-coefficient operator.

## 5. Both logarithmic endpoints at input order1

For classical C1 take the single packet in(13) with sigma=1 and phi(0)psi(0)>0. These inputs have uniformly bounded classical C1 norms. Since partial_y(e^{-t}D_t F)(0)=partial_y F(0), Fourier inversion and the two symmetric carriers give

 D_N(t):=partial_y S_t f_N(0)
 =(2pi)^-2 integral phihat(xi)psihat(zeta)(1+zeta/N)
 [((xi/N)^2+(1+zeta/N)^2)/(z^2 xi^2+(1+zeta/N)^2)]^{a/2} dxi dzeta,
 z=e^{(A-1)t}/N.                                              (19)

For N^{-1}<=z<=1 let

 H(z)=psi(0)/(2pi) integral phihat(xi)(1+z^2 xi^2)^(-a/2)dxi.

Schwartz decay and |(1+w)^(-a/2)-1|<=C_a w for w>=0 give H(z)=phi(0)psi(0)+O(z^2). Uniformly for z in this range, D_N(t)=H(z)+O(N^{-1}). For completeness split |zeta|<=N/2, where v=1+zeta/N>=1/2. Taylor expansion in v around1 and in xi/N around0 is bounded by C_a (|zeta|/N+N^{-2})(1+|xi|)^{a+4}, independently of z<=1. Integrating this against the Schwartz factors is O(N^{-1}). On the complement Q_t<=1 and the rapid decay of psihat give the same estimate with any inverse power; the corresponding H tail is controlled likewise. Therefore

 integral_0^{t_N}D_N(t)dt=phi(0)psi(0)t_N+O(1),                  (20)

because integral_0^{t_N}z^2dt<=1/[2(A-1)] and t_N/N is bounded.

For z>=1, put v=1+zeta/N and use

 [(xi/N)^2+v^2]/[z^2 xi^2+v^2]
       <=(Nz)^(-2)+v^2/[z^2 xi^2+v^2].

Raising to a/2 costs only a fixed factor. Integrating the second term in xi, using bounded phihat and w=z xi/|v|, gives at most

 C |v|/z integral_R(1+w^2)^(-a/2)dw.

This integral is finite because a>1; an explicit elementary upper bound is 2+2/(a-1). The first term is bounded using ||phihat||_1. Including |v psihat(zeta)| and integrating gives

 |D_N(t)|<=C[(Nz)^(-a)+z^{-1}], z>=1.                           (21)

The same absolute Fourier estimate bounds the spatial supremum of partial_y S_t f_N. It is integrable for t>=t_N. For fixed N the earlier time interval is finite, so differentiating the Bochner integral is legitimate in the uniform derivative norm. Equations(20)-(21) prove(3). In particular the output classical C1 and Lipschitz norms are unbounded on this bounded C1 input sequence.

For C_*^1 itself a sum of packets is needed, since a large derivative alone is not a C_*^1 lower bound. Fix 0<epsilon<1/(2A), lambda=2^J, and take j between ceil((b+epsilon)J) and floor((1-epsilon)J), N=2^j. Set

 F_J=phi(s)psi(y)sum_j N^{-1}sin(Ny).                           (22)

The lacunary sum has uniformly bounded C_*^1 norm; each dyadic block meets only a bounded number of carriers. Multiplication by fixed smooth compact factors is bounded on C_*^1, so this remains true for F_J, whose support is fixed.

For a single summand write t=log(lambda/N)+tau and L0=lambda^{A-1}/N^A. In rescaled coordinates,

 lambda S_t f_N(S/lambda,Y/lambda)
 =e^{-tau}[Q_t(phi psi sin(Ny))](L0 e^{A tau}S,e^tau Y/N).       (23)

Uniformly over the stated j range, N tends to infinity, L0<=lambda^{-A epsilon} tends to0, and the lower time endpoint tends to minus infinity. On bounded tau intervals Fourier inversion, Q_t<=1 and Schwartz Fourier decay show that(23) tends to

 e^{-tau}phi(0)psi(0)sin(e^tau Y),

independent of S. Indeed the effective multiplier has transverse ratio e^{(A-1)t}/N=L0 e^{(A-1)tau}, tending to0 on bounded xi and on each carrier; the envelope arguments tend to0. Dominated convergence is uniform over the j range.

Choose a Schwartz test W whose Fourier support has nu bounded away from0 and kappa near0, and with nonzero trace of What at kappa=0. For tau>=0, the pairing in(23) has absolute value at most C e^{-tau}, because Q_t<=1 and the input Fourier L1 norm is uniformly bounded. For tau<=0 use that integral W(S,Y)Y^m dY=0 for m=0,1 and every S. The second Y derivative of(23) is at most C e^tau: the input second y derivative has Fourier L1 norm at most C N^2, and the chain rule contributes(e^tau/N)^2 e^{-tau}. Taylor subtraction in Y then bounds the pairing by C e^tau. These two integrable bounds are uniform in N,j,lambda and justify both time tails.

Consequently the pairing tends uniformly in j to that of the nonzero distribution

 -phi(0)psi(0)integral_R e^{-tau}sin(e^tau Y)dtau.               (24)

This formula is only used against the stated tests, so no absolutely convergent lower-end integral is asserted. Substitution v=e^tau gives integral sin(vY)dv/v^2. Its Fourier transform for nu>0 is a nonzero imaginary multiple of nu^{-2}; it is supported on kappa=0 in the transverse variable. Choose the phase of W so the limiting pairing has positive real part. Every packet then has the same positive contribution for large J. There are at least cJ packets. The local testing estimate(17), with beta=1 and ||RF_J||_2 uniformly bounded, yields

 ||RF_J||_{C_*^1(B_r)}>=cJ.                                    (25)

This proves necessity of the logarithmic loss at input1 separately from(3).

## 6. A fixed smooth forcing attaining the ceiling q

This independent argument avoids importing a generic cusp theorem. Choose nonzero real even compactly supported smooth functions u,v with nonzero integrals. Set phi=u*u and psi=v*v (for even real u,v these autocorrelations have nonnegative real Fourier transforms), and f(s,y)=-phi(s)psi'(y). Then f is smooth, even in s, odd in y, compactly supported, and

 fhat(xi,eta)=-i eta phihat(xi)psihat(eta).

For lambda tending to infinity use anisotropic spatial scaling

 G_lambda(S,Y)=lambda^q Rf(S/lambda,Y/lambda^{1/A}).

Substitute t=log(lambda)/A+tau into(5). On compact frequency sets with kappa>0 and nu>0, its Fourier transform converges to

 -|kappa|^{-a} integral_R e^{(a-A-2)tau}
 |(e^{-A tau}kappa,e^{-tau}nu)|^a
 fhat(e^{-A tau}kappa,e^{-tau}nu)dtau.                         (26)

All lambda factors cancel because q=a-(a-1)/A. The remaining output multiplier is
 |(kappa,lambda^{-(A-1)/A}nu)|^{-a}, converging uniformly to |kappa|^{-a}. At tau tending to minus infinity the Schwartz decay of fhat and kappa>0 dominates every exponential. At plus infinity fhat is O(e^{-tau}) because f is odd in y, while the norm factor is O(e^{-a tau}); the total is O(e^{-(A+3)tau}). Thus convergence follows by a uniform integrable majorant. The limit is nonzero: after multiplication by i its integrand has a fixed sign, and for sufficiently large finite tau both phihat and psihat are positive near0. No cancellation is possible.

Take a fixed Schwartz test with compact Fourier support where(26) is nonzero. The resulting physical test is lambda^{1+1/A}W(lambda s,lambda^{1/A}y). Its Fourier support lies in an isotropic annulus of radius comparable to lambda since kappa stays away from0, and its L1 norm is constant. The dyadic testing bound is therefore C lambda^{-beta}||h||_{C_*^beta}. Localization to any fixed ball has a tail smaller than any prescribed inverse power, since both dilation factors tend to infinity; the L2 tail argument from(17) applies. A nonzero limiting pairing forces

 ||Rf||_{C_*^beta(B_r)}>=c lambda^{beta-q}

for every sufficiently large lambda. This is impossible if beta>q and the norm is finite. Therefore this one fixed forcing attains the stated regularity ceiling. This proves the sharp ceiling claim in(v) but does not prove a logarithmic failure at the exact input sigma=a.

## 7. What does not transfer without additional proof

The frozen obstruction excludes a same-order inverse estimate for this L2-selected realization. It does not exclude an exact IPM profile, all choices of characteristic selection, or every space called Hölder-type. A correction equation must still specify its global domain, far asymptotics, source matching and scalar normalization.

The lead's optional variable-coefficient argument asserts that smooth compact truncations approximate the normalized Rf_N in the graph norm of L at order sigma. Membership in C_*^q intersect L2 alone does not supply the required global cutoff commutator and tail estimates for the unbounded vector field T. We have not proved this graph-density step here. Its use for a variable-coefficient Weyl sequence remains OPEN. Even after it is proved, coefficient regularity and global nonlocal tail estimates are separate hypotheses. P2 gives grad rho only in C^{1,alpha}; it does not make multiplication by grad rho bounded on C^{2,alpha}. A shrinking-packet argument that simply discards the coefficient error is therefore not accepted.

For a local isotropic Sobolev space in two dimensions, H^s embeds in C^{2,alpha} if s>3+alpha. The previously studied frozen energy threshold s_fast=[g+(A+3)/2]/A leaves a local window only if s_fast>3+alpha. This is a comparison of local sufficient conditions; it is not proof of a global IPM inverse or of a preferred unique method. The sigma=a logarithm, global realization, nearby nonlinear inverses, actual residual norms and quantitative closure all remain open here.

## 8. Numerical and reproducibility plan

The theorem is parameterized; no exact profile derivative is inferred from trial digits. For the lead's printed illustrative numbers use the explicit rationals A=101507/10000 and g=119/4. Also record the distinct illustration k=1615536043799051/9007199254740992, A=2/k-1, g=29749490663333/10^12 used in topic70. The latter g is a chosen nearby rational, not a verified exact-profile derivative. Keep both sets separate.

Before any numerical checks, save this proof and its hash. Check all rational exponent identities, the time and Fourier rescaling cancellations, signs of the geometric gaps, and endpoint table with exact rational arithmetic and an independent symbolic expansion. Enclose illustrative constants with Arb512 and mpmath.iv180, using exact rational inputs, then independently audit every saved enclosure at higher precision. These finite checks validate arithmetic only; the analysis above requires separate review. No Lean or other formal verification is claimed. Record actual Opus5.5 model, substantive responses and follow-up corrections alongside the checked sources.
