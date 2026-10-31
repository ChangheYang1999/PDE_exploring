# Canonical representation semantics for the origin calculation

Recorded on 2026-10-29T01:31:14.173880+00:00. This supplements the exact coefficient decoder and does not change the statement or arithmetic of the origin proof.

The decoder validates the numerical archive, metadata equality, channel dimensions, harmonic support and damping. The archive has no twist-convention flag. The semantics below are established by inspection of the representation sources, preserved with hashes in `representation_snapshot_0130/manifest.json`. They are not additional checks performed by the decoder.

Write q=|y|^2 and s=sqrt(q+R0^2). The production radial coordinate is x=(s-R0)/(s+R0), and the shifted Chebyshev argument is xi=2x-1. Thus x(0)=0 and xi(0)=-1. The independent implementation uses the algebraically identical stable expression x=q/(s+R0)^2. The main envelopes are powers of s/R0, which equals one at the origin.

The A, C, B and D channels use beta(q)=omega/(2 c_l) log(1+q/R0^2). It is smooth near q=0 and beta(0)=0. Production adds the E channel after twisting the other poloidal terms; E is explicitly untwisted. The independent implementation passes twisted=False for E. Hence all channels are smooth, but it would be incorrect to state that every channel uses the twist. Each correction channel additionally has the factor (q/(q+R1^2))^d with positive R1 and integer d>=1. These facts give precisely the origin values used in the proof.

The singular exterior angle proportional to log(r/R0) is used for the homogeneous tail and closure, not as the angle of the smooth represented field at the origin. The E distinction does not affect the four surviving axial coefficient sums: its damping vanishes at the origin, and the proof already checks the possible first radial derivative contributions.

The lead's initial lead review correctly accepts the origin identity but its ancillary statement that all channels are twisted is corrected here. The correction has been sent back through team notes. This is a source-semantics inspection, not a new continuum numerical validation or a formal proof.
