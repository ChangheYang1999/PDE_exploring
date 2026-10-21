# Integer axis exponents of the frozen Fourier packet

Date: 2026-10-20. Status: CONFIRMED after independent reconstruction and an actual Claude Opus5.5 review. This is a statement about an explicit solution of the frozen model, not a coupled IPM profile.

## Exact statement and notation

Let A>1, let j>=1 be odd, and let m>=1 be an integer. Set

    g=j-1+Am, q=2(A-1), b=g/q, c_F=(2pi)^(-2), K_j=2 i^j c_F/j!.

Let Phi belong to C_c^infinity(R minus {0}), with integral Phi=0 and Phi(-t)=-conjugate(Phi(t)). Define the real packet

    v(s,y)=2i c_F integral_0^infinity r^(-2) sin(yr)
            integral_R Phi(t) exp(i s t r^A)(1+t^2 r^q)^(-b)dt dr.

The integral is interpreted with the t integral performed first near r=0. Its convergence, continuity and differentiation through the required y order are also justified below. Define the axis function G_j(s)=d_y^j v(s,0)/j!. Put

    Psi(t)=Phi(t)|t|^(-2b),
    M_a=integral_R t^a Psi(t)dt,
    F_epsilon(u)=integral_R Psi(t)exp(i epsilon t u)dt,
    f_(a,epsilon)=(i epsilon)^a M_a/a!.

Then G_j is C^(m-1) as a one-dimensional function near zero. For s tending to zero through either sign epsilon,

    G_j(s)=sum_(a=0)^(m-1) tau_(j,a)s^a
             + L_j s^m log(1/|s|) + D_(j,epsilon)|s|^m
             + o(|s|^m),                                      (1)

where

    L_j=K_j i^m M_m/(A m!).                                   (2)

For a<m and p=j-1+Aa>0,

    tau_(j,a)=K_j i^a/(a!q)
        B(p/q,(g-p)/q) integral_R t^a Phi(t)|t|^(-2p/q)dt.       (3)

Here B(u,w)=integral_0^infinity z^(u-1)(1+z)^(-u-w)dz for positive u,w. The only excluded case is j=1,a=0, where

    tau_(1,0)=-4i c_F/q integral_R Phi(t)log|t|dt.               (4)

The constants D are finite and have an explicit convergent formula below. If L_j is nonzero, G_j is not C^m at zero. If L_j=0 but D_(j,+) differs from (-1)^m D_(j,-), G_j is not C^m at zero. No converse is asserted from the asymptotic alone.

For every A,j,m as above there exist imaginary even Phi with zero integral giving a failure of C^m. More precisely, write Phi=i phi with phi real and even, and put

    I_m=integral_0^infinity phi(t)t^(m-2b)dt.

For even m the logarithmic coefficient is

    L_j=4 c_F i^(j+m+1) I_m/(j! A m!).                         (5)

For odd m the logarithmic coefficient vanishes, and

    D_(j,+)=D_(j,-)=4 c_F i^(j+1) J_m^cos I_m/(j! A),           (6)

where the real absolutely convergent integral

    J_m^cos=integral_0^infinity z^(-m-1)
       [cos z - sum_(k=0)^((m-1)/2) (-1)^k z^(2k)/(2k)!]dz     (7)

has sign (-1)^((m+1)/2) and is nonzero. Thus I_m nonzero gives the claimed failure in both parity cases. These axis statements are separate from two-dimensional regularity and from vanishing of normalized higher traces.

## Convergence and differentiability below the critical order

The t support lies in delta<=|t|<=D for fixed positive delta,D. At small r the zero moment gives, uniformly on compact s intervals,

    integral Phi(t)exp(i s t r^A)(1+t^2r^q)^(-b)dt
          =O(|s|r^A+r^q).

