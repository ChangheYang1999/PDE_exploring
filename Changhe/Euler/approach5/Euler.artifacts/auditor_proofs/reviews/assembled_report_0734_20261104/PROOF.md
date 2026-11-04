# Audit of report pin 7fe98679

## 1. Exact objects and scope

The current report has SHA256
`7fe98679351cf7a1c0be27adb731cae58c697f37679e7a8a214dc0b0ff91b294`,
7318 lines and 1138415 bytes. The last approved report is
`373917244ebdfb6698e63b7b9648b4528df16192d47a9d45fb46146da69946b3`,
approved in A3039 at the verdict cutoff A3032. Both complete byte strings,
the intervening pin 95d4f412, the two author diffs, and an independently
generated direct diff are retained in the team records. Every line of the
424-line direct diff was read. Changed statements were compared with the
independent proofs behind A3033-A3062 and their surrounding report text.
This is not a new collective audit of the historical appendices.

The profile equation is

    (1-c) U + (((cI-omega J)y + U).grad) U + omega J U + grad P = 0,
    div U = 0,

where J(x1,x2,x3)=(-x2,x1,0). Write E(R)=integral_{B_R}|U|^2 and
q=tr((DU)^2). The main arbitrary-rotation conjecture remains open.

## 2. Missing premise in two compressed source-symmetry statements

Summary row 5, line 46, and historical B.5, lines 6288-6293, first discuss
uniformly sublinear profiles and then say that axisymmetry of q also
suffices. This needs an explicit qualification: E(R)=o(R^3), in particular
uniform decay of U. The full Theorem AP paragraph, lines 193-198, states
this qualification correctly.

Here is the exact counterexample to the unqualified reading. Let b be a
nonzero horizontal constant vector and put

    U(y)=b,
    P(y)=-((1-c)b+omega Jb).y+p0.

This is a smooth full profile for every real c and omega, since DU=0 and
the pressure gradient cancels the two constant terms. It is bounded and
uniformly sublinear, and q=0 has every orthogonal symmetry. For 0<c<1/2,
the horizontal vector (1-c)b+omega Jb is nonzero: its squared norm is
((1-c)^2+omega^2)|b|^2. Thus P is not axisymmetric and U is not axial.
Moreover E(R)=(4pi/3)|b|^2 R^3, precisely violating the missing little-o
premise. This reproduces the control already recorded in A3043.

The correction is to insert, at both passages, "under E(R)=o(R^3), in
particular for decaying profiles" after the source-symmetry condition.
The theorem A3040 and the report's fully stated Theorem AP are unaffected.

## 3. The positive Hessian belongs to f, not f times the cutoff

The spherical-source row at line 5508 says that the test
sqrt(1+|y|^2) chi(y/R) has a positive definite Hessian. This is false as a
global statement. A nonzero compactly supported C2 function cannot have a
positive semidefinite Hessian everywhere: its restriction to any line is
convex and zero at both sufficiently distant ends, hence is identically
zero. In particular the indicated nonzero compactly supported test cannot
have a positive definite Hessian.

The actual argument in Theorem 8(e), lines 755-760, is correct. For
f(y)=sqrt(1+|y|^2), D2 f has radial eigenvalue (1+|y|^2)^(-3/2) and two
tangential eigenvalues (1+|y|^2)^(-1/2). Expanding the product gives

    D2(f chi_R)=chi_R D2f+H_R,

where H_R is supported in R<=|y|<=2R and |H_R|<=C/R there. Thus the
annular error is bounded by C E(2R)/R. Under E(R)=o(R), the positive
uncut Hessian controls every fixed ball and yields U=0. The row should
attribute positive Hessian to f and describe H_R separately.

## 4. An open implication must not be stated as false

Lines 4543-4544 say that none of the conditions of Theorem 8(a)-(c)
"follows from bare decay", citing A3038 OPEN. The supported statement is
"none is known to follow from bare decay" or "none is derived here".
A3038 supplies neither a full-profile counterexample nor a proof that
such an implication is impossible. This distinction matters especially
because a proof of the unrestricted conjecture would make every
zero-profile condition automatic.

The table fragments "not from decay" in the new recheck citations should
likewise read "not derived from decay" or "derivation from decay OPEN".
These are epistemic corrections, not mathematical counterexamples to the
underlying conditional theorems.

## 5. Further precisions

Theorem AP line 186 says "The proof does not localize". Its new theorem
does localize pressure symmetry to an absorbing ball. The intended
statement is that local regularity and the local momentum equation alone
do not bound Omega_theta/r or give the angular-work sign. The growing
countertests in A3050-A3052 establish exactly that statement.

Lines 764 and 4684 describe the closed vorticity bound as having "no
condition at infinity". The theorem still assumes bounded U and Hb.
The correct precision is "no additional condition on vorticity at
infinity". No inference removing Hb has been verified.

The two alternatives for the translation-return theorem should both
explicitly inherit 0<c<1 and uniform decay. Parentheses around the
period/return alternatives prevent a syntactic reading that drops those
common hypotheses.

## 6. Positive parts and collaboration

The changed full statements of the C1 absorbing-ball pressure theorem,
orthogonal source symmetry, local countertests, energy recheck,
stationary C1 theorem and source-sign theorem agree with their
designated verdicts at the hypotheses written there. The direct delta
adds no proof of unrestricted nonexistence.

The complete existing coordinator analytical comparison
in the team records was read, including all fourteen
items and three remarks. Its proof agrees with A3047-A3048. Its
diagnostic script, first failed execution and later execution log were
not read or certified by this audit. It predates the report issues above
and is not a response to them. The correction request is sent through
this agent's in the team records for the existing configured model
coordinator. Actual provider execution is independently unattested.
No new agent or remote model client is used.

The assembly is not approved while these corrections are outstanding.
The earlier approval of 37391724 remains the latest cumulative approval.
Only the literal unqualified symmetry inference and cutoff-Hessian
sentence are refuted here; their correctly scoped underlying theorems
remain confirmed.
