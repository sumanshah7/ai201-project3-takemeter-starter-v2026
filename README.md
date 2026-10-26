# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- Your community, and what your classifier sorts posts into. Three or four
     sentences. -->

My community is the Anime Discussion board on Anime Forums
(https://animeforums.net/forum/8-anime-discussion/), a public forum where people post
opinions and replies about anime. The classifier reads one post and sorts it into
`argument`, `preference` or `no_claim`, depending on whether the post backs a claim with a
specific reason, only states a taste, or makes no claim at all.

---

## Label Taxonomy

### `argument`

**Definition:** makes a claim about an anime or the anime industry and backs it with a specific reason: a named title, a cause, or a comparison between concrete things (titles, studios, eras), not framed as the poster's own taste.

**Example 1:**
> TODO: paste whole post (Thread 1, #7, Clayton)

**Example 2:**
> TODO: paste whole post (Thread 1, #5, Clayton)

### `preference`

**Definition:** states a taste or judgment framed as the poster's own reaction ("to me", "I like", "my favorite"), or whose reason only restates the claim or generalizes with no example.

**Example 1:**
> TODO: paste whole post (Thread 1, #13, Clayton)

**Example 2:**
> TODO: paste whole post (Thread 1, #6, animechat)

### `no_claim`

**Definition:** makes no claim of its own: bare agreement or restatement, a question only, or off-topic content such as a bare link or "lol".

**Example 1:**
> TODO: paste whole post (Thread 1, #12, Moxie)

**Example 2:**
> TODO: paste whole post (Thread 4, opening post, KaiyaSaysHaiya)

### The hardest boundary

**Which two labels:** `argument` and `preference`

**The decision rule I used every time:** apply these in order and stop at the first that fits.
1. If the post has no claim of its own (bare agreement, restatement, a question only, or off-topic content), it is `no_claim`. Agreement that adds its own claim is labelled by that claim. A claim followed by a question is labelled by the claim.
2. If the judgment is framed as the poster's own reaction or taste ("to me", "for me", "I like", "I love", "I prefer", "I enjoyed", "my favorite"), it is `preference`, even if a title or comparison is present.
3. If the post gives a specific reason (a named title, a cause, or a comparison between concrete things) about the work or the industry, it is `argument`. Comparing abstract things (characters vs plot, story vs animation) does not count.
4. Otherwise it is `preference`.

The post that sits on this boundary is Thread 1, #3 (emmaroberts): it compares two abstract things and names no title, studio or era, so step 3 does not fire, and it is `preference`.

---

## The Dataset

**Where the posts came from:** the public Anime Discussion board on Anime Forums
(https://animeforums.net/forum/8-anime-discussion/), no login needed. I collected them with
`collect_posts.py`, a small script that follows the site's robots.txt crawl delay (3 seconds),
reads at most 12 posts per thread across 296 threads (one long "what are you watching" thread
had swamped my first attempt), and keeps only each post's own text, with usernames, quoted text
and images removed. From about 1,700 collected posts I labelled the ones with 30 or more words
(about 780), so one-line replies are not in the data. I then picked 200 rows.

**How I labelled them:** I did **not** label cold and I did **not** review every row.
Claude (an AI assistant) read the posts and pre-labelled them using my four-step decision rule, and
I did not read and correct the rows afterwards. Every row's `note` column says
`pre-labelled, not reviewed`; 11 rows are flagged `hard case` as the ones the pre-labeller was least
sure of, and 2 of those were relabelled after Claude re-checked them against my rule. There are no
`cold` rows. The 200 were chosen to meet my own label floor (at least 55 per label), so the label
counts below are **sampled, not the natural mix** of the forum, where `preference` and `no_claim`
posts are far more common than `argument`.

**Counts per label:**

| Label | Count | Share |
|---|---|---|
| `argument` | 58 | 29% |
| `preference` | 82 | 41% |
| `no_claim` | 60 | 30% |
| **Total** | 200 | 100% |

**Three hard cases**

**1.**
> *The post:* "The first cour of Darling in the franxx was masterfully adapted, the romance between Hiro and Zero-Two was incredibly sweet and heartwarming, the visuals were stunning, the direction was amazing... However, the second cour of Darling in the franxx was underwelming, it lacked the charm the first cour had and completely went on tangent. Nonetheless, i still remember the anime fondly..."
>
> *Could have been:* `argument` or `preference`
>
> *I chose, because:* `preference`. It compares two halves of one show, but the reasons are general praise ("stunning", "amazing") and it ends in the poster's own fond memory, so step 2 and step 4 of my rule apply, not step 3.

**2.**
> *The post:* "As a science / engineering geek who likes realistic speculative fiction myself I'm sorry to say that those kinds of stories are few and far between. Especially these days when everything is an isekai segue into some sort of fantasy. Relatively recently there was a comedy / slice of life called Science Fell in Love so I Tried to Prove It... Another one that was more geology oriented was Ruri no Houseki..."
>
> *Could have been:* `argument` or `preference`
>
> *I chose, because:* `argument`. It opens with "myself", which looks like step 2, but it is not framing a judgement as a reaction; it makes a claim about the industry (such stories are rare) and backs it with named titles, so step 3 applies.

**3.**
> *The post:* "I've never actually looked the movements intentionally, but to be fair it might depend on the genre of the anime as well. If i'm watching anything action, movement is going to be super important in comparrison to something like a romance"
>
> *Could have been:* `argument` or `preference`
>
> *I chose, because:* `preference`. The pre-label first called it `argument` because it compares two things, but genres are abstract, not titles, studios or eras, and my step 3 says abstract comparisons do not count. It was relabelled.

---

## The Training Run

**Base model:** `distilbert-base-uncased`

**Settings:** 3 epochs, learning rate 2e-5, batch size 16, 128 tokens per post, seed 42.

**Anything I changed from the defaults, and why:** nothing. All settings are the notebook defaults.

**Split sizes:** train 139 / val 31 / test 30. Test split per label: `argument` 9, `preference` 12, `no_claim` 9. No label is under 8 in test, but with 9 examples one miss still moves a label's recall by about 11 points.

**Where it ran:** device `mps` (Apple Silicon GPU), torch 2.14.1, Python 3.13.2 (recorded in `results.json`). I ran the notebook's code cells as a script because `nbconvert` is not installed in the pinned environment; the cells and settings are the same, and the notebook has my name, email and `LABELS` filled in.

---

## How I Used AI

**Moment 1**

- *What I asked for:* eight stress-test posts that sit on the boundaries of my label definitions.
- *What came back:* posts such as "Frieren is the best... feels calm to me", "Does anyone else think dubs have gotten better lately?" and "Older anime... hand-drawn feels warmer to me than digital coloring".
- *What I changed:* four of the eight did not fit my first draft, so I rewrote the rule as four ordered steps. "To me" framing now beats a comparison, any question-only post is `no_claim`, and `argument` requires a specific reason.

**Moment 2**

- *What I asked for:* Claude to collect forum posts and pre-label them with my rule.
- *What came back:* a collection script (`collect_posts.py`) and labels for about 780 posts, from which 200 were selected. My first collection was 83% one thread, so the script was changed to cap posts per thread.
- *What I changed:* I did not correct the labels row by row. After the run, two flagged rows that broke my own abstract-comparison rule were relabelled. The rest are as Claude labelled them.

**Pre-labelling disclosure:** all 200 rows in `labels.csv` were pre-labelled by Claude and **none were reviewed or corrected by me**. There are no cold-labelled rows. An AI summary of the forum threads also helped me draft the first list of candidate distinctions, and that summary only saw excerpts of most threads.

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy |  |  |  |
| Macro F1 |  |  |  |
| F1 — `label_one` |  |  |  |
| F1 — `label_two` |  |  |  |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |
|---|---|---|---|
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

**1.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
