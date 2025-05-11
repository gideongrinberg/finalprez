notes = []
with open("./finalprez.qmd") as f:
    lines = iter(f.readlines())
    for line in lines:
        if line.startswith("::: {.notes}"):
            buffer = []
            line = next(lines)
            while not line.startswith(":::"):
                if line != "":
                    buffer.append(line)
                line = next(lines)
            notes.append(buffer)

with open("speaker_notes.txt", "w") as f:
    for note in notes:
        f.write("# Speaker Note\n")
        for line in note:
            f.write(line)
        f.write("\n")
