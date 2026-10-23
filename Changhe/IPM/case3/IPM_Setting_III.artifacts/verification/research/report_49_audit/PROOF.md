# Draft 49: forced logarithms and repaired scope

Verifier result 155, written 2026-10-21 before its supporting checker. This audits the frozen report with SHA256 06251778350ce6d7dcf85882e032617f206ed757c55cedd2b1f6e806de012798. The exact calculation of result 150 and the numerical/transcription audit of result 153 are dependencies, not new computations of a profile. The claim audited here is that the revised statements follow under their stated hypotheses. No existence endpoint is asserted.

## 1. Statement and notation

Let rho and its canonical full-plane velocity be smooth Setting III fields in the symbol class S^p, where p=1/ell, ell>1 and delta=1-p. S^p means that every Cartesian derivative of order j is O(r^(p-j)) outside a fixed disc. Assume exact exterior transport (ell X+U).grad rho=rho. The finite-depth expansion theorem of result 142 applies. The additional trace hypothesis in 3.69 is r^(-p)rho -> A sin(theta), A nonzero. All assertions about coefficients below are conditional on these hypotheses.

The report denotes the stream frequency by 2m. Result 150 denotes that same positive even frequency by M. Thus M=2m. The two cases are (ell,k*,m)=(3,5,1) and (5/2,9,2). Set s_k=p-k delta. This audit confirms 3.69 and A.3.69, the three repairs requested in result 153, and the corresponding summary statements. Earlier unchanged report claims retain their prior audits; they are not all re-proved here.

## 2. The three repairs

For a density term r^s P(log r,theta), its source is r^(s-1)G(log r,theta). In stream mode 2m, a particular stream r^(s+1)Q(log r) solves

    [4m^2-(s+1)^2]Q - 2(s+1)Q' - Q'' = G.

Off resonance this triangular polynomial equation preserves the highest logarithmic degree if G is nonzero. At s=-2m-1 it becomes 4m Q'-Q''=G. With the constant harmonic coefficient set separately, a nonzero G of degree d has a solution of degree d+1; if G=0 take Q=0. The revised bound "at most d+1" is therefore correct, including vanishing resonant projections. A harmonic coefficient is global data and cannot cancel the logarithmic coefficient.

A first logarithm can enter this induction only at resonant inversion. Once it has entered, nonresonant inversion, multiplication and transport inversion can move it to other radial degrees. The revised 3.68(c), A.3.68 Step 5' and their explicit propagation sentence state this distinction correctly. Products can subsequently increase log powers; the claim about creation is read, as its proof explains, as the first source of logarithms from initially logfree expressions.

For a steady DR state c_w rho=(c_x X+U[rho]).grad rho, division of rho and U by c_w gives the normalized profile with ell=c_x/c_w. The positive c_w and ell>1 hypotheses in the revised Section 7 are sufficient for this normalization, provided the other Setting III conditions are separately checked. Neither positivity nor the other conditions follow merely from a time stepping gauge. The report states the required ratio and does not claim automatic existence.

## 3. Deficits, recurrence and the first resonance

An interaction of density deficits t1,t2 through the induced velocity has deficit delta+t1+t2. A harmonic velocity of degree -2m-1 acting on density deficit t has deficit 2m+2+t. Harmonic costs are therefore at least 4. Starting from deficit 0, all density deficits belong to

    { k delta+2l : k>=0, l=0 or l>=2 }.

This set is closed under both operations. Transport inversion preserves radial degree. The induced part of canonical velocity inversion preserves the density degree; its additional harmonic terms have already been counted separately. This is the precise interpretation of the shortened "canonical inverse preserve degrees" sentence in A.3.69 Step 1.

For a sine density term, direct differentiation gives

    d_x[r^s sin(n theta)] = r^(s-1)
      [(s-n)/2 sin((n+1)theta)+(s+n)/2 sin((n-1)theta)].

For a stream h r^sigma sin(j theta) acting on a density P r^s sin(n theta), U_r=-psi_theta/r and U_theta=psi_r give

    U.grad rho = (hP/2) r^(sigma+s-2)
      [(sigma n-js)sin((n+j)theta)-(sigma n+js)sin((n-j)theta)].

