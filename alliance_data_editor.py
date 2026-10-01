
import json

class AllianceDataEditor:

    def __init__(self, alliance_data_file):
        self.alliance_data_file = alliance_data_file
        self.data = {}

    def load_data(self):
        with open(self.alliance_data_file, "r") as file:
            self.data = json.load(file)

    def save_data(self):
        with open(self.alliance_data_file, "w") as file:
            json.dump(self.data, file, indent=4)

    def list_alliance_chats(self):
        alliance_chats = {
            f"{edge["attrs"]["name"]}: {", ".join(self.players_in_alliance(edge["edge"]))}"
            for edge in self.data["edges"]
        }
        alliance_chats = sorted(alliance_chats)
        print("\n".join(alliance_chats))

    def players_in_alliance(self, alliance_id):
        playerIDs = {
            incidence["node"]
            for incidence in self.data["incidences"]
            if incidence["edge"] == alliance_id
        }

        return {
            player["attrs"]["name"]
            for player in self.data["nodes"]
            if player["node"] in playerIDs
        }

    def create_alliance_chat(self, name, round_created, players):
        if self.alliance_chat_exists(name):
            print("Alliance chat with that name already exists")
            choice = input("Do you still want to create it? (y/n) ").lower().strip()
            if choice != "y":
                return
        for player in players:
            if self.get_player_id_from_name(player) == None:
                print(f"Player {player} not found")
                return

        id = self.next_alliance_id()
        self.data["edges"].append({
            "edge": id,
            "attrs": {
                "name": name,
                "created_round": round_created
            }
        })
        for player in players:
            self.data["incidences"].append({
                "edge": id,
                "node": self.get_player_id_from_name(player)
            })

    def get_player_id_from_name(self, name):
        for player in self.data["nodes"]:
            if player["attrs"]["name"] == name:
                return player["node"]
        return None

    def get_edge_id_from_name(self, name):
        for edge in self.data["edges"]:
            if edge["attrs"]["name"] == name:
                return edge["edge"]

    def alliance_chat_exists(self, name):
        exists = False;
        for edge in self.data["edges"]:
            if edge["attrs"]["name"] == name:
                exists = True
        return exists

    def next_alliance_id(self):
        numbers = [
            int(edge["edge"].split("-")[1])
            for edge in self.data["edges"]
            if edge["edge"].startswith("alliance-")
        ]

        next_number = max(numbers, default=0) + 1
        return f"alliance-{next_number:03d}"

    def remove_alliance_chat(self, name):
        id = self.get_edge_id_from_name(name)
        self.data["edges"] = [
            edge
            for edge in self.data["edges"]
            if edge["edge"] != id
        ]
        self.data["incidences"] = [
            incidence
            for incidence in self.data["incidences"]
            if incidence["edge"] != id
        ]
        
    def remove_player(self, name):
        choice = input(f"Are you sure you would like to delete {name}? (y/n) ").lower().strip()
        if choice == "n": return
        
        id = self.get_player_id_from_name(name)
        self.data["nodes"] = [
            node
            for node in self.data["nodes"]
            if node["node"] != id
        ]
        removed_edges = [
            incidence["edge"]
            for incidence in self.data["incidences"]
            if incidence["node"] == id
        ]
        self.data["edges"] = [
            edge
            for edge in self.data["edges"]
            if edge["edge"] not in removed_edges
        ]
        self.data["incidences"] = [
            incidence
            for incidence in self.data["incidences"]
            if incidence["edge"] not in removed_edges
        ]
                


if __name__ == "__main__":
    editor = AllianceDataEditor("data/test.json")
    editor.load_data()
    editor.create_alliance_chat("test", 3, ["Will", "Zoe M"])
    editor.list_alliance_chats()
    editor.remove_player("Courtney")
    editor.list_alliance_chats()

