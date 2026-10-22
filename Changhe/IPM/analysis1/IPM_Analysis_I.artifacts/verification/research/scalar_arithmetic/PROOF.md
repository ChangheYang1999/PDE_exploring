# Audit of the modal source interval Newton derivative

Date: 2026-10-20. Status: REFUTED derivative identity in the recorded code snapshot. This does not by itself refute the published numerical root enclosure.

## Exact identity

On the positive axis put x=exp(t), w(t)=V_1(exp(t),0), S(t)=sum_n 2n psi_n(exp(t)). Then w=c_l exp(t)-exp(-t)S. The numerical root function is

F(t)=x w(t)=c_l exp(2t)-S(t).

Its exact derivative is

F'(t)=2c_l exp(2t)-S'(t)=F(t)+x w'(t).

The code `axis_tms` in num/src/cert_scalars2.py returns `xV1=F` and `xdV1=c_l exp(2t)+S-S'`, which is x w'(t), not F'(t). In `main`, the interval Newton numerator is `xV1` while its derivative interval is `xdV1`. The derivative hypothesis of that interval Newton step is therefore not proved. At a true root F=0 these two derivatives agree, but the interval Newton theorem needs an enclosure of the derivative throughout its input interval, including points where F is nonzero. Endpoint equality at the unknown root is insufficient.

## Executable countercheck

The exact manufactured field psi=0, c_l=1/2 has F(t)=exp(2t)/2 and F'(0)=1. The actual source function, called read-only on matching exact zero modal Taylor data, returns a narrow derivative interval near1/2 excluding1. Its source hash and output are in evidence/newton_derivative_audit.json. This is a test of the generic algebraic derivative claim, not an exact stationary trial or a nonlinear normalization example.

## Repairs and scope

A correct derivative Taylor model is `xV1+xdV1`, or directly `2 c_l exp(2t)-S'`. Another valid method evaluates V_1 and its derivative consistently. Direct certified signs at two endpoints plus a positive derivative interval also prove existence and local uniqueness, without Newton. The independent all-mode calculation in ../modal_source/PROOF.md takes this last approach.

The recorded residual arithmetic defects remain separate obligations. Correcting this derivative does not establish their enclosures. Conversely, this mismatch alone does not prove that the reported root ball is numerically false; an independent enclosure may still confirm it.
