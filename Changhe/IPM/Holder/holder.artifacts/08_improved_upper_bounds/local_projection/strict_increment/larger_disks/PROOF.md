# A larger inscribed disk and a stronger projection saving

## Statement

Retain the measure, homogeneous Holder space and operator conventions of ../PROOF.md. At increment length h and local radius R=h/2, put

    eta_star(alpha) = (7/18432) alpha(1-alpha) (5/4)^(alpha-2).

For 0<alpha<1, the proposed stronger bound is

    |mu_(h/2,beta)*f(x)-mu_(h/2,beta)*f(y)|
       <= (1/2-eta_star(alpha)) h^alpha [f]_alpha,
    |x-y|=h.

This improves the eta_alpha in the parent note and is uniform in beta, for real or complex inputs. It is conditional on an independent cross-read. No decimal value is asserted here.

## Exact disk containment

Set h=1 and R=1/2. On each negative kernel lobe, Q has density |cos(2(theta-beta))|/(2 pi r^2), supported where R|sin(2(theta-beta))|<=r<=R. Let n be its negative axis. We use the disks of radius epsilon=1/8 centered at +/-r_0 n, where r_0=3/8. They lie inside the radius-1/2 disk. Their angular deviations d from the corresponding axis satisfy |sin d|<=epsilon/r_0=1/3, so they lie strictly inside the negative angular lobes.

It remains to show that a selected disk does not intersect the interior radial boundary. Normalize lengths by R. The disk has center (3/4)n and radius 1/4. The radial boundary in a half-lobe is r/R=sin(2d), with 0<=d<=pi/4. Put s=sin d, so 0<=s<=1/sqrt(2)<3/4. The squared distance from this boundary point to the normalized disk center, minus (1/4)^2, is exactly

    p(s) = 1/2 - 3s + 4s^2 + 3s^3 - 4s^4.

For t=s-1/3, direct expansion gives

    p(s) = 1/162 + (2/27)t + t^2(13/3 - (7/3)t - 4t^2).

Since -1/3<=t<=5/12, the concave quadratic in parentheses is at least the smaller of its endpoint values, namely 8/3. Completing the square therefore gives

    p(s) >= 1/162 + (2/27)t + (8/3)t^2 >= 11/1944 > 0.

The boundary reflected across the axis has the same distance. The center belongs to the Q support, and every radial boundary point lies strictly outside the disk. The disk is connected and does not meet the sector edges. Hence it lies on the same side of the radial boundary as its center and is contained in the Q support, except for the harmless outer-circle tangency.

Throughout each selected disk,

    |cos(2(theta-beta))| >= 1-2/9 = 7/9,
    q >= (7/9)/(2 pi (1/2)^2) = 14/(9 pi) = c_star.

The two disks are disjoint. Remove the positive measure c_star times area on each disk and leave the remaining measure and identity atom to the translation coupling.

## Coupling cost

Use exactly the reflection coupling from ../PROOF.md on each removed uniform disk. With epsilon=1/8, the evaluation displacement has length 1-2u_1 in [3/4,5/4]. The same second-derivative estimate and the identity E[u_1^2]=epsilon^2/4 yield the saving

    c_star pi epsilon^4 alpha(1-alpha)(1+2epsilon)^(alpha-2)
      = (7/18432) alpha(1-alpha)(5/4)^(alpha-2).

Scaling gives the factor h^alpha. All marginal and convergence arguments are unchanged. To compare the two gains, their ratio is

    [(7/18432)/(82/321489)] (45/44)^(alpha-2),

which is at least [(7/18432)/(82/321489)](44/45)^2>1. Thus the displayed saving is strictly larger at every admissible exponent. This argument was written before any numerical evaluation or use in an operator table.
