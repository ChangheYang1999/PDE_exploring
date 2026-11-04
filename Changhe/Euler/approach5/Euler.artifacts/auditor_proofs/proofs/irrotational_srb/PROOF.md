# Irrotational physical chaos at every nonzero rotation rate

## Exact statement and scope

For every c>0 and every finite real omega different from zero there are real polynomials phi and P on R3 such that Delta phi=0 and U=grad phi solves

    (1-c)U + ((cI-omega J)y+U).grad U + omega J U + grad P = 0.

The backward carrier X=-((cI-omega J)y+U) has a compact nonsingular invariant set supporting a flow-ergodic SRB probability with Lyapunov exponents chi, 0, -3c-chi, where chi>0. Its continuous-time basin has positive three-dimensional volume. Here SRB means positive exponent and absolute continuity of conditional measures along strong unstable manifolds.

U is nonconstant and unbounded. It fails both velocity decay and uniform sublinearity. No global completeness, uniform hyperbolicity, uniqueness, mixing, or full-basin assertion is made. This theorem excludes a universal local ban on irrotational physical chaos. It does not settle any case of the decaying-profile conjecture.

This is an independent reconstruction of LIT50. Two supplements, concerning buffered domains and suspension unstable manifolds, are included below. The external inputs are the published Wang-Young rank-one theorem, Young's stated Pesin physicality and ergodic-component facts, smooth planar Schoenflies and isotopy extension, and compactly supported top-degree de Rham theory. Their exact reading scope is in the team records. These standard or published inputs are not claimed to have been reproved in full.

## 1. A rank-one family

Let K=200*pi, alpha=10K, M=K+1, and let X0=S1 times [-1,1], with circle length 2*pi. Set R(y)=sqrt(K^2+2y) and

    F_a(x,y)=a+R(y)sin x mod 2*pi,
    f_a(x)=a+K sin x mod 2*pi,
    T_a,b(x,y)=(F_a(x,y), b[alpha R(y)sin x+R(y)cos x]).

The annular chart E(x,y)=(R(y)sin x,R(y)cos x) has determinant 1. Two equal outputs imply u-u'=2*pi*m and v-v'=-alpha*2*pi*m. The bound |v-v'|<=2 sqrt(K^2+2)<2*pi*alpha forces m=0. Thus T_a,b is an embedding and det DT_a,b=b>0. For sufficiently small b its image lies in S1 times (-1/4,1/4); it tends jointly in coordinates and a in C3 to F_a#=(F_a,0).

On the whole disk D0={u^2+v^2<=M^2}, use

    T^d_a,b(u,v)=sqrt(K^2+2b(alpha u+v)) (sin(a+u),cos(a+u)).

If b(alpha+1)M<1/4, this is defined on a neighborhood of D0, has determinant b, is injective by alpha*pi>M, and maps D0 strictly inside the annulus E(X0). Also T^d E=E T. A disk embedded inside an annulus causes no topological contradiction: its image is contractible in that annulus, and the associated embedded subannulus need not represent its essential loop.

## 2. Check the one-dimensional hypotheses

The critical points of f_0 are +/-pi/2; their values are zero modulo 2*pi. Zero is a fixed point with derivative K, hence its orbit avoids the critical set. Wang-Young Definition 1.1 holds with

    delta0=4/K, lambda0=log 2, c0=1, M0=1, K0=10.

Outside the critical neighborhoods, |f_0'|>=K sin(4/K)>3. Thus both outside-expansion conditions hold, including segments ending inside a critical neighborhood. The second derivative is nonzero within each critical neighborhood.

For x=xc+epsilon, 0<|epsilon|<4/K<1/150, put L=log(1/|epsilon|)>5. The first image has a real representative q1 satisfying

    K epsilon^2/3 <= |q1|=K(1-cos epsilon) <= K epsilon^2/2 <=8/K.

Let p>=2 be the first integer with |q_(p-1)|>=1/K, taking p=2 if this already holds. Before this exit the signed lift follows q_(j+1)=K sin q_j and grows by factors between K/2 and K. The final q_(p-1) has absolute value at most 1, so every positive iterate j<p stays outside the critical neighborhoods. Upper growth gives

    p >= (2L+log 2)/log K > L/10.

