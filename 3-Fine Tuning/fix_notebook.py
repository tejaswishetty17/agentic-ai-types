import json
from pathlib import Path

# === Change this to your notebook path ===
notebook_path = Path("Fine_Tuning_a_Model.ipynb")
output_path = notebook_path.with_name(f"{notebook_path.stem}_cleaned.ipynb")

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

metadata = nb.get("metadata", {})

# Case 1: Just remove widgets metadata
if "widgets" in metadata:
    print("Removing 'metadata.widgets'...")
    metadata.pop("widgets")

# Case 2: If you prefer to preserve widgets, but fix 'state'
elif "widgets" in metadata and "state" not in metadata["widgets"]:
    print("Adding missing 'state'...")
    metadata["widgets"] = {"state": metadata["widgets"]}

nb["metadata"] = metadata

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=2)

print(f"✅ Cleaned notebook saved as {output_path}")
