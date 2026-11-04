# A nonzero curl derivative under the reduced local B67 equations

Status: exact construction CONFIRMED A2623-A2624; the contrary reduced-equation implication is REFUTED A2625; actual-tail extensions remain OPEN A2626. This result concerns the reduced equations explicitly displayed below. It is not an example of an actual Euler tail, nor a refutation of B67(a).

## 1. Statement and scope

There exist c = 3/7 in (2/5,1/2), omega = 0, a conical open set D in R3 minus {0} containing w = (1,0,0), and real analytic V:D->R3 and P2:D->R such that, with X = cx, L = (1-c)I, b = 2(1-c), W = curl V, k = X.V and S = P2 - |V|^2/2,

    div V = 0, DV X = -LV, -Delta P2 = tr((DV)^2),
    X.grad S = -bS, grad k cross grad S = 0, k = 0.

At w one has

    V(w) = DV(w) = W(w) = S(w) = 0,
    grad S(w) = e3,
    DW(w) = -2 e1 tensor e3 != 0.

Here e3 in the tensor denotes the covector h -> h3. The point w belongs to the closure of {W != 0}. Thus all the exact local hypotheses of Section 1 of auditor_proofs/reviews/w2_flat_contact_pressure_20261103/PROOF.md, including its nonzero-gradient alternative, hold, whereas DW(w) is nonzero. The conclusion of that theorem, k = 0 locally and V = X cross W/(1-2c), still holds.

The further condition W.grad S = 0 is not imposed in that reduced statement. The example explicitly fails this condition. It proves no assertion about whether the additional full-system equations or actual-tail hypotheses force DW(w) = 0. In particular the A2565 question for actual tails stays OPEN.

## 2. Velocity, homogeneity and trace

Write r = |x|, t = z/r, u = t^2 and d = 1 - 1/c = -4/3. On r > 0 define

    f0 = z^2 r^(d-3),
    V = f0(-y,x,0).

All powers of positive r are real analytic. The scalar f0 depends only on x^2+y^2 and z, so (-y,x,0).grad f0 = 0. It follows directly that div V = 0 and x.V = 0. Each component of V is homogeneous of degree d. Euler's differentiation identity therefore gives

    DV X = cd V = (c-1)V = -LV, k = 0.

The convective derivative is

    (V.grad)V = -f0^2(x,y,0).

For a divergence-free field its divergence equals tr((DV)^2): expanding the derivative gives the trace term and V.grad(div V), with the latter zero. Differentiating f0^2 = z^4 r^(2d-6) now gives

    T := tr((DV)^2)
       = -2f0^2 - (x partial_x + y partial_y)f0^2
       = r^(2d-2)[(4-2d)u^2 + (2d-6)u^3]
       = r^(-14/3)[(20/3)u^2 - (26/3)u^3].              (1)

There is no sign convention from pressure hidden in this computation.

## 3. An exact particular pressure and a local harmonic correction

