# A cubic-jet consequence of a global strain cap

Date: 2026-10-20. Independent implementation checks passed 2026-10-20T19:58:41.770083+00:00. Status: independent analytic verification of STRAINCAP2 and
the higher-vanishing weighted extension. Exact rational constants are checked
separately. Every exclusion below assumes the additional global bound sigma<=D.
It is not a theorem about the entire Setting III class.

## Statement and notation

Let rho,psi,U be an exact smooth primary profile on the whole plane, with the
prescribed parities, sublinear growth and canonical inverse. Put ell>1,
D=ell-1, A=2ell-1, a=rho_y(0)!=0, h=rho-ay, phi=psi+Dxy,
v=U-(Dx,-Dy), and sigma=sup|sym DU|_op. Suppose additionally that sigma<=D.
The origin already gives sigma>=D, so this is the equality case sigma=D.
Write the lowest possible nonlinear Taylor terms as

    h=b x^2 y+e y^3+O(r^5),
    phi=q1 x^3 y+q2 x y^3+O(r^6).

Then either

    a>=2A,

or all four coefficients b,e,q1,q2 vanish. Consequently, for 1<ell<4,

    a>0 implies a >= min(4ell-2, 1000(4-ell)/2363),
    a<0 implies |a| >= 1000(4-ell)/1367.                  (1)

For ell>=4 these particular numerical bounds supply no positive exclusion.
They remain logically true with the positive parts of their right sides.
One may retain the stronger envelope over the admissible weights described
below instead of the single m=5 choice in (1).

## The exact cubic calculation

Since psi=-Dxy+q1 x^3y+q2 xy^3+O(r^6),

    U1=Dx-q1 x^3-3q2 xy^2+O(r^5),
    U2=-Dy+3q1 x^2y+q2 y^3+O(r^5).

Thus the quadratic term of S11, S=sym DU, is

    (S2)11=-3q1 x^2-3q2 y^2.

For a trace-free symmetric two-dimensional matrix, |S|_op^2=S11^2+S12^2.
Here S0=diag(D,-D) and S12(0)=0, giving

    |S(X)|_op^2=D^2-6D(q1 x^2+q2 y^2)+O(r^4).            (2)

The global cap implies the local maximum in (2), hence q1>=0 and q2>=0,
by restriction to each coordinate axis and division by its squared coordinate.
These are necessary local conditions, not sufficient for the global cap.

The degree-two Poisson equation and degree-three transport equation give,
respectively,

    q1+q2=-b/3,
    2Ab+3a q1=0, 2e+a q2=0.

Therefore

    q1=-2Ab/(3a), q2=-2e/a, 6e=(a-2A)b.                 (3)

If b!=0, the first sign condition and A>0 give b/a<0. The second sign
condition then says (a-2A)b/a<=0, which forces a>=2A. If b=0, equations
(3) give e=q1=q2=0. This proves the asserted alternative, including the
negative-a case, where the second alternative is compulsory.

The weaker condition M=sup(-X.U/r^2)<=D implies only q2>=0 by this axis
argument: along the vertical axis -X.U/r^2=D-q2 y^2+O(y^4), whereas its
horizontal-axis value begins at -D. It does not supply the q1 sign needed
for this alternative. We do not apply (1) on the basis of an M cap alone.

## Weighted inverse after higher Taylor vanishing

For clarity we prove the extension needed in the second alternative.
More generally suppose, for an integer k>=1, that an exact profile has
h=O(r^(2k+1)) at zero in its smooth Taylor expansion. The exact equation

    W.grad h-h=-a v2, W=ell X+U=O(r),                   (4)

gives v2=O(r^(2k+1)). Oddness of phi in x gives phi(0,y)=0. Integrating
phi_x=v2 from zero to x then proves phi=O(r^(2k+2)), with all corresponding
Taylor derivatives. In particular v1=-phi_y=O(r^(2k+1)).

At infinity h=O(r) and phi=O(r^2), because the sublinear canonical velocity
and the affine germ have been separated. Consequently, for

    2<m<2k+2, m not an even integer,                     (5)

the cylinder variables H=r^(1-m)h and G=r^(-m)phi lie in L2(ds dtheta),
s=log r, together with the derivatives used by the elliptic identity.
At zero their square integrability follows from 2k+2-m>0, and at infinity
from 2-m<0. The weighted transport boundary flux vanishes with the same
powers: r^(4k+4-2m) at zero and r^(4-2m) at infinity.

For the even angular stream frequencies n=2,4,..., the transformed Poisson
multiplier is n^2-(m+i xi)^2. It is nonzero for every real xi under (5).
For each fixed m in (5), its inverse and the associated derivative
multipliers are bounded uniformly over n and xi. At large n or xi this is
immediate from the quadratic expression; only finitely many n near m
remain, and their positive separation from the even integer m suffices.
Plancherel therefore identifies the actual G with the unique L2 inverse.
There is no additional harmonic polynomial in this weighted realization.

The derivation in result59 now applies with exactly the same density
tridiagonal entries and

    b_j(m)=(m^2+4j^2)/(4|4j^2-m^2|), j>=1.

