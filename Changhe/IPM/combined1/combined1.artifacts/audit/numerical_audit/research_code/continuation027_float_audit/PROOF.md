# Literal audit of the preliminary 027 continuation comparison

## Statement, notation and scope

This result concerns the exact locally frozen N1 note headed
2026-10-29T13:38Z and its stored FLOAT probe tables for candidates022,
026 and the prospective027. It does not accept an immutable027 snapshot,
certify a quadrature error, or prove a statement about an exact PDE norm.
Let P be the25 ordered pairs (n,K), with n in {19,23,25,29,31} and
K in {600,900,1200,1800,2400}. Let m_j(p) be the finite positive
floating value stored as m_lower_bound for candidate j at p. Despite
that field name, these values are not validated lower bounds here.

For each pair define q_27,22=m_027/m_022 and q_27,26=m_027/m_026.
For this finite textual audit we read each decimal serialization as an
exact rational. This convention makes the audit reproducible; it does
not turn the serialized quantity into an exact PDE value. We claim
that the note's universal range0.83 to1.17 for the027/022 comparison
is false even at the displayed precision. The pair(25,900) displays
4.02e-5 to5.39e-5, whose quotient is539/402>1.17.
The pair(29,1200) displays4.64e-5 to5.57e-5, whose quotient557/464
also exceeds1.17. All25 source values and displayed pairs are checked.

## Complete finite proof

Every table entry is positive. The ratio for a pair is therefore
well-defined, and comparison with a rational endpoint is equivalent
to cross-multiplication by positive integers. One counterexample
refutes a statement quantified over all25 pairs. In particular,
53900>47034, so539/402>117/100. Also55700>54288, so557/464>117/100.
The checker enumerates P, verifies that the displayed scientific
notation equals the source formatting rule, and records exact ratios,
signs, extrema and the K>=1800 subset. Finite enumeration proves these
statements about the copied serializations without interpolation or
quadrature assumptions.

The note also calls the continuation a control for026. Different
objective functions at equal nominal step counts are a useful trial
comparison, but this finite audit neither establishes identical
accepted optimization trajectories nor a universal causal rule about
all such profiles. The reported effect of adding rows must remain
scoped to the actual experiments and measured quantities. In
particular, a ratio of positive FLOAT proxies is not a ratio of
certified correction distances.

## Dependencies and verification

The source manifest binds the complete note, current report and
status, and all three stored probe JSON files, copied into this topic
before execution. The proof is hashed before writing the checker.
The result binds all executed code and copied sources both before and
after the finite comparison. No N1 program is imported or executed.
The 027 immutable-snapshot arithmetic remains a separate future audit.
