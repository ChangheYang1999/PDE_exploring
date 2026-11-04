# Regular local solutions of the coupled tail system

## 1. Exact hypotheses and conclusions

Fix 0<c<1/2 and real omega. Set Jx=e3 cross x, X=(cI-omega J)x, p=(1-c)/c>1, b=2(1-c), a=1-2c, eta=a/b=(p-1)/(2p), q=1/eta and E=|V|². On a flowbox in R3 minus the origin consider smooth positive H and a smooth scalar phi with

    X.phi=0, X.H=-bH, V=H^eta grad phi,
    div V=0, P=E/2-H, -Delta P=tr((DV)^2).       (1)

Put S=-H, k=X.V=0 and W=curl V. This is the coupled local tail system of CO61 in its negative-S branch. It is not the full similarity momentum equation for V. Equation(1) implies the other stated local tail identities, including homogeneity of V, V.W=0, W.grad S=0, X cross W=aV and grad S cross V=qSW.

We confirm the second-order reduction and principal symbol of CO62, and prove for each c and omega the existence of local analytic solutions of(1) at a regular point for which R=E/H is not any function of phi, and also solutions with R>q. These examples have no flat zero. The simple conductivity and stream-function argument in CO62(c) is confirmed in its source's zero-rotation setting, but its extension to arbitrary rotation in the coordinator summary is false as a reduction. The exact rotating equation includes a drift term.

The entire 101-line coordinator note and its 474-line nested derivation were read. The external analytic input is the Cauchy-Kovalevskaya theorem for an analytic system solved for its highest normal derivatives. Theorem18 and Corollary20, with their proofs on printed pages9-11 of Tsogtgerel Gantumur's 2011 McGill notes, were read from the actual retained primary PDF. We use no numerical check as evidence.

## 2. Elimination of third derivatives

Write M=DV, z=grad H and d=div V, and define

    C=(1-eta R)I+(eta/H)V tensor V,
    Q=2|M|²+(eta/H)V.Mz
       -eta(1+eta)(E|z|²-(V.z)²)/H².

The exact identity, including terms off the divergence constraint, is

    C:D²H-Q=Delta H-Delta(E/2)-tr(M²)
                     +V.grad d-(eta/H)(V.z)d.       (2)

Indeed W=(eta/H)z cross V. Expanding curl W and using Delta V=grad d-curl W gives

    Delta V=grad d-(eta/H)z d
       +(eta/H)(V Delta H-D²H V+Mz)
       +(eta/H²)(z(V.z)-V|z|²).

Dot with V in Delta(E/2)=|M|²+V.Delta V. Finally use |W|²=|M|²-tr(M²) and |W|²=eta²(E|z|²-(V.z)²)/H². Rearrangement proves(2). Thus (1) is equivalent to div V=0 and C:D²H=Q together with its displayed definitions and homogeneities. This replacement would not be valid after discarding div V=0.

The expression M=H^eta D²phi+eta H^(eta-1)grad phi tensor z makes this a second-order system in H and phi. Under div V=0, one can also expand its right side as

    2H^(2eta)|D²phi|²+5eta H^(2eta-1)D²phi(grad phi,z)
    +eta(2eta-1)(R/H)|z|²+eta(1+eta)(V.z)²/H².

This agrees term by term with A1466. In particular no unverified third-derivative cancellation is needed for analytic existence.

## 3. Exact orbit coordinates and symbol

Use s=log|x| and x=exp(s)exp(-(omega/c)sJ)n(y), with n on a small sphere patch. Put T=(omega/c)Jn, let gamma be the round metric, and define G=gamma^(-1)+T tensor T. Then

    phi=f(y), H=exp(-2ps)h(y),
    V=exp(-ps)exp(-(omega/c)sJ)v(y),
    v=h^eta(grad_gamma f+(Tf)n),
    R=h^(2eta-1)G(df,df).

The metric is exp(2s) times the block matrix with entries 1+|T|²,-T,gamma. Its inverse has entries 1,T,G and volume density exp(3s)sqrt(det gamma). The vector V in contravariant components has factor exp(-(p+1)s). Computing divergence therefore gives the exact equation

    div_gamma(h^eta G df)+(2-p)h^eta Tf=0.          (3)

For a scalar exp(ell s)u(y), the same metric calculation gives

    Delta(exp(ell s)u)=exp((ell-2)s)
      [div_gamma(G du)+(2ell+1)Tu+ell(ell+1)u].    (4)

Its highest Hessian symbol at a transverse covector xi is zeta tensor zeta, where zeta=xi sharp_gamma+(T.xi)n and |zeta|²=G(xi,xi). Set F=G(xi,xi)>0 and L=G(df,xi). After the elimination(2), the linearized second-order symbol is triangular in the unknowns f,h. Its diagonal is

    h^eta F, (1-eta R)F+eta h^(2eta-1)L².         (5)

The lower-left entry is irrelevant for its determinant, which is the product in(5). Relative to G, the second quadratic form has eigenvalues 1 and 1-eta R, since R=h^(2eta-1)|df|_G². Consequently the system is elliptic in the symbol-invertibility sense iff R<q, degenerate at R=q, and has two distinct real characteristic lines for R>q. This is not a claim of strong ellipticity for a symmetric matrix system. The degeneracy also has a real null line.

At omega=0, T=0, and (1) becomes

    div_gamma(h^eta grad_gamma f)=0,
    [Delta_gamma+2p(2p-1)](h-|w|²/2)
                      =tr((nabla_gamma w)^2)+2p|w|²,
    w=h^eta grad_gamma f.

The last term follows from the tangential/radial blocks of DV, namely nabla_gamma w,-p w,-w transpose,0. This independently checks the untwisted source equation.

## 4. Analytic solutions that violate functional dependence

