# Balanced residual on the middle arcs

## Statement and scope

Let 0<alpha<1 and let f be real-valued on R^2 with homogeneous Holder seminorm [f]_alpha<=1. The planar trace-free kernel at phase phi is K_phi(z)=Re(e^(i phi)/z^2)/(2 pi), with circular principal values and the extension modulo constants by convergent increments. Put x=1/2, y=-1/2 and G(z)=z/[pi(z^2-1/4)^2]. The middle region E consists of |z|<1 outside both open disks B_(1/2)(x), B_(1/2)(y). No singularity lies in E.

Use the coordinates and extracted cell masses of ../PROOF.md: r=sin t, 0<t<pi/2, z(t,s)=r exp(i(pi/2+ts)), -1<=s<=1, and w_phi(t,s)=t sin t cos t Re(e^(i phi)G(z(t,s))). Fix a t-bin [a,b] and fixed signed extracted masses m_j, satisfying the sign and domination hypotheses of the parent theorem. Write S=sum_j m_j and suppose the variation of the residual on the upper arc is at most tau, uniformly on this bin.

Define

    J(s)=log(1+8s)+8s(1-4s)/(1+8s),     0<=s<=1,
    M_phi(t)=-(2/pi) sin t cos t sin(phi) J(sin^2 t),
    q(t)=M_phi(t)-S.

The residual contribution, together with its negative central reflection, is bounded in absolute value by

    tau (2 sin^2 t)^alpha
      + |q(t)| [(2 sin t)^alpha-(2 sin^2 t)^alpha]                 (1)

at each t, with |q(t)| replaced by min(tau,Q) whenever Q>=|q(t)|. In particular an outward computable bin bound is

    (b-a) [tau A + min(tau,Q)(B-A)],                              (2)
    A=(2 sin^2 b)^alpha,   B=(2 sin b)^alpha,

provided Q bounds |q(t)| on [a,b]. This is no larger than the old antipodal bound (b-a)tau B. The extracted transport plans and all other regions are unchanged. Thus any valid replacement lowers, or preserves, the complete upper bounds for both C_alpha and D_alpha obtained with the parent middle-circle certificate.

## Proof of the geometric estimate

At fixed t, let sigma be the signed residual on the upper arc. Its variation V is at most tau and its signed mass is q. Its positive and negative masses are (V+q)/2 and (V-q)/2. Couple the smaller of these masses within the upper arc, and do the same for the negative central reflection of sigma on the lower arc. The diameter of either arc is 2r sin t=2 sin^2 t because its angular width is 2t<=pi. The total mass transported in these two couplings is V-|q|. The uncoupled mass on the upper arc has one sign and total variation |q|; pair it with its negative reflected copy at distance 2r. The resulting Holder cost is

    (V-|q|)(2 sin^2 t)^alpha+|q|(2 sin t)^alpha.

Both coefficients of V and |q| in the rearranged expression are nonnegative. Substituting V<=tau proves (1). The coupling can be implemented by product measures after normalizing the balanced positive and negative pieces; the one-signed remainder is reflected. Equivalently the inequality follows directly by applying the Holder inequality to these product measures, so no measurable selection of couplings as t varies is needed.

For (2), first bound the two transport distances separately by 2 sin^2 b and 2 sin b. This gives (V-|q|)A+|q|B, with nonnegative coefficients, and then substitute V<=tau and |q|<=min(tau,Q). Integrate on [a,b]. This argument avoids replacing the difference of two increasing distance powers by the difference of their upper bounds without justification.

## Proof of the signed-mass formula

The signed upper-arc mass before extraction is

    integral_(-1)^1 w_phi(t,s) ds
      =r cos t Re[e^(i phi) integral_(pi/2-t)^(pi/2+t) G(r e^(i theta)) dtheta].

On the open upper half-plane take

    F(z)=-2z/(z^2-1/4)+4 atanh(2z).

Here atanh is its analytic branch inherited from the principal logarithms on the upper half-plane. Direct differentiation gives F'(z)=1/(z^2-1/4)^2. The arc endpoints are z_R=r^2+i r cos t and z_L=-conj(z_R). The branch satisfies F(z_L)=-conj(F(z_R)); therefore

    integral G(r e^(i theta)) dtheta
      =[F(z_L)-F(z_R)]/(i pi)=2i Re F(z_R)/pi.

For s=r^2, elementary real arithmetic gives

    |z_R^2-1/4|^2=(1+8s)/16,
    Re[-2z_R/(z_R^2-1/4)]=8s(1-4s)/(1+8s),
    |1+2z_R|^2=1+8s,     |1-2z_R|^2=1.

Consequently Re[4 atanh(2z_R)]=log(1+8s), so Re F(z_R)=J(s). Taking the real part after multiplication by e^(i phi) proves the formula for M_phi. Endpoint values follow by continuity. Subtracting the fixed extracted signed mass S proves the formula for q.

## Numerical implementation and acceptance conditions

An interval evaluation of the displayed real formula on [a,b] supplies Q without complex logarithm branch choices. The old mass rule must be replayed with its original precision and fixed integer unit, preserving the original extracted masses and the original residual summands. The proof does not allow changing a transport marginal without rechecking its plan. The previous residual lower endpoint is subtracted from the previous upper bound and the new residual upper endpoint added. Exact source hashes, row coverage and the rounding of every final endpoint must be retained. A numerical result is not asserted by this proof before those checks.

Dependencies: the parent's coordinate decomposition, certified cell domination and extracted transport bounds; the original local and exterior upper bounds; the existing phase interpolation theorem. This proof concerns only the middle-region Holder functional and makes no PDE claim. Independent analytic cross-read is pending.
