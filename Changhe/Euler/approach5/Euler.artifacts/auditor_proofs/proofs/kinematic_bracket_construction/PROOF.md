# Global decoupled bracket construction

## Exact audited statement

For every 0<c<1/2, every finite real omega, and every integer j>=1, there exist a smooth compactly supported divergence-free U on R^3 and a nonzero C^j vector field W such that, for B=(cI-omega J)y+U,

    [B,W]=-(1+c)W, div W=0, |W(y)|=O(|y|^(-1/c)).

There is a smooth compact genus-two handlebody H which is strictly trapping for -B, on a neighborhood of which W is smooth and nowhere zero. On H the W direction contracts under the -B flow at rate 1+c, with uniform two-sided norm constants. The return map described below has a uniformly expanding one-dimensional quotient. The entire global W is not asserted C^infinity.

This confirms the constructive core of CO6. No Euler pressure is constructed, W is not curl U, and this is not a profile counterexample. No separate mixing, transitivity, or complete attractor classification is asserted.

The source construction is in the team records. The following is a complete independent audit of the gluing, regularity and global scope, including the boundary and topology issues absent from a parameter-only check.

## 1. Local model, rates and return footprints

Use X=-B, a=1+c, d=3c and k=1-2c=a-d. Choose

    b=(a+k)/2, L=b+k, q=b/L,
    K=(2+1/q)/2, T=log(K*q)/k, rho=exp(-a*T),
    delta=(1-rho)/4,
    epsilon=min(delta,1/K-1/2)/2,
    m=(rho*(1+2*delta)+1+delta)/2.

Then 0<k<b<a, L-a-b=-d, 1/2<q<1, 1/q<K<2 and T>0. Also epsilon<delta, K*(1/2+epsilon)<1 and

    rho*(1+2*delta)<m<1+delta.

For the last inequality, 1+delta-rho*(1+2*delta) is at least 1-rho-delta>0.

On a neighborhood of the box

    C={|x|<=1, -epsilon<=z<=1, |y|<=z+delta}

put X=(L*x,-a*y,-b*z), W=partial_y and use Euclidean volume mu. Then L_X mu=-d*mu and [X,W]=a*W. The two x faces are exits. The top and bottom z faces are incoming. On a sloping y face, the derivative of its outward defining function is -(a-b)z-a*delta, strictly negative since z>=-epsilon and epsilon<delta.

Identify the exit faces with disks having coordinates (y,z), and return them to z'=1 by

    P_+(y,z)=( K*(z-1/2), rho*y-m+rho*(z+delta), 1),
    P_-(y,z)=(-K*(z-1/2), rho*y+m-rho*(z+delta), 1).

Both images are strictly inside the top face. Their x magnitudes are less than one. The first y interval is [-m,-m+2*rho*(z+delta)], the second its reflected counterpart. The first upper endpoint is less than rho and the first lower endpoint is greater than -1-delta; the other interval satisfies the reflected bounds. If two image points have the same x', their old z coordinates sum to one; the gap between their y intervals is 2*m-2*rho*(1+2*delta)>0. Thus the images are disjoint embedded disks with a positive margin.

The section-tangent field satisfies DP_pm W=rho*partial_y'. Flux densities have magnitudes L*dy*dz on exits and b*dx'*dy' at the top. The map Jacobian has magnitude K*rho, and

    b*K*rho=L*exp(-d*T),

because q*K=exp(k*T). Choosing orientations by flow direction makes this an equality of signed flux forms.

## 2. Return tubes and their lateral boundaries

In flow coordinates (t,p), where p lies on an exit disk, define on each tube

    X=partial_t, mu=exp(-d*t) dt wedge nu_exit,
    W=exp(a*t) partial_y.

At t=T, the identities in Section 1 match both the flux and the full tangent vector W. Extend the section map to collars by the two flows. Uniqueness of transport then matches mu and W throughout the collars, not merely at their interfaces. Hence all normal derivatives agree and the glued fields are smooth.

