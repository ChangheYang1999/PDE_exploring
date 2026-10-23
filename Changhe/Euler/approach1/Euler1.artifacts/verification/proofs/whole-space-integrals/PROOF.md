# Whole-space pressure and velocity reconstruction

Status: conditional informal identities and a numerical quadrature specification. They do not prove that the available model has a controlled global tail. Dependencies: the fundamental solution G(x)=1/(4 pi |x|) of -Delta in three dimensions, integration by parts, the divergence-curl identity, and Liouville's theorem for bounded harmonic functions. Classical decaying fundamental-solution representations suffice here; no finite-energy hypothesis on U is required.

Assume U is C^3 on R^3, div U=0, and, for some d<-1, its derivatives of order k=0,1,2 obey |grad^k U(y)|<=K(1+|y|)^{d-k}. Write Omega=curl U and f=tr[(grad U)^2]. Then f is continuous and absolutely integrable, since f=O(R^{2d-2}) and 2d-2<-4. Its Newtonian potential P_N=G*f and its first derivative are well defined. Indeed the kernels |x-y|^{-1} and |x-y|^{-2} are locally integrable, the source is bounded near each fixed x, and the tail is integrable. Differentiation under a locally split integral yields

    grad P_N(x) = (1/(4 pi)) integral (y-x) f(y)/|y-x|^3 dy.

It satisfies -Delta P_N=f and tends to zero at infinity. If a C^2 pressure P solves -Delta P=f and P-P_infty tends to zero at infinity, then P-P_infty-P_N is harmonic and tends to zero. It is bounded by compactness on the remaining finite ball, so Liouville's theorem makes it identically zero. Consequently the displayed gradient is the unique pressure gradient in this class. Merely solving the local Poisson equation does not rule out an added harmonic field unless this boundary behavior has been verified.

Because -Delta U=curl Omega, convolution followed by integration by parts gives

    U_N(x) = (1/(4 pi)) integral Omega(y) cross (x-y)/|x-y|^3 dy.

The boundary term at radius R vanishes under the assumed decay: its size is O(R^d). The integral has a locally integrable kernel and an integrable tail. It has the same curl and divergence as U. Equivalently, -Delta(U-U_N)=0. Both fields tend to zero at infinity, so componentwise Liouville gives U=U_N. This establishes the velocity reconstruction under the stated global assumptions.

To remove the integrable singularity for numerical quadrature, substitute y=x+rn. Then dy=r^2 dr dS(n), and the formulas become

    grad P_N(x)=(1/(4 pi)) integral_0^infty integral_{S^2} n f(x+rn) dS(n) dr,
    U_N(x)=(1/(4 pi)) integral_0^infty integral_{S^2} n cross Omega(x+rn) dS(n) dr.

The angular averages of their constant source terms vanish at r=0. Gaussian quadrature in r and mu=cos(theta), combined with trapezoidal azimuthal quadrature, therefore needs no arbitrary singular cutoff. On finite r intervals this is a reproducible numerical approximation. Convergence in angular/radial resolution and outer radius must be checked. Without a proven tail bound, truncation at a large radius remains a numerical diagnostic, not a whole-space certificate.

A sign calibration uses P=exp(-|x|^2), for which f=(6-4|x|^2)exp(-|x|^2). The exact pressure gradient is -2x exp(-|x|^2). A velocity calibration uses U=(-x_2,x_1,0)exp(-|x|^2), whose curl is [2x_1 x_3,2x_2 x_3,2(1-x_1^2-x_2^2)]exp(-|x|^2). These exponentially decaying manufactured functions are quadrature tests only, never proposed Euler profiles.