For p>2, minimality gives (K/2)^(p-3)K epsilon^2/3<1/K, hence p<3+2L/log(K/2)<L. The weaker bound p<10L holds also for p=2.

For 1<=j<=p-2, q_j cot q_j>=1-q_j^2 and sum q_j^2<2/K^2. The product of these ratios exceeds .99. Since |f_0'(x)|/|q1|=cot(|epsilon|/2)>=1/|epsilon|, telescoping gives

    |(f_0^(p-1))'(x)| >= .99 |q_(p-1)|/|epsilon|.

The next derivative is at least K cos 1>K/2. Therefore |(f_0^p)'(x)|>.49/|epsilon|. The bound on p gives

    2^(p/3)<2 |epsilon|^(-theta),
    theta=2 log 2/(3 log(K/2))<1/2.

Since |epsilon|<1/150, .4/|epsilon|>2 |epsilon|^(-theta). This proves the binding expansion. The binding statement is necessarily read for noncritical x and positive iterates j<p; the printed shorthand cannot literally include a critical initial point or j=0.

The critical points remain fixed as a varies. Their critical-value derivatives are 1. The continuation q(a) of the postcritical fixed point satisfies q=a+K sin q, so q'(0)=1/(1-K). Their difference K/(K-1) is nonzero. Finally partial_y F_0(xc,0)=+/-1/K. These are exactly the three standing hypotheses on printed page 353.

Consequently there is a fixed positive C3 tolerance such that every sufficiently close family of embeddings has an SRB measure for a positive-measure set of parameters a. The closeness includes parameter derivatives. No unmentioned Jacobian-comparability condition is added to the cited main theorem.

## 3. Any prescribed contraction per turn

For omega>0 put delta=3c/omega, b0=exp(-2*pi*delta), sigma=sqrt(b0). Choose a finite integer n>=2 so that b=b0^n is small enough for Section 1 and the rank-one tolerance. Let S_i z=sigma^i z+p_i, with p0=0. Choose pairwise disjoint buffered disks D_i=S_i D0, putting all i>0 outside radius 4M. Prescribe

    P_a(S_i z)=S_(i+1)z       for i<n-1,
    P_a(S_(n-1)z)=T^d_a,b(z).

Every piece has determinant b0, their images are disjoint, and P_a^n=T^d_a,b on D0.

Here is the area-preserving extension argument. Given finitely many such area-preserving disk germs with disjoint images, smooth Schoenflies and isotopy extension supply an orientation-preserving plane diffeomorphism G agreeing with them on slightly larger disks and with the identity far away. Write eta=G*(du wedge dv)-du wedge dv. It vanishes near those disks and has compact support and integral zero. The disk complement is connected. The compactly supported top-degree de Rham criterion there supplies beta of compact support with d beta=eta. The positive area forms omega_t=du wedge dv+t eta and the field defined by i_(V_t)omega_t=-beta give a flow h_t stationary near the disks. Differentiating h_t*omega_t yields zero. Thus G composed with h_1 is the required area-preserving extension, still agreeing on the original neighborhoods.

Apply this to sigma^(-1)P_0, obtaining A_0. Let R_a be a Hamiltonian cutoff clockwise rotation by a near D0, supported within radius 3M. Then

    A_a=sigma^(-1) R_a sigma A_0

is a smooth area-preserving family and sigma A_a agrees with P_a near all D_i. The clockwise sign follows directly from (sin(a+u),cos(a+u)). This gives parameter dependence without assuming a parameter version of the extension lemma.

## 4. Harmonic-gradient controls

Every smooth area-preserving plane diffeomorphism has a Hamiltonian isotopy on the compact set being tracked. For A_0, first join the identity to DA_0(0) in SL(2,R), then use

    G_t(z)=(A_0(tz)-A_0(0))/t,
    G_0(z)=DA_0(0)z,

then translate by A_0(0). Taylor's integral formula gives smoothness at t=0. The velocity is divergence-free and therefore Hamiltonian on the plane. Cut its Hamiltonian off outside all tracked paths; the desired local isotopy is unchanged. Append the cutoff rotation to obtain a family smooth in a.

These isotopies can be approximated jointly in any prescribed finite C^r norm by degree-at-most-three harmonic-gradient controls. An explicit generating calculation suffices. Let

    a0=(u^2-v^2)/2, b1=uv, d0=u^2v-v^3/3,
    D=diag(2,1/2).

