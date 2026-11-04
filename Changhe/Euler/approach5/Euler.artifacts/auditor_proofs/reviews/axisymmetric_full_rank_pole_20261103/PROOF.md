# Axisymmetric common polar zeros under the full rank system

## 1. Exact statement and dependencies

Fix 0<c<1/2 and any real omega. Put p=(1-c)/c>1, d=p-1>0, b=2-p, q=2p/d>2, Jx=(-x2,x1,0), A=cI-omega J and lambda=2p(2p-1). Let

    G={r n: r_-<r<r_+, n in S^2, n3>z_*},
    0<r_-<1<r_+, -1<z_*<1.

Suppose V and P2 are C-infinity on G. Require V to be axisymmetric as a vector field and ordinarily homogeneous of degree -p, and P2 to satisfy P2(exp(tA)x)=exp(-2(1-c)t)P2(x) whenever the local orbit segment is in G. Write W=curl V, k=(Ax).V, S=P2-|V|^2/2. Assume

    div V=0, V.W=0, -Delta P2=tr((DV)^2), W.grad S=0,
    grad k cross grad S=0 wherever W!=0.

If V(e3)=W(e3)=0, then V=0 throughout G. This confirms LIT229 and implies LIT228, whose infinite-flatness hypothesis is stronger and whose c range is narrower.

The only previously proved substantial input is the swirl-elimination theorem A1296-A1302, in the team records: under these pressure, transport, homogeneity, helicity and axisymmetry hypotheses, W(e3)=0 eliminates the azimuthal velocity on the whole cap. Its proof works for every p>1. The pressure lemma used here is also proved again in Section7. All other continuation and algebraic steps are supplied below.

## 2. Averaging preserves the rank identity

Let R_alpha denote the axial rotation. Average P2(R_alpha x) over alpha in [0,2pi]. The resulting Pbar is smooth and axisymmetric. Since V and W are equivariant, the source tr((DV)^2) is invariant, and W.grad S is preserved by pullback and averaging. Twisted homogeneity and a change in the averaging angle give Pbar(r n)=r^(-2p)u(n3).

The scalar k is invariant. At each vortical point, applying R_alpha inverse to the rank equation at R_alpha x gives

    grad k(x) cross grad_x[S(R_alpha x)]=0.

The vortical set is rotation invariant. Consequently the rank identity holds for Sbar=Pbar-|V|^2/2 at the same points. No averaging of a quadratic velocity expression is performed.

Use the swirl-elimination input. With z=cos(theta), w=1-z^2 and s=sqrt(w), the remaining meridional field has the form

    V=r^(-p)[R(z)e_r+H(z)e_theta/s], H'=bR,
    W=r^(-p-1)G0(z)e_phi/s, G0=wR'-dH,
    k=c r^(1-p)R, e=(R^2+H^2/w)/2,
    Pbar=r^(-2p)u, Sbar=r^(-2p)h, u=e+h.

Here and below primes denote z derivatives. All coefficient functions are smooth on (z_*,1), and H(1)=R(1)=0 by smoothness and V(e3)=0.

## 3. Pressure and the scalar rank residual

In the orthonormal spherical frame, the dimensionless velocity derivative is

    M=[-pR, -sR'-H/s, 0;
       -pH/s, dR-zH/w, 0;
       0, 0, R+zH/w].

Squaring and tracing, using H'=bR, gives

    T=tr(M^2)
     =2(p^2-p+1)R^2+2b zRH/w+2z^2H^2/w^2
        +2pHR'+2pH^2/w.

