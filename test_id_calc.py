from id_calc import sum_of_odds_from_id


def test_valid_id_sequence():
    # 217 ->  2 + 1 + 7 = 10
    # Odd numbers from 1 to 10: 1 + 3 + 5 + 7 + 9 = 25
    assert sum_of_odds_from_id("217") == 25


def test_empty_or_spaced_input():
    assert sum_of_odds_from_id("") == 0
    assert sum_of_odds_from_id("   ") == 0
    assert sum_of_odds_from_id("  \t  \n ") == 0


def test_invalid_characters():
    assert sum_of_odds_from_id("12A34") == 0
    assert sum_of_odds_from_id("123@45") == 0
    assert sum_of_odds_from_id("ABC") == 0