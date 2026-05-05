# pass2.py — with error handling

def pass2(lines, MNT, MDT, ALA):
    output = []
    errors = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue

        tokens = line.split()

        # Skip macro definitions
        if tokens[0] == "MACRO":
            while i < len(lines):
                if lines[i].strip() == "MEND":
                    break
                i += 1
            i += 1
            continue

        # Expand macro calls
        elif tokens[0] == "CALL":

            # ── Check macro name provided ──
            if len(tokens) < 2:
                errors.append(f"ERROR: Line {i+1} — CALL missing macro name!")
                i += 1
                continue

            macro_name = tokens[1]
            call_params = tokens[2:]

            # ── Check undefined macro ──
            if macro_name not in MNT:
                errors.append(f"ERROR: Line {i+1} — Undefined macro '{macro_name}'!")
                i += 1
                continue

            formal_params = ALA[macro_name]

            # ── Check wrong number of params ──
            if len(call_params) != len(formal_params):
                errors.append(
                    f"ERROR: Line {i+1} — Macro '{macro_name}' expects "
                    f"{len(formal_params)} param(s), but got {len(call_params)}!"
                )
                i += 1
                continue

            # Expand macro
            mdt_index = MNT[macro_name]
            while mdt_index < len(MDT):
                body_line = MDT[mdt_index]
                if body_line == "MEND":
                    break
                for formal, actual in zip(formal_params, call_params):
                    body_line = body_line.replace(formal, actual)
                output.append(body_line)
                mdt_index += 1

        else:
            output.append(line)

        i += 1

    return output, errors


# ── Test ──
if __name__ == "__main__":
    from pass1 import pass1

    with open("input.txt", "r") as f:
        lines = f.readlines()

    MNT, MDT, ALA, errors1 = pass1(lines)
    expanded, errors2 = pass2(lines, MNT, MDT, ALA)

    all_errors = errors1 + errors2

    if all_errors:
        print("=== ALL ERRORS ===")
        for e in all_errors:
            print(f"  ❌ {e}")

    print("\n=== Expanded Output ===")
    for line in expanded:
        print(line)