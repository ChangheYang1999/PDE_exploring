# A logarithmic obstruction at the Lipschitz endpoint

## Statement and scope

Let E_(2,1) denote the physical parity space of bounded globally horizontally Lipschitz functions with h(0,y)=0 and finite norm

 ||h||E_(2,1)=||h||infinity+[h]_x,Lip+[h]_(y,2,Lip),
 [h]_(y,2,Lip)=sup |h(x,y)-h(x,y')|/(x^2|y-y'|).

Let rho0 be the exact joined normalized modal trial, P=(p,0) its positive source, V(P)=0 its actual transport zero, and g=rho0_y(P)>29. Put T=V.grad-1. There are compact smooth physical-parity inputs h_epsilon, supported in fixed neighborhoods separated from the physical vertical axis and origin, with

 J(h_epsilon)=c[h_epsilon]=0,
 ||h_epsilon||E_(2,1)+||T h_epsilon||E_(2,1)<=C,
 ||U[h_epsilon].grad rho0||E_(2,1)
       >=c1 log(1/epsilon)-C,                       (1)

where c1>0 and C are independent of epsilon. Every input and image for each positive epsilon is smooth on the source disks and belongs to the indicated space. With a weighted L2 factor L2((1+r^2)^(-gamma/2)), 4k<gamma<2, the same bounded inputs and transport images still give (1), and their complete actual coupling images belong to that weighted space for each epsilon.

Thus the bounded-coupling argument on E2 for alpha<1 cannot extend to alpha=1, even as a bound from the smooth transport graph, and even after exact strain and cubic normalization. The same construction applies to a source extension equal to the actual coefficients near P. The limiting compact Lipschitz input belongs to the maximal transport domain, but its full image is not Lipschitz, so the maximal transport domain is not contained in the maximal domain of the full expression at this endpoint. No reverse inclusion is asserted.

There is a complementary normalization fact. On compact smooth E_(2,1) inputs,

 |J(h)|<= [h]_(y,2,Lip).                             (2)

The cubic functional consequently has a unique bounded extension to the E_(2,1)-closure of that smooth class. On this closure the extension is the actual limit h(x,y)/(x^2y) as (x,y)->0 away from the axes. This is not a claim that every large Lipschitz-space element has a cubic jet, or that an endpoint full inverse exists or fails on every possible domain. It explains the specific obstruction to obtaining both bounded coupling and cubic-trace control by simply taking alpha=1.

## Source-centered smooth annular inputs

Use local coordinates Z=(s,y)=X-P. Proof 209 certifies an analytic disk about P of radius 1/1000. Fix a smaller radius d>0 whose closed disk is disjoint from its x-reflection and the physical vertical axis. Only C2 density and C^(1,1) transport regularity on this disk are needed here. Choose a smooth radial cutoff chi, equal1 on r<=d/2 and0 on r>=d. Choose a smooth radial kappa, equal0 on r<=1 and1 on r>=2. On the positive-source disk set

 f_epsilon(P+Z)=kappa(|Z|/epsilon)chi(|Z|)
                              |Z| sin(3 arg Z).    (3)

Take 0<epsilon<d/8 and extend by zero. The angular homogeneous function is

 |Z|sin(3 arg Z)=3y-4y^3/(s^2+y^2).

It is smooth away from0, homogeneous of degree1, and has bounded first derivatives there. Its second derivatives have size O(1/|Z|). The inner cutoff makes (3) compact and smooth everywhere. Direct differentiation of its rescaled cutoff gives, uniformly in epsilon,

 ||f_epsilon||infinity+||D f_epsilon||infinity<=C,
 |D^2 f_epsilon(Z)|<=C/(|Z|+epsilon).               (4)

The last estimate includes the transition annulus epsilon<=|Z|<=2epsilon. Reflect this packet evenly in the physical x coordinate and add the copy. Each packet is odd in y, so the sum u_epsilon has both required parities. It vanishes near both physical axes except the horizontal one, on which oddness supplies zero; its support is separated from x=0 and the physical origin. In particular J(u_epsilon)=0.

