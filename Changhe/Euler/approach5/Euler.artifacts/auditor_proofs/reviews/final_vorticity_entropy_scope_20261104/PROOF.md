# Compact-set scope of frozen-vorticity entropy

Date: 2026-11-04T13:04:53.166857+00:00.

## 1. Exact proved statement and the summary issue

Let c>0, omega be any finite real number, U,P be C2 on R3, div U=0, and suppose the rotating profile equation holds and U=o(|y|) uniformly. Set B=(cI-omega J)y+U, Omega=curl U, and let Phi be the complete B flow and Gamma the frozen Omega flow. For every compact set K invariant under all Gamma times,

    h_top(Gamma_1 restricted to K)=0.

This is exactly A015. The AppendixA row at line6111 of reportd12bf1ef says only "zero entropy of the Omega-flow". Its H0,H1' column does not specify a compact invariant set or a convention for entropy on a noncompact phase space. The exact proposed text is "zero topological entropy of the Omega-flow on every compact Omega-invariant set". This leaves all profile hypotheses and every theorem unchanged. No noncompact global entropy assertion is certified by the present proof.

## 2. Complete compact-set proof

Write b0=1+c>0. Uniform sublinearity gives complete Phi and a common compact ball containing Phi_s(K) for all s<=0: the radial component B(y).y is positive outside a sufficiently large ball, independently of omega because Jy.y=0. The exact vorticity transport law gives

    D Phi_s Omega=e^(b0 s) Omega composed with Phi_s,
    Phi_s Gamma_t=Gamma_(e^(b0 s)t) Phi_s.

The second identity follows from local uniqueness. On a compact invariant set all restricted Gamma orbits exist for every real time; the same is true on its Phi images. Fix L>0, put K_n=Phi_(-nL)(K), and choose one closed ball D containing all K_n. The restricted flow on K_n is conjugate to the flow on K with time multiplied by c_n=e^(b0 nL). Thus

    h_top(Gamma_1 restricted to K_n)=c_n h_top(Gamma_1 restricted to K).

For completeness, the real-time entropy uses the orbit distance max_(0<=t<=T)|Gamma_t x-Gamma_t y|. Uniform continuity on a compact invariant set identifies this entropy with the time-one definition; time acceleration changes the interval length from T to c_n T, so multiplies entropy by c_n. A homeomorphism between compact invariant sets preserves entropy by uniform continuity in both directions.

Since Omega is C1, M=sup_D||D Omega|| is finite. For x,y in any K_n, both trajectories remain in D, and the mean-value bound on this convex ball and Gronwall give |Gamma_t x-Gamma_t y|<=e^(Mt)|x-y| for t>=0. Cubes of side eps e^(-MT)/sqrt(3), with one point selected in each occupied cube, form an eps-spanning family of at most C_D(1+eps^(-1)e^(MT))^3 points. Hence h_top(Gamma_1 restricted to K_n)<=3M for every n. Dividing by c_n and letting n tend to infinity proves zero entropy on K. This is a proof for compact invariant sets; completeness and slow escape on the whole space alone do not provide the common derivative bound for noncompact invariant sets.

The adjacent no-periodic-vortex-line assertion is unaffected. A nonconstant periodic orbit is compact, and Phi_(-nL) sends its period T to e^(-b0 nL)T. On the common ball the periodic velocity v=Omega(Gamma_t x) has mean zero and |v'|<=M|v|. Wirtinger's inequality forces T>=2pi/M if M>0 and excludes such an orbit if M=0. The shrinking periods contradict that uniform bound.

## 3. Audit disposition and evidence

The complete155-line A015 source and78-line global-completeness/recurrence proof were freshly read. A015's compact-set entropy conclusion and A014's no-periodic-line conclusion remain CONFIRMED. Report approval at the unqualified noncompact reading is OPEN; this is a missing scope qualifier, not a counterexample to a global entropy claim and not a gap in the source proof. The periodic B-orbit period bound already checked in A030 is a different flow statement and remains unchanged.

Evidence is the captured source and exact report row in verification. No numerical calculation or new external theorem is used. Existing A/C/coordinator comparison is through working files only. This final-phase scope repair does not introduce a new research direction; the main arbitrary-omega nonexistence conjecture remains OPEN.
