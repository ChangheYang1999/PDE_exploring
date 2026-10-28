# A third axis derivative is unbounded in the weaker angular norms

## Statement

Fix beta_0=17/2, eta=37/20 and 18/5<=a<=4. Let R_a be the parity subspace with the decoupled weight in proof 168. For smooth compactly supported even-in-x, odd-in-y inputs whose support avoids x=0, define

 T_h(y)=U_2[h](0,y),
 U_2=R_1^2,
 K(x,z)=(x^2-z^2)/(2pi(x^2+z^2)^2).

Fix y_0=1/2. There is no finite constant C for which

 |T_h'''(y_0)|<=C||h||R_a                              (1)

holds for all such inputs. In particular the old R->C3 compact-axis estimate, valid at angular exponent 17/4, cannot be extended unchanged to this interval. The assertion is about the third derivative at a positive axis point. It does not contradict the origin estimates for T_h(y)/y-c[h] and T_h'(y)-c[h] proved in proof 168.

## A local scaled input

Let K_3(x,z)=partial_z^3 K(x,z). This is a nonzero smooth function off zero, homogeneous of degree -5 and even in x. Choose a nonnegative even-in-x smooth bump phi supported in

 1<sqrt(u^2+v^2)<2, |u|>1/4,

whose support meets a point where K_3(-u,-v) is nonzero. Set

 psi(u,v)=K_3(-u,-v)phi(u,v),
 C_psi=integral K_3(-u,-v)^2 phi(u,v)du dv>0.

For small epsilon define the globally parity-preserving function

 h_epsilon(x,y)=epsilon^(a-1)
  [psi(x/epsilon,(y-y_0)/epsilon)
                  -psi(x/epsilon,(-y-y_0)/epsilon)].    (2)

Its two supports are disjoint and lie near (0,y_0) and (0,-y_0). They avoid the vertical axis and the origin. On these supports r is bounded above and below independently of epsilon, with r<1. Hence w_a is comparable to |x|^(-2a), with constants independent of epsilon. Changing variables in (2) proves

 0<c_1<=||h_epsilon||R_a<=c_2<infinity.                 (3)

The power is exactly epsilon^(2a-2)epsilon^2epsilon^(-2a)=1. Since psi is supported away from u=0, the remaining fixed weighted integral is finite and positive.

The local point mass in U_2 makes no contribution on the axis because h_epsilon vanishes in a neighborhood of it. The first support in (2) contributes to T_h'''(y_0) exactly

 C_psi epsilon^(a-1)epsilon^2epsilon^(-5)
                    =C_psi epsilon^(a-4).              (4)

For the reflected support the kernel and its derivatives stay bounded, since its distance from (0,y_0) is bounded below. Its contribution is O(epsilon^(a+1)). Thus

 T_(h_epsilon)'''(y_0)
        =C_psi epsilon^(a-4)+O(epsilon^(a+1)).           (5)

For a<4, (3)-(5) directly refute (1), after harmless normalization to unit norm if desired.

## The critical angular exponent

At a=4 choose epsilon_j=epsilon_*4^(-j), j>=1, with epsilon_* small enough that all the support comparisons above hold. The annular supports around each of the two axis points are pairwise disjoint, because each lies between radii epsilon_j and 2epsilon_j. Let h_j be (2) at this scale and set

 H_N=N^(-1/2)sum_(j=1)^N h_j.

Every H_N is still a smooth parity input supported away from x=0. Disjointness and (3) give c_1<=||H_N||R_4<=c_2. Equation (5) gives

 T_(H_N)'''(y_0)=C_psi sqrt(N)
                   +O(N^(-1/2)sum_(j=1)^N epsilon_j^5)
                =C_psi sqrt(N)+O(N^(-1/2)).             (6)

This is unbounded, so (1) also fails at a=4. The construction supplies a sequence in the smooth core itself; no interpretation of a rough trace is needed for the counterexample.

## Why the replacement estimate remains valid

The third derivative in (1) tests a singularity at an arbitrary nonzero axis point. In the origin argument of proof 168, the third kernel derivative is used only for sources with |Z|>2y, where the source and observation segment are separated. Sources at the observation scale are estimated using only T and T', with the fixed inner radial exponent beta_0. The two operations have different hypotheses. Formula (6) therefore invalidates the old proof step without invalidating the new quadratic origin cancellation.

Verdict: REFUTED for the proposed uniform third-axis-derivative inequality on the new spaces. The counterexample and the scope of the replacement are CONFIRMED.
