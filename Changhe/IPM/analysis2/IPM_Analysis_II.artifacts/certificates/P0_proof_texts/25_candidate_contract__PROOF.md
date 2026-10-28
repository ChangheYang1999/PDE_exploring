# Necessary point tests for the full reference contract

## Statement and scope

Use the weighted fractional norm N_(s,R) of topics18 and20, with R>=1 and 0<s<=2^-12. The sufficient reference contract in16_weighted_fractional/REFERENCE_AUDIT.md requires the global Euclidean tensor bound |D^2 rho|<=3, even after the low matrix hypothesis is weakened in topic24. At every point, |rho_yy|<=|D^2 rho|. Thus a rigorously enclosed value |rho_yy|>3 at one point refutes that particular contract for the supplied reference. No conclusion about the existence of an exact profile, a theorem with larger derivative constants, or other references follows.

The same norm has the reference-independent point evaluation bound

    |f(X)| <= 16 max(1,|X|^(1/5)) N_(s,R)(f)

on its density parity completion. This is topic18's embedding, proved through the Bessel kernel and weighted interpolation; it needs no reference matrix certificate. Therefore every rigorously evaluated nonzero residual at a fixed point supplies a norm lower bound. This remains valid for the admissible candidate residuals, whose smooth tail has degree gamma-6delta<-2 and hence belongs to the completed forcing space.

## Independent evaluation

The exact candidate coefficient vector is reconstructed in topic19. For A2 and A3, the topic22 certificate differentiates the full Cartesian potential through order seven and independently differentiates its one-dimensional restriction to the vertical axis. Writing Phi(y)=chi(0,y) and A_x(y)=chi_xx(0,y), the two methods compare

    q''(y)=rho_yy(0,y)=-chi_xxyyy(0,y)-chi_yyyyy(0,y)
                        =-A_x'''(y)-Phi'''''(y).

Both methods use 768-bit Arb. The new check binds those records to their exact source and dependency hashes, compares the saved enclosures, and tests the strict endpoint inequalities. The complete two-method identity is established in22_axis_constraints/PROOF.md; using it here does not introduce a fresh unverified derivative formula.

For the A4 residual point bound, use X=(3,4), so |X|=5. Topic19's independent Cartesian and polar evaluations give the same Arb enclosure of F(3,4). Dividing its absolute lower bound by16*5^(1/5) gives a strict lower bound for N_(s,R)(F). The present check performs this division with directed interval arithmetic. It does not estimate a norm upper bound or certify any global coefficient inequality.

## Findings

The completed check records strict values and verdicts. A2 and A3 violate |D^2 rho|<=3 at (0,1/10), separately from their violations of the older19/5 matrix floor. The weaker matrix theorem consequently does not by itself make them valid references for the complete current contract. A4 has a certified positive residual lower bound even if its coefficient hypotheses were all to pass. Later references require their own checks.
