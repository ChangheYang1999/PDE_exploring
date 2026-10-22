# Frozen-expression binding and mandatory scope clarification

Written2026-10-21after the first actual Opus5.5review. Read with PROOF.md.
The original audit's AST checks inspected regenerate.py. Topic115's inherited
structure checker separately inspected the frozen producer. To make the
correspondence direct, code/source_binding.py now extracts the producing
expressions themselves from the frozen cert_forcing.py and evaluates them on
all saved contemporary replay inputs. It checks equality of all regenerated
frequency-power bounds and angular factors, all33995epsSup outputs using the
frozen TMArr.sup method, and all195r2outputs using the frozen r2 assignment.

This establishes correspondence of those selected frozen expressions on
the saved inputs. It is not a replay of the whole forcing pipeline, an
attestation of an old process, or independent input provenance. The radial
coefficients remain outputs of the contemporary radial replay. The two
arithmetic engines share these saved operands and establish independent
arithmetic verification of the conditional inequalities, not independence
of their physical interpretation.

Geometry is inherited from topic115: the true local radial parameter lies
in[0,h], and the true angular displacement lies in[-w,w], on the restricted
parent domain. The angular Taylor polynomial in PROOF.md is the exact real
polynomial. Rounded trigonometric matrix coefficients and the separate
radial-error contribution are not certified here. No physical forcing norm
or endpoint follows from this finite result.
