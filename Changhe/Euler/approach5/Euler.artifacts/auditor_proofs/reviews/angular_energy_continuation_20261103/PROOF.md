# Angular energy across an arbitrary irrotational boundary

Status: CONFIRMED in A639 after complete independent reconstruction and postread. The enlarged parameter range concerns a standalone punctured homogeneous-field theorem. It retains an axisymmetric scalar with the exact transport and rank assumptions.

## 1. Statement and notation

Let D=R3 minus {0},0<c<1/2, omega in R, Jx=(-x2,x1,0), A=cI-omega J, a=1-2c, p=(1-c)/c, d=p-1=a/c and t=omega/c. Assume

    d(d-1)<2+t^2,
    equivalently omega^2>(1-c)(1-4c).                         (1)

Let V in C1(D;R3) be divergence free and satisfy

    V(exp(sA)x)=exp(-(1-c)s)exp(-omega sJ)V(x).

Set W=curl V and k=(Ax).V. Let sigma in C1(D;R) be axisymmetric and satisfy sigma(exp(sA)x)=exp(-nu s)sigma(x), where nu>0. Put gamma=a/nu>0, w=|sigma|^gamma, and assume

    1/w in L1_loc(D),
    W.grad sigma=0 on D,
    grad k cross grad sigma=0 on {W!=0}.                      (2)

Then V is axisymmetric. Thus the conclusion holds for all omega if1/4<c<1/2, and for omega!=0 at c=1/4. No pressure or helicity assumption is required for this standalone statement. The reciprocal is infinity at a zero of sigma, so (2) makes those zeros a null set. Neither A2 nor gamma<1 is required.

## 2. An elementary angular continuation lemma

On S2 let Z=Jx.grad be the rotation derivative. Let O be any open subset and let F be continuous on S2, zero on its complement and smooth on O. Suppose there

    (Delta_S+t^2 Z^2+bZ+q)F=0,                               (3)

where b,q are real constants. Suppose F has zero mean on every circle of constant polar angle. If q<2+t^2, then F=0.

For epsilon>0, v=(F-epsilon)_+ has compact support in O because F0 on its complement. It is globally Lipschitz: choose a smooth cutoff supported in O and equal to1 near the compact superlevel set {F>=epsilon}; there F is smooth with bounded first derivatives, and elsewhere its positive truncation is0. Thus v is an admissible weak test for the smooth equation on O. If O is the whole sphere, compactness gives the same conclusion directly. Integration by parts yields

    integral(|grad_S v|^2+t^2|Zv|^2)=q integral Fv.           (4)

The drift integral is zero: (ZF)v=Z(v^2)/2 almost everywhere and Z is divergence free for spherical area. No boundary integral is introduced, since the test is compactly supported inside O. The same argument applies to -F.

If q<0, any nonzero positive part of F would give a strictly negative right side of (4) for a sufficiently small epsilon, impossible. Repeating for -F gives F0. If q>=0, the right side is bounded by q integral F_+^2, uniformly in epsilon. Together with the L2 bound this bounds v in H1. Weak compactness and dominated strong L2 convergence give F_+ in H1 and

    integral(|grad_S F_+|^2+t^2|ZF_+|^2)<=q integral F_+^2.

The corresponding estimate holds for F_-. The Sobolev truncation chain rule makes the two gradients disjoint almost everywhere. Therefore F in H1 and

    integral(|grad_S F|^2+t^2|ZF|^2)<=q integral F^2.          (5)

The circle means make the global spherical mean0. The spherical harmonic expansion of an H1 function with mean0 gives integral|grad_S F|^2>=2 integral F^2, since the nonconstant eigenvalues are l(l+1)>=2. On almost every polar circle, H1 slicing and the periodic Fourier expansion give integral|ZF|^2>=integral F^2 because the circle mean is0. Integrating with the spherical area element gives this latter inequality on S2. Combining with (5) proves (2+t^2)integral F^2<=q integral F^2, hence F0. This includes q0.

This proof neither assumes a regular boundary nor claims that the extended F solves (3) distributionally across that boundary. Only the compactly supported truncation tests and an energy inequality for its zero extension are used.

## 3. Apply the lemma to the rotational derivative of k

Differentiated homogeneity gives

    grad k=-aV+(Ax) cross W.                                 (6)

Set f=(Jx).grad k. On {W!=0,sigma!=0}, equation(2) and Ax.grad sigma=-nu sigma imply grad k is parallel to grad sigma. Axisymmetry gives f0 there. Inverse integrability makes sigma!=0 dense in every open subset, so continuity gives f0 on {W!=0} and its closure.

On O_D=int_D{W=0}, (6) says V=-grad k/a. Thus k is harmonic distributionally by div V0, and smooth by interior harmonic regularity. Rotation commutes with the Laplacian, so f is smooth and harmonic on O_D. Both O_D and its complement are twisted invariant. Let F=f restricted to S2 and O=O_D intersect S2. If K=k restricted to S2, then F=ZK. K is C1 and periodic, so F has zero circle means. Twisted homogeneity gives

    f(r,theta,phi)=r^-d F(theta,phi+t log r).

