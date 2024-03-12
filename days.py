print("Welcome to Days.com")

while True:
    day = input("What day is it today? ").lower()  

    while day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
        print("Hmmm, I don't know that one. Please enter a valid day of the week.")
        day = input("What day is it today? ").lower()

    match day:
        case "monday":
            print("Monday is the Moon's day.")
        case "tuesday":
            print("Tuesday is Tyr's Day. He is the God of War and Justice.")
        case "wednesday":
            print("Wednesday is Woden's Day. Woden is the Father of all other Gods and very wise.")
        case "thursday":
            print("Thursday is Thor's Day. He is the God of Thunder.")
        case "friday":
            print("Friday is for Freya. She is the lady of love, fertility and beauty.")
        case "saturday":
            print("Saturday is for bathing. Make sure you are squeaky clean.")
        case "sunday":
            print("Sunday is, indeed, the Sun's day.")
    
    moreInfo = input(f"Would you like to learn more about {day}? Y/N ").lower()

    if moreInfo == "y" and day == "monday":
        print("The Moon is associated with silver, receptive energy and transformation.")
    elif moreInfo == "y" and day == "tuesday":
        print("Tyr is a noble and brave God who lost his right arm to Fenrir. This is a day for bravery and to face conflict head on.")
    elif moreInfo == "y" and day == "wednesday":
        print("Wednesday is a good day for communication and negotiation.")
    elif moreInfo == "y" and day == "thursday":
        print("Thursdays are good days to launch new ventures and hear outcomes of ongoing matters. Thursdays are days of happiness and expansion.")
    elif moreInfo == "y" and day == "friday":
        print("Fridays are great for matters of heart and home.")
    elif moreInfo == "y" and day == "saturday":
        print("Saturdays are days of virtue and discipline.")
    elif moreInfo == "y" and day == "sunday":
        print("Sunday is a good day to practice affirmations and elevate your self-esteem.")
    elif moreInfo == "n":
        print("Alrighty, bye-bye.")
        break  
    else:
        print("Please only type 'Y' for yes or 'N' for no.")