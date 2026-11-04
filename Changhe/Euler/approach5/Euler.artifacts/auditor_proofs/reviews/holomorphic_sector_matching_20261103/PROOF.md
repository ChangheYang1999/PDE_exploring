# Excluding a specified holomorphic germ from a C2 global ranked tail

## 1. Statement and exact scope

Let 2/5<c<1/2, omega be any finite real number, a=1-2c, Jx=e3 cross x, A=cI-omega J, L=(1-c)I+omega J and D=R3 minus {0}. Let V in C2(D;R3) and P in C2(D) satisfy

    div V=0, DV(Ax)=-LV, Delta P=-tr((DV)^2),
    grad k cross grad S=0 on {curl V!=0},
    k=(Ax).V, S=P-|V|^2/2.

For lambda=-a/(c-i omega) and any B in C minus {0}, define on an off-axis ball with a branch of log z, z=x1+i x2,

    f=Re(B exp(lambda log z)), V_B=-grad f/a, P_B=-|V_B|^2/2.

The pair (V,P) cannot agree with (V_B,P_B) on any nonempty such ball. No sign, comparison, global helicity or vortex-density premise is used in this abstract tail statement. An actual-profile consequence requires the previously proved rank/Poisson/tail package and the EXTRA global C2 regularity of V. Natural C1,alpha convergence alone is insufficient.

## 2. Supported rank is stationary to first order

Write W=curl V and F=grad k cross grad S. The hypotheses make F continuously differentiable. It vanishes on the open set {W!=0}, and hence DF also vanishes there. By continuity,

    F=DF=0 on supp W.

This uses support relative to D. No boundary regularity or finite component count enters. Only F=0, not DF=0, is available if k,S are merely C1.

## 3. The model has no stationary rank zero

Write B=A0 exp(i gamma), A0>0, lambda=u+iv and log z=log rho+i phi. Since a,c>0,

    u=-ac/(c^2+omega^2)<0,
    psi=gamma+v log rho+u phi,
    f=A0 rho^u exp(-v phi) cos psi,
    E=|V_B|^2=(A0^2 |lambda|^2/a^2)rho^(2u-2)exp(-2v phi)>0.

In the orthonormal cylindrical frame,

    grad f=A0 rho^(u-1)exp(-v phi)
       [(u cos psi-v sin psi)e_rho+(-v cos psi-u sin psi)e_phi],
    grad E=(2E/rho)[(u-1)e_rho-v e_phi].

Differentiating along Ax gives (Ax).grad f=-af, so k_B=f and S_B=-E. The cross product is therefore

    F_B=2A0 E rho^(u-2)exp(-v phi)
             [v cos psi-(|lambda|^2-u)sin psi]e3.

Set C0=|lambda|^2-u>0. At a zero of the bracket its psi derivative has modulus sqrt(v^2+C0^2)>0, while grad psi=(v e_rho+u e_phi)/rho is nonzero. The positive prefactor cannot change this conclusion: F_B=0 implies DF_B!=0. Thus F_B and DF_B never vanish together, for every omega including zero and every amplitude and phase B.

Consequently second-jet matching of the pair (V,P) with an analytic continuation of the model at an off-axis supported point contradicts Section2. The local exclusion needs only this matching and supported rank; it does not need the other global equations.

## 4. Why a global match forces this contact

Let Dstar be R3 with its entire vertical axis removed, and let O be the connected component of int{W=0} relative to Dstar that contains the proposed matching ball. On O, div V=curl V=0 implies Delta V=0. The pressure equation and symmetry of DV imply

    Delta(P+|V|^2/2)=0.

Harmonic regularity makes V and Q=P+|V|^2/2 analytic. Since Q=0 on the initial ball, Q=0 on connected O. The model velocity can be analytically continued along each path avoiding the axis by lifting log z. Harmonic unique continuation propagates equality of V with this branch along paths in O. Pressure equality follows from Q=0.

If O is proper in connected Dstar, choose a finite piecewise-linear path from the starting ball to a point outside O. At its first exit x*, the preceding portion remains in O. Its compact image stays a positive distance from the axis, so the continued logarithm has a finite limit at the exit. A small off-axis ball about x* carries the resulting ordinary analytic branch. Along the last portion approaching x*, equality holds in open neighborhoods, hence includes derivatives through order2. Global C2 continuity yields equality of those jets at x*.

This boundary point belongs to supp W: otherwise a connected ball about it would be irrotational, meet O and belong to the same component, contradicting first exit. Section3 now rules it out. This argument uses a finite path only; no global logarithm, interface smoothness, or control of component multiplicity is assumed.

## 5. The no-exit alternative also contradicts the model

It remains that O=Dstar. Continuity extends W=0 to D, including the nonzero points of the axis. Direct differentiation of k and the twisted homogeneity gives the Lamb identity

    grad k=-aV+(Ax) cross W=-aV.

Thus k is harmonic, and (Ax).grad k=-ak. Put m=a/c in (0,1), sigma=omega/c, and q(x)=exp(sigma log|x| J)x/|x|. Then

    k(x)=|x|^(-m)Psi(q(x))

with a smooth Psi on the whole sphere. Writing Y for axial rotation, Delta k=0 gives

    [Delta_S2+sigma^2 Y^2+sigma(1-2m)Y+m(m-1)]Psi=0.

The second-order symbol is positive definite, and m(m-1)<0. At a positive maximum the first derivatives vanish and the second-order term is nonpositive, a contradiction. Apply the same argument to -Psi to exclude a negative minimum. Compactness gives Psi=0, so k=0 and V=0. This contradicts E>0 on the matching ball and proves the theorem.

## 6. Dependencies and verdict limits

The proof reconstructs all algebra, contact and quotient steps. Its analytic inputs are harmonic regularity and unique continuation on connected open sets, already used in the fully checked B62 audit at in the team records. The explicit local model is independently verified in the team records. The source is pinned in the team records with its hash.

For an original profile, require the full C2/C1 profile equation, global helicity freedom, natural U and full-gradient bounds, and separately impose V in C2(D); the known natural pressure is C2,alpha. Then the actual rank and Poisson hypotheses above follow and the specified germ is excluded. This does not exclude arbitrary three-dimensional harmonic germs or prove the same matching obstruction for natural C1,alpha tails. It does not contradict the exact solution on its sector alone, which has no required global matching. The bare-decay conjecture stays OPEN. No computation, formalization, new model client or agent was used. Existing configured model collaboration remains through files; actual provider runtime is unattested.
