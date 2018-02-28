# microbit-badge

Use **micro:bit** as conference badge, showing owner's name and topics of interest.

## How to use

The **micro:bit** scrolls owner's name continuously.

When owner presses "A", two things happen:

1. own badge displays all topics of interest.

2. nearby badges display matching topics of interest.

Owner's name is always displayed in uppercase.

Topics are displayed in mixed case, with a `#` prefix.


## How to configure

1. Flash `experiments/getid.py` on each **micro:bit** to discover its device id. It's a hex number, but it can be negative...

2. Edit the `people` dictionary in `badge_topics.py` with each **micro:bit** id, the owner's name and a list of topics of interest.

3. Flash `badge_topics.py` on all **micro:bit**s.

