from mb_commons import shell


def test_run_command():
    # stdout
    res = shell.run_command("echo abc 123")
    assert res.stdout.strip() == "abc 123"

    # stderr
    res = shell.run_command("cat /no/such/path")
    assert res.stderr.strip() == "cat: /no/such/path: No such file or directory"

    # out
    res = shell.run_command("echo abc 123")
    assert res.out.strip() == "abc 123"
