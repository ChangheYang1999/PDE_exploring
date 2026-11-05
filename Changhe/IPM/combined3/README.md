# 从压缩证据包复现 IPM 结果

当前目录保留原始源码、Markdown 证明与报告，以及 `IPM.evidence/` 下的少量压缩证据包。原始 JSON、积分分片和缓存没有逐文件放进 Git；其内容与路径由 `IPM.evidence/index.json` 逐项绑定 SHA-256。原来的数学公式、源程序内容和认证常数保持不变。

## 一次命令解包并检查

在仓库根目录运行；若已有下列研究环境，可直接执行第二条命令：

```bash
python3 -B Changhe/IPM/combined3/IPM.artifacts/bootstrap_research_env.py
/tmp/ipm-combined3-venv/bin/python -B Changhe/IPM/combined3/reproduce_packed.py
```

第一条命令按原来的 `requirements-research.txt` 在仓库外创建临时环境。复现入口本身不会下载软件，也不会重新生成昂贵的原始数值分片。

入口先核验全部证据包和原始源码，随后在**仓库外新建的临时目录**还原原目录结构。还原文件包括此项目的源码和数据，以及原有认证需要的六个继承输入，因而常规四项检查不依赖其他历史计算文件。解包后运行：

1. 严格残差 manifest 检查，包括全部 383 个工件与两个精确源文件。
2. 独立精确有理数残差阈值检查。
3. 完整矩阵证书下的最终闭合重放。
4. 独立最终闭合重放。

成功状态为 `PACKED_EVIDENCE_REPRODUCTION_PASS`。终端输出 `workspace` 给出还原目录；该目录的 `verification/` 保存准确命令、返回码、日志和新结果，`REPRODUCTION.json` 保存汇总。这些输出都不会进入 Git 工作树。此入口重放现有检查，不代替独立数学审查。

## 只还原文件，或选择输出位置

仅解包不需要研究依赖，Python 标准库即可运行：

```bash
python3 -B Changhe/IPM/combined3/reproduce_packed.py --materialize-only
```

也可以指定一个**仓库外、尚不存在或为空**的输出根目录：

```bash
/tmp/ipm-combined3-venv/bin/python -B Changhe/IPM/combined3/reproduce_packed.py \
  --output-dir /tmp/ipm-combined3-replay
```

入口拒绝在当前 Git 工作树内解包，拒绝覆盖现有文件，并检查归档成员路径、文件类型、大小和逐文件校验和。已有输出目录若非空，请指定新的目录。

## 使用原来的研究命令

还原后的路径与原仓库一致：

```text
<workspace>/Changhe/IPM/combined3/
```

原报告中的本地数据链接，以及 `IPM.artifacts/REPRODUCE.md` 中的命令，均应在该还原工作区中使用。原目录中的数据链接在解包前可能没有对应的散文件，这是证据打包后的预期布局。

如需重放新残差证书的全部已保存原始面板，而不仅检查其 manifest 与最终阈值，可在还原后运行其既有入口：

```bash
/tmp/ipm-combined3-venv/bin/python -B \
  <workspace>/Changhe/IPM/combined3/IPM.artifacts/residual_recertification/reproduce.py \
  --repo-root <workspace>
```

请用实际 `workspace` 路径替换占位符。默认入口使用保存的证据；只有主动添加其 `--regenerate` 参数才会重新生成原始数值分片。其他历史探索脚本若引用未列入本次六个继承输入的旧材料，仍需对应历史工作区。

## Portability

`reproduce_packed.py` uses only Python's standard library to verify and unpack. Pass `--python /path/to/python` to select an interpreter with the pinned research dependencies for the four checks. Original code and evidence hashes are preserved; extraction and all validation outputs stay outside the Git working tree.
