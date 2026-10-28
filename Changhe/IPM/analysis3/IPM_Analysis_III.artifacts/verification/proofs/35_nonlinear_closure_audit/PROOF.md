# Parametric tails and a precise two-norm closure theorem

This audits the fixed theory author snapshot in `evidence/lead_snapshot.md`. The background is the exactly normalized modal trial from V005. The canonical velocity, c, and normalization conventions are V002. Write ell0=1/k, Phi_q=r^q Theta(theta), and let chi be a smooth radial function with0<=chi<=1, chi=0 for r<=1 and chi=1 for all sufficiently large r. Its particular transition radius is irrelevant below. The actual angular profile Theta is a finite sine polynomial of highest frequency n=521. The original coefficient identity is checked in `code/check.py`.

The exact modal trial is rho0=Phi_k+R outside a large disk, where R and its differentiated modal expansion are O(r^(2k-1)). Here0<k<5/16. Set

    rho_ell = rho0 + chi (Phi_q-Phi_k),  q=1/ell.

Only this parameterization and its far radial behavior are asserted. An anisotropic axis-jet target requires additional membership checks.

## 1. The correct far cancellation and a nonzero highest interaction

The identity

    (ell X.grad-1)Phi_k=(ell-ell0)k Phi_k

has a positive sign. Outside the cutoff, rho_ell=Phi_q+R and (ell X.grad-1)Phi_q=0. Equivalently, the contribution of the **subtracted** Phi_k cancels the parameter variation on the old Phi_k. This proves the intended leading linear cancellation but corrects the displayed sign in the snapshot.

For a homogeneous density r^q S(theta), the stream function has leading form r^(q+1)P(theta). Its equation is

    -[(q+1)^2 P+P''] = q cos(theta) S-sin(theta) S'.

If the highest sine term of S is a_n sin(n theta), n odd, then the highest sine term of P has frequency n+1 and coefficient

    p_(n+1) = (q-n)a_n/[2((n+1)^2-(q+1)^2)]
            = -a_n/[2(n+q+2)].

