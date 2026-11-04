# Planar translation-invariant tails have no internal velocity zero

## 1. Exact local theorem

Fix 0<c<1/2 and finite omega. Set p=(1-c)/c>1, d=p-1, tau=omega/c, A0=1+tau², alpha=d/A0, beta=d tau/A0, a=1-2c, b=2(1-c), q=b/a=2p/d>2, J(x,y,z)=(-y,x,0), X=(cI-omega J)x. Let G be a product of connected open intervals in the one-to-one local coordinates(log rho,theta,z), where rho>0 and theta=phi+tau log rho. Let I denote the theta interval.

Suppose V,P2 are smooth on G, V3=0, partial_z V=0, and, with W=curl V, k=X.V and S=P2-|V|²/2,

    div V=0, X.grad V=-(1-c)V-omega JV,
    X.grad P2=-bP2, -Delta P2=tr((DV)²),
    W.grad S=0, grad k cross grad S=0 on {W!=0}.       (1)

Then V is identically zero or nowhere zero on G. No finite-order zero, uniform component constant, component count, axisymmetry or full momentum equation is assumed. Smoothness and planar axial translation invariance are actual restrictions. Section8 gives nonzero local full-Euler examples, so this is precisely a no-zero theorem in its stated class.

## 2. Angular reduction and the irrotational case

Differentiating the moving cylindrical basis in vector homogeneity gives

    V=rho^(-p)(R(theta)e_rho+T(theta)e_phi).

Define K=R-tau T and L=tau R+T. Then R=(K+tau L)/A0, T=(L-tau K)/A0. Direct cylindrical divergence and curl give

    L'=alpha K+beta L,
    W=rho^(-p-1)Z e3, Z=-K'+beta K-alpha L,
    k=c rho^(-d)K, |V|²=rho^(-2p)E,
    E=(K²+L²)/A0.                                    (2)

Indeed the divergence factor is -dR+tau R'+T', and the curl factor is -R'-dT+tau T'. If Z vanishes on all I, K,L solve the constant-coefficient linear system K'=beta K-alpha L, L'=alpha K+beta L. A simultaneous zero forces the solution to be zero everywhere by the ordinary integral Gronwall uniqueness proof. Otherwise a simultaneous zero never occurs. This proves the theorem in the wholly irrotational case.

## 3. Axial pressure independence and rank continuation

Assume now Z is nonzero somewhere. The Poisson source is independent of z, so partial_z P2 is harmonic. On the open vortical set, W.grad S=0 and independence of the kinetic energy give partial_z P2=0. Harmonic continuation on connected G gives partial_z P2=0 everywhere: the Poisson formula has a convergent interior power series, and overlapping balls propagate a zero along any path. Thus

    P2=rho^(-2p)u(theta), S=rho^(-2p)s(theta), u=E/2+s.

The radial-angular determinant of grad k and grad S is a nonzero factor times -dK s'+2p s K'. Hence on {Z!=0},

    D(theta)=K s'-q s K'=0.                           (3)

It extends to all I as follows. On every open irrotational interval, K,L solve the analytic linear system of Section2. The pressure equation in Section4 is a constant-coefficient linear ODE for u with analytic forcing, so u,s,D are analytic there. At an internal endpoint every derivative of D is zero, by smoothness and a sequence from the open set {Z!=0}. The velocity linear ODE and the pressure ODE extend analytically across that endpoint with the actual initial data. Uniqueness identifies these analytic extensions with the original functions on the interval. D therefore has a zero Taylor series inside its analytic extension and is identically zero there. Every proper irrotational interval has such an endpoint; the wholly irrotational case was already treated. Continuity covers the remaining points.

Thus(3) holds even across arbitrarily many accumulating irrotational intervals. On each component C of {K!=0} it integrates to

    s=D_C |K|^q,                                     (4)

with one finite real constant for that component alone.

## 4. Exact pressure polynomial and its positive endpoint form

Put L_p f=A0 f''-4p tau f'+4p²f. The nonzero planar block of DV, after removing rho^(-p-1), is

    M=[[tau R'-pR, R'-T],[tau T'-pT, T'+R]], tr M=0.

