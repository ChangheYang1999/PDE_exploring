# Audit of the single-operator proof for rough transport perturbations

## Exact setting and conclusions

Use the exact normalized modal case1 trial rho_bar and the canonical velocity U=(-R_1R_2,R_1^2). Set ell=1/k, k=1615536043799051/9007199254740992, V=ell X+U[rho_bar], and write W=(V.e_r/r,V.e_theta/r) on the cylinder C=R times S1. Fix the smooth weight b(t) of proof 158, equal to exp((3+9/5)t) far left and exp(-t/2) far right, and put beta=b'/b. Fix the explicit repeller-block order of proof 130, with 41/20<=s<=25/4, and the nested vertical cutoffs of proof 158. The order equals sigma=25/4 near these cutoffs.

Let p(theta)=cos(theta)^2 sin(theta). The real Hilbert space X_s consists of even-x, odd-y h such that v=h/b lies in H^{s(.)}, u=chi h/(bp) lies in H^sigma, and the two vertical traces of u vanish. Its norm is the square sum of these two Sobolev norms. Let G_s consist of g=J x^2y chi_0(t)+b v_g of the same parity, with v_g in H^{s(.)} and chi_1 v_g/p in H^sigma, without the zero-trace constraint. Its norm is |J| plus these two norms. These fixed definitions are the ones in proof 158.

Set

 B_g=(U[g].e_r/r,U[g].e_theta/r)+(c[g]/3,0),
 T_g h=(V+U[g]+c[g]X/3).grad h-h,
 S_g=T_g+C_R,
 D_g={h in X_s:T_g h in X_s in distributions},

where c[g]=partial_y U_2[g](0) and C_R is the fixed remainder coupling of the exact trial. D_g has its maximal graph norm.

The single-operator argument in the theory author's work/Hs_pert.md proves the following, after the energy-sign correction below. For each finite L, some r,C>0 and a fixed compact K satisfy

 ||h||X_s<=C||(S_g-lambda)h||X_s+||Kh||,
 ||g||G_s<=r, h in D_g, 0<=lambda<=L.                  (1)

It also gives the intermediate estimate with X_(s-epsilon) and the fixed compact coupling remainder, for epsilon=1/2560. Both Sobolev orders are reduced by epsilon in that lower space. The proof is qualitative. Generation and index zero, and a uniform inverse conditional on base injectivity, have the exact meanings and domains in proof 159. The argument reviewed here supplies a second route to the estimate already proved dyadically in proof 158.

## The commutator, products and exact logarithm

Proof 161 proves the theory author's Lemmas K and P, including output almost orthogonality in the low-coefficient term and absolute summation in the high-coefficient term with A inside. No assertion about the full transport commutator is inferred from the coefficient commutator. In particular

 A(B_g.grad v)=B_g.grad(Av)-N(B_g.grad Lambda)Av
 -(B_g.grad s)Op(a log<xi>)v+K_(B_g)v.

The smooth composition Op(a log<xi>)-log<D>A has relative order minus one with harmless powers of log<xi>. It therefore maps H^(s-epsilon) to L2 for the displayed epsilon. Its multiplication by B_g.grad s is bounded on L2. Proof 155 bounds B_g and all needed bulk or divided cofactor scalar coefficients by C||g||G_s, after separating the fixed smooth central-strain field. Thus the remaining terms have L2 norm bounded by C||g||G_s||v||H^s plus a uniform lower-order norm.

The fixed repeller-block order is essential: proof 152 gives W.grad s>=kappa_s|grad s|. The same s therefore has (W+B_g).grad s>=0 throughout the small ball. It would not be enough to choose an arbitrary smooth order satisfying only nonnegative W.grad s.

## Maximal-domain passage

For h in D_g, the bulk conjugated equation has both v and P_g v in H^s. Put w=Av. The finite-regularity background identity of topics147-148 is an identity of distributions; all its nontransport terms belong to L2 and have their previously verified quadratic forms on H^s. Adding the perturbation identity gives

 F=(W+B_g).grad w-a_g log<D>w in L2,
 a_g=(W+B_g).grad s>=0.

Here a_g is uniformly C_b^(1,alpha), alpha=1/40, on the small ball. A Fourier mollifier J_n commutes with log<D>. The Lipschitz Friedrichs commutator [J_n,(W+B_g).grad]w tends to zero in L2. Also [J_n,a_g] maps H^-1 to L2 uniformly: represent an H^-1 distribution as f_0+div F_0 with L2 components, integrate the commutator kernel by parts and use |a_g(X)-a_g(Y)|<=C|X-Y|. It tends to zero first on smooth inputs and then on all of H^-1 by this uniform bound. Since log<D>w lies in H^-1, the logarithmic commutator tends to zero as well.

Apply the C^(1,alpha) positive logarithmic-form bound of proof 153 to J_n w and discard its nonnegative part before taking the limit. Its negative remainder is bounded by C||w||H^(-alpha/64)^2, hence by C||v||H^(s-epsilon)^2. This proves the bulk inequality on the exact maximal domain. The cofactor has constant order; it has no variable-order logarithm. Its coefficients must first be extended from a larger vertical sector, where proof 155 supplies H^sigma regularity. This does not assume global H^sigma regularity of B_g.

