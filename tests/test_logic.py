from second_realize import scrap_json


def test_scrap_json():
    assert isinstance(scrap_json()[0], list)
    assert len(scrap_json()[0]) == 24
