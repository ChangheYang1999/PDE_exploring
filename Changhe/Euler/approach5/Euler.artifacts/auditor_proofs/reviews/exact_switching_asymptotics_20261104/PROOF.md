# Exact asymptotics of the logarithmic switching clock

## 1. Statement, notation and dependencies

Fix a real number a>1/4. Put ell=pi/4 and L=2+3ell. Let h be a smooth nondecreasing real function, zero on s<=1 and pi/2 on s>=1+3ell, with 0<=h'<=1. Assume that h'=1 on [1+ell,1+2ell], where h runs from pi/8 to 3pi/8. These hypotheses hold for the angle function in the previously confirmed LIT352 construction.

For t0>=1, let s be the solution of

    s'(t)=1/2+a/t^2-sin(h(s(t)))cos(h(s(t))),  s(t0)=0.

Let T(t0) be the first time s=L. Define b=sqrt(a-1/4)>0 and Lambda=pi/b. Then T(t0) is finite for every t0>=1. There are explicit constants C,t*>0, depending only on a and L, such that

    |log(T(t0)/t0)-Lambda| <= C/t0,  t0>=t*.

In particular T(t0)/t0 tends to exp(Lambda). For t1=1 and t_(n+1)=T(t_n), there is a finite positive constant Cstar, depending on a and h, such that

    t_n exp(-n Lambda) -> Cstar.

For t in [t_n,t_(n+1)) set N(t)=n. Let F(1)=0 and F'(t)=N(t)+sin^2(h(s_n(t))), where s_n starts at t_n. Then

    N(t)=log(t)/Lambda+O(1),
    F(t)=(t log(t)-t)/Lambda+O(t).

All asymptotic statements fix a>1/4. There is no uniform estimate as a decreases to 1/4. The only general analytic input for the clock is the elementary global existence and uniqueness theorem for a Lipschitz ordinary differential equation. The vector-norm consequence in Section 6 additionally uses the already confirmed LIT352 construction. The prior two-sided growth theorem A2969 is not needed as a premise.

## 2. Global solution and finite entry and exit

Since 0<=h<=pi/2, the speed is between a/t^2 and 1/2+a for t>=1. Its derivative with respect to s is -cos(2h(s))h'(s), whose absolute value is at most one. Thus the solution exists for every finite future time, is strictly increasing, and cannot blow up in finite time.

Set delta=sin^2(pi/8)>0, D=L/delta and k=tan(pi/8)>0. Before s reaches 1+ell, its angle phi=h(s)-pi/4 belongs to [-pi/4,-pi/8], and

    s'=sin^2(phi)+a/t^2 >= delta.

Consequently the entry time S at s=1+ell is finite and S-t0<=D. The same lower bound applies after s=1+2ell until s=L, so once the central exit time E is proved finite, T-E<=D.

In the central interval h'=1, hence phi'=sin^2(phi)+a/t^2 exactly. Set y=tan(phi), w=t y and x=log(t). All changes of variables are nonsingular for |phi|<=pi/8. Direct differentiation gives

    y'=y^2+(a/t^2)(1+y^2),
    dw/dx=w^2+w+a+(a/t^2)w^2.

Let P(w)=w^2+w+a=(w+1/2)^2+b^2. It is strictly positive. For the phase primitive

    H(w)=integral_0^w dv/P(v)
         =[arctan((w+1/2)/b)-arctan(1/(2b))]/b,

its total range has length pi/b=Lambda, and along the trajectory dH/dx>=1. If the trajectory remained central for a logarithmic interval longer than Lambda, this derivative bound would contradict the finite range of H. The global solution is continuous, so it must exit by time S exp(Lambda). Strict increase forbids a lower exit. Therefore E is finite, E<=S exp(Lambda), and the final outer interval reaches T in at most D more units of time. No asymptotic assumption or sampled passage time is used to prove finite exit.

## 3. Exact phase error and the two finite endpoints

The elementary estimate

    w^2 <= 2(w+1/2)^2+1/2 <= M P(w),
    M=2+1/(2b^2),

implies, throughout the central passage,

    1 <= dH/dx <= 1+aM/t0^2.

At entry w=-kS; at exit w=kE. With J=log(E/S), integration gives

    J <= I <= (1+aM/t0^2)J,
    I=integral_(-kS)^(kE) dv/P(v),  0<J<=Lambda.

The truncated integral differs from the whole real-line integral by two positive tails. When |v|>=2, P(v)>=v^2-|v|>=v^2/2. Hence, for t0>=2/k,

    0<=Lambda-I <= 2/(kS)+2/(kE) <= 4/(k t0).

It follows that

    0<=Lambda-J=(Lambda-I)+(I-J)
      <=4/(k t0)+aM Lambda/t0^2.

This retains the positive tangent correction. Dropping that term as an equality would not justify the remainder estimate.

The outer intervals contribute the nonnegative logarithmic time

    R=log(S/t0)+log(T/E)
      <=(S-t0)/t0+(T-E)/E <=2D/t0.

Since log(T/t0)=J+R, a valid choice is

    t*=max(1,2/k),  C=4/k+aM Lambda+2D.

For these constants, |log(T/t0)-Lambda|<=C/t0. This estimate controls both the finite phase endpoints and the outer intervals. Exponentiating proves the limit of T(t0)/t0; every constant is finite for the fixed positive b.

