# A polynomial irrotational saddle example at every nonzero rotation

## Exact statement

For every c>0 and every real omega!=0, let J(x,y,z)=(-y,x,0). There is a real harmonic polynomial phi on R3 such that

    U=grad phi,
    B=(c I-omega J)y+U,
    P=-(1-2c)phi-((c I-omega J)y).grad phi-|grad phi|^2/2

solve the complete steady Euler profile equation

    (1-c)U+B.grad U+omega J U+grad P=0,  div U=0.

The local flow of -B has a compact nonsingular uniformly hyperbolic invariant set with a return map conjugate to the full two-sided two-symbol shift. In particular it supports an ergodic full-flow invariant probability with positive entropy and exponents (chi,0,-3c-chi), chi>0. The velocity is an unbounded nonconstant polynomial. The result does not assert an attractor, an SRB probability, a positive-volume basin, or a decaying profile. It gives no degree bound uniform as omega approaches zero.

This is an independent reconstruction of LIT47. Its relative source path and inspected version hash are in the team records. The earlier A225 construction covered one very large omega. The new argument keeps omega fixed and lets a separate geometric radius grow.

## 1. A robust planar return map

For 0<b<=1 put H_b(u,v)=(v,v^2-100-bu), and Q=[-13,13]^2. Suppose F is injective and a C1 local diffeomorphism on a neighborhood of Q, and each component and first partial derivative of F-H_b has absolute value less than epsilon, where epsilon<=b/10000. We verify a horseshoe directly.

For a sign sequence sigma in {-1,1}^Z, consider the complete metric space of sequences satisfying |u_i|<=13 and 8<=sigma_i v_i<=12, with difference norm max(sup|du_i|/5,sup|dv_i|). Writing F-H_b=(e1,e2), define

    u_i(new)=v_(i-1)+e1(u_(i-1),v_(i-1)),
    v_i(new)=sigma_i sqrt(100+v_(i+1)+b u_i-e2(u_i,v_i)).

The radicand belongs to [74.999,125.001], so the image lies strictly inside the same box. The two Lipschitz bounds in this norm are at most 0.2012 and

    (1+5b+6 epsilon)/(2 sqrt(74.999))<0.35.

Thus there is a unique fixed point. The equations say exactly F(u_i,v_i)=(u_(i+1),v_(i+1)). Successive contraction iterates have finite dependence on the code, and their errors decrease geometrically uniformly in the code. The index-zero point therefore depends continuously on the product-topology code. Injectivity of F makes this coding injective. Its compact image is invariant and the coding is a conjugacy.

At every coded point,

    DF=[[a,1+h],[-b+d,2v+e]],  |a|,|h|,|d|,|e|<epsilon.

Its determinant differs from b by at most 26 epsilon+2 epsilon^2, hence belongs to (0.997b,1.003b). The forward cone |du|<=|dv|/5 is mapped strictly inside itself: the second component expands by at least 16-epsilon-(b+epsilon)/5>15.79, and the first component divided by |dv| is at most 1+6epsilon/5. For the inverse derivative, the cone |dv|<=|du|/5 has dominant first-component expansion at least

    (16-epsilon-(1+epsilon)/5)/(1.003b)>15.

Its second-to-first ratio is less than 1/5. Nested forward and backward cones give complementary invariant lines with uniform expansion in their respective directions. This proves uniform hyperbolicity. All constants are uniform over the compact coded set; they need not be uniform as b approaches zero.

## 2. Harmonic controls for an area-preserving factor

The scalar multiple A_b=b^(-1/2)H_b is area preserving. With beta=b^(-1/2), it factors as

    L_b(u,v)=(beta v,-u/beta),
    S_b(u,v)=(u,v+sqrt(b)u^2-100/sqrt(b)),
    A_b=S_b composed L_b.

The map (u,v)->(v,-u) is the composition of vertical shear (u,v-u), horizontal shear (u+v,v), and vertical shear (u,v-u), in that order. Following this rotation by diag(beta,beta^(-1)) gives L_b.

