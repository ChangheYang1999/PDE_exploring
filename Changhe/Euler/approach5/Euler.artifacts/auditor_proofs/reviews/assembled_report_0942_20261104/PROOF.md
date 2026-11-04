# Report 013d8fd6: corrected hypotheses and source-gradient transfers

## 1. Object and inherited scope

The retained report in the team records has SHA256 013d8fd6552e1071b7597aa4249a3eb5f33f53089ea292c1497256618f84ace5, 7922 lines and 1256105 bytes. The full 206-line delta from eb89620e has been read, including all long table rows, together with the affected statements and their hypothesis headings. The two complete differences use different context alignments; they are not byte-identical after their headers. Each was independently applied as text to the retained base and exactly reconstructs this target.

The cumulative base is report6dd51f88, A3131, cutoff A3120. A3138 confirmed the intervening mathematical transfers of eb89620e but A3137 rejected its blanket hypothesis sentence. This review checks the correction and all subsequent changes. It preserves approval of front matter, main sections0-10 and AppendixA by induction over the exact retained differences. It does not claim a fresh reading of every unchanged line or collective mathematical approval of historical AppendicesB/C.

## 2. The repaired assumptions and energy remainders

The old sentence saying that no derivative decay was assumed has been replaced by an explicit statement that each part keeps its additional hypotheses. Part(m)'s nonexistence criterion assumes DU=o(r^(-1/c)). Its finite-amplitude consequence and part(n)'s profile consequence keep U in C2, P in C1, boundedness, distributional blow-down U(R.)->0, and DU=o(sqrt r). Thus the A3137 defect is removed.

The negative spherical-source moment comparison now distinguishes E(R)=LR^beta+O(R^(beta-1)) from E(R)/(LR^beta)->1. In the first case integration by parts gives F(R)=beta L log R+O(1); in the second it gives F(R)=beta L log R+o(log R). The finite negative moment therefore yields the asserted equality up to O(1) or o(log R), respectively. This is the A3138 qualification and does not differentiate the energy remainder.

## 3. Source-gradient inequality and sequence quantifiers

Let U in C1(R3;R3) be divergence-free, 0<beta<1, L>0 and E(R)/(LR^beta)->1. Put t=(beta-3)/2, k=(beta+1)/2, m=2-beta and K_beta=beta m(1-beta). About a fixed center a, put r=|y-a| and let U_tan be the component tangent to the centered sphere. On1<r<R, F and T integrate r^(-beta)|U|^2 and r^(-beta)|U_tan|^2, G integrates r^(2-beta)|DU|_F^2, and I integrates r^(2-beta)[q]_+. If Q_a(r)=integral_S2 q(a+r n), then J=integral_1^R r^(4-beta)[Q_a(r)]_+ dr. The Frobenius norm is used and q=tr((DU)^2). A3132-A3133 give

    F/log R -> beta L,
    kF <= sqrt(GT)+(k+1)T+C,
    J >= m[(1-beta)F+beta T]-C,  0<=J<=I<=G.

Writing U=r^t v(log r,n), the localized radial square gives G>=G_S+t^2 F-C. The errors are bounded by velocity energy on fixed logarithmic strips. Consequently, if limsup G/(beta L log R)<=M<infinity, then M>=t^2 and

    liminf T/(beta L log R) >= d_beta(M-t^2),
    liminf I/log R, liminf J/log R
      >= K_beta L + m beta^2 L d_beta(M-t^2),
    d_beta(x)=[2k/(sqrt(x+4k(k+1))+sqrt(x))]^2.

These bounds follow along a sequence realizing the tangential liminf, using the gradient limsup on that same sequence. If instead I/log R or J/log R tends to K_beta L along selected radii, the source lower bound forces T/log R->0 there. The divergence pairing then forces G/log R->infinity on those same radii. The report keeps this sequence restriction and center. Its word "equivalently" joins two consequences of the finite-radius inequality, not an assertion that one fixed-center bound implies bounds about arbitrary centers.

