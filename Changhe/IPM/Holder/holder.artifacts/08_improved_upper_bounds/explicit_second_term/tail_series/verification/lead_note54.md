## 2026-10-28T13:44Z  Note 54: cross-reads V217, V216, V218 (and V211): all CORRECT
Checks: scratch/crossread_v216_v218/check.py and check.out (arb, 256 bits; seconds).
1. V217 tail_series (sha b4be8e86...): CORRECT. I rederived the expansion w/[pi(w^2-1/4)^2] = (1/pi) sum (n+1)4^-n w^(-2n-3)
   from 1/(w-p)^2-1/(w+p)^2 = 4pw/(w^2-p^2)^2 with p=1/2, the angular absolute integral 4 per nonzero frequency, the antipodal
   half-variation factor, the radial integral alpha/[(2n+1-alpha)(2n+1)], the identity sum_{n>=1}(n+1)4^-n/(2n(2n+1)) = tau
   (checked to 75 digits), the log-derivative of f_alpha and the geometric tail (4/3)4^-N f_alpha(N), and the monotonicity of each
   summand in alpha for the envelope. Effect (T_old - T_exact): 1.9036e-5 at alpha=1/1000, 9.519e-5 at 1/200, 1.9038e-4 at 1/100;
   envelope coefficient gain 2^(1+eps)(1/(1-eps)+tau-S(eps))/pi = 0.0190381 at eps=1/100, so K_C about 2.4945 -> 2.4755 and K_D
   about 2.7440 -> 2.7250 (before re-optimizing rho). Finite: C_1/1000 about 637.02456, D_1/1000 about 637.42714, D_1/100 about
   64.49384; C_1/100 from J_C stays above Theorem 3.8 (64.08816). Please certify these when convenient; I will integrate them in v33.
2. V216 all_even_moments (sha 24fd5246...): CORRECT. Normalization: density times area t dt dtheta/[2pi(c+t)^2], v=2st cos(theta),
   int cos^2n = 2pi binom(2n,n)/4^n, two disks, -binom(alpha,2n) = alpha prod_{k<2n}(k-alpha)/(2n)!, so g_n =
   2alpha prod(k-alpha)/(n!)^2 s^2n B_{2n+1}; the B_m formula reproduces 2B_3(3/4) = J* and B_5(3/4)/2 = K* exactly (balls contain
   0). Tail ratio (2n-alpha)(2n+1-alpha)/(n+1)^2 < 4 and B_{m+2} <= a^2 B_m: correct. Retained cutoff: 1/(c+t)^2 >= 1 >
   rho^2/(1-rho)^2, and a radial sub-density of the retained translation edges may be re-coupled by reflection: correct; the
   subtracted moments rho^2 a^(m+1)/((m+1)(1-rho)^2) reproduce the accepted 1/512 and 1/49152 terms. The sixth-order term is
   negligible: g_3 = 2.59e-8 at alpha=1/2, s=1/2 (B_7(3/4) = 2.02207e-6, checked by quadrature).
3. V218 optimal_axis_disks: CORRECT. I rederived P_c(s) from the boundary point (2s cos^2, 2s^2 cos), H'(s) = -(1-2s^2)p(s)/v^2
   with 8sv+(1-2s^2)v' = 2p(s), p' = 2+8(s-1/2)^2(s+1), p(1/3) = 2/81, H(1/3) = 49/66, the cone condition a/c < 1/sqrt2, and the
   density condition a <= c/2. Numerically sigma = 0.3226646558, c* = 0.7430325154, a* = 0.2569674846; grid minimum of P_{c*} is
   +9.8e-10 (tangency) and P_{c*-1e-6}(sigma) < 0. Moments at c*: 2B_3 = 0.0024380614 (against 0.0021769945 at c=3/4) and
   B_5/2 = 2.59468e-5 (against 2.19518e-5), so the Theorem 3.9 savings grow by about 12 to 18 percent (about 1.7e-5 at alpha=1/2).
   V211 (c = 1487/2000 > c*) is then a special case and is CORRECT; I suggest using V218 only.

