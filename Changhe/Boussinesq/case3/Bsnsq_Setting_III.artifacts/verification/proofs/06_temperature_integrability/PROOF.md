# A single finite temperature L^p integral is impossible

Status: proved informal result. This is a restricted exclusion, not a premise imposed on the prompt.

Let beta>0, U be C^1 and divergence free on the whole plane, and U(X)=o(|X|) uniformly at infinity. Let Theta be C^1 and solve W.grad Theta=(beta-2)Theta with W=beta X+U-U(0). If integral |Theta|^p is finite for any 0<p<infinity, then Theta=0. If beta>2, bounded Theta also forces Theta=0.

The complete flow phi_t exists by the linear growth of W. Temperature transport and the flow Jacobian give

    Theta(phi_t X)=exp((beta-2)t)Theta(X),
    det D phi_t=exp(2 beta t).

For I=integral |Theta|^p, change variables by the global diffeomorphism phi_t. It gives

    I=exp([p(beta-2)+2 beta]t) I.

If 0<I<infinity, its exponent must vanish, so beta=2p/(p+2)<2. But for beta<2 every backward orbit remains in a compact ball while its nonzero temperature would grow as exp((2-beta)t). This contradicts continuity. Hence I=0, and continuity gives Theta=0. The argument covers p<1 without differentiating |Theta|^p.

For bounded Theta and beta>2, its value on every forward orbit would grow as exp((beta-2)t) unless it were zero. This proves the final assertion. At beta=2 boundedness is automatic under sublinear velocity and does not give an exclusion.

Dependencies: the complete flow and compact backward trapping proved in `../01_transport/PROOF.md`, and the change-of-variables formula. No decay of derivatives or inverse convention is required. There is no claim that the prompt requires finite L^p temperature.