The norm comparison on a fixed compact support away from x=0 turns the uniform ordinary Lipschitz bound (4) into a uniform E_(2,1) bound. All weighted L2 norms of u_epsilon are uniformly bounded as well.

Near P the actual field is smooth and V(P)=0, so |V(P+Z)|<=C|Z| and |DV|<=C. Differentiation gives

 D(T f_epsilon)=(DV)^T D f_epsilon
                       +(V.grad)D f_epsilon-D f_epsilon.

The first and last terms are uniformly bounded by (4); the second is bounded by C|Z|/(|Z|+epsilon). This proves a uniform Lipschitz and supremum bound for T f_epsilon, with compact support. The reflected source has the same property by symmetry. Hence u_epsilon has uniformly bounded transport graph norms, not merely input norms.

## The exact logarithm in the velocity derivative

At P the local packet vanishes on a disk of radius epsilon, so all velocity derivatives there are ordinary separated kernel integrals. The derivative kernel from proof 218, now centered at P, gives exactly

 partial_y U2[f_epsilon](P)
 =(1/pi) integral sin(3theta)r^(-3)
              [kappa(r/epsilon)chi(r)r sin(3theta)]r dr dtheta
 =integral_0^infinity kappa(r/epsilon)chi(r) dr/r.    (5)

The angular integral is pi. Since both cutoffs equal1 for 2epsilon<=r<=d/2, (5) equals log(1/epsilon)+O(1), with an epsilon-independent error. More explicitly its difference from integral_(2epsilon)^(d/2) dr/r is supported in [epsilon,2epsilon] and [d/2,d], where the integral of1/r is bounded independently of epsilon.

The reflected packet is a fixed positive distance from P. Its contribution to this derivative is uniformly bounded by its supremum and compact support. The same holds for every fixed smooth correction supported away from the source disks. Also |U[u_epsilon](P)| is bounded uniformly: the local singular kernel integrated against a function of size Cr has radial bound C dr, and the separated pieces are bounded.

The physical central strain c[u_epsilon] is uniformly bounded because its physical-origin kernel is smooth on this fixed support. Choose a fixed smooth compact physical-parity q with c[q]=1, J(q)=0, supported away from both source disks and both physical axes. Define

 h_epsilon=u_epsilon-c[u_epsilon]q.                 (6)

The coefficient is bounded independently of epsilon. Therefore (6) preserves the input and transport graph bounds, gives exact c=J=0, and changes (5) and the source velocity value by only bounded quantities.

At P the density is odd in y, so rho0_x(P)=0, rho0_yy(P)=0, and U2[h_epsilon](P)=0. Differentiating the coupling at P gives

 partial_y(U[h_epsilon].grad rho0)(P)
       =g partial_y U2[h_epsilon](P)
                       +rho0_xy(P)U1[h_epsilon](P)
       =g log(1/epsilon)+O(1).                     (7)

The ordinary derivative exists for every epsilon. For a smooth output its weighted vertical Lipschitz seminorm is at least the absolute value of (7) divided by p^2. Thus (1) holds with c1=g/p^2 after increasing C. The normalization column vanishes exactly by c[h_epsilon]=0. The transport image itself is zero near P, because the input and correction vanish there, so it cannot cancel (7).

For each epsilon the input is compact smooth. Its canonical velocity is smooth near every finite point and has a decaying multipole tail. The actual density has C^(4,1) origin regularity, C6 radial joins, and the far coefficient bounds of proof 214 (10). Multiplication by its gradient therefore preserves the bounded divided first derivatives needed for E_(2,1); the velocity has the physical parities and is smooth near the physical origin. Exact c=0 removes its linear strain, although mere membership would also hold with the linear term. At infinity the odd-y compact input has zero mass, so its canonical velocity is O(r^(-3)), while grad rho0=O(r^(k-1)). This suffices for weighted square integrability whenever gamma>2k-6. In particular it suffices on the stated common-space range 4k<gamma<2. That common-space range is chosen to match the other theorems, not asserted to be a necessary integrability condition for these individual compact inputs. No sharp threshold for each example is claimed. These checks establish full image membership for every epsilon; the claim is divergence of their norms, not undefined images.

