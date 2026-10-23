"""Apply low priority before exec; never import numerical libraries here."""
import json
import os
from pathlib import Path
import sys
import time


def main():
    increment, metadata_path, command = int(sys.argv[1]), Path(sys.argv[2]), sys.argv[3:]
    if not command:
        raise SystemExit('worker command required')
    actual = os.nice(increment)
    metadata_path.write_text(json.dumps({'pid': os.getpid(), 'time': time.time(),
                                         'nice': actual, 'requested_increment': increment}, indent=2) + '\n')
    if actual < increment:
        raise SystemExit('could not establish requested low priority')
    os.execvpe(command[0], command, os.environ)


if __name__ == '__main__':
    main()
