import os

# -----------------------------
# File paths (Windows-safe)
# -----------------------------
book_file = r"C:\python_task\files.txt"          # 29k filenames
acacharts_file = r"C:\python_task\MA_2026.txt"   # 5.3M full paths
output_file = r"C:\python_task\found files.txt"  # matched paths

# -----------------------------
# Step 1: Load target filenames into a set
# -----------------------------
print("Loading target filenames from files.txt ...")

target_files = set()

with open(book_file, "r", encoding="utf-8") as f:
    for line in f:
        filename = line.strip()
        if filename:
            target_files.add(filename)

print(f"Total target filenames loaded: {len(target_files):,}")

# -----------------------------
# Step 2: Stream through MA_2026.txt
# -----------------------------
print("Searching in MA_2026.txt ...")

matches_found = 0

with open(acacharts_file, "r", encoding="utf-8") as infile, \
     open(output_file, "w", encoding="utf-8") as outfile:

    for lineno, line in enumerate(infile, 1):
        line = line.strip()

        if not line:
            continue

        # Extract filename from full Windows path
        filename = os.path.basename(line)

        # Check if filename exists in target set
        if filename in target_files:
            outfile.write(line + "\n")
            matches_found += 1

        # Progress every 500,000 lines
        if lineno % 500_000 == 0:
            print(
                f"Processed {lineno:,} lines, "
                f"matches found: {matches_found:,}"
            )

print(f"Finished! Total matches found: {matches_found:,}")
print(f"Results saved to: {output_file}")
