def main():
    print ("\n\n\nYou sneak into your neighbor's house just like a typical nosy person would. You suspect they're a top-secret spy for the FBI who's planning to kill you. \nHowever, after sneaking in, the door slams shut behinf you. You're trapped! Escape before they find you!")
    print ("You will have clues to escape, so be alert\n")
    print ("You start off in the living room. There's a closet inside. Open it.\n")
    bool_var = True
    key_cnt = 0
    neg_key_cnt = 0
    print ("You find a vault inside the closet. \n On top of the vault is a question \n\n")
    print ("Question: What are the effects of overfishing? A- A warmer atmosphere, B- Disrupted Food Chain, C- Bleached Coral Reefs, \nD- Too many fish in the ocean \n\n")
    selection = input()
    while (bool_var):
        if (key_cnt == 0):
            if (key_cnt == 0) and (neg_key_cnt == 0):
                if (selection.upper() == "B"):
                    key_cnt += 1
                    print ("\nCorrect! The vault has opened. Inside is a key. \n\nFast Fact: Fisheries capture over 100 million sharks from our oceans every year? They're removing both predators and prey from bodies of water, an imbalanced ecosystem.\n\n")        
                   
                else:
                    neg_key_cnt = neg_key_cnt -1
                    print ( selection, "is not the correct answer. Try again")
                    selection = input()
            elif (neg_key_cnt < 0):
                if (selection.upper() == "B"):
                    key_cnt += 1
                    neg_key_cnt += 1
                    print ("\nCorrect! The vault has opened. Inside is a key. Before you go to the next room, did you know that fisheries capture over 100 million sharks from our oceans every year? They're removing both predators and prey from bodies of water, an imbalanced ecosystem.\n\n")
                    
                elif (selection.upper() != "B"):
                    print ("\nDo you want a hint?")
                    hint = input()
                    if (hint == "y"):
                        print ("\nMarine life depends on organisms in their ecosystem for food and survival. \nWhen a mass amount of their energy sources are diminished, this creates instability and imbalance.\n\n")
                        print ("\nTry again, and enter another answer")
                        selection = input()
                        if (selection.upper() == "B"):
                            key_cnt += 1
                            print ("\nCorrect! The vault has opened. Inside is a key. \nBefore you go to the next room,  did you know that fisheries capture over 100 million sharks from our oceans every year? They're removing both predators and prey from bodies of water, an imbalanced ecosystem.\n\n")
                            neg_key_cnt += 1
                        else:
                            print ("\nYour neighbor found you. You can't escape now")
                            break
                    elif (hint == "n"):
                        print ("\nTry again, and enter another answer")
                        selection = input()
                        if (selection.upper() == "B"):
                            key_cnt += 1
                            print ("Correct! The vault has opened. Inside is a key. \nFast Fact: Did you know that fisheries capture over 100 million sharks from our oceans every year? They're removing both predators and prey from bodies of water, an imbalanced ecosystem.\n\n")
                            neg_key_cnt += 1
                            
                        else:
                            print ("Your neighbor found you. You can't escape now\n\n")
                            break
                            
                                   
        
        elif(key_cnt == 1):
            if (neg_key_cnt == 0):
                neg_key_cnt = 0
                print ("----------You've entered the master bedroom---------")
                print ("After rummaging through all the drawers you find a box with a padlock. Inscripted on the metal is a question.\n\n")
                print ("Question: What is the MAIN cause of water scarcity?")
                print ("A- Droughts, B- Lack of clouds, C- Agriculture, D- People drinking too much water")
                selection = input()
                if (selection.upper() == "C"):
                    key_cnt += 1
                    print ("Correct! The box has opened. Inside is another key. \n Fast Fact: Over 770 million people don't have access to clean water? \n This is due to people's ethnicity, gender, and social statuses.\n\n")                    
                elif (selection.upper() != "C"):
                    neg_key_cnt = -1
                    print ("Incorrect,", selection, "is not the correct answer. Try again")
                    
            elif (neg_key_cnt == -1):
                print ("Enter another answer")
                selection = input()
                if (selection.upper() == "C"):
                    key_cnt += 1
                    neg_key_cnt +=1
                    print ("Correct! The box has opened. Inside is another key, to take you to the bathroom. \n Fast fact: Over 770 million people don't have access to clean water.\n This is due to people's ethnicity, gender, and social statuses.\n\n")
                    
                elif (selection.upper() != "C"):
                    print ("Do you want a hint? y/n")
                    hint = input()
                    if (hint == "y"):
                        print ("It has to do with the amount of water animals consume.")                        
                        print ("Now enter another answer")
                        selection = input()
                        if (selection.upper() == "C"):
                            key_cnt += 1
                            print ("Correct! The box has opened. Inside is another key. \n Fast Fact: Over 770 million people don't have access to clean water? \n This is due to people's ethnicity, gender, and social statuses.\n\n")                            
                            neg_key_cnt += 1
                        else:
                            print ("Your neighbor found you. You can't escape now")
                            break
                        
                    elif (hint == "n"):
                        print ("Try again, and enter another answer")
                        selection = input()
                        if (selection.upper() == "C"):
                            key_cnt += 1
                            print ("Correct! The box has opened. Inside is another key. \nFast Fact: did you know that over 770 million people don't have access to clean water? \n This is due to people's ethnicity, gender, and social statuses.\n\n")                            
                            neg_key_cnt += 1    
                        else:
                            print ("Your neighbor found you. You're trapped") 
                            break             
                   
        elif(key_cnt == 2):    
            if (neg_key_cnt == 0):
                neg_key_cnt = 0
                print ("-----You've entered the bathroom-------")
                print ("Under the sink is a cabinet with a box in it. It has a note with a question.")
                print ("Question: Which of these countries is the biggest polluter?")
                print ("A- US, B- China, C- Brazil, D- Russia")
                selection = input()
                if (selection.upper() == "A"):
                    key_cnt += 1
                    print ("Correct! The box has opened. Inside is another key. \n\nFast fact: The United States contribuets to 28 percent of global carbon emissions. This is due to burning fossil fuels for electricity and transportation\n\n")
                elif (selection.upper() != "A"):
                    neg_key_cnt = -1
                    print ("Incorrect,", selection, "is not the correct answer. Try again")
                    
            elif (neg_key_cnt < 0):
                print ("Enter another answer")
                selection = input()
                if (selection.upper() == "A"):
                    key_cnt += 1
                    neg_key_cnt +=1
                    print ("Correct! The box has opened. Inside is another key. \n\nFast fact: The United States contribuets to 28 percent of global carbon emissions. This is due to burning fossil fuels for electricity and transportation\n\n")                
                elif (selection.upper() != "A"):
                    print ("Do you want a hint? y/n")
                    hint = input()
                    if (hint.lower() == "y"):
                        print ("It's the country with the highest economy.")                        
                        print ("Now enter another answer")
                        selection = input()
                        if (selection.upper() == "A"):
                            key_cnt += 1
                            print ("Correct! The box has opened. Inside is another key. \n\nFast fact: The United States contribuets to 28 percent of global carbon emissions. This is due to burning fossil fuels for electricity and transportation\n\n")                            
                            neg_key_cnt += 1
                        else:
                            print ("Your neighbor found you. You're trapped")
                            break
                        
                    elif (hint.lower() == "n"):
                        print ("Try again, and enter another answer")
                        selection = input()
                        if (selection.upper()  == "A"):
                            key_cnt += 1
                            print ("Correct! The box has opened. Inside is another key. \n\nFast fact: The United States contribuets to 28 percent of global carbon emissions. This is due to burning fossil fuels for electricity and transportation\n\n")                            
                            neg_key_cnt += 1      
                        else:
                            print ("Your neighbor found you. You're trapped") 
                            break     
                 
        elif(key_cnt == 3):    
            if (neg_key_cnt == 0):
                neg_key_cnt = 0
                print ("-----You are now in the kitchen------")
                print ("After frantically running around, you find yourself in the pantry. Here, there is a cookie jar which has a lock. \nTry to answer the question below and find the key.\n\n\n")
                print ("Question: What can we do to stop deforestation?")
                print (" A-Shorter showers, B- Drink less water, C- Make your own paper, D- Plant a tree")
                selection = input()
                if (selection.upper() == "D"):
                    key_cnt += 1
                    print ("Correct! The box has opened. Inside is another key. \n\nFast fact: One football field worth of forests are being lost every second, every day. This is a 9 percent reduction in global tree cover since 2000, according to The World Counts.\n\n")
                else:
                    neg_key_cnt = -1
                    print ("Incorrect,", selection, "is not the correct answer. Try again")
                        
            elif (neg_key_cnt < 0):
                print ("Enter another answer")
                selection = input()
                if (selection.upper() == "D"):
                    key_cnt += 1
                    neg_key_cnt +=1
                    print ("Correct! The box has opened. Inside is another key. \n\nFast fact: One football field worth of forests are being lost every second, every day. This is a 9 percent reduction in global tree cover since 2000, according to\n the website The World Counts.\n\n")                
                elif (selection.upper() != "D"):
                    print ("Do you want a hint? y/n")
                    hint = input()
                    if (hint.lower() == "y"):
                        print ("You need to replace what has been lost")                        
                        print ("Now enter another answer")
                        selection = input()
                        if (selection.upper()  == "D"):
                            key_cnt += 1
                            print ("Correct! The box has opened. Inside is another key. \n\nFast fact: The United States contribuets to 28 percent of global carbon emissions. This is due to burning fossil fuels for electricity and transportation\n\n")                            
                            neg_key_cnt += 1
                        else:
                            print ("Your neighbor got you. You're trapped now")
                            break
                        
                    elif (hint.lower() == "n"):
                        print ("Try again, and enter another answer")
                        selection = input()
                        if (selection.upper()  == "D"):
                            key_cnt += 1
                            print ("Correct! The box has opened. Inside is another key. \n\nFast fact: The United States contribuets to 28 percent of global carbon emissions. This is due to burning fossil fuels for electricity and transportation\n\n")                            
                            neg_key_cnt += 1    
                        else:
                            print ("Your neighbor found you. You're trapped now")   
                            break     
                        
        elif (key_cnt == 4):
            print ("-You made it to the garage!-")
            print ("There's a PIN you need to enter to open the garage door. Enter the letters of the answers above to escape.")
            final_code = input()
            if (final_code.upper() == "BCAD"):
                print ("\n\nYou escaped!\n\n")
                break
            elif (final_code.upper() != "BCAD"):
                neg_key_cnt = -1
                print ("Someone's opening door to enter the garage. Quickly try again!")
                final_code = input()
                if (final_code.upper() == "BCAD"):
                    print ("\n\nYou escaped!\n\n")
                    break
                elif (final_code.upper() != "BCAD"):
                    print ("The door has been opened. Game Over.")
                    break
    if (key_cnt ==4):
        print ("Turns out your neighbor wasn't an FBI agent out to kill you. She was actually just a climate change activist.")
        print ("She was only being cold to you as you didn't install solar panels, and because drive a car that runs on fossil fuels.")
        print ("")
main()