Let a0=(u^2-v^2)/2, b0=uv, d0=u^2v-v^3/3 and D=diag(2,1/2). All three polynomials are harmonic, and direct differentiation gives

    D_*grad b0=(4v,u/4),
    D_*grad d0=(4uv,u^2/8-2v^2),
    (0,u)=(16/15)grad b0-(4/15)D_*grad b0,
    (v,0)=-(1/15)grad b0+(4/15)D_*grad b0,
    (0,u^2)=(16/15)grad d0-(8/15)D_*grad d0,
    (0,1)=grad v.

Here D_*V(x)=D V(D^(-1)x). In particular the first component of D_*grad d0 is 4uv. My earlier A225 proof displayed uv/2 in that position. Its coefficients were already correct; the displayed formula and a correction note have now been fixed.

Diagonal maps diag(beta,beta^(-1)) are exact time-log(beta) maps of grad a0. Each shear field above is a sum grad p+D_*grad q. Its time-one map is approximated by

    [D composed Phi_(grad q)^(1/n) composed D^(-1)
       composed Phi_(grad p)^(1/n)]^n.

To justify this without global completeness of the cubic-gradient flows, choose a compact neighborhood of all ideal shear trajectories from the compact input set. The integral ODE and its first k variational equations give a Ck local error O(n^-2) per step, because finitely many polynomial derivatives are bounded on a slightly larger compact neighborhood. Iteration and Gronwall give a Ck error O(n^-1). Stop at the first exit: the same position estimate excludes an exit for large n. The intermediate linear D and D^(-1) paths occupy another fixed compact set. This proves existence and convergence of the whole composition for the required input set.

There are finitely many factors, so this yields a finite composition A_approx arbitrarily Ck close to A_b on a neighborhood of Q, with all intermediate trajectories in a finite compact box. Place each factor into a positive time interval in (0,2pi), multiplying its harmonic potential to rescale time. Leave an initial and final interval with zero potential. The resulting piecewise constant harmonic polynomial potential Q(s,x), of degree at most three in x, has time-2pi map A_approx.

## 3. Prescribed dissipation

Now fix c>0 and omega>0 and set delta=3c/omega and b=exp(-2pi delta). Define

    q0(u,v)=delta(v^2-u^2)/4,
    q(s,x)=q0(x)+exp(-delta s) Q(s,exp(delta s/2)x).

The controlled equation x'=grad q-(0,delta v) has uncontrolled part -delta x/2. With x=exp(-delta s/2)z, its exact equation becomes z'=grad Q. Its time-2pi map is consequently sqrt(b) A_approx, as close to H_b as desired. No smallness assumption on delta was made.

The coefficients of q equal those of q0 near both ends of the time interval. Extend them periodically and take a sufficiently high Fejer mean coefficient by coefficient. This yields a real finite Fourier sum in s, still a harmonic polynomial of degree at most three in x. Fejer convergence in L1 time, and uniform coefficient bounds, give L1 time convergence in every required spatial Ck norm on the compact trajectory box. Integral ODE and variational estimates then give C1 return-map convergence; stopping at an exit gives existence on the whole interval. Choose the finite Fourier approximation so its return map differs from H_b by less than 2epsilon/3 in the norm from Section 1. The Fourier degree and coefficient sizes are now fixed, however large they may be.

## 4. Exact harmonic lift

Write this Fourier potential as q(theta,u,v)=sum_(|k|<=m) q_k(u,v)exp(ik theta). The q_k are harmonic polynomials of degree at most three, with the reality symmetry. For a radius R define

    w=(x^2+y^2-R^2)/(2R),
    E_k=((x+i y)/R)^k if k>=0,
    E_k=((x-i y)/R)^(-k) if k<0,
    F_R=sum E_k q_k(w,0),
    G_R=sum E_k partial_v q_k(w,0),
    Psi_R=sum_(j=0)^3 (-1)^j z^(2j) Delta_xy^j F_R/(2j)!
          +sum_(j=0)^2 (-1)^j z^(2j+1) Delta_xy^j G_R/(2j+1)!.