## The limiting input and the domain distinction

Remove kappa from (3), keep the outer cutoff, and give the value0 at Z=0. The resulting f0 is compact Lipschitz by homogeneity. Reflect and subtract its physical strain multiple of q as above to get h0 with c=0 by its exact scalar correction and J=0 because it vanishes near the physical origin. The strain integral is absolutely convergent on this compact support. The same estimates for V.grad f0 and its weak derivatives hold away from P; the continuous homogeneous degree-one expression extends across P, with a bounded Lipschitz norm. Equivalently approximate by (3), pass locally uniformly in the transport expressions using their uniform Lipschitz bounds and identify the distributional derivative. Thus h0 belongs to the maximal E_(2,1) transport domain.

The source singular part can be computed exactly by a local potential. Since

 Delta[r^3 log(r)sin(3theta)]=6r sin(3theta),

a local solution of -Delta Phi=f0 is

 Phi_sing=-(1/6)r^3 log(r)sin(3theta).

The contribution of the outer cutoff and the reflected/correcting sources is smooth on a smaller disk. For U2=partial_s^2 Phi, the logarithmic part is

 U2[h0](P+Z)=-y log r+O(r),                         (8)

where the O(r) remainder is a homogeneous degree-one smooth angular function plus a smooth field. It has bounded derivatives away from0. Formula (8) follows by differentiating the polynomial r^3 sin(3theta)=3s^2y-y^3 twice in s. Similarly U1 has logarithmic part s log r. Since rho0_x(P+Z)=O(r) and rho0_y(P+Z)=g+O(r), the coupling has leading term -g y log r plus terms with bounded first derivatives on a smaller disk. Its vertical difference quotient along s=0 diverges as r tends to0. The compact correction is smooth there and cannot change this. Thus the full image of h0 is not E_(2,1), proving the claimed non-inclusion of the transport domain in the full-expression domain.

## The cubic functional at alpha=1

For every smooth physical-parity h with h(0,y)=0, two integrations in x and one in y give a smooth factorization h=x^2y b(x,y) near0, with b(0,0)=J(h). Oddness in y and the weighted Lipschitz seminorm yield

 |h(x,y)|<= [h]_(y,2,Lip) x^2|y|.

Divide by x^2|y| and take the limit to prove (2). The same inequality applies to differences of two such inputs. Hence their J values are Cauchy whenever the inputs are Cauchy in E_(2,1), proving the unique bounded extension on the closure.

To identify it with a genuine cofactor limit there, approximate h by smooth h_j in this norm. Uniformly for x,y nonzero,

 |h(x,y)/(x^2y)-h_j(x,y)/(x^2y)|
       <=[h-h_j]_(y,2,Lip).

For each fixed j the second quotient tends to J(h_j) at0. First choose j with small norm error and then take the spatial limit. This proves the asserted cofactor limit and its value. It does not assert smooth density in the entire large Lipschitz space. The smooth sequence (6) already proves that coupling is unbounded on this smaller smooth class as well.

Dependencies: proof 15 for the certified actual source, g>29 and C6 joins; proof 209 for the analytic source disk; proof 218 for the directly differentiated velocity kernel; topics212/33 for actual origin regularity; and proof 214 for global divided-coefficient and far-field bounds. All endpoint estimates, transport images, exact scalar corrections, logarithmic coefficients and normalization statements are independently derived above. No numerical computation is used, and no endpoint full inverse or nonexistence conclusion is asserted.
