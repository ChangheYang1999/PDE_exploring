# Uniform subcritical one-third growth forces derivative decay

Status: the principal theorem and its stated A476/A477 consequences are PROVED by the direct A498 corollary in Section 8, confirmed in A502. Sections 2-6 retain the independent earlier reconstruction; A502 does not separately certify that longer argument. The theorem uses an explicit growth hypothesis and does not prove the campaign nonexistence conjecture.

## 1. Exact statement and notation

Let0<c<1,omega in R be finite,J(x1,x2,x3)=(-x2,x1,0),A=cI-omega J and B(y)=Ay+U(y). Suppose U in C2(R3;R3),P in C1(R3) satisfy

    div U=0, (1-c)U+(DU)B+omega JU+grad P=0,
    M=sup|U|<infinity,
    lim_(R->infinity) R^(-1/3) sup_(R/2<=|y|<=2R)||DU(y)||=0.       (1)

Then DU tends uniformly to0 at infinity. The confirmed A476, applied only after this conclusion, gives a positive power of derivative decay and the finite Dini integral of m(r)=sup_(|y|>=r)||DU(y)||. In particular DU is bounded. With U tending uniformly to0 and1/3<c<1, A477 further gives DU=O(r^(-1/c)). Constants are allowed to depend on c,omega,M and compact C2 norms. No uniform threshold over these parameters is claimed.

Set G=DU,W=curl U,e=Ay/|Ay| away from0 and P_e=I-e tensor e. All little-o statements are uniform on the exterior and therefore on comparable annuli and balls. M=0 is immediate, so assume M>0. The condition in(1) is equivalent to ||G(y)||=o(|y|^(1/3)) uniformly, and is much stronger than any stated condition along single rays. Bounded or decaying U alone supplies no such estimate in this proof.

## 2. The actual pressure gradient and a directional derivative

Divergence of the equation cancels its two skew terms and gives, distributionally,

    f=Delta P=-tr(G^2)=-partial_i partial_j F_ij, F_ij=U_iU_j.     (2)

Initially the equation gives grad P=O(r^(4/3)). Let N=-1/(4pi|x|), so Delta N=delta0, and N_d=chi(x/d)N for a fixed smooth radial cutoff equal to1 near0 and supported in the radius2 ball. Define

    Q_d=grad N_d*f-partial_i partial_j grad(N-N_d)*F_ij.          (3)

The first convolution is local and absolutely convergent, with kernel L1 norm at most Cd. The second has an L1 kernel of norm at most C/d: its tail has order|x|^-4 and its singularity has been removed. Thus Q_d is continuous. Put a_d=Delta N_d-delta0, a smooth annular function. Differentiating gives

    div Q_d=f+a_d*f+partial_i partial_j a_d*F_ij=f,
    curl Q_d=0.                                                (4)

The first cancellation uses(2) against a compact smooth kernel. In the second identity the near term is a gradient and the mixed fourth derivatives of N-N_d commute and are L1. This avoids invoking an undefined convolution with an undifferentiated potential. For any d,e>0, N_d-N_e is smooth, compactly supported and zero near0. Subtracting(3) and applying(2) to its derivatives shows Q_d=Q_e. Denote the common field by Q.

Fix epsilon>0. Outside a sufficiently large radius, |G|<=epsilon r^(1/3). At a point of radius R choose d=epsilon^-1 R^-1/3. For fixed epsilon and large R the near ball lies in a comparable annulus and d<1. Hence

    |Q(y)|<=C[epsilon^2 R^(2/3)d+M^2/d]
           <=C(1+M^2)epsilon R^(1/3).                         (5)

C does not depend on epsilon; the starting radius may. Thus Q=o(r^(1/3)). By(4), grad P-Q is an entire harmonic vector distribution growing as O(r^(4/3)). Harmonic interior estimates bound its second derivatives at a fixed point by C R^-2/3, so it equals Ky+b for constants K,b. In the momentum equation at y=Rz divide by R on a fixed annulus. G(Rz)=D_z(U(Rz)/R) tends distributionally to0, so G(Rz)Az does too. All other terms besides Kz tend to0, including GU/R=O(R^-2/3) and Q/R=o(R^-2/3). Consequently K=0. The constant b need not vanish and is absorbed by the resulting little-o bound:

    grad P=o(r^(1/3)), G Ay=o(r^(1/3)),
    h:=Ge=o(r^-2/3), |De|<=C/r.                                (6)