The two sums are added. The exact polynomial identity

    Delta_xy(E_k f(w))
      =E_k[(1+2w/R)f''(w)+2(|k|+1)f'(w)/R]

reduces the radial polynomial degree by at least one. Thus Delta_xy^4 F_R=0 and Delta_xy^3 G_R=0. Applying Delta_xy+partial_z^2 to the displayed finite sums telescopes, so Psi_R is real and harmonic.

In cylindrical coordinates r=R+u and z=v, w=u+u^2/(2R) and E_k=(1+u/R)^|k|exp(ik theta). Since m is fixed, these expressions converge with every fixed finite derivative on the chosen compact tube. The radial operator converges to partial_u^2. The limiting finite Cauchy-data formula is exactly q_k(u,v), by harmonicity and its degree bound. Therefore Psi_R(theta,R+u,v) converges to q(theta,u,v) in all required Ck norms, while partial_theta Psi_R/(R+u)^2 converges to zero.

## 5. The actual Euler field

Take

    phi_R=-c(x^2+y^2)/2+c z^2-omega Psi_R.

It is harmonic, and X_R=-B=omega Jy-3cz e3+omega grad Psi_R. The angular speed is omega[1+partial_theta Psi_R/r^2]. For sufficiently large finite R it is between omega/2 and 3omega/2 throughout the relevant tube. The exact transverse equation using theta as time is

    d(u,v)/dtheta
      =[grad_(u,v)Psi_R-(0,delta v)]
         /[1+partial_theta Psi_R/(R+u)^2].

It converges in C1 to the controlled equation of Section 3. A final stopped ODE estimate makes its return map less than epsilon/3 from that controlled map and ensures every input in a neighborhood of Q completes one turn. Uniqueness of this angle-parametrized ODE gives an injective local diffeomorphism. Section 1 supplies the horseshoe. Its complete orbits stay in a compact tube, so their original-time flow is defined for all positive and negative times even though no global completeness of a polynomial field is assumed.

Return times lie between 4pi/(3omega) and 4pi/omega. The fair Bernoulli shift measure suspends to an ergodic flow probability with entropy log(2) divided by its finite positive mean return time. The flow direction has exponent zero since X_R is bounded above and away from zero on the compact set. Transverse hyperbolicity gives exponents of opposite sign, and div X_R=-3c gives their sum. This is the asserted spectrum.

For any harmonic phi, differentiating the stated pressure uses A^T=cI+omega J and grad((Ay).grad phi)=A^T grad phi+D2phi Ay. Its gradient cancels the nonlinear term D2phi(Ay+grad phi). The remaining coefficient of U is (1-c)-(1-2c)-c=0, and the rotation terms cancel. Thus the complete Euler equation holds, with curl U=0.

A constant U would give an affine carrier whose backward flow contracts exponentially toward one equilibrium, hence no positive-entropy compact invariant set. Our U is nonconstant. A nonconstant polynomial vector field is unbounded, by restricting a nonzero leading homogeneous component to a suitable ray. This excludes the decay hypothesis of the campaign.

Finally the reflection R_-=diag(1,-1,1) satisfies R_-JR_-=-J. Composing phi with this reflection transfers the positive-omega example to the prescribed negative omega and conjugates the dynamics.

## Scope and dependencies

The proof uses polynomial differentiation, compact-set ODE estimates, finite Fourier approximation, the contraction theorem, cone hyperbolicity and the standard entropy formula for a suspension with a bounded positive roof. No numerical search, remote computation or recent preprint existence theorem enters. The construction rules out a universal local zero-entropy assertion for irrotational profiles at any nonzero rotation. It leaves the decaying-profile conjecture and any obstruction specific to an irrotational SRB measure OPEN.
