# A conditional Fredholm realization at even integer order

Status: CONFIRMED, 2026-10-20, after independent derivation and checking, the actual Opus5.5 lead audit, and the separate referee fred2 adversarial audit. The parity and Fourier-tail omissions identified by that audit are repaired explicitly below. This is a conditional theorem, not an existence or nonexistence endpoint. No numerical singular value is used.

## 1. Statement and hypotheses

Let (rho,ell) be an exact smooth primary IPM profile: ell>1, a=rho_y(0) nonzero, rho even in x and odd in y, U the canonical full-plane velocity, W=ell X+U, W.grad rho=rho. Include the primary growth condition |rho|+(1+r)|grad rho|<=C(1+r)^gamma for some 0<gamma<1. Thus div W=2ell and DW(0)=diag(A,1), A=2ell-1. Assume additionally:

(Hdyn) Every nonzero trajectory tends to zero in backward time and to infinity in forward time.

(Hsym) For every multi-index beta, outside a fixed circle,

    |partial^beta rho|+|partial^beta U|<=C_beta r^(p-|beta|), p=1/ell.

The displayed Hsym bounds follow from the exact primary assumptions by ../local_ipm_continuation/PROOF.md (result32), whose independent review was completed before the present audit. We retain the name to show each use of those bounds. Hdyn is an additional assumption, equivalent to the strict sign condition by ../sign_and_local_uniqueness/PROOF.md. It is not automatic for the primary class.

Choose p<nu<1 and an even integer s=2m>=4 such that

    s>max(1+ell, (1+ell+max(a,0))/A).                       (1)

Let E=E_nu^s be the dyadic weighted Sobolev space described in the preceding result, and let

    P0 h=W.grad h-h,
    N h=V[h].grad rho,
    P_tau=P0+tau N, 0<=tau<=1,
    X={h in E:P0 h in E}, ||h||_X=||h||_E+||P0h||_E.       (2)

The canonical perturbation inverse V uses no harmonic strain. All spaces have density parity. Then P_tau:X->E is a norm-continuous family of Fredholm operators, all of index0.

Consequently the augmented linearization

    L(h,delta)=P_1 h+delta X.grad rho, X x R -> E            (3)

is Fredholm of index1. Its kernel contains (rho-X.grad rho,0). The assertion that this is its whole kernel is an additional hypothesis, not a consequence. The nonlinear uniqueness inference of ../sign_and_local_uniqueness/PROOF.md assumes Fredholmness on this same Sobolev graph realization and measures the neighbourhood of exact profiles in a stronger weighted Holder norm. The dyadic norms and maximal graph domains there and here agree up to equivalent norms. Thus this result supplies its Fredholm/index hypothesis at the allowed even orders; kernel simplicity remains an additional hypothesis. No transfer of Fredholmness to Holder spaces is required or asserted. Nothing here establishes a solution or excludes a profile outside Hdyn.

## 2. Fixed domain and a usable Hilbert norm

Use the complete metric g=b(r)^2 dX^2, with b=1 for r<=2 and b=1/r for r>=4, modified by harmless radius changes when necessary. Its end is the flat cylinder t=log r. Let A_m=(1-Delta_g)^m. For a positive even-even weight w equivalent to r^(-nu), with bounded covariant derivatives of log w, put J h=A_m(w h) and ||h||_E=||Jh||_(L2(g)). This is an equivalent norm on the stated E.

The complete proof in ../integer_sobolev_conjugation/PROOF.md establishes boundedness of N on E, the distributional conjugation

    B_tau=J P_tau J^-1=T+C_tau,
    T=W.grad+(div_g W)/2,
    C_tau bounded on L2(g),                               (4)

and the common maximal domain D(B_tau)=D(T). The complete transport group makes T skew-adjoint. Moreover B_tau*=-T+C_tau* on the very same domain, and the original compactly supported smooth density tests are a graph core. These assertions hold for the weight constructed below. For reference, write D=W.grad, b0=-1-D log w. The exact bounded remainder is

    C_tau=[A_m,D]A_m^-1+A_m b0 A_m^-1
          +tau A_m w N w^-1 A_m^-1-(div_g W)/2.             (5)

The only step still needed for Fredholmness is a compact-error positive real-part estimate. We now prove it.

## 3. Escape weight and its derivatives

Choose a small outward sphere about the source and a large outward sphere in the sublinear end. Under Hdyn every trajectory issuing from the small sphere crosses the large one. Its crossing time is continuous: transversality gives local continuous crossing times, and a trajectory cannot return across an outward sphere. Compactness of the small sphere then bounds these times uniformly. The same argument works after slightly enlarging the annulus.

