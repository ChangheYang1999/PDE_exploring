# Conditional escaping flat traces: source B50

## 1. Exact setting

Let U in C2(R3;R3), P in C1(R3) solve the rotating Euler profile equation, with global zero helicity, uniform velocity decay, 2/5<c<1/2 and arbitrary finite omega. Put A=cI-omega J, B=Ax+U, a=1-2c, p=(1-c)/c and Omega=curl U. Consider one escaping orbit y(t)=Phi_t y0 of the unstable vortical-closure trace of a lower flat periodic witness. The previously confirmed A820-A830 conclusions supply, along this orbit,

    Omega=0, U!=0, U.B=0, H=H0,
    U(Phi_t y0)=exp(rho t) D Phi_t(y0)^(-T) U(y0), rho<=-2a.

Here H=P+|U|^2/2+(Ax).U, with an arbitrary but fixed pressure constant. Add the global natural bounds

    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1).

The source's alternative DU=O(sqrt(r)) supplies these by the confirmed earlier bootstrap, in the target c interval. The pressure-gradient input A674 is used in this interval. No conclusion for all 1/3<c<=2/5 is inferred merely from the broader range of the derivative bootstrap.

## 2. Exact asymptotic and pressure comparison

The actual scattering map gives a nonzero xi with exp(-tA)y(t) tending to xi. Therefore exp(-ct)|y(t)| tends to |xi|>0. Differentiating the covector law gives

    d_t log|U(y(t))|=rho-c-n.(sym DU)n, n=U/|U|.

The natural derivative bound and the radial growth give |DU(y(t))|<=C exp(-(p+1)ct)=C exp(-t) for sufficiently large t. The strain integral converges absolutely. Consequently

    exp(-(rho-c)t)|U(y(t))| -> C0>0.

This is stronger than the logarithmic asymptotic claimed by B50, and follows from its same natural-rate premises. Since rho<-a, the velocity decays faster than exp(-(1-c)t). The leading tail V thus vanishes on the complete scattering ray exp(tA)xi.

Comparing the differentiated covector law with momentum gives, on the orbit,

    grad P=DU^T U-(a+rho)U.

Since a+rho is nonzero, its magnitude is at least |a+rho||U|/2 for sufficiently large t. The verified pressure lemma A674 gives |grad P|<=C r^(-2p-1). Comparing exponential rates yields

    rho-c <= -c(2p+1),
    rho <= -2cp = -2(1-c).

The source's intermediate line rho<=c(-2p-1) is missing +c. Its final bound rho<=-2(1-c) is correct. The actual uniform Bernoulli limit under the natural bounds and constancy of H along this escaping orbit give H0=Hinf.

There is an additional already confirmed A830 consequence: Xi_*Omega=W and Omega=0 on this entire orbit imply W=0 on its scattering ray. Thus both actual tail V and W vanish there. This differs from the vortical equilibrium-line escape case, whose radial tail vorticity can be nonzero.

## 3. Verification and scope

B50 is confirmed under the target-range natural bounds or the stated derivative premise supplying them. Its relevant proof was already independently established in the team records, Section 8; the full new source and that section were compared. The stronger positive amplitude limit above uses the absolute integrability of strain, not just DU tending to zero. Without a derivative premise only the exact strain-integral formula remains established here. No global lower flat-witness exclusion follows, and no bare-decay rate is promoted. No computation or formalization was needed.
