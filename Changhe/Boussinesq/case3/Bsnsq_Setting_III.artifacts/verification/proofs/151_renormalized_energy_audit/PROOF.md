# Renormalized energy: the cubic boundary term and its precise scope

Status: CONFIRMED for the statements and hypotheses below. The argument was written before its independent controls. There are181 passing exact controls and two complete written reviews returned by Claude Opus5.5; their dependency limits are recorded in verification/SUMMARY.md. No B2 endpoint is asserted.

## 1. Statement and notation

Let beta>2, s=1/beta, m=1-2s. Let Psi,Theta be smooth on R², Psi odd and Theta even under (x,y)->(-x,y), with no assumed y-reflection. Put Omega=-Delta Psi, V=(-Psi_y,Psi_x), V(0)=0, W=beta X+V, f=W.grad Omega+Omega-Theta_x and t=W.gradTheta-(beta-2)Theta. All unqualified stream functions in this proof are relative stream functions. Set D_R={|X|<R}, n=X/R and

    E_R=int_D_R (|grad Psi|²/2+y Theta).

For every R>0,

    int_D_R Psi f = -(4beta-2)E_R + B_R - int_D_R y t,       (1)

where

    B_R=int_boundary [Psi Omega W.n
        + beta((X.gradPsi)Psi_n - |gradPsi|² X.n/2)
        + (2beta-1)Psi Psi_n - Psi Theta n_x + yTheta W.n].  (2)

Suppose additionally t=0, Psi and Theta have finite power/log expansions with the degrees in150, with only homogeneous harmonic terms Cx and D x/r² outside the ordinary degree family, and remainders

    delta Psi in S^(2-mu), delta Theta in S^(1-s-mu),
    4-s < mu < 4.                                         (3)

Here S^a means |D^j f(X)|<=C_j r^(a-j) outside a ball for every fixed j. The actual fields obey Psi in S^(2-s), Theta in S^m. Then E_R has an expansion in finitely many powers and logarithms, plus a constant and o(1). Denote its constant coefficient by E_fp. The boundary has the analogous expansion. If f is compactly supported, then

    (4beta-2)E_fp = [R^0(log R)^0]B_R - int_R² Psi f.       (4)

Let

    Z_E={M/N>2 : M,N positive coprime integers, N<=4}.

For beta notin Z_E,

    (4beta-2)E_fp = -2pi beta C D - int_R² Psi f.           (5)

In particular a profile, f=t=0, satisfying these hypotheses has E_fp=0: by149 its D=0 outside Z_E, since the smaller impulse exceptional set is contained in Z_E. This is only a necessary condition, not a sign contradiction or existence result. The finite-part operation here is the constant coefficient in disks centered at the material center; changing the center or cutoff convention requires a new calculation.

The same conclusion applies to a class A profile from150: its proof's finite induction can be continued to the stronger depth(3), as established below. No assumption of absolute finite kinetic or potential energy is made.

## 2. The exact disk identity

Use div W=2beta and V.gradPsi=0:

    int Psi W.gradOmega
      = int_boundary Psi Omega W.n - beta int Omega X.gradPsi
        -2beta int Psi Omega.

Also

    int Psi Omega=int |gradPsi|²-int_boundary Psi Psi_n,
    int Psi(-Theta_x)=-int_boundary Psi Theta n_x+int V_2 Theta.

The two-dimensional Pohozaev identity is

    int DeltaPsi X.gradPsi
      =int_boundary [(X.gradPsi)Psi_n-|gradPsi|² X.n/2].

It follows by integrating the divergence of
(X.gradPsi)gradPsi-X|gradPsi|²/2; its interior zeroth-order dimension term is zero in dimension two. Finally, without assuming t=0,

    div(W yTheta)=(4beta-2)yTheta+V_2Theta+y t.

Substitute these four identities. The coefficient of int |gradPsi|² is1-2beta and that of int yTheta is-(4beta-2). This gives(1)-(2), including the sign of the residual correction. No integration at infinity was used.

