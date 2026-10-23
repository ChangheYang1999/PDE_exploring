# Remote density perturbations change dynamic center jets while preserving all density jets and the strain

Written 2026-10-21. Verifier result 152. This is an exact nonlocality statement and a manufactured inverse test. It is not a stability or nonexistence theorem.

## 1. Statement

Fix an even integer m>=4 and radii 0<R_1<R_2. Let f be any real C^infinity function compactly supported in (R_1,R_2), and set

    h(r,theta)=f(r) sin((m+1)theta),
    I=int_(R_1)^(R_2) f(t)t^(-m) dt,
    J=int_(R_1)^(R_2) f(t)t^(m+2) dt.

Extended by zero near the origin and outside the annulus, h is a smooth compactly supported density with even-x/odd-y parity. Its canonical stream is exactly

    psi_h=(I/2) r^m sin(m theta)                    for r<R_1,
    psi_h=-(J/2) r^(-m-2) sin((m+2)theta)          for r>R_2.       (1)

In particular every density derivative of h vanishes at the origin, and (psi_h)_xy(0)=0, while the stream has an arbitrary prescribed homogeneous term of degree m whenever I can vary. Every real I is attainable by scaling a fixed nonzero bump with positive I.

Let rho_0 be any smooth admissible density with a=(rho_0)_y(0)!=0 and canonical strain c. Consider fixed-target dynamic rescaling, c_w=c/(1-C), c_x=C c_w, with C>1 and c<0, and its vector field

    V(rho)=c_w[rho]rho-(c_x[rho]X+U[rho]).grad rho.

The perturbed density rho_epsilon=rho_0+epsilon h has exactly the same density jets of every order at the origin, the same canonical c, and therefore the same rates c_w,c_x. On the entire disc r<R_1,

    V(rho_epsilon)-V(rho_0)=-epsilon U[h].grad rho_0.              (2)

The homogeneous term of degree m-1 in this difference is

    -epsilon a m I/2 Im((x+i y)^(m-1)).                           (3)

It is the first nonzero term if epsilon a I!=0. For m=4, the cubic derivatives are therefore

    delta b_tau=-6 epsilon a I,
    delta e_tau= 2 epsilon a I.                                  (4)

Here b,e are coefficients of x^2 y,y^3, not derivatives. They can be changed by an arbitrarily large amount along the direction (-3,1) without changing any initial local density data or the strain. If rho_0 also has a nonzero far-field axis coefficient K, h preserves K. Thus it also preserves the canonical scale (K/a)^(C/(C-1)) when that positive quantity is defined. A nonzero compact perturbation of this kind is not a genuine residual dilation of rho_0: the dilation changes K to lambda^(1-1/C)K, so preserving nonzero K forces lambda=1.

No bound uniform in a fixed global weighted norm is asserted. Taking a perturbation farther away while preserving I may require a larger global norm. The statement concerns the failure of local density jets alone to determine the nonlocal dynamic jet evolution.

## 2. Canonical inverse calculation

For a density f(r)sin(n theta), Cartesian differentiation gives just two source modes:

    partial_x h = g_(n-1)(r)sin((n-1)theta)
                   +g_(n+1)(r)sin((n+1)theta),
    g_(n-1)=(f'+n f/r)/2,
    g_(n+1)=(f'-n f/r)/2.                              (5)

Take n=m+1. The canonical stream of an odd-odd compact source g_k(r)sin(k theta), k positive even, has radial factor

    P_k(r)=(1/(2k))[r^(-k)int_0^r t^(k+1)g_k(t)dt
                        +r^k int_r^infinity t^(1-k)g_k(t)dt].    (6)

It is smooth at zero, decays at infinity, solves -Delta psi=h_x and has the required parities. Thus its velocity is the canonical one. Formula (6) follows from the two radial homogeneous solutions r^k,r^-k and their Wronskian; it can also be differentiated directly to obtain the source. All integrals here have compact support away from zero, so there is no conditionally convergent strain integral.

For r<R_1, only the second integral in (6) is present. Integration by parts with no boundary terms gives

    int t^(1-m)g_m(t)dt
       =[(m-1)+(m+1)]/2 int t^(-m)f(t)dt = m I,

    int t^(-m-1)g_(m+2)(t)dt
       =[(m+1)-(m+1)]/2 int t^(-m-2)f(t)dt = 0.

Thus the interior stream is exactly the first expression in (1), with no frequency m+2. For r>R_2 only the first integral in (6) remains, and

    int t^(m+1)g_m(t)dt=0,
    int t^(m+3)g_(m+2)(t)dt=-(m+2)J.

This proves the second expression in (1), with no exterior frequency m. These identities account for both source modes, not just a selected projection.

Because m>=4, the interior stream has zero second derivative at zero, so c_h=0. The canonical inverse is linear. Therefore c[rho_epsilon]=c[rho_0], and the fixed-target rates are unchanged for every epsilon. On r<R_1 the density h and its derivatives vanish identically. Expanding the definition of V now proves (2) without an omitted quadratic term: h and grad h vanish there, including in U[h].grad h.

## 3. Dynamic jet response

Since r^m sin(m theta)=Im((x+i y)^m), (1) implies

    U_2[h]=partial_x psi_h=(m I/2) Im((x+i y)^(m-1)).

Near the origin grad rho_0=(0,a)+O(r^2), by the density parities. Hence (2) has leading term -epsilon a U_2[h], which is (3); the remaining product is O(r^(m+1)). The leading polynomial is nonzero if epsilon a I!=0. At m=4, Im((x+i y)^3)=3x^2y-y^3, giving (4).

Equivalently, the quartic interior stream is 2I x^3 y-2I x y^3. Substituting delta d=2I, delta f=-2I into b_tau=(c_w-3c_x+c)b-3a d and e_tau=(c_w-3c_x-3c)e-a f gives exactly (4). This supplies a separate Cartesian center check.

Compact support preserves the far-field density coefficient K, the slope a and the density growth class. It preserves c by (1). If K!=0 and the original exponent is 1/C, the ordinary dilation law for K proves the final assertion in Section1. This is not a claim that either perturbed density solves the stationary equation: generally it does not.

## 4. Verification and practical scope

The exact proof above uses arbitrary smooth compact f. A finite algebraic test can take f=t^m phi(t), where phi is a polynomial beta bump on [1,2], normalized by int phi=1 and set to zero outside. Its I is exactly1. Such a test bump is only finitely differentiable at the two endpoints; the test is explicitly a manufactured finite-regularity source, not a smooth primary candidate. All integrations by parts used above require only the stated vanishing boundary values and therefore remain valid for it. Smooth C^infinity bumps give the theorem itself, with the same moment identities.

The independent code performs exact polynomial integration of both source modes, verifies the four moment cancellations, checks the radial Poisson equation inside the annulus by polynomial differentiation and the two Green primitives, and compares the Cartesian homogeneous center response with (3)-(4). Its data belong in verification/EXACT_CHECKS.json. No producer code is needed or executed.

This result makes a useful DR test: perturb a state only on a remote annulus, retain its center density values and strain, and compare the new center time derivative with (4). A numerical method that treats higher center jets as closed local decay equations would miss this response. The result does not prove instability, exclude stabilization by the full nonlocal field, or decide the principal endpoint. In particular an arbitrarily large response under an unrestricted perturbation amplitude is not an instability theorem in a specified function space.