Thus the exact pressure equation is

    (w u')'+lambda u=-T.                                      (1)

The radial-polar determinant in the rank equation gives

    grad k cross grad Sbar=c d s r^(-3p-1)L e_phi,
    L=Rh'-q hR'.                                               (2)

Therefore L=0 on the open set {G0!=0}. The following extension uses ordinary analytic differential equations only inside the angular interval. It assumes no analyticity at the pole.

## 4. Extension through all irrotational intervals

First suppose G0 is identically zero on (z_*,1). Then H'=bR and R'=dH/w. For a sufficiently small epsilon>0, set M_epsilon=sup_[1-epsilon,1]|R|. The endpoint data imply

    |H(z)|<=|b|(1-z)M_epsilon,
    |R'(z)|<=d|b|M_epsilon/(1+z),
    M_epsilon<=d|b|epsilon M_epsilon/(2-epsilon).

Choose epsilon<min(1,1-z_*) making the last coefficient less than1. Then R=H=0 there, and uniqueness of the regular linear system propagates zero across the entire open interval. At b=0 the same estimates give H=0 and R'=0 directly.

Now suppose G0 is not identically zero. Let O=int{G0=0} in (z_*,1). The complement of O is the closure of {G0!=0}; hence every derivative of L vanishes there. Each component I of O has at least one endpoint z0 strictly inside (z_*,1), since I is not the whole interval.

On I the pair (R,H) solves the analytic linear system R'=dH/w, H'=bR. At z0 its coefficients are regular and its limiting data are finite. Solve the analytic initial-value system across z0. The convergent iterated-integral series on a small complex disk avoiding +/-1 supplies analyticity; uniqueness for the real linear equation identifies its restriction with the original (R,H). On I, substituting R'=dH/w into T makes the source in (1) analytic in this extended pair. The regular second-order pressure equation with the limiting data u(z0),u'(z0) therefore extends u analytically as well.

It follows that h=u-e and L extend analytically across z0. Their derivatives there agree with the original smooth one-sided limits. All L derivatives at z0 vanish, so its analytic Taylor series is zero and L vanishes near z0. Analyticity throughout connected I gives L=0 on I. This argument applies separately to every component, including infinitely many. Consequently L=0 everywhere on (z_*,1).

## 5. The meridional endpoint quadratic

On each component I of {R!=0}, integration of L=0 gives h=C_I|R|^q for one finite real C_I. Suppose z0 is an interior endpoint. Write D=R'(z0), H0=H(z0), w0=1-z0^2. Since q>2, h,h',h'' tend to zero at this endpoint; this uses the fixed component constant, not any uniform bound across components.

Since H'=bR, H'(z0)=0 and H''(z0)=bD. Direct differentiation of e gives

    e(z0)=H0^2/(2w0), e'(z0)=z0H0^2/w0^2,
    e''(z0)=D^2+bH0D/w0+H0^2(1/w0^2+4z0^2/w0^3).

Substituting into (1) yields

    w0D^2+(p+2)H0D
      +[(2p^2+p+1)/w0+4z0^2/w0^2]H0^2=0.                       (3)

The first diagonal coefficient is w0>0. Four times the determinant is 7p^2+16z0^2/w0>0, so D=H0=0. This calculation does not require the endpoint itself to be vortical. The extended rank relation is what permits its use at every endpoint.

## 6. Endpoint uniqueness and a single scalar constant

The source admits the exact decomposition

    T=(2pHR)'+T0,
    T0=2(2p-1)dR^2+(2p/w+2z^2/w^2)H^2+2b zRH/w.

Indeed subtracting 2pbR^2 from the original R^2 coefficient gives 2(2p-1)d. The pressure equation becomes

    (w u'+2pHR)'=-lambda u-T0.                                 (4)

On the fixed nonzero R component close enough to z0, u=e+C_I|R|^q is nonnegative and at least a0(R^2+H^2) for some a0>0. Both |2pHR| and |T0| are at most C0u. Equation (3) gives u(z0)=u'(z0)=0. Integrating (4) and using a positive lower bound for w gives, in a coordinate t measuring distance into that component,

    |du/dt|<=C1[u(t)+integral_0^t u(v)dv].

Set F(t)=u(t)+integral_0^t u(v)dv. Then F>=0, F(0)=0 and F'<=C2F. Multiplication by exp(-C2t) and integration show F=0. This contradicts R!=0. The same argument with reversed coordinate handles either endpoint orientation.

Thus no nonzero R component has an interior endpoint. Either R=0 everywhere, in which case H'=0 and H(1)=0 give V=0, or R is nonzero on the whole punctured cap. In the latter case there is a single finite constant C with h=C|R|^q.

## 7. The second-order pressure contradiction

In the nonzero alternative, |Sbar|/|V|^2<=|C||R|^(q-2) tends to0 at the pole, uniformly in the other local coordinates. In particular Pbar(e3)=0 and Sbar>=-|V|^2/8 on a full Euclidean ball about e3 contained in G.

Let M0=DV(e3). Axisymmetry makes it commute with every axial rotation, so

    M0=[alpha,-beta,0; beta,alpha,0; 0,0,gamma].

Homogeneity gives M0e3=-pV(e3)=0, divergence gives 2alpha+gamma=0, and W(e3)=2beta e3=0. Thus M0=0 and V(e3+y)=O(|y|^2).

For completeness, let v,pi be any smooth divergence-free Poisson pair on a ball, with v(0)=Dv(0)=0 and pi-pi(0)-|v|^2/2>=-|v|^2/8. Let E(r) and A0(r) be the spherical averages of |v|^2 and (v.n)^2, and let Y(r)=average(pi-pi(0))+A0(r). Spherical integration of -Delta pi=div div(v tensor v), with its integration constant zero by smoothness, gives Y'=(E-3A0)/r. Since E,A0=O(r^4) and Y(0)=0, Y=O(r^4). The deficit gives Y>=3E/8+A0>=0; hence Y'<=8Y/(3r). The function r^(-8/3)Y is nonnegative and nonincreasing, with limit0 at the center. Therefore Y=E=0 and v=0 near0.

Apply this lemma to V,Pbar. It contradicts nonzero R throughout the punctured cap. The zero alternative is therefore the only one. This proves the exact theorem in Section1 for every p>1, including b=0 and b<0.

## 8. The condition W(e3)=0 cannot simply be deleted

Here is an exact local countermodel to deleting that condition from this necessary-system theorem. Fix any p>1 and beta!=0. Set y=1-z, w=y(2-y), kappa=2p(2p+1). Let

    g(y)=sum_(n>=1) a_n y^n, a_1=2beta^2,
    a_(n+1)=[n(n-1)-kappa] a_n/[2n(n+1)].

The ratio tends to1/2 unless the series terminates, so the series converges for |y|<2. It satisfies w g_yy+kappa g=0. Since g/w is real analytic and equals beta^2 at y=0, choose a small full polar cap on which it is positive, and put

    V=r^(-p) sqrt(g/w) Jn,
    P2=|V|^2/2, S=0.

This field is smooth through the pole, ordinarily homogeneous and axisymmetric, divergence free and helicity free. For a purely azimuthal velocity with squared azimuthal amplitude g, the pressure equation for P2=|V|^2/2 reduces exactly to w g_zz+(lambda+4p)g=0. Since lambda+4p=kappa, Poisson holds. Both scalar equations, including the full rank relation, hold because S=0. Axisymmetry makes twisted homogeneity hold for every omega. We have V(e3)=0 but DV(e3)=|beta|J and W(e3)=2|beta|e3!=0. All the theorem's other local conditions are satisfied. This is a local necessary-system pair, not a claim of an original Euler profile.

## 9. The condition V(e3)=0 cannot simply be deleted

Put l=1-p<0 and define an analytic scalar f near y=0 by

    f(y)=sum_(n>=0) a_n y^n, a_0=1,
    a_(n+1)=[n(n+1)-l(l+1)]a_n/[2(n+1)^2].

Again the series converges for |y|<2 or terminates. It solves

    y(2-y)f_yy+2(1-y)f_y+l(l+1)f=0.

Consequently phi=r^l f(1-z) is harmonic on a small full polar cap. Set V=grad phi and P2=-|V|^2/2. Then V is smooth, axisymmetric, homogeneous of degree -p, and both divergence free and curl free. Since DV is symmetric, Delta(|V|^2/2)=|DV|^2=tr((DV)^2), giving the required Poisson equation. All vorticity and rank equations are vacuous since W=0. Twisted homogeneity holds for every omega. At the pole V(e3)=l e3!=0, whereas W(e3)=0. Thus the other point condition also cannot be removed from the exact local theorem.

## 10. Scope and verification

Both eight-section source proofs were read in full. The averaging, interval analytic continuation, endpoint quadratic, source decomposition, Gronwall argument, pole contraction and pressure contradiction were independently reconstructed above. Sections8-9 are additional exact countertests with convergent series, not numerical observations. No numerical experiment or formal build was run.

The theorem requires smooth axisymmetric velocity on a full cap. The two-dimensional orbit space of a nonaxisymmetric field does not supply the regular one-dimensional endpoint used in Section4. Neither the bare-decay conjecture nor its arbitrary-helicity version follows. General nonaxisymmetric common-flat completion with the full rank identity remains open.
