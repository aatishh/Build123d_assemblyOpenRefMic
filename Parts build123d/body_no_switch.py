from build123d import *

# Load STL as a part
body = import_stl("Body_no_switch.stl")

# Export the same geometry again
export_stl(body, "body_no_switch_recreated.stl")

print("STL loaded successfully")
print("Volume:", body.volume)