Choose an even-even chi>=0 supported in that enlarged annulus and equal to1 on a prescribed compact transition annulus. Set

    F(X)=integral_(-infinity)^0 chi(Phi_t X) dt.             (6)

The uniform transit bound proves F bounded. On each compact set the nonzero integrand lies in a uniformly bounded time interval, so differentiating under the integral proves smoothness. It vanishes near zero and satisfies D F=chi. Far beyond the support of chi it is constant along each trajectory.

The last statement also gives bounded cylinder derivatives of F. Indeed, on a large exterior circle its value is smooth. In (t,theta) coordinates the angular ODE has coefficient Q/V, with all cylinder derivatives O(exp(-(1-p)t)) by Hsym. Its integral and all derivative equations converge uniformly, giving bounded smooth angular transport maps and inverse maps. Transporting the smooth circle value through these maps gives bounded derivatives of every order of F on the end. This is the exterior ODE argument from Section4 of ../sign_and_local_uniqueness/PROOF.md, applied to a quantity constant along trajectories. Its parity follows from that of chi and W.

Choose w0=1 near zero and w0=r^(-nu) near infinity, positive and smooth. Set

    w=exp(-M F)w0.                                        (7)

For each finite M it has all the properties needed for Section2. It changes -D log w by the positive scalar M chi, while remaining equivalent to w0. The number M will be fixed using the compact transition region.

## 4. The local real matrix of the bounded remainder

In physical coordinates, write sym DW=(DW+DW^T)/2. Define the symmetric matrix

    H_tau = s sym DW
       + [s D log b -1-D log w -(div_g W)/2] I
       + tau [[-rho_y, rho_x/2],[rho_x/2,0]].               (8)

We need the following concrete local operator fact. If zeta is a smooth compactly supported even-even cutoff, the real quadratic form of zeta C_tau zeta, after the unitary density conversion from L2(g) to ordinary L2 on that compact set, has the same form modulo a compact operator as

    sum_(i,j) R_i* zeta^2 (H_tau)_(ij) R_j,                (9)

where R_j has Fourier multiplier i xi_j/(1+|xi|^2)^(1/2). All coefficients in (9) are smoothly extended outside the compact set. Only their values on the support matter modulo compact terms. A precise local meaning is obtained by using an input cutoff equal to1 on that support; changing this cutoff changes only a compact remainder. Also [C_tau,zeta] is compact on L2(g).

Here is a proof specialized to (5). Every cutoff applied to the parity-sector operator C_tau, its conjugated density, or a canonical far-input piece is even-even. Radial localizers suffice throughout; overlapping localizations may be symmetrized over the two reflections. Auxiliary Euclidean Fourier operators are considered on full L2, so individual R_j need not preserve density parity. No canonical inverse for arbitrary growing non-parity input is introduced. The proof avoids a general phase-space positivity theorem.

First, the elementary Fourier fact used repeatedly is this: for a smooth order-zero multiplier m with |partial^beta m(xi)|<=C_beta(1+|xi|)^(-|beta|), and a smooth compact coefficient f, [m(D),f] maps L2 to H1. In Fourier variables its kernel is fhat(xi-eta)[m(xi)-m(eta)]. The mean value theorem, splitting |xi-eta|<=|eta|/2 and its complement, bounds (1+|xi|)|m(xi)-m(eta)| by a fixed polynomial in |xi-eta|. The Fourier transform of f decays faster than any power. The convolution L1 bound proves the assertion. Multipliers of order-1 likewise map L2 to H1. With compact output support, these maps are compact into L2 by Rellich. The full commutator is also compact, as follows. If k_m is the distribution kernel of m(D), then away from z=0, |k_m(z)|<=C_N |z|^(-N) for |z|>=1 and every integer N>2. Indeed choose a coordinate with |z_j|>=|z|/sqrt(2); partial_(xi_j)^N m is integrable for N>2, and the distribution identity z_j^N k_m is its inverse Fourier transform, a bounded continuous function. This proves the bound there; a contact distribution at zero has no effect. For X outside a large disk containing supp f, the commutator kernel is k_m(X-Y)f(Y). Its squared integral over X outside that disk and Y in supp f tends to zero. The omitted output therefore has norm tending to zero by the Hilbert-Schmidt bound. Combining this with compactness of every compact output localization proves [m(D),f] compact on full L2. This argument is needed when moving Fourier factors outside cutoffs.

