# MCP Hub Gateway 🚀

> A FastMCP-based project demonstrating STDIO + Streamable HTTP MCP servers.

---

# 📌 Quick Navigation
- Overview
- Project Structure
- Features
- Setup
- Run STDIO Server
- Run HTTP Server
- MCP Inspector Setup
- Tools
- Architecture
- Common Issues
- Future Improvements

---

# 📖 Overview

This project demonstrates how to build Model Context Protocol (MCP) servers using FastMCP in Python.

It includes:
- STDIO MCP server for local agent communication
- Streamable HTTP MCP server for browser/Inspector usage
- Example tools for fetching and processing data

---

# 📁 Project Structure

mcp_hub_gateway/
├── 1_CreateMCP/
│   └── 1_first_mcp_server_stdio.py
├── 2_HTTP_MCP/
│   └── 1_http_mcp.py
├── .gitignore
└── README.md

---

# ⚙️ Features

- MCP STDIO transport support
- MCP Streamable HTTP transport support
- Async tool execution support
- FastMCP framework integration
- MCP Inspector compatibility

---

# 🛠️ Setup

Install dependencies:

pip install fastmcp

---

# 🧪 Run STDIO Server

Used for local AI agents (Claude Desktop / CLI tools).

python 1_CreateMCP/1_first_mcp_server_stdio.py

Tools available:
- fetch()
- process(path: str)

---

# 🌐 Run HTTP Server

Used for MCP Inspector and remote testing.

python 2_HTTP_MCP/1_http_mcp.py

Server URL:
http://127.0.0.1:8050/mcp

---

# 🔎 MCP Inspector Setup

Start inspector:

npx @modelcontextprotocol/inspector

Then configure:

Transport: Streamable HTTP
URL: http://127.0.0.1:8050/mcp

Click Connect.

---

# 🔧 Tools

## fetch_http

Returns sample data:

{
  "data": "Hello, MCP!"
}

---

## process_http

Processes input path.

Example input:
/data/sample

Example output:
{
  "processed_data": "Data has been processed at path: /data/sample"
}

---

# 🧠 Architecture

MCP Client / Inspector
        │
        ▼
FastMCP Server (STDIO / HTTP)
        │
   ┌────┴────┐
   ▼         ▼
fetch     process

---

# ⚠️ Common Issues

## Inspector connection fails

Use:
http://127.0.0.1:8050/mcp

NOT:
http://localhost:3001/sse

---

## Server crash on startup

Fix host:

host="127.0.0.1"

---

## Git push rejected

Run:

git pull origin main --allow-unrelated-histories
git push -u origin main

---

# 🚀 Future Improvements

- Add authentication layer
- Add database integration
- Add logging system
- Dockerize MCP server
- Add CI/CD pipeline
- Convert into reusable MCP framework

---

# 👨‍💻 Author

FastMCP learning project for understanding MCP architecture.

---

# 📜 License

MIT (optional)
