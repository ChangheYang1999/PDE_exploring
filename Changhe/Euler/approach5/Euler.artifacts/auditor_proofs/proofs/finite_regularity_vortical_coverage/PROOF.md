# Finite-regularity vortical basin coverage

## 1. Exact statement

Let r>=3 be an integer, 0<c<1/2 and omega any finite real number. Let U in C^r(R3;R3), P in C1(R3) solve the rotating profile equation

    (1-c)U+((cI-omega J)y+U).grad U+omega JU+grad P=0,
    div U=0,

where Jy=(-y2,y1,0). Assume U is uniformly sublinear: |U(y)|/|y|->0. Put B=(cI-omega J)y+U, W=curl U, a=1-2c and kappa=1+c.

Choose R2>R1>0, b0>0 and a smooth radial cutoff rho, equal to one on a neighborhood of Q={|y|<=R1}, positive for |y|<R2 and zero for |y|>=R2, such that (cy+U).y>=b0|y|2 for |y|>=R1. Define

    Y=-rho(cy+U),
    L=sup_y ||sym DY(y)||_operator.

If (r-1)a>3L, then almost every point of O={W!=0} lies in the continuous-time basin of one of countably many compactly supported full-flow-ergodic probabilities nu_i for the backward B flow Psi. They satisfy

    nu_i(B!=0,W!=0)=1,
    spectrum(Psi,nu_i)=(a,0,-kappa),
    h_(nu_i)(Psi_1)=a,

and have absolutely continuous one-dimensional full unstable conditional measures. Every basin has positive volume and is contained in O. If U is nonconstant, the family is nonempty. In the actual Euler setting, A207/A223 give disjoint invariant open essential domains D_i with Bas(nu_i) subset D_i subset O, nu_i(D_i)=1 and Leb(D_i minus Bas(nu_i))=0; their union covers O modulo a null set. They are invariant under both complete flows B and W.

The support of a measure may meet either zero set. No nonsingular uniformly hyperbolic support, velocity decay, helicity sign or nonexistence is concluded. The quantitative inequality is an additional hypothesis depending on U on a bounded region.

## 2. Cutoff with a skew rotational term

Let X=omega Jy+Y. It equals -B near Q and is globally at most linear. All derivatives through order r are bounded, and local uniqueness plus linear growth gives its complete C^r flow Theta. For a tangent vector v_t along this flow,

    d|v_t|2/dt=2 v_t.sym DY(Theta_t y)v_t.

The skew term has zero quadratic form. Gronwall, applied in either time direction, gives

    ||DTheta_t||infinity<=exp(L|t|).

At fixed finite times, the usual differentiated variational equations give bounded derivatives through order r. Thus f=Theta_1 has all the finite derivative bounds used by A305. We never need a bounded zeroth-order map, and none is asserted: outside a compact set the map is a rigid rotation.

Q is strictly forward trapping, and Theta agrees with Psi on all forward orbits from Q, including derivatives. Every original Psi orbit enters Q in finite time by the radial inequality. Its compact maximal core is K=intersection_(t>=0)Psi_t Q. The bracket and divergence equations are used only along original carrier orbits, where they hold exactly. No assertion of constant divergence in the cutoff transition is needed. Also L>=c because the symmetric derivative has trace -3c inside Q.

## 3. Full positive exponent on almost every vortical point

Let F=B cross W. Since div B=3c, div W=0 and [B,W]=-kappa W,

    curl F=(kappa-3c)W=aW.

For a C1 scalar function, its derivative vanishes almost everywhere on its zero set. At a density-one zero, a nonzero differential would force nearby zeros into an arbitrarily thin cone about its kernel, contradicting density one. Apply this fact to each component of F. It follows that Leb({F=0,W!=0})=0.

Exact transport gives

    D Psi_t B=B composed Psi_t,
    D Psi_t W=exp(-kappa t)W composed Psi_t,
    det D Psi_t=exp(-3ct).

The identity (Lv) cross (Lw)=det(L)L^(-T)(v cross w) then gives

    (D Psi_t(x))^T F(Psi_t x)=exp(a t)F(x).

On a compact backward orbit F is bounded. Therefore every point with F!=0 has ||D Psi_t(x)||>=C_x exp(a t). This is the full exponent a, not the determinant-only half exponent used for the abstract A308 theorem without div W.

For any positive-volume target G subset O intersect int Q, remove its null F=0 part. Since ||Df^N||<=sqrt3 max_j|Df^N e_j|, one fixed coordinate direction has upper exponent at least a on a positive-volume subset. Restrict to a box compactly inside O intersect int Q and use Fubini on its parallel coordinate lines. We obtain a straight original arc with a positive-length target where the tangent upper exponent is at least a. If any such target exists, the strain bound implies a<=L.

## 4. The parameter order at fixed r

Put eta=3L/(r-1)<a. Choose eta<chi<chi'<a. Let g=f^p, with p large. Its A305 quantity M_g=max(2,||Dg||,||Dg^-1||) is at most exp(pL) once exp(pL)>=2. The small-child count A_g may therefore be chosen with

    log A_g<=log C_r+p eta.

