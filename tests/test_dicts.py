from utils.dicts import get_val


DATA = {"vcs": "mercurial"}


def test_get_val():
    assert get_val(DATA, "vcs") == 'mercurial'
    assert get_val(DATA, "git", "vcs") == "vcs"
    assert get_val({}, "vcs", "git") == "git"