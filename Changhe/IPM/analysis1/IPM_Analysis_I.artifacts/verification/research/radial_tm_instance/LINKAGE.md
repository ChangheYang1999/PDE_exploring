# Same-runtime linkage of the forcing boxes

The closure review correctly distinguishes identical source code from identical
runtime arrays. The previous appeal to topic69 alone does not check the latter.
The following additional exact check discharges that finite linkage for the
three saved cells. It does not identify T with the canonical spline.

Write a(u,theta)=sum_m a_m(u) cos(2m theta), with m=0,...,259, and
rho=r^3 cos(theta)^2 sin(theta) a. The elementary identity

 cos(theta)^2 sin(theta) cos(2m theta)
 = [sin((1+2m)theta)+sin((1-2m)theta)
    +sin((3+2m)theta)+sin((3-2m)theta)]/8

gives each density sine coefficient H_j by collecting signed frequencies
2j+1. In particular H_0=(2a_0-a_2)/8. Acting with
partial_x=cos(theta) partial_r-sin(theta) partial_theta/r gives

 F_n=((4-2n)H_(n-1)+(4+2n)H_n+H'_(n-1)+H'_n)/2.

The same formula follows directly by expanding the Cartesian derivative of
x^2 y a and then collecting sine modes. For polynomial order k, collect every
repeated a_(m,k) and a_(m,k+1) symbol before taking interval magnitudes. If
weights w_l multiply independent intervals [m_l-r_l,m_l+r_l], their exact
minimal image is [sum w_l m_l-sum |w_l|r_l, sum w_l m_l+sum |w_l|r_l].
Every input and every output midpoint/radius is an exact dyadic rational.
Thus rational containment checks prove the whole T-box image is in the
saved F box. The independent check generates the angular weights by signed
frequency collection, not by calling the producer's modal map or topic69's
implementation. It checks all 3*261*8 coefficients, including zero boundary
modes and derivative orders. This proof precedes that implementation.

The result removes only the finite T-to-F linkage gap identified in the
closure review. T and A/B membership in the canonical trial, the other7806
cells and full-field inequalities remain OPEN.