Here |Ay|>=c|y|, including on the rotation axis. No normalization of the actual pressure has been imposed.

## 3. Exterior flow and the axial curl component

B is locally Lipschitz and has at most linear growth, so its flow is complete. Since cr-M<=r'<=cr+M, every exterior point comes in finite forward time from a fixed sufficiently large sphere of radius R0>2M/c. On such a segment, with k=M/c,

    k+(R0-k)e^(cs)<=r(s)<=(R0+k)e^(cs)-k,
    r(t)/r(s)<=C e^(c(t-s)), 0<=s<=t.                          (7)

If an exterior backward orbit failed to reach the sphere, r'>=cr/2 would force its radius to0 backward while remaining exterior, a contradiction. These arguments need no bound on DB.

The vorticity equation is B W=G W-W-omega JW. Since D_(Ay)e=-omega Je, sigma=W.e satisfies

    B sigma=-sigma+e.GW+W.D_Ue.                                (8)

In an oriented frame with e=e3, e.GW=G32G13-G31G23+G33W3, whose absolute value is at most C||G||||Ge||. By(1),(6), both forcing terms in(8) are o(r^-1/3). As1>c/3, integration on(7) gives

    sigma=o(r^-1/3).                                          (9)

The uniform little-o transport rule used here is elementary: for damping beta>c theta and source o(r^-theta), start on a larger fixed sphere where the source is at most epsilon r^-theta. Its convolution is bounded by C epsilon r^-theta, while the initial term is O(r^(-beta/c)). Taking an exterior limsup and then epsilon to0 proves the assertion.

## 4. Local Holder control with a vanishing logarithmic coefficient

We next prove the endpoint-sensitive estimate

    log(2+[G]_(1/2,B(y,|y|/8)))=o(|y|^(1/3)).                 (10)

Set tau=1-t,s=-log tau,Q_s=exp(omega sJ),y=exp(sA)x and define the exact physical Euler fields

    u(x,t)=tau^(-(1-c))Q_s U(y), xi(x,t)=tau^-1 Q_s W(y).

On a fixed annulus1/16<|x|<16, given epsilon>0 choose t0 close enough to1 that for t>=t0

    |grad u|<=l(t)=C epsilon tau^(-1-c/3),
    |xi|<=w(t)=C epsilon tau^(-1-c/3).                         (11)

C is independent of epsilon and t0. Globally |u|<=M tau^(-(1-c)), which is integrable in time because c>0. The physical flow is complete on each finite preterminal interval by this velocity bound and local C1 regularity; no global gradient bound is used.

The local kernel estimate needed below is, for a ball E near the unit sphere and margin0<d<=1/16 inside the fixed annulus,

    [grad u]_(1/2,E)<=C[xi]_(1/2,E+d)
       +Cw d^-1/2(1+log(1/d))+CZ,
    Z=M tau^(-(1-c))+w.                                      (12)

Here is a direct justification. Subtract the Biot-Savart field of xi times a fixed cutoff supported in the outer annulus and equal to1 in an inner annulus. The difference is harmonic there, since -Delta u=curl xi and div u=0. The degree-minus-two kernel bounds its size by CZ; harmonic interior estimates bound its first two derivatives on smaller balls. It need not be curl free. For the remaining derivative singular integral, cut xi off again across the margin d. Its near part obeys the usual Holder cancellation estimate C[xi]_(1/2,E+d)+Cw d^-1/2, obtained by subtracting a local value in the mean-zero degree-minus-three kernel. The far part has supremum Cw(1+log(1/d)) and Lipschitz constant Cw/d. Interpolation gives the remaining term in(12). All cutoffs and constants are fixed by local geometry.

