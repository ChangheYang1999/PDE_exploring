You are an independent mathematical researcher and referee, consulted by another researcher working on the problem described below. Be skeptical, concrete and complete; check every step you rely on; say plainly when something is wrong, unproved, or only conditional. Your final message is your answer: make it self-contained.

Machine rules (no exceptions): never start a server or anything that listens on a port; never run JavaScript tooling (node, npm, npx, pnpm, yarn, vite, playwright); no GPU; wrap shell commands in `timeout 540`; single-threaded computations under 2 GB RAM. Write files only in your current directory. Do not modify any other file.

Question:

Literature check (please be precise; give exact theorem statements, hypotheses, function classes, and arXiv numbers/years; say plainly when you are not sure a result exists).

Context. The 2D incompressible porous media (IPM) equation on the whole plane R^2:
  d_t rho + u . grad rho = 0,  u = grad^perp Psi = (-Psi_y, Psi_x),  -Laplace Psi = d_x rho,
equivalently u = -grad p - (0, rho), div u = 0, i.e. u = (-R1 R2 rho, R1^2 rho) with Riesz transforms R_j.
Self-similar ansatz rho(t,X) = C_rho(t) R(C_l(t) X) leads, after normalizing the density exponent to 1, to the stationary profile equation
  (c_l X + U) . grad R = R,  U = grad^perp psi,  -Laplace psi = d_x R   on R^2,
with unknown scalar c_l. We study profiles that are even in x and odd in y, with R = x^2 y a(x,y) near 0, a(0)=1, and the compatibility 3 c_l - psi_xy(0) = 1.

Questions.
1. Which papers construct or numerically compute self-similar (or approximately self-similar) blowup profiles for IPM, with or without a boundary? In particular: Wang, Lai, Gomez-Serrano, Buckmaster et al. "Discovering unstable singularities" (2025) for IPM with boundary; any follow-up computer-assisted proofs of IPM blowup (e.g. by Chen, Hou, or others); Cordoba, Martinez-Zoroa and others on IPM singularities (with forcing, in Holder classes, or in the whole space). For each: domain (half-plane with wall, strip, whole plane), symmetry class of the profile, the self-similar ansatz and exponents, profile growth at infinity, regularity of the profile, and how the velocity of a growing profile is defined (renormalized Biot-Savart, subtractions, boundary conditions).
2. What is known about nonexistence of self-similar blowup or of stationary/self-similar profiles for IPM (Liouville-type theorems, e.g. for profiles in L^p, decaying profiles, or bounded profiles)? Cordoba-Gancedo-Orive "Analytical behavior of 2-D incompressible flow in porous media" (2007), Elgindi "On the asymptotic stability of stationary solutions of the inviscid incompressible porous medium equation" (2017), Castro-Cordoba-Lear (2019) on the strip, Kiselev-Yao (2023) small scale formation, Jo-Kim, Bianchini-Crin-Barat-Paicu, Park, etc. Give exact statements.
3. Is the whole-plane problem with rho odd in y equivalent to the half-plane problem {y>0} with the wall condition u_2 = 0 at y=0 (Dirichlet Green function) when rho vanishes on y=0? Comment on whether the "wall" profiles of the literature (which do not vanish on the wall) can be related to our odd-in-y class.
4. Any results on smoothness selection for self-similar profiles in transport equations with stagnation points (eigenvalue/resonance conditions at sources of the self-similar vector field), e.g. in Chen-Hou, Elgindi-Ghoul-Masmoudi, Eggers-Fontelos, that would constrain c_l.

Write your answer as a structured list. Distinguish what you have verified from memory or from fetched abstracts (you may read arXiv abstract pages) from what you are guessing.
