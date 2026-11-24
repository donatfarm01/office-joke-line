# Build notes — One-Line Office Joke

The bounty asks for one short joke about office life, at most two hundred
characters, judged by a model that compares entries two at a time. The
judge weighs, in order, whether the text is a one-line joke about office
life, whether it is funny, whether it reads as one line, whether it is
fresh, and whether it is clear on first read. Those five tests shaped
every choice below.

The first draft was about a calendar full of meetings about meetings. It
was written, run, and then rejected with the reason recorded in the
program itself. Meetings about meetings is a complaint every office
worker has already made and heard, so it has no surprise and no
punchline, and it fails the freshness test outright. A line that only
repeats a shared gripe loses to any real joke, so the draft was thrown
out rather than polished.

The final line was picked for one device: a single word doing double
duty. A standing desk is a reasonable request, and a standing meeting
is the bureaucratic answer that sounds helpful while giving nothing.
The word standing carries the setup into the punchline, so the joke
needs no second sentence and no explanation. It names two specific
office objects instead of a generic feeling, which keeps it fresh, and
it reads as one plain sentence, which keeps it clear.

The program is deliberately tiny. One constant holds the line, one
validation step refuses anything outside one to two hundred characters,
anything spanning more than one line, or anything with leading or
trailing whitespace, and one write puts it in the output file with no
trailing newline. Two runs in a row produce byte-identical output, so
the entry is deterministic. Nothing is read from the network, no secret
is used, and the entry depends on nothing outside its own repository.
