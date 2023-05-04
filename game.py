# import modules and libraries
import random
import pickle
import cv2
import numpy as np
from os import path
from TicTacToe import tictactoeMinimax

def gameEnd():
    bckgrd=cv2.blur(game.game_mode,(18,18))
    cv2.putText(bckgrd,'THANKS FOR PLAYING',(330,310),cv2.FONT_HERSHEY_COMPLEX,1,(255, 255, 255),2)
    with open('data.pak','wb') as f:
        pickle.dump(game.user_player, f)
        pickle.dump(game.comp_player,f)
        f.close()
    cv2.imshow('Tic Tac Toe with AI',bckgrd)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    exit()

# define mouse callback function
def mouse_event(event,x_position,y_position,*args):
    if cv2.EVENT_LBUTTONDOWN==event:
        if x_position>795 and x_position<925 and y_position>240 and y_position<300:
            gameEnd()
        elif x_position>645 and x_position<775 and y_position>240 and y_position<300:
            with open('data.pak','wb') as f:
                pickle.dump(0,f)
                pickle.dump(0,f)
                f.close()
            game.user_player=0
            game.comp_player=0
    if cv2.EVENT_LBUTTONDOWN==event and game.players_move:
        if x_position<210 and x_position>0:
            if y_position>0 and y_position<210 and game.game_status[0][0]==' ':
                game.game_status[0][0]=game.select_player
                game.board()
                game.moveDisplay()
                if game.comp_selection=='O':
                    cv2.rectangle(game.game_mode,(670,400),(800,530),game.move_colour,9)
                else:
                    cv2.rectangle(game.game_mode,(820,400),(950,530),game.move_colour,9)
                game.players_move=False
            elif y_position>210 and y_position<420 and game.game_status[1][0]==' ':
                game.game_status[1][0]=game.select_player
                game.board()
                game.moveDisplay()
                if game.comp_selection=='O':
                    cv2.rectangle(game.game_mode,(670,400),(800,530),game.move_colour,9)
                else:
                    cv2.rectangle(game.game_mode,(820,400),(950,530),game.move_colour,9)
                game.players_move=False
            elif y_position>420 and y_position<630 and game.game_status[2][0]==' ':
                game.game_status[2][0]=game.select_player
                game.board()
                game.moveDisplay()
                if game.comp_selection=='O':
                    cv2.rectangle(game.game_mode,(670,400),(800,530),game.move_colour,9)
                else:
                    cv2.rectangle(game.game_mode,(820,400),(950,530),game.move_colour,9)
                game.players_move=False
        elif x_position>210 and x_position<420:
            if y_position>0 and y_position<210 and game.game_status[0][1]==' ':
                game.game_status[0][1]=game.select_player
                game.board()
                game.moveDisplay()
                if game.comp_selection=='O':
                    cv2.rectangle(game.game_mode,(670,400),(800,530),game.move_colour,9)
                else:
                    cv2.rectangle(game.game_mode,(820,400),(950,530),game.move_colour,9)
                game.players_move=False
            elif y_position>210 and y_position<420 and game.game_status[1][1]==' ':
                game.game_status[1][1]=game.select_player
                game.board()
                game.moveDisplay()
                if game.comp_selection=='O':
                    cv2.rectangle(game.game_mode,(670,400),(800,530),game.move_colour,9)
                else:
                    cv2.rectangle(game.game_mode,(820,400),(950,530),game.move_colour,9)
                game.players_move=False
            elif y_position>420 and y_position<630 and game.game_status[2][1]==' ':
                game.game_status[2][1]=game.select_player
                game.board()
                game.moveDisplay()
                if game.comp_selection=='O':
                    cv2.rectangle(game.game_mode,(670,400),(800,530),game.move_colour,9)
                else:
                    cv2.rectangle(game.game_mode,(820,400),(950,530),game.move_colour,9)
                game.players_move=False
        elif x_position>420 and x_position<630:
            if y_position>0 and y_position<210 and game.game_status[0][2]==' ':
                game.game_status[0][2]=game.select_player
                game.board()
                game.moveDisplay()
                if game.comp_selection=='O':
                    cv2.rectangle(game.game_mode,(670,400),(800,530),game.move_colour,9)
                else:
                    cv2.rectangle(game.game_mode,(820,400),(950,530),game.move_colour,9)
                game.players_move=False
            elif y_position>210 and y_position<420 and game.game_status[1][2]==' ':
                game.game_status[1][2]=game.select_player
                game.board()
                game.moveDisplay()
                if game.comp_selection=='O':
                    cv2.rectangle(game.game_mode,(670,400),(800,530),game.move_colour,9)
                else:
                    cv2.rectangle(game.game_mode,(820,400),(950,530),game.move_colour,9)
                game.players_move=False
            elif y_position>420 and y_position<630 and game.game_status[2][2]==' ':
                game.game_status[2][2]=game.select_player
                game.board()
                game.moveDisplay()
                if game.comp_selection=='O':
                    cv2.rectangle(game.game_mode,(670,400),(800,530),game.move_colour,9)
                else:
                    cv2.rectangle(game.game_mode,(820,400),(950,530),game.move_colour,9)
                game.players_move=False
        cv2.imshow('Tic Tac Toe with AI',game.game_mode)
        cv2.waitKey(600)

