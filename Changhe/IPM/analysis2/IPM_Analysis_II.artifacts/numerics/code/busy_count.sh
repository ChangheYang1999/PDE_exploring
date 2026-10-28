#!/bin/bash
# Number of running Python workers whose current directory is within this numerical workspace.
task_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd) || exit 1
n=0
for p in $(ps -u "$(id -u)" -o pid,stat,args | awk '$2 ~ /^R/ && $3 ~ /python/ {print $1}'); do
  cwd=$(readlink /proc/$p/cwd 2>/dev/null)
  case "$cwd" in "$task_dir"|"$task_dir"/*) n=$((n+1));; esac
done
echo $n
