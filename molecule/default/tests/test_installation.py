"""
Role tests
"""

import os
import pytest

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', ['apt-transport-https', 'bacula-client'])
def test_bacula_fd_debian_packages(host, name):
    """
    Ensure packages installed
    """

    if host.system_info.distribution not in ['debian', 'ubuntu']:
        pytest.skip('Only for Debian family systems')

    assert host.package(name).is_installed


def test_bacula_fd_user(host):
    """
    Ensure user exists
    """

    bacula_user = host.user('bacula')

    assert bacula_user.exists
    assert bacula_user.home == '/var/lib/bacula'


@pytest.mark.parametrize('path,item_type,user,group,mode', [
    ('/var/lib/bacula', 'directory', 'bacula', 'bacula', 0o700),
    ('/etc/bacula', 'directory', 'root', 'root', 0o755),
    ('/etc/bacula/bacula-fd.conf', 'file', 'root', 'root', 0o400),
])
def test_bacula_fd_files(host, path, item_type, user, group, mode):
    """
    Ensure paths exists
    """

    current_item = host.file(path)

    if item_type == 'directory':
        assert current_item.is_directory
    else:
        assert current_item.is_file

    assert current_item.user == user
    assert current_item.group == group
    assert current_item.mode == mode


def test_bacula_fd_service(host):
    """
    Ensure service enabled and started
    """

    bacula_service = host.service('bacula-fd')

    assert 'is running' in host.check_output('service bacula-fd status')
    assert bacula_service.is_enabled


def test_bacula_fd_socket(host):
    """
    Ensure socket listening
    """

    assert host.socket('tcp://0.0.0.0:9102').is_listening
