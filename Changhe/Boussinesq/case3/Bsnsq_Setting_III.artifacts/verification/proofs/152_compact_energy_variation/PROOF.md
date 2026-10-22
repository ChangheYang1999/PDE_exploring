# Compact thermal-preserving deformations change the finite-part energy

Status: CONFIRMED independent argument, written before controls and model review and refined after both. It is a statement about necessary conditions and nonprofiles. It is not a B2 existence or nonexistence result.

## 1. Statement

Fix beta>2 and smooth whole-plane fields Psi,Theta, with Psi odd and Theta even under (x,y)->(-x,y), gradPsi(0)=0 and gradPsi=o(r). Put

    J grad h=(-h_y,h_x), V=J gradPsi, W=beta X+V,
    Omega=-DeltaPsi, f=W.gradOmega+Omega-Theta_x.

Assume the canonical relative full-plane inverse ofOmega exists and equalsV; the symbol hypotheses of150 are one sufficient case. Assume exact thermal transport W.gradTheta=(beta-2)Theta. Suppose the energy disks E_R=int_(|X|<R)(|gradPsi|²/2+yTheta) admit a finite power/log expansion with a constant coefficient E_fp and o(1) remainder. Packet151 supplies this property under its finite-expansion hypotheses.

Let h be a smooth compactly supported odd-in-x function whose support is separated from the material center. Let Phi_epsilon be the complete flow of H=J grad h. Define

    W_epsilon=(Phi_epsilon)_*W,
    Theta_epsilon=Theta o Phi_epsilon^(-1).

Then W_epsilon=beta X+J gradPsi_epsilon for a unique smooth odd stream Psi_epsilon agreeing with Psi outside a fixed compact set. It agrees near the center too. The fields retain the canonical relative inverse, symmetry, center data, all complete exterior fields and exact thermal transport. Their finite-part energies exist and satisfy

    d E_fp(epsilon)/d epsilon at0
       = -int h [W.gradOmega+4beta Omega+Theta_x]
       = -int h [f+(4beta-1)Omega+2Theta_x].             (1)

All integrals in(1) have compact support. These equalities use the stated orientation ofJ.

The three affine moments of the vorticity residual are unchanged whenever they exist: if f is compact, so is f_epsilon, and

    int f_epsilon=int f,
    int x f_epsilon=int x f,
    int y f_epsilon=int y f.                           (2)

No compactness or integrability of the individual velocity or temperature is required.

On a region where the fields are the exact polynomial B2 configuration

    Psi=(1+beta/2)xy-q x³/6, Theta=a x², Omega=q x,
    q=4a/beta, a!=0,

and supp h is contained in that region, formula(1) becomes

    d E_fp(epsilon)/d epsilon at0
             = -4a(5-1/beta) int x h.                 (3)

There are smooth odd h supported in a reflected pair of disks away from the axis and center with int xh>0. Therefore the energy is not locally constant on these compact thermal-preserving deformations. It increases in one parameter direction and decreases in the other. This concerns differences of energies; it does not assert that both absolute signs occur around an arbitrary base value.

## 2. Exact nonlinear deformation and relative gauge

A smooth compactly supportedH has a global flow for each real epsilon: outside a compact set it vanishes, and on that set it is bounded with bounded derivative. The flow preserves area because divH=0. Since h is odd, H has odd first and even second component, so its flow commutes with x reflection. It is the identity near0 and outside a fixed compact set containing suppH.

Area preservation gives divW_epsilon=2beta. One way to verify this without a coordinate formula is to push forward the area form: L_(W_epsilon) dX=(Phi_epsilon)_*(L_W dX)=2beta dX. Equivalently the elementary change of variables in the divergence theorem on arbitrary transported domains gives the same identity.

The derivative of the pushforward, with epsilon as flow time, is

    partial_epsilon W_epsilon=DH W_epsilon-DW_epsilon H.

For every smooth Wtilde with divWtilde=2beta, component differentiation gives

    DH Wtilde-DWtilde H
               =J grad[(Wtilde.grad-2beta)h].          (4)

Define explicitly

    Psi_epsilon=Psi+int_0^epsilon (W_t.grad h-2beta h)dt. (5)

