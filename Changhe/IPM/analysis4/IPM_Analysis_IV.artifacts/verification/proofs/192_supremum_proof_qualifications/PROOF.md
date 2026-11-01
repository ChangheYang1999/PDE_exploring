# Qualifications in the computation of the tail supremum

Status: PROVED by the elementary argument below. The related source wording is to be corrected; the tail bound in187 remains valid.

## Exact statement

Let m>0, Q>0, K be a nonnegative integer, 0<t<1 and d be a nonnegative integer. Define a_k=(m+Qk)^(d-1)t^k for k>=K. For d=0 and d=1 the maximum is a_K. For d>=2 it occurs at the least k>=K for which t(1+Q/(m+Qk))^(d-1)<=1. Equality gives two adjacent maximizers. The maximum is rational when m,Q,t are rational. It need not be rational for arbitrary real t.

## Complete proof

The ratio a_(k+1)/a_k is t(1+Q/(m+Qk))^(d-1). For d=0 this ratio is less than t<1 and increases toward t; hence the sequence itself strictly decreases. For d=1 the ratio equals t<1. For d>=2 the ratio strictly decreases to t<1. Thus it eventually lies below one, and the sequence increases exactly before the first index where the ratio is at most one. This proves the claimed maximum rule, including the possible adjacent tie. Rational inputs and an integer maximizing index give a rational value by finite rational arithmetic.

For a concrete counterexample to decreasing ratios at d=0, take m=10,Q=5,t=1/2,K=0. The first two ratios are 1/3 and3/8, with 3/8>1/3. At d=1 they are both1/2. To disprove unqualified rationality of the maximum, take m=10,Q=5,K=1,d=0,t=sqrt(2)/2. Then the maximum is sqrt(2)/30, which is irrational: otherwise multiplying by30 would make sqrt(2) rational, contradicting the elementary parity proof from an assumed reduced fraction for sqrt(2).

## Source correction and scope

The theory part's version35, section12.6 remark6, says that the displayed ratios decrease and that the maximum is an exactly computable rational without restricting d or t. The first statement needs the split above, and the second needs rational inputs. Topic187 already separates d=0,1, but its computational paragraph should also keep rationality conditional explicitly. No numerical certificate is affected: all retained examples use rational input, and the correct maximum algorithm already separates d=0,1. No convergence theorem is withdrawn.