A bounded multiplier supported in a bounded frequency set has an L2 symbol and an L2 inverse Fourier kernel. Its product on either side with a compact smooth multiplication operator is Hilbert-Schmidt: the squared kernel norm is the product of the squared L2 norms of the two factors. Thus the nonsmooth low-frequency parts of the actual Riesz multipliers cause only compact localized errors. Their high-frequency parts can be replaced by smooth order-zero symbols as above. Local derivative gain alone would not prove either full-output assertion. These Euclidean tail arguments are separate from the cylindrical estimate (15).

Second, on any fixed compact coordinate region the principal differential part of A_m is b^(-s)(-Delta)^m. Put D_m=(1-Delta)^m and extend b smoothly, positive and bounded above and below, beyond that region. The differential parametrix Q=b^s D_m^-1 has A_m Q-I of order-1 locally: expanding products cancels the order0 term and leaves differential operators of order at most s-1 after D_m^-1. It follows that A_m^-1-Q gains s+1 derivatives locally on localized L2 input. To check the last statement, the difference already belongs locally to H^s by the elliptic estimate, and applying A_m gives a locally H1 right-hand side. Cutoff commutators have order s-1 and map the known H^s difference into H1. The local elliptic estimate at one higher order supplies H^(s+1). Thus, after composing with any order-s differential operator and taking compact output, this replacement makes only a compact L2 error.

Expand [A_m,D] using this parametrix. Its degree-s Fourier numerator divided by |xi|^s is

    s xi^T(sym DW)xi/|xi|^2+s D log b.                    (10)

This can be checked directly: [-Delta,D] has principal part -2(partial_i W_j)partial_ij; there are m such factors, giving s=2m, and [b^(-s),D]=s b^(-s)D log b. Lower differential terms gain a derivative after the inverse. Replacing |xi|^-2 by (1+|xi|^2)^-1 changes only order-2 terms. The first Fourier fact allows moving smooth coefficients past the order-zero factors modulo compact operators. Hence the real part of this term is (9) with its first two contributions.

Similarly A_m b0 A_m^-1-b0=[A_m,b0]A_m^-1 has compactly localized order-1 remainder. The scalar coefficient -div_g W/2 acts by multiplication. It is generally spatially variable: it equals -ell at the source and tends to zero on the end. For N, the exact Fourier symbols of V on a localized density are

    V_1: xi_1 xi_2/|xi|^2,
    V_2: -xi_1^2/|xi|^2.                                 (11)

The local parametrix, coefficient commutator fact and commutation of constant-coefficient derivatives with (11) show that conjugation by A_m and w leaves its degree0 part unchanged. Its real scalar numerator is rho_x xi_1 xi_2-rho_y xi_1^2, precisely the last matrix in (8). Each commutator or lower differential term gains one derivative locally. Conversion between L2(g) and Euclidean L2 is multiplication by smooth b and has the same type of compact commutator. This proves the local formula (9).

For clarity about nonlocal input, if input and compact output are separated, the inverse A_m^-1 satisfies a homogeneous elliptic equation near the output, so its derivatives there gain every order with bounds from its global H^s norm. The canonical V kernel is smooth across separated supports; its far-input derivatives are uniformly controlled by the summable annular cancellation estimates. If the input is first transformed by A_m^-1, split its density by an even-even cutoff into a neighbourhood of the output and its complement. The neighbourhood piece has the extra local elliptic derivatives; the complement is handled by the smooth kernel bound. Consequently all the separated pieces in (5), with compact output, map bounded sets to bounded local H1 sets after the order-s conjugation. They are compact. These arguments prove compactness of every compactly output-localized piece of [C_tau,zeta]: in the overlapping region its leading term cancels by the Fourier commutator calculation, while separated regions have just been handled. To pass to its full output, use (15) below. Outside any large compact set containing supp zeta, the commutator equals C_tau zeta=(C_tau-(ell nu-1)I)zeta, whose output norm tends to zero by (15). Thus the full commutator is a norm limit of compact operators, hence compact. This use of Section5 is not circular: (15) follows directly from (5) and the coefficient estimates, without a commutator compactness assertion. It completes the local fact.

## 5. Strict positivity at the source, in transit, and at infinity

Near zero b=w0=1 and F=0. At zero equation(8) gives

    H_tau(0)=diag(s A-1-ell-tau a, s-1-ell).               (12)

Condition(1) gives a uniform positive lower bound for every tau in[0,1]. Smoothness and compactness of that parameter interval preserve a positive margin on a fixed small ball. This step is the exact Sobolev source threshold, including the volume term 1+ell; it is not the pointwise Holder indicial threshold.

