# Acceptance criteria — TakeMeter

Five criteria that say what "working" means for this classifier, written in
unit 5 **before** anything was trained.

**All five are yours this time.** None are given. You've had two projects of
practice.

An acceptance criterion names a number. *"The model is accurate"* is an
opinion. *"Every label has an F1 of at least 0.60 on the held-out set"* is a
criterion.

Under each, write a sentence or two on **why that number**. A reason that says
something about your data or your taxonomy earns credit — *"I picked 0.60 F1
for `reaction` because it's my smallest label and I only have about 50
examples of it"*. A reason that could be attached to any project does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

Not numbers that sound impressive. Three labels means a coin-flip guesser gets
about 33%, so a target of 0.40 is barely a target. Your number should sit
somewhere you'd honestly call useful.

**Cover at least three of these five areas.** They're here as prompts, not as a
form to fill in — a criterion that fits none of them is fine if it names a
number.

| Area | A question it could answer |
|---|---|
| Overall accuracy | How often does it need to be right to be worth using? |
| Per-label performance | Is one label allowed to be much worse than the others? |
| Balance | How lopsided can your label counts get before it's a problem? |
| Consistency | If someone else labelled the same posts, how often should you agree? |
| Confidence | Should a confident prediction be right more often than an unsure one? |

Two things worth knowing before you pick numbers, because both will affect
whether you hit them:

- **Your smallest label will have the jumpiest score.** If a label has 50
  examples, about 8 land in the test split. An F1 computed on 8 examples moves
  a lot between seeds. A target for that label should be looser than one for
  your biggest label, and saying so is a good reason.
- **Unit 6 tests across three seeds, and the target has to hold across all
  three.** A target of 0.65 against results of 0.71, 0.62, 0.68 is a **miss**.
  Pick with that in mind — it is stricter than it first sounds.

---

## 1. Overall accuracy, at least 0.70

Measured on the held-out test split, in each of the three seeds (all three must pass).

**Why this target:** with the label floor in criterion 4, the largest label is at most 45% of
labels.csv, so always guessing it scores about 0.45 and chance is 0.33. 0.70 clears both by
a wide margin.

---

## 2. Macro F1 across the three labels, at least 0.60

Measured on the held-out test split, in each of the three seeds (all three must pass).

**Why this target:** accuracy alone can reward leaning on the biggest label. Macro F1 weights
argument, preference and no_claim equally, so a model that ignores one of them fails.

---

## 3. F1 on the smallest label, at least 0.50

The smallest label is the one with the fewest rows in labels.csv. Measured on the held-out
test split, in each of the three seeds (all three must pass).

**Why this target:** in my 40-post tally the smallest label (no_claim) was 12.5%. Below 0.50
the model misses that label more often than it finds it. With about 8 test examples, one
miss moves recall by about 12 points, so I set this lower than criterion 2.

---

## 4. Every label has at least 55 rows in labels.csv (of 200)

Counted directly from labels.csv.

**Why this target:** with a 70/15/15 split, 55 rows puts about 8 in the test split, the
minimum the assignment gives for stable per-label metrics. My tally had no_claim at
12.5% (about 25 of 200), so I will collect about 30 more no_claim posts. One-liners and
question-only posts are common on this forum, so that's realistic.

---

## 5. Self-agreement on a blind relabel, at least 85% (26 of 30)

30 rows drawn at random from labels.csv with a fixed seed, relabeled at least 24 hours
later with the label column hidden. Agreement is exact match on the label.

**Why this target:** my hardest boundary (argument vs preference, post #3) needed a four-step
rule. If I can't apply it the same way twice, the model learns my inconsistency, not the labels.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 6 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Every label performs acceptably

         The model performs well on all labels.

         **Why this target:** ...

         > **Revised in unit 6:** Every label has an F1 of at least 0.60 on
         > the held-out set.
         >
         > **Why revised:** "performs well" gave me nothing to check. I
         > couldn't produce a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "Overall accuracy of at least 0.65" → "at least 0.55", because
            0.65 turned out to be optimistic for 200 examples.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
