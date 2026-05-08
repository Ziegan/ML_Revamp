# server.py
from fastmcp import FastMCP

mcp = FastMCP("MyLocalHelper")

@mcp.tool()
def calculate_area(radius: float) -> str:
    """Calculates the area of a circle given its radius."""
    import math
    area = math.pi * (radius ** 2)
    return f"The area is {area:.2f}"

if __name__ == "__main__":
    mcp.run()