On the end, DW=ell I+O(r^(p-1)), D log b=-ell+O(r^(p-1)), div_g W=O(r^(p-1)), and grad rho=O(r^(p-1)). Also D F=0 beyond the cutoff support and D log w0=-nu ell+O(r^(p-1)). Therefore

    H_tau=(ell nu-1)I+O(r^(p-1)),                          (13)

uniformly with all cylinder derivatives needed. Since nu>p, this is uniformly positive sufficiently far out. The initial choice of chi can cover the remaining compact annulus with chi=1. Its contribution M chi I in (8) then makes H_tau>=epsilon0 I everywhere, for one sufficiently large fixed M and epsilon0>0, independent of tau.

We also need a norm assertion at infinity, not just its principal matrix. In the cylinder g is flat and A_m=(1-partial_t^2-partial_theta^2)^m. The constant field ell partial_t commutes with A_m. Thus the coefficients of [A_m,D] tend to zero at rate exp(-(1-p)t), in all the required derivatives. The coefficients of b0-(ell nu-1) and div_g W do too. From (5) and A_m^-1:L2->H^s it follows that their outputs, restricted to t>T, have operator norm O(exp(-(1-p)T)). The N term has the same property: all scaled derivatives of grad rho are O(exp(-(1-p)t)); the product estimate and V:E->E bound give

    ||1_(t>T) A_m w N w^-1 A_m^-1 v||_2
            <=C exp(-(1-p)T)||v||_2.                      (14)

Derivatives of w/r^(-nu) are bounded; no decay of F itself is needed. Consequently

    ||1_(t>T) [C_tau-(ell nu-1)I]||_(L2->L2)->0.           (15)

This output estimate is stronger than the two-sided cutoff estimate needed below. It does not say N is compact on the core.

## 6. Compact-error energy and Fredholmness

Choose smooth real even-even cutoffs zeta0,zeta1 with zeta0 compactly supported, zeta1 supported in the sufficiently distant end, and zeta0^2+zeta1^2=1. The transition lies where both descriptions are valid. The commutators from Section4 are compact, including [C_tau,zeta1] since zeta1-1 has compact support. Therefore

    C_tau - zeta0 C_tau zeta0-zeta1 C_tau zeta1

is compact. On the end, (15) gives

    Re <C_tau zeta1 v,zeta1 v>
            >=(ell nu-1)/2 ||zeta1 v||^2

after choosing the cutoff far enough out. On the compact part use (9) and H_tau>=epsilon0 I. Since

    sum_j R_j* R_j=I-(1-Delta)^-1,

and commuting the cutoffs makes compact errors, the compact contribution is bounded below by epsilon0||zeta0 v||^2 modulo a compact quadratic form. This last conclusion follows directly from

    sum_(i,j) <zeta0^2 H_ij R_j v,R_i v>
         >=epsilon0 sum_j ||zeta0 R_j v||^2,

together with the displayed identity and the first Fourier fact. The density conversion to Euclidean measure is unitary on the compact support, so it does not change this lower bound or compactness.

Combining the two regions, there are epsilon>0 and a compact self-adjoint remainder K0 such that

    Re <C_tau v,v> >=epsilon||v||^2-<|K0|v,v>.

Set K=|K0|^(1/2), compact by the spectral theorem for compact self-adjoint operators. Since T is skew-adjoint, this proves

    Re <B_tau v,v> >=epsilon||v||^2-||Kv||^2.              (16)

The bounded form calculation holds on all L2 for C_tau, hence on the maximal transport domain for B_tau. Its adjoint has the identical real form on that same domain by (4). The elementary compact-error lemma in ../transport_graph_domains/PROOF.md now proves finite kernel and cokernel and closed range. Thus every P_tau is Fredholm. The family is continuous on the fixed graph space because N:E->E is bounded. Its index is constant on[0,1]. No unverified adjoint regularization or density-core step remains in this argument.

## 7. Computing the index at tau0

Let J0 h=h_y(0), a continuous functional on E since s>=4. For h in X, local embedding and the smooth coefficients allow differentiating P0h at zero; the center identity gives

    J0(P0h)=0.                                            (17)

The source label eta=rho/a belongs to E by Hsym and nu>p. It spans ker P0. Indeed, if P0h=0, the function h-(J0h)eta vanishes to second order at zero by local C2 regularity and parity. Backward source contraction at any rate lambda<1 sufficiently near1 gives

    h(X)-(J0h)eta(X)
       =exp(T)[h-(J0h)eta](Phi_(-T)X)->0

