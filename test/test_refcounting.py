from gc import collect

from pyalpm import Handle
from conftest import TEST_MIRROR, REPO_1, ARCH


# PYTHONPATH="$PWD/build/lib.linux-x86_64-3.7" pytest -k test_refcount_segfault -s


def get_localdb():
    # Return localdb, so handle should go out of scope
    handle = Handle('/', '/tmp/')
    return handle.get_localdb()

def register_syncdb():
    handle = Handle('/', '/tmp/')
    repo = handle.register_syncdb(REPO_1, 0)
    repo.servers = [TEST_MIRROR.format(REPO_1, ARCH)]
    return repo

def get_syncdb():
    # Return syncdb, so handle should go out of scope
    handle = Handle('/', '/tmp/')
    repo = handle.register_syncdb(REPO_1, 0)
    repo.servers = [TEST_MIRROR.format(REPO_1, ARCH)]
    return handle.get_syncdbs()[0]

def test_refcount_segfault():
    localdb = get_localdb()
    collect()
    x = localdb.search('yay')
    assert x == []

def test_syncdb_segfault():
    syncdb = get_syncdb()
    collect()
    assert syncdb.search('yay') == []

def test_register_syncdb_segfault():
    syncdb = register_syncdb()
    collect()
    assert syncdb.search('yay') == []
