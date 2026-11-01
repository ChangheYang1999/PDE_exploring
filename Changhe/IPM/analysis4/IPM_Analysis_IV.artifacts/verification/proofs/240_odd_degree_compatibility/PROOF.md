# Odd-degree compatibility on finite profile spaces

Status: independently checked proof of the theory part's Proposition T_(Q,h).8. The conclusion about convergent series retains every response hypothesis of Theorem T_(Q,h).5.

## Statement

Let h>=2 and Q>2h be coprime integers, with Q odd, and set delta=2h/Q. Let V be a finite-dimensional real linear space of finite real odd-frequency sine polynomials. Define O_Q(f) as the coefficient of sin((2h-3)theta) in the density term f_Q constructed from leading profile f by the nonresonant recursion below Q. Define sigma_k(f), k>=1, as the response of the next compatibility coefficient to a unit free stream harmonic at order kQ.

Both O_Q and sigma_k are homogeneous polynomial functions of degree Q on V, allowing the zero polynomial. Consequently they are odd. Every two-dimensional subspace W of V contains a nonzero f with O_Q(f)=0. If O_Q is nonzero on V, its positive and negative sets are nonempty open cones interchanged by f -> -f.

For normalized profiles f(b,t)=sin(theta)+b sin(3theta)+sum t_j sin(jtheta), with a fixed finite set of odd j>=5, O_Q(f(b,t)) has degree at most Q in b and leading coefficient O_Q(sin(3theta)). If that coefficient is nonzero, there is a real root in b for every fixed real t. If it vanishes, sin(3theta) is itself compatible.

Suppose additionally that O_Q(b,0) has degree exactly Q and is irreducible over the rationals, and every finite and limiting response at t=0 is not a rational multiple of O_Q(b,0), including the zero multiple. Then the regular compatibility set is nonempty, and the genericity theorem proved in the cited dependency gives a nonempty open dense set of convergent tuned profiles on its component through a real root at t=0.

## Proof

All stream inverses below order Q are linear maps with fixed nonzero rational divisors. Inductively f_n is homogeneous of degree n in f: each ordered nonlinear product has the form of a derivative of g_i multiplied by a derivative of f_j, i+j=n, so its degree is i+j. The same applies to g_n for n<Q. Taking a Fourier coefficient of f_Q preserves its degree.

To compute sigma_k, start with a unit harmonic perturbation of g_(kQ). At its rth propagated density order, U_r is the sum of its product with f_r, terms involving a propagated stream V_s and f_(r-s), and terms involving g_(r-s) and U_s, 1<=s<r. The unit harmonic has degree zero in f. By induction U_r and V_r are homogeneous of degree r. The r=Q compatibility coefficient is therefore homogeneous of degree Q. These are finite polynomial expressions for every fixed k. Oddness follows because Q is odd.

Choose a Euclidean norm on W and a unit vector v. If O_Q(v)=0, v is a required profile. Otherwise O_Q(v) and O_Q(-v) have opposite signs. Either semicircle from v to -v stays away from zero and is connected, so continuity and the intermediate value theorem give a zero on that semicircle. For a nonzero form, a nonzero value and its negative prove nonemptiness of both sign sets; continuity gives openness, and positive homogeneity gives their cone property.

Polynomial homogeneity shows that the coefficient of b^Q in O_Q(b sin(3theta)+g) is O_Q(sin(3theta)), independently of g. When it is nonzero, the polynomial in b has odd degree Q, hence opposite signs for sufficiently large positive and negative b, and therefore a real root. The zero-coefficient case has the stated compatible pure mode by its definition.

Finally, the nonzero degree-Q polynomial O_Q(b,0) has a real root b_0. Its irreducibility in characteristic zero makes it square-free, so its b derivative at b_0 is nonzero. Thus (b_0,0) is a point of the regular compatibility hypersurface. The admitted genericity theorem applies with the full response and irreducibility assumptions just stated; its good set is open and dense in the regular component containing this point. Such a component is nonempty, so its dense subset is nonempty.

## Scope and dependencies

Dependencies: recurrence01, affine response144, rational majorant145 and the equal-degree genericity theorem used for the delta4/9 profiles. This argument establishes first compatibility without a response assumption, but it does not establish any response hypothesis from parity alone. It makes no assertion for one-dimensional profile spaces, h=1, or even Q. It does not give quantitative radii or an explicit compatible point in the arbitrary two-dimensional case.