With sin(yr)=O(r), the low-r density integrand is bounded by C(r^(A-1)+r^(q-1)), which is integrable. At large r it is bounded by C r^(-2-g). The same bounds with the first y derivative use r^(-1) and the cancellation just displayed. For derivative orders 2<=c<=j the low-r power r^(c-2) is already integrable. At infinity every derivative through j is bounded by C r^(c-2-g), and g>j-1. These bounds hold locally uniformly in (s,y), so dominated differentiation gives

    G_j(s)=K_j integral_0^infinity r^(j-2)
              integral Phi(t)exp(i s t r^A)(1+t^2r^q)^(-b)dt dr. (8)

The a-th s derivative inserts (it r^A)^a. For a<m its high-r exponent is j-2+Aa-g=-1-A(m-a)<-1. Its low-r exponent is integrable whenever a>=1; the a=0,j=1 case uses the same zero moment. Consequently G_j is C^(m-1). At zero, substitution z=t^2r^q gives (3), with 0<p<g. Absolute convergence permits Fubini.

For j=1,a=0, subtract the reference amplitude (1+r^q)^(-b), whose t integral is zero. The convergent radial difference equals -2log|t|/q. To see this, set z=r^q and differentiate

    H(d)=integral_0^infinity [(1+dz)^(-b)-(1+z)^(-b)]dz/z

for d>0. On compact positive d intervals differentiation is dominated and H'(d)=-1/d, while H(1)=0. This proves (4), including the first-trace exception to the ordinary beta formula.

## Removal of the leading high-frequency tail

Define

    P_j(s)=K_j/A integral_1^infinity z^(-m-1)F_+(sz)dz,
    H_j(s)=G_j(s)-P_j(s).                                  (9)

Equivalently, P_j is the r>=1 part of (8) with its amplitude replaced by |t|^(-2b)r^(-g), using z=r^A. This fixes the splitting convention and therefore the constants below.

Uniformly for t on the support and r>=1,

    (1+t^2r^q)^(-b)-|t|^(-2b)r^(-g)=O(r^(-g-q)).

The m-th s derivative of the difference integrand is bounded by C r^(j-2+Am-g-q)=C r^(-1-q), which is integrable. Lower derivatives have better powers. For r<1, the previous low-r bounds suffice, including the moment cancellation for the undifferentiated first trace. Therefore H_j is C^m near zero. Write h_a=H_j^(a)(0)/a!, so that

    H_j(s)=sum_(a=0)^m h_a s^a+o(|s|^m).                    (10)

This step isolates all potentially non-C^m terms in the single explicit tail P_j. It requires neither an infinite expansion nor any regularity of a variable-coefficient solution.

## The critical logarithm and finite constants

Let x=|s|>0. Substitution u=xz in (9) gives

    P_j(s)=K_j/A x^m integral_x^infinity u^(-m-1)F_epsilon(u)du.

Since Psi is smooth and compactly supported, F_epsilon is smooth and rapidly decreasing. Its Taylor expansion at zero has coefficients f_(a,epsilon). Define

    C_epsilon = integral_0^1 u^(-m-1)
                    [F_epsilon(u)-sum_(a=0)^m f_(a,epsilon)u^a]du
                 + integral_1^infinity u^(-m-1)F_epsilon(u)du
                 - sum_(a=0)^(m-1) f_(a,epsilon)/(m-a).        (11)

Both integrals converge absolutely. At zero the Taylor remainder is O(u^(m+1)); at infinity rapid decrease is more than sufficient. Integrating each subtracted monomial from x to 1 yields exactly

    P_j(s)=K_j/A [sum_(a=0)^(m-1) i^a M_a s^a/[a!(m-a)]
                   + i^m M_m s^m log(1/x)/m!
                   + C_epsilon x^m + O(x^(m+1))].             (12)

Indeed the omitted integral from 0 to x of the Taylor remainder is O(x), before multiplication by x^m. Adding (10) proves (1) with

    D_(j,epsilon)=h_m epsilon^m+(K_j/A)C_epsilon.              (13)

