"""20 mm cube with a 5 mm diameter through-hole along Z."""
from build123d import Box, Cylinder, export_step, export_stl

part = Box(20, 20, 20) - Cylinder(radius=2.5, height=20)

if __name__ == "__main__":
    export_step(part, "cube_with_hole.step")
    export_stl(part, "cube_with_hole.stl")
    bb = part.bounding_box()
    print(f"size: {bb.size}, volume: {part.volume:.2f} mm^3")
