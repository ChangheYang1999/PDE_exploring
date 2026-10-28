# Independent cross-audit of V229 (proof 218) and V230 (proof 219)

Auditor: independent auditor. Proof files were only read. One small sympy check ran under nice with python3 -B. Its script was written to /tmp and deleted as soon as it had run. No git, node, servers or heavy computation were used.

Audited files (sha256sum):
- verification/proofs/218_holder_weight_limit/PROOF.md
  9bc72570548213fa9da0ac1788d253fb1ce7edbcf8606d3f8ee6f052364eb257
- verification/proofs/219_lipschitz_source_obstruction/PROOF.md
  c51566b7ba2d8f61e6445fda3ef4f56e32eaa57dfd68c30ad2ee3f8db381ded7

Both hashes match evidence/check.json. Every dependency hash in the two manifests matches the current file: proof 01 f0e20786..., proof 212 be13a724..., proof 15 20071e87..., proof 218 9bc72570.... Context read: topics 01, 15 (with evidence/source_512.log), 202, 209, 212, 213, 214, 215, and verifier team message 78 and 79.

VERDICT V229: PASS WITH REMARKS
VERDICT V230: PASS WITH REMARKS

I found no mathematical gap in either proof. I rederived every displayed coefficient. All findings below are remarks or typos, and each comes with a suggested rewording.

## V229 (proof 218): what was checked

