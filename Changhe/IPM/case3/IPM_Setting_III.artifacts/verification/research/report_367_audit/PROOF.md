# Audit of report 3.67 and its scope additions

Written 2026-10-21T05:00:40.041497+00:00, before the new supporting algebra. This is an audit of draft46, frozen at SHA3fccb072b4c704bbbab271e4d112f36962cf6efc3aa7d317ed893f04d02d494f. It does not decide the primary SettingIII endpoint. All mathematical statements below concern smooth parity-preserving fields on the plane, canonical U=(-psi_y,psi_x)=o(r), and -Delta psi=rho_x.

## Dependencies and inverse

The complete arguments in ../finite_far_field_cascade/PROOF.md and ../angular_mode_count/PROOF.md are inputs rechecked against this report text. They assume exact exterior transport, rho,U in S^p and uniform nonzero trace, with p=1/ell in (0,1). The report obtains these inputs from3.23 and3.7. Inverse existence for any smooth exterior S^b density, b<1, follows from ../inverse/PROOF.md by choosing max(b,0)<gamma<1. This supplies regularity at zero before using the Fourier formulas.

Report mode sin(2m theta) corresponds to our positive even index2m; its Green factor1/(4m) and moment exponent2m+1 are correct. Substituting s=r exp(-v) or r exp(v) gives the rates lambda=2m+b+1 and mu=2m-b-1. If lambda<0, the inner integral is its complete moment minus a convergent tail, accounting for the minus sign and retained harmonic term. Arbitrarily many source modes cause no problem because every log-radius derivative of r^(1-b)g_m(r) decays faster than any frequency power, uniformly in log r. Angular differentiation only costs powers of2m. All-order Cartesian exterior bounds follow from the two conormal vector fields. The finitely many slower harmonic velocity degrees -2m-1>b must be retained. Thus a compact density producing r^-3 velocity does not refute this weighted statement. The explicit threshold b=-3 gives a logarithmic counterexample, as in the complete proof138.

For general finite power-log expressions, a remainder threshold used to retain only degrees strictly above it must avoid all expression degrees. A term r^b log r cannot be put into S^b. Own proof138 now makes this missing hypothesis explicit. Report A.3.66 Step2 retains induced terms without discarding degrees equal to b, and its Step3 already chooses thresholds away from the degrees. Thus this local defect in the earlier abstract statement does not invalidate report3.67.

## Free selection of frequencies

For any odd positive j, the coefficient functional has bounds |g_j| <=4||g||_inf/pi and |g_j|<=||g||_2/sqrt(pi). If J has M+1 frequencies, a sum P of at most M sine modes omits at least one j in J. At that frequency (rho-P)_j=rho_j. Hence either norm of rho-P is at least its stated constant times min_(j in J)|rho_j|, uniformly over P. An infimum is legitimate without a minimizer or a fixed missing frequency.

Let V_M be all sums of at most M sine modes. Its invariance under multiplication by any positive scalar implies r^-p E_M(r)=dist(r^-p rho(r,.),V_M). For every nonempty subset V of a normed space, the triangle inequality and infimum give |dist(f,V)-dist(g,V)|<=||f-g||. Uniform angular convergence gives convergence in both the sup norm and the unnormalized L2 norm, proving the new exact limit to dist(Theta0,V_M). No closedness of V_M is needed.

If Theta0 has N0 nonzero coefficients and M>=N0, set L=M+1-N0. The N0 trace frequencies and n1,...,nL are M+1 distinct positive odd frequencies. After multiplication by r^-s_L, the trace coefficients diverge in absolute value, since p-s_L=L delta>0. The first L-1 cascade coefficients diverge for the same reason, and the last tends in absolute value to |A_L|. Their finite minimum therefore tends to |A_L|. This proves the sharper bound with L in both norms. When the trace has infinitely many nonzero coefficients, choose any M+1 of them and use uniform convergence. These two cases prove C(r)>M eventually for each M; no uniform threshold in M or monotonicity of C is inferred.

## Locally finite scope example and local correction

