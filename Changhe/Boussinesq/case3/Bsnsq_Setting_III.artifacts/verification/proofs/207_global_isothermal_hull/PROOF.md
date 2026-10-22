# Constant-temperature open sets and their global orbit saturation

Status: CONFIRMED as the global necessary-condition theorem stated below. This is a necessary-condition theorem for global classical profiles. It does not exclude all smooth B2 profiles.

## 1. Exact statement

Let beta>0, let V be a C2 vector field on R2 with V(X)=o(|X|), and put W(X)=beta X+V(X). Assume div V=0, Omega=-curl V is C1, and Theta is C1. Use the physical Cartesian curl curl V=partial_x V2-partial_y V1. Assume on the whole plane

 W.grad Theta=(beta-2)Theta,
 W.grad Omega+Omega=partial_x Theta.                         (1)

For any nonempty open D on which Theta has one constant value L, one has (beta-2)L=0. Let phi_t be the global flow of W and define the orbit saturation

 H(D)=union over t in R of phi_t(D).                         (2)

Then H(D) is open, invariant in both time directions, contains D, and satisfies Theta=L and Omega=0. Consequently V and W are harmonic componentwise on H(D), and are real analytic there. Connectedness of D or H(D), boundedness of H(D), vorticity decay, and a uniform backward bound for all points of H(D) are not required.

In particular supp Omega is contained in supp grad Theta, with supports taken as closed supports of continuous functions on the whole plane. Here grad Theta denotes the whole gradient, not just partial_x Theta.

For the endpoint consequence assume beta=2 and the smooth B2 center-arc setting. Let gamma be the connected zero component of W through the material center, and let p be either endpoint. In oriented orthonormal coordinates (s,z) at p, assume DW(p)=diag(0,4), W=0 along the negative half-arc through p, and no positive zero interval extends that component. Then Theta-Theta(p) cannot vanish on any neighborhood of p. No outgoing/incoming classification or isolation of other zeros is needed. The zero-arc and endpoint properties in this application are the already proved hypotheses of lead4.7(iii)-(iv), not conclusions of (1) alone.

The argument uses the relative velocity V=U-U(0) in B2. Subtracting the fixed vector U(0) preserves sublinearity and divergence. It adds no new drift, boundary, harmonic field or inverse convention.

## 2. Completeness and backward boundedness

Sublinearity and local boundedness give |W(X)|<=C(1+|X|). Since W is C1, local solutions are unique. The scalar differential bound for 1+|phi_t X| on each finite positive or negative time interval, followed by Gronwall, prevents escape to infinity in finite time. Therefore the flow exists for every real time. Its inverse is phi_-t, so each time map is a C1 diffeomorphism and an open map.

Choose R*>0 such that |V(X)|<=(beta/2)|X| for |X|>=R*. Then W(X).X>=(beta/2)|X|2 there. If Y(t)=phi_-t(Y0),

 d/dt |Y(t)|2=-2Y(t).W(Y(t))<=-beta |Y(t)|2                 (3)

whenever |Y(t)|>=R*. The first outward crossing of any sphere of radius larger than max(R*,|Y0|) contradicts (3). Hence the entire backward orbit lies in the closed ball of radius max(R*,|Y0|). Every backward orbit starting outside the ball of radius R* reaches that radius in finite time: otherwise integrating (3) would give |Y(t)|2 <= |Y0|2 exp(-beta t) while |Y(t)| remains above R*. The ball is backward invariant. Its closure is compact in the original whole-plane domain. In particular Omega is bounded along this orbit. This is a pointwise bound depending on Y0, and that is sufficient below.

## 3. Transport on the open saturation

Because Theta is constant on the open D, its full gradient is zero there. The first equation in (1) gives (beta-2)L=0. Along any global flow line the chain rule and the scalar linear ODE give

 Theta(phi_t X)=exp((beta-2)t)Theta(X).                      (4)

For X in D the right side equals L for every t: either beta=2, or L=0. Thus Theta=L on H(D). Equation(2) is a union of open images, so H(D) is open. The flow group property gives phi_s(H(D))=H(D) for all s in R.

Fix Y in H(D). On the entire backward orbit through Y, the physical derivative partial_x Theta vanishes, since that orbit remains in the open set H(D) where Theta is constant. With reversed time, the second equation of (1) becomes

 d/dt Omega(phi_-t Y)=Omega(phi_-t Y).

Consequently

 Omega(Y)=exp(-t)Omega(phi_-t Y).                            (5)

