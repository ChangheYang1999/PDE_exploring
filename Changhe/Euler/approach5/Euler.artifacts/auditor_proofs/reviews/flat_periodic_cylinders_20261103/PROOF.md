# Flat periodic orbits: invariant cylinders and the limits of a second-jet test

Status: CONFIRMED at the exact scope below by A474, 2026-11-03T04:42:53.296940+00:00. The proof was independently reconstructed and fully postread. No global nonexistence conclusion follows.

## 1. Exact setting and claims

Let U in C2(R3;R3), P in C1 solve full rotating incompressible Euler,0<c<1/2,omega in R, with uniform U=o(|y|) and U.curl U=0 everywhere. Set

    A=cI-omega J, B=Ay+U, W=curl U,
    a=1-2c, kappa=1+c, d=3c,
    H=P+|U|^2/2+(Ay).U, g=U.B, O={W!=0}.

Let Gamma be a nonconstant periodic B orbit of least period T>0, contained in closure(O), with W=DW=0 on Gamma. A470-A471 applied to its time measure give U!=0,g=0,H=h0 on Gamma and a finite constant rho with

    grad H=-aU, Hess H=-aM,
    grad g=rho U, Hess g=rho M+tau U tensor U,
    M=DU=M^T, tr M=0, tau|U|^2=2|M|_F^2.             (1)

Let Phi be the forward carrier flow. Its covector law on Gamma is

    U(Phi_t x)=exp(rho t)D Phi_t(x)^(-T)U(x).         (2)

The following conclusions hold.

(a) If rho<0 or rho>d, Gamma is a hyperbolic saddle periodic orbit, with positive Floquet multipliers1,exp(rho T),exp((d-rho)T). Vorticity vanishes on its local unstable cylinder.

(b) If rho<=-2a, vorticity is tangent to the local stable cylinder. Its nearby H-level curves are closed loops, and every such loop contains a zero of W.

(c) If rho<=-kappa, vorticity vanishes on the entire sufficiently small local stable cylinder as well. This includes the endpoint rho=-kappa. The proof uses flatness DW=0 and C2 carrier regularity. The condition rho<=-kappa also implies the tangency criterion used here, since the unstable rate d-rho>kappa.

Part(c) is stated independently of rho<=-2a: for c below1/5 these two ranges are not nested in the direction relevant to(b). In the campaign range c>2/5, rho<=-kappa is a subrange of rho<=-2a.

The positive-rho analogue of(c) is not asserted. Nor does simultaneous vanishing on the two cylinders contradict Gamma being in closure(O): vortical points can approach from outside both cylinders.

## 2. Floquet multipliers and orientation

Since B is transported by its own derivative, the line R B on Gamma has multiplier1. Equation(2) makes ker U invariant and makes the quotient R3/ker U have multiplier exp(rho T). As U.B=g=0, the flow line lies in ker U. The determinant of D Phi_T is exp(dT), so its induced multiplier on ker U/R B is exp((d-rho)T).

These are the three eigenvalues with algebraic multiplicity. For rho<0 or rho>d they are distinct and positive, one transverse multiplier below1 and one above1. The stable and unstable real line bundles are orientable because their period multipliers are positive. Standard C2 local stable-manifold theory for a hyperbolic periodic orbit therefore supplies two cylinder neighborhoods of Gamma. Their strong stable and unstable directions are one-dimensional.

Since grad H=-aU!=0 on Gamma, the plane ker U is the tangent plane of the regular H level there. For rho<0 the stable direction is transverse to this plane, while the unstable direction lies in it. For rho>d the unstable direction is transverse and the stable direction lies in it. These assertions concern tangent planes on Gamma; invariance of an entire H level outside Gamma is not being assumed.

## 3. Vanishing on the unstable cylinder

Write lambda_u=max(rho,d-rho)>0. Fix q on a sufficiently small local unstable cylinder and put z_t=Phi_-t(q). The orbit segment from z_t to q stays in a fixed small tube for every t>=0, and the hyperbolic estimates give, for any sufficiently small eta>0,

    dist(z_t,Gamma)<=C_q exp(-(lambda_u-eta)t).

