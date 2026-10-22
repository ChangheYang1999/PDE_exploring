# Ninth-order curvature removes the fifth-equation sign restriction

Status: complete informal argument written before the independent coefficient controls. The coefficient arithmetic and source comparison are to be checked. This is a local finite-jet theorem, not a global Boussinesq profile.

## Statement and conventions

Fix beta=2, a real point y_*, and signed distance s=y_*-y. All primes below denote d/ds. Let C be a nonzero real number, and let k,H be arbitrary real numbers. Set

    c = k(231H+k^7)/6930,
    a = -Ck/260 - (2642/6435)c k^4,
    B = s + k s^2 + c s^9 + a s^13.

Then there are real analytic functions T, eta, v, D and gamma on a two-sided neighborhood of s=0 satisfying

    B T' = (8+2B')T,
    B eta' = (5+B')eta-T,
    eta = -B''-2v,
    B D' = (16+4B')D + 8v'T-12vT',
    B gamma' = (13+3B')gamma-D+2v'eta-6v eta'.       (1)

Their leading forms are T=C s^10(1+O(s)), eta=s^6(H+O(s)), D=O(s^9), and gamma=O(s^5). Each of D and gamma has one free homogeneous constant. If k is nonzero,

    I_2=D/T^2=-(120k/(11C))s^-11(1+O(s)).           (2)

For any A with A/C>0 and H/A>0, both signs of k are allowed. On s>0, the limit of A I_2 is -sgn(k) infinity. Its sign is reversed on s<0. Thus the five equations in (1) impose neither sign of this infinite limit across this family. The coefficient k=0 is allowed in the analytic construction but is excluded from (2). The quotient I_2 is not defined when C=0.

