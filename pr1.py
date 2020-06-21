input_list=['Vivek:roger:6-4,6-3,6-4']
# while True:
#     input_string = input()
#     if input_string == "":
#         break
#     else:
        
#         input_list.append(input_string)

print(input_list)

player1_game_won= 0
player2_game_won= 0
player1_game_score_total = 0
player2_game_score_total = 0
player1_game_won_set_3 = 0
player1_game_won_set_5 = 0
player2_game_won_set_3 = 0
player2_game_won_set_5 = 0

input_list2=[]
for line in input_list:
    input_list2 = (line.split(":"))
print(input_list2)
player_data = {}
player1_name = input_list2[0]
player_data[player1_name] = {"name ": player1_name} 
player_data[player1_name]["player1_game_score_total "] = player1_game_score_total
player2_name = input_list2[1]
player_data[player2_name] = {"name": player2_name} 
player_data[player2_name]["player2_game_score_total "] = player2_game_score_total
Players_scores = input_list2[2]
print(Players_scores)

game_scores = []
game_scores = Players_scores.split(",")

print(game_scores)
print(len(game_scores))
for i in range(len(game_scores)):
    game_1_scores = []
    game_1_scores =  game_scores[i].split("-")
    player1_game_score = game_1_scores[0]
    player1_game_score_total += int(player1_game_score)
    player2_game_score = game_1_scores[1]
    player2_game_score_total += int(player2_game_score)
    # print(player1_game_1_score)
    # print(player2_game_1_score)

    if (int(player1_game_score) > int(player2_game_score)) and abs(int(player1_game_score) - int(player2_game_score)) > 1 :
        player1_game_won += 1
    elif (player1_game_score < player2_game_score) and abs(player1_game_score - player2_game_score) > 1 :
        player2_game_won += 1
if player1_game_won > player2_game_won :
    if player1_game_won == 2 :
        player1_game_won_set_3 += 1
    elif player1_game_won == 3 :
        player1_game_won_set_5 += 1
elif player1_game_won < player2_game_won :
    if player2_game_won == 2 :
        player2_game_won_set_3 += 1
    elif player2_game_won == 3 :
        player2_game_won_set_5 += 1

print(player1_game_score_total)
print(player2_game_score_total)
player_data[player1_name]["player1_game_score_total "] = player1_game_score_total
player_data[player2_name]["player2_game_score_total "] = player2_game_score_total




print("player1_game_won ",player1_game_won)
print("player2_game_won ",player2_game_won)
print(player_data)








# Vivek:roger:6-4,6-3,6-4