import random
movies=['anand','anbe sivam','vickram vedha','visvasam','mersal','kaaka kaaka','alaipayuthe','fidaa','lkg','taare zameen par']
def create_question(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if letters[i]==' ':
            temp.append(' ')
        else:
            temp.append('*')
        qn=' '.join(str(x) for x in temp)
        return qn


def is_present(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True


def unlock(qn,movie,letter):
    ref=list(movie)
    qn_list=list(qn)
    temp=[]
    n=len(movie)
    for i in range(n):
        if ref[i]==' ' or ref[i]==letter:
            temp.append(ref[i])
        else:
            if qn_list[i]=='*':
                temp.append('*')
            else:
                temp.append(ref[i])
        qn_new = ''.join(str(x) for x in temp)
        return qn_new







def play():
    p1name=input("enter the player1 name")
    p2name=input("enter the player2 name")
    pp1=0
    pp2=0
    turn=0
    willing=True
    while willing:
        if turn%2==0:
            #turn of player 1
            print(p1name,"its your turn")
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_ques=qn
            not_said=True
            while not_said:
                letter=input("your letter: ")
                if(is_present(letter,picked_movie)):
                    #unlock
                    modified_ques=unlock(modified_ques,picked_movie,letter)
                    print(modified_ques)
                    d=input("press \n\t1 to guess the movie\n\t2.unlock the character")
                    if d==1:
                        ans=input("your answer")
                        if ans==picked_movie:
                            pp1=pp1+1
                            print("correct")
                            not_said=False
                            print(p1name,"you win....your point is ",pp1)
                        else:
                            print("Wrong answer !! Try Again")


                    else:
                        print(letter,"letter not found")
            c=input("whether u need to continue ....\n press 0 to pause or 1 to continue\n")
            if c==0:
                print(p1name," Your score ",pp1)
                print(p2name," your score ",pp2)
                willing=False
        else:

            print(p2name, "its your turn")
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_ques=qn
            not_said = True
            while not_said:
                letter = input("your letter: ")
                if (is_present(letter, picked_movie)):
                    # unlock
                    modified_ques = unlock(modified_ques, picked_movie, letter)
                    print(modified_ques)
                    d = int(input("press \n\t1 to guess the movie\n\t2.unlock the character"))
                    if d == 1:
                        ans = input("your answer")
                        if ans==picked_movie:
                            pp1 = pp1 + 1
                            print("correct")
                            not_said = False
                            print(p1name, "you win....your point is ", pp1)
                        else:
                            print("Wrong answer !! Try Again")


                else:
                    print(letter, "letter not found")
            c =int(input("whether u need to continue ....\n press 0 to pause or 1 to continue\n"))
            if c == 0:
                print(p1name, " Your score ", pp1)
                print(p2name, " your score ", pp2)
                willing = False
            turn=turn+1

play()
