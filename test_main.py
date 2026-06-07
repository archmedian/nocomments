import main


def test_main():
    assert main.main(b"OK") == "OK"
    assert main.main(b"NOT OK") == "NOT OK"
    assert main.main(b"\xff") == "NOT OK"
