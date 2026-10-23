"""Safety tests use tiny dummy subprocesses only; no optimization is launched."""
import fcntl
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

import psutil
from policy import Policy, evaluate
import telemetry

HERE = Path(__file__).resolve().parent
GUARD = HERE / 'guard.py'


def sample(**changes):
    value = dict(monotonic_seconds=10.0, family_rss_mib=50.0, available_mib=10000.0,
                 available_pct=60.0, load_per_cpu=0.1, disk_free_gib=100.0,
                 swap_used_mib=0.0, pageout_mib=0.0, swapout_mib=0.0)
    value.update(changes)
    return value


class PolicyTests(unittest.TestCase):
    def test_separate_rss_and_pressure_limits(self):
        base = sample()
        self.assertFalse(evaluate(base, base, None, Policy())['stop'])
        self.assertTrue(evaluate(sample(family_rss_mib=2049), base, None, Policy())['stop'])
        self.assertTrue(evaluate(sample(available_mib=100), base, None, Policy())['stop'])
        self.assertTrue(evaluate(sample(available_pct=10), base, None, Policy())['stop'])

    def test_missing_required_telemetry_fails_closed_optional_sensors_do_not(self):
        base = sample()
        self.assertTrue(evaluate(sample(available_mib=None), base, None, Policy())['stop'])
        self.assertFalse(evaluate(sample(temperature_c=None), base, None, Policy())['stop'])

    def test_swap_allocation_is_not_equivalent_to_paging(self):
        base = sample()
        allocation = sample(swap_used_mib=1024)
        self.assertFalse(evaluate(allocation, base, None, Policy())['stop'])
        self.assertTrue(evaluate(sample(swap_used_mib=1024, available_pct=35), base, None, Policy())['stop'])
        self.assertTrue(evaluate(sample(monotonic_seconds=11, swapout_mib=9), base, base, Policy())['stop'])
        linux = sample(monotonic_seconds=11, pageout_mib=20, pageout_semantics='Linux pgpgout KiB')
        self.assertFalse(evaluate(linux, base, base, Policy())['stop'])
        linux['available_pct'] = 25
        self.assertTrue(evaluate(linux, base, base, Policy())['stop'])

    def test_psi_thermal_cgroup_and_budgets(self):
        base = sample(cgroup_oom_kill=0)
        for value in (sample(memory_psi_full_avg10=6), sample(thermal_warning=True),
                      sample(temperature_c=100), sample(memory_pressure_level='critical'),
                      sample(cgroup_oom_kill=1, monotonic_seconds=11)):
            self.assertTrue(evaluate(value, base, base, Policy())['stop'])
        self.assertTrue(evaluate(base, base, None, Policy(), elapsed=601)['stop'])
        self.assertTrue(evaluate(base, base, None, Policy(), elapsed=1, session_seconds=3600)['stop'])

    def test_invalid_policy(self):
        for value in ({'blas_threads': 2}, {'max_seconds': float('nan')},
                      {'unknown': 1}, {'sample_seconds': 0}, {'nice_increment': 0}):
            with self.assertRaises(ValueError):
                Policy.from_dict(value)