# Create the window
cv2.namedWindow('Tic Tac Toe with AI')

# set mouse callback function
cv2.setMouseCallback('Tic Tac Toe with AI',mouse_event)

#! the game object
game=tictactoeMinimax()

bckgrd=cv2.blur(game.game_mode,(18,18))
cv2.putText(bckgrd,'Welcome to Tac Tac Toe!',(300,310),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
cv2.imshow('Tic Tac Toe with AI',bckgrd)
cv2.waitKey(1200)
if game.select_player=='X':
    cv2.rectangle(game.game_mode,(670,400),(800,530),game.move_colour,9)
else:
    cv2.rectangle(game.game_mode,(820,400),(950,530),game.move_colour,9)
game.board()
game.players_move=random.choice([True,False])

# start program loop
while True:
    
    cv2.imshow('Tic Tac Toe with AI',game.game_mode)
    game.board()
    if game.players_move:
        if game.comp_selection=='X':
            cv2.rectangle(game.game_mode,(670,400),(800,530),game.move_colour,9)
        else:
            cv2.rectangle(game.game_mode,(820,400),(950,530),game.move_colour,9)
    else:
        if game.comp_first_move:
            temp=random.choice([0,1])
            if temp:
                game.game_status[random.choice([0,2])][random.choice([0,2])]=game.comp_selection
            else:
                game.game_status[1][1]=game.comp_selection
            game.moveDisplay()
            game.comp_first_move=False
            game.players_move=True
            continue

        if game.checkGameOver(game.game_status):
            game.moveDisplay()
            if game.comp_selection=='X':
                cv2.rectangle(game.game_mode,(670,400),(800,530),game.move_colour,9)
            else:
                cv2.rectangle(game.game_mode,(820,400),(950,530),game.move_colour,9)
            cv2.imshow('Tic Tac Toe with AI',game.game_mode)
            cv2.waitKey(600)
            game.makeLine()
            game.resetMode()
            if game.players_move==False:
                game.comp_first_move=True
            continue

        if game.select_player=='X':
            cv2.rectangle(game.game_mode,(670,400),(800,530),game.move_colour,9)
        else:
            cv2.rectangle(game.game_mode,(820,400),(950,530),game.move_colour,9)
        best_move=(-1,-1)
        best_score=-999
        for i in range(3):
            for j in range(3):
                if game.game_status[i][j]==' ':
                    game.game_status[i][j]=game.comp_selection
                    score=game.minimax(game.game_status,9,False)
                    game.game_status[i][j]=' '
                    if score>best_score:
                        best_score=score
                        best_move=(i,j)
        game.game_status[best_move[0]][best_move[1]]=game.comp_selection
        game.players_move=True
        
    game.moveDisplay()
    cv2.imshow('Tic Tac Toe with AI',game.game_mode)
    if game.checkGameOver(game.game_status):
        cv2.waitKey(600)
        game.makeLine()
        game.resetMode()
        if game.players_move==False:
            game.comp_first_move=True

    if cv2.waitKey(1) & 0xff==ord('q'):
        gameEnd()