Increase t0 so the total backward displacement (2M/c)(1-t0)^c is at most1/8 and (M/c)(1-t0)^c<=1/16. For each|xstar|=1 define

    r0(t)=1/4+(2M/c)(1-t)^c,
    Theta(t)=[xi(t)]_(1/2,B(xstar,r0(t))),
    E(t)=exp(integral_(t0)^t l(v)dv).

Two trajectories ending in this ball at time t lie at earlier q in the ball of radius r0(t)+d(q,t), where

    d(q,t)=(M/c)((1-q)^c-(1-t)^c),
    M(t-q)<=d(q,t)<=1/16, r0(q)=r0(t)+2d(q,t).

All these balls and the segments joining two points lie inside the fixed annulus. Local backward Gronwall gives distance at q at most E(t)/E(q) times terminal distance. Subtract the physical vorticity equations along the paths, divide by the square root of terminal distance, and apply(12) using the remaining margin d. This yields

    Theta(t)<=E(t)^1/2 Theta(t0)
       +integral_(t0)^t (E(t)/E(q))^1/2
          [(l+Cw)Theta+Cw^2 ell(t-q)+CwZ](q)dq,
    ell(v)=v^-1/2(1+|log v|).                                 (13)

The initial norms are uniformly finite by compact C2 regularity. Actual seminorms are finite and locally bounded on finite preterminal intervals; their integral inequality is legitimate without presupposing the bound being proved. The kernel ell is integrable.

Put Y=E^-1/2 Theta. Its inhomogeneous integral is at most C_(epsilon,t0) tau^-4, since w^2 and wZ are bounded by constants times tau^(-2-2c/3) and c<1. Meanwhile

    integral_(t0)^t(l+Cw)<=C_c epsilon tau^-c/3,
    log E(t)<=C_c epsilon tau^-c/3.

Gronwall with the nondecreasing inhomogeneous bound gives

    Theta(t)<=C_(epsilon,t0) tau^-4 exp(C_*epsilon tau^-c/3),  (14)

where C_* is independent of epsilon and t0. Large initial norms affect only the prefactor. Apply(12) with fixed margin1/16 on the ball of radius1/8, then rescale with tau=R^-1/c and xstar=exp(-sA)y. The scaling is

    [G]_(1/2,B(y,R/8))=tau^(1+c/2)[grad u]_(1/2,B(xstar,1/8)).

After taking logarithms and dividing by R^1/3, the exterior limsup is at most C_*epsilon. Let epsilon tend to0. This proves(10), with no assertion about the endpoint physical flow.

## 5. Frozen planar data and their logarithmic estimate

For a C2 vector field v on a radius2ell ball in dimension2 or3, cut it off smoothly, equal to itself on the radiusell ball. Let F collect divergence and antisymmetric derivatives of the compact field, epsilon_F=||F||_infinity and K=[F]_(1/2). The Newtonian div-curl identity, with its local distributional term, gives

    |Dv(0)|<=C[K eta^1/2+epsilon_F(1+log(2ell/eta))],
    ell>=1, 0<eta<=1.                                        (15)

Indeed the derivative kernel has degree minus the dimension and zero spherical mean away from0. In radius eta subtract F(0), giving the first term. In the remaining annulus integrate epsilon_F dr/r. The bounded local distributional term contributes C epsilon_F. Compact support rules out harmonic-gradient ambiguity, including in dimension2.

Fix y of radius R, freeze n=e(y),P0=I-n tensor n, and restrict V(v)=P0 U(y+v) to the Euclidean plane n-perp on the disk|v|<2ell with ell=R^1/3. For large R this disk lies in B(y,R/8). Since n is constant,

    div_2 V=-n.Gn, curl_2 V=W.n.                              (16)

On this disk |e(y+v)-n|<=C R^-2/3. Equations(1),(6),(9) make both uncut data o(R^-1/3). Cutting off V adds O(M/ell), so its full planar data obey

    ||F||_infinity=O(R^-1/3), log(2+[F]_(1/2))=o(R^1/3).       (17)

For the Holder statement use(10), restriction and cutoff products. The additional cutoff terms grow at most polynomially. Choose eta=(R^2 max(1,K))^-2. Then K eta^1/2<=R^-2, while

    1+log(2ell/eta)<=C log R+C log(2+K)=o(R^1/3).

