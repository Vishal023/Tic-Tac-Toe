def gamePrint(choice):
    one = choice[1]
    two = choice[2]
    thr = choice[3]
    fou = choice[4]
    fiv = choice[5]
    six = choice[6]
    sev = choice[7]
    eig = choice[8]
    nin = choice[9]
    #print('   |   |   ')
    print(f' {sev} | {eig} | {nin}  ')
    #print('   |   |   ')
    print('-----------')
    #print('   |   |   ')
    print(f' {fou} | {fiv} | {six} ')
    #print('   |   |   ')
    print('-----------')
    #print('   |   |   ')
    print(f' {one} | {two} | {thr} ')
    #print('   |   |   ')    
def playerChoice():
    marker = ''
    while marker != "x" and marker != "o":
        marker = input("Do you want 'x' or 'o' Player 1: ")
    player1 = marker
    if player1 == 'x':
        player2 = 'o'
    else:
        player2 ='x'
    return(player1,player2)
def inputPos():
    print()
    p1,p2 = playerChoice()
    if p1 == 'x':
        player = 1
        marker = p1
        print(f"Player 1 will start the game Marker => {marker}")
    else:
        player = 2
        marker = p2
        print(f"Player 2 will start the game Marker => {marker}")
        
    tryChances = 0
    lis = ["#"," "," "," "," "," "," "," "," "," "]
    placeHolder = [0,0,0,0,0,0,0,0,0,0]
    x = 1
    print()
    gamePrint(lis)
    while tryChances < 9:
        print()
        placeHold = input(f'Enter your position Player {player} : ')
        if placeHold not in placeHolder:
            lis[int(placeHold)] = marker
            placeHolder[int(placeHold)] = placeHold
            gamePrint(lis)
            x = check(lis,player)
            if(x == 0):
                return
            if player == 1:
                player = 2
                marker = p2
            else:
                player = 1
                marker = p1
            tryChances += 1
        else:
            continue
    if x == 1:
        print()
        print('Game Over :(')
def check(playerList,mark):

    #horizontal
    if playerList[1:4] == [ 'x' , 'x' , 'x' ] or playerList[4:7] == [ 'x' , 'x' , 'x' ] or playerList[7:10] == [ 'x' , 'x' , 'x' ]:
        print(f"Player {mark} won the game")
        return 0
    if playerList[1:4] == [ 'o' , 'o' , 'o' ] or playerList[4:7] == [ 'o' , 'o' , 'o' ] or playerList[7:10] == [ 'o' , 'o' , 'o' ] :
        print(f"Player {mark} won the game")
        return 0
    #diaognal
    if playerList[3:8:2] == [ 'x' , 'x' , 'x' ] or playerList[1:10:4] == [ 'x' , 'x' , 'x' ]:
        print(f"Player {mark} won the game")
        return 0
    if playerList[3:8:2] == [ 'o' , 'o' , 'o' ] or playerList[1:10:4] == [ 'o' , 'o' , 'o' ]:
        print(f"Player {mark} won the game")
        return 0
    
    #vertical
    if playerList[1:8:3]  == [ 'x' , 'x' , 'x' ] or playerList[2:9:3] == [ 'x' , 'x' , 'x' ] or playerList[3:10:3] == [ 'x' , 'x' , 'x' ]:
        print(f"Player {mark} won the game")
        return 0
    if playerList[1:8:3] == [ 'o' , 'o' , 'o' ] or playerList[2:9:3]  == [ 'o' , 'o' , 'o' ] or playerList[3:10:3] == [ 'o' , 'o' , 'o' ] :
        print(f"Player {mark} won the game")
        return 0
    return 1
def startGame():
    print("WELCOME TO TIC TAC TOE")
    inp = input("DO YOU WANT TO PLAY THE GAME YES/NO : ")
    if inp.lower() == "yes":
        inputPos()
    else:
        print("Thank You :)")

startGame()