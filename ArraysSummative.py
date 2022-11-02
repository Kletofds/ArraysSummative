###################################################
# Kelton Figurski
# Arrays Summative
###################################################

import time

# ---------------------- Lists ---------------------- #

# creates dictionaries for each class
english = {}
math = {}
history = {}
science = {}
physed = {}

classes = [] # creates a list for the classes added

# ---------------------- Functions ---------------------- #

# function to add people to class
def addfunc(classname):
    while True:
        student = input("What is the name of the student?")
        mark = input("What mark did that student get?")
        classname[student] = mark
        
        while True:
            cont = input("\nWould you like to add more students?")
            cont = cont.lower()
       
            if cont != "yes" and cont != "no":
                print("\nType 'yes' or 'no'")
                
                time.sleep(1)
            
            else:
                break
                
        if cont == "no":
            break   

# function to remove students from class
def removestudent(classname):   
    while True:
        print(f"\nCurrent Class Marks: {classname}")
        

        removestudent = input("What student would you like to remove?")
        
        if removestudent not in classname:
            print("\nThat student is not in that class?")
            time.sleep(3)
            break
        
        del classname[removestudent]
        
        while True:
            delcont = input("\nWould you like to remove more students?")
            delcont = delcont.lower()
            
            if delcont != "yes" and delcont != "no":
                print("Type 'yes' or 'no'")
                
            else:
                break
            
        if delcont == "no":
            break
        

# ---------------------- Main Code ---------------------- #

while True: # Starts a loop 
    
    while True:
        #Asks the user what they want to do
        action = input("""
What would you like to do?
    1: Add a class
    2: Add student to  previous class 
    3: Remove student from previous class
    4: Delete a class
    5: Print Marks
    6: Exit
""")
        
        if action != "1" and action != "2" and action != "3" and action != "4" and action != "5" and action != "6":
            print("Type '1', '2', '3', '4', '5', or '6'")
            time.sleep(3)
        
        else:
            break
        
    # Adds student to a class if the student wants
    if action == "1" or action == "2":
        
        print("""
Available Classes:
    English
    Math
    History
    Science
    PhysEd
""")

        time.sleep(3)

        class1 = input("What class would you like to add marks for?")
        class1 = class1.lower()

        if class1 == "english":
            addfunc(english)
            
            if "english" not in classes:
                classes.append("english")

        elif class1 == "math":
            addfunc(math)
            
            if "math" not in classes:
                classes.append("math")

        elif class1 == "history":
            addfunc(history)
            
            if "history" not in classes:
                classes.append("history")

        elif class1 == "science":
            addfunc(science)
            
            if "science" not in classes:
                classes.append("science")

        elif class1 == "physed":
            addfunc(physed)
            
            if "physed" not in classes:
                classes.append("physed")
            
        
    # removes student from class if user wants
    elif action == "3":
        removeaction = input("\nWhat class would you like to remove students from?")
        removeaction = removeaction.lower()
        
        if removeaction == "english" and "english" in classes:
            removestudent(english)
                
        elif removeaction == "math" and "math" in classes:
            removestudent(math)
            
        elif removeaction == "history" and "history" in classes:
            removestudent(history)
            
        elif removeaction == "science" and "science" in classes:
            removestudent(science)
            
        elif removeaction == "physed" and "physed" in classes:
            removestudent(physed)
        
    # Deletes a class if the user wants    
    elif action == "4":
        delclass = input("What class would you like to delete?")
        delclass = delclass.lower()
        
        if delclass not in classes:
            print("That is not a current class")
            continue
        
        if delclass == "english":
            english.clear()
            classes.remove("english")
        
        elif delclass == "math":
            math.clear()
            classes.remove("math")
            
        elif delclass == "science":
            science.clear()
            classes.remove("science")
            
        elif delclass == "physed":
            physed.clear()
            classes.remove("physed")
            
        elif delclass == "history":
            history.clear()
            classes.remove("history")
        
    # Prints all added classes and marks if the user wants
    elif action == "5":
        if "english" in classes:
            print(f"\nEnglish: {english}")
            
        if "math" in classes:
            print(f"\nMath: {math}")
            
        if "science" in classes:
            print(f"\nScience: {science}")
            
        if "history" in classes:
            print(f"\nHistory: {history}")
            
        if "physed" in classes:
            print(f"\nPhysEd: {physed}")
            
        while True:
            time.sleep(3)
            printcont = input("\nWould you like to make more changes?")
            printcont = printcont.lower()
            
            if printcont != "yes" and printcont != "no":
                print("Type 'yes' or 'no'")
                
            else:
                break
            
        if printcont == "no":
            break
    
    # Ends the program if the user wants
    elif action == "6":
        break