C1. Kernel. With proof 01 conventions, U2=R1^2 h=d_xx G*h, where G=-(1/2pi)log r. Off the support, the kernel is K2=(x^2-y^2)/(2pi r^4)=Re(z^-2)/(2pi). Using d_y Re f(z)=Re(i f'(z)), I get d_y K2(-Y)=sin(3theta)/(pi r^3) and d_y^3 K2(-Y)=-12 sin(5theta)/(pi r^5). I checked both symbolically and at a numerical point. The c formula agrees with proof 01 (1) and proof 213, and b[h]=-(2/pi) integral sin(5theta) r^-5 h follows.

C2. Signs and parity. Both sin(3theta) and sin(5theta) are unchanged by theta -> pi-theta, so they are even in x, and both are odd in y. That is the same parity as H, so all four reflected copies contribute with one sign: c[H]>0 and b[H]<0. The scalings c[H_a]=a^-1 c[H] and b[H_a]=a^-3 b[H] are correct. For h=H-aH_a this gives c[h]=0, b[h]=(1-a^-2)b[H], which is nonzero for a>1, and J(h)=0 because h vanishes near 0.

C3. Axis expansion. U is harmonic on a disk about 0 because h vanishes there. Parity rules out constant and quadratic terms, and c=0 removes the linear term. So U2(0,y)=b y^3+O(y^5), and by incompressibility U1/x at x=0 is -3b y^2+O(y^4). Proof 212 (17) gives the axis cofactors a1(0,y)=2y+O(y^3) and a2(0,y)=1+O(y^2). The sum is -6b y^3+b y^3=-5b y^3.
I also checked this independently. I took psi=beta(x^3y-xy^3)+b5 Im(z^6), which has b=-beta, and rho=x^2y+g1x^4y+g2x^2y^3+g3x^2y^5+g4x^6y. The limit of F/x^2 at x=0 is -5b y^3+(3beta g2-54 b5)y^5+..., which confirms (5).

C4. Membership failure. F is odd in y and F(x,0)=0. The quotient |F(x,y0)|/(|x|^p y0^alpha)=|x|^(2-p)|F(x,y0)/x^2|/y0^alpha tends to infinity as x->0 when p>2. Since c[h]=0, every column c[h]M vanishes. The transport image is compact, lies inside supp h and away from both axes, and so belongs to E_p for every p.
The proof 202 origin extension equals the linear field (-A0 x,D0 y) on supp h, because the support has radius at least 1 and delta is small. That field is smooth there.

## V229 findings

1. (remark) "The actual C3 transport regularity alone": proof 202 proves C3 only on a small disk about 0. The support of h is at radius 1 or more. What is actually needed there is C^alpha regularity of V (C^1 is more than enough) on a compact set away from the axes. That follows from the global C6 joins (proof 15) and the C1 coefficients used in proof 214. Repair: cite those instead.
2. (remark) Angular window. sin(5theta) vanishes at pi/5, only pi/30 from pi/6. Both sines are positive exactly on 0<theta<pi/5, so the "small disk" needs angular half-width below pi/30. Repair: state this explicitly.
3. (remark) The sentence "The maximal domain of a possible full E_p realization must be a proper restriction of that transport domain" claims more than is shown. The proof shows that D_T={h in E_p: Th in E_p} is not contained in D_full={h in E_p: Lh in E_p}. It does not show D_full is contained in D_T. Repair: "D_T is not contained in D_full, so any E_p realization of the full expression on a subdomain of D_T must use a proper subdomain."
4. (typo) The displayed size |5b y0^3+O(y0^5)| should read |-5b y0^3+O(y0^5)|. It is harmless inside the absolute value.
5. (remark) The obstruction uses only the leading axis cofactors (2y,1), so any background x^2y+... gives the same -5b. The stated scope is accurate: this space and domain only, with no claim about stronger anisotropic norms or a full inverse. "Largest preserved power" relies on proof 214 for p=2. Exponents p<2 are not addressed and nothing is claimed about them.
6. (remark) The actual C^(4,1) background regularity is proof 33, used through proof 212. It could be added to the dependency list.

## V230 (proof 219): what was checked

D1. The identity |Z|sin(3 arg Z)=3y-4y^3/(s^2+y^2) holds. The bounds (4) hold uniformly, including on the transition annulus.
On parity: the packet is odd in y and its reflection is even in x. Its supports are disks of radius d about +-P, separated from x=0 and the origin. J=0, c[u_eps] is uniformly bounded, and subtracting c[u_eps]q gives c=J=0 exactly.

D2. Transport graph. The formula D(Tf)=(DV)^T Df+(V.grad)Df-Df is correct. V(P)=0, and V(-P)=0 by parity, so V.D^2 f_eps=O(|Z|/(|Z|+eps)) and the graph bound is truly uniform. This term would be unbounded at a point where V does not vanish, so the source location is essential here, and the proof uses it correctly.

D3. The logarithm. The angular integral of sin^2(3theta) is pi, so d_y U2[f_eps](P)=integral kappa(r/eps)chi(r)dr/r=log(1/eps)+log(d/4)+O(1). The two transition annuli each contribute at most log 2. The reflected packet, the q correction and U1(P) are bounded. U2(P)=0 by oddness in y.

D4. Equation (7). Oddness in y gives rho0_x(P)=rho0_yy(P)=0 and U2(P)=0. So d_y F(P)=g log(1/eps)+O(1). The proof 15 evidence encloses g in [29.7494906633, 29.7494906634], so g>29 holds strictly.
F is C^1 near P, so [F]_(y,2,Lip)>=|d_y F(P)|/p^2. The transport image vanishes on |Z|<eps, so it cannot cancel this.

D5. Membership of the images for each eps. The velocity is smooth and decays like r^-3, because the integral of h is 0. a1 and a2 are Lipschitz near 0 by proof 212 (17), C5 across the joins, and satisfy the far bounds (10) of proof 214. The images are therefore in E_(2,1). Their weighted L2 norms are finite because |F|^2 is O(r^(2k-6)).

D6. Limiting input. Tf0=(DV(P)Z).grad f0+O(|Z|^2).grad f0-f0. The first term is homogeneous of degree 1, and the gradient of the second is O(|Z|), so Tf0 is Lipschitz and h0 is in D_T.
I checked symbolically that Delta[r^3 log r sin 3theta]=6r sin 3theta, and that -Delta of -(1/6)r^3 log r sin 3theta equals f0. d_s^2 of that potential is -y log r plus a degree-one homogeneous term. -d_s d_y of it is s log r plus a degree-one homogeneous term. So the coupling is -g y log r plus a Lipschitz remainder. At s=0 its vertical difference quotient is about -g log|y|, which diverges. Claim (8) and the non-membership follow.

D7. Inequality (2) and the closure statement. |h(x,y)|<=[h]x^2|y| follows from h(x,0)=0. The Cauchy extension and the two-step limit argument are correct. The result is consistent with proof 214, where J is non-closable for alpha<1.

## V230 findings

1. (remark) "That domain is strictly larger than the maximal domain of the full expression" has the same issue as V229 finding 3. What is proved is that h0 lies in D_T but not in D_full. The inclusion D_full in D_T is not shown, and it is not automatic, because coupling and transport could cancel for other inputs. Repair: "the maximal transport domain is not contained in the maximal domain of the full expression."
2. (remark) The analytic disk of radius 1/1000 about P, inside one knot span, is certified in proof 209, not proof 15. Proof 15 only gives C6 joins. The proof actually needs only C^2 regularity of rho0 and C^(1,1) of V near P. Repair: cite proof 209, or weaken the hypothesis to C^2.
3. (remark) The image-membership paragraph cites only "smooth-on-annuli, C^(4,1)-at-origin". It also needs the C5 join regularity and the far bounds (10) of proof 214, for a1, a2 and grad rho0 along the whole vertical axis. Repair: add proof 214 to the dependencies.
4. (remark) Weight range. For these compact inputs the images lie in L2(w_gamma) for every gamma>2k-4. 4k<gamma<2 is the common-space range: gamma>4k is needed for F0 to be in Y (proof 213), and gamma<2 for the weighted velocity bound (proof 214). It is not needed for these images. The proof text is correct as written. The check.json amendment phrase "necessary lower bound for far-field image integrability" is inaccurate. Repair: correct that sidecar wording.
5. (remark) c1=g/p^2 itself works, since the error term is O(1). This is about 0.40. Cosmetic.
6. (typo) Notation clash. P names both the source point and the local potential, as in "-Delta P=f0" and "U2=d_s^2 P". Also, p is the source abscissa here but the weight exponent in proof 218. Repair: rename the potential Phi.
7. (typo) "h0 with c=J=0 in the sense that it vanishes near the physical origin" mixes two reasons. J=0 because h0 vanishes near 0. c=0 because c[u0]q was subtracted, and c[u0] is an absolutely convergent integral. Repair: reword.
8. (remark) Scope. The logarithm is the classical Lipschitz endpoint loss of the order-zero multiplier R1^2. What is new is the uniform bound in the actual transport graph together with exact c=J=0. As stated, nothing is claimed for stronger graph norms or for an endpoint full inverse, consistent with Note78.

## Summary

V229: the -5b y^3 axis coefficient, the independence of b from c, the exact zero-strain input, the transport-image membership and the p>2 divergence are all correct. V230: the exact kernel logarithm, the uniform transport-graph bound (which depends on V(P)=0), the -g y log r singularity of the limiting input, the J continuity at alpha=1 and the weighted extension are all correct. The only overstatements are the two "proper or strictly larger domain" sentences (V229-3, V230-1) and the sidecar wording on the weight range (V230-4). None of these affects the main theorems.