## The penalty with a lower-order source

The fixed-field comparison in proof 146 is a distributional comparison between W.RAv and the order-(s-1) reduction of W.grad v. It only needs the latter source in H^(s-1), not in H^s. The equation for h in D_g gives that source as the sum of f/b, the fixed bounded coupling and scalar terms, and -(B_g.grad v+beta B_(g,r)v).

Proof 161 at r=s-1 bounds the added source by C||g||G_s||v||H^s. The cofactor source has the same bound at sigma-1, using the localized divided coefficient; the angular cutoff term at that order is controlled by the lower norm. Thus the proof of proof 146 reruns directly and gives

 ||W.Rw||+||W.Rz||<=C_5||f||X_s+(a+C||g||G_s)||h||X_s+C_a||h||X_(s-epsilon)

for every a>0. The constants multiplying the high perturbation norm can be fixed independently of a. The lower-norm constant need not remain bounded as a decreases. This is a legitimate rerun with a lower-order source, rather than a use of a domain hypothesis which no longer holds.

The fixed coupling and norm comparisons of topics144-145 are unchanged. Fix the background matrix margin, then N,L_0, then the approximation errors and a, and finally the perturbation radius. The cofactor-to-bulk cutoff forcing remains triangular, with a uniformly bounded coefficient. The same absorption as proof 149 proves the intermediate estimate, with the fixed compact coupling map.

## A sign correction in the auxiliary weighted energy

For the physical h, put omega=b^(-2)cos(theta)^(-8) and N_0(h)^2=int |h|^2 omega. For a physical perturbation B.grad+m, integration by parts gives exactly

 -Re <(B.grad+m)h,h>_(N_0)
 =int [div B/2+B.grad(log omega)/2-Re m]|h|^2 omega.

Consequently the change for T_g-T_0=B_g.grad, with no physical zeroth-order term, is

 delta kappa=div B_g/2-beta B_(g,r)+4 B_(g,theta)tan(theta).             (2)

The sign written in Corollary(i) of the theory author's work/Hs_pert.md at the reviewed snapshot, namely -div B/2-B.grad(log omega)/2+d, is its negative. That literal identity is false. For example, on an outer constant-weight-slope region take B=(b_0,0), beta=-1/2 and a compactly supported h. Direct radial integration gives delta kappa=b_0/2, whereas the negative formula gives -b_0/2. If a conjugated scalar d_v=beta B_r is used, it must be combined with the conjugated measure, not inserted again into the physical formula.

This error does not invalidate the intended small-perturbation inequality. The absolute value of (2) is bounded by C||g||G_s using the divided angular estimate of proof 155. The fixed positive end margin therefore survives after decreasing the radius. To pass to D_g, the double-Hardy formula places h/(b cos^4) in H1 using three cofactor derivatives. Ordinary L2 integration by parts then proves the identity directly; no unproved common graph core or high semigroup is needed. The radial cutoff commutator is bounded by a fixed constant times a compactly supported N_0 norm, since q+B_r is uniformly bounded. This supplies one fixed compact map for the whole ball and proves (1).

## Generation, index and inverse conclusion

The theory author's dyadic H2 argument has the correct sign: for the forward equation partial_tau h=T_g h, the total nonnegative order logarithm contributes a nonpositive energy term. Smooth approximation must preserve the canonical coefficient form and the robust sign, for example by approximating g in G_s as in proof 155 and choosing the radius with a factor of two margin. A random coefficient smoothing is not a substitute for checking that sign.

Proof 159 supplies the full construction: smooth-data flows, a uniform positive Hilbert energy, a weak limit identified by the limiting flow, and strong continuity from weak convergence plus convergence of the energy norm. It identifies the generator domain with D_g by the flow integral identity. This avoids treating formal dissipativity alone as a surjectivity proof.

For completeness the radius choices for spectral continuation can be ordered as follows. First obtain the uniform semigroup bound on a preliminary small ball. Choose a large real Lambda_0 so that S_g-Lambda_0 is invertible throughout that ball. Apply (1) on [0,Lambda_0] and decrease the radius if necessary. For each fixed g, D_g is fixed along this spectral path. Peetre's lemma and upper semi-Fredholm index continuation from Lambda_0 give index zero on that interval; above Lambda_0 the resolvent already exists. No continuity of the domains in g is asserted.

If S_0 is injective, a failed uniform lower bound would give g_n->0 and h_n in D_(g_n), ||h_n||=1, with S_(g_n)h_n->0. Weak compactness and the fixed compact map in (1) yield a nonzero weak limit h. The perturbation terms tend to zero in local distributions, so S_0h=0 and T_0h=-C_Rh in X_s. Thus h belongs to D_0, contradicting injectivity. Index zero then gives surjectivity and the uniform graph-norm inverse. Base injectivity remains unproved.

## Scope

The corrected statements are confirmed for the fixed-coupling remainder family. The literal sign identity above is refuted. The full scalar-axis block, moving-tail coefficient family, actual base injectivity and quantitative constants are not proved by this audit. Dependencies are topics144-155,158-159 and161, with the exact spaces and coefficient map specified above.