The linear variational equation near the periodic orbit also gives

    ||D Phi_t(z_t)||<=C exp((lambda_u+eta)t).

For completeness, this last upper bound follows by choosing a periodic Floquet norm on the orbit and extending it continuously across a small tube. Its logarithmic growth bound is at most lambda_u+eta there after allowing a smaller intermediate margin; equivalence with the Euclidean norm supplies C. A neutral flow direction is included and lambda_u>0 dominates it. No positive lower speed off the tube is needed.

Since W is C1 and vanishes on the compact orbit, |W(z_t)|<=C dist(z_t,Gamma). Cauchy transport gives

    W(q)=exp(-kappa t)D Phi_t(z_t)W(z_t),
    |W(q)|<=C_q exp((2eta-kappa)t).

Choose2eta<kappa and let t increase. This proves W(q)=0. The argument requires only W=0 on Gamma, not DW=0, and it uses only trajectory segments contained in the tube.

## 4. Tangency and zeros on stable H-level loops

The confirmed local geometric theorem A462 says that, for an orientable hyperbolic saddle carrier orbit, the Cauchy eigenfield W is tangent to the local stable cylinder when lambda_u>kappa. It applies here to the positive multipliers of Section2. If rho<=-2a, then

    lambda_u=d-rho>=d+2a=2-c>1+c=kappa.

If rho<=-kappa, lambda_u=d-rho>=d+kappa>kappa as well. Thus W is tangent to the stable cylinder in either range.

For rho<0, the restriction of H to the stable cylinder is a C1 submersion near Gamma: its derivative on the strong stable direction is nonzero all along the compact orbit. Choose an oriented cylinder chart(theta,r), with Gamma given by r=0. The derivative partial_r H has a fixed nonzero sign after a consistent orientation and shrinking the cylinder. The implicit function theorem, compactness of the circle and uniqueness in each radial fibre show that for each sufficiently small ell the set

    Gamma_ell=W^s_loc intersect {H=h0+ell}

is one C1 closed loop close to Gamma. This is only a local annular statement; the cylinder may be shrunk to a tube on which these loops are defined.

Global zero helicity gives WH=-aU.W=0. Together with tangency to the stable cylinder, this makes W tangent to Gamma_ell. If W had no zero on one loop, it would be a nonvanishing continuous C1 vector field on a compact circle, and its flow would traverse that circle in finite positive time. This would be a nonconstant periodic vortex orbit. A014 excludes such orbits for the global C2 uniformly sublinear Euler class. Hence every Gamma_ell has a zero of W. This conclusion does not make the entire loop irrotational.

## 5. Exact stable decay, including the endpoint

Let rho<0. A generic hyperbolic estimate with rho+eta is insufficient at rho=-kappa, so we establish the exact upper bound

    dist(Phi_t q,Gamma)<=C_q exp(rho t), t>=0,       (3)

on a smaller local stable cylinder. Choose a C2 transverse section through Gamma and restrict its C2 return map to its one-dimensional C2 stable curve. In a local coordinate r the map satisfies

    f(0)=0, f'(0)=m=exp(rho T) in(0,1),
    f(r)=m r+O(r^2).

Choose a small interval where |f(r)|<=q0|r| for some q0<1. For r_j=f^j(r0), the sum of |r_j| is finite. For nonzero iterates,

    |r_n|<=m^n |r0| product_(j=0)^(n-1)(1+C|r_j|)
           <=C_r0 m^n.

If an iterate is0 the estimate is immediate thereafter. The return time is T(r)=T+O(|r|), so the nth return time is nT+O(1), because the corrections are summable. Between successive returns, bounded-time C1 flow estimates control distance to Gamma by C|r_n|, while the return times are uniformly bounded above and below. This proves(3). A starting point off the chosen section is treated by one bounded-time flow shift. This derivation uses C2 regularity to obtain the summable quadratic distortion; no equality of asymptotic rates is assumed without proof.

The tangent splitting on the stable cylinder is R B plus the strong stable line. Write

    W(q)=alpha B(q)+v_s.

The splitting is invariant, and D Phi_t(v_s) tends to0 exponentially. Since B is bounded away from zero on a small tube of Gamma, if alpha!=0 then for all sufficiently large t,

    |D Phi_t(q)W(q)|>=C_q |alpha|>0,
    |W(Phi_t q)|>=C'_q |alpha| exp(-kappa t).         (4)

