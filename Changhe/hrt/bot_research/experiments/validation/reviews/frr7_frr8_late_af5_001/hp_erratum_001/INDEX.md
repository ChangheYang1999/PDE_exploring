# Reading order

1. [ERRATUM.md](ERRATUM.md) states the exact correction and its scope.
2. [EVIDENCE.json](EVIDENCE.json) binds archived/current rows, terminal records, both full-history comparisons and the literal-copy search.
3. [check_retained_hp.py](check_retained_hp.py) is the independent standard-library reader.
4. [seal.json](seal.json) binds these new artifacts. Original sealed files remain unchanged.