Set alpha = 2d = -8/3 and K = alpha(alpha+1) = 40/9. For any twice differentiable axisymmetric angular function H(t), direct spherical differentiation gives

    Delta[r^alpha H(t)]
      = r^(alpha-2)[K H + (1-t^2)H'' - 2tH'].            (2)

For H(t) = g(t^2), the angular part in brackets is

    K g + 4u(1-u)g'' + 2(1-3u)g'.

Choose the rational polynomial

    g(u) = 729/12740 - (81/637)u - (3/182)u^2 - (3/13)u^3.

A coefficient comparison yields

    K g + 4u(1-u)g'' + 2(1-3u)g'
       = -(20/3)u^2 + (26/3)u^3.                       (3)

For example the four equations, from highest to lowest coefficient, are

    (K-42)g3 = 26/3,
    (K-20)g2 + 30g3 = -20/3,
    (K-6)g1 + 12g2 = 0,
    K g0 + 2g1 = 0.

They verify (3) using exact rational arithmetic.

Define F(t) = sum_(n>=0) h_n t^n by

    h0 = -729/12740, h1 = 1,
    h_(n+2) = [n(n+1)-K]h_n/[(n+2)(n+1)].              (4)

For n >= 2 the factor in (4) is positive and less than 1. Thus each parity subsequence of coefficients is bounded. The series and all its termwise derivatives converge locally uniformly for |t| < 1. Coefficient substitution proves

    (1-t^2)F'' - 2tF' + K F = 0,
    F(0) = -g(0), F'(0) = 1.                           (5)

No global solution of this angular equation or regularity at either pole is asserted or needed.

On the conical open set D = {r > 0, |t| < 1/2, x > r/2}, put

    P2 = r^alpha[g(t^2)+F(t)],
    S = P2 - |V|^2/2
      = r^alpha[g(t^2)+F(t) - (1/2)t^4(1-t^2)].        (6)

Equations (1)-(5) prove -Delta P2 = T exactly on D. Both P2 and |V|^2 are homogeneous of degree alpha. Hence

    X.grad S = c alpha S = -(8/7)S = -bS.

The rank condition is identically true everywhere because k = 0; this is stronger than requiring it only where W!=0. All fields are real analytic on D. No boundary condition or pressure normalization at infinity is used or inferred; the freedom to add the local harmonic function is stated explicitly.

## 4. The zero jets and the supported point

The factor z^2 in V makes V(w) = DV(w) = 0. To see the curl jet directly, differentiation gives

    W1 = -x[2z r^(d-3) + (d-3)z^3 r^(d-5)],
    W2 = -y[2z r^(d-3) + (d-3)z^3 r^(d-5)],
    W3 = 2z^2 r^(d-3) + (d-3)z^2(x^2+y^2)r^(d-5).

Consequently W(w) = 0 and DW(w) = -2 e1 tensor e3. In particular W(1,0,z) has first component -2z + O(z^3), so w is supported by the vortical open set. The trace of DW(w) is zero, and its range is precisely span X(w), as required by the differentiated carrier relation. It is a nonzero instance of that allowed rank-one form.

At w, (6) and F(0) = -g(0) give S(w) = 0. The angular derivative there equals F'(0) = 1; the radial derivative vanishes because the angular value is zero. Since grad t(w) = e3, one gets grad S(w) = e3.

For completeness, the general carrier identity here follows by differentiating k = X.V and using DV X = -LV:

    grad k = -(1-2c)V + X cross W.

Since k vanishes identically, V = X cross W/(1-2c). At w, differentiation gives X(w) cross DW(w)h = 0 for every h. This is satisfied by the displayed nonzero DW(w). The identity controls its range, not its size or vanishing.

## 5. The missing full-system equation and the precise consequence

The construction does not accidentally solve W.grad S = 0. Along (1,0,z), homogeneity and the angular Taylor expansion give

    partial_x S = (alpha-1)z + O(z^2),
    partial_z S = 1 + O(z), partial_y S = 0,
    W1 = -2z + O(z^3), W3 = (d-1)z^2 + O(z^4).

The derivative in x uses r^alpha t = z r^(alpha-1) as the first angular term. The constant angular term vanishes by (5); higher angular terms contribute O(z^2) to partial_x S. Thus

    W.grad S(1,0,z)
       = [-2(alpha-1)+(d-1)]z^2 + O(z^3)
       = 5z^2 + O(z^3),

which is nonzero for sufficiently small nonzero z. This prevents using the example as a full common-flat tail, an actual escaping direction, or a counterexample to any global Euler nonexistence assertion.

Its exact consequence is narrower: the reduced local equations and supported zero-jet hypotheses printed in Section 1 cannot imply DW(w) = 0, even with analyticity and grad S(w) != 0 and even for a parameter strictly inside the target interval. Any proof of that further vanishing for actual tails must use additional information. B67(a) itself is consistent with this example and remains confirmed.

## 6. Verification and dependencies

This proof uses only elementary differentiation, a convergent explicitly defined power series, and the exact reduced statement recorded in the earlier independent audit. The calculation in the team records checks the divergence, carrier identity, trace, pressure polynomial and all stated velocity/curl jets with exact symbolic rational arithmetic. Its nine checks passed; in the team records records the actual time. The symbolic check supports the displayed calculations but does not replace the arguments above about convergence, scope, or support.

The formal_sources directory names the source statements. No Lean or other formal build is claimed. The complete eleven-item existing coordinator comparison in the team records was read, together with its full supplemental check log. Its analytic rederivation agrees. Numerical samples are not used as proof, and its timed-out earlier script is not evidence. No external client or additional agent was started.
