# Largest outer-tangent disks centered on the negative axis

## Statement

Use the scalar homogeneous Holder space, the kernels, and the positive local measure mu_R of ../../../PROOF.md and ../../../../../01_setup/PROOF.md. Let 0<alpha<1. The two negative-axis lobes of the density Q_R contain the following explicit pair of disks.

Let sigma be the unique root in (0,1/3) of

    p(s)=2s^4-3s^2+4s-1=0,

and define

    c_*=(1-2sigma^2)^2/[2(1-2sigma+2sigma^3)],
    a_*=1-c_*.

Then 49/66<c_*<3/4 and 1/4<a_*<17/66. The disks centered at plus or minus c_*R on the negative kernel axis and of radius a_*R lie in the support of Q_R. They are largest in the family of disks centered on that axis, contained in one lobe, and internally tangent to the outer circle |z|=R. The claim is only about this family; no optimality among all submeasures or transport plans is asserted.

Their exact radial minorant about either disk center is

    w_*(r)=1/[2pi R^2(c_*+r/R)^2], 0<=r<=a_*R.

In all previously proved reflection formulas for such disks, one may use c=c_* and a=a_*. In particular, for s=R/h with 2a_*s<1 and h=|x-y|,

    |mu_R*f(x)-mu_R*f(y)|
        <= [1/2-alpha(1-alpha)J_*s^2
               -alpha(1-alpha)(2-alpha)(3-alpha)K_*s^4]
             h^alpha[f]_alpha,
    J_*=2 integral_0^(a_*) t^3/(c_*+t)^2 dt,
    K_*=(1/2) integral_0^(a_*) t^5/(c_*+t)^2 dt.

The full positive even-moment series in ../../all_even_moments/PROOF.md is also available after its independent acceptance. At every fixed admissible s these moments are largest in the stated disk family. For the retained-cutoff version 0<rho<1/2, subtract the same constant-density moments as in ../enlarged_exact_disks/PROOF.md with a=a_*; these are valid because the surviving radial density remains positive. This does not automatically improve every optimized global G radius: the condition 2a_*s<1 must still be checked.

## Geometry reduced to one variable

Scale R=1 and rotate the negative axis horizontally. A disk of radius a=1-c centered at (c,0) is internally tangent to the outer circle. With s0=sin(theta), 0<=theta<=pi/4, a point on the inner lobe boundary r=sin(2theta) has squared distance from (c,0), minus a^2, equal to

    P_c(s0)=2c-1-4cs0+4s0^2+4cs0^3-4s0^4
           =2c(1-2s0+2s0^3)-(1-2s0^2)^2.

The denominator v(s)=1-2s+2s^3 is positive on [0,1/sqrt(2)]. Indeed its minimum on that interval occurs at 1/sqrt(3), and equals 1-4/(3sqrt(3))>0. Therefore the condition that every inner-boundary point lie outside the open disk is equivalent to

    c>=H(s) for all 0<=s<=1/sqrt(2),
    H(s)=(1-2s^2)^2/[2(1-2s+2s^3)].

Direct differentiation gives

    H'(s)=-(1-2s^2)p(s)/v(s)^2,
    p'(s)=2+8(s-1/2)^2(s+1)>0.

Moreover p(0)=-1 and p(1/3)=2/81>0. Thus p has exactly one root sigma in (0,1/3), H increases up to sigma and decreases afterward. Its maximum on the full interval is precisely H(sigma)=c_*.

Since sigma<1/3 and H strictly decreases after sigma,

    c_*>H(1/3)=49/66>2/3.

The accepted strict containment proof for the c=3/4,a=1/4 disks in ../PROOF.md gives P_(3/4)(s)>0 on the whole compact interval. As v is positive, this implies max H(s)<3/4. Hence c_*<3/4 and the displayed bounds on a_* follow.

The disk with c=c_* avoids the open complement across the inner boundary. Its center belongs to the lobe, and it stays between the two boundary rays: a_*/c_*<1/2<1/sqrt(2), because c_*>2/3. Together with its outer containment and connectedness this proves containment in the closed lobe. Equality at an inner-boundary tangency affects only a set of planar measure zero. Central symmetry supplies the second disk. Conversely, for c<c_*, P_c(sigma)<0, so an inner-boundary point lies in the open disk and this disk is not contained in the lobe. This proves maximality within the stated family.

## Radial density and reflection moments

Because a_*<c_*/2, the density computation in ../exact_radial_density/PROOF.md applies without alteration. For t=r/R and the angular cosine v, the derivative of the scaled density is

    2t[-c_*^3+3c_*t^2+2t^3v]/[c_*^2+2c_*tv+t^2]^3<=0.

The angular minimum is its value at v=1, namely 1/(c_*+t)^2. This proves the radial minorant. Reflection in the direction of the output increment preserves that radial submeasure. The accepted symmetric concavity inequality and its fourth-order term therefore give the stated estimate with exactly these moments.

For any integer m>=0, the positive integral

    B_m(c)=integral_0^(1-c) t^m/(c+t)^2 dt

strictly increases as c decreases within the admissible family: the integration interval grows, and the integrand strictly increases on their common interior. Every coefficient of the accepted even-moment reflection series is positive. Thus c=c_* maximizes all these moment savings at once for a fixed s satisfying the displacement condition. This is a comparison of these explicit couplings only.

At cutoff radius rho, the removed constant-density bound is H_rho=1/[2pi(1-rho)^2]. The radial density is at least 1/(2pi rho^2)>H_rho, since c_*+a_*=1 and rho<1/2. The same positive retained radial weight proves the cutoff estimate. Its moments also increase as c decreases: the common integrand 1/(c+t)^2-rho^2/(1-rho)^2 increases and is positive throughout the enlarged interval.

## Dependencies and status

The only new geometry is the one-variable maximization proved above. The norm estimate uses the accepted positive-measure decomposition, reflection coupling and exact radial-density calculation. No decimal approximation to sigma is needed for the theorem. Numerical use must isolate sigma by rational signs of p, enclose c_* and the logarithmic moment formulas, and retain the displacement condition. Written before any numerical evaluation; OPEN pending independent lead cross-read.
