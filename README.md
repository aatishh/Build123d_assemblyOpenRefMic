# Build123d_assemblyOpenRefMic
# CAD Assembly using Build123d

## Project Overview

This project reconstructs and assembles a microphone-style mechanical system using **Python CAD scripting with the build123d library**.

The goal of the task was to recreate the provided **STL parts as parametric CAD scripts**, generate individual components programmatically, and assemble them into a final model while maintaining minimal deviation from the original STL geometry.

The final result is a **script-driven CAD workflow** that generates all parts and the final assembly automatically.

---

# Parts Modeled

The assembly consists of four individual components:

* Body
* Grille
* Spacer
* Solder Jig

Each part is generated using **build123d parametric modeling** and exported as STL.

---

# Reverse Engineering Approach

The assignment initially provided **only STL files**, meaning the parametric CAD history of the parts was not available.

To extract the required dimensions and features, the following approach was used:

1. The STL files were inspected and analyzed.
2. The meshes were inspected and reconstructed in Fusion to understand the underlying geometry.
3. From this reconstruction process, approximate engineering dimensions and feature relationships were derived.
4. These extracted parameters were then used to recreate the parts programmatically using **build123d**.

This step allowed the transition from **mesh-based geometry to parametric CAD modeling**.

---

# Key Dimensions Identified

### Body

* Outer Diameter: **12.7 mm**
* Total Length: **83.8 mm**
* Thread: **M11 × 1.5**
* Thread Length: **11.31 mm**
* Side Hole Radius: **3 mm**
* Hole Offset: **60.27 mm**
* Button Section Length: **25.33 mm**

---

### Grille

* Outer Diameter: **13.2 mm**
* Inner Diameter: **11.27 mm**
* Height: **12.9 mm**
* Slot Width: **1.93 mm**
* Slot Depth: **4.07 mm**
* Top Chamfer: **~45°**

---

### Spacer

* Outer Diameter: **8.3 mm**
* Inner Diameter: **5.4 mm**
* Height: **5.65 mm**

---

### Solder Jig

* Overall Length: **111 mm**
* Width: **50 mm**
* Base Height: **10 mm**
* Internal cylindrical support seat for the body.

---

# Challenges Faced

While recreating the geometry, it was observed that modeling purely from extracted dimensions sometimes produced slight deviations compared to the STL geometry.

This was mainly due to **complex CAD operations present in the original models**, such as:

* Fillets
* Chamfers
* Slot edge transitions
* Small geometric offsets

Since STL models only contain **triangular mesh surfaces and not parametric feature history**, some of these operations were difficult to reproduce exactly using dimensions alone.

This issue was particularly noticeable in:

* **Body**
* **Grille**

where small surface features affect the final volume.

---

# Part Generation

Each component is generated individually through Python scripts.

Example:

```
python parts/body.py
python parts/grille.py
python parts/spacer.py
python parts/solder_jig.py
```

These scripts produce STL files inside:

```
stl_generated/
```

---

# Assembly

Once the individual parts are generated, they are imported and positioned using transformation operations.

```
python assembly/assembly.py
```

This script loads the generated STL files and places them in their correct assembly positions.

The final assembled model is exported as:

```
final_assembly.stl
```

---

# Verification

To validate the recreated parts, the generated STL files were compared against the original STL files.

Two primary checks were performed:

* **Volumetric Difference**
* **Symmetric Difference**

To support this validation, an additional **Python script was written to compute and compare the volumes of each generated part with the original STL files**.

This helped ensure that the recreated geometry closely matches the original models.

---

# Technologies Used

* Python
* build123d
* OpenCascade CAD Kernel
* STL Mesh Geometry
* Fusion (for mesh inspection and dimension extraction)

---

# Repository Structure

```
parts/           → individual CAD scripts  
assembly/        → assembly script  
stl_original/    → provided STL files  
stl_generated/   → generated STL files  
comparison/    → volume comparison scripts
```

---

# Result

This project demonstrates how **parametric CAD scripting can be used to reconstruct and assemble mechanical components from STL geometry**.

The workflow highlights the importance of **mesh inspection, dimensional reconstruction, and script-based modeling** in situations where the original CAD design history is unavailable.
