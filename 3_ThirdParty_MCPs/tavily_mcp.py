from langchain_mcp_adapters.client import MultiServerMCPClient, Connection
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

async def main():
    # Create an instance of the MultiServerMCPClient with a Connection object
    client = MultiServerMCPClient(
        {
            "tavily_mcp_http":{
               "transport":"streamable-http",
                "url": f"https://mcp.tavily.com/mcp/?tavilyApiKey={os.getenv('TAVILY_API_KEY')}"
 }
        } 
    )

    # List the tools
    tools = await client.get_tools()
    print("Available tools:", tools)

if __name__ == "__main__":
    asyncio.run(main()) 







