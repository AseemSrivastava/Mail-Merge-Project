PLACEHOLDER = "[name]"

#Reading list of names from invited_names file
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

#Reading body of letter from starting_letter file
with open("./Input/Letters/starting_letter.txt") as letters_file:
    letter_content = letters_file.read()
    for name in names:
        stripped_name = name.strip() #Remove leading and trailing spaces
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)

        #open/create the file for each person separately with a letter addressing to that person.
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as final_letter:
            final_letter.write(new_letter)