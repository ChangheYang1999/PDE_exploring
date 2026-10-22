# An exact conjugation for the full frozen source operator

Date: 2026-10-20. Status: CONFIRMED analytic model theorem after independent derivation and two actual Claude Opus 5.5 reviews. This is a whole-space constant-gradient, linear-drift model result. It is not an inverse for the variable-coefficient profile operator, nor an admissible P_2 correction-space theorem.

## Statement

Let A>1 and g be real constants. On coordinates (s,y) in R^2 let

T=A s partial_s+y partial_y,
M=(-partial_s^2)(-Delta)^(-1),
L=T-1-gM.

The multiplier M has symbol xi^2/(xi^2+eta^2). For the IPM convention -Delta psi=partial_s h and U=(-partial_y psi,partial_s psi), Fourier transformation gives psi_hat=i xi h_hat/r^2 and U_2[h]=-Mh, so this L is exactly the frozen coupled operator at a source with density gradient (0,g), omitting no part of its local order-zero velocity multiplier. The global rank-one normalization functional and variable coefficients are not part of this model.

Put a=g/(A-1) and Lambda=(-Delta)^(1/2). On the core C of functions whose Fourier transforms are smooth, compactly supported, and avoid zero, the exact conjugation identity is

Lambda^a L Lambda^(-a)=T+(a-1).

Let H_a be the Hilbert completion of C under ||h||_{H_a}=||Lambda^a h||_{L^2}. This specifies an abstract homogeneous Fourier space, without silently choosing representatives modulo polynomials. Its unitary identification with L^2 is h maps to Lambda^a h. Define the graph realization of L by transporting the closed generator domain described below through this identification. Set

c=a-(A+3)/2.

If c!=0, that realization is bijective from its graph domain to H_a and has inverse norm exactly 1/|c|. If c=0, it is injective but has no bounded inverse on H_a. The same inverse bound holds on the odd-y subspace, and also on the even-s, odd-y subspace. These symmetries are centered at this model source, not the origin symmetry of the full two-source profile.

## Fourier reconstruction of the identity

Use a unitary Fourier transform with frequency zeta=(xi,eta). Write D=A xi partial_xi+eta partial_eta and r=|zeta|. Fourier differentiation of multiplication by a coordinate gives

widehat(T h)=-D h_hat-(A+1)h_hat,
widehat(L h)=-D h_hat-(A+2)h_hat-g xi^2/r^2 h_hat.

Furthermore

D log r=1+(A-1)xi^2/r^2.

For a smooth Fourier function F supported away from zero,

r^a L_hat(r^(-a)F)
 =-D F+[a D log r-(A+2)-g xi^2/r^2]F
 =-D F-(A+2-a)F.

The M term cancels because a(A-1)=g. The last expression is the Fourier transform of (T+a-1)F_check. This proves the identity without replacing M by its horizontal-frequency limit.

## The closed graph domain and inverse

On L^2(R^2), define the strongly continuous unitary dilation group

(V_t H)(s,y)=exp((A+1)t/2)H(exp(A t)s,exp(t)y), t real.

A change of variables proves unitarity. Strong continuity follows first for compactly supported smooth functions by dominated convergence, then for all L^2 functions by density and the uniform norm bound. Its generator agrees on smooth functions with

S=T+(A+1)/2.

The precise closed domain is specified next.

One can see the closed realization directly, without an unproved core assertion. On y>0 use coordinates y=exp(t), s=exp(A t)v, and put

(J_+ H)(v,t)=exp((A+1)t/2)H(exp(A t)v,exp(t)).

The Jacobian is exp((A+1)t), so J_+ is a unitary map to L^2(dv dt). The same construction with y=-exp(t) gives J_- on the lower half-plane. Together J=(J_+,J_-) is unitary, since the omitted axis has measure zero. Under J the group V_tau is translation F(v,t) maps to F(v,t+tau), and S is partial_t on the maximal distribution domain

D(S)={H in L^2: partial_t JH in L^2}.

Fourier transform only in t identifies S with multiplication by i omega. This proves that S is closed and its kernel on L^2 is zero. Injectivity here refers to this L^2 realization, not to arbitrary local homogeneous solutions. The graph realization below is defined by this explicit unitary identification.

The maximal distribution domain on the full plane agrees with this generator domain. Indeed, a strong group derivative implies the distribution identity by testing against smooth compactly supported functions. Conversely, if the formal distribution derivative S H belongs to L^2, the chain rule for the linear dilation acting on test functions gives d_t V_t H=V_t(S H) in distributions. Integrating yields V_t H-H=integral_0^t V_tau(S H) d tau, an equality of L^2 functions. Strong continuity then proves that the strong group derivative at zero is S H. This argument applies equally after Fourier transform and avoids any unproved identification across the omitted physical axis.

