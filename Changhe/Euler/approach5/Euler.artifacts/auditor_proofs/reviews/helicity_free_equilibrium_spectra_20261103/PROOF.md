# Equilibrium spectra under the global helicity-free rank identity

Status: independent reconstruction of items N2-N3 in the coordinator's flat-stratum check. The complete configured-model check and the underlying equilibrium proof have been read. Final postwrite inspection is complete. A468-A469 and A714 confirm the exact necessary-condition scopes below.

## 1. Exact setting

Let U in C2(R3;R3), P in C1 solve

    div U=0,
    (1-c)U+(B.grad)U+omega JU+grad P=0,
    A=cI-omega J, B=Ay+U,

where0<c<1/2, omega is arbitrary real and J is the fixed rotation generator about the third axis. Assume U=o(|y|) uniformly and U.curl U=0 everywhere. Write

    W=curl U, O={W!=0},
    a=1-2c, kappa=1+c, d=3c, D=d+kappa=1+4c,
    H=P+|U|^2/2+(Ay).U, g=U.B.

At a carrier equilibrium p, set

    u=U(p)=-Ap, M=DU(p), F=DB(p)=A+M, w=W(p).

A is invertible because c>0. The identities used are

    grad H=-aU+B cross W,
    BH=-ag,
    [B,W]=-kappa W,
    tr F=d.                                        (1)

They hold at C2 regularity. A413 gives dH wedge dg=0 on O; the rank tensor is C1 and both it and its first ambient derivative vanish on closure(O). These are genuinely global consequences under the stated hypotheses. They are not assumed for arbitrary local Euler germs.

The backward exponents of the equilibrium point mass are the negatives of the real parts of the eigenvalues of F, with algebraic multiplicities. Polynomial factors from Jordan blocks do not change these exponents.

## 2. Vortical equilibria

Suppose w!=0. At B(p)=0 the vorticity equation gives

    Fw=kappa w.                                    (2)

If p=0 then u=0. Differentiating the exact helicity identity gives M^T w=0. Taking the inner product of(2) with w gives

    kappa|w|^2=w.Aw+w.Mw=c|w|^2,

since A has symmetric part cI and w.Mw=(M^T w).w=0. This contradicts kappa-c=1. Thus a vortical carrier equilibrium cannot be the spatial origin. This particular exclusion only needs the vanishing first helicity jet at that point, not the global rank theorem.

For p!=0, u=-Ap!=0. At the equilibrium(1) gives grad H=-au, while differentiating g=U.B gives grad g=F^T u. Since p belongs to the open set O, the rank identity gives a real rho with

    F^T u=rho u.                                   (3)

The plane T=u-perpendicular is F-invariant. Helicity gives w in T and(2) gives one tangent eigenvalue kappa. The action on the one-dimensional quotient by T has eigenvalue rho. Trace F=d fixes the remaining tangent eigenvalue d-rho-kappa=-a-rho. Hence

    spec F={rho,kappa,-a-rho},
    lambda_top(delta_p)=max(-rho,a+rho).             (4)

All eigenvalues are real, with multiplicities retained when rates coincide. The omitted candidate -kappa is smaller than the maximum displayed, since that maximum is at least a/2>0. The strict C2 growth test lambda_top<2a holds exactly when

    -2a<rho<a.                                     (5)

No bound placing rho in this interval is proved.

For clarity about what a higher-jet argument must keep, let C_w(v)=w cross v and T_u=sum_i u_i D2U_i(p). Then

    L_H:=Hess H(p)=-aM-C_w F,
    Hess g(p)=M^T F+F^T M+T_u.                      (6)

Indeed D(B cross W)(p)v=Fv cross w, and the second product derivative of U.B contains T_u even though B(p)=0. Differentiating the rank identity gives

    Hess g=-(rho/a)L_H+tau u tensor u.              (7)

Combining the second Taylor coefficient of BH=-ag with(7) gives

    F^T L_H+L_H F-a T_u=rho L_H-a tau u tensor u.    (8)

The product expansion is valid with H C2: B vanishes at p, so multiplying the first-order remainder of grad H by B is o(|y-p|^2). There is no assumption of H C3. Discarding T_u would give an unjustified extra constraint; equations(6)-(8) do not themselves bound rho.

## 3. Irrotational equilibria away from the origin

Suppose p!=0, w=0 and p in closure(O). The closure premise is explicit: zero helicity does not by itself extend A413 to the interior of an irrotational open set. Now M is symmetric and traceless. Again u!=0, grad H=-au and grad g=F^T u, so the closure rank identity gives(3) and an invariant plane T=u-perpendicular.

Since B=w=0, D(B cross W)=0 at p. Thus Hess H=-aM. The first ambient derivative of the rank tensor gives

    Hess g=rho M+tau u tensor u.                   (9)

Let K=DW(p). If K=0 then Delta U=-curl W=0 at p. The scalar product identity gives

    Delta g=(Ay+2U).Delta U+2M:A+2|M|_F^2
            =2|M|_F^2,

