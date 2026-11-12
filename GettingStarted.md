# Software
- Download and install Archi : https://www.archimatetool.com/download/
- Download the latest MCP plugin release from : https://github.com/fanievh/archi-mcp-server/releases
- Install the plugin : Help -> Manage plugins -> Install -> choose ```net.vheerden.archi.mcp_1.10.0.archiplugin``` -> restart Archi when asked.

# Add MCP server

- Start the MCP server in the menu

- Open Claude Desktop. Edit the ```claude_desktop_config.json``` file and add:
```
{
  "mcpServers": {
    "archi": {
      "command": "uvx",
      "args": [
        "mcp-proxy",
        "--transport",
        "streamablehttp",
        "http://127.0.0.1:18090/mcp"
      ]
    },
  }
}
``` 

# Get the content

- open a terminal or use your favorite IDE
```
git clone https://github.com/UNECE/Statistical-Architecture-Framework.git
cd Statistical-Architecture-Framework
```
- You now have a copy of the SAF repository
- Use a new branch to apply changes. 

# Open the model
The architecture model can be loaded into Archi. Please open the ```SAF.archimate``` file in Archi or ask your AI-agent to do so.

# Collaboration

You are now set up to communicate with model the documentation as well as the Archimate model. Commit the changes when ready, create a pull request and collaborate to merge the new contents.