These are the first two temperature coefficients, first two vorticity coefficients and the relevant Poisson coefficient for x-reflection symmetry. In factorial conventions, T=Theta_xx at x=0, D=Theta_xxxx, eta=Omega_x and gamma=Omega_xxx. They do not include the center normalization or a full-plane inverse. The last equation follows by inserting W2=B+v x^2+..., W1=(4+B')x+v'x^3/3+..., Theta=T x^2/2+D x^4/24+..., Omega=eta x+gamma x^3/6+... into W.gradOmega+Omega-Theta_x=0 and using d_y=-d_s. This gives the stated signs without using a numerical implementation.

## Analytic reduction and the two residues

Write B=sP_B with P_B(0)=1 and define analytic units by convergent integrals

    t=s^10 exp int_0^s[(8+2B')/B-10/u]du,
    Y=s^6 exp int_0^s[(5+B')/B-6/u]du,
    J'=t/(BY), J(0)=0.

The subtracted integrands are analytic at zero, and t/(BY) has order three. Set T=Ct, eta=Y(H-CJ), v=-(B''+eta)/2, q=t'/t and h=Y'/Y. The first three equations of (1) hold directly. Variation of constants in the fourth gives D=T^2 I, where

    I'=Q=[-4B'''+6B''q+6eta q-4eta']/(BT)
        =[-4B'''+6B''q]/(BT)
          +4eta(7+2B')/(B^2 T)+4/B^2.              (3)

The scalar homogeneous factor for the fifth equation is Z=tY, of order sixteen. Its obstruction is

    R=Res[(-D+2v'eta-6v eta')/(BZ)].                (4)

The first obstruction is Res Q. The pole order of Q is at most twelve, hence zero residue is necessary and sufficient for an analytic D of order at least nine. The fifth right hand side divided by BZ has pole order at most twelve, so zero residue is likewise necessary and sufficient for analytic gamma of order at least five. This follows by integrating a convergent Laurent series: only the coefficient of s^-1 introduces a logarithm; all other negative powers are finite in number and become analytic after multiplication by the appropriate vanishing homogeneous factor. A nonzero fifth residue yields a nonzero s^16 log|s| term, which is not C^16. A change I -> I+constant contributes to (4) only at order three, so cannot change its residue.

For the coefficient calculation one may allow arbitrary c,a temporarily. If Res Q is nonzero, I has a logarithm, but D's logarithm starts at order twenty and has no effect on (4). Thus (4) uses its Laurent part through degree sixteen, a well-defined linear calculation before compatibility is imposed. No analytic D is asserted in that untuned case.

## Independent coefficient calculation for arbitrary c and a

The exact obstruction formulas are

    Res Q = 48k/5 + 2496a/C + (169088/165)c k^4/C,

    R = -(6/5)CHk -(9/385)Ck^8 +1092aH
          +(517832/1155)cHk^4 +162Cc.              (5)

Here is a finite derivation. Put P=1+ks and B0=sP. Then

    t0=s^10/P^6, Y0=s^6/P^4, J0'=s^3/P^3,
    [s^n]J0=(-1)^(n-4) binom(n-2,2)k^(n-4)/n, n>=4.

The quadratic values, derived by the finite sums in P303 and P306, are Res Q0=48k/5 and R0=-(6/5)CHk-(9/385)Ck^8. For clarity, the latter is the sum of the temperature contribution -(88/5)CHk-(16/385)Ck^8 and the other two contributions Ck^8/55 and (82/5)CHk. Their finite-polynomial residue sums are rechecked independently in this packet.

Relative corrections to t, Y and B from c start in degree eight, while those from a start in degree twelve. Squares of these relative corrections start in degree sixteen and cannot contribute to a residue of a pole of order at most twelve. The explicit derivatives B'' and B''' must be counted separately. Terms with an explicit c derivative have pole order at most five, so multiplying them by another degree-eight relative correction also cannot change a residue. This proves that the following first-order bookkeeping is exact for the residues, for arbitrary finite c,a, rather than an approximation in small parameters.

Let L describe the first c correction to t/t0: t/t0=1+cL+terms irrelevant to the residues. Direct logarithmic differentiation gives

    L'=s^7(8+14ks)/P^2,
    L=s^8-(2k/9)s^9-(2k^2/5)s^10+(10k^3/11)s^11+O(s^12).   (6)

The corresponding logarithmic derivative variations are

    delta_c q=s^7(8+14ks)/P^2,
    delta_c h=s^7(3+7ks)/P^2.

In (3), the c correction to the eta terms starts too high to affect a residue. The explicit curvature derivatives contribute

    (288c/C)s^-5 P^4(8-ks),

whose residue is 1152c k^4/C. The combination of the q correction and the explicit 1/B correction contributes

    (24kc/C)s^-4 P^3(-1+5ks),

whose residue is 336c k^4/C. The correction from 1/t contributes the negative of

    (12kc/C)s^-12(10+4ks)P^4 L.

Since

    [s^11](10+4ks)P^4 L
       = k^3(64-152/9-88/5+100/11),

the total c coefficient is

    [1152+336-12(64-152/9-88/5+100/11)]/C
       =169088/(165C),

multiplied by c k^4. The a correction comes only from B''=...+156a s^11 and B'''=...+1716a s^10 in (3), with residue (-4*1716+6*156*10)a/C=2496a/C. This proves the first formula in (5).

To compute the second residue without explicitly finding D, use residue integration by parts:

    Res[-D/(B tY)]=C^2 Res[JQ].                  (7)

Indeed D=C^2t^2 I and t/(BY)=J', so the left hand side is -C^2 Res(J'I). The possible logarithm contributes no residue after multiplication by J=O(s^4). The other terms of (4) are exactly

    (H-CJ)(-B'''+3B''h)/(Bt)
    -3C B''/(B^2Y)
    +2(Y/t)(H-CJ)^2 h/B
    -2C(H-CJ)/B^2.                               (8)

This identity follows from 2v'eta-6v eta'=-B'''eta+3B''eta'+2eta eta' and eta'=h eta-Ct/B.

The part proportional to cH comes solely from the first term of (8). The explicit derivatives give residue 504cHk^4. The combination of delta_c h with delta_c(1/B) gives 72cHk^4. The correction from 1/t is -6cHk times

    [s^11](6+2ks)P^4 L
       =k^3(36-88/9-52/5+60/11).

Their sum is (517832/1155)cHk^4. The explicit a derivatives give (-1716+3*156*6)aH=1092aH. No other a correction contributes by the pole-order bounds above.

The terms proportional to Cc in (7)-(8) require only J0=s^4/4+O(s^5). In (7), the leading c curvature correction to Q is (2304c/C)s^-5, giving 576Cc. The -CJ part of the first term of (8) gives -198Cc. The second term gives -216Cc from B''=...+72c s^7. Their sum is 162Cc. Every remaining c correction has nonnegative Laurent order: the last two terms of (8) have worst pole order six before the degree-eight relative correction, and the other unit corrections after the necessary J factor also start too high. This proves the second formula in (5).

## Cancellation, signs, and analytic realization

Choose a=-Ck/260-(2642/6435)c k^4. The first residue vanishes exactly. In the second, the cHk^4 coefficient cancels, because 1092*(2642/6435)=517832/1155. Its remaining value is

    R=162Cc-(9Ck/385)(231H+k^7).

The prescribed c=k(231H+k^7)/6930 makes it zero. The convergent Laurent primitive criterion now constructs analytic D and gamma. Their homogeneous factors T^2 and Z both vanish at zero, so the asserted free constants preserve the indicated orders.

If k is nonzero, the leading term of Q is (120k/C)s^-12. Thus I=-(120k/(11C))s^-11(1+O(s)), proving (2). If k=0 then c=a=0 and the exact formula is instead

    I=-(36H/(5C))s^-5+5s^-1+constant.

This shows directly why the k-nonzero restriction in (2) is necessary. Taking C and H with the same nonzero sign and A of that sign imposes no restriction on k. Formula (2) then proves the two claimed infinite limits.

For a local polynomial realization let d be an arbitrary constant, put

    p=-(gamma/6+v''/3)/4,
    Psi=(B-beta*y+d)x+v x^3/3+p x^5/5,
    Theta=T x^2/2+D x^4/24,
    Omega=-Delta Psi.

Then the x and x^3 vorticity coefficients are eta and gamma/6, respectively. With W=beta X+U-(0,d), U=(-Psi_y,Psi_x), the five relations in (1) imply R_Theta=O(x^6) and R_Omega=O(x^5), with analytic coefficient functions. The Poisson relation is exact. This is only a finite local polynomial realization. The free d is not claimed to equal a global canonical U2(0).

Dependencies are the already checked quadratic finite sums in P303/P306, rechecked here, and elementary convergent analytic ODE and Laurent-series calculations. No full transverse convergence, full-plane inverse, center attachment, simultaneous endpoints or B2 solution is asserted. This extension therefore corrects no previously stated restricted theorem and proves no decisive endpoint.
