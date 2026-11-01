# Independent numerical audit of the smaller four-ninths branches

Status: CONFIRMED for roots1,2,3,4 through72. All four requested roots completed.

## Statement and hypotheses

Let delta=4/9, c=9/5, and f_1=sin(theta)+b_i sin(3theta), where b_i is one of the first four real roots, in increasing order, of the exact compatibility polynomial146. The all-index response bounds164 give a unique tuned pure series by145. Starting from an exact enclosing interval for b_i, the independent Cartesian implementation encloses its density and stream coefficients through72, with the harmonic H72 determined using the obstruction at81.

Successful coefficient overlaps certify consistency with the separate numerical implementation through72. At the selected later orders through306, exact interval norm extraction gives source-bound finite values. Those later coefficients are not independently recomputed by this audit. Neither their root tests nor any fitted constant proves an infinite convergence boundary.

## Complete argument

Refine the isolating rational interval146 by exact sign-preserving bisection. Directed interval arithmetic then encloses the root and every recurrence operation, with no midpoint reset. The first resonant density coordinate is zero because the root solves the first-obstruction polynomial. At every subsequent resonance the harmonic chosen nine orders earlier cancels the obstruction. The interval must contain zero before the known zero coordinate is projected out.

For each current harmonic, run two provisional continuations with its value0 and1. Their difference encloses the affine response. Its interval must exclude zero. Division then encloses the unique harmonic that removes the next obstruction, as proved in145. This procedure also tunes the last retained H72; it does not substitute the particular stream with harmonic zero. Cartesian second derivatives check each Poisson inversion. Each retained source coefficient is compared with the independent enclosure, and the stored harmonic and response values are compared separately. The already certified179 density norms and harmonics provide an additional consistency comparison through72.

For any retained coefficient interval, directed absolute value and summation enclose the angular l1 norm. Directed logarithm and exponential enclose its positive order root. The sum of coefficient radii divided by the sum of absolute midpoints records the source norm uncertainty. If a final resonant source coefficient has its harmonic unset, its stream norm is excluded: the density is already fixed, but that particular stream is not the coefficient of the infinite tuned series. Source hashes, selected exact dyadic records, root intervals, independent norm balls, counts and real runtimes are retained. The full source recurrence beyond72 is outside this certificate.

## Finite least-squares statistics

For each selected fitting window150<=n<=300 or306, let y_n=log(||f_n||_1). Define the finite least-squares coefficients by minimizing sum_n [y_n-alpha*n-beta*log(n)-gamma]^2. The three columns n,log(n),1 are linearly independent on either window: strict concavity of log prevents its values at any three distinct positive n from being affine in n. Thus their Gram matrix is positive definite. Interval summation constructs this matrix and right side, and elimination is used only when every pivot excludes zero. Thus the retained intervals enclose the exact least-squares coefficients of the source norms. The reported finite statistic A_fit=exp(alpha) and its converted radius A_fit^(9/4) are certified evaluations of this particular regression, not bounds on the infinite radius. No asymptotic assumption is justified by solving the finite normal equations. The per-order source log-norm intervals are retained to make the regression independently reproducible.

## Completed root1 audit

At 2026-10-31T13:35:49+00:00, all73368Poisson coefficient checks,8964ordered products,16provisional continuations and eight compatibility projections pass. The independent3072-bit prefix agrees with all5256density and5328stream source coefficients through72, all eight harmonic/response pairs, and179's72norms and seven earlier pairs. Runtime202.99292797595263seconds. The selected archive passes byte-exact hash checks.

On the source density norms, the finite150..300 fit gives A_fit=0.30424143123367474589... and A_fit^(9/4)=0.06874502903922314002.... The150..306 fit gives0.30412594964009048452... and0.06868633213547172697.... The density306 norm root is0.29993424789458599383... with relative norm radius5.2844535916257214e-129. SourceG306has its final harmonic untuned and is excluded. These are finite source-bound statistics only.

## Completed root2 audit

At 2026-10-31T13:39:25+00:00, all73368Poisson checks,8964ordered products,16provisional continuations and eight compatibility projections pass. All5256density and5328stream coefficients agree by interval overlap with the independent source, together with eightH/sigma pairs;179 contributes72norm and sevenpair overlaps. Runtime205.42579611111432seconds. Selected archive hashes pass. The150..300 and150..306 finite fits give A_fit=0.40955976211157979347608... and0.40750456388264526786648..., with converted statistics0.13418806323108426109407... and0.13267774246057546463400.... SourceF306 norm root0.39333984628832650547190..., relative norm radius[2.08271635446360805188469517597e-181 +/- 1.79e-212]. SourceG306is untuned and excluded. These finite statistics do not prove an infinite convergence boundary. V348.

## Completed root3 audit

At 2026-10-31T13:42:10+00:00, all73368Poisson checks,8964ordered products,16provisional continuations and eight compatibility projections pass. All5256density and5328stream coefficients agree by interval overlap with the independent source, together with eightH/sigma pairs;179 contributes72norm and sevenpair overlaps. Runtime202.87344757001847seconds. Selected archive hashes pass. The150..300 and150..306 finite fits give A_fit=1.04470777924941403315877... and1.03068207841274638434171..., with converted statistics1.10341368104140220255048... and1.07036187157980480175320.... SourceF306 norm root0.91203726980961149950584..., relative norm radius[5.37217665659975609514388818976e-178 +/- 2.39e-208]. SourceG306is untuned and excluded. These finite statistics do not prove an infinite convergence boundary. V350.

## Completed root4 audit

At 2026-10-31T13:45:39+00:00, all73368Poisson checks,8964ordered products,16provisional continuations and eight compatibility projections pass. All5256density and5328stream coefficients agree by interval overlap with the independent source, together with eightH/sigma pairs;179 contributes72norm and sevenpair overlaps. Runtime202.0222439370118seconds. Selected archive hashes pass. The150..300 and150..306 finite fits give A_fit=1.72008090512779131294864... and1.71432990654565433839585..., with converted statistics3.38832428192811696439620... and3.36288799877771329352684.... SourceF306 norm root1.75311222019587103889542..., relative norm radius[2.63802789693684276867418979553e-194 +/- 4.14e-224]. SourceG306is untuned and excluded. These finite statistics do not prove an infinite convergence boundary. V351.
