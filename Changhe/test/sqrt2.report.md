# Result

$\sqrt{2}$ is irrational: there are no integers $p, q$ with $q \neq 0$ and $(p/q)^2 = 2$.

## Proof

Suppose $\sqrt{2} = p/q$ with $p, q$ positive integers. Among all such representations choose one with $q$ as small as possible. Squaring gives

$$p^2 = 2q^2 .$$

So $p^2$ is even. The square of an odd number is odd, since $(2k+1)^2 = 2(2k^2+2k)+1$, so $p$ is even: $p = 2r$ with $r$ a positive integer. Substituting, $4r^2 = 2q^2$, that is,

$$q^2 = 2r^2 .$$

By the same argument $q$ is even, $q = 2s$, and then $r^2 = 2s^2$, so $\sqrt{2} = r/s$ with $0 < s = q/2 < q$. This contradicts the minimality of $q$. Hence no such $p, q$ exist and $\sqrt{2}$ is irrational. $\blacksquare$

The same argument, phrased with $\gcd(p,q) = 1$ instead of minimality, reaches the contradiction one step earlier: both $p$ and $q$ are even, so $2$ divides $\gcd(p,q)$.

## Method

The proof above is the classical parity (infinite descent) argument. It was also checked mechanically in Lean 4 (v4.35.0) with Mathlib. The descent step, stated over the natural numbers, and Mathlib's own theorem both compile without errors or warnings:

```lean
import Mathlib

/-- Mathlib's statement: `√2` is irrational. -/
example : Irrational (Real.sqrt 2) := irrational_sqrt_two

/-- The textbook descent: `a ^ 2 = 2 * b ^ 2` in the naturals forces `b = 0`. -/
theorem sq_eq_two_mul_sq (b : ℕ) : ∀ a : ℕ, a ^ 2 = 2 * b ^ 2 → b = 0 := by
  induction b using Nat.strong_induction_on with
  | _ b ih =>
    intro a h
    obtain ⟨c, rfl⟩ : 2 ∣ a := Nat.prime_two.dvd_of_dvd_pow ⟨b ^ 2, h⟩
    have hb : b ^ 2 = 2 * c ^ 2 := by nlinarith
    obtain ⟨d, rfl⟩ : 2 ∣ b := Nat.prime_two.dvd_of_dvd_pow ⟨c ^ 2, hb⟩
    have hc : c ^ 2 = 2 * d ^ 2 := by nlinarith
    by_contra hne
    have := ih d (by omega) c hc
    omega
```

`sq_eq_two_mul_sq` is exactly the descent in the proof: from $a^2 = 2b^2$ it extracts $a = 2c$, then $b = 2d$, then $c^2 = 2d^2$ with $d < b$, and strong induction on $b$ finishes.

## Findings

The only arithmetic fact needed is that an odd number has an odd square, equivalently that $2$ is prime, so $2 \mid p^2$ implies $2 \mid p$. The same proof shows $\sqrt{n}$ is irrational for every prime $n$, replacing parity with divisibility by $n$.

## Limitations / Open Questions

None. This prompt was a test of the prompt/report workflow.
