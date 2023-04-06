import cv2
from cvzone.HandTrackingModule import HandDetector
cap=cv2.VideoCapture(0)


class button :
    def __init__(self,pos,width,heigth,value):
        self.pos=pos
        self.width=width
        self.heigth=heigth
        self.value=value
    def draw(self,img):
        
        cv2.rectangle(img,self.pos,(self.pos[0]+self.width ,self.pos[1]+self.heigth),(255,255,255),cv2.FILLED)
        cv2.rectangle(img,self.pos,(self.pos[0]+self.width ,self.pos[1]+self.heigth),(50,50,50),3)
        cv2.putText(img,self.value,(self.pos[0]+40,self.pos[1]+60),cv2.FONT_HERSHEY_PLAIN,2,(50,50,50),2)

cap.set(3,1280)
cap.set(4,720)

detector=HandDetector(detectionCon=0.8,maxHands=1)
buttonlistvalue=[

    ['7','8','9','*'],
    ['4','5','6','+'],
    ['1','2','3','-'],
    ['0','/','.','='],
]


buttonlist=[]
for i in range(4):
    for j in range(4):
        xpos=i*100 +800
        ypos=j*100+150
        buttonlist.append(button((xpos,ypos),100,100,buttonlistvalue[j][i]))


myEquation='10+5'

while True:
    success,img =cap.read()
    img=cv2.flip(img,1)
    hands,img=detector.findHands(img,flipType=False)

    
    cv2.rectangle(img,(800,50),(800+400,70+100),(255,255,255),cv2.FILLED)
    cv2.rectangle(img,(800,50), (800+400,70+100),(50,50,50),3)

    for button in buttonlist:
        button.draw(img)





    # check hand

    if hands:
        lmList=hands[0]['lmList']
        # print(lmList[8],lmList[12])
        length,info,img=detector.findDistance(lmList[8][:2], lmList[12][:2],img)
        print(length)
        x,y=lmList[8][:2]
        if length<50:
            pass








    # Processiing

    #result
    cv2.putText(img,myEquation,(810,120),cv2.FONT_HERSHEY_PLAIN,3,(50,50,50),3)




    cv2.imshow("Image", img)
    cv2.waitKey(1)