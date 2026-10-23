"""Best-effort Linux/macOS telemetry normalized for the common policy.

Counters are system-wide. Missing optional sensors remain null, never zero.
"""
import os
from pathlib import Path
import platform
import re
import subprocess
import time
import psutil

MIB = 2 ** 20


def command(argv):
    try:
        completed = subprocess.run(argv, capture_output=True, text=True, timeout=2)
        return completed.stdout.strip() if completed.returncode == 0 else None
    except (OSError, subprocess.TimeoutExpired):
        return None


def read(path):
    try:
        return Path(path).read_text()
    except OSError:
        return None


def parse_pairs(content):
    result = {}
    for row in (content or '').splitlines():
        values = row.split()
        if len(values) >= 2:
            try:
                result[values[0].rstrip(':')] = int(values[1])
            except ValueError:
                pass
    return result


def linux_cgroup():
    """Read v2 hierarchy and legacy v1 memory limits without assuming root cgroup.

    Mountinfo's mount root is accounted for (containers can expose a subtree).
    The tightest readable ancestor limit is used. Unavailable files remain null.
    """
    memberships = (read('/proc/self/cgroup') or '').splitlines()
    mounts = (read('/proc/self/mountinfo') or '').splitlines()
    choice = None
    for membership in memberships:
        parts = membership.split(':', 2)
        if len(parts) != 3:
            continue
        _, controllers, member = parts
        version = 2 if controllers == '' else 1 if 'memory' in controllers.split(',') else None
        if not version:
            continue
        for row in mounts:
            left, separator, right = row.partition(' - ')
            columns, after = left.split(), right.split()
            if not separator or len(columns) < 5 or len(after) < 3:
                continue
            if (version == 2 and after[0] == 'cgroup2') or (version == 1 and after[0] == 'cgroup' and 'memory' in after[2].split(',')):
                mount_root, mountpoint = columns[3], columns[4]
                if member == mount_root:
                    suffix = ''
                elif mount_root == '/':
                    suffix = member.lstrip('/')
                elif member.startswith(mount_root.rstrip('/') + '/'):
                    suffix = member[len(mount_root):].lstrip('/')
                else:
                    continue
                choice = (version, Path(mountpoint), Path(mountpoint) / suffix)
                break
        if choice:
            break
    if choice is None:
        return {}
    version, mountpoint, leaf = choice
    result = {'cgroup_version': version, 'cgroup_path': str(leaf)}
    headrooms, limits = [], []
    here = leaf
    while True:
        limit_text = read(here / ('memory.max' if version == 2 else 'memory.limit_in_bytes'))
        current_text = read(here / ('memory.current' if version == 2 else 'memory.usage_in_bytes'))
        try:
            limit, current = int(limit_text.strip()), int(current_text.strip())
            # v1's unlimited sentinel lies near LONG_MAX.
            if limit < 2 ** 60:
                limits.append(limit / MIB)
                headrooms.append(max(0, limit - current) / MIB)
        except (TypeError, ValueError, AttributeError):
            pass
        if here == mountpoint or mountpoint not in here.parents:
            break
        here = here.parent
    result['cgroup_limit_mib'] = min(limits) if limits else None
    result['cgroup_available_mib'] = min(headrooms) if headrooms else None
    if version == 2:
        events = parse_pairs(read(leaf / 'memory.events'))
        result['cgroup_oom'] = events.get('oom')
        result['cgroup_oom_kill'] = events.get('oom_kill')
    return result


def linux_extra():
    result = linux_cgroup()
    vmstat = parse_pairs(read('/proc/vmstat'))
    page_size = os.sysconf('SC_PAGE_SIZE')
    # pgpgout is KiB of block paging I/O (may include file-backed writeback).
    result['pageout_mib'] = vmstat['pgpgout'] / 1024.0 if 'pgpgout' in vmstat else None
    result['swapout_mib'] = vmstat['pswpout'] * page_size / MIB if 'pswpout' in vmstat else None
    result['pageout_semantics'] = 'Linux pgpgout KiB; includes block paging/writeback, system-wide'
    psi = read('/proc/pressure/memory')
    if psi:
        for row in psi.splitlines():
            columns = row.split()
            values = dict(item.split('=', 1) for item in columns[1:] if '=' in item)
            if columns and 'avg10' in values:
                result['memory_psi_' + columns[0] + '_avg10'] = float(values['avg10'])
    return result


