from gc import collect

from pyalpm import Handle


# PYTHONPATH="$PWD/build/lib.linux-x86_64-3.7" pytest -k test_refcount_segfault -s


def get_localdb():
    handle = Handle('/', '/tmp/')
    return handle.get_localdb()

def test_refcount_segfault():
    localdb = get_localdb()
    collect()
    x = localdb.search('yay')
    assert x == []
