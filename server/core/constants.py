PalworldCommands = {
  "Shutdown": {
    "command": "Shutdown",
    "description": "Shut down the server with the indicated time",
    "args": [
      {
        "name": "Seconds",
        "type": "int",
        "description": "Seconds until shutdown"
      },
      {
        "name": "Message",
        "type": "str",
        "description": "Shutdown message"
      }
    ]
  },
  "DoExit": {
    "command": "DoExit",
    "description": "Shut down the server immediately after using the command"
  },
  "Broadcast": {
    "command": "Broadcast",
    "description": "Broadcast a message to all players",
    "args": [
      {
        "name": "Message",
        "type": "str",
        "description": "Message to broadcast"
      }
    ]
  },
  "KickPlayer": {
    "command": "KickPlayer",
    "description": "Kick a player from the server",
    "args": [
      {
        "name": "PlayerID",
        "type": "str",
        "description": "Player ID to kick (SteamID or PlayerUID)"
      }
    ]
  },
  "BanPlayer": {
    "command": "BanPlayer",
    "description": "Ban a player from the server",
    "args": [
      {
        "name": "PlayerID",
        "type": "str",
        "description": "Player ID to ban (SteamID or PlayerUID)"
      }
    ]
  },
  "TeleportToPlayer": {
    "command": "TeleportToPlayer",
    "description": "Teleport to a player",
    "args": [
      {
        "name": "PlayerID",
        "type": "str",
        "description": "Player ID to teleport to (SteamID or PlayerUID)"
      }
    ]
  },
  "TeleportToMe": {
    "command": "TeleportToMe",
    "description": "Teleport a player to you",
    "args": [
      {
        "name": "PlayerID",
        "type": "str",
        "description": "Player ID to teleport to you (SteamID or PlayerUID)"
      }
    ]
  },
  "ShowPlayers": {
    "command": "ShowPlayers",
    "description": "Show all players on the server"
  },
  "Info": {
    "command": "Info",
    "description": "Show server information"
  },
  "Save": {
    "command": "Save",
    "description": "Save the server"
  },
}