A product tube would have tangent lateral boundary, so the boundary must actually be adjusted. In the core's exit flow coordinates, for small negative t the allowed transverse disk is

    -epsilon*exp(b*t)<=z0<=exp(b*t),
    |y0|<=delta*exp(a*t)+z0*exp((a-b)*t).

The lower z side decreases, the upper side increases, and the derivative of the last upper bound is at least (a*delta-(a-b)*epsilon)*exp(a*t)>0. Thus these disks are strictly increasing toward the exit. Continue that motion smoothly into a slightly increasing family along each tube, reducing its speed after a small collar. The total enlargement can be arbitrarily small. The positive endpoint margins proved above leave room for the enlarged return footprints. X then points strictly inward along each lateral boundary.

Round the remaining corners between strictly incoming faces using a smoothed maximum of local defining functions, with nonnegative derivatives in its arguments. Their strict negative X derivatives are preserved. The resulting H is a smooth strictly trapping handlebody. Abstractly it is a ball with two 1-handles. The vector W is smooth and nowhere zero throughout a neighborhood of H. Since H is compact, exact transport gives, for t>=0,

    D F_t W(p)=exp(-a*t) W(F_t p), F_t=flow of X,

with uniform two-sided norm bounds on this direction.

For points entering at z=1 with x!=0, local exit time is -log|x|/L and z_exit=|x|^q. The quotient return map is f(x)=sign(x)*K*(|x|^q-1/2), apart from the harmless assignment of signs to branches. Its derivative magnitude is K*q*|x|^(q-1)>1. This is the asserted expanding Lorenz-type quotient; no classification theorem is being invoked.

## 3. Filling the handles without a cutoff of W

Choose disjoint attaching annuli on the boundary of the standard genus-two handlebody, each core crossing its corresponding 1-handle once and missing the other handle. Attach a 2-handle along each. Each attaching circle meets its 1-handle belt circle transversely once, so the corresponding 1/2-handle pair cancels. Doing this successively leaves a ball. This is the standard smooth handle-cancellation fact, in dimension three with its exact intersection hypothesis. The annular coordinate changes below are isotopic to the chosen attaching maps, so they preserve that cancellation.

On each 2-handle D={|u|<=1, |v|<=1}, choose lambda=k/(j+3), h=d+2*lambda and

    X_D=(lambda*u1,lambda*u2,-h*v),
    mu_D=kappa du1 wedge du2 wedge dv.

The cylindrical side exits and the two caps enter. Divergence is -d. The side flux is kappa*lambda*dtheta*dv. Orient the chosen annulus by the incoming X direction, opposite its outward boundary orientation. In any such annular coordinates its flux is f(theta,z)dtheta*dz with f>0. Put F(z)=integral_0^(2*pi) f(theta,z)dtheta and M=integral_-1^1 F(z)dz, and choose kappa=M/(4*pi*lambda).

Determine z(v) by integral_-1^z F(s)ds=M*(v+1)/2, and theta'(theta,z) by integral_0^theta' f(s,z)ds=F(z)*theta/(2*pi). Both are smooth diffeomorphisms, and their combined pullback flux is exactly M/(4*pi)dtheta*dv. They remain in the prescribed attaching isotopy class. This verifies signed flux compatibility, not only equality of total area. Gluing flow collars now matches X and mu smoothly.

Transport the already defined full vector W into D from its outgoing side. If r=|u|>0, the exit time is tau=log(1/r)/lambda and exit point is (u/r,v*r^(h/lambda)). With G the smooth side vector in fixed Cartesian components,

    W_ui=r^(a/lambda+1) G_ui(u/r,v*r^(h/lambda)),
    W_v =r^((a-h)/lambda) G_v(u/r,v*r^(h/lambda)).

These formulas use the derivative of the fixed-time flow, not the derivative of the variable exit map. They therefore transport normal as well as tangential components correctly. Here (a-h)/lambda=j+1 and h/lambda>2. Each transverse derivative of the composed smooth G costs at most a factor r^(-1), while each v derivative gains r^(h/lambda). Derivatives of W of total order at most j consequently tend to zero at r=0. Defining W=0 on that axis gives C^j regularity. For j=1 the explicit estimates are W=O(r^2), DW=O(r). The bracket equation holds on the axis by continuity, since W and DW vanish there.

