
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




# add alliance chat
    # if already exists, send warning that it already exists and cancel the add
    # make sure to add a round metadata

# remove alliance chat


if __name__ == "__main__":
    editor = AllianceDataEditor("test.json")
    editor.load_data()
    editor.list_alliance_chats()

