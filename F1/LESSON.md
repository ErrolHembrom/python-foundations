# Week F1: Python basics, if-else and loops (23–29 Nov 2026)

**Book:** *Automate the Boring Stuff with Python*, 3rd edition, chapters 1–3:
- Ch 1 Python Basics: https://automatetheboringstuff.com/3e/chapter1.html
- Ch 2 if-else and Flow Control: https://automatetheboringstuff.com/3e/chapter2.html
- Ch 3 Loops: https://automatetheboringstuff.com/3e/chapter3.html

**By Saturday you'll be able to:** do maths and work with text in Python, ask the user for input, make decisions with `if`/`elif`/`else`, and repeat things with `while` and `for` loops.

**Every day (about 2 hours):**
1. **Read (30 min):** the book section listed for the day. Type every example into VS Code yourself. Don't copy and paste.
2. **Learn the differences (10 min):** read today's "JavaScript vs Python" box below.
3. **Practise (60 min):** open today's file in `F1/exercises/`. Each one has instructions and the expected output in comments at the top. Write your code under the instructions.
4. **Commit (10 min):** save to GitHub (commands at the bottom of this page), then tell Claude **"review day N"**. Claude reads your file and gives feedback. Claude won't write the answers for you.

**When you're stuck:**
1. Read the error message's **last line** first. It usually names the problem.
2. Paste your code into https://pythontutor.com/ to watch it run line by line.
3. Still stuck after 15 minutes? Ask Claude, and include the code and the full error.

The prices in this week's exercises are **made-up practice numbers**, not real vendor prices.

---

## Day 1 (Mon 23 Nov): numbers, text and variables

**Read:** Ch 1 from the start up to and including "Storing Values in Variables".

| Idea | JavaScript | Python |
|---|---|---|
| Make a variable | `let seats = 5;` | `seats = 5` (no `let`/`const`, no semicolon) |
| Variable names | `monthlyCost` (camelCase) | `monthly_cost` (snake_case is the Python style) |
| Comment | `// note` | `# note` |
| Divide | `7 / 2` gives `3.5` | `7 / 2` gives `3.5` (same) |
| Divide and round down | `Math.floor(7 / 2)` | `7 // 2` gives `3` |
| Remainder | `7 % 2` | `7 % 2` (same) |
| Power | `2 ** 3` | `2 ** 3` (same) |
| Add 1 | `seats++` | `seats += 1` (Python has no `++`) |
| Repeat text | `"ab".repeat(3)` | `"ab" * 3` gives `"ababab"` |

**The big trap:** JavaScript quietly joins a number and text, so `5 + "3"` gives `"53"`. Python refuses: `5 + "3"` gives **`TypeError`**. You must convert first, with `str(5) + "3"` or `5 + int("3")`. Python is stricter on purpose, so mistakes show up early.

**Practise:** `F1/exercises/day1_costs.py`

---

## Day 2 (Tue 24 Nov): print, input and f-strings

**Read:** Ch 1 from "Your First Program" to the end of the chapter.

| Idea | JavaScript | Python |
|---|---|---|
| Print | `console.log("Hi")` | `print("Hi")` |
| Put values in text | `` `Total: ${total}` `` | `f"Total: {total}"` |
| Two decimal places | `total.toFixed(2)` | `f"{total:.2f}"` |
| Thousands comma | `total.toLocaleString()` | `f"{total:,.2f}"` gives `1,234.50` |
| Ask the user | `prompt("Seats?")` (browser) | `input("Seats? ")` |
| Text length | `name.length` | `len(name)` |
| Text to whole number | `parseInt("5")` | `int("5")` |
| Text to decimal | `parseFloat("4.5")` | `float("4.5")` |
| Number to text | `String(5)` | `str(5)` |

**The trap:** `input()` **always gives back text**, even when the user types a number. `input()` then `+ 1` crashes. Convert first: `seats = int(input("Seats? "))`.