Equations(4)-(5), with the initial value, yield W_epsilon=betaX+J gradPsi_epsilon. Each integrand in(5) is odd and compactly supported in supp h. It vanishes near0. Hence Psi_epsilon-Psi has compact support, zero center gradient and the required relative normalization, with no arbitrary exterior constant or linear stream term. Uniqueness follows because two streams for the same velocity differ by a constant, and odd parity fixes it to0.

Sublinear relative velocity is unchanged on the exterior. The original canonical inverse is assumed to exist. The correction to its vorticity is -Delta chi_epsilon, where chi_epsilon=Psi_epsilon-Psi is smooth and compact. Its full-plane logarithmic potential equals chi_epsilon by the fundamental-solution identity and compact integration by parts, and its Biot-Savart velocity is J gradchi_epsilon. The latter is0 near the center, so center subtraction adds no constant. The canonical operator is the once-subtracted full-plane kernel of150, whose velocity kernel is K(X-Y)-K(-Y). It is linear on a convergent base field plus a compact smooth density and, on the latter, equals the ordinary Biot-Savart velocity minus its value at0. This follows directly by splitting the integral; on any expanding truncation the compact part stabilizes once its support is included. Thus the new canonical relative inverse exists and is precisely J gradPsi_epsilon. Additionally harmonic uniqueness applies: two smooth odd streams with the same Laplacian, sublinear gradients and zero center gradients differ by an entire harmonic function with sublinear gradient, hence a constant, which oddness makes0. This uses no finite-box boundary condition. Sublinear velocity alone is not being claimed to justify convergence of an arbitrary vorticity integral.

Transport commutes with pushforward/pullback:

    W_epsilon.gradTheta_epsilon
        =(W.gradTheta)oPhi_epsilon^(-1)
        =(beta-2)Theta_epsilon.

All center derivatives are fixed since the flow and(5) are unchanged near0. Every sign or value ofTheta is retained under pullback. If supp h is also separated from the axis andOmega is strictly positive on its right-half-plane part, positivity on that support persists for sufficiently small |epsilon| by compact C2 continuity. No claim of positivity away from the support is added; it is exactly whatever the original field has there.

## 3. Finite-part variation

The complete exterior fields are identical. For every disk containing the common compact support, the difference E_R(epsilon)-E_R(0) equals the ordinary finite integral

    int [|gradPsi_epsilon|²/2-|gradPsi|²/2
                    +y(Theta_epsilon-Theta)].         (6)

It is independent ofR. Consequently E_fp(epsilon) exists with the same divergent power/log terms as the original energy, and its difference equals(6). Differentiate under this compact integral. At epsilon0,

    chi=partial_epsilon Psi_epsilon=(W.grad-2beta)h,
    tau=partial_epsilon Theta_epsilon=-H.gradTheta.

Compact integration by parts gives

    dotE=int Omega chi+int y tau,
    int Omega W.gradh=-int h(W.gradOmega+2betaOmega),
    int y tau=int Theta H_2=int Theta h_x=-int hTheta_x.

Substitution proves the first formula(1). From W.gradOmega=f-Omega+Theta_x one obtains its second formula. No divergent individual integral was separated or assigned a finite part in this derivation.

For the polynomial patch, f=0, Omega=qx and Theta_x=2ax. Thus the multiplier in(1) is

    [(4beta-1)q+4a]x=4a(5-1/beta)x,

which proves(3). Choose a nonnegative nonzero smooth bump b in a disk onx>0 inside the polynomial patch. Its reflection is in a disjoint disk onx<0. Set h(x,y)=b(x,y)-b(-x,y). This is odd and int xh=2int_(x>0) xb>0. The derivative is nonzero sincea!=0. Smooth dependence on epsilon makes it keep a fixed sign near0, so the energy varies strictly monotonically on a sufficiently small parameter interval.

## 4. The affine moments and weighted residual-energy identity

The compact changes ofPsi andTheta satisfy all hypotheses of142, which proved using only compact differences that

    int delta f=int y delta f=0,
    int x delta f=int deltaTheta,
    int delta t=-(3beta-2)int deltaTheta.