The lower coefficients agree with (3)-(4), since both are the actual derivatives of G_j through m-1. This proves the general critical asymptotic and the explicit constants.

If a C^m function is expanded through m-1 and divided by s^m, the quotient has a finite common limit from both sides. The logarithm in (1) prevents this if L_j is nonzero. With L_j=0, the two quotient limits are D_(j,+) and (-1)^m D_(j,-), so their inequality also prevents C^m. This proves the stated obstructions without asserting a converse.

## Even packets and existence of nonzero obstructions

For Phi=i phi with phi real and even, all odd M_a vanish and both G_j and H_j are even functions of s. If m is even, M_m=2i I_m, giving (5). Its prefactor is real and nonzero because j is odd and m is even.

For this imaginary-even choice, if m is odd then M_m=0 and h_m=0. General Phi with odd m can have M_m nonzero. In the even-data case (11) can equivalently be written as C_epsilon=integral_0^infinity u^(-m-1)[F_epsilon(u)-sum_(a=0)^(m-1) f_(a,epsilon)u^a]du: integrating the subtracted monomials on [1,infinity) gives exactly the last sum in (11). A direct cosine subtraction then gives the simpler leading coefficient. Subtract the Taylor polynomial through m-1 in the tail (9), combine positive and negative t, and use z=|s|t r^A. The cosine Taylor remainder in (7) is O(z^(m+1)) at zero and O(1+z^(m-1)) at infinity. After multiplication by z^(-m-1), both ends are absolutely integrable. The fixed positive t support is separated from zero. Fubini and dominated convergence then give (6). In particular no hidden order-m Taylor coefficient from H_j occurs, since H_j is even and C^m with m odd.

To prove the sign in (7), let n=(m-1)/2 and

    E_n(z)=cos z-sum_(k=0)^n(-1)^k z^(2k)/(2k)!.

E_0=cos z-1 is nonpositive and nonzero on an interval. For n>=1, E_n''=-E_(n-1), and E_n(0)=E_n'(0)=0. Twice integrating proves the constant weak sign (-1)^(n+1), and a nonempty interval of strict sign. The positive integration weight in (7) preserves that sign and gives a nonzero integral.

Finally,

    m-2b = m-g/(A-1) = -(m+j-1)/(A-1) <0.

Choose two nonnegative smooth bumps of equal positive integral on the positive half-line, with the support of the first entirely to the left of the second and both away from zero. Let phi be their difference there and extend it evenly. Then integral_R phi=0 and I_m>0, since t^(m-2b) is strictly decreasing. The resulting Phi has all the required properties. For even m, (5) is nonzero. For odd m, (6) gives equal nonzero one-sided constants, whereas (-1)^m=-1. Thus each case fails C^m, as asserted.

## Dependencies and scope

The density convention agrees with the independently checked packet in ../packet-dyadic-audit/PROOF.md. The argument above gives all trace convergence, beta coefficients, the first-trace logarithmic moment and critical asymptotics directly. The general two-dimensional finite expansion is in ../packet-expansion-audit/PROOF.md; it is not needed for this proof. The noninteger counterpart is in ../packet-axis-asymptotics/PROOF.md.

This is an integer axis theorem for a specified frozen packet. It neither constructs nor excludes a coupled admissible profile, establishes a full linearized kernel, gives a nonlinear family, nor changes either task endpoint. Review records and any exact checks belong in verification/. No numerical experiment is a proof of the asymptotic.

Actual Claude Opus5.5 completed its full review at2026-10-20T23:43:53.887480+00:00 with end_turn. It found no mathematical gap or factor/sign error. This verifier checked its reconstruction and added the optional explicit odd-m subtraction identity and parity qualification above. Its complete response and model metadata are saved under ../model-review/verification/packet_integer_axis_*. The exact checks and finite moment illustrations are separate evidence, not the proof.
