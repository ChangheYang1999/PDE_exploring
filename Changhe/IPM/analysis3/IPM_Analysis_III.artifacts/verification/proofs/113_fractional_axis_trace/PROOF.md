# Fractional axis regularity in the actual weighted remainder space

## Spaces and result

Let a=17/4, eta=5/4 and k=1615536043799051/9007199254740992. Write

 R=L2_P(|x|^(-2a)W(r)dX), W(r)=max(1,r)^(2a-eta),
 g(t)=exp(-t/2) for t<0, g(t)=exp(27t/4) for t>=0.

Here P means even in x and odd in y. Let chi_s be a fixed degree-zero smooth sector cutoff, equal1 in a neighborhood of both vertical half-axes and supported in a slightly larger such sector. Put

 R_(4,s)={h in R:E^j(chi_s h) in R,1<=j<=4}, E=X.grad,

with its Hilbert graph norm. The scalar space B_6, the positive axis rate d and its integrating factor H are as in proof 110, with the actual coefficients. In particular its norm controls |J| and ||beta-J chi||_(H_g^7), for a fixed smooth endpoint cutoff chi.

For noninteger s define G^s by a uniform smooth partition on the t line:

 ||f||_(G^s)^2=sum_(n in Z) g(n)||psi_n f||_(H^s(R))^2,      (1)

where psi_n(t)=psi(t-n), the supports lie in [n-2,n+2], and sum psi_n^2=1. Any such fixed partition gives an equivalent norm. For integer s this is equivalent to the weighted weak-derivative norm H_g^s used earlier. This definition avoids differentiating the corner of the literal piecewise exponential g.

