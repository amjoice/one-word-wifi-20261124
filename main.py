#!/usr/bin/env python3
"""One Word for Your Wi-Fi.

Writes one word describing home Wi-Fi to /output/entry.txt.

Stdlib only: the grading sandbox is plain python:3.13-slim, no Pillow,
no network. The program is deterministic: the same word every run.

The word was picked against the published judge brief, not as a first
draft. The brief weighs, in order: on-subject fit, a laugh at once,
truth about how home Wi-Fi actually behaves, a fresh angle, and a
single word that needs no context. Candidates weighed:

- "Buffering" -- the first word everyone reaches for. True, but stale;
  it loses criterion 4 before the game starts.
- "Ghosting" -- true (the signal vanishes without explanation) and
  short, but it is common slang now and several entrants will pick it.
- "Moody" -- short and funny, but generic; it could describe anything.
- "Situationship" -- funny on-again-off-again energy, but it describes
  a relationship pattern and needs a beat to land on Wi-Fi.
- "CommitmentIssues" -- funny and true, but it reads as two words
  jammed together, weak on the single-word criterion.
- "Gaslighting" -- the winner. Your router shows full bars and says
  "Connected" while nothing loads: it insists everything is fine while
  it plainly is not. That lie is the most recognisable home-Wi-Fi
  experience there is, it is funny the instant you read it, no other
  entrant's obvious word takes that angle, and as a network name it is
  perfect: the SSID itself is the joke.

"Gaslighting" is 11 characters, inside the 1-20 gate, one clean word,
no trailing newline (fewer bytes also wins a size tie-break).
"""

import os

# Each candidate scored 0-5 on the judge brief's criteria, in order:
# on-subject fit, laugh at once, true to home Wi-Fi, fresh angle,
# works as one word with no context. The winner is the highest total;
# ties break to the shorter word, then alphabetically, so the pick is
# deterministic.
CANDIDATES = {
    "Buffering": (5, 2, 4, 1, 5),
    "Ghosting": (5, 3, 4, 3, 5),
    "Moody": (4, 3, 3, 3, 5),
    "Situationship": (4, 4, 4, 4, 4),
    "CommitmentIssues": (4, 4, 4, 4, 3),
    "Gaslighting": (5, 5, 5, 5, 5),
}


def pick_word(candidates):
    """Return the strongest candidate word, deterministically.

    Highest total score wins; ties break to the shorter word, then to
    the alphabetically first, so the same candidates always pick the
    same word.
    """
    ranked = sorted(
        candidates.items(),
        key=lambda item: (-sum(item[1]), len(item[0]), item[0]),
    )
    return ranked[0][0]


def main() -> None:
    word = pick_word(CANDIDATES)
    assert 1 <= len(word) <= 20, f"word must be 1-20 chars, got {len(word)}"
    assert word == word.strip() and " " not in word, "word must be one clean word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(word)
    print(word)


if __name__ == "__main__":
    main()
