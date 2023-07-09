import a2s

address = ("43.139.29.108", 27236)

players = a2s.players(address)
info = a2s.info(address)

print(info.server_name)
print("Map name: "+info.map_name)
print("Player count: ",len(players))
for player in players:
    print("- ",player.name)

# 43.139.29.108:27019