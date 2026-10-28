# Lead Note 44 (2026-10-28T11:57Z): cross-read of V176 (strict positive-remainder increment): correct

To the verification work. I read strict_increment/PROOF.md (5f1e2a54...) against ../PROOF.md and checked every step independently.

1. Density. From the definition of Q_R, the angular weight sin(2t)/(2 pi) dt with dr/r is the area density
   sin(2t)/(2 pi r^2), with t = angle from the zero ray, so on the negative lobe at deviation d from its axis the density
   is cos(2d)/(2 pi r^2) on R|sin 2d| <= r <= R. The four positive half-lobes map onto the four negative half-lobes
   exactly once, so this is the full density of Q. Mass 1/pi as stated.
2. Disks. Centers +-(7/18)n, radius 1/9: radii in [5/18, 1/2], |sin d| <= 2/7, cos 2d >= 41/49, and
   (1/2)|sin 2d| = |sin d| cos d <= (2/7)(sqrt45/7) = 6 sqrt5/49 < 5/18 (108^2*5 = 58320 < 60025 = 245^2); |sin 2d| is
   increasing on |d| <= arcsin(2/7) < pi/4, so the bound holds on the whole disk. The disks are disjoint (7/9 > 2/9).
   Density >= (41/49)/(2 pi/4) = 82/(49 pi).
3. Coupling. Reflection in the line through the disk center perpendicular to e1 preserves the uniform measure, so the
   marginals are exact; the displacement is (1 - 2u_1)e1 with |u_1| <= 1/9. Lagrange remainder with
   (t^alpha)'' <= -alpha(1-alpha)(11/9)^(alpha-2) on [7/9, 11/9]; mean of u_1 is 0 and of u_1^2 is eps^2/4, so the mean
   cost is <= 1 - a eps^2/2. Gain 2 c pi eps^2 a eps^2/2 = (82/49)(1/6561) alpha(1-alpha)(11/9)^(alpha-2), and
   49*6561 = 321489. The rest of Q and the atom are translated (cost 1); total mass 1/2. Uniform in the kernel phase.
   Complex inputs: only |f(p)-f(q)| <= [f]|p-q|^alpha is used.

Scope: every D bound of Theorems 3.3, 3.4, 3.5 and 3.6 in the report has the term 2^(1-alpha)A_alpha/alpha + 1/2 with
local radius h/2, so 1/2 -> 1/2 - eta_alpha applies to all of them (including the exterior-circle D values at 1/20 and
1/10), not to G (Theorem 3.2, optimized radius) or the cutoff bounds of Theorem 5.7 (alpha = 1/1000, 1/100).
Float values of eta: 1/5 2.84e-5, 3/10 3.81e-5, 1/2 4.72e-5, 3/4 3.72e-5, 9/10 1.84e-5, 99/100 2.06e-6.

Status of my work: the 2048 x 2048 cross-disk run (unchanged copy of certify_cross_only.py, six exponents 1/5 ... 99/100)
started 11:52:35Z on core 62 (scratch/cross2048/, prelaunch.txt has the hashes); about 20 min. It is my only job.


Verifier capture: parent proof SHA256 5f1e2a54da5ef2186657923bec78db63cd41727fe5bf85d1a40202dea7355a1e. The lead reports a complete independent cross-read and no error. Captured 2026-10-28T12:00:32.675592+00:00.
