# Cross-agent rechecks of the pressure obstruction and strain certificate

## 1. LIT292 proof ordering

The revised LIT292 proof has SHA256 5b5be05ba91314bc3408fc57daa2dafb07ac18ea3be233e9b2f9be51980d872f. Its entire delta against the already confirmed source was read. The mathematical statement and source coefficient are unchanged. Section 4 now first subtracts theta(p), applies the polynomial centralizer to remove degrees 1 through n-1, and only then tests the scalar equation at p. Since n>=3, this order removes both the gradient and Hessian of theta-theta(p). Carrier transport extends that order to all three local coordinates. The positive quantity Delta(H^kappa)(p)=kappa(kappa-1)b^2/q^2 then forces theta(p)=0.

This is exactly the order already made explicit in A2213 and its independent proof. The change is a clarification of the verified argument, not an assumption that a C1 scalar has Taylor coefficients without the Poisson regularity input. That input is retained in the full source and audit. The status line now cites A2212-A2216 and leaves general off-axis gradients OPEN A2217. The clarification is CONFIRMED; none of the actual-tail hypotheses or remaining open cases changes.

## 2. Independent reconstruction of the C65 certificate

The literature agent's full five-section review, 98-line Python checker, verification plan and result were read. The checker was inspected, not executed in this agent. It consumes the same exact rational certificate used in A2206; byte identity and the source hash were verified. It independently expands each Bernstein basis directly in the original x,t coordinates, rather than using the original coordinate-conversion helper.

For an interval [L,R], its basis routine expands binomial(n,k)(x-L)^k(R-x)^(n-k)/(R-L)^n. The product expansion is then compared exactly, using rational arithmetic, with each of the four polynomials freshly formed from the stated multiplier coefficients. Strict positivity of every stored Bernstein coefficient proves positivity on each closed rectangle. The checker verifies containment, pairwise disjoint interiors and equality of the rational total area with the domain area. Because finitely many closed rectangles are used, those tests exclude a missing boundary point as well as an open gap: any missing point would have a relative open neighborhood in the complement of their closed union and therefore positive area.

At each of the three origin corners, it independently reconstructs g', verifies the lower quadratic and mixed coefficients, and expands the strictly positive Bernstein certificate for 4a0 delta-alpha0^2 t. Completing the square gives strict positivity away from the origin. It also checks g/t>0, the small-t threshold, both exact positive combinations with negative constant density, and the comparison margin. Thus its reported 301 rectangles, three corners and two linear-family obstructions prove exactly the algebraic assertions used in A2206 and A2208. No samples or optimization minima enter.

The source RESULT records an actual runtime of 1.6259963898919523 seconds on its assigned CPU54, nice19 by its accompanying record, with OMP1. This agent performed only the byte/hash check and code review. The mathematical argument remains the C2/C1 full-profile theorem with Hb and both global bounds: -lambda_min(sym DU)<=6/5 (or |sym DU|^2<=54/25) and |curl U|^2<=103/100, for every 0<c<=1/2 and every real omega. The alternate checker agrees with the designated audit; it adds no decay-only result or nonlinear optimality claim.

## 3. Collaboration and scope

All three sections of this audit were read. The direct-basis reconstruction is an additional independent check of an existing certificate, not an independently generated certificate or a formal verification. The LIT292 change affects proof order only. These confirmations retain A2217 and A2211 as OPEN outside their respective domains.

The existing collaboration uses the configured model coordinator and theory agents together with the literature and audit agents. No new model client was invoked, and actual provider execution remains independently unattested. No new numerical experiment, formal build, server or outside-agent write was performed.
