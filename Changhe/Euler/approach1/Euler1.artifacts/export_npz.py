#!/usr/bin/env python3
"""Export a checkpoint to a plain NPZ (FP64 weights) + JSON manifest for independent validation.
Usage: python3 export_npz.py <ckpt.pt> <out_prefix>   -> <out_prefix>.npz, <out_prefix>.json
The manifest documents the architecture so that the forward pass can be reconstructed without this code
(see CHECKPOINT_FORMAT.md)."""
import json, sys, hashlib, os
import numpy as np
import torch

ck = torch.load(sys.argv[1], map_location="cpu", weights_only=False)
out = sys.argv[2]
sd = ck["model"]; cfg = ck["cfg"]
arrays = {k: v.detach().cpu().double().numpy() for k, v in sd.items()}
np.savez(out + ".npz", **arrays)
mcfg = cfg["model"]
feature_set = mcfg.get("feature_set", "dir_log")
n_tail = int(mcfg.get("n_tail", 2 if feature_set == "dir_tau" else 1))
cl_trainable = bool(cfg.get("cl_trainable", False))
lo, hi = cfg.get("cl_bounds", [0.4, 0.5])
if cl_trainable:
    th = float(sd["cl_theta"]); cl = lo + (hi - lo) / (1 + np.exp(-th))
else:
    cl = float(sd["cl_fixed"])
man = {
    "source_checkpoint": os.path.abspath(sys.argv[1]), "source_sha256": hashlib.sha256(open(sys.argv[1], "rb").read()).hexdigest(),
    "exp_id": ck.get("exp_id"), "saved": ck.get("saved"), "state": {k: v for k, v in ck.get("state", {}).items() if k != "interruptions"},
    "dtype": "float64", "cl": cl, "cl_trainable": cl_trainable, "cl_bounds": [lo, hi], "C": float(cfg.get("C", 0.0)),
    "architecture": {
        "feature_set": feature_set, "l_in": float(mcfg.get("l_in", 1.0)), "xi_scale": float(mcfg.get("xi_scale", 3.0)),
        "l_env": float(mcfg.get("l_env", 1.0)), "n_tail": n_tail, "a_env_shift": float(mcfg.get("a_env_shift", 0.0)),
        "p_env_shift": float(mcfg.get("p_env_shift", 0.0)), "width": int(mcfg.get("width")), "depth": int(mcfg.get("depth")),
        "activation": "tanh", "out_scale": float(mcfg.get("out_scale", 1.0)),
        "netA_keys": sorted(k for k in sd if k.startswith("netA.")), "netP_keys": sorted(k for k in sd if k.startswith("netP.")),
        "seed": {"use": bool(cfg.get("seed", {}).get("use", True)), "abc": sd["seed_abc"].tolist(), "trainable": bool(cfg.get("seed", {}).get("trainable", False))},
    },
    "formulas": {
        "features_dir_tau": "xi = y / sqrt(l_in^2 + |y|^2); x = [xi_1, xi_2, xi_3, |xi|^2]",
        "features_dir_log": "x = [y / sqrt(l_in^2+|y|^2), log(1+|y|^2/l_in^2)/xi_scale]",
        "mlp": "h_0 = x; h_{i+1} = tanh(W_i h_i + b_i) for i < depth; out = W_depth h_depth + b_depth; keys netX.lins.{i}.weight/bias",
        "raw": "NA(y) = out_scale * netA(x) reshaped (n_tail, 3); NP(y) = out_scale * netP(x) (n_tail,)",
        "projection": "Q = diag(-1,-1,1); SA(y) = [NA(y) + Q NA(Qy)]/2 per term; SP(y) = [NP(y) + NP(Qy)]/2",
        "envelopes": "d = 1 - 1/cl; base = 1 + |y|^2/l_env^2; envA_k = base^((d+1+k(d-1)+a_env_shift)/2); envP_k = base^(d + k(d-1)/2 + p_env_shift/2)",
        "seed": "M = [[a,b,0],[c,-1-a,0],[0,0,1]]; chi = (1+|y|^2)^(-1/(2cl)); A_seed = -(chi/3) y x (M y); P_seed = -(chi^2/2) y.(M+M^2) y",
        "fields": "A = A_seed + sum_k envA_k SA_k ; P = P_seed + sum_k envP_k SP_k ; U = curl A ; pressure gauge P(inf) = 0",
    },
    "config": cfg,
}
json.dump(man, open(out + ".json", "w"), indent=1)
print("wrote", out + ".npz", out + ".json", "cl", cl)
