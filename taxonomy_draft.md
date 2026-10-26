# Milestone 2 draft: label taxonomy

Candidate distinctions I'm building from (see notes.md): names a title, gives a reason,
adds a point to a quoted post.

## Labels
Names are lowercase with underscores and must match LABELS in the notebook and labels.csv exactly.

### argument
Definition: makes a claim about an anime or the anime industry and backs it with a specific
reason: a named title, a cause, or a comparison between concrete things (titles, studios, eras).
Example post 1: Thread 1, #7 (Clayton): taboo-breaking drives popularity, Harry Potter as the comparison
[PASTE WHOLE POST]
Example post 2: Thread 1, #5 (Clayton): explains a cause, early anime doing what US cartoons avoided
[PASTE WHOLE POST]

### preference
Definition: states a taste or judgment that is framed as the poster's own reaction, or whose
reason only restates the claim or generalizes with no example.
Example post 1: Thread 1, #13 (Clayton): wishes for new ideas and better villains, no example
[PASTE WHOLE POST]
Example post 2: Thread 1, #6 (animechat): one-line generalization about creative freedom
[PASTE WHOLE POST]

### no_claim
Definition: makes no claim of its own: bare agreement or restatement, any post whose only
content is a question, or off-topic content such as a bare link or "lol".
Example post 1: Thread 1, #12 (Moxie): repeats the money-over-enjoyment point already made
[PASTE WHOLE POST]
Example post 2: Thread 4, opening post (KaiyaSaysHaiya): neutral question about what matters
[PASTE WHOLE POST]

## Hardest boundary
Post: Thread 1, #3 (emmaroberts), https://animeforums.net/topic/17178-makes-an-anime-truly-memorable/
[PASTE WHOLE POST]

Between: argument and preference

Decision rule, applied in this order, stop at the first that fits:
1. If the post has no claim of its own (bare agreement, restatement, a question only, or
   off-topic content), it is no_claim. Agreement that adds its own claim is labeled by that
   claim. A claim followed by a question is labeled by the claim.
2. If the judgment is framed as the poster's own reaction or taste ("to me", "for me",
   "I like", "I love", "I prefer", "I enjoyed", "my favorite"), it is preference, even if a
   title or comparison is present.
3. If the post gives a specific reason (a named title, a cause, or a comparison between
   concrete things) about the work or the industry, it is argument. Comparing abstract
   things (characters vs plot, story vs animation) does not count.
4. Otherwise it is preference.

Applied to #3: it compares two abstract things and names no title, studio or era, so step 3
does not fire. Its closing question doesn't change that (step 1: claim + question goes by the
claim). Label: preference.

## Stress test
1. "Frieren is the best... feels calm to me": preference (step 2)
2. "Agreed, season two was better. Studio change made a big difference.": argument (adds a claim with a specific cause)
3. "Sports anime drag... stretch tournament arcs... Haikyuu gets away with it": argument
4. "Does anyone else think dubs have gotten better lately?": no_claim (question only)
5. "Dropped Black Clover after 20 eps, Asta's yelling was too much for me": preference (step 2)
6. "Yeah exactly, like you said, studios only care about money": no_claim
7. "Long series are worse than short ones. They always lose the plot.": preference (no specific reason)
8. "Older anime... hand-drawn feels warmer to me than digital coloring": preference (step 2 beats the comparison)

Which ones I couldn't classify cleanly, and what I changed: 2, 4, 7 and 8 didn't fit the first draft.
- argument now requires a SPECIFIC reason (title, cause, or concrete comparison), which moved #7 out.
- Own-reaction framing marks preference even when a comparison is present (#8).
- Agreement plus a new claim is labeled by the claim (#2).
- Any question-only post is no_claim (#4). Dropped the "presupposed view" split as too
  hard to apply consistently.

## If I dropped a label
adds_to_quote: describes how a post relates to another post, not what it does. A reply can
add a new point that is still preference (#10), so it overlaps the other labels.
off_topic_media: only 4 of 40 posts, and a link or image says nothing about whether the text
is argued. Off-topic content now goes to no_claim; links inside a real post are ignored.

## Check before Milestone 4
Provisional tally of my 40 posts under the rule above (Threads 2-7 were excerpts, recount
after fixing notes.md):
argument: 10 (25%)   preference: 25 (62.5%)   no_claim: 5 (12.5%)
Under 70%, but close. When collecting to 200, target threads with replies and debates
(reviews, unpopular opinions, AI characters) to raise argument and no_claim.

Note: step 2 includes "my favorite" and "I enjoyed" because favorite-character posts
(#25-27) and first-person reviews (#14) otherwise slipped into argument just by naming a title.
