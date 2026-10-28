# Fourth-moment reflection saving

## Statement and scope

Let0<alpha<1 and [f]_alpha=sup_(x!=y)|f(x)-f(y)|/|x-y|^alpha on R^2. Let mu be a positive finite measure of mass M that contains two disjoint radial area submeasures w(|u|)du on disks of radius R/4, with w>=0. Write R=s h, where h=|x-y|>0 and0<s<2, and put

    I_3=int_0^(R/4) r^3 w(r)dr,
    I_5=int_0^(R/4) r^5 w(r)dr.

Assume the moments are finite. With p=alpha(1-alpha) and q=alpha(1-alpha)(2-alpha)(3-alpha), the difference of convolutions obeys

    |int [f(x-z)-f(y-z)]dmu(z)|
       <= [M-4pi p I_3/h^2-pi q I_5/h^4] h^alpha [f]_alpha.     (1)

As in the parent proof, individual convolutions need not exist; the difference is absolutely integrable for finite mu by the Holder inequality. The statement holds for real and complex scalar inputs.

For the local projection remainder Q_(R,beta), use the disks centered at distance3R/4 on the negative kernel axis and the radial density

    w(r)=[1-(32/9)(r/R)^2]/[2pi R^2(3/4+r/R)^2].

Define

    J=653/288-(63/8)log(4/3),
    K=(1/2)int_0^(1/4) t^5[1-(32/9)t^2]/(3/4+t)^2 dt > 0.

Then the positive local term of mass1/2 may be bounded by

    [1/2-p J s^2-q K s^4]h^alpha[f]_alpha.                    (2)

Thus its saving improves the parent quadratic saving by the strictly positive term q K s^4. No numerical endpoint is asserted here. The disk containment, projection decomposition and density domination are dependencies; applications remain OPEN pending an independent cross-read of this proof and those dependencies.

In the retained-edge cutoff plan, at normalized increment h=1 and0<rho<=1/3, the dominated density is w-H with H=1/[2pi(1-rho)^2]. Its proposed saving is

    p[J rho^2-rho^4/(512(1-rho)^2)]
      +q[K rho^4-rho^6/(49152(1-rho)^2)].                     (3)

Both terms are strictly positive because w-H>0 throughout the disk, as established by the cutoff density proof. Accordingly J_D(alpha,rho) from ../../cutoff_plan/PROOF.md would be decreased by (3). At larger radii the same conclusion holds using (w-H)_+ and its exact second and fourth moments instead. No existing accepted numerical bound is changed by this note.

## Symmetric scalar inequality

For|v|<1 let A(v)=((1-v)^alpha+(1+v)^alpha)/2. Its fourth derivative is

    A''''(v)=-q[(1-v)^(alpha-4)+(1+v)^(alpha-4)]/2 <= -q,

because t^(alpha-4) is convex and the two arguments have mean1. At zero, A=1, A'=A'''=0 and A''=-p. Integrating the fourth-derivative inequality four times from0 to v>=0 gives

    A(v)<=1-p v^2/2-q v^4/24.

Evenness extends this to negative v, and continuity covers|v|=1. This proves an upper bound, which is the needed direction when estimating the coupling cost.

## Marginals and moments

Use the reflection coupling of ../PROOF.md. In each radial disk centered at c, pair z=c+u with z'=c+u-2(u dot e)e, where e=(x-y)/h. Radial symmetry proves exact equality of the target marginal with the source submeasure. The evaluation displacement is(h-2u dot e)e; its signed factor remains positive since2|u dot e|/h<=s/2<1.

Average the cost at u and its reflection and apply the scalar estimate with v=2u dot e/h. For one disk,

    int (u dot e)^2 w du=pi I_3,
    int (u dot e)^4 w du=(3pi/4)I_5.

There are two disks. The quadratic coefficient is therefore2*(p/2)*4*pi=4pi p. The fourth coefficient is2*(q/24)*16*(3pi/4)=pi q. Translate the remaining positive measure at cost h^alpha per unit mass. This gives (1), including the full mass M, without changing any atom or other transport edge.

For the stated density,4pi I_3=J R^2 and pi I_5=K R^4, proving (2). Subtracting H from w reduces4pi I_3 by rho^4/[512(1-rho)^2] and pi I_5 by rho^6/[49152(1-rho)^2], because int_0^(rho/4)r^3dr=rho^4/1024 and int_0^(rho/4)r^5dr=rho^6/24576. This proves (3).

## Explicit evaluation without a numerical integral

For an integer n>=2 and c=3/4, let

    B_n=(-c)^n(1/c-1)
        +n(-c)^(n-1)log(1/c)
        +sum_(j=2)^n binom(n,j)(-c)^(n-j)(1-c^(j-1))/(j-1).

Expanding t^n=(u-c)^n with u=c+t proves B_n=int_0^(1/4)t^n/(c+t)^2dt. Hence

    K=(B_5-(32/9)B_7)/2.

This is an exact rational linear combination of1 and log(4/3), suitable for directed interval evaluation. Its positivity follows directly from its displayed integral; cancellation in a decimal computation must not be used as a positivity proof.