Here C_r is independent of p; the higher derivatives of g affect only the scale epsilon chosen later. Use A306's finite-time estimate directly, with

    h=p chi+2, alpha=p chi'-1, L_word=pL,
    q=2ceil(pL)+3,
    theta0=(chi'-chi)/(2L), beta=theta0/2.

For sufficiently large p, 1<h<alpha<=L_word and (alpha-h)/(L_word-h)>=theta0. Furthermore h-log A_g grows at least p(chi-eta)+2-log C_r. Its product with theta0-beta eventually exceeds log(32q)+1. The bad set in A306 is then at most 2exp(-n).

Fix this p before choosing epsilon to control the C^r jets of g. Choose a small straight subarc retaining positive target length and build the entire A305 tree. All this precedes the later density subset E. Bounded derivative and inverse bounds for the remainders f^j, j<p, show that the original tangent limsup remains at least a on multiples of p. Each target point consequently belongs to infinitely many expansion sets with J_(g^n)>=exp(np chi'). Positive target measure and Borel-Cantelli imply that infinitely many of these sets have normalized length at least 1/n2. Removing the exponentially small bad set leaves mass at least 1/(2n2) and at least beta n large hyperbolic times.

The selection argument uses only positive measure and the pointwise limsup, so it remains valid after Egorov and inner regularity choose a compact positive-length E on which the original target density in all shrinking parents converges uniformly to one. No parameter depends on that later density scale.

## 5. No higher regularity is used later

A307's proof now applies at this fixed r. The only C-infinity use in its initial statement was selection of a sufficiently large r. We supplied its finite-time substitute in Section4. All its remaining bounds use derivatives through this one r.

In particular, at window M, each selected original parent contains a good descendant within M steps, so its image length is at least epsilon/(2max(1,||Dg||^M)). The curve class has a compact closure in C^(r-1), hence in C1, with a positive lower speed. The relative-entropy argument A257 needs only the lower original mass 1/(2n2), the whole-parent selection, distortion below two and descendant diameters at most 2epsilon100^-N. Its choice N=floor(sqrt n) is unchanged. It gives joint incoming arclength absolute continuity separately for every fixed M.

The exact witness shift from window M at time ell to window M+1 at time ell-1 gives invariant mass in the bounded increasing limit. Early levels contribute at most a fixed level divided by n, so almost every limiting curve retains original approximants with depth(P_j)=ell_j->infinity and original target fraction tending to one. The inverse-iterate C1 derivative and diameter estimates pass at each fixed iterate and then simultaneously over countably many iterates.

The A308 capture deduction uses C2 carrier regularity, C1 transported field regularity, C^(1+alpha) incoming arcs, Oseledets-Pesin theory and the entropy formula. Here r>=3 gives all these inputs, with incoming C^(r-1,1) arcs. Arclength removes equilibrium atoms. A201's stable-zero plaque and A299's original-strip intersection remove irrotational components. Full-flow averaging, exact W contraction and recurrence give the spectrum. A local box along incoming curve, carrier and W gives positive-volume generic sets. A299 captures a fixed basin fraction in the original parents; their density property forces every prescribed positive-volume vortical target to meet one basin. The disjoint positive-volume Borel basins are countable and the complement argument proves coverage. These are exactly the checked A308 steps, without a new smoothness assumption.

The actual Euler A207 positive-density and A223 essential-domain results need no additional derivatives here. Completeness of the vortex flow follows from uniform sublinearity as in A048. All claimed conclusions therefore follow at this finite r.

## 6. Necessary size and scope of the sufficient criterion

If U is nonconstant and uniformly sublinear, W is nonzero somewhere. Otherwise U is entire harmonic with uniformly sublinear growth and hence constant. Move a vortical point into Q. The inverse derivative bound gives |D Psi_t W(x)|>=exp(-Lt)|W(x)|, whereas exact transport and bounded W on Q give |D Psi_t W(x)|<=M exp(-kappa t). Letting t grow forces L>=kappa.

Thus any nonconstant profile satisfying this sufficient condition must have

    r-1>3(1+c)/(1-2c).

This is a limitation of this criterion, not a regularity obstruction for arbitrary profiles. It does not approach a C2 theorem. No explicit omega term appears in L, but Y and its strain still depend on the actual unknown profile. There is no uniform bound on L for a family U_omega without further information.

For a C-infinity profile, fix rho and L and then choose r sufficiently large. This recovers the smooth coverage result. No pressure estimate or helicity sign is used. The main conjecture remains open.

## 7. Verification

This is an independent reconstruction of LIT68. It uses A027, A305, the finite-time part of A306, the proof of A307, and the low-regularity deduction in A308. All parameter, compactness, parent-provenance and flow-completeness conditions have been checked. The exact input snapshot and hash are retained. No numerical computation or formal build was needed.
