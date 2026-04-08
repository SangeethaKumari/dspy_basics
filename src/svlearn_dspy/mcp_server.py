from fastmcp import FastMCP

mcp = FastMCP(name="mcp server")
    

@mcp.tool()
def subtraction(a: int, b: int) -> int:
    """
    Subtract second number from first.
    
    Args:
        a (int): The first number (minuend).
        b (int): The second number (subtrahend) to subtract from the first.
    
    Returns:
        int: The result of subtracting b from a (a - b).
    """
    print(f"Subtracting {b} from {a}")
    return a - b

@mcp.tool()
def addition(a: int, b: int) -> int:
    """
    Add two numbers together.
    
    Args:
        a (int): The first number to add.
        b (int): The second number to add.
    
    Returns:
        int: The sum of a and b (a + b).
    """
    print(f"Adding {a} and {b}")
    return a + b



if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=9000)