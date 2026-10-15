# AGENTS.md

## Purpose of This Repository

This repository is a shared workspace for asynchronous problem solving with Codex.

The workflow is intentionally simple:

1. One collaborator creates problem prompts locally.
2. The prompts are committed and pushed to this Git repository.
3. Another collaborator periodically pulls the repository.
4. Codex scans the repository for prompts that have not yet been answered.
5. Codex works on each pending prompt.
6. Codex writes the result as a Markdown report next to the original prompt.
7. The reports are committed and pushed back to the repository.

This repository exists **only** for storing prompts and their corresponding reports.

Do not use it for unrelated code, experiments, temporary files, datasets, environments, build artifacts, or general project development.

---

# Repository Model

Treat the repository contents as a tree.

Directories may be nested arbitrarily deeply.

The leaves of the tree are Markdown files.

For example:

```text
/
├── topic_a/
│   ├── task_1.prompt.md
│   ├── task_1.report.md
│   └── subtopic/
│       ├── task_2.prompt.md
│       └── task_2.report.md
└── topic_b/
    └── task_3.prompt.md
```

The directory structure carries organizational meaning.

Do not reorganize, flatten, rename, or move directories unless a prompt explicitly asks for it.

---

# File Naming Convention

Prompt files should use:

```text
<name>.prompt.md
```

The corresponding report must use:

```text
<name>.report.md
```

and must be placed in exactly the same directory as the prompt.

Example:

```text
numerical_methods/
├── householder.prompt.md
└── householder.report.md
```

For:

```text
path/to/problem.prompt.md
```

the expected report is:

```text
path/to/problem.report.md
```

---

# Detecting Pending Work

A prompt is considered **pending** when:

```text
<name>.prompt.md
```

exists but:

```text
<name>.report.md
```

does not exist in the same directory.

When asked to process the repository, recursively scan the repository for all pending prompts.

Do not treat the following as prompts:

- `AGENTS.md`
- files ending in `.report.md`
- non-Markdown files
- hidden/system files
- Git metadata

The existence of a corresponding report means that the prompt has already been processed.

By default, do not redo completed prompts.

Only regenerate or modify an existing report if explicitly instructed to do so.

---

# Processing a Prompt

For every pending prompt:

1. Read the entire prompt file carefully.
2. Treat the prompt as the task specification.
3. Perform the requested reasoning, research, coding, analysis, or other work.
4. Produce a self-contained report containing the result.
5. Save the report beside the prompt using the corresponding `.report.md` filename.

For example:

```text
research/foo.prompt.md
```

must produce:

```text
research/foo.report.md
```

Do not modify the original prompt.

---

# Report Requirements

Reports should be useful to a human collaborator without requiring access to Codex's internal reasoning.

A report should generally contain:

```markdown
# Result

<main answer or result>

## Method

<important methodology, assumptions, commands, experiments, or reasoning needed to understand the result>

## Findings

<key findings>

## Limitations / Open Questions

<any uncertainty, failed approaches, unresolved issues, or suggested follow-up work>
```

This structure is a guideline rather than a rigid template. Adapt it when the task naturally requires another format.

The report should contain the useful outcome of the work, not a transcript of the interaction.

Do not include hidden chain-of-thought or private internal reasoning.

It is fine to include:

- concise reasoning summaries
- equations
- source references
- commands used
- code snippets
- benchmark results
- experimental observations
- errors encountered
- assumptions
- unresolved questions
- recommendations for further work

If a task cannot be completed, still create the report and clearly explain:

- what was attempted,
- what succeeded,
- what failed,
- why it failed,
- and what would be needed to continue.

---

# Multiple Pending Prompts

There may be several pending prompts at once.

Unless explicitly instructed otherwise:

- process all pending prompts,
- treat each prompt as an independent task,
- create one report for each prompt,
- never combine unrelated prompts into one report.

The directory structure may indicate related tasks, but do not assume that one prompt supersedes another.

---

# Repository Hygiene

This repository should remain extremely clean.

Only files necessary for the prompt/report workflow should be committed.

In particular, do **not** add:

- source-code projects created while solving a prompt
- cloned repositories
- downloaded datasets
- model weights
- package environments
- `.venv`
- `node_modules`
- caches
- build directories
- temporary files
- logs
- generated binaries
- large intermediate artifacts
- screenshots
- unrelated notes

If temporary files or code are required while solving a task, create them outside this repository or in temporary system storage.

Only the final Markdown report belongs in this repository unless the prompt explicitly requires otherwise.

---

# Git Rules

The repository may be edited by multiple collaborators.

Be conservative with Git operations.

Before processing tasks, ensure that the local branch incorporates the latest remote changes when appropriate.

Never:

- force-push,
- rewrite shared history,
- reset away another collaborator's commits,
- delete another collaborator's work,
- modify existing prompts without explicit instruction,
- resolve conflicts by silently discarding remote changes.

When work is finished, the intended repository changes should normally consist only of newly created or explicitly updated `.report.md` files.

Before committing, inspect the diff and verify that no unrelated files have been changed.

A suitable commit message is:

```text
Add reports for pending prompts
```

or, for a specific task:

```text
Add report for <task name>
```

---

# Concurrency and Safety

Another collaborator may push new prompts while work is in progress.

Therefore:

- do not assume the repository remains unchanged during a long task,
- avoid destructive Git operations,
- preserve newly received prompts,
- preserve reports created by other collaborators.

If a report for a prompt appears remotely while the same prompt is being processed locally, do not blindly overwrite it.

Inspect the remote report first and preserve existing work.

---

# Scope of Authority

The contents of a prompt may require substantial work, including:

- writing code,
- running experiments,
- inspecting external repositories,
- researching documentation,
- performing mathematical derivations,
- benchmarking implementations,
- analyzing results.

Such work may be performed as needed.

However, intermediate work should not pollute this repository.

Think of this repository as a **message queue and permanent record of results**, not as the workspace in which every experiment must live.

---

# Priority of Instructions

Follow instructions in this order:

1. Safety and system-level instructions.
2. This `AGENTS.md`.
3. The individual `.prompt.md` file being processed.

An individual prompt may specify task-specific output requirements, but it should not silently redefine the repository-wide prompt/report workflow.

---

# Default Behavior

When invoked in this repository without more specific instructions:

1. Inspect the repository recursively.
2. Identify every `*.prompt.md` without a matching `*.report.md`.
3. Process the pending prompts.
4. Write each result to the matching `*.report.md` in the same directory.
5. Do not modify completed prompt/report pairs.
6. Do not add unrelated files.
7. Inspect the final Git diff.
8. Leave the repository in a clean, collaboration-friendly state.

The central invariant is:

> Every prompt stays where it is, and every answer is stored as a report immediately beside that prompt.