# The two escaping witness types have different tail vorticity

Status: A971 REFUTED as a merged source attribution; A972 CONFIRMED as the corrected conditional statement. No actual nonzero decaying profile is constructed or asserted to exist.

## 1. Exact setting

Let 2/5<c<1/2, omega be any finite real number, Jx=(-x2,x1,0), A=cI-omega J, a=1-2c, kappa=1+c and p=(1-c)/c. Suppose U in C2(R3;R3), P in C1(R3) satisfy

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1).

Put B=Ax+U, Omega=curl U, and let Phi be the complete carrier flow. Let Xi be the actual scattering diffeomorphism from the escaping set to D=R3 minus{0}, and let V and W=curl V be the actual velocity and vorticity tails. The previously verified identities are Xi(Phi_t x)=exp(tA)Xi(x), D Xi Omega=W composed with Xi, and the uniform compact-annulus limits

    exp((1-c)t)exp(omega tJ)U(exp(tA)z)->V(z),
    exp(t)exp(omega tJ)Omega(exp(tA)z)->W(z).

Define H=P+|U|^2/2+(Ax).U. Its pressure-dependent constant limit at infinity is Hinf. Fix an escaping carrier orbit y(t)=Phi_t y0 with U nonzero and exact covector law

    U(Phi_t y0)=exp(rho t)D Phi_t(y0)^(-T)U(y0),
    rho<=-2a, U.B=0, H=H0.

There are two distinct sources of such an orbit:

(W1v) y0=gamma(tau0), tau0!=0, on the vortex line gamma'=Omega through a vortical carrier equilibrium gamma(0)=q. The exact relation is B(gamma(tau))=kappa tau Omega(gamma(tau)).

(W2) y0 belongs to an escaping lower-window vortical-closure trace of a flat periodic carrier witness. This entire trace is irrotational: Omega(y(t))=0 for every t.

These are additional configurations, not existence assertions.

## 2. Conclusions common to both configurations

Bounded velocity and the radial carrier estimate cr-sup|U|<=r'<=cr+sup|U| give |y(t)| comparable to exp(ct). The nonzero scattering vector v=Xi(y0) satisfies exp(-tA)y(t)->v. The covector law gives

    d_t log|U(y(t))|=rho-c-n.(sym DU)n, n=U/|U|.

The gradient assumption makes the last term absolutely integrable, since |DU(y(t))|<=C exp(-t). Thus

    exp(-(rho-c)t)|U(y(t))|->C0>0.

Momentum and the covector law imply

    grad P=DU^T U-(a+rho)U.

The canonical-pressure estimate A674 is |grad P|<=C r^(-2p-1). Since a+rho!=0 and DU tends to zero, comparison of rates gives

    rho-c<=-c(2p+1), hence rho<=-2(1-c).

In particular rho<-a. The uniform actual tail limit then gives V(v)=0, hence V=0 on the entire scattering ray exp(tA)v. Constancy of H and its uniform limit give H0=Hinf. None of these rate statements is inferred from bare velocity decay alone.

## 3. Nonzero vorticity on the W1v ray

Along the W1v orbit, tau(t)=tau0 exp(kappa t), so

    exp(t)exp(omega tJ)Omega(y(t))
      =[A exp(-tA)y(t)+exp(-ct)exp(omega tJ)U(y(t))]/(kappa tau0).

Taking the uniform actual tail limit yields

    W(v)=Av/(kappa tau0)!=0.

Nonvanishing follows because A is invertible when c>0 and v!=0. For the unit twisted direction w=exp(-sA)v, s=log|v|/c, put G(w)=W(w), G_r(w)=w.G(w), and

    Y(w)=G(w)-(G_r(w)/c)Aw.

Twisted homogeneity gives

    G(w)=|v|^(1+1/c)Aw/(kappa tau0),
    G_r(w)=c|v|^(1+1/c)/(kappa tau0)!=0, Y(w)=0.

Thus this is a common zero of V and the projected field Y, with nonzero full tail vorticity. No regularity or uniqueness of the Y flow is used.

## 4. Zero vorticity on the W2 ray

The W2 trace instead has Omega(y0)=0. The actual identity D Xi(y0)Omega(y0)=W(Xi(y0)) gives W(v)=0. Homogeneity extends this to its entire scattering ray. Combined with Section2 this is a common zero of V and W. The trace's irrotationality is precisely the hypothesis unavailable for W1v.

## 5. Report correction and scope

The report draft Remark6.1 joins the two cases in the assertion that an escaping trace or half-line lies over a common zero of V and curl V, citing A829-A830 and A870-A871. Those audits treat W2 and explicitly distinguish W1v; A602 proves the nonzero W1v tail-vorticity formula. Therefore the merged source attribution and its inference are refuted. This does not furnish an actual profile counterexample to the conjecture; both witness configurations remain conditional.

A correct replacement is:

> Under the natural bounds, an escaping trace or half-line has rho<=-2(1-c), Bernoulli value Hinf, and zero tail velocity on its scattering ray. For a W1v vortex half-line the projected tail vorticity vanishes but its radial component is nonzero (A602). For a W2 trace both tail velocity and full tail vorticity vanish (A830,A871).

The same replacement is needed in the report's source fragment in the team records. The smooth all-order W2 manifold statement following the faulty sentence is already present and is not an error. No additional theorem excluding either remaining connection is proved here.

Dependencies: A602 and its complete proof; A674 canonical pressure; A829-A830 and A870-A871 with their complete escape sections. The configured model Theory Agent B agent independently flagged precisely this distinction in its 11:56Z note, which was read and compared; provider runtime is not independently attested. No new model client, computation, numerical experiment or formal build was used.
