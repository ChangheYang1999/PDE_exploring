# P228: finite horizontal polynomial temperature excluded

Published 2026-10-21T23:47:48.391625+00:00. CONFIRMED: under beta>0, C1 W, div W=2beta, W=betaX+o(|X|), and temperature transport, an exact polynomial Theta=sum_0^N f_j(y)x^j with one fixed finite N has no positive-degree terms. With the B2 axis condition Theta(0,y)=0 it vanishes identically. No vorticity equation or inverse is needed. General polynomial growth is not the same hypothesis and remains outside this result.

Method: the top coefficient f cannot have a critical point where nonzero. Temperature transport forces W2(x,y) to converge horizontally to g=-[(N-1)beta+2]f/f'. Integrating divergence on long rectangles gives g=beta y+d. The resulting negative-power coefficient cannot vanish continuously at a finite component endpoint or extend over the zero of beta y+d.

Independent controls: 49 PASS, 2026-10-21T23:45:26.628737+00:00 to 2026-10-21T23:45:27.700944+00:00, 1.072227 seconds. They include finite-degree fixtures, flux factors, both sign branches and counterexamples when hypotheses are removed. Actual Opus4465.5 confirmed in48.197985s. The full informal proof supplies the arbitrary-degree and global reasoning; finite controls are not a proof by sampling.