D is the time-log 2 map of grad a0. Direct pushforward gives D_*grad b1=(4v,u/4) and D_*grad d0=(4uv,u^2/8-2v^2). Hence

    (0,u)=16 grad b1/15-4 D_*grad b1/15,
    (v,0)=-grad b1/15+4 D_*grad b1/15,
    (0,u^2)=16 grad d0/15-8 D_*grad d0/15.

Reflected harmonic polynomials give the other quadratic shear; no orientation-reversing flow is required. Linear harmonic polynomials give translations. The available Hamiltonians therefore include u,v,u^2,v^2,u^3,v^3 in the closure under flow products. Their Poisson algebra contains every polynomial: first obtain u^2v and uv^2, then bracket u^m with u^2v to obtain a nonzero multiple of u^(m+1), and similarly for v. Bracketing pure powers gives all mixed monomials.

Approximate the target smooth Hamiltonian spatially by polynomials, retaining the needed derivatives and smooth parameter dependence, and approximate its time dependence by a finite partition. Lie-Trotter products handle sums, and commutator products handle brackets. On each fixed compact set the bracket word has its order-h^2 term and an order-h^3 remainder in the prescribed finite C^r norm. Repeating with h proportional to the inverse square root of the number of repetitions gives convergence. For a coefficient g(a), place g in one vector-field factor, rather than using sqrt(g). Thus parameter derivatives are also controlled. Induction over each finite Lie expression supplies the general polynomial approximation.

For rigor concerning existence of the polynomial flows, stop paths at exit from a larger box containing the target paths and the finitely many conjugating linear paths. Uniform ODE error estimates prevent exit. Differentiating the integral equations gives the same conclusion through the chosen derivative order. Thus only finite-time compact-set flow is used; polynomial completeness is not assumed. Fit the finitely many controls into (0,2*pi), rescaling amplitudes, and use zero controls near its endpoints.

## 5. Restore divergence and lift to an exact Euler profile

Let Q(s,z;a) be the preceding harmonic cubic control. Set

    q0=delta(v^2-u^2)/4,
    q(s,z;a)=q0(z)+exp(-delta*s) Q(s,exp(delta*s/2)z;a).

The equation z'=grad q-(0,delta v) becomes w'=grad Q under z=exp(-delta*s/2)w. Its return is sigma times the controlled approximation to A_a. The coefficients equal those of q0 near both endpoints. Extend periodically and take finite Fejer means. Convergence in time L1, uniformly for the needed parameter derivatives, and differentiated ODE estimates preserve the return approximation. We now have a finite Fourier polynomial q(theta,u,v;a), harmonic of transverse degree at most three.

For a large geometric radius L, write q=sum q_k exp(ik theta), w=(x1^2+x2^2-L^2)/(2L), and E_k=((x1+i x2)/L)^k for k>=0, with its conjugate power for k<0. Put

    F_L=sum E_k q_k(w,0),
    G_L=sum E_k partial_v q_k(w,0),
    Psi_L=sum_(j=0)^3 (-1)^j x3^(2j) Delta_12^j F_L/(2j)!
          +sum_(j=0)^2 (-1)^j x3^(2j+1) Delta_12^j G_L/(2j+1)!.