Define Qminus(m) and Qplus(m) as in that result, using all positive even
stream frequencies. Its Hermitian comparison and sharpness argument do
not depend on restricting m below4. Thus

    (m-1)ell-1 <= m sigma + a Qminus(m)       if a>0,
    (m-1)ell-1 <= m sigma + |a| Qplus(m)     if a<0.       (6)

In the vanishing-cubic alternative k=2, (5) permits both 2<m<4 and
4<m<6. Under sigma=D, equation (6) reduces to

    m-1-ell <= |a| Qsign(m).                             (7)

The single value m=5 and the exact upper constants proved next imply
|a|>=1000(4-ell)/2363 for positive a in this alternative, and
|a|>=1000(4-ell)/1367 for negative a. The first alternative instead has
a>=2A. Taking their union proves (1).

## A rational certificate for the m=5 constants

The same independent Schur-tail construction as in result59, now with

    b_j=(4j^2+25)/(4|4j^2-25|), N=8,

proves

    Qminus(5)<2363/1000, Qplus(5)<1367/1000.              (8)

Here is the complete finite procedure. For s=+1 or -1, set

tau_s=s/2+2b_9, lambda=2363/1000 or1367/1000 respectively, and d1=1/4,
d_j=1/2 for j>=2. The links b_j decrease for j>=3, so the infinite tail
beginning at index9 has quadratic form at most tau_s. Since lambda>tau_s,
its resolvent is bounded above by 1/(lambda-tau_s). Define

    p1=lambda-s/4,
    pj=lambda-s/2-b_(j-1)^2/p_(j-1) for 2<=j<8,
    p8=lambda-s/2-b_7^2/p7-b_8^2/(lambda-tau_s).

All eight pivots are strictly positive for each sign. They are exact
fractions, recorded with their integer-arithmetic checker in verification.
Positive finite pivots, the strict tail gap and completion of the square
prove (8) for the entire infinite operator. A floating-point truncation
alone would not certify an exclusion. Supporting finite spectra are
reported separately and do not enter (1).

At ell decreasing to1, (1) gives positive-slope lower bound
3000/2363, approximately1.2695726, and negative-slope bound3000/1367,
approximately2.1945867. At ell=1.5 the corresponding bounds are
2500/2363 and2500/1367; at ell=2 they are2000/2363 and2000/1367.
These are certified single-weight lower bounds. They need not equal the
suprema over m and are not labelled optimized constants.

## General envelopes and flat jets

Without a cap and with only the ordinary cubic vanishing of h, result59
gives the unconditional necessary envelope

    sigma >= max(D, sup_{2<m<4}
                    [ell-(ell+1)/m-|a| Qsign(m)/m]).     (9)

For fixed ell and any exact-profile sequence with a tending to zero,
first keep each m<4 fixed in (9), then take the supremum as m increases
to4. This proves liminf sigma>=max(D,(3ell-1)/4). No bound on Q(m)
uniformly up to its pole is required, since these limits are in that order.
With ell_n tending to ell>1 the same argument gives the corresponding
limit statement. It says nothing about whether such a sequence exists.

For any non-even m>2, a direct norm estimate on the two shifts of the
tridiagonal operator gives

    ||v2||_m <= C_m ||h||_m,
    C_m=(3+R_m)/4, R_m=sup_{n positive even}(n+m)/|n-m|.  (10)

Indeed the diagonal norm is at most1/2; the lower shift coefficients have
modulus at most1/4; and the upper shift has modulus at most R_m/4. These
bounds hold at every radial frequency because adding xi^2 decreases each
ratio above1. For2<m<4 only n=2 or4 can maximize R_m, giving C3=5/2.
For m=2J+1 one has R_m=2m+1 and C_m=m/2+1.

A separate closed quadratic bound is Qminus(m)<=max_j(d_j+b_(j-1)+b_j),
with b_0=0, by 2|u_j u_(j+1)|<=|u_j|^2+|u_(j+1)|^2. At m=sqrt(8),
b1=b2=3/4 and b3=11/28, with all subsequent links decreasing. The
first row sum is1, the second is2, and every subsequent row is less than2.
Thus Qplus<=Qminus<=2, proving
(sqrt(8)-1)ell-1<=sqrt(8)sigma+2|a| directly.


If h is flat at the origin, the extension (5) holds at every such odd m.
Use C_m in (6), divide by m, and let m tend to infinity. This proves the
conditional bound sigma>=ell-|a|/2. Flatness has not been proved for the
whole class, or even for every capped profile. The cubic alternative does
not license induction to infinite order without further arguments.

## Dependencies and scope

The center equations are checked directly above. The canonical growth and
weighted identity are those of results57 and59; their extra integrability
and uniqueness for m>4 have been supplied here. This completes WID1(a-e,g)
and STRAINCAP2(i-ii) within the stated conditional scope. The first-derivative
energy extension is a separate item. No global strain cap is assumed from
a sampled maximum. No kinematic non-profile is required to satisfy (6).
