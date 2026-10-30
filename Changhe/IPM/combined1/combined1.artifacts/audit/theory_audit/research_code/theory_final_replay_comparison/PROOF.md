# Finite comparison of T1's final verification rerun

## Statement and scope

T1 team note 69 reports a rerun of the 69 jobs listed in its frozen
artifacts/run_all.sh. This audit concerns the saved outputs and run log.
The exact job list, 69 original outputs, 69 rerun outputs, three pairs of
side JSON records, the note and comparison helper are copied into source
and bound by hash. T1's reported process execution, wall time and affinity
are not independently attested by this file comparison. No peer program
is executed here and no mathematical proof is rerun.

The finite claims are: the log contains exactly these 69 jobs, in order,
with recorded return code zero; 51 output files agree byte for byte;
three more agree after removing only a final literal “rc=0” line from
the original file; the remaining 15 differ only in the displayed elapsed
seconds or the named started_utc/finished_utc fields. The three side JSON
files consist of one byte-identical pair and two pairs differing only in
the top-level numeric seconds field. These claims are CONFIRMED by the
exact comparisons specified below. Therefore no printed mathematical
number, check count or verdict differs in these records.

This does not convert a grid diagnostic into a proof, strengthen a
conditional claim or establish that every implemented theorem is sound.
The previous T4-506 audit of the final theory and its dependencies remains
the mathematical premise. This is independent evidence for the consistency
of the final rerun, not a new candidate computation or existence result.

## Complete finite argument

Parse the job identifiers from the frozen shell script without executing
it. Require 69 distinct identifiers. Parse each log line by the complete
pattern “job rc=integer integer-s”; require exact order, no extra line and
return code zero in each row. File names are derived from those identifiers
and required to be unique. The resulting files exhaust this comparison.

For byte-identical pairs nothing remains to prove. For the three terminal
line differences, removing exactly that final rc=0 line leaves identical
bytes. Their return codes are separately present in the bound log.

Every other changed line was read before writing the checker. The complete
list of old and new text blocks is in data/changes.json. The differences
are elapsed decimal seconds before the literal unit “ s”, the top-level
seconds value in printed JSON, or the string value of the explicitly named
started_utc and finished_utc fields. Replace only these tokens by a fixed
placeholder and require exact equality of the rest of each file. The
source-bound change list is independently reconstructed and must match.
The mathematical portions of those lines, including certified intervals,
coefficient values, check counts, cell counts and verdict words, are thus
retained byte for byte. No whole line is silently discarded.

For side JSON, parse decimals exactly rather than through binary floats.
Require the same key set and equality of all values other than seconds.
Require the seconds entries to be nonnegative decimals and distinct only
in the two declared pairs. For the unchanged pair require raw byte identity.
These comparisons prove the asserted partition 51+3+15=69 and the side
record classification. Source hashes bind the conclusion to the actual
copied files; they do not attest unobserved process behavior.

## Evidence and limitations

The proof precedes code/check.py. The checker records every finite test and
writes its own result with the real execution time. It uses no integration,
network, server, JavaScript/TypeScript, cluster, GPU or Lean/Lake process.
The original Opus-configured T1 lane's note and helper remain inactive
inputs. There is no reason to rerun the 69 jobs again for this comparison.
The reported 195 artifact checks are outside this acceptance; T4-506 had
already checked that bound final artifact list. All existing OPEN
conditions, including the complete 017 upper bound and existence closure,
remain OPEN.
