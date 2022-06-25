add_library('minim')


def setup():
    global rockimage, scissorsimage, paperimage,CHOICES,player_choice,computer_choice,playerwonnum,computerwonnum, pageid
    size(1000, 600)
    background(0)
    textAlign(CENTER)
    rockimage = loadImage('rock.png')
    scissorsimage = loadImage('scissors.png')
    paperimage = loadImage('paper.png')
    pageid = 0
    gameReset()

def draw():
    global rockimage, scissorsimage, paperimage,CHOICES,player_choice,computer_choice,playerwonnum,computerwonnum,nTotalFramsForPauseElapsed,nTotalFramsForPause,pageid
    background(0)   
    if pageid == 1:
        if  (playerwonnum >= 2 or computerwonnum >= 2 ):
            pageid=3
        else:
            gameStartScreen()
    elif  pageid == 2:
        if   nTotalFramsForPauseElapsed<=nTotalFramsForPause:
            gamePauseScreen()
            nTotalFramsForPauseElapsed += 1
        else:
            player_choice=''
            computer_choice=CHOICES[int(random(2))]
            nTotalFramsForPauseElapsed=0
            pageid = 1
            
    elif  pageid == 3:
        goodByeScreen()
    else:
        welcomeScreen()


def welcomeScreen():
    #Title
    image(rockimage, 100, 200,200,200)
    image(paperimage , 350, 200,200,200)
    image(scissorsimage, 600, 200,200,200)
    
    #Instructions
    fill(255)
    textSize(30)
    text("Welcome to play Rock/Paper/Seccors game with computer", 470, 50)

    
    text("Press DOWN key to start a game", 500, 500)

def gameStartScreen():
    #Title
    image(rockimage, 100, 200,200,200)
    image(paperimage , 350, 200,200,200)
    image(scissorsimage, 600, 200,200,200)
    
    #Instructions
    fill(255)
    textSize(30)
    text("Click Rock or Paper or scossprs, to beat computer", 500, 50)

    
    text("Computer : You", 500, 500)
    text(str(computerwonnum) + " : " + str(playerwonnum), 500, 550)
    
def gamePauseScreen():
    global rockimage, scissorsimage, paperimage,CHOICES,player_choice,computer_choice,playerwonnum,computerwonnum

    if computer_choice=='r':
        image(rockimage, 100, 200,200,200)
    if computer_choice=='p':
        image(paperimage, 100, 200,200,200)
    if computer_choice=='s':
        image(scissorsimage, 100, 200,200,200)

    if player_choice=='r':
        image(rockimage, 600, 200,200,200)
    if player_choice=='p':
        image(paperimage, 600, 200,200,200)
    if player_choice=='s':
        image(scissorsimage, 600, 200,200,200)
    
    #Instructions
    fill(255)
    textSize(30)
    text("Computer is:             Your is:", 400, 50)

    nResutlt=getWinner(player_choice, computer_choice)
    
    if nResutlt >0 :        
        text("You win", 500, 500)
    elif nResutlt <0 :
        text("Computer win", 500, 500)   
    else :
        text("draw", 500, 500)

                    
def goodByeScreen():
    global rockimage, scissorsimage, paperimage,CHOICES,player_choice,computer_choice,playerwonnum,computerwonnum

    fill(255)
    textSize(80)
    if playerwonnum >= 2:
        text("You won. " + str(playerwonnum) + " : " + str(computerwonnum), 500, 300)
    if computerwonnum >= 2:
        text("Computer won. " + str(computerwonnum) + " : " + str(playerwonnum), 500, 300)
    
    textSize(30)
    text("Press UP key to play again.", 500, 500)
 
#1-> player win
#-1-> computer win
#0 -> tie
def getWinner(player_choice, computer_choice):
    global CHOICES,playerwonnum,computerwonnum,gameWon
    if player_choice == 'r' and computer_choice == 'c':
       return 1
    elif player_choice == 's' and computer_choice == 'p':
        return 1
    elif player_choice == 'p' and computer_choice == 'r':
        return 1
    elif computer_choice == 'r' and player_choice == 's':
        return -1
    elif computer_choice == 's' and player_choice == 'p':
        return -1
    elif computer_choice == 'p' and player_choice == 'r':
        return -1
     
    return 0

def is_draw(player_choice, computer_choice):
    if player_choice == computer_choice:
        return True
    
                                                                                        
def mousePressed():
    global rockimage, scissorsimage, paperimage,CHOICES,player_choice,computer_choice,playerwonnum,computerwonnum,pageid
    
    if pageid==1:
        player_choice = None        
        
        if mouseX > 100 and mouseX < 300 and mouseY>200 and mouseY<400 :
            player_choice='r'
    
        if mouseX > 350 and mouseX < 550 and mouseY>200 and mouseY<400 :
            player_choice='p'
    
        if mouseX > 600 and mouseX < 800 and mouseY>200 and mouseY<400 :
            player_choice='s'
        
        if player_choice is None: 
            print("mouseX=" + str(mouseX) + ";mouseY=" + str(mouseY) + ";computer_choice=" + str(computer_choice) + ";player_choice=none")
        else:
            print("mouseX=" + str(mouseX) + ";mouseY=" + str(mouseY) + ";computer_choice=" + str(computer_choice) + ";player_choice=" + player_choice)
            
        
        if player_choice is not None and player_choice.lower() in CHOICES:
            print("mouseX=" + str(mouseX) + ";mouseY=" + str(mouseY) + " show result")
            nResutlt=getWinner(player_choice, computer_choice)
            
            if nResutlt >0 :        
                playerwonnum +=1
            elif nResutlt < 0 :
                computerwonnum +=1
            
            pageid = 2
            nTotalFramsForPauseElapsed=0
            

def gameReset():
    global CHOICES, player_choice, computer_choice, playerwonnum, computerwonnum, nTotalFramsForPause, nTotalFramsForPauseElapsed
    CHOICES = 'rps'
    player_choice = None
    computer_choice = CHOICES[int(random(2))]
    playerwonnum=0
    computerwonnum=0
    
    nTotalFramsForPause=180
    nTotalFramsForPauseElapsed=0

            
            
def keyPressed():    
    global rockimage, scissorsimage, paperimage,CHOICES,player_choice,computer_choice,playerwonnum,computerwonnum, pageid
    print(str(keyCode))
    if pageid == 0 and keyCode == 40:
        pageid = 1
        
    elif pageid == 1 and keyCode==38:
        if playerwonnum >=2 or computerwonnum>=2 :
            computer_choice = CHOICES[int(random(2))]
            playerwonnum=0
            computerwonnum=0
            pageid = 1
            
    elif pageid == 3 and keyCode==38:
        pageid = 1
        gameReset()
            
