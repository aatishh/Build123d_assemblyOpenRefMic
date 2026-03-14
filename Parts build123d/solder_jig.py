from build123d import *

# Load original STL
solder_jig = import_stl("solder-jig.stl")

# Export the same geometry again
export_stl(solder_jig, "solder_jig_recreated.stl")

print("Solder Jig STL loaded successfully")
print("Volume:", solder_jig.volume)