Use positive odd n, the sequence n_k=(k+1)(n+1)-1, s_k=p-k delta and the nonzero A_k of138. With chi zero on[0,1] and one on[2,infinity), set f=sum A_k chi(r/R_k)r^s_k sin(n_k theta), R0>=2 and R_(k+1)>2R_k. At derivative order at most j each term is bounded by C_j|A_k|(1+|s_k|+n_k)^j r^s_k on its support. For k>=1 choose R_k large enough to make C_j|A_k|(1+|s_k|+n_k)^j R_k^(-k delta/2)<=2^-k for j<=k. Such a choice exists because k delta/2>0. **Draft46 omits k>=1; that literal requirement is false at k=0 for arbitrary amplitude, since its radius factor equals1.** Choose R0 separately and restore this restriction. The zeroth term is one finite term.

For any fixed K,j, terms k>=max(j,2K+2) have the summable bound2^-k r^s_(K+1). The finitely many terms K<k<max(j,2K+2) use their individual derivative estimate, not the restricted j<=k bound. The first K+1 cutoffs are1 for r>=2R_K. This proves the asserted full symbol remainder, with constants allowed to depend on K and j. Local finiteness proves smoothness, and frequency orthogonality gives the exact coefficient A_k r^s_k for r>=2R_k. Neither assertion establishes transport.

For the nonzero-slope amendment, let h=y chi0(r), chi0 smooth radial,1 near0,0 for r>=R0. Its only source is g2=(r/2)chi0'(r). Near0 the inner Green integral is zero, while the upper integral is (1/2)int chi0'=-1/2. Thus psi_h=-r^2 sin(2theta)/8=-xy/4 exactly there. Outside the support, integration by parts gives int s^3g2 ds=(1/2)int s^4chi0' ds=-2 int s^3chi0 ds; endpoints vanish at0 and infinity. Hence psi_h=-(I/2)r^-2 sin(2theta), I=int s^3chi0. Its velocity is I r^-3(cos3theta,sin3theta). Adding kappa h changes the center slope from0 to kappa and the canonical strain by -kappa/4. The necessary origin equation c=1-ell therefore holds for at most one kappa. Every other nonzero kappa gives an explicit non-profile with all the claimed density asymptotics and finite support on each circle. This confirms the scope without mistaking nonzero slope for the missing PDE.

## First-correction cancellation

At p=1/2, ell=2 and D=1, let Theta=a sin theta+eta sin5theta. The leading source is cos(theta)p Theta-sin(theta)Theta'. Solving -[d_theta^2+(p+1)^2]Psi for its even sine modes gives

    Psi=-(a/7)sin2theta+(eta/5)sin4theta-(eta/15)sin6theta.

The first transport correction is B/D with B=-p Psi' Theta+(p+1)Psi Theta'. Products are evaluated using sin(u)cos(v)=[sin(u+v)+sin(u-v)]/2. The a^2 contribution at sin3theta is -a^2/28. Cross terms from stream frequency2 with density5, and stream frequencies4 and6 with density1, sum to (67/70)a eta. Pure eta^2 terms have frequencies1,9,11 and do not contribute. Thus the reported coefficient is -a^2/28+(67/70)a eta, vanishing at eta=5a/134. The top-frequency nonvanishing theorem is unaffected because the highest leading frequency is5 when eta!=0. This is coefficient algebra, not a construction of an exact profile.

## Other changed passages and scope

The K=11 to K=10 gauge direction follows from K_lambda=lambda^(2/3)K and cubic coefficients multiplied by lambda^-2. Its factor is(11/10)^3; the reverse factor is its reciprocal. The L=2 line-search run has five accepted updates and a failure on its sixth iteration, as independently established in141. Draft46 now states both correctly. The actual date of direct140verification is04:41:32Z, and its Opus hand-review response was independently checked04:44. Timeline review dates are provenance, not proof.

The two external answers were fully read and their arguments rederived. Their logs identify openai.gpt-6-referee, not Claude Opus5.5, and both record unavailable Bedrock credentials for a further Opus consultation. Actual lead Opus5.5 hand reviews are separately recorded. No claimed external code run is adopted as our independent verification. The full changed299-line diff and dependent A.3.66 steps were inspected; this is not a fresh certification of all preceding report sections. Global existence, nonexistence, infinitely many modes on one fixed circle and uniform numerical certification remain OPEN.
