# pass1.py — with error handling

def pass1(lines):
    MNT = {}
    MDT = []
    ALA = {}
    errors = []  # collect all errors here

    # ── Check empty file ──
    if len(lines) == 0:
        errors.append("ERROR: Input file is empty!")
        return MNT, MDT, ALA, errors

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue

        tokens = line.split()

        if tokens[0] == "MACRO":

            # ── Check enough tokens ──
            if len(tokens) < 2:
                errors.append(f"ERROR: Line {i+1} — MACRO keyword missing name!")
                i += 1
                continue

            macro_name = tokens[1]
            params = tokens[2:]

            # ── Check duplicate macro ──
            if macro_name in MNT:
                errors.append(f"ERROR: Line {i+1} — Duplicate macro definition '{macro_name}'!")
                i += 1
                continue

            # Store in tables
            MNT[macro_name] = len(MDT)
            ALA[macro_name] = params

            # Collect body
            i += 1
            found_mend = False
            while i < len(lines):
                body_line = lines[i].strip()
                if body_line == "MEND":
                    MDT.append("MEND")
                    found_mend = True
                    break
                MDT.append(body_line)
                i += 1

            # ── Check missing MEND ──
            if not found_mend:
                errors.append(f"ERROR: Macro '{macro_name}' is missing MEND!")

        i += 1

    return MNT, MDT, ALA, errors


# ── Test ──
if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()

    MNT, MDT, ALA, errors = pass1(lines)

    if errors:
        print("=== ERRORS FOUND IN PASS 1 ===")
        for e in errors:
            print(f"  ❌ {e}")
    else:
        print("✅ Pass 1 completed with no errors!")

    print("\n=== MNT ===")
    for name, idx in MNT.items():
        print(f"  {name} → {idx}")

    print("\n=== MDT ===")
    for i, line in enumerate(MDT):
        print(f"  {i}: {line}")

    print("\n=== ALA ===")
    for name, params in ALA.items():
        print(f"  {name} → {params}")