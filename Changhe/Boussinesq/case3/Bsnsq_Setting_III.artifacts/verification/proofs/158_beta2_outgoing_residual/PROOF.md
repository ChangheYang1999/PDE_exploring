# Outgoing endpoint geometry and a forced vorticity defect at beta = 2

Status: complete informal proof. This is a further check of construction156, not a B2 profile or a nonexistence theorem for the target class.

## 1. Statement, hypotheses, and dependencies

Take the smooth configuration constructed in ../156_beta2_local_pde_realization/PROOF.md. In that notation A>R0+1, F is even, F(x)=a0 x^2 near0, F'>0 on (0,A), F=M>0 for |x|>=A, and all derivatives of F-M vanish at +/-A. The even positive cutoff chi equals1 on [-A,A], is less than1 outside, and chi-1 is flat at the endpoints. The vertical strip parameter B is larger than R0+1+M/4. Write

    a(x)=chi(x)+x chi'(x), v(x)=2x(1-chi(x)),
    p_+=(A,M/4), Y=y-M/4.

Here a is a cutoff expression, not the center coefficient a0; v is a scalar horizontal drift, not the canonical vector velocity. On a sufficiently small right neighborhood of p_+, the compact shear from156 is the constant translation (x,Y)->(x,Y+M/4). Then

    W=(v(x), 2Y(1+a(x))), Theta=M,
    Omega=-2Y a'(x),
    R_Omega=-2Y[v(x)a''(x)+(3+2a(x))a'(x)].             (1)

The endpoint has the outgoing type described in lead report4.7(iv)(b). There exists a nonempty open invariant set O_+ such that every point of O_+ tends to p_+ in backward time, Theta=M throughout O_+, but Omega is not identically zero there. Consequently R_Omega is not identically zero on O_+. Reflection gives the corresponding statement at p_-.

On the open equilibrium arc (x,F(x)/4), set ell=F'(x), h=sqrt(1+ell^2/16),

    tau=(1,ell/4)/h, n=(-ell/4,1)/h, theta'=ell/h.

Here theta' is differentiation of the temperature restricted to the arc with respect to arclength, oriented by increasing x. The full geometric identities are

    Omega=ell,
    DW=(4n+ell tau) tensor n,
    grad Theta=theta'(tau-ell n/4),
    ell[1-theta' tau_y/4]=theta' tau_x.                 (2)

At either endpoint DW=4n tensor n and every derivative of Omega and Theta-M vanishes. In particular, the endpoint flatness and interior identities necessary for a true profile are compatible with an outgoing nonprofile.

Dependency156 supplies the globally smooth fields, their full-plane canonical inverse, the exact compact equilibrium arc, the global transport equation W.gradTheta=0, and global completeness of W=2X+O(1/|X|). This proof derives the additional endpoint and geometric assertions directly. No numerical calculation is a premise.

## 2. Local formulas and the outgoing type

In the original strip of156, Psi_base=2xY chi(x), so W_base=(v,2Y(1+a)) and Omega_base=-2Y a'. For x>A sufficiently close to A, F=M and the shear is a constant translation. Its derivative is the identity, so the pushed-forward W has exactly the same displayed components in x,Y. Subtracting 2X to recover the canonical velocity adds to the translated stream only the affine term -(M/2)x and a constant. Its Laplacian vanishes, proving the vorticity formula in(1).

Since Theta=M locally, Theta_x=0. Differentiate Omega=-2Y a'(x) and apply W.grad+1 to obtain the last line of(1). Because chi(A)=1, chi<1 for x>A, and chi-1 is flat at A, v is positive and flat on the outgoing side, and v(A)=0. Also a(A)=1, so 1+a>0 near A. The normal nullcline is exactly Y=0. The arc has a horizontal tangent at the endpoint because F'(A)=0. Thus the reduced horizontal drift on the nullcline points outwards for x>A. Since156 proved that the complete zero set is precisely the compact arc, these facts give the outgoing type. The left endpoint follows by x-reflection.

## 3. An open backward-attracted set with nonzero vorticity

Choose eta>0, then delta>0 small enough that for A<x<A+delta,

    eta v(x)<B/2,
    v'(x)-2(1+a(x))<-1.

Such a choice is possible because v(A)=v'(A)=0 and a(A)=1. Define the nonempty open wedge

    N={A<x<A+delta, |Y|<eta v(x)}.

Under backward time u=-t, the equations are dx/du=-v(x), dY/du=-2(1+a(x))Y. On N,

    d/du [Y/v(x)]=[v'(x)-2(1+a(x))]Y/v(x).             (3)

Thus N is invariant under all backward times for which its flow is defined. The horizontal coordinate decreases and stays larger than A. Smooth uniqueness prevents reaching the equilibrium boundary in finite time; equivalently v(x)<=C(x-A) near A makes the travel integral infinite. Its limiting value must be A, since v is positive at any larger possible limit. Formula(3) keeps |Y|<=eta v(x), hence Y tends to0. Therefore every point in N has backward limit p_+.

Let phi_t be the complete global flow supplied by156 and put

    O_+= union_{t>=0} phi_t(N).

This set is open and invariant for every real time: a negative shift beyond the displayed forward time sends a point back into N. Every point of O_+ has backward limit p_+. Since Theta is globally transported and continuous, Theta=M throughout O_+.

For x>A near A, the specific cutoff of156 satisfies a(x)<1, while a(A)=1. The mean value theorem then gives points with a'(x) not zero arbitrarily close to A. For one such point choose 0<|Y|<eta v(x). Formula(1) gives Omega not zero at that point of N. If R_Omega vanished on all O_+, then Theta_x=0 there and the vorticity equation would imply

    Omega(phi_{-u}(X))=exp(u)Omega(X), u>=0.

The left side stays bounded and tends to Omega(p_+)=0. This contradicts the chosen nonzero Omega(X). Hence R_Omega cannot vanish identically on O_+.

This statement concerns a specified open invariant subset of the endpoint's backward-limit basin. It does not identify the entire basin with an open set. In this construction the local strong unstable curve x=A is straight, hence analytic. Its presence is consistent with the failure of the vorticity equation and does not evade the further nonanalytic-boundary condition required of actual outgoing profiles in lead4.7(vi).

## 4. Arc identities

On every interior point of the arc,156 gives W=(0,4y-F(x)), Theta=F(x), Omega=F'(x). Thus

    DW=[[0,0],[-ell,4]], grad Theta=(ell,0).

Using h^2=1+ell^2/16 in the definitions of tau,n proves(2) by direct multiplication. For example 4n+ell tau=(0,4h), whose tensor product with n is the displayed DW. Also tau-ell n/4=(h,0), and theta'=ell/h. Finally

    1-theta' tau_y/4=1-ell^2/(16h^2)=1/h^2,

so both sides of the last identity equal ell/h^2. At each endpoint ell and all of its derivatives tend to0, giving DW=diag(0,4)=4n tensor n. Flatness of Omega and Theta-M was proved in156 in full ambient coordinates, not only on the arc.

## 5. Exterior defect and exact scope

The independently derived exterior formula of156, on the ray x=kappa y with kappa>0 small enough, is

    R_Omega=x[12m2/y^3+16m2^2/y^5-2a0 m1^2/y^2].       (4)

Consequently

    lim_{y->infinity}|X|R_Omega
          =-2a0 m1^2 kappa sqrt(1+kappa^2)<0.          (5)

The symbol kappa avoids the center-strain letter c. The vorticity is positive for small positive x in the prescribed polynomial core and negative in this cone, so it changes sign in the right half-plane.

Together156 and this proof show that center compatibility, both equations on a prescribed disk and along the open equilibrium arc, the flat endpoint jets, the canonical inverse and the interior geometric identities are compatible. The constructed configuration fails the vorticity equation on an outgoing set and at infinity. This does not exclude some different smooth flat-endpoint profile and does not decide the prompt's beta=2 branch.

Written UTC 2026-10-21T11:01:48.031860+00:00.
