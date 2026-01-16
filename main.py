from fastmcp import FastMCP

mcp =FastMCP.as_proxy("https://expense-tracker-remoteserver.fastmcp.app/mcp",name='proxy server - ExpenseTracker')


if __name__ == "__main__":
    mcp.run()
    