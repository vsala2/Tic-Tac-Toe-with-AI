import random
import pickle
import numpy as np
import cv2
from os import path

# Main game class
class tictactoeMinimax:
    def __init__(self):
        # define parameters
        self.window_width=1100
        self.window_height=680
        self.game_mode=np.zeros([self.window_height,self.window_width,3],dtype=np.uint8)
        self.user_player=0
        self.comp_player=0
        self.bckgrd_colour=(0,0,0)
        self.grid_colour=(70,85,93)
        self.X_colour=(67,130,240)
        self.O_colour=(255,255,255)
        self.O_radius=50
        self.thickness=7

        if path.exists('data.pak'):
            with open('data.pak','rb') as f:
                self.user_player=pickle.load(f)
                self.comp_player=pickle.load(f)
                f.close()
        self.winline_colour=(67,130,240)
        self.move_colour=(70,85,93)
        self.game_status=[
            [' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']
        ]
        self.players_move=None
        self.comp_selection=None
        self.comp_first_move=False
        self.select_player=random.choice(['X','O'])
        if self.select_player=='X':
            self.comp_selection='O'
        else:
            self.comp_selection='X'

    # determine best possible move    
    def minimax(self,current_status,depth,isMaximising):
        maximum=-999        #maximum
        minimum=999         #minimum
        if depth==0 or self.checkGameOver(current_status):
            return self.finalPosition(current_status)
        
        if isMaximising:
            for i in range(3):
                for j in range(3):
                    if current_status[i][j]==' ':
                        current_status[i][j]=self.comp_selection
                        eval=self.minimax(current_status,depth-1, False)
                        current_status[i][j]=' '
                        maximum=max(maximum,eval)
            return maximum

        else:
            for i in range(3):
                for j in range(3):
                    if current_status[i][j]==' ':
                        current_status[i][j]=self.select_player
                        eval=self.minimax(current_status,depth-1,True)
                        current_status[i][j]=' '
                        minimum=min(minimum,eval)
            return minimum
        
