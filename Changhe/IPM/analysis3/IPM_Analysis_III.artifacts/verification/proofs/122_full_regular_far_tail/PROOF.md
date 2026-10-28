# Far-tail integration retaining every regular outer power

## Exact decomposition

Use the actual modal trial and notation of topics117 and120. Let h^r_j(tau)=sum_l A_(j,l) exp(alpha_l tau) retain all ten regular powers of rho/r^3, and let h^m=h-h^r be the exactly matched exponential-polynomial correction. Let P^r,Q^r be the particular Green velocities of these ten powers, excluding both the exterior homogeneous Green solution and the matched correction. Put P^e=P-P^r and Q^e=Q-Q^r.

Define the finite exponential sum

 f^r=L h^r-P^r D h^r+Q^r Theta h^r,

where L=ell D-I, D=3+partial_tau and Theta is the angular derivative. The alpha_0 term of L h^r is identically zero. Consequently f^r is a finite sum

 f^r(tau,theta)=sum_e exp(e tau) S_e(theta),                 (1)

whose largest possible exponent is alpha_1=2k-4. Each S_e is an exactly conforming finite sine polynomial. The scalar term and every product can be collected by their exact rational exponents before any evaluation. Angular division gives S_e=cos(theta)^2 sin(theta)[gamma_e+cos(theta)^2 Q_e(theta)].

The error is exactly

 f-f^r=L h^m-P^r D h^m-P^e D h+Q^r Theta h^m+Q^e Theta h.   (2)

The exterior homogeneous velocity starts at rate -4. The matched density has rate -b_o, with b_o>125. Therefore (2) has a uniform exponential bound B_T exp(a_e s) for t=T+s, s>=0, with

 a_e=alpha_0-4=k-7.

Specifically bound P^r,Q^r at rate k-1, h^m and D h^m at rate -6, P^e,Q^e at rate -4, h and D h at rate alpha_0, and L h^m at rate a_e. Every required bound follows from the directed exponential-polynomial formula(5) of proof 120. The rates satisfy (k-1)+(-6)=(-4)+alpha_0=a_e. The angular product l1 bound then proves (2) quantitatively.

## Exact integration of the retained part

Let G_(e,f)=M H(Q_e,Q_f) and J_(e,f)=gamma_e gamma_f, with H the exact angular bilinear form and M the beta mass of proof 98. Since every e<=alpha_1 and 2alpha_1+27/4<0,

 I_R^r(T)=exp(27T/4) sum_(e,f)
   G_(e,f) exp((e+f)(T-t_+))/[-(e+f+27/4)]                (3)

is the exact remainder tail energy of the retained sum. Replacing G by J gives its axis tail energy. Equation(3) follows by integrating each finite exponential term. The matrix entries can have either sign, but the full sums are nonnegative because they are squared norms.

The error norm is bounded by

 D_R(T)=sqrt(M) C_N B_T exp(27T/8)/sqrt(-(2a_e+27/4)),      (4)

with C_N as in proof 120. For the complete Y norm use sqrt(1+M). The triangle and reverse triangle inequalities give actual tail bounds

 max(0,sqrt(I_R^r)-D_R)^2 <= I_R <= (sqrt(I_R^r)+D_R)^2,    (5)

and the identical formula with I_R^r+I_axis^r and the complete error constant gives the full Y tail. These are finite-radius certificates, not fitted asymptotic rates.

## Verification and scope

The code reconstructs the same exact outer data directly from the read-only original as proof 120. It assembles all ten-by-ten regular nonlinear interactions, groups exact exponents, verifies the angular factors and compares the leading coefficient with the independently computed proof 117 result. It evaluates the finite Gram sums with directed arithmetic. No low angular truncation or quadrature is used.

The certificate applies only to t>=T. It leaves the inner and intermediate radial integral open. It also does not supply an inverse bound or nonlinear smallness theorem.
