# Ordering two rigorous angular-prefix upper bounds

Written UTC 2026-10-29T16:22:34.334004+00:00 before the checker. This checks a single algebraic comparison in the work-in-progress T2 review of T4-474. It does not reject that theorem or a completed review.

Let F be the real S1 source of T4-474, locally integrable on R2 with rF in L2. Write q_n=pi integral r^3 f_n^2 dr, S=sum q_n, and fix an odd positive N. Suppose every positive odd n<N is included and exact rational endpoints satisfy 0<=L_n<=q_n<=U_n and S<=V. Define

 P=V/N^2+sum_(n<N)(1/n^2-1/N^2)U_n,
 Q=sum_(n<N)U_n/n^2+(V-sum_(n<N)L_n)/N^2.

Both bound the complete Hardy quantity M2=sum q_n/n^2 from above. The first follows from positivity of all included coefficients and q_n/n^2<=q_n/N^2 for omitted modes; the second separately bounds the included energy and the complete omitted energy S-sum q_n. Moreover

 Q-P=sum_(n<N)(U_n-L_n)/N^2>=0.

This is immediate by cancellation of V and of the sum U_n/n^2. If at least one interval has positive width then Q>P strictly. Thus the positive-coefficient form P is the smaller upper; a statement P-Q=sum(U_n-L_n)/N^2 is false. With exact degenerate intervals they agree. For example N=3,V=2,L_1=1/2,U_1=1 gives P=10/9,Q=7/6 and Q-P=1/18. A nonnegative omitted-energy upper follows from valid premises and is separately checked numerically.

For candidate016 use exactly T4-476's frozen endpoints at n=1,3,5,7, N=9, and V equal to the square of the accepted full rF upper. T4-476 explicitly proves the correct direction in its informal argument. Its stored M2_upper_exact uses the positive-coefficient form P, not the safe split form Q. The peer draft also misidentifies that output field. Recompute P and Q from those exact JSON inputs and verify Q>P, Q-P=sum widths/81, and both P and Q preserve the already accepted strict H and E2 upper displays after subtraction of the accepted cross floor. Every conclusion retains the original moment-enclosure and whole-field binding premises. No candidate integral or copied peer script will be executed.

The inspected T2 draft code currently asserts the reversed inequality in its part G. Record the exact source hash and time; the inspection also verifies the stored output definition against the original476 checker. its existing 27-check result is from the earlier A-F script, so it cannot be treated as a successful run of the newer part G. The general analytic T4-474 review remains pending. A later repair is a new source object, not evidence that the old expression was correct.
