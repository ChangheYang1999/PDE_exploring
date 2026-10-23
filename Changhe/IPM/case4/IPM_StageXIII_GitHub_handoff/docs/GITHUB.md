# Create the GitHub handoff

The local staging repository has been initialized on `main`. No commit, remote
repository, remote URL, GitHub release, or push was created automatically.
Replace `OWNER` with the intended GitHub account or organization, then run:

```sh
cd /Users/caltech/research/IPM_R2_macpro_experiments/stage13_absolute_optimization/github_handoff_20261023
python3 -B tools/verify_repository.py
git add .
git commit -m "Handoff current IPM Stage XIII accepted278"
gh repo create OWNER/ipm-stage13-current --private --source=. --remote=origin
git push -u origin main
```

On the destination, clone that private repository and follow
[DEPLOY_LINUX.md](DEPLOY_LINUX.md). The main repository contains the complete
accepted optimizer state; no release download is required to resume it.

The separate 683.6 MB original derivative-evidence archive is optional.
[ARTIFACTS.md](ARTIFACTS.md) records its exact size, SHA-256 and verification
commands. If desired, upload that archive and its three sidecars as GitHub
Release assets after creating the repository. Keep them outside the Git tree;
no Git LFS dependency is needed. The existing 5.29 GB archival release is a
different preserved artifact and is not part of this compact handoff.

The ignored `runs/`, `work/`, `.venv/` and expanded coordinate JSON are local
runtime products. Required historical native-process proof files under
`research/resource_session/runs/` are intentionally tracked: unchanged epoch
recovery checks their hashes. Do not replace the root-anchored `/runs/` ignore
with a recursive `runs/` pattern.