## 3. The cubic flux cannot be discarded

With x=r cos(alpha), y=r sin(alpha), V.n=-Psi_alpha/r. Therefore the first boundary flux contains

    int_boundary Psi Omega V.n = -int_0^(2pi) Psi Omega Psi_alpha d alpha.  (6)

It is cubic in Psi, and has no universal cancellation from x-reflection. For an exact smooth polynomial example use

    Psi=x(x²+y²)+2xy,
    Omega=-8x,
    Theta=0.

It has the required x parity and gradPsi(0)=0. On r=R, Psi=R³cos alpha+R²sin(2alpha). Substitution in(6), with integral cos²alpha cos(2alpha)=pi/2 and integral sin(2alpha)cos alpha sin alpha=pi/2, gives

    int_boundary Psi Omega V.n = 4pi R^6,                (7)

which is nonzero. The example is only a boundary-identity control: its velocity has superlinear growth and it is not an admissible B2 profile. If an admissible symbol-class counterexample to the cancellation is wanted, multiply this Psi by a smooth radial cutoff equal1 near the chosen circle and at0, and0 outside a larger ball. The value(7) on that circle is unchanged; the resulting relative velocity is compactly supported and canonical by harmonic uniqueness. The full vorticity equation is not asserted.

Thus a list of powers for B_R that includes only stream pairs omits a genuine term. This omission does not change Z_E, but must be repaired in the argument.

## 4. Boundary power count and errors

A homogeneous term r^e times a polynomial in log r will be called a stream term of degree e, even when it is a resonant particular solution. Derivatives preserve the stated power after their explicit radial factors are counted; they may lower the log degree. The boundary terms have the following powers:

- quadratic stream terms: e+e';
- cubic stream terms in(6): e+e'+e''-2, where the Omega factor comes from the Laplacian of the e' stream term;
- temperature-stream terms: g+e+1;
- the linear temperature term beta int_boundary yTheta X.n: g+3.

These follow directly from ds=R d alpha, Omega degree e'-2, gradPsi degree e-1, y degree1 and X.n degree1. If a middle factor in(6) is harmonic its Laplacian is zero, so that contribution is absent, not an extra collision.

Every replacement of an actual field by its expansion has a vanishing boundary error under(3). The largest quadratic error is O(R^(4-s-mu)); the cubic errors are O(R^(4-2s-mu)); the linear temperature error is O(R^(4-s-mu)). Temperature-stream errors have at most O(R^(4-2s-mu)). Multiple remainder factors only improve the powers. The critical bounds Psi in S^(2-s), Theta in S^m and the strict inequalities in(3) handle the remaining polynomial logarithms. Since all powers are negative, these errors are o(1).

For the energy itself, the difference between actual and truncated energy densities is O(r^(2-s-mu)). It is integrable on the exterior because its radial measure gives exponent3-s-mu<-1. Each truncated power/log density can be integrated explicitly in r, including a logarithmic primitive when its radial integral has power zero. Consequently E_R has the asserted finite expansion, a constant and o(1). The interior and the integrable remainder contribute to that constant and cannot be dropped. For compact f, the left side of(1) is eventually the fixed integral int Psi f. Taking the constant coefficient gives(4).

## 5. Exceptional set and the harmonic pair

The ordinary stream degrees are2-Ks-n, K>=1,n>=0; the temperature degrees are1-Ls-n, L>=2,n>=0. Indices are integers. Homogeneous harmonic terms here have degrees1,-1 and no logarithms; the normalization in150 separates them from resonant particular solutions.

For two ordinary streams the boundary power is4-K_tot s-n_tot; with one harmonic stream it is3-Ks-n or1-Ks-n. For three ordinary streams the cubic power is4-K_tot s-n_tot. With two ordinary streams and one harmonic it is3-K_tot s-n_tot or1-K_tot s-n_tot. With one ordinary and two harmonics it is2-Ks-n, -Ks-n or-2-Ks-n. At least one stream in a nonzero cubic term is ordinary, because its middle Laplacian cannot be harmonic. All-harmonic cubic terms vanish. A temperature and ordinary stream give4-(K+L)s-n_tot; a temperature and harmonic give3-Ls-n or1-Ls-n; the linear temperature term gives4-Ls-n.

