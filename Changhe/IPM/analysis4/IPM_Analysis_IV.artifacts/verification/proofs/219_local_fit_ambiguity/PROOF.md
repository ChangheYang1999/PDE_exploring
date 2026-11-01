# Why the two multiplier fits are close on a short order window

Status: PROVED. The directed specialization is verified in V465; independent theory-part review and admission are recorded in V472.

## Statement

Let a,b be positive real numbers with a<b, n0=(a+b)/2 and h=(b-a)/(a+b)<1. Let alpha,beta be real. On a<=n<=b define

    f(n)=alpha+beta log10(n),
    g(n)=alpha+beta log10(n0)+(beta/ln(10))(1-n0/n).

The function g is an inverse-order model c0+c1/n that agrees with f in value and first derivative at n0. Uniformly on this window,

    |f(n)-g(n)| <= |beta| h^2/[2 ln(10)(1-h)^2].

Consequently, for any finite set of sample orders in the window and any data values there, the root-mean-square residuals of these two specified models differ by no more than the same upper bound. In particular, the best inverse-order least-squares fit has residual no greater than the residual of f plus that bound.

For the orders348 through370, n0=359 and h=11/359. If |beta|<=0.557, the uniform upper bound is less than0.000125 in log10 units. The corresponding tangent inverse coefficient is c1=-359 beta/ln(10). The numerical specialization uses only a directed elementary logarithm and the already verified fitted beta interval from215.

## Proof

Set x=(n-n0)/n0. Then |x|<=h and direct subtraction gives

    f(n)-g(n)=(beta/ln(10))[ln(1+x)-x/(1+x)].

The bracket vanishes at zero and has derivative x/(1+x)^2. Its absolute value is therefore bounded by the integral of |t|/(1-h)^2 between zero and x, which is x^2/[2(1-h)^2]. This proves the uniform bound. The matching value follows by setting n=n0; matching derivatives follows from f'(n0)=beta/[n0 ln(10)]=g'(n0).

For samples n_j and data d_j, apply the reverse triangle inequality for the Euclidean norm to the residual vectors (f(n_j)-d_j) and (g(n_j)-d_j). Division by the square root of the sample count bounds the difference of their root-mean-square residuals by the uniform distance between the models. Minimization over all inverse-order models can only decrease its residual. This proves the stated least-squares consequence.

The numerical bound for the specified rational beta upper bound, n0 and h is evaluated with directed arithmetic in the accompanying script. No statistical noise model is assumed.

## Interpretation and scope

The full-precision fits in215 have root-mean-square residuals near0.0023. A difference below0.000125 between the two tangent model classes is much smaller than those residuals. Their similar quality on this window is therefore expected from the local geometry of the functions and supplies weak discrimination between their very different infinite-order consequences.

This result does not identify the true coefficient growth, prove either asymptotic model, or assert that a larger finite window will settle an infinite-order question. The source data themselves remain conditional on the order329 midpoint reset.
