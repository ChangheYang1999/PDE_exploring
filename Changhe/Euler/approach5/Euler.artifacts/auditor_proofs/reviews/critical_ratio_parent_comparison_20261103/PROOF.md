# A second complete critical-ratio continuation proof

## 1. Scope of the comparison

The existing coordinator parent, configured for model, independently checked a nested the external referee (a second model) argument for A1449. Its actual provider runtime is not independently attested. The nested requested model consultation failed before model invocation; it is not counted as another model review. Both complete source texts have been read. The parent agrees with the critical logarithmic-energy criterion and preserves the open bounded-only case.

Here is a direct reconstruction of its factorization-first route. It provides a valid alternative to the quasiconformal-first route in the team records. The key extra step after multiplication is a near-L2 regularity bootstrap; omitting that step would leave the use of ordinary quasiregular factorization unjustified.

For clarity, in the local consequence Jx=e3 cross x, X=(cI-omega J)x, a=1-2c, b=2-2c and eta=a/b. Smooth V,S on a flowbox about x0!=0 obey div V=0, W=curl V, k=X.V=0, X.grad V=-(1-c)V-omega JV, X.grad S=-bS, grad k=X cross W-aV and W.grad S=0. The scalar is zero on the central orbit, has one strict sign off it and is infinitely flat at x0.

The local Euler consequence is exactly A1449: for every0<c<1/2 and finite omega, a smooth k=0 flat germ with one strict scalar sign off an isolated X-orbit and ratio R=|V|²/|S| between positive constants is excluded if its transverse logarithmic Dirichlet energy is finite. No pressure equation is needed once this additional energy condition is supplied. The proof works with m=1/c>2, not only the campaign interval.

## 2. The complex-gradient equation and its exact constants

The already verified orbit and isothermal reduction gives a transverse scalar v, smooth with Dv!=0 on the punctured disk, with Dv continuous and infinitely flat at the puncture, satisfying

    Delta_m v+Acal.(|Dv|^(m-2)Dv)=0,
    Acal=d+grad log sigma-((m-2)/2)grad log R in L2.

Here sigma is smooth positive and d smooth. The positive bounded ratio and finite logarithmic energy give exactly the L2 assertion after a smooth coordinate change.

Set alpha=(m-2)/2, F=|Dv|^alpha(v_x-i v_y), kappa=(m-2)/(m+2), ell=m/(3m-2). At a point rotate coordinates so Dv=(t,0), t>0, and denote the Hessian entries by A0,B0,C0. Then

    (m-1)A0+C0=-Acal_1 t,
    F_z=t^alpha[(alpha+1)A0-C0-i(alpha+2)B0]/2,
    F_barz=t^alpha[(alpha+1)A0+C0+i alpha B0]/2.

Eliminating C0 and expressing the result in Re F_z and Im F_z gives

    F_barz=-(m-2)/(3m-2) Re F_z
           -i(m-2)/(m+2) Im F_z-ell Acal_1 F.

The coefficients and rotation covariance therefore imply

    |F_barz|<=kappa|F_z|+ell|Acal||F|,
    F_barz=nu F_z+beta F,
    |nu|<=kappa<1, |beta|<=ell|Acal|.

For the measurable split, assign as much of F_barz as possible, up to magnitude kappa|F_z|, to nu F_z in its own direction; divide the remainder by nonzero F. This works on the puncture. Later the zero point is negligible. The exact distortion is K=(1+kappa)/(1-kappa)=m/2.

## 3. Removal of the puncture before multiplication

For a real compact cutoff chi supported away from zero, the Fourier identity ||(chi F)_z||2=||(chi F)_barz||2 gives

    (1-kappa)||chi F_z||2
       <=ell||chi Acal F||2+|||Dchi| F||2.

Use a fixed outer cutoff times a cutoff vanishing on B_epsilon and equal to one outside B_(2epsilon). The inner derivative term is at most a fixed constant times sup_(B_(2epsilon))|F|, which tends to zero. The remaining terms are bounded because F is bounded and Acal is L2. Fatou and the displayed differential inequality give both Wirtinger derivatives in L2 across zero.

To identify the weak derivatives, repeat integration by parts with the same inner cutoff. Its boundary error against a fixed smooth test is O(epsilon sup|F|), and hence tends to zero. Thus F belongs to W1,2 on the full disk, and its first-order equation holds distributionally. This shortcut uses classical regularity off the one puncture and avoids claiming that an arbitrary nonlinear gradient already has this Sobolev regularity.

## 4. Critical integrating factor

Shrink and rescale to the unit disk. Extend nu,beta by zero outside it. For the Beurling transform S and Cauchy transform C, S is an L2 isometry, barpartial Cg=g and partial Cg=Sg. The Neumann series for I-nu S converges on L2. Define

    g=(I-nu S)^(-1)beta, psi=Cg.

Then g is supported in the unit disk, ||g||2<=||beta||2/(1-kappa), psi_barz-nu psi_z=beta and ||Dpsi||2=2||g||2. No boundedness of psi is asserted.

