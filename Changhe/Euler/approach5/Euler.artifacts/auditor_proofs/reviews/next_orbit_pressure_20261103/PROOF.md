# The next pressure coefficient on an actual characteristic

## 1. Exact profile class, gauge and inputs

Fix2/5<c<1/2, finite omega, p=(1-c)/c, a=1-2c, b=2(1-c)=a+1, Jx=(-x2,x1,0), A=cI-omega J. Let U in C2(R3;R3), P in C1(R3) solve

    ((1-c)I+omega J)U+DU(Ax+U)+grad P=0, div U=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1). (1)

Use the actual pressure constant Pinf and normalized quantities

    B=Ax+U, H=P-Pinf+|U|²/2+(Ax).U,
    Q=P-Pinf-|U|²/2, g=U.B=H-Q.

The confirmed scattering theorem gives a C1 conjugacy Xi from the escaping region E onto D=R3 minus{0}, the complete B flow Phi_t, actual tails V,W=curl V,P2, X=Ax, k=X.V, S=P2-|V|²/2, and V in C^(1,alpha), P2 in C^(2,alpha) locally for every alpha<1. For x0 in D let y0=Xi^(-1)x0, y_t=Phi_t y0 and z_t=exp(-tA)y_t. Then z_t tends to x0; H,Q,g are bounded and tend to zero at infinity; y_t escapes every compact set forward. Also

    BH=-ag, e^(at)H(y_t)->k(x0), e^(bt)Q(y_t)->S(x0),
    if k(x0)=0, e^(bt)H(y_t)->-aS(x0).             (2)

Let R_t=exp(omega tJ), u_t=e^((1-c)t)R_t U(exp(tA)x), p_t=e^(bt)(P(exp(tA)x)-Pinf), S_t=p_t-|u_t|²/2. A539 gives u_t->V locally uniformly, S_t->S in C1 and e^t(u_t-V)->Z=DV V+grad P2 locally in positive Holder norms.

For Sections2-4 and8 assume additionally c!=3/7. A575 gives a unique continuous p1 on D satisfying

    p1(exp(tA)x)=e^(-(3-2c)t)p1(x),
    -Delta p1=partial_i partial_j(V_i Z_j+Z_i V_j).

After subtracting every pressure multipole of rate r_n=(n+5)c-2<1, e^t(S_t-S) tends locally uniformly to S1=p1-V.Z. A623 makes every such multipole zero under(1), so the same limit holds without subtraction. These inputs were reread in their full independent proofs. At c=3/7, an axisymmetric degree-four exterior harmonic function has the required homogeneity, and uniqueness fails; the actual resonant correction is not provided by these inputs. Every claim below involving p1 retains c!=3/7.

## 2. Exact second-order orbit asymptotic

Differentiating z_t and using B-Ax=U gives

    z_t'=e^(-t)u_t(z_t).

For large t the points z_t lie in a compact ball within D, so u_t(z_t)->V(x0) and is bounded. Integration to the terminal limit gives

    z_t-x0=-e^(-t)(V(x0)+o(1)).                    (3)

The pressure identity e^(bt)Q(y_t)=S_t(z_t) is exact. Suppose k(x0)=S(x0)=0. Taylor's integral formula, C1 convergence of S_t and(3) show

    e^t[S_t(z_t)-S_t(x0)]->-V(x0).grad S(x0).

Hence e^((b+1)t)Q(y_t) tends to

    sigma1=S1-V.grad S=p1-2V.grad P2              (4)

at x0: V.DV V=V.grad(|V|²/2) cancels the kinetic terms. From BH=-a(H-Q),

    (e^(at)H(y_t))'=a e^(at)Q(y_t).

Its terminal limit is k(x0)=0. Since b+1=a+2, the just-proved asymptotic makes the future integral absolutely convergent and yields

    e^((a+2)t)Q(y_t)->sigma1(x0),
    e^((a+2)t)H(y_t)->-(a/2)sigma1(x0),
    e^((a+2)t)g(y_t)->-((a+2)/2)sigma1(x0).       (5)

The errors in the integral are controlled by their supremum after time t, so integrating an o(1) coefficient is legitimate. If V(x0)=0 then sigma1(x0)=p1(x0).

## 3. Signs and derivative classification

The following exact inputs were independently confirmed in C47/C49. At a supported zero of W with range DW contained in R X0, one has g(y_t)<=0 for every real t. At a zero of W, DW is nilpotent and DW X0=0; if X0 belongs to its range then g=H=Q=0 along the whole orbit and k=S=0. Rank two implies that range condition. If V=W=0 and DW!=0, then DW=X0 tensor ell for a nonzero covector ell.

Consequently, at a supported W zero with DW=0 and k=S=0, equation(5) gives sigma1>=0. If X0 lies in range DW, it gives sigma1=0. On

    T0={V=DV=0,S=0} intersect supp W,

these alternatives exhaust the possibilities and sigma1=p1. Therefore p1>=0 on T0, with p1=0 wherever DW!=0. At a point where V is C2 and vanishes to infinite order, D²V=0 and DW=0. If p1>0 there, (5) gives H<0 and g<0 for every sufficiently large t. Thus identically zero work on that orbit requires p1=0.

Finally suppose W=0 at a supported point, k=S=0 and sigma1<0. Then DW cannot vanish and X0 cannot lie in its range. Also V cannot vanish, since the last derivative input would then force X0 into the range. Rank two is impossible, leaving rank one DW=w tensor ell. Nilpotence gives ell(w)=0; DW X0=0 gives ell(X0)=0, and w is not parallel to X0. This is precisely the source's transverse rank-one conclusion. It is conditional on sigma1<0, not a classification of every W zero.

