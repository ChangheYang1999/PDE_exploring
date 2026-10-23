# Bounds from an incomplete activity ledger

Status: CONFIRMED as a measure-theoretic bound under the explicit containment and clock assumptions below. This does not certify the historical trainer's classification of every elapsed second as substantive computation.

## Statement and notation

Let A_i be unknown measurable activity sets. Suppose A_i is contained in a known finite union of intervals I_i and its length is at least a_i >= 0. Let E be an exactly known activity set, also a finite union of intervals. Then, with U=E union (union_i I_i),

    max(|E|, max_i a_i, |U| - sum_i (|I_i|-a_i), 0)
        <= |E union (union_i A_i)| <= |U|.

If I_i is empty, its a_i must be zero. Every a_i must be at most |I_i|. If these consistency conditions fail, the input assumptions are invalid; clipping the missing measure to zero does not repair them.

## Proof

Every point of U absent from E union (union_i A_i) is outside E and lies in some I_i but not A_i. Thus the absent set is contained in union_i (I_i minus A_i), whose length is at most sum_i (|I_i|-a_i). Subtraction gives the third lower bound. Containment gives the upper bound. Inclusion of E and each A_i gives the first two lower bounds. Length is nonnegative. This proves all claims.

For one worker with pairwise disjoint credited step intervals divided among ledger records, take A_i to be the union over all its records. Its length is the sum of the recorded activity lengths, allowing for rounding error. Take I_i to be the union of all the corresponding outer intervals. Aggregating this way reduces artificial missing-measure penalties caused by overlapping outer intervals for adjacent records. Aggregation requires a verified unique worker identity and pairwise disjoint credited intervals, not merely equal experiment names.

## Audited historical trainer assumptions

The source uses `strftime` at whole-second resolution, flooring the epoch clock. A displayed start s and end e are therefore not exact endpoints. Also `checkpoint()` resets the ledger interval start but retains `t_last_step`. The first subsequently credited elapsed step interval can start before the new displayed start. Every credited interval has length at most 30 seconds. Under an ordered, non-jumping epoch clock, each record's credited set is contained in

    [s - 30, e + 1].

Indeed its right endpoints occur before the record's end timestamp is formatted, which is less than e+1. All endpoints credited after the new start occur after that start; the only possible preceding part has length at most 30. The first recorded interval of a process is covered by the same conservative enlargement. Intervals skipped by the >30-second gap rule are not counted. A rounded `active_seconds` value a has lower bound max(0,a-0.0005001), allowing half a millisecond plus a small floating-point margin.

For the audited trainer, successful step end times are ordered and `t_last_step` advances after each accounting update. Credited step intervals within a process do not overlap, including across checkpoint records. Grouping by host and PID is valid provided the records are from this source protocol, are not duplicated and have consistent time/step order. A reused PID cannot refer to concurrent processes on one host, but arbitrary externally fabricated records are not covered. The implementation checks duplicate records and rejects inconsistent sizes. The source does not provide monotonic-clock corroboration; absence of clock jumps remains an explicit assumption for historical reconstruction.

These are bounds on the union of elapsed chunks that the old trainer credited. Such chunks can include checkpoint I/O and uninstrumented short pauses. The old ledger alone cannot distinguish that overhead from numerical work. Future instrumentation should delimit actual compute/validation blocks, use full-resolution epoch endpoints plus monotonic durations, record interruption handling and exact subintervals, and restart workers onto the repaired source. Changing a Python file on disk does not update an already running process.

## Scope

No endpoint reconstruction makes the density estimate exact. No historical lower bound alone establishes 96 active hours. Empty new subinterval arrays must mean zero activity, not fallback to coarse legacy data. Mathematical activity bounds, clock fidelity, and classification as eligible experiment time are three separate checks. This result is not an Euler theorem and its computation is not counted as an Euler experiment.

## Rounded explicit chunks

The repaired trainer writes each chunk endpoint rounded to 0.001 seconds. This makes the union of recorded endpoints an exact quantity for the serialized data, but not an exact duration of the unrounded events. For a recorded pair [s,e], the underlying pair lies in [s-q,e+q] with q=0.000502 seconds, allowing half a millisecond plus conservative floating-point slack at the recorded 2026 epoch. Its duration is at least max(0,e-s-2q). An explicit empty array has zero recorded activity and must not be interpreted as a legacy record.

Combine these enlarged explicit chunks with the historical enlarged intervals. If one worker's underlying credited pieces are disjoint, group them by host and process and add their lower duration bounds before applying the earlier union-minus-missing-measure proof. This also accounts for possible overlap between different workers. The result bounds the union of the credited elapsed pieces, conditional on the source protocol and ordered clock. It does not show that those pieces consist exclusively of eligible numerical work: the audited trainer still merges inter-step I/O and short pauses. First steps omitted by the trainer are not reconstructed. Therefore these bounds are not bounds on all actual eligible numerical activity.
