# Strict cutoff saving at every admissible radius

## Statement

Use0<alpha<1,0<rho<1/2 and the real or complex homogeneous Euclidean Holder seminorm. Let D_alpha be the norm of R_1^2=T_xx-I/2, with the quotient extension and circular principal values of the setup. The explicit old upper bound J_D(alpha,rho) and the surviving-edge argument are stated in ../PROOF.md. Define

    q=rho/(1-rho),
    tau=min{1/4, [sqrt(32/9-q^2)-(3/4)q^2]/(32/9+q^2)},
    F(u)=-(8/9)u^4+(40/9)u^3-(19/2)u^2+(51/4)u
          -(63/16)log(u)-27/(64u),
    E(alpha,rho)=alpha(1-alpha)(1+rho/2)^(alpha-2) rho^2
                 [2(F(3/4+tau)-F(3/4))-(q^2/2)tau^4].

Then the proposed bound is

    D_alpha <= J_D(alpha,rho)-E(alpha,rho),  E(alpha,rho)>0.

It is uniform in the kernel phase. This is an analytic extension of the parent candidate, pending independent cross-read. It asserts no numerical endpoint. Whenrho<=1/3, tau=1/4 and E is exactly the parent eta_cut, so all existing proposed scalar evaluations are unchanged.

## Positive radial submeasure

Inside each of the two selected radiusrho/4 disks, the already derived radial density is

    w(r)=[1-(32/9)t^2]/[2pi rho^2(3/4+t)^2], t=r/rho.

The retained translation-edge density after the finite perturbation is at least w-H whenever this is positive, where H=1/[2pi(1-rho)^2]. Thus one may remove the radial positive part (w-H)_+ from each disk and replace its translation coupling by reflection. The source and target marginals are exact translates of the same radial submeasure. The old remaining flows and every local identity term are unchanged.

The sign of w-H equals the sign of

    p(t)=1-(32/9)t^2-q^2(3/4+t)^2.

Because0<q<1, p(0)=1-9q^2/16>7/16>0. Its derivative is strictly negative fort>=0. The positive root is

    t_*=[sqrt(32/9-q^2)-(3/4)q^2]/(32/9+q^2).

This follows from the quadratic formula; the discriminant before dividing by4 is128/9-4q^2. The numerator of t_* is positive because p(0)>0. Hence tau=min(1/4,t_*) is positive, and w-H is positive on0<=t<tau, zero or positive at tau, and nonpositive beyond tau if that region exists. The extracted density is therefore precisely w-H on the smaller concentric disk of radiusrho*tau and zero outside it.

## Exact cost saving

The reflection coupling has normalized displacement1-2u_parallel. Throughout the selected disks it lies in[1-rho/2,1+rho/2], a positive interval. The same concavity estimate as in the parent proof bounds its total saving by at least

    alpha(1-alpha)(1+rho/2)^(alpha-2)
      *4pi integral_0^(rho*tau) r^3(w(r)-H)dr
    =alpha(1-alpha)(1+rho/2)^(alpha-2) rho^2
      *2 integral_0^tau t^3
          {[1-(32/9)t^2]/(3/4+t)^2-q^2}dt.

The integrand in braces is positive on[0,tau), so the saving is strictly positive. The antiderivative in the radial-density proof evaluates the first integral by F(3/4+tau)-F(3/4). The constant-density correction contributes(q^2/2)tau^4. This yields E(alpha,rho). Finite submeasures and compact disks justify the coupling integrals directly; all principal-value normalization and far-field convergence remain in the unchanged J_D proof.

Finally, forrho<=1/3 one has q<=1/2. At t=1/4,

    p(1/4)=7/9-q^2>=19/36>0.

Thus t_*>1/4 and tau=1/4. The radial-density identity2(F(1)-F(3/4))=J gives

    E(alpha,rho)=alpha(1-alpha)(1+rho/2)^(alpha-2)
                  [J rho^2-rho^4/(512(1-rho)^2)],

which is exactly the parent formula. The same equality actually holds whenever q^2<=7/9. The positive-part construction extends the strict inequality to every remaining0<rho<1/2 without changing any previously proposed table value.
