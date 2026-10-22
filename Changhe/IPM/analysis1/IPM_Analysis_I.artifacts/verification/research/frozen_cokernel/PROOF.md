# Explicit infinite-dimensional cokernels of the frozen whole-plane operator

Date: 2026-10-20. Status: CONFIRMED frozen-model theorem after independent derivation and actual Claude Opus 5.5 adversarial audit. This concerns a globally linear drift with constant density gradient. It is not a local source-index theorem or a global profile obstruction.

## Statement

Let A>1, g>=0, b=(A+3)/2, s_fast=(g+b)/A and s_slow=b. Let L=A x partial_x+y partial_y-1-gM, with M symbol xi^2/(xi^2+eta^2), on the dilation graph realization described in ../coupled_thresholds/PROOF.md.

1. In the homogeneous Fourier space H_s, if s_fast<s<s_slow, the adjoint kernel is infinite-dimensional. If s_slow<s<s_fast, the kernel is infinite-dimensional. Both statements hold in the even-x, odd-y subspace as well. Thus these realizations are not Fredholm in either open band.
2. In the ordinary whole-plane Sobolev space H^s, for every s>s_fast the adjoint kernel is infinite-dimensional, including in the even-x, odd-y subspace. In particular, merely raising ordinary isotropic Sobolev order does not make this frozen whole-plane realization surjective.
3. At s=s_fast the ordinary H^s realization has normalized approximate kernels. This does not assert existence of such kernels below s_fast. If s_fast<=s_slow, the preceding coercivity theorem proves bijectivity for every 0<=s<s_fast.

All statements refer to graph domains. No axis boundary condition or exterior extension is imposed on a disc. These distinctions are essential to their scope.

## Fourier dilation coordinates

Let W_s be multiplication by r^s for the homogeneous norm or by (1+r^2)^(s/2) for the ordinary norm. It is a unitary map from the respective completion to Fourier L^2. Write D=A xi partial_xi+eta partial_eta, and let S=-D-(A+1)/2. The transformed operator is S+C, with

C_h=s-b+[s(A-1)-g]m,
C_i=-b-gm+s(A xi^2+eta^2)/(1+xi^2+eta^2),
m=xi^2/(xi^2+eta^2).

The homogeneous space here is the abstract Fourier completion, not a chosen class of distribution representatives modulo no polynomials. Both C's are bounded real functions. The operator adjoint is -S+C on the same generator domain, by the bounded perturbation argument already proved in the cited note.

On each half-plane eta=epsilon exp(t), epsilon in {-1,1}, put xi=exp(A t)v. The Jacobian is exp((A+1)t). Thus

(J F)_epsilon(v,t)=exp((A+1)t/2)F(exp(A t)v,epsilon exp(t))

is unitary onto two copies of L^2(dv dt). The frequency axis eta=0 has measure zero. Direct differentiation gives J S J^(-1)=-partial_t. The maximal domain is exactly functions whose distributional t derivative belongs to L^2; this also follows from the unitary translation group. No v derivative is required. In these coordinates

m(v,t)=v^2 exp(2(A-1)t)/(1+v^2 exp(2(A-1)t)).

We will choose v in 1<=|v|<=2, so all asymptotic estimates below are uniform on its support.

## Homogeneous adjoint and kernel

For the homogeneous case, an exact positive solution of (partial_t+C_h)G=0 is

G_h(v,t)=exp((b-s)t) [1+v^2 exp(2(A-1)t)]^((g-s(A-1))/(2(A-1))).

This follows by logarithmic differentiation, since the derivative of log(1+v^2 exp(2(A-1)t)) is 2(A-1)m. As t tends to minus infinity, G_h is uniformly comparable to exp((b-s)t). As t tends to plus infinity, it is uniformly comparable to exp((b+g-A s)t). If s_fast<s<s_slow, the first exponent is positive and the second is negative, so G_h and its t derivative are square integrable, uniformly for 1<=|v|<=2. The derivative is -C_h G_h and C_h is bounded.

For every a(v) in L^2 supported in 1<=|v|<=2, a(v)G_h(v,t) belongs to the adjoint domain and its image is zero. This map is injective, since G_h is positive, and is bounded above and below in L^2 by uniform bounds on its positive t integral over the compact v set. Hence the adjoint kernel contains an infinite-dimensional closed subspace. The adjoint kernel is the orthogonal complement of the range. Its injection into the algebraic quotient by the range is injective, so this already gives infinitely many missing range directions whether or not the range is closed.

For s_slow<s<s_fast use instead G_h^(-1), which solves (-partial_t+C_h)G=0. Its asymptotic exponents are s-b at minus infinity and A s-g-b at plus infinity. They again have the signs required for square integrability. The same construction gives an infinite-dimensional kernel.

## Ordinary Sobolev adjoint

For the ordinary H^s norm define

G_i(v,t)=exp(b t) [1+v^2 exp(2(A-1)t)]^(g/(2(A-1)))
             [1+exp(2t)+v^2 exp(2A t)]^(-s/2).

Its logarithmic derivative is

b+g m-s [exp(2t)+A v^2 exp(2A t)]/[1+exp(2t)+v^2 exp(2A t)] = -C_i.

It therefore solves the exact adjoint equation. At minus infinity it is comparable to exp(b t); at plus infinity it is comparable to exp((b+g-A s)t). For s>s_fast both ends decay in their respective directions. The preceding construction with arbitrary a(v) proves the infinite-dimensional adjoint kernel, including graph-domain membership. This is an exact formula, not a principal-symbol approximation.

At s=s_fast, C_i(v,t) tends to zero uniformly on 1<=|v|<=2 as t tends to plus infinity. Let a be a unit L^2 function supported there, and let chi be smooth, nonzero and supported in (0,1), with L^2 norm one. Set

F_N(v,t)=a(v)N^(-1/2)chi((t-N^2)/N).

Then ||F_N||_2=1, ||partial_t F_N||_2=||chi'||_2/N, and ||C_i F_N||_2 tends to zero. Thus ||(-partial_t+C_i)F_N||_2 tends to zero. They converge weakly to zero because their supports escape to t=plus infinity, as follows by Cauchy-Schwarz against the L^2 tail of any fixed test function. Transforming back gives the stated graph-domain approximate kernels at the critical order.

## Reflections and limits

Reflection in x corresponds to v maps to -v. Reflection in y swaps the two eta signs with the same v. The displayed profiles depend only on v^2. Choose a even in v and take opposite signs in the two eta components; this yields even-x, odd-y data. There are infinitely many even a supported in 1<=|v|<=2, so the kernel and cokernel dimensions and the critical sequences survive this restriction. If real-valued physical functions are wanted, multiply these real odd-eta Fourier functions by i, obtaining the required Hermitian symmetry under full frequency reversal.

For the rounded illustration A=10.1507252 and g=29.75, s_fast is about 3.5786 and s_slow about 6.5754. The ordinary frozen H^4 and H^5 realizations have infinite-dimensional cokernel; the homogeneous H_4 and H_5 realizations do also. Ordinary H^3 has the confirmed coercive inverse. These facts cannot be transplanted to a disc or a variable-coefficient operator without controlling spatial cutoffs, their nonlocal commutators, and the changed global flow and function space. In particular they do not prove SPEC's proposed normalized index -1, nor do they exclude a nearby P_2 profile.
