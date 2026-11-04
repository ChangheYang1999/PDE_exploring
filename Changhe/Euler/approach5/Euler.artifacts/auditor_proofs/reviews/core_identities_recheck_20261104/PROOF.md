# Repeated audit of the core rotating-profile identities

Status: CONFIRMED A2796-A2798 for the precise core claims below; the general Liouville inference remains OPEN A2799. This does not collectively recertify later indexed results in either source file.

## 1. Setting, notation and regularity

Let c and omega be real, let Jx=e3 cross x, A=cI-omega J, X=cy+U and B=Ay+U. Write G=DU with G_ij=partial_j U_i, S=(G+G^T)/2, Omega=curl U, q=|U|^2/2 and h=U.Omega. Define the momentum residual and two Bernoulli functions by

    Res=(1-c)U+G B+omega JU+grad P,
    H=P+q+(Ay).U,
    H0=H-c(1-2c)|y|^2/2.

The first-order residual identities below require U and P of class C1 on an open set. The curl, helicity and enstrophy residual identities are classical for U,P of class C2 and div U=0. For an exact profile with U C2 and P C1, all those identities remain valid: curl grad P=0 distributionally, their remaining terms are continuous, and a continuous distributional identity holds pointwise. In fact the equation itself makes grad P C1 locally, hence P C2 locally.

No statement in Sections2-4 needs decay, a pressure gauge at infinity or a complete flow. Every real c and omega is allowed there. Sections5-6 explicitly add their global hypotheses.

## 2. Bernoulli, covector and vorticity identities

The elementary identity (G-G^T)v=Omega cross v gives

    grad H=grad P+G^T B+(cI+omega J)U,
    Res=(1-2c)U+Omega cross B+grad H
       =(1-2c)X+Omega cross B+grad H0.                 (1)

Dotting these identities with B and Omega gives

    B.grad H=B.Res-(1-2c)U.B,
    B.grad H0=B.Res-(1-2c)X.B,
    Omega.grad H=Omega.Res-(1-2c)h.                  (2)

Thus the prompt's Bernoulli function is H0. Indeed, expanding its displayed expression in X produces P+q+(Ay).U-c(1-2c)|y|^2/2. For omega=0, X=B and B.grad H0=-(1-2c)|B|^2 for a profile. For nonzero omega the exact product is X.B=|X|^2-omega(Jy).U, with no general sign.

For the one-form u=U.dy, direct differentiation gives

    L_B u=(G B+(DB)^T U).dy
         =-(1-2c)u+d(q-P)+Res.dy.                    (3)

Here DB=A+G and A^T=cI+omega J, which cancel the two rotational terms. Taking the exterior derivative and using d u=i_Omega vol yields, when div U=0,

    curl Res=[B,Omega]+(1+c)Omega
             =B.grad Omega-G Omega+omega J Omega+Omega. (4)

To check the coefficient, L_B(i_Omega vol)=i_[B,Omega] vol+(div B)i_Omega vol and div B=3c. Combining this with (3) gives (4), without commuting Cartesian derivatives unjustifiably. It also shows exactly where incompressibility enters. Dotting (4) with Omega gives

    B.grad(|Omega|^2/2)=Omega.S Omega-|Omega|^2+Omega.curl Res. (5)

Finally differentiation of h, substitution of Res and (4), and skew-symmetry of J give

    B.grad h=-(2-c)h-Omega.grad(P-q)
              +Omega.Res+U.curl Res.                 (6)

The two rotation terms cancel because (JU).Omega+U.(JOmega)=0.

## 3. Divergence identities and pressure equation

Assume div U=0. Then div B=3c and the following exact residual formulas hold:

    (1-5c/2)|U|^2+div(qB+PU)=U.Res,                  (7)
    (1-4c)U+omega JU+div(U tensor B+P I)=Res,       (8)
    (2-4c)h+div(hB+(P-q)Omega)
                    =Omega.Res+U.curl Res,           (9)
    (1-3c/2)|Omega|^2+div(B|Omega|^2/2)
                    =Omega.S Omega+Omega.curl Res.  (10)

For (7), dot the original residual with U and use div(PU)=U.grad P. Formula (8) uses div(U tensor B)=G B+3cU. Formulas (9)-(10) follow from (5)-(6) and div Omega=0.

For any constant antisymmetric matrix K set M_K=(Ky).U and [J,K]=JK-KJ. The product rule and (KU).U=0 give

    B.grad M_K=(2c-1)M_K+omega M_[J,K]
                         -(Ky).grad P+(Ky).Res.

Since div(Ky)=0,

    (1-5c)M_K+div(M_K B+P Ky)
                         =omega M_[J,K]+(Ky).Res.    (11)

For K=J the commutator is zero. For K_i v=e_i cross v, [J,K1]=K2 and [J,K2]=-K1; therefore Z=M_K1+i M_K2 obeys the same formula with coefficient 1-5c+i omega on the left. This accounts for the horizontal phase sign.

The virial identity is

    (1-5c)y.U+div(B(y.U)+Py)=|U|^2+3P+y.Res.         (12)

Indeed B.grad(y.U)=(2c-1)y.U+|U|^2-y.grad P+y.Res; the rotation cancels between B.U and -omega y.JU.

For the pressure identity incompressibility need not be imposed in advance. Set d=div U and differentiate the residual to obtain

    div Res=Delta P+tr(G^2)+d+B.grad d.              (13)

