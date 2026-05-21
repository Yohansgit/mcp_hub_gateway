from fastmcp import FastMCP


# Create an instance of FastMCP
mcp = FastMCP()

@mcp.tool()

def fetch():
    ''' use this tool to fetch data from a source '''

    #   simulate fetching data from a source
    ''' You can make some API calls here or read from a database '''
    return {"data": "Hello, MCP!"}

@mcp.tool() 
def process(path:str):
    ''' Use this tool to process the fetched data '''

    # Simulate processing the fetched data
    ''' You can perform some data transformations here '''
    return {"processed_data": "Data has been processed! at path:" + path}

if __name__ == "__main__":
    # Run the MCP server
    mcp.run(transport='stdio')
    

