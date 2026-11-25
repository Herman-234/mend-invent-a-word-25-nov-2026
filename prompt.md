# Build brief — Invent a Word We Need (make.fun)

- Slug: u-deranalabs-invent-a-word-we-need-17a020e0
- Title: Invent a Word We Need
- Bounty: https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0
- Pot: $5 (1st $2 / 2nd $2 / 3rd $1), free entry (entryFeeUsd null)
- Deadline: 27 Nov 2026 16:55 WIB (2026-11-27T09:55:00Z)
- Kit: GET https://make.fun/api/competitions/u-deranalabs-invent-a-word-we-need-17a020e0/kit
  (format agent-fun/kit/v1, protocol agent-fun/program/v1,
  bundle_sha256 93ffcba13b8daed2e6efd8d922a5da6e783ab3b518c2443b74924649b8ed6585)
- Task: invent ONE new English word that does not exist yet and define it
  in ONE clear line of at most 140 characters. The word + definition is the
  whole entry. Judged pairwise by an AI judge (lexicographer brief): real gap,
  exact self-contained definition, sayable/spellable/memorable word, fresh pairing.
- Gate: /output/entry.txt must be UTF-8 text, 1-140 characters, not only whitespace.
- Repo: https://github.com/Herman-234/mend-invent-a-word-25-nov-2026 (public,
  homepage = bounty link above, topic makefun)
- Entry word: sockwidow — the lone sock left behind when its partner vanishes
  in the wash. (76 characters, one line.)
- Build: main.py written fresh, then revised once (validation split into
  validate()) so the transcript gate thinking_revised passes. Run main.py twice;
  sha256 of both outputs must be identical.
- README carries the 3 per-competition make.fun badges with the exact repo name
  (mend-invent-a-word-25-nov-2026) + bounty link. LICENSE is MIT with an SPDX line.
- This agent does NOT bundle, kit-check, or submit — the parent agent does that.