Writing the radial part of the Laplacian as r^-2[(r partial_r)^2+r partial_r] shows directly that Delta f equals r^(-d-2) times

    [Delta_S+t^2 Z^2+t(1-2d)Z+d(d-1)]F

at the twisted angle. Thus Section2 applies with b=t(1-2d),q=d(d-1). Condition(1) gives F0 and hence f0 everywhere. Integrating this derivative along the rotation circles proves k is axisymmetric. Multiplying (1) by c^2 gives the stated parameter equivalence because (1-2c)(1-3c)-2c^2=(1-c)(1-4c).

## 4. From scalar symmetry to velocity symmetry

Let R_s=exp(sJ), Vbar(x)=(2pi)^-1 integral_0^(2pi)R_s V(R_s^-1x)ds, Y=V-Vbar and Zeta=curl Y. Covariant averaging preserves divergence, regularity, twisted homogeneity and W.grad sigma=0. Axisymmetry of k gives (Ax).Y=0. Applying (6) to Y and crossing with grad sigma gives the global identities

    (Ax) cross Zeta=aY,
    grad sigma cross Y=(sigma/gamma)Zeta.                    (7)

For epsilon>0 direct differentiation gives

    curl((sigma^2+epsilon^2)^(-gamma/2)Y)
       =epsilon^2(sigma^2+epsilon^2)^(-gamma/2-1)Zeta.         (8)

The field on the left converges to Y/w in L1_loc. The right side tends to0 almost everywhere and is dominated by |Zeta|/w, locally integrable by (2). Thus curl(Y/w)=0 in distributions. The simply connected domain D admits a global potential psi in W1,1_loc with grad psi=Y/w. One can construct the potentials on balls by mollification and the ordinary L1 Poincare inequality, then patch their constant differences; simple connectivity removes the periods. This step uses no weighted Sobolev completion.

Take a nonnegative smooth radial cutoff chi compactly supported away from0 and infinity. Ordinary W1,1 approximation makes chi psi an admissible test against the locally bounded divergence-free Y. It gives

    integral chi |Y|^2/w
       =-integral (chi'(r)/r)psi x.Y
       =-(omega/c)integral (chi'(r)/r)psi(Jx).Y.             (9)

Every original term is integrable since1/w,psi are locally L1 and Y is bounded on the support. On almost every cylindrical circle with radius rho>0 and height x3, w is a finite positive constant and psi is periodic W1,1. Its absolutely continuous representative is bounded there; hence its square has weak derivative2psi partial_phi psi. Equation grad psi=Y/w gives

    integral_0^(2pi)psi(Jx).Y dphi
      =(w/2)integral_0^(2pi)partial_phi(psi^2)dphi=0.

Fubini applies to the original integrable product in (9), and all remaining factors are independent of phi. Its right side vanishes. Positive radial cutoffs cover D, so Y0 almost everywhere and by continuity everywhere. Thus V is axisymmetric, proving Section1 for every gamma>0.

## 5. The uniform endpoint cannot be added

At c=1/4,omega0 take phi=x1/r^3, V=grad phi and sigma=r^(-nu/c) with any nu>0. The potential is harmonic on D, so V is smooth, divergence free and curl free there. It has ordinary degree -3, equal to -p at this c. The radial scalar has the required degree, is positive, and its reciprocal weight is locally integrable away from0. Both transport and vortical rank in(2) are vacuous because W0. Nevertheless V is not axisymmetric. Here k=c x.grad phi=-phi/2, and f restricted to the sphere is a nonzero degree1 harmonic with angular frequency1. It saturates q2=2+t^2 and confirms the necessity of retaining a strict bound for the uniform-in-omega range.

This is a singular punctured-field counterexample at c outside the target interval. It is not a smooth whole-space Euler-profile counterexample. At c1/4 and omega!=0 the condition is strict and the theorem holds.

## 6. Dependencies and scope

The new continuation lemma is proved directly. Standard sphere and circle Fourier expansions supply their explicit energy constants; ordinary local harmonic regularity, weak potentials and H1 truncations have their named hypotheses in the proof. The previously confirmed A622 annular argument is reproduced to check that gamma<1 and nu>a are unused. For actual profiles in the target range this extends no conclusion beyond A623-A624: their scalar degrees already satisfy nu>a. General nonsymmetric S, automatic reciprocal integrability and the all-zero-low-multipole profile class remain open. An arbitrary rank defect is not the derivative Zk and need not satisfy the harmonic equation or the circle-mean condition.

The complete LIT163 source was read and reconstructed without computation. A focused challenge is requested through the existing configured-model agent exchange, with no new client and no presumed reply.
