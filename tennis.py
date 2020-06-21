data = input()
result = {}

while data:
    
    (winner , looser, sets) = data.split(":")
    (winner_set , looser_set) =(0,0)
    (winner_games , looser_games) =(0,0)
    (winner_BO5 , winner_BO3) =(0,0)
    #federar nadal
    
    for single_set in sets.split(','):
        #3-6
        temp = single_set.split("-")
        temp[0] = int(temp[0])
        temp[1] = int(temp[1])
        #temp[0] winner
        #temp[0] looser
        
        if temp[0] > temp[1] :
            winner_set+=1 # won by winner
        else:
            looser_set+=1 # won by looser
        
        winner_games+= temp[0] #won by winer
        looser_games+= temp[1] #won by looser
    if winner_set>=3:
        winner_BO5+=1
    elif winner_set<3:
        winner_BO3+=1
        
    for player in [winner , looser]:
        try:
            result[player]
        except:
            result[player] = [0,0,0,0,0,0]
            
        if player == winner:
            result[player][0]+= winner_set
            result[player][1]+= winner_games
            result[player][2]+= looser_set
            result[player][3]+= looser_games
            result[player][4]+= winner_BO5
            result[player][5]+= winner_BO3
        if player == looser:
            result[player][0]+= looser_set
            result[player][1]+= looser_games
            result[player][2]+= winner_set
            result[player][3]+= winner_games
            
    print(result)
    data = input()