Applying(15) proves H:=P_e G P_e=o(1). The projection was frozen before differentiation, so no derivative of a variable plane has been omitted.

## 6. Stretching cancellation and recovery of all derivatives

At each point write g=P_e G^T e,h=Ge. Exactly

    G=H+e tensor g+h tensor e.

In an oriented frame with e=e3 the matrix and actual curl are

    G=((a,b,h1),(d,f,h2),(g1,g2,h3)),
    W=(g2-h2,h1-g1,d-b),
    g.W=-g1h2+g2h1.                                          (18)

Thus the source's estimate is valid:

    W.GW<=(||H||+|h|)|W|^2+|g||h||W|.

Since |g|=o(R^1/3),h=o(R^-2/3),H=o(1), outside a large sphere this gives q'=B|W|<=-beta q+o(r^-1/3) with beta=(1+c/3)/2>c/3. Along a trajectory with nonzero terminal W the homogeneous linear vorticity equation guarantees W never vanishes; otherwise the assertion is immediate. Hence the comparison is valid without differentiating a norm at its zero. By(7) and the rule after(9), W=o(r^-1/3).

Now cut off U on B(y,2ell),ell=R/32. The full three-dimensional div-curl data have supremum o(R^-1/3), including the smaller O(M/R) cutoff error, and Holder logarithm o(R^1/3) by(10). Apply(15) with the same adaptive eta. Both terms tend to0, so G tends uniformly to0. This proves the principal statement. Only now invoke A476 and, under the additional stated decay hypothesis, A477.

There is also a simpler exact strengthening of the stretching estimate. Equation(18) implies

    g.W=(W-(W.e)e).h, so |g.W|<=|W||h|.

Therefore W.GW<=(||H||+2|h|)|W|^2 and q'<=-(1-||H||-2|h|)q, with no additive forcing. Once H,h tend to0, (7) yields W=O(r^(-beta/c)) for every0<beta<1. This strengthening is not needed for the source proof and is submitted separately for the same focused review. It still does not by itself prove that H tends to0 without the growth assumption.

## 7. Dependencies and limits

Sections2-6 reconstruct the conclusion directly from(1), the actual Euler equation, elementary kernel identities, harmonic estimates and finite-time flow estimates. They do not use LIT120, LIT122 or any bound on the full gradient before proving one. A476 and A477 enter only as confirmed downstream consequences.

No helicity, symmetry, finite energy, pressure normalization or small rotation assumption occurs. This proves neither a universal bound at the critical big-O exponent nor a growth bound from U tending to0. The arbitrary-omega nonexistence conjecture and unconditional C2 basin coverage remain open. The source's separate LIT121 consequences need their own final verdict. Existing-file collaboration uses configured model agents; actual provider runtime is not independently attested.


## 8. Final verdict by the stronger confirmed theorem

A498(A) is already CONFIRMED for every finite omega and every 0<c<1: a full C2 velocity/C1 pressure profile with bounded U and DU=o(r^(1/2)) has DU tending uniformly to zero. It assumes neither velocity decay nor a pressure gauge.

The annular premise in (1) gives uniform DU=o(r^(1/3)). For r>=1,

    ||DU(y)||/r^(1/2) = (||DU(y)||/r^(1/3)) r^(-1/6) -> 0.

Thus all A498(A) hypotheses hold and its conclusion proves the principal theorem in Section 1. Once DU tends to zero, it is bounded by continuity on compact sets. The already confirmed A476 and A492 give Dini decay and DU=O(1/r); A477 gives DU=O(r^(-1/c)) when U tends to zero and 1/3<c<1.

This is a complete proof by a stronger audited dependency, with no new analytic estimate. It closes the LIT123 principal statement. It does not provide a separate verdict for every intermediate estimate of the earlier direct proof, or for the separate LIT121 far-field-constant theorem. The existing focused configured-model comparison supporting A498 supplies the model collaboration for this corollary. The model configuration is the primary model; independent provider runtime attestation is unavailable.
