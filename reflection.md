# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  - Attempts count is already set to 1 upon launching the game
    - Causes initial attempts count to be one attempt less, than the initial attempt count for each difficulty. I suspect this could be part of a 0-indexing issue
  - No hint shows up upon clicking "Show Hint". 
  


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Clicked on Submit Guess on first guess | Would be told to go higher, lower, or correct guess | Was told to go higher, BUT the first guess was not recorded in the index history | None |
|Made another guess after the first guess (corresponding to the first bug) | Recorded this guess, while maintaining correct order of guesses | The very first guess (see bug above) was recorded instead of this guess | None |
|Guess of 101 on Medium Difficulty, range 1-100 | Out of bounds error | Given wrong guess, just as any other incorrect value | None |
|Checked the "Show Hint" box | a box, change in UI, or a pop-up would appear | no activity whatsoever | None |
|Switched from Medium (1-100 range) to Hard (1-50) difficulty | The UI would tell me to make a guess between numbers 1 to 50 | Secret number isn't in range | None |
|Guessed, 4, 3, 2, and 1 as being told to guess lower | 1 would be the secret number, so guessing 1 would win the game | Was told to guess even lower. It would be out of bounds error because 1 is the minimum value we can guess | None |
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
