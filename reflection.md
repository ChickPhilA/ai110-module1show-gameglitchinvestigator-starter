# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
    Attempts count is already set to 1 upon launching the game
      Causes initial attempts count to be one attempt less, than the initial attempt count for each difficulty. I suspect this could be part of a 0-indexing issue
    No hint shows up upon clicking "Show Hint". 
  
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Clicked on Submit Guess on first guess | Would be told to go higher, lower, or correct guess | Was told to go higher, BUT the first guess was not recorded in the index history | None |
|Made another guess after the first guess (corresponding to the first bug) | Recorded this guess, while maintaining correct order of guesses | The very first guess (see bug above) was recorded instead of this guess | None |
|Guess of 101 on Medium Difficulty, range 1-100 | Out of bounds error | Given wrong guess, just as any other incorrect value | None |
|Checked the "Show Hint" box | a box, change in UI, or a pop-up would appear | no activity whatsoever | None |A
|Switched from Medium (1-100 range) to Hard (1-50) difficulty | The UI would tell me to make a guess between numbers 1 to 50 | Secret number isn't in range | None |
|Guessed, 4, 3, 2, and 1 as being told to guess lower | 1 would be the secret number, so guessing 1 would win the game | Was told to guess even lower. It would be out of bounds error because 1 is the minimum value we can guess | None |

Since I found out that we only had to fix two bugs, the only bugs I focused on were fixing the bug where:
    1. Guessing 100, the max value that we could guess, (on Medium difficulty) would tell us to guess higher, despite the secret number being lower. There was a specific case to this due to string casting and comparing lexiographically instead of numerically
    2. Guessing a number that is higher than the secret number would display "TOO LOW", or guessing a number that is lower than the secret number would display "TOO HIGH". Different case than bug 1 above
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    I used Claude for VS Code on this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    An example of how Claude was correct was discovering in our code that the secret number was being parsed as a string, meaning that it wouldn't be possible to have accurate comparisons between two values. 100 would lexiographically be less than 80 because the leading value, 1, in 100 would be less than the leading value of 8 in 80. However, when we removed the parsing, I verified that the comparsions were numerical again, where guessing 100 finally told us "TOO HIGH".
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
    This was from another bug that I discovered but decided not to document here. A bug that the AI refactored and still was inaccurate was the Developer Debug Info not recording the first guess, where until upon sending our second guess, would finally record our first guess. What Claude initially suggested and refactored was wrapping the input and submit button within the form for atomic submission, and adjusting the attempts increment to fire only on valid guessing. I had to validate the fix by sending in my first guess again, and wrapping the submit and input buttons inside the form did not change much. The true bug was the debug menu being rendered before the first guess being submitted.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    I decided a bug was ultimately fixed by first, running it through the streamlit webpage. However, I thought just visually working as it should was not enough. I asked Claude to help me generate a test case to verify that under the hood, it also runs as intended, when being given that specific test case passed through pytest.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
    One test I ran was the secret number being too low or too high. This test case was made in respect to the secret number initially being parsed as a string, casuing a bug in comparing input values to the secret number. 100 was our test value here, because at first, when it was being lexiographically compared, '100' was less than the secret number (89 in this case), so debugging the parsing helped verify my test case to pass.
- Did AI help you design or understand any tests? How?
    Claude helped design and further comprehend my understandings of our test cases being wrote, knowing how values in general programming can be compared in different ways (lexiographically vs numerically)

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
    Every time you interact with a Streamlit app (ex: clicking a button, typing in a box), the entire script reruns from top to bottom. Without session state, every rerun would reset your variables to their starting values, losing things like your score or guess history. Session state is like a persistent memory that survives each rerun, so values you care about stick around between interactions. It's a similar concept to state in React, except Streamlit reruns the whole script instead of just re-rendering a component.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

    A habit I want to keep/reuse in future projects is delegating tasks with my AI agent, so that not one of us dominate the work in a project. I would say that I am happy with the amount of work that was distributed between Claude and I, where I identified and marked possible bugs and provided context, while Claude refactored code and we both made reviews together before anything could be changed. I also Claude to not make any changes unless I prompt that it's necessary to do so, so that it doesn't work ahead of me and only is constrained to work upon prompts I give it.

- What is one thing you would do differently next time you work with AI on a coding task?

    One thing I would do differently next time when I work with AI on a coding task is to provide the whole documentation to the AI agent, but not to work ahead of itself, so that we can both work on the same pace effectively, step-by-step. This also helps my AI agent know what would be worked on next, in advance.

- In one or two sentences, describe how this project changed the way you think about AI generated code.


    This project definetly highlighted the idea that AI code is not perfect, and almost will not be, as it created a broken game. However, the code that AI makes can be efficiently measured, based on how much context and constraint you provide it.
