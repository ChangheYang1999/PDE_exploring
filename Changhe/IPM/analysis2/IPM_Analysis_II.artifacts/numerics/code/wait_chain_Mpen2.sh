#!/bin/bash
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
while [ $(grep -c "done" runs/diag_chain.log) -lt 3 ]; do sleep 30; done
./code/diag_chain.sh nb_Mpen2