Here the last step is forward Cauchy transport. Because W=DW=0 on compact Gamma, uniform first-order Taylor remainder gives

    |W(y)|=o(dist(y,Gamma))

as y approaches Gamma. Equations(3)-(4) contradict each other whenever rho<=-kappa: multiplying the upper little-o estimate by exp(kappa t) tends to zero, also at equality. Thus alpha=0 at every sufficiently close stable-cylinder point.

For rho<0, the strong stable line remains transverse to the H levels throughout a small stable-cylinder neighborhood, by its transversality on Gamma and continuity of the stable splitting. But W=v_s is tangent to those H levels, by Section4. Hence v_s=0 and W=0 there. This proves(c).

For rho>d, the strong stable direction is tangent to ker dH on Gamma. The last transversality step is unavailable. Even if the same alpha=0 argument applies when d-rho<=-kappa, it only places W in the strong stable line and does not prove W=0. No positive-rho cylinder exclusion is inferred.

## 6. What the second-jet completion actually proves

At a point of Gamma write b=B,u=U, so b,u are nonzero and orthogonal. Flatness W=DW=0 makes the third-order tensor T=D2U fully symmetric. Differentiating div U=0 makes it trace-free in every pair. Let C=T[b]=D_B M be its contraction in the third slot and put

    N=rho M+tau u tensor u-C-2cM-omega[J,M]-2M^2.      (5)

The ambient Hessian formula for g says T[u]=N. Two necessary compatibility conditions are

    tr N=0, N b=C u.                                (6)

The first follows from tau|u|^2=2|M|_F^2 and the trace-free terms. To check the second, the first covector law is equivalently

    M(B+U)=(rho I-A^T)U.

Differentiate along B on Gamma, using constant rho, U'=M B and B'=(A+M)B. This gives

    C(B+U)=(rho I-A^T)M B-M(A+2M)B.

Rearrangement and A^T=cI+omega J yield exactly N b=C u with N as in(5). No third derivative of U is taken: M is C1 and its along-orbit derivative is C.

Conversely, given nonzero orthogonal b,u and symmetric trace-free matrices C,N satisfying N b=C u, there is exactly one fully symmetric trace-free3-tensor T with T[b]=C and T[u]=N. Choose the orthonormal frame e1=b/|b|,e2=u/|u|,e3, and write A1=C/|b|,A2=N/|u|. The compatibility becomes A1 e2=A2 e1. Set T_ij1=(A1)_ij and T_ij2=(A2)_ij and extend by symmetry. The three common components agree by that compatibility. These assignments fix all components except T_333. Tracelessness in the third slot determines

    T_333=-T_113-T_223.

The trace conditions in slots1 and2 are exactly tr A1=tr A2=0, already assumed. This proves existence and uniqueness of the pointwise tensor completion.

This is an algebraic sufficiency statement conditional on the existing first-jet and along-orbit data. It does not produce periodic M(t),B(t),U(t) for arbitrary rho, does not solve all compatibility conditions along a closed curve, and does not construct a local or global Euler germ. Consequently it cannot justify an unrestricted assertion that every possible low-order restriction on rho has been exhausted. The differentiated momentum equation has a symmetric required pressure Hessian at W=DW=0, but that pointwise fact likewise does not solve a periodic extension problem.

## 7. Dependencies and remaining cases

A470-A471 provide the flat covector laws, A462 gives stable-cylinder tangency, A014 excludes nonconstant periodic vortex lines, and ordinary C2 hyperbolic periodic-orbit stable-manifold theory supplies the local cylinders and return map. Their uses are explicit above. Pressure normalization plays no role. The global helicity and sublinearity hypotheses enter through the covector laws and the closed-vortex exclusion; the local Cauchy and distortion arguments have narrower dependencies.

No computation is necessary or used. The complete coordinator analysis is pinned in verification. Its positive-rho stable-cylinder assertion was already marked unverified there and remains unproved here. Every remaining high-growth flat periodic orbit in A471 remains an open possibility in the global profile class, including the cases where both local cylinders are irrotational.
