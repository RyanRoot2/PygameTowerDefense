def test_main_exists():
    from tower_defense.main import main

    assert callable(main)