Here t_epsilon=t=0 and3beta-2!=0. Therefore int deltaTheta=0 and the third affine moment is unchanged as well, proving(2). This conclusion also follows from the area-preserving temperature pullback, but no separate full-plane integral ofTheta is needed.

When f is compact, the exact disk identity151 has the same boundary flux for all epsilon and t=0. Subtracting its two finite-radius versions gives

    int(Psi_epsilon f_epsilon-Psi f)
                  =-(4beta-2)[E_fp(epsilon)-E_fp(0)].  (7)

Every product difference here is compact even if one relaxes the compactness of individualf. Equation(7) shows explicitly how energy variation is balanced by a weighted residual integral. On the polynomial support f=0, differentiating it yields

    int Psi dotf=(4beta-2)4a(5-1/beta)int xh.           (8)

This is compatible with the zero affine moments ofdotf becausePsi is cubic and quadratic, not an affine weight. It is not a solvability assertion for arbitrary dotf.

## 5. Application to zero-impulse compact-residual configurations

Write Z_crit={M/N>2: M,N positive coprime integers,N<=3} and Z_E={M/N>2: M,N positive coprime integers,N<=4}.

Fix a disk D whose polynomial center data are to remain untouched. Apply148 with a larger protected polynomial disk Dprime. Choose the two bump disks of section3 inside Dprime and outside D, separated from the axis. This choice is possible by first making Dprime sufficiently large;126 and148 allow any prescribed finite disk.

For every sufficiently large chosen gluing radius,148 supplies a smooth configuration with global exact thermal transport, canonical relative inverse, nonzero compact f and all three affine moments0. Its exterior satisfies the full symbols and both equations, so150 and151 give a finite-part energy. The deformation above keeps the prescribed fields onD, all complete exterior fields, compactness and vanishing of the affine residual moments, and its nontrivial nonnegative temperature. By(3) its energy is not locally constant. At least one sufficiently small deformed configuration has E_fp!=0; this follows immediately from the nonzero derivative, without locating a zero or crossing both signs. If beta is outside Z_crit, the actual exterior dipoleD is0 by148 via149 and150, and remains0 because the whole exterior stream is identical. In particular outside Z_E the new energy necessary condition E_fp=0 is not a consequence of these other conditions.

These remain nonprofiles: the open annulus used in148 and124 to certify a nonzero residual is outside the deformation support and unchanged. Choose the bumps to avoid the negative-vorticity point retained by148. This is automatic if they lie in its positive polynomial core, since a0>0. That point and a neighborhood of it are unchanged. The deformation can be chosen small so the positive-vorticity polynomial patches stay positive; the full configuration still has signed vorticity. No full positive-vorticity construction with zero impulse is supplied here.

## 6. Dependencies and scope

The exact variation and nonlinear conjugacy use only compact smooth flows, constant divergence and integrations by parts.142 supplies the affine-moment identity, re-stated above.151 supplies the disk boundary identity and one sufficient hypothesis for finite-part energy. The application uses124,126,135,145,146,147,148,149,150 and151 section6 as stated in section5. The radius constants in126,147 and148 may depend on the enlarged prescribed diskDprime, which is chosen first and then held fixed; no uniformity inDprime is needed. The independent gluing, moment sign and symbol arguments and their model-review status are recorded in the corresponding proof packets; this follow-up model review did not re-audit those dependencies. This application is conditional on those precise statements; it is not a fresh review of every earlier proof or a computed PDE solution.

A nonzero derivative proves a local change and one configuration with nonzero energy. It does not prove that any selected energy can be reached, that zero can be reached from a given configuration, that the full vorticity residual can be removed, or that the energy has both signs under the full B2 hypotheses. No endpoint follows.

Written UTC 2026-10-21T09:49:55.071066+00:00.

Independent scope refinement 2026-10-21T09:52:32.326401+00:00: canonical inverse existence is an explicit base assumption, retained by a compact potential correction; positivity persistence requires supports away from the axis. Neither issue changes the tested identities or the intended polynomial-patch application.

Final audit UTC 2026-10-21T09:59:38.274344+00:00: independent exact and finite-deformation controls passed; actual Claude Opus5.5 reviews233 and234 returned written confirmations, with the stated dependency limitation. The canonical operator properties and attribution refinements requested in234 are explicit above.