class TelemetryTests(unittest.TestCase):
    def test_mac_no_warning_and_vm_page_size(self):
        outputs = {'vm_stat': 'Mach Virtual Memory Statistics: (page size of 16384 bytes)\nPageouts: 2.\nSwapouts: 4.',
                   'sysctl': '1', 'pmset': 'Note: No thermal warning level has been recorded\nNote: No performance warning level has been recorded\nCPU_Speed_Limit = 100'}
        with patch.object(telemetry, 'command', side_effect=lambda argv: outputs[argv[0]]):
            state = telemetry.macos_extra()
        self.assertFalse(state['thermal_warning'])
        self.assertEqual(state['memory_pressure_level'], 'normal')
        self.assertEqual(state['pageout_mib'], 2 * 16384 / 2 ** 20)
        outputs['pmset'] = 'CPU_Speed_Limit = 70'
        with patch.object(telemetry, 'command', side_effect=lambda argv: outputs[argv[0]]):
            self.assertTrue(telemetry.macos_extra()['thermal_warning'])

    def test_linux_v2_ancestor_limit_and_psi_rates(self):
        files = {'/proc/self/cgroup': '0::/team/job\n',
                 '/proc/self/mountinfo': '1 2 0:1 / /sys/fs/cgroup rw - cgroup2 cgroup rw\n',
                 '/sys/fs/cgroup/team/job/memory.max': 'max',
                 '/sys/fs/cgroup/team/job/memory.current': '104857600',
                 '/sys/fs/cgroup/team/job/memory.events': 'oom 2\noom_kill 1\n',
                 '/sys/fs/cgroup/team/memory.max': str(2048 * 2 ** 20),
                 '/sys/fs/cgroup/team/memory.current': str(1024 * 2 ** 20),
                 '/proc/vmstat': 'pgpgout 1024\npswpout 256\n',
                 '/proc/pressure/memory': 'some avg10=3.00 avg60=1.00 total=0\nfull avg10=1.50 avg60=0.20 total=0'}
        with patch.object(telemetry, 'read', side_effect=lambda path: files.get(str(path))), patch.object(telemetry.os, 'sysconf', return_value=4096):
            state = telemetry.linux_extra()
        self.assertEqual(state['cgroup_limit_mib'], 2048)
        self.assertEqual(state['cgroup_available_mib'], 1024)
        self.assertEqual(state['cgroup_oom_kill'], 1)
        self.assertEqual(state['pageout_mib'], 1)
        self.assertEqual(state['swapout_mib'], 1)
        self.assertEqual(state['memory_psi_full_avg10'], 1.5)

    def test_linux_container_mount_root(self):
        files = {'/proc/self/cgroup': '0::/team/job\n',
                 '/proc/self/mountinfo': '1 2 0:1 /team /sys/fs/cgroup rw - cgroup2 cgroup rw\n',
                 '/sys/fs/cgroup/job/memory.max': '1073741824',
                 '/sys/fs/cgroup/job/memory.current': '1048576'}
        with patch.object(telemetry, 'read', side_effect=lambda path: files.get(str(path))):
            state = telemetry.linux_cgroup()
        self.assertEqual(state['cgroup_path'], '/sys/fs/cgroup/job')
        self.assertEqual(state['cgroup_limit_mib'], 1024)


class SupervisorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.session = self.root / 'session'
        self.lock = self.root / 'worker.lock'

    def tearDown(self):
        self.temp.cleanup()

    def cli(self, *args):
        return subprocess.run([sys.executable, str(GUARD), *map(str, args)],
                              capture_output=True, text=True, timeout=20)

    def init(self, **changes):
        values = dict(max_seconds=3.0, max_session_seconds=10.0, sample_seconds=0.1,
                      terminate_grace_seconds=0.3, min_available_mib=0.001,
                      min_available_pct=0.001, max_load_per_cpu=1000.0, min_disk_free_gib=0.001,
                      max_pageout_mib_s=1e9, max_swapout_mib_s=1e9)
        values.update(changes)
        path = self.root / 'policy.json'
        path.write_text(json.dumps(values))
        outcome = self.cli('init', '--session-dir', self.session, '--policy', path, '--disk-path', self.root)
        self.assertEqual(outcome.returncode, 0, outcome.stderr)

    def run_worker(self, code):
        return self.cli('run', '--session-dir', self.session, '--cwd', self.root,
                        '--lock-file', self.lock, '--label', 'test', '--', sys.executable, '-c', code)

    def results(self):
        return [json.loads(path.read_text()) for path in self.session.glob('runs/*/result.json')]

    def test_dummy_launch_threads_priority_and_fresh_session(self):
        (self.root / 'HARDWARE_HOLD.json').write_text('{"historical": true}')
        self.init()
        outcome = self.run_worker('import os,json; print(json.dumps({"threads":os.environ["OPENBLAS_NUM_THREADS"],"nice":os.nice(0)}))')
        self.assertEqual(outcome.returncode, 0, outcome.stderr + outcome.stdout)
        record = self.results()[0]
        self.assertTrue(record['worker_started'])
        run_dir = Path(json.loads(outcome.stdout)['run_dir'])
        worker = json.loads((run_dir / 'worker.log').read_text())
        self.assertEqual(worker['threads'], '1')
        self.assertGreaterEqual(worker['nice'], 15)
        self.assertEqual(len((self.session / 'session_ledger.jsonl').read_text().splitlines()), 1)
        self.assertNotEqual(self.cli('init', '--session-dir', self.session).returncode, 0)

    def test_exclusive_lock_prevents_launch(self):
        self.init()
        with self.lock.open('a+') as stream:
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
            outcome = self.run_worker('open("launched", "w").write("bad")')
        self.assertNotEqual(outcome.returncode, 0)
        self.assertIn('exclusive worker lock held', outcome.stderr)
        self.assertFalse((self.root / 'launched').exists())
        self.assertEqual(self.results(), [])

    def test_preflight_rss_hold_and_policy_immutability(self):
        self.init(max_family_rss_mib=0.001)
        outcome = self.run_worker('open("launched", "w").write("bad")')
        self.assertNotEqual(outcome.returncode, 0)
        self.assertFalse(self.results()[0]['worker_started'])
        self.assertTrue((self.session / 'ACTIVE_HOLD.json').exists())
        self.assertFalse((self.root / 'launched').exists())
        path = self.session / 'policy.json'
        values = json.loads(path.read_text())
        values['max_family_rss_mib'] = 2048
        path.write_text(json.dumps(values))
        self.assertIn('session policy changed', self.run_worker('pass').stderr)

    def test_timeout_grace_kills_orphaned_descendant_and_hold_blocks_retry(self):
        self.init(max_seconds=0.9)
        grandchild = 'import signal,time; signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(30)'
        code = 'import subprocess,sys,time; p=subprocess.Popen([sys.executable,"-c",%r]); open("grandchild.pid","w").write(str(p.pid)); time.sleep(30)' % grandchild
        outcome = self.run_worker(code)
        self.assertNotEqual(outcome.returncode, 0, outcome.stdout)
        record = self.results()[0]
        self.assertTrue(record['termination']['sigterm_sent'])
        self.assertTrue(record['termination']['sigkill_sent'])
        pid = int((self.root / 'grandchild.pid').read_text())
        try:
            proc = psutil.Process(pid)
            self.assertEqual(proc.status(), psutil.STATUS_ZOMBIE)
        except psutil.NoSuchProcess:
            pass
        retry = self.run_worker('open("launched", "w").write("bad")')
        self.assertIn('current-session resource hold', retry.stderr)
        self.assertFalse((self.root / 'launched').exists())
        ack = self.cli('acknowledge', '--session-dir', self.session, '--lock-file', self.lock,
                       '--reason', 'Dummy timeout is expected; checkpoint grace and group cleanup verified.')
        self.assertEqual(ack.returncode, 0, ack.stderr)
        self.assertTrue((self.session / 'ACTIVE_HOLD.json').exists())
        retry = self.run_worker('print("safe dummy retry")')
        self.assertEqual(retry.returncode, 0, retry.stderr + retry.stdout)

    def test_sigterm_checkpoint_grace(self):
        self.init(max_seconds=0.8, terminate_grace_seconds=1)
        code = ('import signal,time,sys; '
                'signal.signal(signal.SIGTERM, lambda a,b: (open("checkpoint.json","w").write("{\\"saved\\":true}"),sys.exit(0))); '
                'time.sleep(30)')
        outcome = self.run_worker(code)
        self.assertNotEqual(outcome.returncode, 0)
        record = self.results()[0]
        self.assertTrue(record['termination']['sigterm_sent'])
        self.assertFalse(record['termination']['sigkill_sent'])
        self.assertEqual(json.loads((self.root / 'checkpoint.json').read_text()), {'saved': True})


if __name__ == '__main__':
    unittest.main(verbosity=2)
