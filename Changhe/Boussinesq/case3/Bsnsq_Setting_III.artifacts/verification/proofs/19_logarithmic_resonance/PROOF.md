# A logarithmic resonance in the whole-plane inverse

Status: CONFIRMED as a manufactured Poisson example and a conditional far-field warning. This is not a B2 profile and supplies no nonexistence endpoint.

## Statement and notation

Write X=(x,y)=(r cos theta,r sin theta), -Delta Psi=Omega, and U=(-Psi_y,Psi_x). For each integer n>=1, the angular mode cos(n theta) obeys

    -Delta[r^p cos(n theta)] = (n^2-p^2) r^(p-2) cos(n theta).

At the resonant exponents the particular inverses are

    Omega=a r^(n-2) cos(n theta):
        Psi= -a/(2n) r^n log r cos(n theta),
    Omega=a r^(-n-2) cos(n theta):
        Psi= +a/(2n) r^(-n) log r cos(n theta).

These identities hold on r>0. Identical formulas hold for the sine mode. Homogeneous harmonic terms may be added locally; the prescribed global inverse and sublinear velocity decide which are permissible.

In particular a nonzero r^(-1) cos theta vorticity coefficient requires an r log r cos theta stream term. Its velocity grows logarithmically, which is sublinear. The following globally smooth example realizes this without a singularity at zero:

    Omega(X)=x/(1+r^2),
    Psi(X)=x H(r^2),
    H(s)=[1-(1+1/s)log(1+s)]/4, H(0)=0.

The resulting U has U(0)=0, is the canonical relative velocity, is sublinear, and has the required x reflection for the div-curl pair. Its ordinary circularly truncated vertical drift is (1/4)log(1+R^2), which diverges.

## Proof of the mode formulas

The polar Laplacian is partial_rr+r^(-1)partial_r+r^(-2)partial_thetatheta. Applying it directly gives the displayed power identity. Differentiate that identity with respect to the real parameter p and then set p=n or p=-n. At either root the term multiplying log r vanishes. The remaining derivative is -2p r^(p-2) cos(n theta). Dividing by this coefficient proves the two resonance formulas. No assertion at r=0 is implicit in this calculation.

## Proof of the smooth whole-plane example

For |s|<1 the power series is

    H(s)=sum_(k>=1) (-1)^k s^k/[4k(k+1)].

Thus H is analytic at zero. Direct differentiation, or the series followed by continuation, gives

    H'(s)= -[s-log(1+s)]/(4s^2),
    4s H''(s)+8H'(s)= -1/(1+s).

Since Delta[x H(r^2)]=x[4r^2H''(r^2)+8H'(r^2)], this proves -Delta Psi=x/(1+r^2) on the whole plane. Differentiation gives

    U1=-2xy H'(r^2), U2=H(r^2)+2x^2H'(r^2).

In particular U(0)=0. At infinity H(r^2)=1/4-(1/2)log r+O(r^(-2)log r); H'(r^2)=O(r^(-2)). Hence U=O(log(2+r)) and

    Psi= -(x/2)log r+x/4+O(r^(-1)log r).

The relative Biot-Savart integral with K(Z)=(Z2,-Z1)/(2pi|Z|^2) converges absolutely because Omega=O(r^(-1)). It has the same div-curl data and vanishes at zero. Its difference from the displayed U is an entire harmonic sublinear vector field, hence constant, and is zero at the origin. This identifies the prescribed relative inverse without selecting a free strain.

For the unsubtracted center drift, the circular integral is

    (1/(2pi)) integral_(r<R) x Omega/r^2 dX
      = (1/(2pi)) integral_0^(2pi) cos^2 theta dtheta
                     integral_0^R r/(1+r^2) dr
      = (1/4)log(1+R^2).

It has no finite ordinary limit. This does not obstruct the well-defined relative inverse or an explicitly declared observer convention.

## Independent computation and scope

code_independent/resonant_inverse_test.py evaluates the exact field and code_independent/cartesian_inverse.py computes the full-plane integral by Cartesian Duffy quadrature and a separately compactified exterior. Six points include the origin, a near-origin point, the axis and non-axis points. At quadrature order48 the maximum velocity errors for core radii8,16,32 are respectively 9.22e-13, 4.44e-16 and 2.88e-16. Omitting the exterior gives errors about .0313, .00559 and .00126. These are floating-point numerical checks, not certified interval bounds. Full outputs and source hash: verification/resonant_inverse.json.

If a formal scalar tail ladder r^(-k/beta) has a nonzero dipole term with k=beta, then beta must be an integer for that term to belong to this integer-indexed ladder, and its stream inverse has the logarithm just derived. One must either allow this resonant term or prove its coefficient vanishes. The calculation does not show that every B2 solution has a nonzero resonant coefficient, nor that all solutions admit such a ladder. It does not by itself determine logarithmic corrections in Theta or Omega. A modal integral inverse can generate the logarithm even when it is absent from a separately assumed stream power ansatz.

Dependencies: polar Laplacian, convergent Taylor series, elementary integration, the subtracted inverse and harmonic uniqueness proved in research/03. No numerical evidence is used in the analytic proof.
