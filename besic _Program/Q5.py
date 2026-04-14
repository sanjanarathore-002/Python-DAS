# multiple condition if else statement

hindi=int(input("enter the marks of hindi subject:"));
english=int(input("enter the marks of english subject:"));
math=int(input("enter the marks of math subject:"));
history=int(input("enter the marks of history subject:"));

total=hindi+english+math+history;
precentage=(total/400)*100;

if hindi>=33:
    if english>=33:
        if math>=33:
            if history>=33:
                print("congratulation you are pass");
              
                print("total :",total);
                print("precentage :",precentage);
                if hindi>90 and english>90 and math>90 and history>90:
                    print("you are pass with A grade");
                    print("total:",)
                    if hindi>80 and english>80 and math>80 and history>80:
                        print("you are pass with B grade");
                        if hindi>70 and english>70 and math>70 and history>70:
                            print("you are pass with C grade");
            else:
                print("you are fail in history subject");
        else:
            print("you are fail in math subject");
    else:
        print("you are fail in english subject");