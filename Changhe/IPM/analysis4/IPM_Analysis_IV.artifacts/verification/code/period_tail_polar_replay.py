"""Run the independent polar replay of the topic262 prefix."""
from pathlib import Path
import sys
sys.dont_write_bytecode=True
import period_polar_prefix_replay as core
core.ROOT=Path('research/262_tail_response_prefix')
core.main()
(core.ROOT/'sources/period_tail_polar_replay.py').write_bytes(Path(__file__).read_bytes())
