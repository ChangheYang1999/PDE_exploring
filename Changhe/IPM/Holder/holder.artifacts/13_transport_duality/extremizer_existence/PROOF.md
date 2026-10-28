# Attainment in the homogeneous Holder space

## Statement and conventions

Fix0<alpha<1. Work with real scalar functions on R^2 and the Euclidean Holder seminorm [f]_alpha=sup_(z!=w)|f(z)-f(w)|/|z-w|^alpha, modulo constants. The kernel convention is K_phi(z)=Re(e^(i phi)/(2pi z^2)), T_phi=cos(phi)T_xx+sin(phi)T_xy, and R_1^2=T_xx-I/2. Singular-integral increments and their homogeneous extension are defined in ../../01_setup/PROOF.md.

Let x=(1/2,0), y=-x. For each phase phi, both functionals

    Lambda_phi(f)=T_phi f(x)-T_phi f(y),
    Lambda_phi^D(f)=Lambda_phi(f)-(f(x)-f(y))/2

attain their norms on the homogeneous Holder unit ball. The sharp operator norms C_alpha,D_alpha are maxima, over phases and normalized homogeneous functions, of these functionals in absolute value. Hence there are homogeneous functions with seminorm1 and evaluation pairs at distance1 attaining C_alpha for T_xx and D_alpha for R_1^2. The same conclusion holds for T_xy by rotation.

The maximizing function for either normalized fixed-pair problem may be chosen real and centrally odd, f(-z)=-f(z). This statement does not assert uniqueness, compact support, smoothness, a maximizing phase, or attainment in the compact smooth class. The compact smooth supremum remains equal to the homogeneous norm by the previously proved approximation theorem.

## Compactness of the normalized unit ball

Choose the representative f(0)=0 and let

    B={f:R^2->R : f(0)=0, [f]_alpha<=1}.

For every f in B and every z, |f(z)|<=|z|^alpha. On each closed disk, these functions are uniformly bounded and equicontinuous. Given any sequence in B, the Arzela-Ascoli theorem on disks of integer radius, followed by a diagonal subsequence, gives uniform convergence on every compact subset. The limit satisfies f(0)=0 and |f(z)-f(w)|<=|z-w|^alpha by passing to the limit at each pair. It therefore belongs to B.

The topology of uniform convergence on compact subsets is metrizable, for example by

    d(f,g)=sum_(n>=1)2^(-n) min(1, sup_(|z|<=n)|f(z)-g(z)|).

Thus this sequential compactness proves compactness of B. No global uniform convergence or density in the full Holder seminorm is required.

## Continuity of each singular increment

Use the compact finite signed measures mu_phi and mu_phi^D with cutoffs0<epsilon<1/2 and R>1 in ../PROOF.md. Their supports lie in the closed disk of radius R and their total variations are finite. The maps f -> integral f dmu_phi and f -> integral f dmu_phi^D are consequently continuous on B for local uniform convergence.

The same accepted proof gives the functional errors

    |Lambda_phi(f)-integral f dmu_phi|<=E(alpha;epsilon,R),
    |Lambda_phi^D(f)-integral f dmu_phi^D|<=E(alpha;epsilon,R)

for every f in B, uniformly in phi. The explicit error is

    E=2a2(alpha)epsilon^alpha/alpha
      +(1+2epsilon)^alpha epsilon^2/[2(1-epsilon)^2]
      +2^alpha R^(alpha-1)/[(1-alpha)(1-1/(4R^2))^2],
    a2(alpha)=2^(1+alpha/2)/(pi(alpha+2)).

It tends to zero as epsilon tends to zero and R tends to infinity. Therefore each singular increment is a uniform limit on B of continuous compact-measure functionals, and is continuous on B. This proves continuity across both singular poles and at infinity; merely using pointwise convergence in the principal-value integral would not suffice.

The dependence on phi is also jointly continuous. For fixed cutoffs, the density is linear in cos(phi),sin(phi), the atomic part is fixed, and the kernels have a common integrable bound on their compact support away from the poles. Thus the truncated functionals are jointly continuous on the compact product B times the phase circle. The same uniform E makes the limiting increments jointly continuous on that product.

## Maxima, normalization and central oddness

A continuous real function on a compact space attains its maximum and minimum. Apply this first to a fixed phase and then to the phase circle times B, including an absolute value when taking the norm. The transport/setup theorem identifies the resulting phase maxima with C_alpha and D_alpha. These constants are positive by the already established lower bounds, so a maximizing function for either global norm has seminorm exactly1: otherwise scaling it up would contradict maximality. Rotating its coordinates transfers T_phi to T_xx, and T_phi-I/2 to R_1^2, while preserving the distance of the two evaluation points and the seminorm.

The compact measures are odd under central reflection, and the atomic combination -delta_x/2+delta_y/2 is odd as well. For every f define

    f_odd(z)=[f(z)-f(-z)]/2.

Then [f_odd]_alpha<=[f]_alpha and f_odd(0)=0. Central change of variables gives integral f_odd dmu_phi=integral f dmu_phi and the analogous atomic equality. Passing through the uniform cutoff limit gives the same equality for Lambda_phi and Lambda_phi^D. Thus odd symmetrization preserves a maximizing value and remains in B. Multiplication by -1, if needed, makes the value nonnegative.

For phases with additional coordinate symmetries, averaging or antisymmetrizing by the corresponding reflections gives the analogous fixed-functional symmetry. No such extra symmetry is imposed uniformly on an unknown maximizing phase.

## Dependencies and status

Dependencies are the established setup/rotation/approximation theorem, the finite-transport truncation theorem in ../PROOF.md, and the standard compact Arzela-Ascoli theorem. Every singular-integral limit is justified by the displayed uniform error. This is a qualitative existence theorem in the homogeneous space, not a construction or a numerical sharpness certificate.

Status at creation: OPEN pending independent cross-read.
