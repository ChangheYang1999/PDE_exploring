# Helicity and angular momentum at infinity

## Setting and previously established input

Let U,P solve the rotating Euler profile equation on R3, div U=0, with U bounded and U(R.) tending to zero in distributions as R tends to infinity (Hb). Put B=(cI-omega J)y+U, Omega=curl U, q=|U|^2/2 and alpha=5-2/c. The canonical pressure and energy theorems give, for 2/5<=c<1,

    E(R)=int_{|y|<R}|U|^2<=G R^alpha, R>=1,

with alpha=0 at c=2/5. For each dyadic annulus A_R={R<|y|<2R}, a pressure constant p_R can be chosen so

    ||P-p_R||_{L2(A_R)}<=C R^{alpha/2}, R>=1.

The sharper pressure estimate is already proved, but this weaker bound suffices here. No pointwise pressure decay is assumed.

## Total helicity under an annular vorticity hypothesis

Assume U is C2, 2/5<c<1/2, and

    ||Omega||_{L2(A_R)}<=C R^{3/2-1/c}, R>=1.             (H)

Then h=U.Omega is integrable and int h=0 for every omega. In particular this proves Theory Agent A C10, whose pointwise derivative bound implies (H).

Indeed Cauchy-Schwarz gives

    int_{A_R}|h|<=C R^{alpha/2+3/2-1/c}=C R^{4-2/c}.

The exponent is negative, so a dyadic sum proves integrability at infinity; smoothness handles the origin. The exact helicity identity integrated on a ball is

    c r H'(r)+(2-4c)H(r)+int_{S_r}[h U.n+(P-p_R-q)Omega.n]=0,

where H(r)=int_{B_r}h and any constant p_R is allowed because Omega has zero flux. Use the same p_R throughout r in [R,2R] and average by dividing by R. The first term is bounded by 2c int_{A_R}|h|, which tends to zero. If M=||U||_infinity, then

    R^{-1}int_{A_R}|h U|<=M R^{-1}int_{A_R}|h|,
    R^{-1}int_{A_R}|q Omega|<=M R^{-1}||U||_{L2(A_R)}||Omega||_{L2(A_R)},
    R^{-1}int_{A_R}|(P-p_R)Omega|
       <=R^{-1}||P-p_R||_{L2(A_R)}||Omega||_{L2(A_R)}.

All three are O(R^{3-2/c}), hence vanish. Finally the average of H(r) tends to int h by absolute integrability. Since 2-4c is nonzero, int h=0.

This proof uses the vorticity bound explicitly; no such bound has been deduced from Hb alone. Vanishing of signed helicity is not vanishing of vorticity.

## Pressure-free angular moments

For any real skew matrix K let m_K(y)=(Ky).U(y). Direct differentiation of momentum gives

    B.grad m_K=(2c-1)m_K+omega m_[J,K]-(Ky).grad P.

As div(Ky)=0, this is equivalent to

    (1-5c)m_K+div(m_K B+P Ky)=omega m_[J,K].

Every Ky is tangent to centered spheres. Put Gamma(R)=int_{B_R}(Jy).U. The pressure boundary term therefore vanishes identically and

    c R Gamma'(R)+(1-5c)Gamma(R)=-int_{S_R}(Jy).U (U.n).

Set gamma=5-1/c>0. The derivative of R^{-gamma}Gamma is bounded in magnitude by c^{-1}R^{-gamma}E'(R). Since alpha-gamma=-1/c<0, integration by parts and E(R)<=G R^alpha give

    int_R^infinity r^{-gamma}E'(r)dr<=C R^{-1/c}.

Hence Gamma_infinity exists and

    R^{-gamma}Gamma(R)=Gamma_infinity+O(R^{-1/c}).

Let K_i v=e_i cross v, i=1,2, and Z(R)=int_{B_R}(m_{K_1}+i m_{K_2}). The commutators [J,K_1]=K_2 and [J,K_2]=-K_1 give

    cR Z'(R)+(1-5c+i omega)Z(R)=-int_{S_R}(m_{K_1}+i m_{K_2})(U.n).

The integrating factor is R^{-gamma+i omega/c}. Its modulus is R^{-gamma}; the same estimate proves

    R^{-gamma+i omega/c}Z(R)=Z_infinity+O(R^{-1/c}).

The hypotheses for these two moment limits are only U,P C1, Hb and 2/5<=c<1. The constants in the bounds do not acquire a factor |omega| from the integrating factor.

## Identification with the weak terminal profile

For 2/5<c<1 put Q_s=e^{omega sJ}, R=e^{cs}, V_s(x)=e^{(1-c)s}Q_s U(RQ_s^{-1}x). The weak L2_loc limit V exists by A068. The change of variables y=RQ_s^{-1}x gives

    int_{B_1}(Jx).V_s(x)dx=R^{-gamma}Gamma(R).

For the complex horizontal moment, Q_s^{-1}(e1+i e2)=e^{i omega s}(e1+i e2), giving

    int_{B_1}((K_1+iK_2)x).V_s(x)dx
       =R^{-gamma+i omega/c}Z(R).

Both test fields belong to L2 on B1, so weak convergence identifies Gamma_infinity and Z_infinity with the corresponding moments of V. No strong limit or sign condition is needed. This confirms Theory Agent A C11.

## Pressure-normalization clarification

A bounded example witnessing harmonic ambiguity without Hb is the constant velocity U=b, with P=-[(1-c)b+omega Jb].y. Its canonical pressure is constant but its actual pressure can have a nonzero linear part. Nonconstant affine examples also have harmonic ambiguity, but are outside the bounded class. This distinction does not affect any result above, which uses Hb.
