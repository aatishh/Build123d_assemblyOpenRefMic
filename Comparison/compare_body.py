import trimesh
import os

ORIGINAL_FILE  = "Body.stl"
GENERATED_FILE = "body_recreated.stl"

# ── File checks ──────────────────────────────────────────────
if not os.path.exists(ORIGINAL_FILE):
    print(f"❌ File not found: {ORIGINAL_FILE}")
    exit()

if not os.path.exists(GENERATED_FILE):
    print(f"❌ File not found: {GENERATED_FILE}")
    exit()

# ── Load meshes ──────────────────────────────────────────────
original  = trimesh.load_mesh(ORIGINAL_FILE)
generated = trimesh.load_mesh(GENERATED_FILE)

# ── Volume comparison ────────────────────────────────────────
vol_orig = original.volume
vol_gen  = generated.volume
diff     = abs(vol_orig - vol_gen)
pct      = (diff / vol_orig * 100) if vol_orig != 0 else float("inf")

print("\n===== VOLUME CHECK =====")
print(f"Original  Volume : {vol_orig:.4f} mm³")
print(f"Generated Volume : {vol_gen:.4f} mm³")
print(f"Difference       : {diff:.4f} mm³ ({pct:.2f}%)")

# ── Symmetric difference ─────────────────────────────────────
try:
    sym = original.symmetric_difference(generated)
    print(f"\n===== SYMMETRIC DIFFERENCE =====")
    print(f"Sym Diff Volume  : {sym.volume:.4f} mm³")
except Exception as e:
    print(f"\n⚠️  Symmetric difference failed: {e}")
    print("   (Mesh may not be watertight — try trimesh.repair.fix_normals)")

# ── Result ───────────────────────────────────────────────────
print("\n===== RESULT =====")
if pct < 1.0:
    print(f"✅ Match — {pct:.2f}% difference (under 1%)")
elif pct < 5.0:
    print(f"⚠️  Close — {pct:.2f}% difference (under 5%)")
else:
    print(f"❌ Mismatch — {pct:.2f}% difference")