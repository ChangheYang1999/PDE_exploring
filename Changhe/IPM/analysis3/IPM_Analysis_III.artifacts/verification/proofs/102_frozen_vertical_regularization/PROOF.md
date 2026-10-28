# Regularization of the frozen vertical remainder

## Statement

Let D,Sigma>0, a,lambda real, and b>=3/2. On R_t x R_z set

 P=D partial_t-Sigma z partial_z+a,
 H_(lambda,b)=L2(exp(lambda t)|z|^(-2b)dt dz).

Assume

 kappa=D lambda/2+Sigma(b-1/2)-a>0,
 kappa_2=3 Sigma/2-a>0.                                 (1)

Give P its maximal distributional domain in this space. Let s>=2, and suppose u belongs to H_(lambda,b) and Pu=F, where F belongs to H_(lambda,b) intersect H^s(R^2). Then for every finite Z>0,

 u belongs to H^s(R_t x (-Z,Z)).                         (2)

Here H^s on a strip means the restriction of the ordinary isotropic Bessel-potential space, with its usual restriction norm. No prior high regularity of u is assumed. There is a finite constant C depending only on s,Z,D,Sigma,a such that

 ||u||_H^s(strip Z)<=C ||F||_H^s(R^2).                  (3)

The constant in (3) is not numerically evaluated. The normal-derivative estimate used in its proof is explicit:

 ||partial_z^2 u||_(L2_t H_z^(s-2))
       <=||partial_z^2 F||_(L2_t H_z^(s-2))/kappa_2.     (4)

The space on the left is unweighted. The hypotheses b>=3/2 and the low-domain selection are essential: they remove the two affine integration constants at z=0.

## The selected inverse

The transport group is

 S_tau F(t,z)=exp(a tau)F(t+D tau,exp(-Sigma tau)z).

A direct change of variables gives ||S_tau||_H=exp(-kappa tau). Thus P is bijective on its low space and

 u=-integral_0^infinity S_tau F d tau.                   (5)

The generator equals the maximal domain. To see this, conjugate by exp(lambda t/2)|z|^(-b), and then set |z|=exp(v), including the Jacobian factor exp(v/2). On each side of z=0 the result is the constant translation generator D partial_t-Sigma partial_v-kappa. Fourier transformation identifies its generator and maximal domains. Cutoffs in log|z| show that the two halves glue distributionally, with no trace condition introduced at z=0. The semigroup argument and uniqueness are otherwise exactly the direct proof in proof 101.

## Two normal derivatives and their fractional regularity

Differentiate the finite integrals in (5) twice. The identity

 partial_z^2 S_tau F
 =exp((a-2 Sigma)tau)(partial_z^2 F)(t+D tau,exp(-Sigma tau)z)

holds in distributions. For any q>=0, Fourier transformation in z gives

 ||partial_z^2 S_tau F||_(L2_t H_z^q)
 <=exp(-(3 Sigma/2-a)tau)||partial_z^2 F||_(L2_t H_z^q).

The Fourier weight decreases because the z-frequency is multiplied by exp(-Sigma tau). This proves convergence of the differentiated integrals in L2_t H_z^(s-2) and (4). The undifferentiated finite integrals converge in H to u and hence in distributions on compact sets. Local differentiation commutes with that limit, identifying the normal derivative with the preceding limit. No fractional derivative of a growing distribution is needed.

For almost every t, u and u_zz are locally square integrable in z. Therefore u(t,.) has a W^{2,2} representative on bounded intervals. One elementary proof integrates u_zz twice and observes that the remaining distribution has second derivative zero, hence is affine. Local square integrability makes its two coefficients ordinary measurable functions of t. In one dimension W^{2,2} has continuous value and first derivative at0. The integrability of |u|^2 |z|^(-2b), with b>=3/2, forces both traces to be zero. Indeed a nonzero value contributes |z|^(-2b), and a nonzero linear term contributes |z|^(2-2b), neither integrable at the stated endpoint. Consequently

 u(t,z)=integral_0^z (z-v)u_zz(t,v)dv.                   (6)

On (-Z,Z) this twice-integration map is bounded from H_z^(s-2) to H_z^s, for every s>=2. For integer s this follows by differentiation and Cauchy-Schwarz in (6); for noninteger s=m+alpha, 0<alpha<1, the same argument controls derivatives below order m, while the fractional difference quotient of the mth derivative is exactly that of the (m-2)nd derivative of u_zz. The corresponding interval norm is equivalent to the restriction Bessel norm. Hence (4) gives

 ||u||_(L2_t H_z^s(-Z,Z))<=C_(s,Z)||F||_H^s/kappa_2.     (7)

