add_library('minim')

CHOICES = 'rps'
player_choice = None
computer_choice = CHOICES[int(random(2))]
playerwonnum=0
computerwonnum=0
gameWon = False
gamePause = False

nTotalFramsForPause=180
nTotalFramsForPauseElapsed=0

def setup():
    global rockimage, scissorsimage, paperimage,CHOICES,player_choice,computer_choice,playerwonnum,computerwonnum
    size(1000, 600)
    background(0)
    textAlign(CENTER)
    rockimage = loadImage('rock.png')
    scissorsimage = loadImage('scissors.png')
    paperimage = loadImage('paper.png')
    computer_choice = CHOICES[int(random(2))]
    playerwonnum=0
    computerwonnum=0

def draw():
    global rockimage, scissorsimage, paperimage,CHOICES,player_choice,computer_choice,playerwonnum,computerwonnum,gamePause,nTotalFramsForPauseElapsed,nTotalFramsForPause
    background(0)   
    if gamePause:
        if nTotalFramsForPauseElapsed > nTotalFramsForPause:
            gamePause=False
            player_choice=''
            computer_choice=CHOICES[int(random(2))]
            nTotalFramsForPauseElapsed=0
    
    if not gamePause and (playerwonnum >= 2 or computerwonnum >= 2 ):
        endScreen()
    elif gamePause:           
        nTotalFramsForPauseElapsed += 1;
        pauseResult()
    else:
        startScreen()    

def startScreen():
    #Title
    image(rockimage, 100, 200,200,200)
    image(paperimage , 350, 200,200,200)
    image(scissorsimage, 600, 200,200,200)
    
    #Instructions
    fill(255)
    textSize(30)
    text("Click Rock or Paper or scossprs, to beat computer", 400, 50)

    
    text("Computer : You", 300, 500)
    text(str(computerwonnum) + " : " + str(playerwonnum), 300, 550)
    
def pauseResult():
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
        text("You win", 300, 500)
    elif nResutlt <0 :
        text("Computer win", 300, 500)   
    else :
        text("draw", 300, 500)

                    
def endScreen():
    global rockimage, scissorsimage, paperimage,CHOICES,player_choice,computer_choice,playerwonnum,computerwonnum

    fill(255)
    textSize(30)
    if playerwonnum >= 2:
        text("You won. " + str(playerwonnum) + " : " + str(computerwonnum), 400, 50)
    if computerwonnum >= 2:
        text("Computer won. " + str(computerwonnum) + " : " + str(playerwonnum), 400, 50)
    
    
    text("Press UP key to play again.", 300, 500)
 
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
    global rockimage, scissorsimage, paperimage,CHOICES,player_choice,computer_choice,playerwonnum,computerwonnum,gamePause
    
    if not gamePause:
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
            
            gamePause=True
            
def keyPressed():    
    global rockimage, scissorsimage, paperimage,CHOICES,player_choice,computer_choice,playerwonnum,computerwonnum,gamePause
    if keyCode==38:
        if playerwonnum >=2 or computerwonnum>=2 :
            computer_choice = CHOICES[int(random(2))]
            playerwonnum=0
            computerwonnum=0
            gameWon = False
            gamePause = False
