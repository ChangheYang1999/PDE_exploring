# Negative pressure with controlled convective acceleration

## 1. Exact theorem

Let v be C1 and P continuous on a full ball B_R in R3 centered at0. Suppose div v=0 and div div(v tensor v+P I)=0 in distributions. Put E=|v|^2, a=(v.grad)v and F=P(0)-P. Assume F>=kappa E throughout some full neighborhood of0, where kappa>0 is fixed. This forces v(0)=0 and F>=0.

If |a(x)|<=K E(x)/|x| for0<|x|<r0 and |v(x)|<=C|x|^m there, with K finite, m>0 and 2m>K/kappa, then v=0 and P=P(0) on a smaller neighborhood. Infinite value vanishing order of v suffices for every finite K. Alternatively, if |a(x)|<=q(|x|)E(x) with q nonnegative and integrable on(0,r0), no separate order hypothesis is needed. In particular a bounded acceleration-to-energy coefficient suffices.

These are conditional local theorems. All pressure and acceleration bounds apply on a full neighborhood, not just one vortical component. There is no helicity, symmetry, homogeneity or rotation restriction. No numerical or formal verification is claimed.

## 2. The pressure mean at continuous regularity

Incompressibility gives div(v tensor v)=a. Thus Delta F=div a in distributions. Write normalized spherical averages

    M(r)=average F(rn), A(r)=average a(rn).n,
    K0(r)=average E(rn), n in S2.

Both a and F are continuous at0. Testing the distributional identity against a radial smooth function psi supported away from0 yields

    integral [r^2 M psi''+2r M psi'+r^2 A psi'] dr=0.

In one-dimensional distributions this becomes integral(-r^2 M'+r^2 A)psi'=0. The distribution in parentheses is therefore a constant C. Hence M'=A-C/r^2. A is continuous and bounded near0, and a primitive of the extra term is C/r. Continuity of M at0 excludes C!=0. Consequently

    M'(r)=A(r), M(r)=integral_0^r A(t)dt,
    M(0)=0, M(r)>=kappa K0(r)>=0.

In particular the mean is C1 away from0 despite the lack of a classical pressure derivative. No differentiation of P or unjustified integration over its gradient occurs. Subtracting P(0) fixes the pressure gauge exactly.

## 3. Finite order and infinite flatness

Under the inverse-radius bound and |v|<=C r^m, the mean identity implies

    |M'|<=K K0/r<=K C^2 r^(2m-1).

The right side is integrable at0 because m>0. With M(0)=0, this proves M=O(r^(2m)). Independently the pressure sign gives

    M'<=d M/r, d=K/kappa.

Thus r^-d M is nonnegative and nonincreasing in r. If 2m>d, its limit at0 is zero, forcing it to vanish identically. This reasoning never divides by a possibly zero M. Since E and F are nonnegative continuous functions, their zero averages on every small sphere give E=F=0 pointwise. This proves the stated local conclusion.

For infinite value flatness, choose any m>K/(2kappa). No derivative flatness of v or separate flatness of P is needed. The constant K and kappa stay fixed while m is chosen. For K=0 the same proof gives M'=0 directly.

## 4. Integrable coefficients and a quantitative lower bound

If |a|<=q(r)E with q integrable at0, then M'<=q(r)M/kappa almost everywhere. The product

    exp(-integral_0^r q(t)/kappa dt) M(r)

is nonnegative and nonincreasing, and tends to zero at0 by continuity. It must vanish. This gives the integrable and bounded-coefficient versions without an order assumption.

More generally let q be locally integrable away from0, and suppose M(r1)>0. Integrating the same inequality from r to r1 gives

    M(r)>=M(r1) exp(-integral_r^r1 q(t)/kappa dt), 0<r<r1.

This is a necessary lower bound for a nonzero pressure mean; it does not derive an upper bound on q from the equations. In particular a supported infinitely value-flat negative-pressure germ under the theorem's pressure sign cannot obey any one fixed K/r acceleration bound on a full neighborhood.

## 5. Directional criterion and ratio consequence

On the nonzero set write v=f n with f=|v| and |n|=1. Divergence freedom gives n.grad f=-f div n. Differentiating v along itself therefore yields

    a/E=(n.grad)n-n div n.

If the Frobenius norm satisfies |x||Dn|<=L there, then |a|<=K E/|x| with K=(1+sqrt(3))L. At velocity zeros a=Dv v=0, so the undivided inequality extends automatically. No direction field is defined or required on that zero set. Bounded |Dn| gives the bounded-coefficient version. Smoothness of v alone does not imply either bound for its normalized direction.

For tail notation with P(0)=0, set H=E/2-P. Suppose H>=0, v=0 on {H=0} and Rratio=E/H<=Rstar<2 on {H>0}, throughout a full neighborhood. For0<Rstar<2 this gives

    -P>=kappa E, kappa=1/Rstar-1/2>0.

The inequality extends across {H=0}. The theorem excludes a nonzero infinitely value-flat germ with the additional inverse-radius acceleration control. It includes the negative endpoint -P>=E by kappa=1. If Rstar=0 then v=0, and the pressure mean identity with a=0 and F=-P>=0 gives P=0.

The new cylindrical negative-pressure stationary example has bounded a/E near its outer boundary but limsup R=2, so it supplies no fixed positive kappa. The positive-pressure axis example fails the negative sign altogether. Neither contradicts this theorem.

## 6. Verdict and outstanding assumption

The pressure mean, all three exclusion versions, the geometric sufficient condition and the ratio consequences are CONFIRMED. The proof uses incompressibility through div(v tensor v)=a and through the direction identity. Its constants and argument are independent of omega.

The actual coupled tail equations have not been shown to give bounded |x||Dn| or |a|/E<=K/|x| at a supported common flat point. The unrestricted negative endpoint, A1502 and the arbitrary-helicity bare-decay rotating-profile conjecture remain OPEN. The added bound cannot be omitted from a report statement or described as a consequence of smooth flatness.
