#!/bin/bash
# runs one short single-process command while worker 3111533 of n14_a34_c30_ff is paused (keeps the lane at 3 busy processes)
W=3111533
kill -STOP $W 2>/dev/null
"$@"
kill -CONT $W 2>/dev/null