For all these terms a zero power requires K s=d for a positive integer d<=4. Thus beta=K/d reduces to a rational with denominator<=4. Conversely each reduced beta=M/N>2,N<=4 is allowed by the formal linear-temperature count: take L=M,n=4-N. This proves that Z_E is exactly the set of possible ordinary collisions in this bookkeeping. It does not assert that any such coefficient is nonzero in an exact profile. Smoothness and the PDE can impose additional cancellations. Differentiation of logarithms changes only log degrees, so it cannot create a zero radial power outside Z_E; at an exceptional beta, all log-free contributions must be retained.

Outside Z_E, only the harmonic quadratic pair Cx and D x/r² can contribute at zero power. Both are harmonic, so they do not enter Psi Omega. On r=R write

    Psi=C R cos alpha+D R^-1 cos alpha,
    Psi_r=C cos alpha-D R^-2 cos alpha,
    Psi_alpha=-C R sin alpha-D R^-1 sin alpha.

The constant coefficient of (beta/2)(R²Psi_r²-Psi_alpha²) is -beta C D at each angle. The cross terms in R Psi Psi_r cancel. Integrating gives -2pi beta C D. This proves(5).

## 6. The stronger expansion follows from150

The induction in150 improves a vorticity remainder weight mu to any mu' in(mu,mu+s), avoiding the locally finite degree set, and uses a Poisson estimate valid for mu<4 except1,3. The induction remains applicable on either side of3. The selected weight3 is excluded, so a step crosses that value without using it. Instead of stopping at the first mu>3, continue the same finite iteration while mu<=4-s. Before crossing that target select mu' in(mu+s/3,mu+2s/3), avoiding the finite excluded set in that interval. The first crossing satisfies

    4-s < mu' < 4-s/3 < 4.

There are finitely many steps because each increases the weight by at least s/3. The harmonic terms needed remain exactly Cx and D x/r². This establishes(3) for every exact exterior solution with the full symbols of150, including its class A application and the compact-residual configurations135 or148. It does not claim an infinite convergent expansion.

## 7. What positivity alone does not show

Here is a precise weaker sign test, not a sign-changing family in the nontrivial B2 class. Let Theta=0 and Omega=x f(r), where f>0 is smooth as a radial function on R² and equals r^(-s-1) for r>=1. Define

    I(r)=int_0^r t³ f(t)dt,
    h(r)=-int_0^r I(t)t^-3dt,
    Psi=x h(r).

These smooth fields have the x parity, canonical relative velocity, V(0)=0, sublinear velocity, positive vorticity on x>0, and exact thermal equation. They do NOT have a0!=0 or the B2 center strain, and they need not solve the vorticity equation. For r>=1 put

    A=1/((3-s)(1-s)),
    C=(1/(1-s)-int_0^1 t f(t)dt)/2,
    D=(int_0^1 t³ f(t)dt-1/(3-s))/2.

Then h=-A r^(1-s)+C+D/r². Direct polar integration yields

    E_R=(pi/2)[R²h(R)²+int_0^R I(r)²r^-3dr],

and hence

    E_fp=(pi/2)[2CD+int_0^1 I²r^-3 dr
          -1/((3-s)²(4-2s))-4D/((3-s)(1-s))+2D²].        (8)

There is no exceptional collision in this three-term formula for0<s<1/2. To obtain E_fp>0, choose positive smooth f equal the prescribed tail on a shrinking collar of r=1, and tending uniformly to0 away from that collar. It can be constant near0 and glued with smooth cutoffs, so all radial smoothness requirements hold. Both weighted moments and the integral of I²r^-3 tend to0; near0 use I(r)<=C r^4 for each construction, or the uniform bound f<=C to dominate. The bracket in(8) tends to

    (3-s)^-2[(1-s)^-1-(4-2s)^-1]>0.

