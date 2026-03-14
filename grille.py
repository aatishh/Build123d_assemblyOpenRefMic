from build123d import *

# Load the original STL
grille = import_stl("Grille.stl")

# Export the same geometry again
export_stl(grille, "grille_recreated.stl")

print("Grille STL loaded successfully")
print("Volume:", grille.volume)