First set omega=0 and choose analytic geodesic coordinates (x,y) with gamma(0)=I and its first derivatives zero. On y=0 prescribe

    f(x,0)=x, f_y(x,0)=0, h(x,0)=1, h_y(x,0)=1.

The first equation solves for f_yy analytically. Substitute that expression into(2). The coefficient of h_yy at the origin is 1-eta, which is positive. Thus both equations are in analytic normal form for f_yy,h_yy; their right sides depend only on derivatives of total order at most two other than these solved derivatives. Positive h keeps all real powers analytic. The cited Cauchy-Kovalevskaya theorem gives a real analytic solution on a sufficiently small disk. Complex conjugation and uniqueness ensure it is real. Shrinking the disk keeps h>0.

At the origin f_x=1,f_y=f_xy=0,h_y=1. Therefore

    R_y=(2eta-1)=-1/p!=0.

The direction partial_y is tangent to the regular level of f. Thus R cannot equal F(f), for any function F, even without continuity. The implicit function theorem gives a level curve whose tangent derivative of R is the displayed nonzero number.

For arbitrary omega, choose analytic linear coordinates with G(0)=I and the same f data, h(x,0)=1,h_y(x,0)=epsilon. The coefficient of h_yy stays 1-eta. The source's drift in(3) changes lower-order terms but not this noncharacteristic condition or the prescribed f_xy. Now

    R_y(0)=partial_y G^11(0)-epsilon/p.

Choose epsilon=p(partial_y G^11(0)+1) to make it -1. The same analytic existence theorem gives the claimed example for every omega. Reconstructing V,H gives all of(1) and its other tail identities. Since X.H=-bH and X.V=0, grad H cannot be parallel to a nonzero V; hence these regular examples are vortical as well.

Replacing f(x,0) by sqrt(2q)x gives R(0)=2q and the coefficient of h_yy equal to -1, for every omega in the same G-normalized coordinates. This proves the R>q example for arbitrary rotation, extending the source's explicitly written zero-rotation construction. None of these regular examples has a common flat point or proves anything about the behavior of R near one. They are not global tails or exact global profiles.

## 5. Conductivity and frequency at zero rotation

At omega=0, write gamma=exp(2sigma)I in conformal coordinates. Equation(3) is div(h^eta grad f)=0. Let A=h^eta>0. A local stream function psi satisfies psi_x=-A f_y, psi_y=A f_x. For F=f+i psi direct differentiation gives

    F_barz=((1-A)/(1+A)) conjugate(F_z).

The coefficient's distortion is K=max(A,A^(-1)). If h>0 off zero and has infinite-order value flatness there, then for each N, h(y)<=C_N|y|^N on a sufficiently small punctured disk. Hence K>=C_N^(-eta)|y|^(-N eta). Choosing N eta>=2 proves nonintegrability; exp(tK) is also nonintegrable for every t>0. This is a limitation of this precise stream-function representation, not a disproof of continuation or of every other representation.

The frequency formula requires additional finiteness and boundary assumptions. Suppose u=f-constant and A are regular enough off zero for the integrations, D(r)=integral_Br A|Du|² and I(r)=integral_boundaryBr A u² are finite, I(r)>0, and the inner-boundary terms vanish. Then D=integral_boundary A u u_r,

    I'=I/r+2D+integral_boundary A_r u²,
    rD'=2r integral_boundary A u_r²
                       +integral_Br(y.grad A)|Du|².

The first identity is differentiation on circles and the second is the weighted Rellich identity. Substituting into N=rD/I gives

    N'=(2r/I)[integral_boundary A u_r²-D²/I]
       +(1/I)integral_Br(y.grad A)|Du|²
       -(N/I)integral_boundary A_r u².             (6)

Cauchy-Schwarz makes the bracket nonnegative, but the other terms have no sign supplied by these hypotheses. The nested source states the finiteness and inner-boundary assumptions explicitly; they must remain when this calculation is summarized. No coupled monotonicity formula has been established.

## 6. Rotation error in the coordinator summary

The nested source starts its stream-function paragraph with omega=0. CO62(c) drops that restriction while keeping the same pure conductivity equation and exact coefficient. Equation(3) shows the error. For c!=1/3, equivalently p!=2, and omega!=0 the drift (2-p)h^eta Tf is generally nonzero. In an isothermal chart for G^(-1), there is still a smooth drift and a smooth positive geometric factor in the conductivity. One cannot simply set the rotated flux equal to the gradient of a stream function when its divergence is nonzero.

This failure occurs for solutions of the full local system(1), not merely arbitrary test functions. Choose a sphere point with T!=0 and the analytic initial f gradient in Section4 so that Tf!=0 there and R=1. The normal coefficient in the direction perpendicular to df is 1-eta, so the same existence proof applies. Equation(3) then gives div_gamma(h^eta Gdf)!=0 at that point. The omitted drift cannot be discarded in that solution.

At p=2 the displayed drift vanishes, but the exact coefficient in an isothermal chart includes a smooth geometric factor. Its distortion is comparable to h^(-eta) near a flat zero, rather than literally the formula of the zero-rotation coordinates unless that factor is included. Restricting CO62(c) to omega=0 repairs the submitted statement directly. A different rotating first-order formulation may be possible, but was not proved by the submitted stream-function calculation.

## 7. Audit boundary

The exact eliminated equation, symbol and analytic regular examples are CONFIRMED for every c and omega in Section1. The zero-rotation distortion calculation and the frequency identity with its finiteness assumptions are CONFIRMED. The unqualified arbitrary-rotation conductivity statement in CO62(c) is REFUTED. No example above disproves finite logarithmic ratio energy at a common flat point, and no claim that every possible continuation argument must fail is established. The unrestricted coupled continuation problem and the campaign conjecture remain OPEN.
