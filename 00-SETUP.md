# Stage 0: Set-up (22 Nov 2026)

Claude checked your Mac first. Most of it is already done:

| Item | Status |
|---|---|
| Python | ✅ Python 3.13.5 (installed with Anaconda, at `/opt/anaconda3/bin/python3`) |
| VS Code | ✅ installed as **"Visual Studio Code 2"** in Applications (there's an old copy in Downloads too; ignore it) |
| VS Code Python extension | ✅ Microsoft's Python extension is installed |
| Git | ✅ installed (version 2.50.1) |
| GitHub account | ✅ ErrolHembrom, already signed in on this Mac |
| Git name and email | ❌ **not set**: step 1 below |
| `python-foundations` repo | ❌ **not created**: step 4 below |

About 20–30 minutes in total.

---

## Step 1: Tell Git who you are (2 minutes)

Every commit is stamped with a name and an email, and Git refuses to commit until you set them.

To keep your real email private on a public repo, use GitHub's **no-reply address**:
1. On github.com, go to **Settings**, then **Emails**.
2. Tick **Keep my email addresses private**.
3. Copy the address shown, which looks like `12345678+ErrolHembrom@users.noreply.github.com`.

Then run these in Terminal, with your own name and the no-reply address:

```bash
git config --global user.name "Your Name"
```

```bash
git config --global user.email "PASTE-NOREPLY-ADDRESS-HERE"
```

> **JS comparison:** this is like a global setting in `~/.npmrc`. You set it once for the whole computer.

## Step 2: Make your learning folder the VS Code workspace (3 minutes)

1. Open **Visual Studio Code 2** from Applications.
2. Go to **File**, then **Open Folder…**, and choose `Downloads/Education/python-foundations`.
3. If VS Code asks "Do you trust the authors?", click **Yes** (it's your own folder).
4. Optional but handy: press **Cmd + Shift + P**, type `shell command`, and choose **Shell Command: Install 'code' command in PATH**. After that, `code .` in Terminal opens the current folder in VS Code.

## Step 3: Your first Python file (10 minutes)

1. In VS Code, create a new file called `hello.py` in this folder.
2. Type this yourself (don't paste it), using your own name:

```python
name = "Robert"
print(f"Hello, {name}! Python is ready.")
```

3. Click the ▶ (Run) button at the top right. The output appears in the terminal panel at the bottom.
4. Check which Python VS Code used: look at the bottom-right corner of the window. It should say **3.13.5**. If it says something else, click it and choose the one at `/opt/anaconda3/bin/python3`.

> **JS comparison:**
> | JavaScript | Python |
> |---|---|
> | `const name = "Robert";` | `name = "Robert"` (no `const`/`let`, no semicolon) |
> | `` console.log(`Hello, ${name}!`) `` | `print(f"Hello, {name}!")` (the `f` before the quotes works like backticks) |
> | `node hello.js` | `python3 hello.py` |

Try the same thing from Terminal too:

```bash
cd ~/Downloads/Education/python-foundations && python3 hello.py
```

## Step 4: Create the `python-foundations` repo on GitHub (10 minutes)

1. On github.com, click **+** at the top right, then **New repository**.
2. Name: `python-foundations`. Visibility: **Public**. Tick **Add a README file**. Click **Create repository**.
3. Connect your folder to it. In Terminal:

```bash
cd ~/Downloads/Education/python-foundations && git init && git branch -M main
```

```bash
git remote add origin https://github.com/ErrolHembrom/python-foundations.git
```

```bash
git pull origin main
```

```bash
git add hello.py && git commit -m "Set-up: first Python script" && git push -u origin main
```

If the push asks you to sign in, follow the browser prompt. This Mac's GitHub sign-in is already set up for the `gh` tool, so if `git push` complains about credentials, tell Claude.

> **What just happened:** `git init` makes the folder a Git project. `remote add` links it to GitHub. `pull` brings down the README GitHub created. `add`, `commit` and `push` save `hello.py` and upload it, like saving a file and then syncing it.

**Keep out of GitHub:** this folder's lesson files are fine to share. Never commit passwords or API keys (that matters from Project 3).

## Step 5: Read the book's Introduction (15 minutes, optional today)

*Automate the Boring Stuff with Python*, 3rd edition, Introduction: https://automatetheboringstuff.com/3e/chapter0.html

---

## Done when
- [ ] `git config --global user.name` prints your name
- [ ] `hello.py` runs from VS Code and from Terminal
- [ ] github.com/ErrolHembrom/python-foundations shows `hello.py`

Then tell Claude **"set-up done"**. Claude checks it from here and ticks it off in the tracker. On Monday 23 Nov, say **"start week F1"**.
