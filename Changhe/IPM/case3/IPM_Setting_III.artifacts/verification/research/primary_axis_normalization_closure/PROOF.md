# Exact axis-amplitude check for three saved primary trials

Written 2026-10-22T12:17:48.872759+00:00, before implementing or evaluating this check. The purpose is to distinguish the radial basis length from the axis reporting length in the closing synthesis. This extends the existing scale audit with direct finite arithmetic; it does not establish transport or convergence.

## Statement

For each unchanged exact coefficient file of N36,N40,N44 in result336, write the finite density with basis length L_b=1 as rho=y w sum_k Re(z^k)P_k(t), w=(1+r²)^(-alpha),t=1-2w,z=(x+iy)²/(1+r²), and P_k=sum_j b_kj T_j. All b_kj and alpha retain their exact imported rational meanings. Assume0<alpha<1/2 and put p=1-2alpha. Then

    a=rho_y(0)=sum_j (-1)^j b_0j,
    K=lim_(y->+infinity) rho(0,y)/y^p=sum_k sum_j (-1)^k b_kj.

Both a and K are finite exact rational functionals of these coefficient data. They are not freely normalizable invariant parameters. If a and K are nonzero with K/a>0, define the reporting length L_axis=(K/a)^(1/(1-p)). This is a separate quantity from the fixed basis length L_b. Their equality requires K=a when L_b=1, and must be measured rather than presumed from the solver constraint.

## Proof

At the origin all k>0 contributions to rho_y vanish because z=O(r²). The k=0 term has w=1,t=-1 and T_j(-1)=(-1)^j. This gives a. On the positive vertical axis z=-y²/(1+y²) approaches-1, w/y^(-2alpha) approaches1 and t approaches1. Since every sum is finite and T_j(1)=1, division by y^p gives K. No exchange of an infinite expansion with a limit is used.

Under the genuine dilation rho_lambda(X)=lambda rho(X/lambda), direct differentiation yields a_lambda=a and the axis limit yields K_lambda=lambda^(1-p)K. Therefore L_axis,lambda=lambda L_axis, provided the same actual exponent p is used. This algebra is valid for these asymptotic trial fields even without exact transport. The theorem that every exact admissible primary profile has p=1/ell and K/a>0 is separate, proved in research/scaling/PROOF.md. For the saved approximate fields p need not equal1/ell exactly, and their scale chart supplies no evidence of exact transport.

To rigorously bound the length defect without evaluating a transcendental power, suppose1<s=1/(1-p)<2 and |K/a-1|<=1/100. For u between1 and K/a, 99/100<=u<=101/100. Since0<s-1<1, u^(s-1)<=max(1,u)<=101/100. Hence the derivative of u^s is at most101/50. The mean-value theorem gives

    |L_axis-1| <= (101/50)|K/a-1|.

All hypotheses and the right-hand side can be checked exactly with Fractions. The resulting interval is a rigorous bound for the reporting length of the supplied finite formula, conditional only on exact source parsing, not an interval for an IPM solution or a numerical parameter uncertainty. Verify the independently summed a equals the already accepted334exact slope. Record K-a,K/a-1,p,ell*p-1 and the length-defect bound. Do not round the source exponent to3/10 or substitute p=1/ell.

All writes remain here. NoJavaScript/TypeScript/Node,servers/listeners/tunnels,RLScience cluster,GPU,Lean/Lake,commits/push/posts/humancontact. This is one short single-thread exact-arithmetic check under10minutes, with actual Opus5.5 review before acceptance.