The orbit is in the compact ball of Section2, so its vorticity values have a finite bound. Letting t tend to infinity in (5) gives Omega(Y)=0. No forward boundedness or global vorticity bound has been assumed.

On H(D), div V=0 and curl V=0. The Cartesian identities

 Delta V1=partial_x div V-partial_y curl V,
 Delta V2=partial_y div V+partial_x curl V

give componentwise harmonicity. Since beta X is affine, the same holds for W. Interior regularity for harmonic functions yields real analyticity on this open set. This conclusion does not assert analytic continuation across its boundary.

For any L, let I_L be the interior of the level set {Theta=L}. If I_L is nonempty, apply the theorem with D=I_L. Its open saturation H(D) still has value L, so H(D) is contained in I_L by the definition of interior. Since I_L is contained in H(D), equality follows. Thus I_L is invariant in both time directions and lies in the interior of {Omega=0}. Empty interiors satisfy the same assertions trivially.

## 4. The support inclusion

If X lies outside supp grad Theta, some ball around X has grad Theta=0. Integrating the derivative along line segments inside that ball makes Theta constant there. Section3 gives Omega=0 on that ball, so X lies outside supp Omega. Taking complements proves supp Omega subset supp grad Theta.

A single scalar level set or a single orbit on which Theta is constant is insufficient: the physical derivative partial_x Theta need not vanish there. No support inclusion involving partial_x Theta alone follows from this argument, since its vanishing on an open set does not by itself make that set invariant.

## 5. Every endpoint has no isothermal neighborhood

Suppose Theta=Theta(p) on a disk D about an endpoint p. Section3 gives Omega=0 there; hence W is real analytic there. In the orthonormal endpoint coordinates, the normal component W_z has derivative partial_z W_z(p)=4. The analytic implicit-function theorem gives an analytic graph z=k_an(s) containing all nearby zeros of W_z. The negative zero half-arc lies on this graph. The analytic one-variable function

 f_an(s)=W_s(s,k_an(s))

vanishes on a negative interval, so its Taylor expansion or the one-variable identity theorem makes it zero on an interval through0. Thus W vanishes on the entire graph interval, including its positive half. That interval connects through p to gamma and extends its connected component beyond its endpoint. This contradicts the endpoint hypothesis. The argument is independent of the positive reduced zero set, its sign, and the existence of neighboring isolated zeros.

The application requires global equations and backward boundedness. It supplies a global alternative to the earlier outgoing, isolated-incoming and conditional accumulating arguments. It does not prove that Theta is nonconstant on every terminal subarc of gamma at a general incoming endpoint. Nor does it exclude an isothermal neighborhood around every nonstationary point of a strong unstable orbit: an open saturation can approach p without containing p. Those are different assertions.

## 6. Why backward boundedness cannot be deleted

There is a smooth polynomial counterexample to the blanket claim that the coupled equations alone force Omega=0 wherever Theta is locally constant. Put beta=2 and

 Psi(x,y)=3xy+x3/6,
 V=(-3x,3y+x2/2),
 W=(-x,5y+x2/2),
 Omega=-x, Theta=0.                                        (6)

Direct differentiation gives V=(-Psi_y,Psi_x), div V=0, -Delta Psi=Omega, and W=2X+V with V(0)=0. Both equations(1) hold: W.grad Omega=x and Omega=-x cancel. The x-reflection parities and Theta(0,y)=0 hold. Nevertheless Theta is constant on the whole plane while Omega is not zero.

This field has quadratic velocity growth, nondecaying vorticity, and zero temperature jet a0, so it is not an admissible B2 profile. Its backward x coordinate is x0 exp(t). Solving the backward y equation gives

 x(t)=x0 exp(t),
 y(t)=exp(-5t)(y0+x0^2/14)-x0^2 exp(2t)/14.                 (7)

For x0!=0 the backward orbit is unbounded and Omega(phi_-t Y)=-x0 exp(t). The product exp(-t)Omega(phi_-t Y) stays -x0 instead of tending to0. This verifies exactly the missing step if (3) is unavailable. It also shows why replacing the actual whole-plane flow by a bounded artificial coordinate extension is not legitimate for this theorem.

## 7. Verification and limits

