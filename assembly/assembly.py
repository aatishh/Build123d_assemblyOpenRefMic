from build123d import *
from build123d.importers import import_stl

print("Starting assembly...")

# Load STL parts
jig = import_stl("solder-jig.stl")
body = import_stl("Body.stl")
spacer = import_stl("spacer.stl")

# Bounding boxes
jig_box = jig.bounding_box()
body_box = body.bounding_box()
spacer_box = spacer.bounding_box()

# Move jig so its bottom sits on Z = 0
jig = jig.moved(Location((0, 0, -jig_box.min.Z)))

# Place cylinder inside jig groove
body_x = jig.bounding_box().center().X - body_box.center().X
body_y = jig.bounding_box().center().Y - body_box.center().Y

# Drop cylinder slightly into groove
body_z = jig.bounding_box().max.Z - body_box.min.Z - (body_box.size.Z * 0.35)

body = body.moved(Location((body_x, body_y, body_z)))

# Align spacer with body center
spacer_x = body.bounding_box().center().X - spacer_box.center().X
spacer_y = body.bounding_box().center().Y - spacer_box.center().Y

# Insert spacer into hole
spacer_z = body.bounding_box().max.Z - spacer_box.size.Z * 0.8

spacer = spacer.moved(Location((spacer_x, spacer_y, spacer_z)))

# Create assembly
assembly = Compound(children=[jig, body, spacer])

# Export STL
export_stl(assembly, "final_assembly.stl")

print("Final assembly STL created.")