## 4. Coefficient scope and the source status line

Theorem1 in the source explicitly starts with c!=3/7 and therefore includes part(c) within that restriction. Its requested-label line singles out(a),(b),(d) when mentioning that scope; this must not be read as removing it from(c). The source's separate current team note correctly gives the restriction for all Theorem1. No sign conclusion for a resonant p1 is certified here. The coefficient theorem also retains global zero helicity and natural derivative bounds because they supply A623 and the orbit sign law. Bare velocity decay alone does not supply these inputs.

## 5. Work on a forward-invariant open region

This section allows every c in the campaign interval, including3/7. Let O be open in E with Phi_t(O) contained in O for all t>=0, and O'=Xi(O). If g<=0 on O, then for every y in O, forward escape and BH=-ag give

    H(y)=a integral_0^infinity g(Phi_s y)ds<=0.      (6)

The improper integral exists because it equals the finite difference of H and its zero limit; its integrand has one sign. Equation(2) implies k<=0 on O' and S>=0 on O' intersect{k=0}.

If g=0 on O, the same argument gives H=Q=0 there and k=S=0 on O'. Suppose x1 in O' has V=DV=0. Choose a full ball about x1 inside O'. The actual Holder derivative gives |V(x)|<=C|x-x1|^(1+alpha). Also P2=|V|²/2 on that ball and P2(x1)=0. The sphere-mean argument below, with m=1+alpha>1 and delta=1/2, forces V=0 there. Thus x1 is not in supp W. An open forward-invariant zero-work neighbourhood cannot contain the preimage of a supported T-flat point. This does not show that zero work on one orbit extends to such a neighbourhood.

## 6. Sphere means and the finite-order criterion

Let v in C1 and pi in C1 on B_r0(0), div v=0, v(0)=0, and -Delta pi=partial_i partial_j(v_i v_j) in distributions. Suppose |v(x)|<=C|x|^m for a real m>0. Let E(r) be the spherical average of |v|², F(r) that of(v.n)², and

    Y(r)=average_sphere(pi-pi(0))+F(r).

The confirmed distributional spherical identity A1199 is Y'=(E-3F)/r. Continuity gives Y(0)=0, and 0<=F<=E<=C²r^(2m) gives

    Y(r)=integral_0^r(E-3F)(s)ds/s,
    |Y(r)|<=C²r^(2m)/m.                          (7)

If average_sphere(pi-pi(0))>=delta E for all0<r<r0 and delta>1/(2m), then Y>=delta E+F>=0 and Y'<=Y/(delta r). Therefore r^(-1/delta)Y is nonnegative and nonincreasing, while(7) makes its limit at zero equal zero. It is identically zero. Hence E=0 at every radius and v=0 on the entire ball. An infinitely flat v permits any fixed delta>0 by choosing m large enough. No pointwise pressure sign was assumed.

## 7. Sharpness correction and the actual C1 threshold

The source says the threshold is sharp using v=rho^(m-1)Jx, pi=|v|²/(2m). This field is C1 at the axial line for m>=1, but not for0<m<1: its nonzero transverse derivative has size comparable to rho^(m-1). Thus this example establishes sharpness for m>=1 only. The source's unrestricted sharpness wording is false over its entire stated m>0 range; the theorem itself remains valid.

In fact the best threshold for the displayed C1 class with a given m>0 is

    delta_crit=1/(2 max(m,1)).                     (8)

For m<1, C1 regularity and v(0)=0 imply |v|<=C|x|, so Section6 with exponent1 proves exclusion for delta>1/2. For m>=1 Section6 applies directly. Sharpness at equality follows from the same swirl with exponent M=max(m,1): it is C1, divergence free, satisfies the pressure equation and |v|<=C|x|^m on a fixed small ball, and pi=|v|²/(2M). Its full stationary acceleration is canceled by grad pi, so the pressure equation is exact.

There is also a useful endpoint strengthening. If |v(x)|=o(|x|^m) and delta=1/(2m), then E=o(r^(2m)), and integration in(7) gives Y=o(r^(2m)). The same monotonicity proof at equality forces v=0. This explains directly why a nonzero C1 equality example cannot have0<m<1: every such v is o(r^m).

## 8. What flatness says about the next pressure mean

Retain c!=3/7. If V and P2 are smooth and infinitely flat at x0, then Z=DV V+grad P2 and M1=V tensor Z+Z tensor V are smooth and infinitely flat. The distributional equation for continuous p1 has smooth right side near x0, so local elliptic regularity makes p1 smooth there and Delta p1 infinitely flat. The spherical mean equation

    (r² mean(p1)'(r))'=r² mean(Delta p1)(r)

integrated twice gives mean(p1)=p1(x0)+O(r^N) for every N, after raising the order in the right-hand bound. Thus at a common-flat T0 point its pressure-correction means are nonnegative up to errors smaller than every power.

This is not a lower bound for the leading pressure mean used in Section6. The exact leading rescaling relates that mean on a sphere about x0 to original pressure means on spheres of radius e^(ct)r about exp(tA)x0. Those are whole spheres, whereas(5) gives data on one characteristic. No implication from those orbit data to the required mean inequality has been proved. The unrestricted common-flat configuration remains open.

## 9. Evidence and dependencies

All C50 sections through5.4, A575's full finite-part proof and A623's full independent proof were read. Sources and hashes are pinned under verification. The derivation uses confirmed scattering, C47/C49 and A1199, preserving every hypothesis needed by them. No new computation or formal build was needed. C50 is work from the existing configured model agent; the actual provider runtime remains unattested. Section7 supplies an independently checked correction and sharpening for exchange through those working files. No new model client was used.
