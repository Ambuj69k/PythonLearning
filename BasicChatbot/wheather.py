from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Weather")

@mcp.tool()
async def get_wheather(location:str)->str:
    """Get the wheather location. """
    return "It's always raining in Mumbai"

if __name__=="__main__":
    mcp.run(transport="streamable-http")

