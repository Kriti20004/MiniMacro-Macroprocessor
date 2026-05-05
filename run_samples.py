# run_samples.py — runs all 3 sample programs

from pass1 import pass1
from pass2 import pass2

samples = ["sample1.txt", "sample2.txt", "sample3.txt"]

for sample in samples:
    print("=" * 50)
    print(f"  RUNNING: {sample}")
    print("=" * 50)

    try:
        with open(sample, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"❌ {sample} not found! Skipping...\n")
        continue

    # Pass 1
    MNT, MDT, ALA, errors1 = pass1(lines)

    # Pass 2
    expanded, errors2 = pass2(lines, MNT, MDT, ALA)

    # Errors
    all_errors = errors1 + errors2
    if all_errors:
        print("\n=== ❌ ERRORS ===")
        for e in all_errors:
            print(f"  {e}")
    else:
        print("\n✅ No errors!")

    # Output
    print("\n=== Expanded Output ===")
    for line in expanded:
        print(f"  {line}")

    # Save
    out_file = sample.replace(".txt", "_output.txt")
    with open(out_file, "w") as f:
        for line in expanded:
            f.write(line + "\n")

    print(f"\n✅ Saved to {out_file}")
    print()