## 4. Summability and the positive prefactor

The global speed upper bound gives T(t0)-t0>=d, where d=L/(1/2+a)>0. Thus t_n>=1+(n-1)d tends to infinity. Define epsilon_n=log(t_(n+1)/t_n)-Lambda for every n. These numbers are finite because all passage times are finite.

For sufficiently large n the previous section gives |epsilon_n|<=C/t_n. Choose n0 so large that this upper bound is at most Lambda/2. Then

    t_(n+1)>=exp(Lambda/2)t_n,  n>=n0.

Therefore the series of reciprocals 1/t_n converges geometrically in the tail, and sum_n |epsilon_n| is finite, including its finite prefix. Telescoping, with t1=1, yields

    log(t_n)-n Lambda=-Lambda+sum_(j=1)^(n-1)epsilon_j.

The right side tends to a finite real number beta. Thus Cstar=exp(beta) is strictly positive and finite, and t_n exp(-n Lambda) tends to Cstar. In particular log(t_n)=n Lambda+O(1).

For t_n<=t<t_(n+1), the last relation at the two endpoints traps log(t)-n Lambda in a bounded interval. Consequently N(t)=log(t)/Lambda+O(1), uniformly between joins. The convention t1=1 changes beta, not Lambda.

## 5. The smooth envelope and its leading term

On the terminal plateau of passage n, h=pi/2 and F'=n+1. On the initial plateau of passage n+1, h=0 and F'=n+1 as well. Each is constant on an interval adjacent to the join, so the assembled F' is smooth there. Away from joins smoothness follows from the ODE and h. This is the same envelope used by LIT352.

Since 0<=sin^2(h)<=1, Section 4 gives a uniformly bounded error in

    F'(t)=log(t)/Lambda+O(1)

for all sufficiently large t. Integrating and absorbing the finite initial interval proves

    F(t)=(t log(t)-t)/Lambda+O(t).

The error is only asserted at this order. No convergence of the bounded oscillation N(t)-log(t)/Lambda is required or claimed.

## 6. Exact vector-norm consequence and scope

For the LIT352 two-component vector take a=2A with A>1/8, let r=|z| and t=log(1/r). That construction has the exact identity |u(z)|=exp(-F(t)): the two angular factors have unit modulus and the squared amplitudes sum to cos^2(theta)+sin^2(theta)=1. Thus

    [-log|u(r exp(i vartheta))|]/[log(1/r) log log(1/r)]
       =F(t)/(t log t) -> 1/Lambda=sqrt(2A-1/4)/pi.

The quotient is independent of vartheta for each r, so convergence is uniform in the angle. Smooth extension at zero, infinite-order vanishing and the full partial_bar bound continue to depend on the confirmed construction; a norm asymptotic alone would not prove them.

All six submitted LIT355 sections, its 36 manual checks in the team records and its verification plan have been read. The proposed proof resolves the exact switching ratio previously left heuristic by the coordinator. The completed comparison is recorded in Section 7. Actual provider execution is independently unattested. No numerical experiment or formal build was needed. This is a clock theorem and a norm consequence for a vector example. It provides no scalar counterexample, no Euler coefficient estimate, no higher-dimensional sharpness result and no decaying Euler profile.


## 7. Completed independent comparison and diagnostic limits

The existing configured model Theory Agent C  comparison dated 2026-11-04T05:45:38Z was read in full, including all six analytical items, both optional remarks and the disclosure of diagnostic failures. It compares the submitted source fb7be0e1935447bafe5f38f5ce96fd934d9d634dc18ea3fdf21f67623f56db40 with the six-section independent reconstruction e9c997d00c77cce27e88c42ad789d922db36788f8a2fb1a85ff6505dfb1e595b. Its derivations agree with Sections 1-6: the tangent correction has the positive sign, both phase tails are retained, finite exit precedes the asymptotic argument, and summability gives a strictly positive prefactor with the stated indexing. The term -t/Lambda is itself O(t); retaining it records the primitive and does not assert a second-order asymptotic.

The complete retained diagnostic script and log were also read, without rerunning them. They contain 37 passing checks: 13 symbolic identities, one exact check over eight rational parameter samples, four negative controls and 19 numerical samples. One negative control is an exact rational counterexample to the estimate with M=2. The other three compare numerical passage times with the incorrect rate pi/sqrt(a). The 19 samples use a trapezoidal angle table and floating-point ODE integration; no interval enclosure is supplied. Thus these computations neither prove the universal error estimate nor certify a next asymptotic coefficient, positivity of the remainder for every start time, or numerical accuracy at arbitrarily large times.

There is a small literal qualification to the comparison's statement that the iterated times remain below 10^6. The script tests the current starting time against that cap and then appends the next endpoint. The last returned endpoint may exceed 10^6. The comparison discloses that an earlier run failed three checks and its log was overwritten, and describes changes to the negative-control start time, iteration cap and prefactor test. Those historical failure counts and values cannot be independently verified from the retained log. The retained run's 37 passing checks and its script are inspectable; no inference in Sections 1-6 depends on either run.

The general theorem rests on the analytical proof. The comparison and diagnostic records are retained in the team records, in the team records and in the team records, with capture hashes in the team records. Actual provider execution remains independently unattested. No new model client, agent, mathematical computation or formal build was launched for this completed comparison.