The derivative of B supplies c d-omega tr(GJ)+tr(G^2), and div(omega JU)=omega tr(JG), so the traces involving J cancel. The original zeroth-order term contributes (1-c)d, leaving exactly d. For a divergence-free profile, (13) gives -Delta P=tr(G^2), distributionally and classically wherever the second derivatives exist. This equation alone does not fix its harmonic ambiguity; no such normalization is asserted here.

## 4. Finite-ball boundary terms

Now suppose the exact profile is defined on a neighborhood of the closed ball of radius R centered at0. Let n=y/R on its sphere and let p be any real constant. The divergence theorem gives integral U.n=integral Omega.n=0, and B.n=cR+U.n. With E(R)=integral_ball |U|^2,

    (cR/2)E'(R)+(1-5c/2)E(R)
                 =-integral_sphere(q+P-p)U.n.        (14)

No boundary term has been discarded. The constant p may be chosen separately for each R because no derivative of p(R) is taken in (14).

If Gamma_K(R)=integral_ball M_K, then

    cR Gamma_K'+(1-5c)Gamma_K
       +integral_sphere M_K U.n=omega integral_ball M_[J,K]. (15)

The pressure surface term vanishes because (Ky).n=0. For K=J the right side is zero. With I_h(R)=integral_ball h and W(R)=integral_ball |Omega|^2, the remaining identities are

    cR I_h'+(2-4c)I_h
      +integral_sphere[h U.n+(P-p-q)Omega.n]=0,      (16)
    (cR/2)W'+(1-3c/2)W
      +integral_sphere(|Omega|^2/2)U.n
                         =integral_ball Omega.S Omega. (17)

Also integral_ball y.U=integral_sphere (|y|^2/2)U.n=0 for every R. Its derivative is zero. Integrating (12) and using this identity gives

    integral_ball(|U|^2+3(P-p))
                  =R integral_sphere[(U.n)^2+P-p].  (18)

The p terms match because the sphere area times R is three times the ball volume. With bounded U and c>0, the sum of the first and surface terms in (17) is nonnegative for R>=||U||_infinity/c, giving integral_ball Omega.S Omega>=(1-3c/2)W(R). This inequality does not contradict a nonzero profile by itself.

All radial derivatives above exist for R>0 by continuity and polar integration. Neither U in L2 nor vanishing energy or pressure flux at infinity follows from these finite-ball identities. Any limiting argument must establish those claims separately.

## 5. Complete flow and exact transported quantities

Assume henceforth that U is C1 on R3 and uniformly o(|y|) as |y| tends to infinity. Then |B(y)|<=C(1+|y|), so Gronwall's inequality bounds every trajectory on every finite positive or negative time interval. Local existence and uniqueness and extension on bounded sets give a complete C1 flow phi_t. Its derivative solves d(Dphi_t)/dt=DB(phi_t)Dphi_t. Under div U=0, Jacobi's determinant formula gives

    det Dphi_t(a)=exp(3ct).                            (19)

If c>0, choose R0 large enough that B(y).y>=c|y|^2/2 for |y|>=R0. For psi_t=phi_-t, differentiation of |psi_t a|^2 gives at most -c|psi_t a|^2 outside this ball. The ball is forward invariant for psi, and each backward trajectory stays in the ball of radius max(R0,|a|). This boundedness uses the outward estimate and is not a consequence of positive divergence alone.

For a divergence-free exact C2 profile, (4) gives d Omega(phi_t a)/dt=(DB-(1+c)I)Omega(phi_t a). Uniqueness for the linear variational equation proves

    Dphi_t(a)Omega(a)=exp((1+c)t)Omega(phi_t a).         (20)

For a transported compact closed C1 curve, differentiating its circulation and applying (3) gives

    d/dt integral_(phi_t curve) U.dy
                         =(2c-1) integral_(phi_t curve) U.dy. (21)

The integral of d(q-P) is zero on a closed curve. The corresponding transported two-form is phi_t^*(d u)=exp((2c-1)t)d u. These statements are valid on the available time interval even without a complete flow; the global growth hypothesis above is what makes every t admissible here. No decay of derivatives or finite kinetic energy is needed.

## 6. Scope of the repeated comparison

The current Theory Agent A integral/pressure file, Sections0-4, and the current Theory Agent B core file, Sections0-11, were read. The new derivations above match their core pointwise, finite-ball and Cauchy/Kelvin identities. The Theory Agent A source is part of the existing configured model collaboration; the Theory Agent B source is from the configured model agent. Actual provider execution is independently unattested. No new model client or remote computation was used.

This audit does not newly certify the source files' later index entries, sharp tail asymptotics, BMO pressure construction, stagnation-point classifications, invariant-manifold results, or the second-order Riccati identity. It does not claim that global sublinearity may be omitted from statements of flow completeness. In the task's C2 decay class, uniform sublinearity and boundedness do follow from U tending to0, so (19)-(21) apply for every real omega. The identities leave the general sign of the rotating Bernoulli derivative unresolved.

If a separate argument proves Omega=0 for a C2 divergence-free decaying profile, Delta U=grad div U-curl curl U=0. Each bounded entire harmonic component is constant, and decay makes it zero. None of (7), (14), (19) or (21) by itself supplies that separate vanishing-vorticity argument.