For completeness the Fourier core is indeed a graph core, as follows by an elementary approximation. On Fourier space the generator is -D-(A+1)/2. For a function F in its maximal distribution domain, multiply by smooth radial cutoffs chi_n supported in 1/(2n)<r<2n and equal to one on 1/n<r<n. Choose them by fixed dilations so that |D chi_n| is uniformly bounded. Then chi_n F tends to F in L^2, and D(chi_n F)=chi_n DF+(D chi_n)F tends to DF because the extra term is supported in shrinking inner and escaping outer annuli. Next convolve each truncated function with a smooth compactly supported approximate identity small enough to remain away from zero. If eta_epsilon is that mollifier,

D(F*eta_epsilon)-(DF)*eta_epsilon=F*K_epsilon,
K_epsilon=(A+1)eta_epsilon+D eta_epsilon.

This identity follows by integration by parts in the distribution formula. The integral of K_epsilon is zero and its L^1 norm is bounded independently of epsilon, since D has linear coefficients. Therefore

||F*K_epsilon||_2
 <=integral |K_epsilon(z)| ||F(. -z)-F(.)||_2 dz tends to zero,

by continuity of translations in L^2. The smoothed Fourier functions approximate in the graph norm and belong to the stated core. Conversely their graph closure is in the maximal domain because distribution differentiation is closed under simultaneous L^2 convergence of the function and its derivative. This proves the core assertion directly. Lambda^a maps this core bijectively onto itself, since r^a is smooth and nonzero on its compact Fourier supports.

The graph realization of L is precisely

D(L)={h in H_a:Lambda^a h belongs to D(S)},
L=Lambda^(-a)(S+c)Lambda^a.

For c>0, define the convergent Bochner integral

(S+c)^(-1)F=integral_0^infinity exp(-c t)V_{-t}F dt.

For c<0, define

(S+c)^(-1)F=-integral_0^infinity exp(c t)V_t F dt.

Unitarity gives norm at most 1/|c|. In the (v,omega) representation these formulas multiply by (c+i omega)^(-1), which proves both left and right inverse identities and membership in D(S): |omega/(c+i omega)|<=1. The essential supremum of |c+i omega|^(-1) is exactly 1/|c|. It is approached by nonzero Fourier data supported in |omega|<epsilon, so the inverse bound is sharp. At c=0, the same localized data have unit norm and S-image norm at most epsilon, proving failure of any bounded-below estimate. A t-independent L^2 function on the full t line is zero, so the kernel is nevertheless trivial.

The operators Lambda, M, and V_t preserve reflections in s and y. In the J representation oddness in y identifies the two half-plane components up to sign. Evenness in s is evenness in v. The same low-omega data with an even nonzero v factor prove sharpness in the indicated parity subspaces.

## Relation to an actual source and limits

For the illustrative rounded values A=10.1507252 and g=29.75, a is about 3.25 and c is negative. These rounded numbers are not certified profile data. The exact formulas, with any certified interval input separated from c=0, would give a model inverse constant. The result shows that the frozen full order-zero operator admits an explicit nonlocal conjugation; it does not establish a local Fredholm index from a heuristic M approximately 1.

Several missing steps prevent using this result as the required IPM inverse. The space H_a is homogeneous and does not on its own supply a canonical function representative, center factorization, weighted far-field growth, or source-local boundary traces. At the illustrative a about 3.25, the obstruction to an ordinary distribution representative already occurs: r^(-a) times an arbitrary L^2 Fourier function need not be locally integrable at zero. One may choose a tempered representative by testing it only after subtracting a fixed smooth-cutoff Taylor polynomial through degree two from the test function. The remainder is O(r^3), and Cauchy-Schwarz makes the integral finite since a<4. Different choices change a polynomial of degree at most two in physical space. This note instead uses the abstract completion throughout. The multiplier M and the original differential expression are asserted on the Fourier core; their closed realization on the completion is specified by the conjugation, with no unexplained action on polynomial representatives. Multiplication by spatial cutoffs does not commute with Lambda^a, and neither does a variable density gradient. Variable source drift, the origin saddle, both sources, the global rank-one normalization and far-field matching are absent from L. Quantitative commutator and gluing estimates would be needed, followed by a genuine global injectivity and surjectivity argument. No such estimate is claimed here.