Poisson becomes L_p u+tr(M²)=0. With u=E/2+s it is Q+L_p s=0, where

    Q=K K''+(K')²+c1 K K'+c2 L K'
                         +c3 K²+c4 K L+c5 L²,
    c1=-2tau(2p+1)/A0, c2=-(p+1)/A0,
    c3=(2p²tau²+5p²+2p tau²-2p+1)/A0²,
    c4=tau(p-5)(p-1)/A0²,
    c5=(2p(p+1)+4tau²)/A0².                           (5)

To derive this expansion, differentiate E twice using L'=alpha K+beta L and L''=alpha K'+beta L'. The kinetic part is

    L_p(E/2)=K K''+(K')²+alpha L K'+alpha²K²
       +3alpha beta KL+2beta²L²
       -(4p tau/A0)(KK'+alpha KL+beta L²)
       +(2p²/A0)(K²+L²).

Add tr(M²)=2(M11²+M12 M21) and collect coefficients. The independent exact symbolic check reconstructs M and these derivatives from scratch and agrees with every coefficient. At K=0 the form is

    (K')²-((p+1)/A0)LK'+((2p(p+1)+4tau²)/A0²)L².      (6)

Its discriminant is ((p+1)(1-7p)-16tau²)/A0²<0 for p>1. Its leading coefficient is one, so it is strictly positive except at K'=L=0. The sign is uniform over every real tau; no large-rotation approximation is used.

## 5. Every possible component endpoint has zero data

Let C be a component of {K!=0} with an endpoint theta0 inside I. Equation(4) uses one fixed constant on C. Since q>2 and K,K',K'' remain bounded near theta0, s,s',s'' tend to zero there; explicitly the second derivative consists of terms proportional to |K|^(q-2)(K')² and sign(K)|K|^(q-1)K''. Smoothness makes these the actual endpoint values. Also K(theta0)=0.

Taking the endpoint limit of Q+L_p s=0 and using(6) gives

    K(theta0)=L(theta0)=K'(theta0)=0.                 (7)

No uniform bound over other component constants has been used.

## 6. Integrated pressure excludes the endpoint itself

Inside C sufficiently near theta0, set

    F=K²/2+A0s,
    J0=F'+(c1/2)K²+c2LK-4p tau s.

Because q>2, shrink within this one component until F>=K²/4>=0 and |s|<=C F. Equation(5) rewrites exactly as

    J0'=-[(c3-c2alpha)K²+(c4-c2beta)KL+c5L²+4p²s].    (8)

At the endpoint F=J0=L=0. Orient a coordinate t>=0 into the component. Reversing its direction changes fixed signs but none of the following bounds. Variation of constants in the linear L equation and Cauchy-Schwarz give

    |L(t)|²<=C t integral_0^t K(v)²dv
             <=C t integral_0^t F(v)dv.

Integrate(8), use |KL|<=(K²+L²)/2, and recover F' from the definition of J0. For t<=1 this yields

    |F'(t)|<=C(F(t)+integral_0^t F(v)dv).

The nonnegative Y=F+integral_0^t F has Y(0)=0 and Y'<=C1Y. Therefore exp(-C1t)Y is nonincreasing from zero and Y=0. It forces K=0 in a short subinterval of C, a contradiction.

Thus no nonzero K component has an internal endpoint. On connected I either K never vanishes or K is identically zero. The former makes V nowhere zero; in the latter case L'=beta L gives either L nowhere zero or L identically zero. These are exactly the theorem's alternatives.

## 7. What regularity and component hypotheses were used

Smoothness is used to pass every derivative of the rank defect across a boundary of an irrotational interval. The endpoint pressure argument itself needs only the displayed finite derivatives, but this proof does not claim the entire theorem at C1 or C2 regularity. Each component is handled separately, so infinitely many components and arbitrarily large D_C do not produce a gap. The harmonic step concerns partial_z P2 and retains the exact pressure equation; it is not an assumed pressure normalization.

## 8. Nonzero examples and a degenerate ratio

The no-zero conclusion cannot be replaced by local nonexistence. For any nonzero constant Astar and every p>1, set on rho>0

    V=Astar rho^(-p)e_phi,
    P2=-(Astar²/(2p))rho^(-2p).

These smooth fields solve both stationary and full rotating similarity Euler locally for every finite omega. Their nonlinear acceleration is -Astar²rho^(-2p-1)e_rho, canceled by grad P2. Vector homogeneity cancels all remaining linear and rotation terms. Their vorticity is -d Astar rho^(-p-1)e3, and

    k=-omega Astar rho^(-d),
    S=-((p+1)/(2p))Astar²rho^(-2p).

Both scalar gradients are radial, so rank holds; W.grad S=0 as well. This explicitly meets every hypothesis on each allowed coordinate box and has no velocity zero. It is singular at the excluded axis and does not decay along vertical lines, so it is no whole-space counterexample.

When omega=0, k=0 and the ratio |V|²/|S| is exactly 2p/(p+1)=q/(q-1), the upper degenerate endpoint of the CO56 matrix. This shows that endpoint is attained by nonzero local solutions. The example has no common-flat point and does not refute CO56 or settle its remaining flat case.

## 9. Verification and scope

All eight source sections and the complete independent algebra script were read. The single exact symbolic computation passed every stated criterion in0.565 seconds at its recorded real UTC time, on CPU55 with nice19 and OMP1. The theoretical question and pass criterion were written before it ran. It checks rational identities and the explicit discriminant, not the continuation argument; Sections3,5-6 provide that proof separately.

The source, independent script and certificate are retained under verification. No formal build or new model client was used. Section8 is an additional exact check for comparison through the existing configured model agents, whose provider runtime remains unattested. General axial dependence and the unrestricted common-flat problem remain open.