as T->infinity, since the right side is O(exp((1-2lambda)T)). Hdyn lets every point enter that neighbourhood. Thus the kernel is exactly one-dimensional.

We next prove ran P0 is all ker J0. Let f be smooth compactly supported with density parity and J0f=0. Parity gives f=O(r^3) near0. Define

    h(X)=integral_(-infinity)^0 exp(-t) f(Phi_t X) dt.      (18)

The source contraction makes this converge. It is smooth at and near zero: derivatives of the backward source flow of any fixed order are O(exp(lambda t)), t<=0, for any fixed lambda<1 sufficiently close to1. This follows inductively from the variational equations, since the linear part has eigenvalues A,1 and the nonlinear part has small first derivative near0. In each derivative of f(Phi_t X), its vanishing to cubic order makes the terms with at most3 outer derivatives O(exp(3lambda t)); terms with more outer derivatives have at least that decay as well. Thus all differentiated integrands in (18) are integrable when 3lambda>1. The identity obtained by changing the upper endpoint along the flow gives P0h=f.

Outside a circle containing supp f, this h solves the homogeneous transport equation with smooth data on that circle. Hsym and the exterior angular/travel-time argument prove h has all symbol bounds O(r^(p-|beta|)). Hence h in E and P0h=f in E, so h in X. Such f are dense in ker J0: approximate in E by compact smooth parity tests and subtract their J0 values times one fixed compact test with J0=1. Fredholmness has already supplied closed range. Together with (17), this proves ran P0=ker J0, of codimension1. Thus ind P0=1-1=0, and the whole family has index0.

For clarity, (18) extends to every compatible f in ker J0, not to unrestricted E. Restrict P0 to X0={h in X:J0h=0}. The kernel and range statements make P0:X0->ker J0 a bounded bijection, whose inverse S is bounded in the graph norm by the Banach inverse theorem. The compact smooth compatible approximations f_n above have characteristic solutions h_n with J0h_n=0, so h_n=S f_n converge in X. For a compact set of initial points, Hdyn and the source contraction put all backward trajectories in the small source ball after a common finite time. For g=f_n-f, local C2 embedding and zero trace give |g(Z)|<=C||g||_(C2) |Z|^2 there. The corresponding backward-integral tail is bounded by C||g||_(C2) integral_T^infinity exp(-(2lambda-1)t)dt, with lambda>1/2. The finite integral segment converges in local C0. Thus h_n also converge locally uniformly to (18) for f, identifying it with S f and proving graph membership without assuming symbol bounds for arbitrary E data. Compatibility is essential: f=y zeta(r), zeta=1 near0, has f_y(0)=1. Along a small nonzero y-axis orbit, exp(T)y(Phi_(-T)X) has a nonzero limit because W2(0,y)=y+O(y^3). Its integral (18) diverges. This countertest concerns the unrestricted formula, not the compatible range assertion.

Finally G=X.grad rho belongs to E by Hsym. Adding the one-dimensional domain column delta G is a finite-rank perturbation of the operator that ignores that scalar; its index is index P_1+1=1. Differentiating the exact scaling orbit proves the indicated kernel vector. It is nonzero, since a smooth degree1 homogeneous primary density would be the excluded affine profile. This finishes the conditional statement.

## 8. Scope and verification record

Hsym is used in the high-order multiplier bounds, escape-function derivatives and end estimate (15); result32 now proves it for every exact primary profile. Hdyn supplies the global transit construction and transport index and remains an additional dynamical assumption. The strict inequality in (1) and even integer order s=2m>=4 are essential to this particular realization. No assertion at arbitrary real s, at an equality threshold, or in a Holder topology is made.

Dependencies are the independently checked inverse, origin, transport graph, integer Sobolev conjugation and local IPM continuation results. The actual Opus5.5 lead read this proof on 2026-10-20T15:56Z, found no objection, and requested a further check of the compactness reductions. The separate referee fred2 audit, returned by 16:38Z, read this proof and the two domain companions in full, supplied the parity and full Fourier-tail repairs, and checked the transport-range argument. The verifier independently checked each repair against the kernels and domain, incorporated it above, and explicitly separated the Holder uniqueness scope. Nine exact symbolic checks in that audit supplement the proof; they are not operator compactness certificates. The audit's attempted Opus call failed during credential retrieval, so it supplies no additional Opus execution or endorsement. No proof-assistant verification is claimed. Exact input hashes, audit paths and repair-check record are in verification/audit_resolution.json.