**Practise:** `F1/exercises/day2_quote.py`

---

## Day 3 (Wed 25 Nov): True/False and if-else

**Read:** Ch 2, the whole chapter.

| Idea | JavaScript | Python |
|---|---|---|
| Booleans | `true` / `false` | `True` / `False` (capital letter) |
| Nothing | `null` | `None` |
| Equal | `===` | `==` (there's no `===`) |
| Not equal | `!==` | `!=` |
| And / or / not | `&&` `\|\|` `!` | `and` `or` `not` (plain words) |
| Between | `x > 1 && x < 10` | `1 < x < 10` also works |
| Blocks | `{ ... }` braces | a colon `:` then **4 spaces of indentation** |
| Else-if | `else if` | `elif` |

```python
if seats <= 5:
    print("Starter plan")
elif seats <= 20:
    print("Team plan")
else:
    print("Business plan")
```

**The trap:** indentation **is** the code in Python, not just style. If the lines inside an `if` aren't indented the same way, you get `IndentationError`. VS Code adds 4 spaces when you press Tab, so let it.

**Practise:** `F1/exercises/day3_plan_check.py`

---

## Day 4 (Thu 26 Nov): while loops

**Read:** Ch 3, the "while Loop Statements" section (it includes `break` and `continue`).

| Idea | JavaScript | Python |
|---|---|---|
| While loop | `while (x < 10) { ... }` | `while x < 10:` plus an indented block |
| Loop forever | `while (true)` | `while True:` |
| Stop the loop | `break` | `break` (same) |
| Skip to next round | `continue` | `continue` (same) |
| Is this text a whole number? | `/^\d+$/.test(s)` | `s.isdecimal()` |

A pattern you'll use often: keep asking until the answer is valid.

```python
while True:
    text = input("How many seats? ")
    if text.isdecimal():
        break
    print("Please type a whole number.")
seats = int(text)
```

**Practise:** `F1/exercises/day4_ask_until_valid.py`

---

## Day 5 (Fri 27 Nov): for loops and range()

**Read:** Ch 3 from "for Loops and the range() Function" to the end of the chapter.

| Idea | JavaScript | Python |
|---|---|---|
| Count 0 to 4 | `for (let i = 0; i < 5; i++)` | `for i in range(5):` |
| Count 1 to 10 | `for (let i = 1; i <= 10; i++)` | `for i in range(1, 11):` (the end number is **not** included) |
| Count by 5s | `for (let i = 0; i < 50; i += 5)` | `for i in range(0, 50, 5):` |
| Print without a new line | `process.stdout.write(...)` | `print(..., end="")` |

**The trap:** `range(1, 10)` stops at **9**. To include 10, write `range(1, 11)`.

**Practise:** `F1/exercises/day5_cost_table.py`

---

## Saturday (28 Nov, about 3 hours): mini-project and weekly review

**Mini-project:** `F1/exercises/sat_plan_picker.py`. It uses everything from the week: input, conversion, if/elif/else, a validation loop, a `for` loop and f-strings.

Then say **"weekly review"**. Claude checks every file, updates [the tracker](../../../skills-roadmap/TRACKER.md) and sets up week F2 (functions, debugging, lists).

**Sunday 29 Nov:** off.

---

## Saving your work to GitHub (every day)

In VS Code's terminal, inside `python-foundations`, run one at a time:

```bash
git add -A
```

```bash
git commit -m "F1 day 1: costs exercise"
```

```bash
git push
```

Change the message each day ("F1 day 2: quote", and so on). If `git push` shows an error, screenshot it and send it to Claude.

## Week F1 done when
- [ ] days 1–5 exercises run and print the expected output
- [ ] the Saturday plan picker works, including rejecting bad input
- [ ] at least 6 commits on GitHub this week
- [ ] you can explain the difference between `"5" + "3"`, `5 + 3` and `5 + "3"` in Python