#board object placement
    def board(self):
        self.game_mode=np.zeros([self.window_height,self.window_width,3],dtype=np.uint8)
        self.game_mode[:,:]=self.bckgrd_colour
        cv2.line(self.game_mode,(210,30),(210,600),self.grid_colour,self.thickness)
        cv2.line(self.game_mode,(420,30),(420,600),self.grid_colour,self.thickness)
        cv2.line(self.game_mode,(30,210),(600,210),self.grid_colour,self.thickness)
        cv2.line(self.game_mode,(30,420),(600,420),self.grid_colour,self.thickness)
        cv2.rectangle(self.game_mode,(670,400),(800,530),(23,13,4),2)
        cv2.rectangle(self.game_mode,(820,400),(950,530),(23,13,4),2)
        cv2.circle(self.game_mode,(735,465),45,self.O_colour,self.thickness) # O
        cv2.line(self.game_mode,(850,430),(920,500),self.X_colour,self.thickness) # X
        cv2.line(self.game_mode,(920,430),(850,500),self.X_colour,self.thickness) # X
        cv2.putText(self.game_mode,f'Player {self.select_player}',(610,100),cv2.FONT_HERSHEY_COMPLEX,1, (255,255,255),2)
        cv2.putText(self.game_mode,f'Computer {self.comp_selection}',(780,100),cv2.FONT_HERSHEY_COMPLEX,1, (255,255,255),2)
        cv2.line(self.game_mode,(770,80),(770,180),(255,255,255),4)
        cv2.line(self.game_mode,(610,120),(980,120),(255,255,255),4)
        cv2.putText(self.game_mode,str(self.user_player),(770-70,160),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        cv2.putText(self.game_mode,str(self.comp_player),(770+70,160),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        cv2.rectangle(self.game_mode,(645,240),(775,300),(15,166,166),-1)
        cv2.rectangle(self.game_mode,(795,240),(925,300),(12,12,148),-1)
        cv2.putText(self.game_mode,'Reset',(665,281),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        cv2.putText(self.game_mode,'Quit',(822,281),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

    # the display move function
    def moveDisplay(self):
        for i in range(3):
            for j in range(3):
                if self.game_status[i][j]=='O':
                    cv2.circle(self.game_mode,(105+210*j,105+210*i),self.O_radius,self.O_colour,self.thickness)
                elif self.game_status[i][j]=='X':
                    cv2.line(self.game_mode,(50+210*j,50+210*i),(160+210*j,160+210*i),self.X_colour,self.thickness)
                    cv2.line(self.game_mode,(160+210*j,50+210*i),(50+210*j,160+210*i),self.X_colour,self.thickness)


    def makeLine(self):
        # horizontal
        if self.game_status[0][0]==self.game_status[0][1] and self.game_status[0][1]==self.game_status[0][2] and self.game_status[0][0]!=' ':
            if self.select_player==self.game_status[0][0]:
                self.user_player+=1
                self.players_move=True
            else:
                self.comp_player+=1
                self.players_move=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.game_mode,(105-50,105),(_,105), self.winline_colour,16)
                cv2.imshow('Tic Tac Toe with AI',self.game_mode)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True
        if self.game_status[1][0]==self.game_status[1][1] and self.game_status[1][1]==self.game_status[1][2] and self.game_status[1][1]!=' ':
            if self.select_player==self.game_status[1][1]:
                self.user_player+=1
                self.players_move=True
            else:
                self.comp_player+=1
                self.players_move=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.game_mode,(105-50,315),(_,315), self.winline_colour,16)
                cv2.imshow('Tic Tac Toe with AI',self.game_mode)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True
        if self.game_status[2][0]==self.game_status[2][1] and self.game_status[2][1]==self.game_status[2][2] and self.game_status[2][2]!=' ':
            if self.select_player==self.game_status[2][2]:
                self.user_player+=1
                self.players_move=True
            else:
                self.comp_player+=1
                self.players_move=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.game_mode,(105-50,525),(_,525), self.winline_colour,16)
                cv2.imshow('Tic Tac Toe with AI',self.game_mode)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True

        # vertical
        if self.game_status[0][0]==self.game_status[1][0] and self.game_status[1][0]==self.game_status[2][0] and self.game_status[0][0]!=' ':
            if self.select_player==self.game_status[0][0]:
                self.user_player+=1
                self.players_move=True
            else:
                self.comp_player+=1
                self.players_move=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.game_mode,(105,105-50),(105,_), self.winline_colour,16)
                cv2.imshow('Tic Tac Toe with AI',self.game_mode)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True
        if self.game_status[0][1]==self.game_status[1][1] and self.game_status[1][1]==self.game_status[2][1] and self.game_status[1][1]!=' ':
            if self.select_player==self.game_status[1][1]:
                self.user_player+=1
                self.players_move=True
            else:
                self.comp_player+=1
                self.players_move=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.game_mode,(315,105-50),(315,_), self.winline_colour,16)
                cv2.imshow('Tic Tac Toe with AI',self.game_mode)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True
        if self.game_status[0][2]==self.game_status[1][2] and self.game_status[1][2]==self.game_status[2][2] and self.game_status[2][2]!=' ':
            if self.select_player==self.game_status[2][2]:
                self.user_player+=1
                self.players_move=True
            else:
                self.comp_player+=1
                self.players_move=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.game_mode,(525,105-50),(525,_), self.winline_colour,16)
                cv2.imshow('Tic Tac Toe with AI',self.game_mode)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True
                
        # diagonals
        if self.game_status[0][0]==self.game_status[1][1] and self.game_status[1][1]==self.game_status[1][1]==self.game_status[2][2] and self.game_status[0][0]!=' ':
            if self.select_player==self.game_status[0][0]:
                self.user_player+=1
                self.players_move=True
            else:
                self.comp_player+=1
                self.players_move=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.game_mode,(_,_),(_,_), self.winline_colour,16)
                cv2.imshow('Tic Tac Toe with AI',self.game_mode)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True
        if self.game_status[2][0]==self.game_status[1][1] and self.game_status[1][1]==self.game_status[0][2] and self.game_status[1][1]!=' ':
            if self.select_player==self.game_status[1][1]:
                self.user_player+=1
                self.players_move=True
            else:
                self.comp_player+=1
                self.players_move=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.game_mode,(_,525+105-_),(_,525+105-_), self.winline_colour,16)
                cv2.imshow('Tic Tac Toe with AI',self.game_mode)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True

    # is somebody winner
    def checkWinner(self,current_status):
        # horizontal
        if current_status[0][0]==current_status[0][1] and current_status[0][1]==current_status[0][2] and current_status[0][0]!=' ':
            return True
        if current_status[1][0]==current_status[1][1] and current_status[1][1]==current_status[1][2] and current_status[1][1]!=' ':
            return True
        if current_status[2][0]==current_status[2][1] and current_status[2][1]==current_status[2][2] and current_status[2][2]!=' ':
            return True

        # vertical
        if current_status[0][0]==current_status[1][0] and current_status[1][0]==current_status[2][0] and current_status[0][0]!=' ':
            return True
        if current_status[0][1]==current_status[1][1] and current_status[1][1]==current_status[2][1] and current_status[1][1]!=' ':
            return True
        if current_status[0][2]==current_status[1][2] and current_status[1][2]==current_status[2][2] and current_status[2][2]!=' ':
            return True
                
        # diagonals
        if current_status[0][0]==current_status[1][1] and current_status[1][1]==current_status[2][2] and current_status[0][0]!=' ':
            return True
        if current_status[2][0]==current_status[1][1] and current_status[1][1]==current_status[0][2] and current_status[1][1]!=' ':
            return True

    def checkGameOver(self,current_status):
        if self.checkWinner(current_status):
            return True
        for i in range(3):
            for j in range(3):
                if current_status[i][j]==' ':
                    return False
        return True
    

    # reset the game
    def resetMode(self):
        self.board()
        for i in range(3):
            for j in range(3):
                self.game_status[i][j]=' '
        self.moveDisplay()
        cv2.imshow('Tic Tac Toe with AI',self.game_mode)
        cv2.waitKey(500)


        
    # finalPosition the score of final position
    def finalPosition(self,current_status):
        comp_score=0
        # horizontal
        if current_status[0][0]==current_status[0][1] and current_status[0][1]==current_status[0][2]:
            if current_status[0][0]==self.select_player:
                comp_score-=1
            elif current_status[0][0]==self.comp_selection:
                comp_score+=1
        if current_status[1][0]==current_status[1][1] and current_status[1][1]==current_status[1][2]:
            if current_status[1][0]==self.select_player:
                comp_score-=1
            elif current_status[1][0]==self.comp_selection:
                comp_score+=1
        if current_status[2][0]==current_status[2][1] and current_status[2][1]==current_status[2][2]:
            if current_status[2][0]==self.select_player:
                comp_score-=1
            elif current_status[2][0]==self.comp_selection:
                comp_score+=1

        # vertical
        if current_status[0][0]==current_status[1][0] and current_status[1][0]==current_status[2][0]:
            if current_status[0][0]==self.select_player:
                comp_score-=1
            elif current_status[0][0]==self.comp_selection:
                comp_score+=1
        if current_status[0][1]==current_status[1][1] and current_status[1][1]==current_status[2][1]:
            if current_status[0][1]==self.select_player:
                comp_score-=1
            elif current_status[0][1]==self.comp_selection:
                comp_score+=1
        if current_status[0][2]==current_status[1][2] and current_status[1][2]==current_status[2][2]:
            if current_status[0][2]==self.select_player:
                comp_score-=1
            elif current_status[0][2]==self.comp_selection:
                comp_score+=1

        # diagonals
        if current_status[0][0]==current_status[1][1] and current_status[1][1]==current_status[2][2]:
            if current_status[0][0]==self.select_player:
                comp_score-=2
            elif current_status[0][0]==self.comp_selection:
                comp_score+=2
        if current_status[2][0]==current_status[1][1] and current_status[1][1]==current_status[0][2]:
            if current_status[2][0]==self.select_player:
                comp_score-=2
            elif current_status[2][0]==self.comp_selection:
                comp_score+=2
        return comp_score
    
if __name__=='__main__':
    print('Everything is working Fine!')