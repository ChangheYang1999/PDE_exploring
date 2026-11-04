# Independent audit of the Pan-Zhang2024v1 Carleman scope

Status: independent reconstruction complete; existing configured model comparison and designated verdict pending. Submitted source audit SHA25663f196868292942088adb7b317765a4e7651304d4fdc67f929630bb6e7d5da92. All five source sections and18 manual checks were read. The actual primary PDF is retained in the adjacent Example4 audit, SHA2560b0954e59be965e9a3456fb7c3ba019fe45c2116ecc36ffe5bd6dd08b5741249. Printed pages20-22 were read as text and each rendered page was visually inspected here.

## 1. Exact statements under review

Write partial=(partial_x-i partial_y)/2 and dbar=(partial_x+i partial_y)/2. Proposition6.3 on printed page20 assumes u in H1(C;C^N), supported outside a neighborhood of0, and any half-integer lambda in Z+1/2. It asserts

    integral_C |u|^2 r^(-2lambda-2)
       <=16 integral_C |dbar u|^2 r^(-2lambda),               (P)

as well as the corresponding partial estimate. Its printed hypotheses impose no compact support or separate weighted integrability. Page21 first proves compact support and then estimates weighted approximation errors by ordinary H1 errors.

Corollary6.4 on page22 assumes u in Hl_loc(C), zero near0, positive integers k<=l, multi-indices alpha<=beta componentwise with |alpha|=k and |beta|=l, and a half-integer lambda. It claims

    integral |partial^alpha1 dbar^alpha2 u|^2 r^(-2lambda-2(l-k))
       <=C_l integral |partial^beta1 dbar^beta2 u|^2 r^(-2lambda). (H)

The following countertests satisfy exactly those printed unweighted hypotheses. They do not address a different version of the manuscript or an implicitly repaired statement.

## 2. Global H1 countertest for the negative weight

Choose smooth radial chi, equal0 for r<=1 and1 for r>=2, with0<=chi<=1. Set u=chi(r)z^(-2) off0 and u(0)=0, and lambda=-5/2. The cutoff makes u globally smooth. At infinity |u|=r^(-2) and |Du|<=C r^(-3), so the radial L2 and gradient tails are bounded by constants times integral_2^infinity r^(-3)dr and integral_2^infinity r^(-5)dr. Both are finite. Thus u belongs to global H1 and is supported outside a neighborhood of0.

Since z^(-2) is holomorphic away from0, dbar u is supported in1<=r<=2. The right side of(P) is therefore finite. The left side on r>=2 is

    2pi integral_2^infinity r^(-4) r^3 r dr
       =2pi integral_2^infinity 1 dr=infinity.

This disproves(P) at an allowed half-integer. Replacing z^(-2) by conjugate(z)^(-2) gives the identical countertest for the partial version.

The failure in the printed approximation is concrete: at lambda=-5/2 the multiplier r^(-lambda)=r^(5/2) grows at infinity, whereas page21 bounds it by the value at the fixed inner radius. The left multiplier r^(-lambda-1)=r^(3/2) also grows. Unweighted H1 approximation cannot support either displayed error estimate.

## 3. Local H2 countertest for a positive weight

With the same chi, set v=chi(r)z^2, k=1, l=2, alpha=(1,0), beta=(1,1), lambda=1/2. The function is smooth and in H2_loc, is zero near0, and the multi-index conditions hold. For r>=2, partial v=2z and partial dbar v=0. The right side of(H) has compact support and is finite. The left side includes

    2pi integral_2^infinity 4r^2 r^(-3)r dr
       =8pi integral_2^infinity 1 dr=infinity.

Thus the printed local-Sobolev corollary fails even at a positive half-integer. The example is not in global H2; the source assumes only local H2, which is precisely why it is admissible.

## 4. Valid repairs, with proofs

For compactly supported H1 functions away from0, the full Fourier argument in the team records, Section5, proves(P) for every half-integer. It includes every angular mode and has the exact squared constant16. Both weights are bounded on a containing compact annulus, so approximation passes to the limit there. Conjugation gives the partial version.

For noncompact global H1 functions supported outside r0>0 and lambda>=0, the two multipliers r^(-lambda-1) and r^(-lambda) are bounded on that exterior region. Approximate by smooth compactly supported functions vanishing on a slightly smaller fixed disc; ordinary H1 convergence then controls both weighted errors. This proves(P) on this sufficient noncompact class. No maximal noncompact class is claimed.

For compactly supported Hl functions away from0, let d=l-k. Start with the derivative of order k and apply(P), choosing partial or dbar according to the next required derivative, with weight parameter lambda+d-1. This bounds the weight exponent2lambda+2d by the next derivative with exponent2lambda+2d-2. Repeat d times, shifting the parameter down by1 each time. All parameters remain half-integers, the final derivative is beta, and the resulting squared constant is16^d<=16^l. Approximation on a fixed annulus proves the Hl statement. If d=0, it is the identity inequality. This supplies the compact repair of(H) without the unsupported global claim.

## 5. Effect and limits

Theorem6.1 uses u_k=psi_k eta u with a compactly supported outer cutoff eta, as directly visible on page22. Hence its continuation route only requires the valid compact version of(P). The complete independent proof of the strict theorem, including both cutoff limits and global propagation, is in the adjacent vector audit. The countertests here do not refute that theorem or the scalar inverse-radius theorem.

The tests concern behavior at infinity of auxiliary planar functions. They construct no Euler profile, pressure, divergence-free carrier, decay-compatible transport or counterexample to the main rotating conjecture. They certify neither all later uses of the corollary nor the entire manuscript. No mathematical computation or formal proof assistant was used. The original printed pages, rather than an abstract or OCR alone, determine the scope of this audit.

## 6. Existing model comparison

The complete Theory Agent C comparison dated2026-11-04T04:43:19Z was read. Items11-14 agree with the exact v1 statement, the two counterexamples, the compact-annular repair and the limited effect on Theorem6.1. For the more general tail chi z^(-k), k>=2, the left radial power in(P) is -2k-2lambda-1, so divergence occurs exactly when lambda<=-k. For k=2 the largest allowed half-integer causing divergence is-5/2. This verifies the note's arithmetic without claiming failure at-1/2 or-3/2.

The H2_loc example independently fails at positive lambda1/2, which prevents the first repair from silently fixing the corollary. Iterating the compact estimate shifts lambda by integers and gives16^(l-k), as stated in Section4. Theorem6.1 uses a compact outer cutoff, removes its inner cutoff at fixed lambda, then sends lambda to infinity; these counterexamples attack neither of those legitimate limits.

The comparison reports reading the actual v1 text pages10-12 and19-23; this agent retains its own visual page coverage rather than inheriting another reader's coverage. Existing configured model collaboration is through files, with actual provider execution independently unattested. No mathematical computation or new client was needed.


## 7. Confirmed-source status revision

The exact current source has SHA256 544d84b8f2e8b3fab425688f66a3803a77cf9b332cc61bfbb5e24cf39fa16a24. The full difference from the retained submission has been read: one opening status line changes, and one final comparison section is added. The opening and final section distinguish A2933-A2934 refutations from A2935 repairs. They do not refute Theorem6.1, extend the result to a journal copy or claim a new computation. No displayed equation, mathematical hypothesis or proof argument changes. The old pending sentences belong to the dated original submission and are superseded by the new status section. The capture and complete difference are retained in verification.
