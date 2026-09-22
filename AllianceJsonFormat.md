## Alliance HIF JSON Structure

* `network-type`: Type of hypergraph. Use `"undirected"`.
* `metadata`: Information about the entire dataset.
* `nodes`: List of players.

  * `node`: Unique player ID.
  * `attrs.name`: Player’s display name.
* `edges`: List of alliance chats.

  * `edge`: Unique alliance ID.
  * `attrs.name`: Alliance chat name.
  * `attrs.created_round`: Round the chat was created.
* `incidences`: Records connecting players to alliance chats.

  * `edge`: ID of the alliance.
  * `node`: ID of a player in that alliance.

```json
{
  "network-type": "undirected",
  "metadata": {
    "name": "Season Alliances"
  },
  "nodes": [
    {
      "node": "player-001",
      "attrs": {
        "name": "Alice"
      }
    }
  ],
  "edges": [
    {
      "edge": "alliance-001",
      "attrs": {
        "name": "The Final Three",
        "created_round": 4
      }
    }
  ],
  "incidences": [
    {
      "edge": "alliance-001",
      "node": "player-001"
    }
  ]
}
```

Each player and alliance must have a unique ID. An incidence should only reference player and alliance IDs that already exist.