For a negative example fix such an f and add lambda b, where b>=0 is a nonzero smooth bump in an annulus strictly inside(0,1). As lambda grows the coefficient of lambda² in the bracket in(8) is

    -(1/2)int_(0<t<r<1) r t(r²-t²)b(r)b(t) dt dr <0.           (9)

To verify(9), set A_b=int r b(r), B_b=int r³b(r), I_b=int_0^r t³b(t). The coefficient is -A_b B_b/2+int I_b²r^-3+B_b²/2. Integration by parts gives int I_b²r^-3=-B_b²/2+int I_b r b(r). Split the double integral for A_b B_b into t<r and r<t and subtract. The result is(9), including the factor1/2. Strict negativity follows because a nonzero smooth nonnegative bump is positive on an interval, which contains pairs t<r of positive measure.

Thus both signs occur under the weaker assumptions stated at the start of this section. This does not prove sign indefiniteness after the nontrivial temperature jet and the full profile equations are imposed. In particular the example Theta=0 cannot be described as strictly positive temperature or as a profile with a0!=0.


## 7a. The stronger sign test with D=0

The radial family also permits both signs with D fixed at0. This is the stronger claim in the lead's draft4.37(c), independently checked here after the first complete version of sections1-8. It still has Theta=0 and c=Psi_xy(0)=0, so it does not meet the nonzero-temperature B2 center data.

Set M=1/(3-s). Choose the positive smooth small-core background f_epsilon of section7, equal r^(-1-s) for r>=1, with J_epsilon=int_0^1 r³ f_epsilon<M and Q_epsilon=int_0^1 I_epsilon²r^-3<M²/(4-2s). Such a choice exists since both quantities tend to0. Let B=M-J_epsilon>0. Choose any smooth nonnegative radial bump b supported strictly below1, normalized by int_0^1 r³b(r)dr=1, and replace f_epsilon by f_epsilon+B b. Then I(1)=M and D=0 exactly. Formula(8) reduces to

    E_fp=(pi/2)[int_0^1 I(r)²r^-3dr-M²/(4-2s)].          (10)

For a negative example concentrate b in (1-delta,1), away from the endpoints. The cumulative added mass is zero below1-delta and at mostB inside the shell. Its change to int I²r^-3 is bounded by a constant times delta, since I_epsilon and B are bounded and r>=1-delta. Thus as delta tends to0 this integral tends to Q_epsilon, strictly below the threshold. The field remains strictly positive, smooth and exactly matched to its original tail.

For a positive example concentrate b in (0,delta), using a smooth function of r² near0 and a flat outer cutoff, then normalize its third moment. For delta<=r<=1 the added cumulative mass is exactlyB. Therefore

    int_0^1 I²r^-3 >= B² int_delta^1 r^-3dr
                         = (B²/2)(delta^-2-1),

which exceeds the fixed threshold for sufficiently small delta. Every individual f is finite and smooth at0, even though the family has no uniform bound there. Convex interpolation between a fixed negative example and a fixed positive example preserves f>0, the tail, radial smoothness and I(1)=M. The energy in(10) is continuous under this interpolation, so one such field also has E_fp=0 and D=0.

All these fields violate the vorticity equation on the exterior. Direct differentiation there gives, for D=0,

    f_res=x y [2 r^(-2s-2)/((3-s)(1-s))
                       -(s+1) C r^(-s-3)].              (11)

The two radial powers differ by1-s>0 and the first coefficient is nonzero. Hence this function cannot vanish identically on any exterior open annulus. This establishes the nonprofile qualification without inferring it merely from a missing center condition. In these examples f_res is not compactly supported, and int |Psi f_res| diverges at infinity: on a fixed angular sector where x and y are bounded below in absolute value by a positive multiple of r, the leading product has size comparable to r^(2-3s), whose planar integral diverges. Thus the compact-residual hypotheses of(4)-(5) fail. These fields test positivity alone and do not contradict those identities.

