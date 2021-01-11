#Guilherme Consiglio Gasperotto - 161157
#Guilherme Proença Cravo da Costa - 160068

from cv2 import cv2
import numpy as np
import glob

for g in glob.glob("jogos/*.jpg"):
    cont_x = 0
    cont_o = 0
    flag_x = 0
    flag_o = 0

    img = cv2.imread(g, cv2.IMREAD_COLOR)  
    img = cv2.resize(img,(600,600))  

    img2 = cv2.GaussianBlur(img, (5,5), 0)
    _,img2 = cv2.threshold(img,115,255,cv2.THRESH_BINARY_INV)

    img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    
    _,img2 = cv2.threshold(img2,127,255,0)
   
    contours, hierarchy = cv2.findContours(img2,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
    hierarchy = hierarchy[0]
      
    for i in zip(contours,hierarchy):
        contorno_atual = i[0]
        hierarquia_atual = i[1]
        x,y,w,h = cv2.boundingRect(contorno_atual)
        
        aux_x = 0
        aux_o = 0

        if (hierarquia_atual[3] < 0):            
            if (hierarquia_atual[0] > -1 and x+w>50 and h>70 and w<100):
                cv2.rectangle(img, (x,y), (x+w,y+h),(0,0,255), 2)
                aux_x = 1
                # Verifica de há 3 "X" na primeira coluna
                if (x < 150 and y > 400 and flag_x == 0):
                    flag_x = 1    
                if (x < 150 and y < 300 and flag_x == 1):
                    flag_x = 2
                if (x < 150 and y < 150 and flag_x == 2):
                    flag_x = 3
                
                # Verifica de há 3 "X" na segunda coluna
                if (x > 150 and x < 300 and y > 350 and flag_x == 0):
                    flag_x = 1    
                if (x > 150 and x < 300 and y > 200 and y < 250 and flag_x == 1):
                    flag_x = 2
                if (x > 150 and x < 300 and y < 150 and flag_x == 2):
                    flag_x = 3
                
                # Verifica de há 3 "X" na terceira coluna
                if (x > 400 and y > 400 and flag_x == 0):
                    flag_x = 1     
                if (x > 400 and y > 200 and y < 300 and flag_x == 1):
                    flag_x = 2
                if (x > 400 and y < 150 and flag_x == 2):
                    flag_x = 3

                # Verifica de há 3 "X" na primeira linha
                if (x < 150 and y < 150 and flag_x == 0): 
                    flag_x = 1      
                if (x > 350 and y < 150 and flag_x == 1):
                    flag_x = 2
                if (x > 200 and  y < 150 and flag_x == 2):
                    flag_x = 3

                # Verifica de há 3 "X" na segunda linha
                if (x < 150 and y > 200 and y < 300 and flag_x == 0):
                    flag_x = 1    
                if (x > 200 and x < 300 and y > 200 and y < 300 and flag_x == 1):
                    flag_x = 2
                if (x > 300 and y > 200 and y < 300 and flag_x == 2):
                    flag_x = 3

                # Verifica de há 3 "X" na terceira linha
                if (x > 350 and y > 350 and flag_x == 0):
                    flag_x = 1
                if (x > 350 and y > 200 and y < 300 and flag_x == 1):
                    flag_x = 2
                if (x > 350 and y < 150 and flag_x == 2):
                    flag_x = 3

            elif (hierarquia_atual[0] > -1 and x+w>50 and h>70 and w>100 and w<200):
                cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0), 2)
                aux_o = 1
                # Verifica de há 3 "O" na primeira coluna
                if (x < 150 and y > 400 and flag_o == 0):
                    flag_o = 1    
                if (x < 150 and y < 300 and flag_o == 1):
                    flag_o = 2
                if (x < 150 and y < 150 and flag_o == 2):
                    flag_o = 3
                
                # Verifica de há 3 "O" na segunda coluna
                if (x > 150 and x < 300 and y > 350 and flag_o == 0):
                    flag_o = 1    
                if (x > 150 and x < 300 and y > 200 and y < 250 and flag_o == 1):
                    flag_o = 2
                if (x > 150 and x < 300 and y < 150 and flag_o == 2):
                    flag_o = 3
                
                # Verifica de há 3 "O" na terceira coluna
                if (x > 400 and y > 400 and flag_o == 0):
                    flag_o = 1     
                if (x > 400 and y > 200 and y < 300 and flag_o == 1):
                    flag_o = 2
                if (x > 400 and y < 150 and flag_o == 2):
                    flag_o = 3

                # Verifica de há 3 "O" na primeira linha
                if (x < 150 and y < 150 and flag_o == 0): 
                    flag_o = 1    
                if (x > 350 and y < 150 and flag_o == 1):
                    flag_o = 2
                if (x > 200 and y < 150 and flag_o == 2):
                    flag_o = 3
                
                # Verifica de há 3 "O" na segunda linha
                if (x < 150 and y > 200 and y < 300 and flag_o == 0):
                    flag_o = 1    
                if (x > 200 and x < 300 and y > 200 and y < 300 and flag_o == 1):
                    flag_o = 2
                if (x > 300 and y > 200 and y < 300 and flag_o == 2):
                    flag_o = 3

                # Verifica de há 3 "O" na terceira linha
                if (x > 350 and y > 350 and flag_o == 0):
                    flag_o = 1
                if (x > 350 and y > 200 and y < 300 and flag_o == 1):
                    flag_o = 2
                if (x > 350 and y < 150 and flag_o == 2):
                    flag_o = 3
        
        if (aux_x == 1):
            cont_x = cont_x + 1
        if (aux_o == 1):
            cont_o = cont_o + 1
 
    cv2.putText(img, "X = ",(50,550),0,1,(255,0,0),2)
    cv2.putText(img, str(cont_x),(120,550),0,1,(255,0,0),2)

    cv2.putText(img, "O = ",(50,580),0,1,(255,0,0),2)
    cv2.putText(img, str(cont_o),(120,580),0,1,(255,0,0),2)

    if(cont_o >=(cont_x+2) or cont_x >= (cont_o+2) or flag_x == 3 and flag_o == 3):
        cv2.putText(img,"Jogo invalido",(25,25),0,1,(0,0,255),2)
    else:
        cv2.putText(img,"Jogo valido",(25,25),0,1,(0,0,255),2)   
    
    cv2.imshow('Jogo da Velha', img)
    cv2.waitKey(5000)

cv2.destroyAllWindows()