This argument works on arbitrary bounded strips and supplies the unweighted local L2 norm, not merely normal derivatives modulo polynomials.

## Tangential regularity

We give the elementary local regularity argument needed to pass from (7) to the isotropic space (2). It is useful to state it separately.

Let v be supported in a bounded z interval, and let B(z) be smooth and bounded with bounded derivatives, equal to -Sigma z near that support. Put P_B=D partial_t+B(z)partial_z+a. For r>=1, smooth v satisfies

 ||v||_H^r <= C_r (||P_B v||_H^(r-1)
                 +||v||_(L2_t H_z^r)+||v||_H^(r-1)).   (8)

To prove this, Fourier weights first give

 ||v||_H^r <=C (||partial_t v||_H^(r-1)
                          +||v||_(L2_t H_z^r)).

Use D!=0 and the equation to replace partial_t v. Multiplication by B is bounded on H^(r-1). For every epsilon>0 the pointwise frequency split |zeta|<=epsilon(1+xi^2+zeta^2)^(1/2), or its complement, gives

 ||partial_z v||_H^(r-1)
 <=epsilon ||v||_H^r+C_(r,epsilon)||v||_(L2_t H_z^r).

Choose epsilon to absorb its first term. The remaining zeroth-order term is included in (8). Multiplication by a fixed smooth bounded B is bounded on these Sobolev spaces, as follows directly from its Fourier convolution after a compact extension in z and the inequality <p>^(r-1)<=C<p-q>^(r-1)<q>^(r-1).

Estimate (8) also proves regularity when its right side is finite but v is only known to belong to H^(r-1). Here are the regularization details. Apply the Fourier multiplier J_epsilon=(1+epsilon^2|p|^2)^(-N), with integer N>r+2. It commutes with partial_t and partial_z, is contractive in every Sobolev norm, and its commutator with B partial_z is uniformly bounded on H^(r-1). For completeness its Fourier kernel has the factor

 Bhat(p-q) i q_z [j_epsilon(q)-j_epsilon(p)].

Writing k=p-q, the mean value formula on |k|<=|q|/2 and the trivial bound on its complement show

 |q_z| |j_epsilon(q)-j_epsilon(p)|<=C_N |k|

uniformly in epsilon: in the first case |q| is comparable to every intermediate frequency and |p| |grad j_epsilon(p)|<=2N; in the second |q|<=2|k|. Peetre's inequality and Young's convolution inequality then bound the commutator by C_N integral |k|<k>^(|r-1|)|Bhat(k)|dk. Since B depends only on z, this is a one-dimensional integral; a smooth compact extension has all the required moments. A constant part commutes and may be separated. Thus P_B J_epsilon v has a uniform H^(r-1) bound from P_Bv and v. Apply (8) to J_epsilon v. Its pure normal norm is no larger than that of v. Fatou's lemma in Fourier variables as epsilon tends to zero proves v in H^r and (8). This step does not start by assuming the desired regularity.

Finally apply (8) to v=chi(z)u, using nested cutoffs equal to1 on successively smaller strips. Its equation is

 P_B v=chi F-Sigma z chi' u.

From (7), u is initially in unweighted L2 on every bounded strip. Induction with r=1,2,...,floor(s) gives local H^r, since F is in H^s and the cutoff commutator has the previous order. If s is noninteger, one last application with r=s uses the already known order floor(s)>=s-1. The pure normal norm needed at every step is supplied by (7). This proves (2)-(3). The finite number of nested cutoffs and their derivative bounds depend only on s and the chosen strip radii.

## Relation to the frozen IPM remainder

In the chart y>0, t=log y, z=x/y, write

 h(x,y)=x^2 y y^delta u(t,z).

Since L00(x^2 y)=0, conjugation of L00 gives precisely

 P=D partial_t-Sigma z partial_z+D delta.

For the near-origin remainder space with a_weight=17/4, its norm becomes H_(lambda,b) with

 b=a_weight-2=9/4,
 lambda=2(3+delta+1-a_weight)=2delta-1/2,
 a=D delta.

Then kappa=7 Sigma/4-D/4=1+(D-A)/2+(17/4)A>0. At delta=9/5, kappa_2=3 Sigma/2-9D/5>0, so the theorem applies to every finite s>=2, in particular s=25/4, when its localized cofactor forcing is H^s. Exact rates and checks are in the evidence. This is the low remainder component, whose cofactor has zero value and first normal derivative at the vertical axis. It is not a theorem about a freely varying jet coordinate.

To localize an actual frozen remainder solution, its cutoff cofactor right side must include the complete commutator P(chi u)-chi Pu. As in proof 101, (3) does not create high regularity of a transition term from a low bound. The full variable IPM coupling, the jet equation and propagation through the transition regions remain separate open steps.
