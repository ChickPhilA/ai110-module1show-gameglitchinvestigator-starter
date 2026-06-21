# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] Describe the game's purpose.
      The game's purpose is a simple, number guessing game. The player is to guess a secret number between a range of two numbers (different per every difficulty), being given a limited number of attempts to guess.
- [X] Detail which bugs you found.
   During the debugging process, I found a couple of bugs:
      1. The guessing hint being reversed. For example, if I were to guess 56 when the secret number is actually 45, I would be told that my guess is too low. Vice versa, guessing 33 would tell me my gueess is too high.
      2. The secret number being unpurposely casted to a string. When the secret number is casted, it's being compared to the secret number lexiographically, rather than numerically. Sttrangely, this was only for even-numbered guesses.
      3. The very first guess not being recorded in the debugging log until the player makes their second guess. This is caused by the debugging log being rendered in streamlit first, before the first guess is recorded by the user.
- [X] Explain what fixes you applied.
      1. For the guessing hints being reversed, we simply reversed the logical conditions on what the hints should print out. When guess is lower than the secret number, the hint is to display "Go HIGHER", while a guess that is higher than the secret number is to display "GO LOWER".
      2. The condition block that was converting secret to a string on even-numbered attempts was removed. It was replaced with a one-liner, where the secret is always passed to the check_guess() function as an integer.
      3. The order of the rendering was changed. Claude discovered that it would be efficient to place recording the guess first before streamlit could render the debugging log on the website.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters the value 89 ->  Game does not specify "Too High" nor "Too Low", and guessed correctly
3. User checks "Show hint" box
3. User enters a guess of 75
4. Game Returns "Too Low"
5. User enters a guess of 34
6. Game Returns "Too High"
7. User enters a guess of 67
8. Game ends, telling user they got the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here:
platform darwin -- Python 3.12.10, pytest-9.0.3, pluggy-1.6.0
rootdir: /Users/chickphila/Desktop/CodePath/Summer2026/ai-110/projects/project1/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.9.0
collected 5 items                                                                                                                                                       

tests/test_game_logic.py .....                                                                                                                                    [100%]

=========================================================================== 5 passed in 0.01s ===========================================================================
```


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
