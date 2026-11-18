import os

TEXT = """The kettle ticks, smaller each time.
The hallway lamp is left low.
On the folded laundry, the cat
has pressed a warm, uneven dent.

Frost gathers at the window's edge,
slow as a thought arriving late.

No door closes. One spoon waits in the sink.
The clock's thin hand moves without a sound.

Down the street, the last kitchen dims.
The frost keeps spreading, leaf by quiet leaf,
till the glass holds a small white field."""

path = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
with open(path, "wb") as f:
    f.write(TEXT.encode("utf-8"))
