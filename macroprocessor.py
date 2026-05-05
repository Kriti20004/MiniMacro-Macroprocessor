# macroprocessor.py — Final version with error handling

from pass1 import pass1
from pass2 import pass2

print("=" * 50)
print("      MINIMACRO MACROPROCESSOR")
print("=" * 50)

# Load file
try:
    with open("input.txt", "r") as f:
        lines = f.readlines()
    print("\n✅ Input file loaded!")
except FileNotFoundError:
    print("\n❌ ERROR: input.txt not found!")
    exit()

# Pass 1
print("\n--- Running Pass 1 ---")
MNT, MDT, ALA, errors1 = pass1(lines)

print("\n=== MNT ===")
for name, idx in MNT.items():
    print(f"  {name} → MDT index {idx}")

print("\n=== MDT ===")
for i, line in enumerate(MDT):
    print(f"  {i}: {line}")

print("\n=== ALA ===")
for name, params in ALA.items():
    print(f"  {name} → {params}")

# Pass 2
print("\n--- Running Pass 2 ---")
expanded, errors2 = pass2(lines, MNT, MDT, ALA)

# Show errors
all_errors = errors1 + errors2
if all_errors:
    print("\n=== ❌ ERRORS DETECTED ===")
    for e in all_errors:
        print(f"  {e}")
else:
    print("\n✅ No errors found!")

# Show output
print("\n=== Expanded Output ===")
for line in expanded:
    print(line)

# Save output
with open("output.txt", "w") as f:
    for line in expanded:
        f.write(line + "\n")

print("\n✅ Output saved to output.txt")
print("=" * 50)
print("      MACROPROCESSOR COMPLETE!")
print("=" * 50)