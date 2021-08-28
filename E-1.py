L=1
R=1
l=1
r=1
def split1(c,x,y):
    global L,R                                  #split for player 1
    if(c=='L'):
        L1=L
        L=((L*(x))//(x+y))
        R=(L1-L)
    elif(c=='R'):
        R1=R
        R=((L*(y))//(x+y))
        L=R1-R
    else:
        print("invalid Entry")
def split2(c,x,y):                                
    global l,r  
    if(c=='L'):                                     #split for player 2
        l1=l
        l=((l*(x))//(x+y))
        r=(l1-l)
    elif(c=='R'):
        r1=r
        r=((r*(y))//(x+y))
        l=r1-r
    else:
        print("invalid Entry")
def attack1(af1,at1):                           #attack from player 1 to player 2
    global L,R,l,r
    if(af1=='L' and at1=='L'):
        l+=L
    elif (af1=='L' and at1=='R'):
        r+=L
    elif (af1=='R' and at1=='L'):
        l+=R
    elif (af1=='R' and at1=='R'):
        r+=R
    else:
        print("Invalid Entry")
def attack2(af2,at2):
    global L,R,l,r                                   #attack from player 2 to player 1
    if(af2=='L' and at2=='L'):
        L+=l
    elif (af2=='L' and at2=='R'):
        R+=l
    elif (af2=='R' and at2=='L'):
        L+=r
    elif (af2=='R' and at2=='R'):
        R+=r
    else:
        print("Invalid Entry") 
def update():
    global L,R,l,r
    if(l==5):
        l=0
    elif(L==5):
        L=0
    elif(R==5):
        R=0
    elif(r==5):
        r=0
def main():
    global L,R,l,r
    print("Current status:\nPlayer1: ",L,R,"\nPlayer2:",l,r,"\n")
    while ((l<=5 and r<=5) and (L<=5 and R<=5)):
        print("Press A for Attack and Press S for split ")
        c1=input("Enter move for Player 1:")
        if (c1=='A'):
            print("Enter the move combination in the form of L<space>R [Left hand to opponent's right hand]")
            s=str(input("Enter the move combination -"))                                                                  #TURN FOR PLAYER 1
            attack1(s[0],s[2])
        elif (c1=='S'):
            print("Enter the move combination in the form of 'L<space>1<space>1' [Split Left hand i nto 1(Left Hand) & 1(Right Hand)]")
            s1=str(input("Enter the move combination -"))
            x=int(s1[2])
            y=int(s1[4])
            split1(s1[0],x,y)
        else:
            print("Invalid Entry")
        update()                                                                                 #UPDATE WHEN ONE LIVE HAND HAS 5 FINGERS
        print("Current status:\nPlayer1: ",L,R,"\nPlayer2:",l,r,"\n")
        c2=input("Enter move for Player 2:")
        if (c2=='A'):
            print("Enter the move combination in the form of L<space>R [Left hand to opponent's right hand]")
            s3=str(input("Enter the move combination -"))
            attack2(s3[0],s3[2])                                                                                                #TURN FOR PLAYER 2
        elif (c2=='S'):
            print("Enter the move combination in the form of 'L<space>1<space>1' [Split Left hand i nto 1(Left Hand) & 1(Right Hand)]")
            s4=str(input("Enter the move combination -"))
            x=int(s4[2])
            y=int(s4[4])
            split2(s4[0],x,y)
        else:
            print("Invalid Entry")
        update()                                                                                    #UPDATE WHEN ONE LIVE HAND HAS 5 FINGERS
        print("Current status:\nPlayer1: ",L,R,"\nPlayer2:",l,r,"\n")
main()