The source division is H_j=G_j/[j^2-(s+1)^2]. Hence at a pure deficit k delta, before resonance,

    P_k = [ell k delta]^(-1) sum_(i+j=k-1) B(H_i,P_j).

Both signs and the positive divisor agree with the equation ell r rho_r-rho=-U.grad rho. The amplitude degree is k+1.

At ell=3, delta=2/3 and the first resonant density degree is -3, reached by k=5. Every nonpure deficit is at least 4, larger than 10/3. At ell=5/2, delta=3/5; the possible degree -3 would require deficit 17/5, which is neither pure nor at least 4. The degree -5 requires deficit 27/5. A coincidence with a nonpure degree would require 3(k-k')=10l, l>=2, whose smallest possible positive k-k' is 10. Thus no nonpure sector reaches a pure degree with k<=9. No earlier inversion is resonant. These facts also exclude an earlier logarithm from another sector.

The exact recurrence calculation of result 150 gives

    g* = -177047/301056000000 * A^6                  (ell=3),
    g* = 26243642326438735772269905591088207
         /4898218301752285282303033607434666157015040 * A^10
                                                            (ell=5/2).

Its two independent implementations compare every intermediate density and stream coefficient. The report transcribes these numbers correctly. This audit rechecks the frozen evidence and its conversion of notation, not a decimal approximation to these numbers.

## 4. First stream and density logarithms

At resonant stream exponent -2m,

    -Delta[q r^(-2m) log(r) sin(2m theta)]
      =4m q r^(-2m-2) sin(2m theta).

Thus q=g*/(4m). The velocity's highest logarithmic part is

    U_r=-(g*/2) r^(-2m-1)log(r)cos(2m theta),
    U_theta=-(g*/2) r^(-2m-1)log(r)sin(2m theta).

Acting on A r^p sin(theta) gives

    -(A g*/4) r^(p-2m-2)log(r)
       [delta sin((2m-1)theta)+(1+p)sin((2m+1)theta)].

Why is this the entire first logarithmic forcing? Use the finite expansion induction in decreasing degree, rather than assuming the conclusion. There is no logarithm above the first resonant stream degree, as proved in Section 3. Its velocity degree is v=-2m-1. Any logarithmic velocity of this degree must come from that single resonant term. Its product with a density gradient of degree at most p-1 has degree at most t=v+p-1. Equality uses the leading density. The transport inverse cannot create a logarithm from logfree forcing. Inductively there is no density logarithm above t. A density logarithm of degree at most t, after a derivative and multiplication by any velocity of degree at most p, contributes degree at most t-delta<t. Its own induced velocity also contributes only at that smaller degree. Other logarithmic velocities are strictly below v. This finite descending argument rules out a same-degree feedback term and proves the claimed uniqueness of the forcing at t.

The highest-log coefficient of ell r partial_r-1 at degree t is ell(t-p)=-2ell(m+1). The transport equation has the negative advection on its right side, so the density logarithm equals the displayed forcing divided by 2ell(m+1). Its factor is therefore -A g*/[8ell(m+1)], as in 3.69(c). It is nonzero. The explicit coefficients are (-A g*/72,-A g*/36) in degrees -11/3 at ell=3, and (-A g*/100,-7A g*/300) in degree -28/5 at ell=5/2. The report transcribes them correctly.

## 5. Verdict and scope

CONFIRMED: the three repairs, 3.69, its proof and its summary under the explicit conditional hypotheses. The phrase in Step 1 about degree preservation refers to the induced inverse, with the harmonic part separately counted; adding "induced part of" would remove any possible ambiguity. This is a wording clarification, not a missing mathematical step in the given context.

The exact trace hypothesis is essential to the specific computed coefficients. The report makes no assertion for another trace. Its timeline references to manufactured DR checks are method claims, not simulations. Logarithms at infinity do not contradict local smoothness on the plane. No exact profile has been constructed or excluded, and the primary endpoint remains OPEN. The later high-mode extension of the external audit is not included in this verdict.

Supporting checks are finite algebra and transcription checks. They do not verify an infinite expansion, a uniform numerical residual, or a time-dependent solution.
