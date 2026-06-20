from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_guess_100_when_secret_is_lower_is_too_high():
    # Guessing 100 when secret is 89 should say Too High, not Too Low
    # Previously broken by lexicographic string comparison ("100" < "89")
    outcome, _ = check_guess(100, 89)
    assert outcome == "Too High"


def test_guess_at_minimum_is_too_low():
    # Guessing 1 (the minimum) when secret is higher should say Too Low, not Too High
    outcome, _ = check_guess(1, 50)
    assert outcome == "Too Low"