The identity

    Delta_12(E_k f(w))=E_k[(1+2w/L)f''+2(|k|+1)f'/L]

lowers the radial polynomial degree. Thus Delta_12^4 F_L=Delta_12^3 G_L=0, and the displayed sums telescope to Delta Psi_L=0. Reality follows from the conjugate Fourier coefficients. On r=L+u, x3=v, one has w=u+u^2/(2L) and E_k=(1+u/L)^|k| exp(ik theta). The finite Cauchy-data sums therefore converge jointly in all needed finite derivatives to q.

Define

    phi=-c(x1^2+x2^2)/2+c x3^2-omega Psi_L,
    U=grad phi,
    P=-(1-2c)phi-((cI-omega J)y).grad phi-|grad phi|^2/2.

These are real polynomials and Delta phi=0. The carrier is

    X=omega Jy-3c x3 e3+omega grad Psi_L,
    div X=-3c.

Its angular speed is omega[1+partial_theta Psi_L/r^2], between omega/2 and 3omega/2 for sufficiently large L. Its transverse equation parametrized by theta tends in the required finite C^r norms to grad q-(0,delta v). Thus its actual one-turn return Ptilde_a approximates P_a as closely as needed.

**Buffered-domain supplement.** The unperturbed map sends the boundary of D_i to the boundary of D_(i+1), so arbitrary small perturbations need not map the whole closed D_i into D_(i+1). Define all finite compositions on slightly larger open neighborhoods instead. The tracked annuli S_i E(X0) lie strictly inside D_i, with positive distances from their boundaries and from every other disk. For fixed n choose errors smaller than these finitely many clearances. The annular trajectories then make exactly n turns before returning to D0. The full n-fold composition is still defined on a neighborhood of D0 and maps D0 strictly into E(S1 times (-1/2,1/2)), since the final map has a strict margin. This is all that is needed.

Choose n and b first, then the control and Fourier accuracies, then L. The n-turn annular map is jointly C3-close to F_a# within the Wang-Young tolerance. Its determinant is positive and less than 1, by choosing its C1 error small relative to the fixed b and 1-b.

## 6. SRB, physicality and the variable roof

Wang-Young supplies an SRB measure for some a. The second return-map exponent is negative because the determinant is uniformly below 1 and the first exponent is positive. The smooth disk embedding extends to a diffeomorphism of the sphere, agreeing on a neighborhood of the trapping disk. Its invariant measure is supported on the compact intersection of its nested annular images. Young's no-zero-exponent theorem supplies at most countably many ergodic components, and disintegration retains the SRB property on these components. Choose one. Its stable-saturation construction inside the trapping annulus supplies a positive-area set generic for it.

The physical n-turn roof tau is smooth and obeys

    4*pi*n/(3omega) <= tau <= 4*pi*n/omega.

Suspend the chosen ergodic measure, normalized by its mean roof. Ergodicity for the full flow follows from ergodicity of the return map. Genericity for the return map applied to tau and to each integrated continuous flow observable proves genericity for continuous-time averages. A short flow-box thickening of the positive-area generic set has positive volume.

**Strong-unstable supplement.** A variable roof tilts strong unstable leaves; transporting a section unstable curve without a time correction only describes a transversal in a weak unstable leaf. On a Pesin block, if x and y lie on the same local section unstable curve, define the time correction

    beta(y)=-sum_(j>=1)[tau(f^(-j)y)-tau(f^(-j)x)].

Backward exponential contraction and bounded derivatives of tau give convergence, including the tangential derivative on a smaller plaque. The strong unstable leaf is the resulting time graph. In local section-unstable/time coordinates the suspension measure has density with respect to du dt, conditionally on the remaining transverse coordinate, because the section conditionals are absolutely continuous. The change (u,t) to (u,t+beta(u)) has Jacobian 1. Fubini therefore gives absolute continuity along the strong unstable time graphs. This proves the SRB assertion for the suspension without a constant-roof assumption.

The positive return exponent divided by mean tau is chi>0. X is bounded and bounded away from zero on the compact invariant set, giving the zero flow exponent. Liouville's formula gives total exponent -3c, so the last exponent is -3c-chi. The support has complete trajectories in both directions by compact invariance. The local physical basin has forward-complete trajectories by trapping. No assertion about other trajectories is needed.

## 7. Final equation and scope checks

For A=cI-omega J, grad((Ay).grad phi)=A^T grad phi+D2phi Ay and A^T=cI+omega J. Also D2phi grad phi=grad(|grad phi|^2/2). Substituting the displayed P into the momentum equation cancels the Hessian terms; the remaining scalar coefficient is (1-c)-(1-2c)-c=0 and the rotational terms cancel. Thus the full Euler profile equation holds globally, with curl U=0.

For negative omega conjugate the positive-|omega| construction by an orthogonal reflection S with SJS^(-1)=-J. All measure, basin, and equation assertions are preserved. Constant U would give an affine backward carrier with eigenvalues -c and -c+/-i omega and no positive-entropy compact invariant measure. Therefore U is nonconstant. A nonconstant polynomial vector field is unbounded and is not uniformly sublinear. This completes the claimed theorem with its stated external inputs.
