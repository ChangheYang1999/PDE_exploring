# One-sided expansion gives a smaller orbit-weight Lipschitz constant

Status: CONFIRMED independent audit of the T2 theory worker the review of T4-170 Remark R1. This is an analytic estimate, with no certified candidate value of the new coefficient.

## Statement

Let V:R2->R2 be globally Lipschitz, V(0)=0, with global flow Phi_t. Suppose for some real mu,

    (V(X)-V(Y)).(X-Y) >= mu |X-Y|^2 for all X,Y.

Let theta be globally Lipschitz with constant L_theta. For T>=0 and real lambda define

    psi(X)=max_(0<=tau<=T) integral_(-tau)^0 (theta(Phi_t X)-lambda) dt.

Then psi is globally Lipschitz and

    Lip(psi)<=L_theta Q_mu(T),
    Q_mu(T)=(1-exp(-mu T))/mu if mu!=0, and Q_0(T)=T.

For mu>0 this is at most L_theta/mu, independently of T. The same bound holds for the supremum over every tau>=0 whenever that supremum is finite at every X. Under the remaining hypotheses of T4-170, the compact orbit weight is exactly such a finite-window maximum, so its other conclusions remain unchanged with this improved bound. Positive mu also supplies the radial expansion constant m=mu.

## Proof

For x(s)=Phi_(-s)X and y(s)=Phi_(-s)Y, differentiate their squared distance:

    d/ds |x-y|^2=-2(x-y).(V(x)-V(y))<=-2mu|x-y|^2.

Gronwall gives |x(s)-y(s)|<=exp(-mu s)|X-Y|. For every fixed tau<=T the corresponding integral therefore differs between X and Y by at most

    L_theta |X-Y| integral_0^tau exp(-mu s) ds
       <= L_theta Q_mu(T)|X-Y|.

The maximum of functions with a common Lipschitz bound has the same bound, which proves the claim. For an infinite time horizon and mu>0, the bound is uniform in tau, so it passes to a finite-valued supremum. Setting Y=0 in the one-sided hypothesis gives V(X).X>=mu|X|^2.

For a C1 vector field, Sym DV>=mu I everywhere implies the one-sided condition by integration along the segment joining X and Y. For a globally Lipschitz field whose symmetric derivative has this lower bound almost everywhere, mollify V: convolution preserves the distributional matrix inequality, so every smooth mollification satisfies the segment inequality. Uniform convergence on compact sets passes that inequality to V. This avoids applying an almost-everywhere derivative assertion along an exceptional fixed segment.

If T4-170 gives support in r1<=|X|<=R, then ||grad psi||_2<=L_theta Q_mu(T) sqrt(pi(R^2-r1^2)). The smaller support radius accepted in T4-180 can be used in the same formula. This does not itself bound ||psi||_2 unless the amplitude or orbit budget has also been bounded.

## Scope

This verifies the proposed R1 sharpening. For the IPM candidates, mu=inf lambda_min(Sym DV) must be certified over the whole plane before it is used. Positivity at the origin and the positive limit cI at infinity do not prove positivity on the intermediate region. No such intermediate-region certificate is supplied here.
