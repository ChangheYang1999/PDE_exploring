# Notes118-119: the aligned-family insertion and the four open routes

## 1. Exact scope and evidence

This audit concerns this report at SHA256 bf26780396864cdf045378dac0a1b906f9c4402cdf3af7e37406f11574f01854, together with the four contemporaneous companion files pinned by in the team records. The report has6733 lines. The baseline is Note117, SHA256 fec0c41e4698e801f8f222bbf1eea7afeb01611d953440da35d069e91fe15819, whose scoped audit is in the team records. Its scalar-W0 omission A2314 remains an exception unless explicitly repaired.

Every new report change and every companion change was read:12568 report-delta characters,19396 assumptions-delta characters and3106 obstruction-delta characters. THEOREM_ATTEMPTS and README are unchanged. The complete named2A,2B,2C,2D foundation blocks remain byte identical, with hashes recorded in the team records. AppendixA begins at4703; AppendixB begins at5167. The claimed approval below covers the front, main text and AppendixA, plus earlier specifically audited changed historical clauses. It does not newly certify all of AppendixB-D.

## 2. LIT296 retains its prescribed-family hypotheses

Write a=1-2c, b=2(1-c) and eta=a/b. The independent proof in the team records, Sections1-7, establishes the complete next-scalar obstruction for the smooth local leading system with carrier

    X=(cx+ry-vz,-rx+cy,1+vx+cz),

for every0<c<1/2, every real r, every v>0 and integer n>=4. Its hypotheses fix speed1 at the point, S(0)=1, the leading transverse potential Re((x+iy)^n)/n, the aligned gradient and the prescribed section pressure jets through degree3. Every remaining smooth completion and every C1 scalar are excluded by a nonzero coefficient in the complete next-scalar Poisson equation after imposing both transports.

The new AppendixA and ASSUMPTIONS rows retain all these qualifications. They identify the rotation magnitude sqrt(r^2+v^2), so examples of the prescribed carrier family cover each nonzero rotation magnitude. This is not an assertion that an arbitrary zero at a fixed physical point can be converted to the prescribed pressure jets. For each magnitude Omega>0 one can choose r=0,v=Omega. Rotation of the adapted frame handles the direction; the prescribed family remains the restriction.

The main-section insertion says prescribed aligned-gradient, fixed-phase earlier jets, unit carrier speed and S(0)=1, and explicitly leaves arbitrary earlier jets and n=3 open. O12 says the whole aligned family of LIT293 and every off-axis carrier; this is read with the normalized carrier and prescribed jets of the LIT296 statement, not as removal of those hypotheses. Repeating the normalization there would improve precision, but the stated family reference supplies it. No general off-axis zero or actual global profile is excluded by this local family calculation. The confirmed scopes A2307-A2311 and open scope A2312 are preserved.

## 3. The four open statements and their implications

For the profile-level discussion retain every hypothesis of the theorem invoked. Specifically, let2/5<c<1/2, omega real, U in C2(R3), P in C1(R3), div U=0 and

    (1-c)U+DU((cI-omega J)y+U)+omega JU+grad P=0,

where Jy=e3 cross y, and assume U tends uniformly to0 at infinity. Helicity-free means U.curl U=0 everywhere. Theorem7 adds DU(y)=O(|y|^(1/2)), or its stated separately proved sufficient replacement. In this class the natural velocity and derivative bounds hold and define the actual C1 leading tails V,P2; put W=curl V and S=P2-|V|^2/2. Define

    T0={w in S2 intersect supp W: V(w)=DV(w)=S(w)=P2(w)=0}.

First, assume the tail V is smooth near every point of T0. The pressure equation supplies smooth S there. Theorem7(f), equivalently A1292, says a nonzero profile then has some point of T0 at which both V and S vanish to infinite order. Therefore an exclusion of all such common infinitely flat points gives U=0 in that precise smooth-tail subclass. This is the first new bullet. It does not say that every finite-order point of T0 is individually excluded. The complete A1292 proof conclusion was reread in the team records, Section9.

Second, suppose every profile in Theorem7 has either T0 empty or a tail smooth near T0. If T0 is empty, Theorem7(c) gives U=0. Otherwise combine smoothness with the first proposed exclusion and Theorem7(f). Thus the first two open statements together would give U=0 throughout Theorem7's class. The references A1145,A1190 only give smooth tails from all-order natural derivative bounds, allowing original smoothness merely outside a compact set in the latter result. They do not establish smoothness from the stated C2 assumptions alone.

Third, if decay and the other C2 helicity-free profile hypotheses imply DU=O(|y|^(1/2)), every such profile enters Theorem7. Combining this hypothetical derivative implication with both previous proposed exclusions gives U=0 without the added derivative assumption. No part of this bullet proves the derivative implication. Its implication is simple inclusion of classes, not a new PDE estimate.

Fourth, Theorem6/A571 requires the profile hypotheses above and global zero helicity, but no derivative bound or tail condition. It gives a specified witness whenever U is nonzero: an appropriate vortical carrier equilibrium, irrotational carrier equilibrium, or flat periodic carrier orbit, each in the indicated vortical closure and with its stated spectral or Floquet rate. If none of the three witness alternatives of that exact theorem can occur, its contrapositive directly gives U=0 for every helicity-free decaying C2 profile. All three must be excluded, not merely one witness chosen in an attempted proof. The new bullet says exactly this.

These implications all concern global zero helicity. They do not give a theorem for profiles whose helicity takes both signs. The new closing sentence correctly leaves the sign-changing-helicity C-infinity problem open. The actual common-flat, smoothness, derivative and witness-exclusion statements remain OPEN; confirming their conditional implications is not confirming them.

## 4. Remaining exception and assembly conclusion

The new changes do not repair A2314: the scalar-multiplier summary still lacks the requirement that W0 itself satisfy the same bracket equation as W. A2315 supplies the exact valid replacement. The counterexample and proof in the team records, Section3, therefore still apply to the corresponding unchanged AppendixA and ASSUMPTIONS sentence in this pin.

Subject to this single explicitly retained exception and the normalized-family reading in Section2, the Note118/119 insertions preserve every cited theorem scope, and the front/main/AppendixA assembly is confirmed. A clean approval of this pin, a blanket historical approval and the unrestricted arbitrary-helicity decay-only conjecture are not established. No computation beyond deterministic file comparison was needed or executed.
