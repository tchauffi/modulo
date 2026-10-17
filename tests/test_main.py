from modulo import main


def test_main_prints_greeting(capsys):
    main()
    assert capsys.readouterr().out == "Hello from modulo!\n"
