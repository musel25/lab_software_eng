#!/usr/bin/env bash
set -euo pipefail

SRC_DIR="code"
OUT_DIR="diagrams"
FORMAT="png"          # change to svg or pdf if you prefer

# Create output directory if missing
mkdir -p "$OUT_DIR"

# Loop through every .mmd file in the source directory (recursively, keeps sub-dir structure)
find "$SRC_DIR" -type f -name '*.mmd' | while read -r mmd_file; do
  rel_path="${mmd_file#$SRC_DIR/}"                 # path relative to SRC_DIR
  out_path="$OUT_DIR/${rel_path%.mmd}.$FORMAT"     # replace extension, prepend OUT_DIR
  mkdir -p "$(dirname "$out_path")"                # ensure nested folder exists
  echo "🖼️  Rendering $mmd_file → $out_path"
  npx mmdc -i "$mmd_file" -o "$out_path" -e "$FORMAT"
done

echo "✅ All diagrams generated in $OUT_DIR/"