The homogeneous velocity in polar components is (-r^q P', (q+1)r^q P). Therefore

    U[Phi_q].grad Phi_q
      = r^(2q-1) [-q P'S+(q+1)PS'].

The coefficient of sin((2n+1)theta) is

    -(n-q)a_n^2/[4(n+q+2)],                         (1)

which is nonzero for0<q<1 and a_n!=0. No other pair of frequencies reaches2n+1. Compact modifications of Phi_q contribute only lower far powers to its canonical velocity. This follows either from the exact radial Green formula or from the multipole expansion; the first parity-allowed decaying velocity is O(r^-3).

For the actual trial,

    a_521 = exp((3-k)t_plus) Aout[259,0]/8,
    Aout[259,0] = -8059128652303703 /
                  10384593717069655257060992658440192 != 0.

The scalar normalization repair changes only the lowest angular coefficient, so this identity survives the repair. Formula(1) proves that the new far self-interaction is not accidentally zero.

Let F_ell(rho)=(ell X+U[rho]).grad rho-rho. Then

    F_ell(rho_ell)-F_ell0(rho0)
      = (ell-ell0) X.grad R
        + U[Phi_q+R].grad(Phi_q+R)
        - U[Phi_k+R].grad(Phi_k+R)
        + lower compact-cutoff velocity terms.

It is O(r^(2 max(q,k)-1)). If q>k, its highest interaction has the nonzero r^(2q-1) coefficient(1). If q<k, the old interaction supplies a nonzero sin(1043theta) coefficient of order r^(2k-1); the parameter variation of R cannot cancel it because every angular mode of R has frequency at most521. The cross terms with R are lower order for q near k. Thus the snapshot's O(r^(q+k-1)) claim is false for every sufficiently close q!=k.

The corrected exponent causes no new radial integrability obstruction. For weight r^-5/4 dX, a power r^beta is square integrable at infinity iff beta<-3/8. Hence the corrected residual and all its parameter derivatives, whose additional factors are powers of log r, lie in the far radial target whenever max(q,k)<5/16. This assertion alone does not remove the singular angular factor |cos theta|^-2a.

## 2. Scalar normalization can be eliminated exactly

Let s3/pi be the positive angular moment from V034, denoted S>0. The strain of a cutoff homogeneous tail is

    c[chi Phi_q] = S int_1^infinity chi(r) r^(q-2) dr.

For ell>1, define

    nu(ell,h)=3ell-1-c[rho_ell]-c[h].

Assume h has the exact zero leading jet and c[h] is defined, for example in Z_cap of V034. Differentiation under the integral is justified on every compact ell interval in(1,infinity). It gives

    d_ell nu = 3 + q^2 S int_1^infinity chi(r) r^(q-2) log r dr >= 3.       (2)

If chi=1 eventually, nu tends to minus infinity as ell decreases to1 and tends to plus infinity as ell tends to infinity. Thus for every real c[h] there is exactly one ell(h)>1 satisfying nu=0. It depends smoothly on c[h]. Since nu(ell0,0)=0, the mean value theorem and(2) give

    |ell(h)-ell0| <= |c[h]|/3.                         (3)

This is a scalar normalization result, not an existence theorem for the PDE. It makes the normalization closed in any Banach space on which c is continuous. It does not make c continuous in the radial graph refuted in V032.

At h=0, write KP=chi r^k log r Theta and d=3ell0+k c[KP]. Then

    d_ell rho_ell|ell0=-k^2 KP,
    d_ell nu|ell0=3+k^2 c[KP]=k d>0,
    D ell(0)[h]=c[h]/(k d).

This matches the linear bordering denominator and the exponent-variation convention.

## 3. The augmented residual must also remove the origin defect

An off-shell rho_ell+h has leading coefficient1 but generally has nu(ell,h)!=0. Its cubic residual is nu x^2y. A forcing space whose origin jet has a positive exponential weight does not contain this nonzero constant factor. Thus the unmodified PDE residual is not a map into that target for arbitrary independent(ell,h).

Let G=X.grad rho0 and choose a compact smooth chi0 equal1 near0. Put H0=chi0 G/3, whose leading cubic coefficient is1. The correctly augmented map is

    (F_ell(rho_ell+h)-nu(ell,h) H0, nu(ell,h)).          (4)

When nu=0, its first component is the original PDE residual. Formula(4) removes exactly the forbidden cubic coefficient off shell. Full membership and continuity of its remaining axis jets and derivatives still require the selected X and Y definitions.

At the base point, let Lfix g=(V.grad-1)g+U[g].grad rho0 and Lren=Lfix+c[.]H0. The derivative of(4) is

    (g,deltaell) |->
      (Lren g + z_ell deltaell, -c[g]+k d deltaell),

where

    z_ell = G-3H0-k^2(Lfix KP+c[KP]H0).

Writing gfar=(1-chi0)G-k Phi_k and

    yKP=Lfix KP+c[KP]H0-ell0 Phi_k,

one gets z_ell=gfar-k^2 yKP. Eliminating the scalar row gives exactly

    Lred g = Lren g+c[g](ell0 gfar-k yKP)/d.

This independently recovers V034. The condition d!=0 only permits this elimination. It does not imply invertibility of Lred; when Lren is invertible, the additional rank-one condition is1+c[Lren^-1 zeta]!=0.

## 4. A valid abstract two-norm iteration

Let X_H be a reflexive Banach space continuously and injectively embedded in a Banach space X_L. Let Y_H embed continuously in a Banach space Y_L. Let A0:X_H->Y_L be bounded and B:X_L x X_H->Y_L be bounded bilinear, with

    ||B(d,h)||_Y_L <= C_B ||d||_X_L ||h||_X_H.

For every v in the closed X_H ball of radius r, suppose a compatible linear solution operator R_v is defined on Y_L, with values in X_L, and maps Y_H into X_H. The two bounds are

    ||R_v f||_X_L <= K_L ||f||_Y_L,
    ||R_v f||_X_H <= K_H ||f||_Y_H.

Require that A_v=A0+B(v,.) satisfies A_v R_v f=f for f in Y_H and that

    ||g||_X_L <= K_L ||A_v g||_Y_L                    (5)

for every g in X_H. Equivalently, these conditions follow from compatible maximal-domain inverses. The compatibility requirement prevents two unrelated realizations from being used in the two norms.

For f in Y_H, set eta=||f||_Y_H, h0=0 and h_(j+1)=R_(h_j)(-f). If

    K_H eta <= r,   q0=K_L C_B K_H eta<1,             (6)

then the iterates stay in the radius-r high ball. Subtracting the two equations gives, for j>=1,

    A_(h_j)(h_(j+1)-h_j)=-B(h_j-h_(j-1),h_j).

By(5), the differences contract in X_L by q0. The sequence converges strongly in X_L to h. Reflexivity gives a weakly convergent subsequence in X_H, and the continuous embedding identifies its limit with h. Weak lower semicontinuity gives ||h||_X_H<=K_H eta.

To pass to the equation, write

    B(h_j,h_(j+1))-B(h,h)
      =B(h_j-h,h_(j+1))+B(h,h_(j+1)-h).

The first term tends strongly to0 in Y_L; the second tends weakly to0 along the chosen subsequence because B(h,.) is bounded linear on X_H. A0 h_(j+1) converges weakly to A0 h. Hence

    A0 h+B(h,h)=-f.

Uniqueness in the high ball follows if K_L C_B r<1: for two solutions h,g, A_h(h-g)=-B(h-g,g), and(5) gives h=g. If only(6) holds, uniqueness follows within the smaller ball of radius K_H eta. The iteration supplies a solution without assuming convergence in the high norm.

The same proof is possible with a dual high space only after specifying weak-star compactness and weak-star continuity of A0 and B(h,.), with limits identified by the low embedding. An unspecified Banach high space does not itself supply these properties. This is the missing logical hypothesis in the snapshot's weak-star argument.

## 5. Why this theorem does not yet close the parametric IPM problem

For the formal fixed-background equation, B(d,h)=W[d].grad h and A0=L have the structure above. But the actual far exponent varies. A fixed linear correction space with only one log column does not contain chi(Phi_q-Phi_k) when q!=k, by V025. Splitting the exact residual into Lh and B(h,h) in that inadequate space is therefore not a valid application of section4.

One must prove the hypotheses for the augmented map(4), or for its scalar-eliminated version using ell(h). Its parameter columns and nonlinear tail cancellations must be treated jointly. Merely saying that ell is updated after a fixed-background step does not prove those hypotheses. Moreover, in the parametric formulation the background coupling gradient varies with ell; the claim that the compact remainder is exactly independent of every iterate no longer follows from the fixed-background quadratic identity. Uniform compactness or a quantitative perturbation bound may be enough, but it must be proved.

The velocity margin bound and any desired global flow structure are separate hypotheses. A pointwise bound on DW controls the displayed multiplier perturbation, but it does not by itself establish the number and connections of all equilibria of the unperturbed flow or the global structural stability assumptions. No nonexistence claim follows from these gaps.

## 6. Verdict

CONFIRMED: the exact quadratic fixed-background expansion, corrected leading cancellation, corrected far radial membership, monotone scalar normalization, augmented linearization and the abstract two-norm theorem under its stated hypotheses. REFUTED: the snapshot's smaller far remainder exponent and any inference that d!=0 proves the reduced inverse. OPEN: the actual spaces and all uniform inverse, high-norm, bilinear, axis-jet and residual bounds required to apply the theorem to the nonlinear parametric IPM equation.
