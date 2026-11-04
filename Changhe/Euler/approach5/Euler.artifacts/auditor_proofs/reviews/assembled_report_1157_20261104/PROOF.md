# Audit of report6682d0c2

## 1. Inputs and inherited scope

The candidate is SHA256 6682d0c2fd98efa72b63e45a25b13c7e957087991dcd4d34eb3ba4b3ebc286b3 at cutoff A3225. The baseline c546a20a1ac5954227147d927a99636f59e031cffaa42d2bf1dbfca7e6603eec was approved in A3222 for front matter, main Sections 0-10 and Appendix A. Historical appendices were not collectively certified. Exact files are retained in verification. The declared and independently generated differences agree byte for byte, SHA256 6c1fd74aaf4e2debccc0300c0ce1ae9c8ae1a4eed1dc3cd56a07e82a9b86f206: 77 total lines, 64 changed-content lines, seven hunks. All lines and full table rows have been read.

## 2. Confirmed changes

The front matter correctly records the previous approved assembly and the new cutoff. Theorem 8(p) states A3223's K and J bounds exactly, retains finite M for profile applications, and cites the reviewed source and final independent proof. Its optimal global K coefficient1/m, uniform1, agrees with A3224. Since 0<beta<1 implies1/m<1<=C_beta, the distinction from the pointwise modal optimum is correct. Its statement K=o(log R) at M=H and the open J, profile and fixed-delta questions agree with A3225. Table A and the history have the same scope. These conclusions resolve checks(a) and(c) of coordinator Note252.

## 3. Sharpness quantifier in Section 5

One phrase needs clarification before assembly approval. Lines5430-5432 say, after naming a gradient rate H_beta+delta, that "for all fields with the energy law and this budget no smaller constant is possible". Read at a prescribed positive delta, this is stronger than A3224. The proof of A3224 takes any C<1/m, chooses delta sufficiently small, then chooses a field near the family supremum. It proves optimality of a coefficient that must work for every admissible delta. It does not determine the best envelope at one prescribed positive delta.

More explicitly, the known family supremum is F_beta(delta)=(sqrt(C_s^2+4C_s delta/m)-C_s)/2. Since C_s>0, for every fixed delta>0 it is strictly below delta/m, whereas its ratio to delta tends to1/m as delta tends to0. This does not prove that a smaller fixed-delta coefficient works for the whole kinematic class. It explains why the family does not establish fixed-delta optimality. That stronger question remains A3225 OPEN, as Theorem8(p) correctly says.

A sufficient repair is: "the coefficient1/(2-beta) cannot be decreased in a bound required to hold for every admissible gradient excess delta; the sharpness family proves this as delta tends to zero." The same qualification should accompany any matching summary phrase in README. This is a precision request, not a refutation of a stronger fixed-delta theorem. Other new mathematics in the exact difference agrees with the verdicts. Assembly approval remains OPEN solely for this wording repair.