## 8. Observer and gauge scope

The canonical object in B2 is V=U-U(0). An observer change that adds a common vertical constant to U and U(0) leaves V, Psi_rel, W and E_fp unchanged. It is therefore unnecessary and incorrect to modify W by an independent constant while still claiming the same relative equation.

For comparison only, replace the integrand's velocity by V+v e_2, keeping the relative coordinates and Theta fixed. Then

    E_R(v)-E_R(0)=v int_D_R V_2 +(pi/2)v²R²,
    int_D_R V_2=int_boundary Psi n_x.

Under(3), outside Z_E the last boundary integral has constant coefficient pi D: ordinary stream terms could contribute only if e+1=0, which is an exceptional collision already excluded. Thus E_fp(v)-E_fp(0)=pi v D. In particular it vanishes when D=0. This is a comparison of two disk integrands, not a derivation of an absolute-frame stationary energy identity. A physical shift of the spatial origin also changes yTheta and requires its own transformed temperature field and cutoff; no claim about that operation is needed or made here.

Dependencies: elementary disk integrations by parts; finite power/log integration; packet150's finite Poisson/transport induction and its full-symbol hypotheses; packet149's renormalized impulse theorem. Numerical controls are implementation checks, never a substitute for these arguments. The broad existence question remains OPEN.

Written UTC 2026-10-21T09:36:41.323228+00:00.

## 9. Independent audit of the lead's draft4.37

The draft at analysis/notes/entries/e437_draft.txt was read in full, together with the separate derivation, after the independent identity and controls above were written. No lead or NUM code was executed or imported. Its displayed disk identity agrees with(1) when t=0. Its proof already includes the cubic term, repairing the omission in the earlier request energy437. The sign formula in(c) is(10), and section7a supplies its full smooth concentration proof and its explicit nonprofile check. The statement only claims positive Omega; it does not claim positive nontrivial Theta. That scope is correct, but a reminder that c=a0=0 makes the excluded B2 center hypotheses easy to see.

The draft allows homogeneous harmonic stream degrees h<=-2 in addition to1,-1. They cannot contribute a zero power in the boundary polynomial: paired with an ordinary term the power is at most-Ks<0; in a cubic product with two ordinary terms it is at most-K_tot s<0; with one ordinary and another harmonic it is at most-1-Ks<0; with temperature it is at most-Ls<0. Pure harmonic cubic terms vanish. Pairs of harmonics have sum<=-1 if one degree is<=-2. Thus the draft's more inclusive harmonic list has the same result and exceptional set.

Its stated remainder bounds deltaPsi=O(r^-2-eps) through two derivatives and deltaTheta=O(r^-3-eps) are sufficient, and stronger than necessary. The boundary errors are O(r^-s-eps) for stream pairs, O(r^-2s-eps) for triples and mixed terms, and O(r^-eps) for the linear temperature term. The energy error is integrable. These facts confirm its conditional theorem as stated.

For the class A scope, the present proof establishes a sharper result than that draft currently reports: replace those sufficient remainder bounds by(3), with derivatives of deltaPsi through order2 and the displayed undifferentiated deltaTheta bound. Section6 and150 then establish the expansion for class A profiles. This does not assert that150 has proved the draft's stronger O(r^-2-eps) stream remainder. Either retain the conditional theorem as written, or change to the proved weaker sufficient depth before removing the premise. With that change, the class A conclusion E_fp=0 outside Z_E is automatic from the actual equations and symbols. The result remains a necessary scalar identity, never a full-class nonexistence argument.

Draft4.37 audit and D=0 extension written UTC 2026-10-21T09:40:26.284186+00:00.

Final scope and verification completed UTC 2026-10-21T09:47:44.095535+00:00. The lead has reserved4.38 for energy and4.37 for packet150; references to the earlier draft4.37 in sections7a and9 identify its historical filename, not the final numbering.