Every finite exponential moment of |psi| on the disk is finite. One can verify this directly: for integers n>=2, Young's convolution inequality with exponent q_n=2n/(n+2) gives ||psi||_n<=4 sqrt(n)||g||2. Expanding exp(t|psi|), the nth term is bounded by (4t||g||2)^n n^(n/2)/n!, a summable series for every fixed t; the first two terms are finite by the L2 bound. These estimates were also checked in the source with its exact kernel norm. Sobolev exponential chain and product rules follow by truncation and Holder, or by the previously read critical product argument in BBC15.

Consequently f=F exp(-psi) belongs locally to W1,s for every1<s<2 and to every finite Lr, and distributionally

    f_barz=nu f_z.

This alone does not yet place f in the standard W1,2 quasiregular class.

## 5. The missing regularity is supplied, not assumed

Choose s<2 sufficiently close to2 that kappa||S||_(Ls to Ls)<1. Such an s exists by interpolation of the L2 isometry with any fixed bounded exponent below2. Explicitly, with Nstar=max(e,||S||_(L^(4/3) to L^(4/3))), theta=min(1/2,log(1/kappa)/(2log Nstar)) and s=4/(2+theta), interpolation gives kappa||S||s<=sqrt(kappa)<1.

For chi smooth compactly supported in the disk let h=chi f and a0=h_barz. Then h_z=Sa0 and

    (I-nu S)a0=f(chi_barz-nu chi_z).

The right side lies in Ls intersect L2 because f has every finite local moment. Its L2 solution under the inverse operator is supported in the unit disk: outside, both nu and the right side vanish. It therefore also lies in Ls. Uniqueness of the Ls inverse identifies it with the original a0. Hence a0 and Sa0 are L2, so h is W1,2. This proves f in W1,2 locally before any quasiregular theorem is invoked.

## 6. Flat mass versus finite holomorphic order

The ordinary quasiregular factorization now gives either a constant f or f=Holo composed with chi0, where Holo is holomorphic and chi0 is K-quasiconformal. After conformally normalizing its simply connected image, take chi0 from the unit disk to itself with chi0(0)=0. Mori's point estimates give

    (|z|/16)^K<=|chi0(z)|<=16|z|^(1/K).

For every N, flatness of F and exponential integrability imply

    integral_(B_r)|f|²<=C_N r^(2N) integral_(B_1)exp(2|psi|).

Continuity of quasiregular f makes f(0)=0. A nonzero constant is also ruled out by this estimate. If f is nonzero, Holo has a finite zero order j>=1, so |Holo(zeta)|>=d|zeta|^j near zero. The lower Mori bound then gives integral_(B_r)|f|²>=d' r^(2Kj+2). Choosing N>Kj+1 contradicts the preceding upper bound as r tends to zero. Therefore f=0 and F=0 locally, contrary to Dv!=0 on the puncture.

This proves the same critical exclusion by a complete alternative route. The quasiconformal-first argument in A1446-A1449 remains independently valid and does not require the bootstrap of Section5.

## 7. Two matrix checks and two scalar diagnostics

The exact pressure-ratio matrix for negative S is

    M_R=((1-eta)R-1)I+eta V tensor V/H,

with eigenvalues R-1 parallel to V and R/b-1 perpendicular, since1-eta=1/b. It is indefinite exactly for1<R<b. The coupled Hessian matrix C=(1-eta R)I+eta V tensor V/H has eigenvalues1 and1-eta R, and on R<=b it is at least2cI. Neither statement controls the derivative terms of the coupled equation.

For r>0, H=exp(-1/r²), R=2+sin(1/r)/2 and E=RH extend smoothly and flatly in H,E across zero, whereas integral|DR|² diverges. Differentiation gives a leading r^(-2)cos(1/r) in DR; in polar measure its squared integral contains integral cos²(t)t dt after t=1/r. This is a scalar diagnostic only, not a solution of the coupled equations.

The bounded ratio R=2+sin(log log(e r0/r))/2 has no limit as r tends to zero, but |Dlog R|<=1/[3r log(e r0/r)]. Its logarithmic energy is at most2pi/9. For any s>2 the derivative s-energy contains a positive factor times integral_1^infinity exp((s-2)t)t^(-s)|cos(log t)|^s dt. On successive intervals where |cos(log t)|>=1/2, the exponential factor overwhelms the polynomial and the integral diverges. Thus it is in W1,2 but in no W1,s with s>2. Again it is only a scalar regularity example.

## 8. What remains open

The parent comparison is confirmed. Its factorization-first proof has the needed regularity repair, its constants are correct, and its critical criterion is strictly weaker than a positive supercritical Sobolev assumption. The actual Guo-Kar Theorem1.2 requires locally Lipschitz drift; none of the L2 steps silently invokes that theorem at weaker regularity. The source's remaining question, whether the coupled pressure equation forces finite logarithmic energy from boundedness alone, is open. No numerical computation or new model client was used. All eight independent sections were postread.
