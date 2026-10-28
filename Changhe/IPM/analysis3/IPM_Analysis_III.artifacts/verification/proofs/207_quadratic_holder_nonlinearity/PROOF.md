# Nonlinear failure in the quadratic Holder graph

## Exact statement

Fix0<alpha<1. Let E_2 be the Banach space of bounded continuous even-x,odd-y functions h with h(0,y)=0 and

 ||h||E2=||h||infinity+[h]_x+[h]_(y,2),
 [h]_x=sup |h(x,y)-h(x',y)|/|x-x'|^alpha,
 [h]_(y,2)=sup |h(x,y)-h(x,y')|/(|x|^2 |y-y'|^alpha).

Let L_delta be either of the normalized local operators of proof 203, for the exactly joined normalized modal trial rho0 and sufficiently small fixeddelta. Its transport is the frozen origin saddle in the first case and the extension of the actual variable field in proof 202 in the second. In both cases write

 L_delta h=V_delta.grad h-h
          +chi_delta(U[h]+c[h]X/3).grad rho0,
 D_delta={h inE2:V_delta.grad h-h inE2 distributionally},
 ||h||graph=||h||E2+||L_delta h||E2.

The cutoff is1 onB_(delta/2). The canonical velocity has multiplier (xi eta/(xi^2+eta^2),-xi^2/(xi^2+eta^2)); c is the absolutely convergent central-strain integral of proof 201. Proof 203 proves that L_delta is a closed bijection onD_delta and that its coupling is bounded onE2.

Define the quadratic nonlinearity on smooth compact inputs by

 N(h)=(U[h]+c[h]X/3).grad h.

There is a fixed compactK contained inB_(delta/2), separated from both axes, and smooth real functions h_n supported inK such that

 J(h_n)=c[h_n]=0,
 sup_n ||h_n||graph<infinity,
 ||N(h_n)||E2>=c_1 n,
 ||L_delta^(-1)N(h_n)||E2>=c_2 n                       (1)

for all sufficiently large integersn, with constantsc_1,c_2>0 depending on the fixed construction. Every input and nonlinear image belongs to its stated space. In particularN andL_delta^(-1)N, initially defined on these smooth inputs, fail to be continuous at0 from the graph topology toE2. They also have no bounded extension on graph-norm bounded sets of this smooth core. This gives a precise nonlinear limitation to the improved linear inverse. It does not imply that every stronger norm must control h_x in a specified Holder class.

The construction adapts proof 27's transverse characteristic strips. The additional work here is membership and uniformity in the weighted E2 norm and the exact localized maximal graph, including the nonlocal image near the axes. A counterexample in an unweighted graph cannot be transferred to this graph merely by naming an angular weight.

## A compact transverse velocity with exactly zero strain

Choose a pointQ in the first quadrant, strictly inside the innermost analytic modal region andB_(delta/4), away from0 and both axes. The origin expansion gives V_delta,1=-A0 x+O(r^3), A0>0, soQ can be chosen regular. All coefficients are smooth on a sufficiently small box aroundQ and its three reflected boxes. For the actual modal trial this follows from its finite inner powers, logarithms and angular modes, all smooth away from0; the frozen transport is smooth directly. The global finite regularity at0 and at other spline interfaces is not being used as a smoothness assertion.

The flow map (s,z) -> Phi_s(Q+z nu), withnu transverse toV_delta(Q), has nonsingular derivative at(0,0). The inverse function theorem supplies smooth local coordinates satisfying

 V_delta.grad s=1, V_delta.grad z=0.                  (2)

Shrink the box and choose a constant vectorw such thatw.grad z>=b_*>0 throughout a smaller flow tube. Choose a smooth compact potentialP0, supported in the larger first-quadrant box and equal on a neighborhood of that tube to

 (w2/2)(x-Qx)^2-w1(x-Qx)(y-Qy).

Reflect it evenly inx and oddly iny to getP. Letd=-Delta P. Fourier multiplication, including the local velocity multiplier term, gives exactly

 U[d]=(-P_xy,P_xx).                                   (3)

Indeed multiplying the Fourier transform of-DeltaP by the stated degree-zero symbol gives these two second derivatives. Both sides vanish at infinity, so no constant velocity is added. On the inner tube U[d]=w andd=-w2, hencegrad d=0. The density and velocity are compactly supported away from0, soJ(d)=0 andDU[d](0)=0. The canonical strain identity givesc[d]=0 exactly. This verifies the required transverse velocity without an approximation to a nonlocal controllability statement.

## Characteristic strips and strain correction

Choose a smooth eta(s), compactly supported in the flow coordinate interval and equal1 on a neighborhood of[0,tau], with fixedtau>0 sufficiently small. Let Psi be compact smooth onR and equalz^2 near both0 and1. On the first box put

 k_n^0=n^(-alpha)Psi(nz)eta(s),

and reflect it evenly inx and oddly iny. For largen these strips are supported in a fixed compact unionK of four boxes, still separated from both axes. Their amplitude isO(n^-alpha), support areaO(n^-1), and Lipschitz normO(n^(1-alpha)). Splitting each difference at distancen^-1 proves

 ||k_n^0||C^alpha<=C,
 ||V_delta.grad k_n^0||C^alpha<=C,                    (4)

because(2) gives V_delta.grad k_n^0=n^-alpha Psi(nz)eta'(s), with no transverse factor n. All cutoffs have support strictly inside the coordinate patch, so extension by0 preserves smoothness.

The strain kernel is smooth onK, hence|c[k_n^0]|<=C n^(-alpha-1). Choose a fixed smooth compact functionzeta, with the same density parity, supported in the outer boxes away from all the inner flow tubes, such thatc[zeta]=1. To construct it take a small nonnegative first-quadrant bump at a point where sin(3theta)!=0, reflect with density parity, and divide by its nonzero exact strain integral. The box contains such a point because the zero set of sin(3theta) has no open subset. EnlargeK within the original boxes if necessary. Put

 k_n=k_n^0-c[k_n^0]zeta, h_n=d+k_n.                   (5)

Then all supports lie inK, andJ(h_n)=c[h_n]=0 exactly. Equations(4) remain uniform after this fixed small correction. The compensator need not have zero strain separately; its localized linear image belongs to the graph by boundedness of the coupling, so there is no unaccounted far-column norm.

## Membership in E2 and its actual graph

For functions supported in a fixed compact setK separated fromx=0, the E2 norm is bounded by a constant times their global bounded C^alpha norm. For weighted y differences the function is identically zero when|x| is below the positive distance ofK from the vertical axis; otherwise|x|^-2 is uniformly bounded. The x difference is already an ordinary Holder difference. Thus(4)-(5) give

 ||h_n||E2+||V_delta.grad h_n-h_n||E2<=C.              (6)

The normalized coupling B_delta=L_delta-(V_delta.grad-1) is boundedE2->E2 by proof 203, on exactly these global input norms. It follows thath_n belongs to the maximal domainD_delta and

 ||h_n||graph<=C.                                     (7)

This step controls the nonlocal linear image globally, including near both axes and the origin, where the input support argument alone would not apply. It uses the proved weighted coupling, not a presumption that the output remains supported inK.

EachN(h_n) is compactly supported inK, since the differentiated density is. For fixedn the density is smooth and compact, so its canonical velocity is smooth on every compact set; its full normalized product is smooth. Its support avoids the axes. HenceN(h_n) belongs toE2. There are no neglected nonlinear image or far-tail conditions. SinceK is inside the region wherechi_delta=1, the sameN(h_n) is obtained if the nonlinear term is also localized bychi_delta.

## The large transverse nonlinear term

We need the small velocity amplitude ofk_n, as well as its bounded Holder norm. The compact density estimates in(4)-(5) imply

 ||U[k_n]||infinity<=C n^-alpha(1+log n) ->0,
 ||U[k_n]||C^alpha(K')<=C                             (8)

on any fixed compact neighborhoodK' ofK. For the first bound, in a kernel ball of radius1/n subtract the density at the observation point and use its bounded alpha seminorm; the integral ofr^(alpha-2) with planar area isO(n^-alpha). Between radii1/n and a fixed radius use the density amplitudeO(n^-alpha), givingO(n^-alpha log n). Beyond a common support neighborhood use the absolutely integrable compact-source bound. The local point-multiplier term has the same amplitude. The compensator has sizeO(n^(-alpha-1)). The second bound follows from the same compact local C^alpha singular-integral estimate used in proof 199; its separated far part is smooth. These are uniform estimates, not an asymptotic plane-wave substitution.

On every inner flow tubeeta=1,grad d=0,U[d]=w, and the compensator vanishes with its derivatives. Sincec[h_n]=0, there

 N(h_n)=n^(1-alpha)Psi'(nz)(w+U[k_n]).grad z.          (9)

At every point of the trajectoryz=0 this is exactly0, becausePsi'(0)=0. On the neighboring trajectoryz=1/n, Psi'(1)=2 and(8) shows that(9) is at leastb_* n^(1-alpha) for largen, uniformly for0<=s<=tau. The two trajectories stay at distance at mostC/n. The local full C^alpha seminorm ofN(h_n) is therefore at leastc n.

For any functionf inE2, its C^alpha norm on a fixed compact set is bounded byC_K||f||E2. To see this, join two points by one horizontal and one vertical segment and use the two defining seminorms, with|x| bounded on these segments. Thus the preceding two-point lower bound implies

 ||N(h_n)||E2>=c_1 n.                                 (10)

The nonlinearity has a derivative transverse to the characteristic direction even though(6) controls the derivative along that direction.

## The local inverse cannot remove this transverse oscillation

Letg=L_delta^(-1)N(h_n). OnK the equation is

 V_delta.grad g-g=N(h_n)-U[g].grad rho0-(c[g]/3)X.grad rho0.

Proof 199 bounds the local C^alpha norms ofg andU[g] byC||g||E2, and proof 200 atp=2 gives|c[g]|<=(4/pi)||g||E2. The background coefficients are smooth on the fixed flow tubes. Therefore the right side excludingN(h_n), and its local Holder differences, are controlled byC||g||E2.

The equation has the following exact characteristic identity for0<=tau'<=tau:

 e^(-tau')g(Phi_(tau')X)-g(X)
 =integral_0^(tau')e^-s[N(h_n)-U[g].grad rho0
                          -(c[g]/3)X.grad rho0](Phi_sX)ds.  (11)

This is valid on the maximal distributional domain. In a smooth flow box a continuous distributional solution whose transport derivative is continuous satisfies the one-dimensional distributional fundamental theorem along flow time. It holds first for almost every transverse parameter and then for every parameter by continuity. This proves(11) without transverse differentiability ofg.

Subtract(11) for the initial pointsz=0 andz=1/n. By(9), the difference of the nonlinear integrals has absolute value at leastb_*(1-e^-tau)n^(1-alpha). All other endpoint and integrated differences are bounded byC||g||E2 n^-alpha, because the two trajectories areO(1/n) apart uniformly. Consequently||g||E2>=c_2 n, proving the final part of(1).

Finally definea_n=n^-1/2 h_n. Their graph norms tend to0 by(7), while exact quadratic homogeneity gives||N(a_n)||E2>=c_1 and||L_delta^(-1)N(a_n)||E2>=c_2. They retain exactJ=c=0 and the same compact support. This proves the stated discontinuity at0. Stronger norms may make this sequence unbounded before rescaling and are outside the conclusion. No nonexistence theorem for the IPM profile follows.

## Dependencies and audit scope

Proof 27 proves the compact transverse-potential construction and strip mechanism. Topics199-203 give the exact weighted input and coupling estimates and maximal localized inverse used here. Proof 201 identifies the canonical strain; the original inner modal expansion supplies the smooth flow boxes. Every membership and limiting step needed to apply the earlier mechanism toE2 is included above. No numerical computation is required. Independent independent cross-audit is requested before theory author integration.