The large-M sharpness is the specific sine specialization of the belt construction used in A3118 and reconstructed in A3133: g_n=-k chi sin(n(theta-pi/2))/n and h_n=chi cos(n(theta-pi/2))+(chi'+cot(theta)chi)sin(n(theta-pi/2))/n. If c_chi=(1/2)integral chi^2, then K_n=c_chi+O(1/n), T_n=k^2 c_chi/n^2+O(1/n^3), M_n=n^2(1+O(1/n)) and M_n T_n/K_n->k^2. Homogeneous radial testing gives Q_n=m[(1-beta)K_n+beta T_n]>0. The normalized spherical-source coefficient is exactly K_beta L+m beta^2 L(T_n/K_n). Compact core completion gives the exact energy and a nonzero momentum curl. This proves first-order tangential and spherical-source sharpness, not pointwise-source sharpness. The report's belt reference is read as this A3133 specialization; naming it explicitly would improve precision.

## 4. The profile consequence keeps the extra derivative input

For a nonzero bounded C1/C1 full rotating profile with U(R.)->0 in distributions, the established energy theorem supplies beta=5-2/c and L>0 when 2/5<c<1/2. Hence K_beta=(5-2/c)(2/c-3)(2/c-4). This is the coefficient in report3(o). No symmetry or restriction on finite omega occurs.

Under the additional C2 and DU=o(sqrt r) premises, A3102 supplies |DU|_F<=D r^(-1/c) eventually for some finite D>0. About the origin the critical integral is at most4pi D^2 log R+C. For a fixed translated center the weights differ relatively by O_a(1/r), whose integral against the r^-1 radial bound is finite; fixed cores also contribute finite constants. Thus G_a<=4pi D^2 log R+C_a. Substitution gives the report's strict positive surplus with argument4pi D^2/(beta L)-t^2. This argument is nonnegative because the preceding lower bound applies. Since d_beta(x)~k^2/x, the surplus has leading term m beta^3 k^2 L^2/(4pi D^2) as D->infinity. Velocity decay alone does not supply D.

## 5. Single-field source attainment and version scope

A3139-A3140 establish one smooth odd divergence-free control for each L,beta with E_0(R)=LR^beta for R>=2, E_a(R)=LR^beta+O_(a,epsilon)(R^(beta-2+epsilon)), and |D^h U|<=C_(h,epsilon)r^(t-h+epsilon). Choosing epsilon smaller than h-t proves decay of every fixed derivative. Its I_a/log R and J_a/log R tend to K_beta L; T_a=o(log R), G_a/log R->infinity and G_a=o(R^p) for every p>0. Its natural rescaled gradient is unbounded. The control has a smooth Poisson pressure but fails full momentum for every c,omega by the explicit swirl-core curl. Thus it supplies kinematic attainment at tangential fraction0, completing the previously confirmed fractions in(0,1]. It is not an Euler counterexample.

The general implication from exact source attainment to T_a=o(log R) and gradient divergence follows from Section3 under the ratio alone. It is not a radiuswise claim about toroidal amplitudes. The report explicitly records A3143's invalid upper-bound inference and does not use it. It pins the first retained A comparison separately from revision524dd668. The later correction b13f5a14 is outside this report's stated cutoff and can be recorded in a later revision.

The LIT376-LIT380 source revisions are the status or explicit indexing changes checked in A3136 and A3142. No unreviewed mathematical content is imported. TableA's older LIT377 row is historically scoped to that construction; its no-attainment statement should preferably say "LIT377 alone", since LIT380 now settles kinematic attainment. The theorem text and new LIT380 row state the current result correctly.

## 6. Verdict and limitations

The corrections and new mathematical transfers are confirmed, with the scope in Sections1-5. Cumulative approval applies to this exact report at cutoffA3143, for front matter, main sections0-10 and AppendixA. It does not cover later report edits, future source revisions, entire primary papers, numerical scripts, or historical AppendicesB/C collectively. The unrestricted rotating nonexistence conjecture remains OPEN.

The text checks found no NUL, em/en dash or absolute local path; table row counts are recorded in verification. These are document checks, not mathematical evidence. The existing configured model comparisons by A, C and the coordinator were checked through their files; actual provider execution is independently unattested. No new client, computation of mathematical examples, formal build or external retrieval was used.
