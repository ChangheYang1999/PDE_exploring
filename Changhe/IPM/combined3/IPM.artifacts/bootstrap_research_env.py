#!/usr/bin/env python3
"""Recreate the temporary research environment without adding an env to Git."""
import argparse
from pathlib import Path
import subprocess
import sys
import venv

ap=argparse.ArgumentParser()
ap.add_argument('--directory',type=Path,default=Path('/tmp/ipm-combined3-venv'))
args=ap.parse_args()
here=Path(__file__).resolve().parent
assert not args.directory.resolve().is_relative_to(here.parents[3])
venv.EnvBuilder(with_pip=True).create(args.directory)
python=args.directory/'bin/python'
subprocess.run([str(python),'-m','pip','install','-r',str(here/'requirements-research.txt')],check=True)
print('Run research scripts with',python,'-B')