because M:A=c tr M-omega M:J=0 for symmetric traceless M. Taking the trace of(9) yields

    tau|u|^2=2|M|_F^2.                              (10)

This does not bound the eigenvalues of F.

If K!=0, differentiating helicity at p gives K^T u=0. The first vorticity jet satisfies

    FK-KF=kappa K.                                  (11)

There is no differentiation of W twice. Write B(p+h)=Fh+o(|h|), W(p+h)=Kh+o(|h|), DW(p+h)=K+o(1) and DB(p+h)=F+o(1), and compare the linear terms of(1). Nonzero K also implies p in closure(O), so that premise is automatic in this nonflat case.

Complexify the vector space only to classify spectra. Equation(11) maps each generalized F-eigenspace of eigenvalue sigma into the generalized eigenspace of eigenvalue sigma+kappa. To verify this, commute K repeatedly through F-(sigma+kappa)I. Also image K is contained in the invariant complexification of T, by K^T u=0. A nonzero component of K therefore has a source eigenvalue sigma and a target eigenvalue sigma+kappa among the two tangent eigenvalues. The source is either the quotient eigenvalue rho or a tangent eigenvalue.

If the source is rho, a tangent eigenvalue is rho+kappa and trace gives the other one -a-2rho. If the source is tangent, the two tangent eigenvalues differ by kappa and sum to d-rho. The complete alternatives are therefore

    spec F={rho,rho+kappa,-a-2rho},                  (12a)
    spec F={rho,(-a-rho)/2,(D-rho)/2}.               (12b)

They are real, including all repeated-eigenvalue cases. If a tangent pair had nonreal conjugate eigenvalues, its difference could not equal the positive real kappa, nor could one member differ from the real rho by kappa. Hence it cannot support a nonzero K. The argument does not assume diagonalizability and exhausts generalized-eigenspace possibilities.

## 4. Scope and evidence

Equations(4)-(5) and(12) are necessary spectra, not constructions or exclusions of these equilibria in a global decaying profile. The flat origin is not settled here. Its first-vorticity-flat conclusion is the separate LIT102 submission. No condition on a surrounding invariant measure, basin coverage, isolated equilibria or pressure normalization is used. Arbitrary finite omega is allowed; no step divides by omega.

The source equilibrium proof is pinned in the team records. Its upstream nested model consultation failed; the subsequent coordinator check identifies its own configuration as the primary model and explicitly rechecks N2-N3. The full coordinator check was read, and its algebra was independently rederived above. Model configuration is not independent provider attestation. No new model client and no computation were used for this audit.


## 5. Completion of LIT108: exact thresholds and the rank-two first jet

Independent addition at 2026-11-03T10:25:38.427723+00:00. The hypotheses are exactly Section1 and, for the irrotational statements, p!=0, W(p)=0 and K=DW(p)!=0. The whole current LIT108 source was read and compared. Sections2-3 above already prove its covector and spectral alternatives.

For family (12a), the largest backward exponent is

    max(-rho,a+2rho),

because -rho-kappa<-rho. It is less than2a precisely when -2a<rho<a/2. For family (12b), the largest backward exponent is

    max(-rho,(a+rho)/2),

because (rho-D)/2<(a+rho)/2, using D+a=2kappa>0. It is less than2a precisely when -2a<rho<3a. These statements include repeated eigenvalues: polynomial Jordan factors do not change exponential rates.

The commutator FK-KF=kappa K gives K:E_sigma -> E_(sigma+kappa) on generalized eigenspaces. Three shifts would require four distinct eigenvalues if K^3 were nonzero, which is impossible in dimension3. Therefore K^3=0 and K is nilpotent of rank at most2. If its rank is1, write K=x tensor ell. Nilpotence implies trace K=ell(x)=0, hence K^2=0.

If rank K=2, nilpotence forces a length-three Jordan chain, so K^2!=0. Choose a generalized F-eigenspace on which K^2 is nonzero. Its images require three distinct eigenvalues sigma,sigma+kappa,sigma+2kappa. They exhaust dimension3, so each eigenspace is one-dimensional and F is diagonalizable in this particular case. The image of K is exactly the span of the two higher eigenspaces, because K maps the lowest to the middle and the middle to the highest. It is also the invariant plane u-perpendicular, by rank2 and K^T u=0. Consequently the eigenvalue on the quotient, previously called rho, is sigma. Taking the trace yields

    3c=3rho+3kappa, rho=-1,
    spec F={-1,c,1+2c}.

Its largest backward exponent is1. In the target interval2/5<c<1/2, this exceeds2a<2/5. This identifies an obstruction to applying the strict C2 growth criterion to such an equilibrium; it does not construct or exclude the equilibrium in a global profile.

The original C2 assumptions suffice throughout: the first vorticity commutator uses only first-order expansions of the C1 W, not second derivatives of W. The rank theorem is a global helicity-free consequence and is not licensed for arbitrary local Euler germs. No new computation or formal build was used. This completes all the submitted algebraic assertions of LIT108, beyond the already confirmed A468-A469 portion.
