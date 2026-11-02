"""Independent static source closure without importing or executing bot code.

Callers must declare roots loaded from specification strings, and data files.
Dynamic imports computed by a bot are not inferred. Final validation checks
all source hashes actually reported by each isolated match against its freeze.
"""
from __future__ import annotations
import ast
from pathlib import Path

LOCAL_ROOTS = {'td_game', 'td_bots', 'bot_research'}


def module_file(module, root=Path('.')):
    if not module or module.split('.')[0] not in LOCAL_ROOTS:
        return None
    parts = module.split('.')
    if any(not p.isidentifier() for p in parts):
        return None
    package = Path(*parts) / '__init__.py'
    source = Path(*parts).with_suffix('.py')
    if (root/package).is_file():
        return package
    if (root/source).is_file():
        return source
    return None


def static_closure(modules, root=Path('.')):
    pending = list(modules)
    visited = set()
    files = set()
    while pending:
        module = pending.pop()
        if module in visited:
            continue
        visited.add(module)
        path = module_file(module, root)
        if path is None:
            continue
        files.add(path)
        parts = module.split('.')
        for size in range(1, len(parts)):
            parent = '.'.join(parts[:size])
            if module_file(parent, root) is not None:
                pending.append(parent)
        package = module if path.name == '__init__.py' else module.rpartition('.')[0]
        tree = ast.parse((root/path).read_text(), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                pending.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                if node.level:
                    ancestors = package.split('.') if package else []
                    if node.level > len(ancestors):
                        raise ValueError(f'Invalid relative import in {path}')
                    base = '.'.join(ancestors[:len(ancestors)-node.level+1])
                    if node.module:
                        base += '.' + node.module
                else:
                    base = node.module or ''
                pending.append(base)
                # Imported names can be submodules or attributes. Existing
                # project submodules are included conservatively, without execution.
                pending.extend(base+'.'+alias.name for alias in node.names if alias.name != '*')
    return sorted(files)


def job_source_roots(jobs):
    modules = {'bot_research.experiments.validation.final_validation',
               'bot_research.experiments.validation.isolated_match'}
    for job in jobs:
        for bot in job.get('bots', []):
            if 'spec' in bot:
                modules.add(bot['spec'].partition(':')[0])
            if 'profile' in bot:
                modules.add('bot_research.bots.counters.archetypes')
    return sorted(modules)