The prescribed field agrees in the full attaching collar. Every point with r>0 reaches that collar in finite X time; only the stable axis fails to exit. Thus there is no unexamined basin interface in this extension. After both attachments, round the remaining incoming corners as before. We obtain a smooth compact ball N, smooth X and mu, and C^j W, with the original nonzero field on H preserved.

## 4. Euclidean volume and the fixed exterior linear field

Set B=-X and V=integral_N mu. Choose R by 4*pi*R^3/3=V. The outgoing boundary flux nu=i_B mu has integral d*V=4*pi*c*R^3. A boundary diffeomorphism psi to S^2 therefore can be chosen with

    psi^*(c*R^3 dS)=nu.

To justify this, start from a smooth ball identification and apply the equal-total-volume Moser argument on S^2; its correcting diffeomorphism is isotopic to the identity. In outward B-time s the collar volume is exp(d*s)ds wedge nu. The map

    (s,p) -> R*exp(c*s)*exp(-omega*J*s)*psi(p)

pushes B to (cI-omega J)y and pulls Euclidean volume back to mu exactly. The boundary isotopy and collar uniqueness let this map extend to a smooth ball diffeomorphism f0. Its volume pullback equals mu near the boundary and has the same total volume.

For completeness, the relative volume correction uses a compactly supported two-form eta with d eta=f0^*(dy)-mu. Such eta exists because this top-degree difference has integral zero. In interior R^3 coordinates it can be built by successive one-variable integrations: subtract a fixed compact bump times each fiber integral before integrating, and use zero total integral in the last variable. All primitives then have compact support. For mu_t=(1-t)mu+t*f0^*(dy), solve i_Zt mu_t=-eta. Its compactly supported flow ht satisfies h1^*f0^*(dy)=mu and is the identity near the boundary. Thus f=f0 composed with h1 is the required relative correction. This does not alter the exterior collar or the bracket identity.

Push the fields forward by f and extend B by (cI-omega J)y outside the ball. The extension is smooth because equality already holds on a collar. U=B-(cI-omega J)y is smooth and compactly supported, with div U=0. On the exterior write y=R*exp(c*s)*exp(-omega*J*s)*theta and set

    W(y)=exp(-s)*exp(-omega*J*s)*W(R*theta).

This is precisely the bracket transport formula there. It agrees on the common collar, preserves C^j regularity including zero curves, and gives O(r^(-1/c)) decay. Nonvanishing on the interior H is unchanged by a diffeomorphism.

## 5. Divergence, volume and exact scope

The B-flow is complete and has bounded backward orbits, since it is linear outside a ball and strictly outward there. Constant Jacobian and the bracket transport give

    div W(Phi_s p)=exp(-(1+c)*s) div W(p).

This identity follows by transformation of divergence under the flow, requiring only W in C1, not second derivatives of W. For s tending to minus infinity the left side stays bounded on the compact backward orbit. Hence div W(p)=0.

More generally, for any continuous nonzero eigenfield with the invertible transport law, O={W!=0} is a nonempty open invariant set. If its Lebesgue measure were finite, invariance and the Jacobian exp(3c*s) would give |O|=exp(3c*s)|O|, impossible for s!=0. Thus |O| is infinite. In particular W cannot be curl U in the constructed example: curl U is compactly supported. The same observation shows that every nonzero decaying actual profile has an infinite-volume vortical set, since curl-free decaying divergence-free fields are zero.

The exact primitive two-form identities that follow from div W=0 and its bracket law remain available for an arbitrary primitive beta of i_W volume. They do not identify beta with U flat and therefore do not supply the Euler energy law. Writing a literal convergent Biot-Savart integral in the general target class would require an additional convergence justification; the differential coupling W=curl U is the essential missing condition.

The construction is an obstruction to arguments using only the stated finite-regularity bracket, decay and divergence assumptions. It does not refute an argument that uses W=curl U, does not construct a C-infinity W at the added axes, and does not by itself prove a general classification of the invariant set inside H.
