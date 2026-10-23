# Critical decay and the first moment in the full-plane inverse

Date: 2026-10-20. Status: CONFIRMED by independent proof and 108 full-plane manufactured checks at three quadrature levels (PASS 2026-10-20T19:22:47Z); actual Opus5.5 review pending. This is a theorem about the canonical inverse, not a transport profile or a nonexistence theorem.

## 1. Statement and conventions

Write X=(x,y), r=|X| and

    K(X)=(-xy/pi,(x^2-y^2)/(2pi))/r^4,
    Tf=-f e_2/2+PV integral_R2 K(X-Y)f(Y)dY.

Let f be smooth, even in x and odd in y. At infinity assume the bounds stated below with every fixed number of Cartesian derivatives. All integrals in this note converge at infinity without an exterior renormalization. The local principal value includes the displayed contact term. This is the same canonical IPM velocity as in ../inverse/PROOF.md: div(Tf)=0, curl(Tf)=-f_x and Tf=o(r).

(a) Suppose, for some delta>0 and a smooth angular function Theta with the density parities,

    f(r,theta)=r^(-3) Theta(theta)+O(r^(-3-delta)).        (1)

Every derivative of the error has the corresponding symbol bound. Put

    a_1=(1/pi) integral_0^(2pi) Theta(theta)sin(theta)dtheta.

Then

    Tf(X)=-pi a_1 log(r) partial_y K(X)+O(r^(-3)),        (2)

again with every derivative. In particular a_1!=0 prevents Tf=O(r^(-3)). If a_1=0, the conclusion Tf=O(r^(-3)) does hold.

(b) Suppose instead f=O(r^(-3-delta)), with the same derivative bounds. Its first moment

    mu=integral_R2 y f(X)dX

is absolutely convergent. Then

    Tf(X)=-mu partial_y K(X)+E(X),                       (3)

where, with every derivative,

    E=O(r^(-3-delta))       if 0<delta<2,
    E=O(r^(-5) log r)       if delta=2,
    E=O(r^(-5))            if delta>2.                   (4)

The estimates concern r>=2. In particular faster density decay does not imply equally fast velocity decay when mu!=0. The previously proved inverse estimate for degrees b in (-3,1) cannot be extended through b=-3 or below without moment information.

## 2. Proof at the critical exponent

Fix a large R and queries X=R Z in a fixed annulus 1<=|Z|<=2. Split the density with smooth radial cutoffs into |Y|<R/4, a middle annulus, and |Y|>4R. Intermediate transition annuli are included in the middle part. Radial cutoffs preserve parity.

In the inner part, Taylor-expand the separated smooth kernel:

    K(X-Y)=K(X)-DK(X)Y+O(R^(-4)|Y|^2).

The zeroth term integrates to zero by central oddness. The x moment vanishes by reflection in x. By (1), the y moment up to radius R/4 is

    integral_(|Y|<R/4) y f(Y)dY = pi a_1 log R+O(1).      (5)

The bounded error follows by integrating the remainder r^(-3-delta): its contribution to this moment has an integrable radial tail r^(-1-delta). A smooth transition in the radial cutoff changes (5) by O(1). The Taylor remainder is bounded by

    C R^(-4) integral_(|Y|<R/2) |Y|^2 |f(Y)|dY
       <= C R^(-4)(1+R)=O(R^(-3)).                      (6)

The middle part, after rescaling Y=R V, is a localized order-zero singular integral of a density with uniformly bounded smooth norm times R^(-3). The local subtraction at the query and the contact term therefore give O(R^(-3)); the same argument after differentiating gives every symbol bound. The exterior separated kernel contributes

    C integral_(4R)^infinity t^(-2)t^(-3)t dt
       =O(R^(-3)).                                     (7)

