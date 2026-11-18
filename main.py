import os

TEXT = """Kettle ticks, smaller.
Hall lamp low.
Folded laundry keeps
the cat's warm dent.

Frost gathers at the window's edge,
slow as a shadow on the floor.

No door shuts. One spoon waits.
The clock hand turns without sound.

Down the street, a kitchen dims.
It spreads, leaf by leaf,
till the glass holds a small white field
that grows on in the dark, unseen."""

path = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
with open(path, "wb") as f:
    f.write(TEXT.encode("utf-8"))