Independent symbolic controls checked (3)-(7), the curl convention and the div-curl identities. They retained the counterexample's nonzero vorticity and failed growth condition. All38 exact and text controls passed. The lead candidate v1 initially received K1-K3 confirmation, but the K2 logical-novelty and unqualified K3 scope verdicts were corrected after the prior scattering implication was identified. Section8 and the current verification summary supersede those two initial verdicts. The argument is an informal proof; no formal proof or numerical profile certificate is asserted. General smooth beta2 and beta>2 slow-tail B2 profiles remain open.

Publication UTC: 2026-10-21T21:02:26.423932+00:00. Candidate v1 SHA256: 8118e73ddfe5ee4854f5884e071ab5785d1140eb3a6a6ad8076ea4be00b2d834. Complete visible Opus5.5 review and independent adjudication are in verification/.

## 8. The prior scattering implication and the v2 scope repair

Written before the v2 controls, 2026-10-21 after the lead's second candidate. The v1 statement that the general conclusion was not previously established is withdrawn as a logical novelty claim. Its direct proof in Sections2-5 is valid, but the earlier report4.7(vii) already implies it. This section gives the implication explicitly, conditional on those earlier identities.

Take beta=2 and the whole-plane hypotheses of Section1. Choose the backward invariant closed ball B of Section2. Let K be the set of initial points with bounded forward orbits. Once an orbit is outside B, the forward version of (3) makes its radius grow exponentially for all later time. Hence a bounded forward orbit must stay in B at every nonnegative time, and conversely one staying in B is bounded. Thus

 K=intersection over t>=0 of phi_-t(B).

This is a closed subset of the compact B. Shifting a bounded forward orbit by any fixed real time preserves forward boundedness, since the additional finite orbit segment is compact. Consequently phi_s(K)=K for all real s. The variational equation for the flow, or differentiation of its two-column determinant, gives det Dphi_s=exp(4s). The change of variables formula yields |K|=exp(4s)|K|; finite area and any s>0 imply |K|=0. Therefore E=R2\K is open and dense. This proof does not require K to be empty, nor require the whole zero set to be the central arc.

Use the previously proved scattering identities: on E there is a C1 map Phi into R2\{0} with det DPhi=1, Theta=h(arg Phi), and h in C1(S1); if h'(alpha)=0, Omega vanishes along each escaping orbit with scattering direction alpha. These are explicit dependencies, not claims proved anew here. In any angular coordinate patch, the differential of arg at a nonzero vector is nonzero. Multiplication by the invertible DPhi leaves it nonzero. Thus arg Phi is a submersion, locally open. If H is open and Theta=L on H, the angular image of H intersect E is open, and h=L on this image. Its derivative vanishes there. The prior implication makes Omega zero on H intersect E. Since E is dense and H is open, H intersect E is dense in H; continuity of Omega gives Omega=0 on H. This proves the v2 alternative derivation. It does not need H invariant, because the quoted scattering implication is already global.

For the lead's displayed counterexample set W=(-x/2,9y/2-x^3/3), Theta=0, Omega=x^2. It has div W=4, curl W=-x^2 and W.grad Omega+Omega=-x^2+x^2=0. A stream function for U=W-2X is Psi=5xy/2-x^4/12. Its backward orbit through (x0,y0) is

 x(t)=x0 exp(t/2),
 y(t)=exp(-9t/2)(y0-x0^3/18)+x0^3 exp(3t/2)/18.

Substitution gives the reversed ODE and e^-t Omega(phi_-t(x0,y0))=x0^2. The cubic velocity fails sublinearity. Omega is even in x, so the example also fails the prescribed odd vorticity parity; it tests precisely the displayed differential identities, not the full local B2 class. Section6 supplies an independent parity-preserving control. Neither field has the required nonzero temperature jet.

The v2 phrase "neither was stated before" is read as an inventory of the two general formulations in the prior report, not as logical independence or mathematical priority. The derivability from (vii) is explicit. The outgoing and accumulating neighborhood proofs cited as local are the arguments in (xii)(b) and (xx)(a). The incoming result (xiv)(c) uses the global basin statement (xiv)(b) and is not classified as purely local. The v2 F8 repair preserves the distinction between a neighborhood of the stationary endpoint and a neighborhood of other points of a strong unstable orbit. Endpoint nonconstancy does not rule out plateaus that merely accumulate there.

V2 audit completed 2026-10-21T21:14:39.563111+00:00. K1-K3 CONFIRMED for SHA256 49379c358bc90427e8eff49a5e2e94476f26d421f1ae4e8c2dd366144ff1b8ed. The original v1 scope verdict is superseded as described in Section8.