def macos_extra():
    result = {}
    vm = command(['vm_stat'])
    page = re.search(r'page size of (\d+) bytes', vm or '')
    if page:
        for label, key in (('Pageouts', 'pageout_mib'), ('Swapouts', 'swapout_mib')):
            match = re.search(r'^' + label + r':\s+(\d+)', vm, re.M)
            result[key] = int(match.group(1)) * int(page.group(1)) / MIB if match else None
    pressure = command(['sysctl', '-n', 'kern.memorystatus_vm_pressure_level'])
    result['memory_pressure_level'] = {'1': 'normal', '2': 'warning', '4': 'critical'}.get(pressure)
    result['pageout_semantics'] = 'macOS vm_stat Pageouts and Swapouts in native VM pages, system-wide'
    thermal = command(['pmset', '-g', 'therm'])
    result['thermal_raw'] = thermal
    if thermal:
        limits = [re.search(r'(CPU_Speed_Limit|CPU_Scheduler_Limit)\s*=\s*(\d+)', row) for row in thermal.splitlines()]
        warning = any(match and int(match.group(2)) < 100 for match in limits)
        warning = warning or any('warning level' in row.lower() and not re.search(r'\bno (thermal |performance )?warning', row.lower()) for row in thermal.splitlines())
        result['thermal_warning'] = warning
    return result


def family_metrics(root_pid=None, process_group=None):
    """Sum RSS rather than USS: conservative double counting of shared pages.

    Process-group enumeration retains orphaned descendants if the leader exits.
    Workers must not deliberately escape their process group/session.
    """
    pids = {os.getpid()}
    if root_pid:
        try:
            root = psutil.Process(root_pid)
            pids.update([root.pid] + [child.pid for child in root.children(recursive=True)])
        except psutil.NoSuchProcess:
            pass
    if process_group:
        for proc in psutil.process_iter(['pid', 'status']):
            try:
                if proc.info['status'] != psutil.STATUS_ZOMBIE and os.getpgid(proc.pid) == process_group:
                    pids.add(proc.pid)
            except (ProcessLookupError, PermissionError, psutil.Error):
                pass
    rss, threads, active = 0, 0, []
    for pid in pids:
        try:
            proc = psutil.Process(pid)
            if proc.status() == psutil.STATUS_ZOMBIE:
                continue
            rss += proc.memory_info().rss
            threads += proc.num_threads()
            if pid != os.getpid():
                active.append(pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return {'family_rss_mib': rss / MIB, 'family_threads': threads, 'worker_pids': sorted(active)}


def snapshot(disk_path, root_pid=None, process_group=None):
    vm, swap = psutil.virtual_memory(), psutil.swap_memory()
    result = {'time': time.time(), 'monotonic_seconds': time.monotonic(),
              'platform': platform.system(), 'total_mib': vm.total / MIB,
              'available_mib': vm.available / MIB, 'available_pct': 100.0 * vm.available / vm.total,
              'swap_used_mib': swap.used / MIB, 'pageout_mib': None,
              'swapout_mib': swap.sout / MIB if platform.system() == 'Linux' else None,
              'logical_cpus': psutil.cpu_count() or 1,
              'load_1m': os.getloadavg()[0],
              'disk_path': str(Path(disk_path).resolve()),
              'disk_free_gib': psutil.disk_usage(str(disk_path)).free / 2 ** 30,
              'temperature_c': None, 'thermal_warning': None,
              'memory_pressure_level': None, 'memory_psi_full_avg10': None,
              'cgroup_oom': None, 'cgroup_oom_kill': None}
    result['load_per_cpu'] = result['load_1m'] / result['logical_cpus']
    if platform.system() == 'Linux':
        result.update(linux_extra())
    elif platform.system() == 'Darwin':
        result.update(macos_extra())
    else:
        raise RuntimeError('supported operating systems are Linux and macOS')
    if result.get('cgroup_limit_mib') is not None:
        result['effective_total_mib'] = min(result['total_mib'], result['cgroup_limit_mib'])
        result['available_mib'] = min(result['available_mib'], result['cgroup_available_mib'])
        result['available_pct'] = 100.0 * result['available_mib'] / result['effective_total_mib']
    try:
        temperatures = psutil.sensors_temperatures() if hasattr(psutil, 'sensors_temperatures') else {}
        values = [sensor.current for sensors in temperatures.values() for sensor in sensors if sensor.current is not None]
        result['temperature_c'] = max(values) if values else None
    except (OSError, RuntimeError):
        pass
    result.update(family_metrics(root_pid, process_group))
    return result
