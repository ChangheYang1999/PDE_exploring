"""Platform adapters for isolated, explicit migration workspaces."""
import os
from pathlib import Path
import platform

def output_dir():
    default = Path(__file__).resolve().parents[2] / "work" / Path(__file__).resolve().parent.name
    return Path(os.environ.get("IPM_WORK_DIR", str(default))).expanduser().resolve() / "results"

def peak_rss_mib(usage):
    return usage.ru_maxrss / (2**20 if platform.system() == "Darwin" else 1024)