Derivatives of order j give the same estimates with the factor R^(-j), including derivatives of the cutoffs. Thus the sum equals -pi a_1 log R partial_y K(X)+O_Cj(R^(-3-j)) on the query annulus. Replacing log R by log r changes it by an O(r^(-3)) symbol because log(r/R)=log|Z| and all its derivatives are uniformly bounded on that annulus. This proves (2) without differentiating a sharp query-dependent integration boundary.

For clarity, the nonzero angular tensor in (2) is explicit:

    -pi partial_y K(r cos theta,r sin theta)
       =r^(-3)(cos(3theta),sin(3theta))
       =r^(-3)(cos(2theta)e_r+sin(2theta)e_theta).        (8)

Its Euclidean magnitude is r^(-3). This proves the asserted failure of an O(r^(-3)) bound when a_1!=0.

## 3. Proof below the critical exponent

The same inner expansion can now be taken through degree two. Both the degree-zero and degree-two moments vanish by central oddness. The Taylor error is

    C R^(-5) integral_(|Y|<R/2) |Y|^3 |f(Y)|dY.

The radial integral outside a fixed disk is at most C integral_1^(R/2) t^(1-delta)dt. This gives exactly the three alternatives in (4). Replacing the truncated y moment by the full mu contributes at most

    C R^(-3) integral_(|Y|>R/4) |Y| |f(Y)|dY
       <= C R^(-3-delta).

The middle and exterior pieces are O(R^(-3-delta)) by the estimates of Section 2 with the stronger density decay. The same rescaling and differentiated Taylor estimates prove the derivative bounds. This proves (3)-(4).

## 4. Explicit smooth manufactured fields

Take f_2=y(1+r^2)^(-2). Define

    I_2(r)=[log(1+r^2)+(1+r^2)^(-1)-1]/2,
    psi_2=-xy I_2(r)/r^4.

The removable value at zero is I_2(r)/r^4 -> 1/4, so psi_2 is smooth. The identity I_2'=r^3(1+r^2)^(-2) verifies -Delta psi_2=partial_x f_2 by differentiating a radial function times xy. Its rotated gradient is

    U_2,r=r^(-3) I_2 cos(2theta),
    U_2,theta=r^(-3)[I_2-r^4/(2(1+r^2)^2)]sin(2theta).

This smooth div-curl pair has sublinear velocity and the required parities, so canonical uniqueness identifies U_2=Tf_2. Since I_2=log r-1/2+O(r^(-2)),

    Tf_2=r^(-3)log r [cos(2theta)e_r+sin(2theta)e_theta]
          -r^(-3)[cos(2theta)e_r/2+sin(2theta)e_theta]
          +O(r^(-5)).                                  (9)

This is an explicit example of (2) with a_1=1. It satisfies the original density growth upper bound but fails transport.

For a faster-decaying example take f_3=y(1+r^2)^(-3) and

    psi_3=-xy/[4(1+r^2)^2].

Direct differentiation gives the same canonical identities and

    integral_R2 y f_3 dX = pi/4,
    Tf_3=(1/4)r^(-3)(cos(3theta),sin(3theta))+O(r^(-5)).  (10)

The moment follows from pi integral_0^infinity r^3(1+r^2)^(-3)dr=pi/4. The density is O(r^(-5)); its nonzero velocity still has degree -3. Neither field is asserted to satisfy stationary self-similar transport.

## 5. Consequences and scope

The second-term expansion in ../far_field_second_term/PROOF.md uses inverse weights strictly above -3, so these observations do not refute it. They identify a necessary extra step in any attempt to continue that argument through the critical weight: distinguish the first angular mode, retain a logarithmic term when it is present, and account for the finite moment below the threshold. We have not proved that a particular exact primary profile reaches such a term with a nonzero coefficient. Smoothness in Cartesian coordinates on the finite plane does not, by itself, assert smoothness after a far-field compactification.

The proof uses only the explicit canonical kernel, Taylor expansion, parity and integrable symbol bounds. Numerical manufactured tests verify its implementation independently; they are not used in the argument.
