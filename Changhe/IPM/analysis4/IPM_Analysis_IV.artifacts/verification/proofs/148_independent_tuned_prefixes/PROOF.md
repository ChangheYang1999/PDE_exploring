# Independent Cartesian prefixes for tuned rational profiles

Status: finite Q4 root-6 prefix CONFIRMED in V290. Every conclusion is a finite certificate unless a previously proved convergence theorem is explicitly invoked.

## Exact statement and hypotheses

Let delta=2h/Q with positive coprime integers h,Q and Q>2h. Set c=Q/(Q-2h), p_n=1-n delta, and P_n=p_n+1. Let b be an isolated exact real root of a specified rational obstruction polynomial, and take f_1=sin(theta)+b sin(3theta). Assume the first obstruction vanishes and every response needed in the computed prefix is nonzero. When used, these assumptions come from the exact results in 119, 142 or 146; a small numerical obstruction alone does not establish them.

The purpose is to enclose the unique tuned coefficients through a finite order N by a Cartesian implementation, independently of the source Fourier convolution and its explicit response recurrence. Comparison of two valid enclosures is a consistency test; it is not the reason either enclosure is valid.

## Cartesian identities

Encode a real sine polynomial by sum_m a_m(z^m-z^(-m))/2, so its physical value on the unit circle is minus i times the encoding. For radial degree a define

    X_a z^m = ((a+m)z^(m-1)+(a-m)z^(m+1))/2,
    Y_a z^m = ((a+m)z^(m-1)-(a-m)z^(m+1))/2.

Physical differentiation in x and y is represented by X and iY, respectively. Consequently the source equations are

    (-XX+YY)g_n = X f_n,
    lambda_n f_n = sum_(i+j=n)(Xg_i Yf_j-Yg_i Xf_j),
    lambda_n = delta(n-1)/(1-delta).

The first identity also follows coefficientwise by dividing Xf_n at angular mode m by m^2-P_n^2. Nonresonant denominators are exact nonzero rationals. At a resonance the corresponding entire output is deleted from this particular inverse. A free coefficient H_n is then added at positive frequency 2hn/Q-2. The zero angular sine mode is always absent.

## Tuning by two provisional continuations

At a resonant order n, keep all preceding coefficients fixed. Compute provisional density coefficients through n+Q twice: once with H_n=0 and once with H_n=1. No intermediate order is resonant. A coefficient depending on H_n first occurs in g_n, and a density coefficient depending on it first occurs at n+1. Thus a product containing two H_n-dependent factors first has total order 2n+1. Since n>=Q, this is strictly larger than n+Q. Every computed provisional density coefficient is therefore affine in H_n.

Let R be the next obstruction in the H_n=0 continuation, and let S be the difference between the next obstructions in the H_n=1 and H_n=0 continuations. Then S is exactly the response sigma_k. If its interval excludes zero, H_n=-R/S encloses the unique compatible harmonic. The main recurrence then proceeds again from the fixed lower coefficients with this H_n. It does not copy the source's affine block correction.

At each resonance, an independently proved exact compatibility identity permits projection of the obstruction coefficient to zero. The discarded interval must contain zero. The same rule applies to symmetry and support projections: each discarded component must enclose zero, and the projected identity must follow from the exact recurrence. Hence projection does not discard the exact solution.

## Interval induction and comparison

Start with rational bisection of a previously certified isolating interval. Every midpoint sign is evaluated exactly in rational arithmetic. The resulting interval still contains the same root. Its interval representation is outward rounded. Induction using interval addition, multiplication, exact rational division, and division by a response interval separated from zero encloses every coefficient computed above. The affine argument supplies the exact tuning relation used in this induction.

A retained source prefix is decoded from its exact packed dyadic midpoint and radius. Its input root is separately checked to contain the independently refined root interval. Every available coefficient and harmonic is compared by interval intersection. The two-continuation response enclosures are also compared against the previously certified exact response polynomials, including the folded low-carrier cases. Norms and root tests refer only to the exact finite prefix and have no asymptotic interpretation.

## Dependencies, evidence and scope

The Cartesian identities are independently derived in 01. The resonance and affine argument are in 119, 130 and 144. Root isolation and nonvanishing are supplied by the relevant exact algebraic certificates. Source files, selected prefixes, checksums, arithmetic precision, comparison counts and actual runtimes are retained in clearly named subfolders. No assertion about an improved infinite convergence radius follows from these finite computations.

## Completed finite certificate

At 2026-10-31T11:21:01Z, the Q4 sixth real root was independently computed through order40 at1536-bit precision. All1640 density and1680 stream source coefficients overlap; all21808 Cartesian Poisson coefficient checks,22832 support checks,11198 symmetry checks and9 compatibility projections pass. There are2616 ordered nonlinear products and18 provisional continuations. All9 response enclosures overlap their exact symbolic polynomial evaluations. The main computation took10.889230161439627 actual seconds. Its evidence is verification/Q4_root6_20261031T111750Z/checks.json and verification/response_comparisons.json. At order40, the density norm root is1.7957388298142385 and the stream norm root is1.7468159058382468. These values describe this finite prefix only.