Let alpha be the axis cofactor of the actual normalized modal background, and chi_0 its fixed radial normalization cutoff. Define the canonical trace and complete axis row by

 T_h(y)=U_2[h](0,y), V_h(t)=T_h(exp(t))/exp(t),
 Gamma_h=(alpha'-alpha)V_h-2alpha V_h'
                         +c[h]chi_0(alpha+alpha'/3).       (2)

Then

 Gamma:E B_6 direct-sum R_(4,s) -> G^(25/4)                (3)

is compact. More precisely it is bounded into G^(51/8), and its tails in that stronger norm tend to zero uniformly on the input unit ball. Both25/4 and51/8 are below the actual coefficient ceiling13/2.

Therefore, in the block continuation theorem, choose Gamma_H=G^(25/4) and B_H={beta in B:A beta in Gamma_H}. Since B_H is continuously included in B_6, condition J2 holds whenever the high remainder domain is continuously included in R_(4,s). Proof 111 supplies that inclusion for the actual factored H^(25/4) remainder and its cone-bulk extension. This result does not prove J1 or any high transport resolvent estimate.

## The local trace gains15/4 derivatives

First consider a density h supported in |x|<=L and with finite norm

 ||h||_a^2=integral |x|^(-2a)|h(x,y)|^2 dx dy.

Use the unitary Fourier transform in y. For a smooth density vanishing near x=0 the multiplier of U_2 is -xi_x^2/(xi_x^2+zeta^2), hence at the axis

 T_hat(zeta)=(|zeta|/2) integral_R exp(-|zeta||x|) h_hat(x,zeta) dx. (4)

The local -h term has zero trace on this core. The formula extends to the weighted space by density, as shown by the following bound, and agrees with the canonical trace because the pointwise trace kernels of proof 46 are continuous on R after localization.

Cauchy-Schwarz gives the exact homogeneous estimate

 |T_hat(zeta)|^2
 <= C_a^2 |zeta|^(1-2a) integral_R |x|^(-2a)|h_hat(x,zeta)|^2 dx,
 C_a^2=Gamma(2a+1)/2^(2a+2).                              (5)

Indeed the integral of exp(-2|zeta||x|)|x|^(2a) is 2 Gamma(2a+1)/(2|zeta|)^(2a+1). Thus

 ||T||_(dot H^(a-1/2))<=C_a||h||_a.                      (6)

For |zeta|<=1 use the support restriction instead, obtaining

 |T_hat(zeta)|^2 <= [L^(2a+1)/(2(2a+1))]
                      integral |x|^(-2a)|h_hat|^2 dx.

Together these bounds give a full H^(a-1/2) estimate with squared constant at most

 2^(a-1/2) max(C_a^2,L^(2a+1)/(2(2a+1))).                (7)

No trace of a generic weighted L2 density is presumed in this argument. The trace is the limit of the velocity on the dense core. Here a-1/2=15/4.

On a compact vertical-axis patch away from the origin, a smooth change from y to t=log y preserves these local Sobolev orders. The dilation identity from proof 109 gives partial_t^j T_h=T_(E^j h) when the corresponding graph derivatives exist. Consequently four graph derivatives of a density supported in a fixed annulus give T locally in H^(31/4). Division by y is smooth there, and (2) uses one additional t derivative, leaving order27/4 before multiplication by the background coefficients.

## The actual coefficient ceiling

On every compact t interval the actual alpha is C6, piecewise analytic, with finitely many knots and bounded one-sided derivatives of every fixed order. Thus alpha' belongs locally to H^s for every s<13/2. To verify the fractional part explicitly, its sixth weak derivative is piecewise Lipschitz with finitely many jumps. If v has this property on a compact interval, then

 integral |v(t+h)-v(t)|^2 dt <= C(|h|+h^2).

The O(|h|) term comes from intervals crossing a jump and the O(h^2) term from the Lipschitz pieces. Integrating against |h|^(-1-2epsilon) gives a finite fractional seminorm for epsilon<1/2. Apply this to the sixth derivative, with epsilon=3/8. The same conclusion holds for alpha and the cutoff coefficients.

The space H^(51/8) on a bounded one-dimensional interval is a multiplication algebra. For a direct proof after cutoff extension, use the Fourier weight inequality <xi>^s<=C_s(<xi-zeta>^s+<zeta>^s), convolution, and ||fhat||_1<=C_s||f||_Hs for s>1/2. Therefore the local H^(27/4) trace-row regularity and the actual coefficients give the local H^(51/8) bound asserted in (3).

## Uniform bounds at both radial ends

The local argument must be combined with the complete normalization. The following gives that endpoint check and makes compactness global.

Fix an output interval I_n=[n-1,n+1], put R_n=exp(n), and select a radial input cutoff equal1 on [R_n/4,4R_n], supported in [R_n/8,8R_n]. Each of its first four dilation derivatives is uniformly bounded. On this input annulus the scaled density h_n(R_n Z) has weighted norm, including the first four dilation derivatives, bounded by

 C R_n^(a-1) W(R_n)^(-1/2)||h||_(R_(4,s)).               (8)

The factor follows by changing variables in the exact R norm. After dividing the trace by y, (8) becomes

 C R_n^(a-2) W(R_n)^(-1/2)||h||_(R_(4,s)).               (9)

This is R_n^(9/4) at the inner end and R_n^(-11/8) at the outer end. Formula (7), the dilation identities and the local product estimate give the same bounds in H^(51/8)(I_n) for the normalized row, with the alpha coefficient factor1 at the inner end and R_n^(k-3) at the outer end. The local strain coefficient scales as the factor in (9). These bounds are uniform because the endpoint coefficient expansions and all their fixed-order derivatives obey alpha=alpha_0+O(R_n^2) at0 and alpha=O(R_n^(k-3)) at infinity.

It remains to control the radially separated input. For smaller input radius, odd-y parity removes the constant kernel term. Every fixed number of output t derivatives of T/y is bounded by

 C R_n^(-4) integral_(r<R_n/4) r|h| dX.                  (10)

The square of its dual norm uses integral r^2/w dX, which is O(R_n^(2a+4)) at0 and O(R_n^(eta+4)) at infinity. Thus (10) has exactly the two powers in (9). The near-origin strain of this small input has the same R_n^(a-2) bound.

For larger input radius use the odd-y Taylor expansion about the origin. The exact linear term is c[h_large]y, and every fixed number of t derivatives of the remainder after division by y is bounded by

 C R_n^2 integral_(r>4R_n) r^(-5)|h|dX.                 (11)

The ratios of output to input radii are uniformly below1, so the differentiated Taylor remainder is uniform at every fixed order. The dual norm of integral r^(-5)|h| is globally finite: its squared radial exponents are2a-9=-1/2 at0 and eta-9<-1 at infinity. At the inner end use the exact identity

 Gamma=(alpha'-alpha)(V-c)-2alpha V'+(4/3)c alpha'.       (12)

Since alpha'=O(R_n^2), equations (11)-(12) give C R_n^2||h|| in every local order needed. At the outer end chi_0=0; the raw large-input bound uses integral_(r>4R_n)r^(-3)|h|, whose dual norm is O(R_n^(eta/2-2))=O(R_n^(-11/8)). Multiplication by alpha gives R_n^(k-35/8).

For input outside the angular sector, the distance from the output axis is at least a fixed positive multiple of max(r,R_n). All output derivatives fall on an absolutely bounded separated kernel. On comparable radii the same change of variables as (8)-(9) gives the same powers, while (10)-(12) apply to the smaller and larger radii. No input dilation derivatives are needed for this complementary sector. The finite transition intervals cause no problem and contribute finite constants.

These estimates establish

 ||Gamma_h||_(H^(51/8)(I_n)) <= C||h||_(R_(4,s)) times
       exp(2n),                         n sufficiently negative,
       exp((k-35/8)n),                  n sufficiently positive. (13)

Smooth local cutoff extensions used in (1) have uniform norms. Multiplying (13) by g(n)^(1/2) yields exp(7n/4) and exp((k-1)n). Their squared sums converge, and their tails tend uniformly to zero.

## The free-jet input

For h=E beta with beta in B_6, proof 110 gives the exact moments

 P=int_(exp(t))^infinity s beta(log s)ds,
 Q=exp(-4t)int_0^(exp(t))s^5 beta(log s)ds,
 S=exp(-6t)int_0^(exp(t))s^7 beta(log s)ds,
 V=P/4-Q/4+S/2, V'=Q-3S,
 V''=-2 exp(2t)beta-4Q+18S.                              (14)

The graph norm controls beta locally in H7. The first-order moment equations give Q,S locally in H8, and (14) gives V' locally in H8 as well. The coefficient argument above again gives Gamma locally in H^(51/8).

The weighted graph norm gives ||beta||_(H7(I_n))<=C exp(-27n/8)||beta||_(B_6) at the outer end, while beta=J+v at the inner end with ||v||_(H7(I_n))<=C exp(n/4)||beta||_(B_6). Integrating the three moments and using their first-order equations, including (14) for the extra derivative, gives

 ||V-c||_(H8(I_n))+||V'||_(H8(I_n))<=C exp(2n)||beta||_(B_6)

at the inner end, and the corresponding raw norms are O(exp(-11n/8)) at the outer end. For the latter, split each integral at0; the fixed inner moments decay as exp(-4t) or exp(-6t), faster than exp(-11t/8). Thus the complete normalized row has the same endpoint bounds (13). In the displayed inner H8 estimate, the constant c is subtracted on the whole local interval; its derivatives vanish. All norm estimates are for fixed smooth extensions slightly beyond I_n.

## Compactness and consequences

The bounds prove (3) into the stronger space G^(51/8). On every fixed compact t interval, the embedding H^(51/8)->H^(25/4) is compact. One direct proof cuts off spatially and then cuts off the Fourier variable: the discarded Fourier tail has operator norm O(M^(-1/8)), and the remaining spatially localized integral operator is Hilbert-Schmidt. Equation (13) makes the tails outside a fixed compact t interval arbitrarily small uniformly on the input unit ball. Combining these two facts proves compactness in (3).

Finally B_H is continuously included in B_6 because G^(25/4) is continuously included in G^6. Proof 111 gives the required continuous remainder embedding for a high domain with the stated base and cone-bulk control. Restricting a compact map to that domain proves J2 for this fractional scalar target. The differentiated lift of J1 and the remainder transport hypotheses remain independent obligations.
