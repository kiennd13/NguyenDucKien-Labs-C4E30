import pymongo
client = pymongo.MongoClient("mongodb+srv://kiennd13:jxDB1SH3TY0rBbpf@cluster0-nfuqv.mongodb.net/test?retryWrites=true")
db = client.player

# db.Manchester_United.insert_one({"Name":"Marcus Rashford","Age":"22"})
# print(list(db.Manchester_United.find({})))
# def add_player_MU(player):
#     player = []
#     for _ in range(3):
#         a = input(str("Name_player:"))
#         b = input(str("Age:"))
#         add_player = {"Name":a,"Age":b}
#         player.append(add_player)
#     for player in player:
#         db.Manchester_United.insert_one(player)
# player = []
# add_player_MU(player)

def get_player_MU():
    return list(db.Manchester_United.find({}))
