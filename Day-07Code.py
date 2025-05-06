# Day 7 - Email Validator & Username Extractor
# Topic: Strings and String Methods

# This Function to represent introduction of this assignment / Project. Starting with a little welcome message.
def show_intro():
    print("🔹 Welcome to Day 7 of Python 30-Day Challenge!")
    print("🔹 Topic: Strings & String Methods")
    print("📧 Today we’re validating emails and extracting usernames\n")

# Validates the email by checking for '@' and '.'
def ValidateEmail(email):

    # Removes extra spaces by using strip()
    email = email.strip() 

    # This returns false if '@' and '.' not in given email address with a error msg.
    if "@" not in email or "." not in email:
        return False, "❌ Invalid email: Missing '@' or '.'"
    
    # This returns false if the email starts and ends with @ and if not have characters length < 5
    if email.startswith("@") or email.endswith("@") or len(email) < 5:
        return False, "❌ Invalid email: Structure looks off or it's just too short"
    
    # Else return true.
    return True, "✅ Email format looks good!"

# Extracts user name from email, which was before @. Already basic checks are completed. 
def ExtractUsername(e):
    return e.split("@")[0]  

# main
def main():

    # calls show_intro() to print the basic introduction about project / assignment.
    show_intro()

    # Takes input from user and removes extra spaces from it by using .strip()
    user_input = input("📨 Enter your email address: ").strip() 

    # Validates the email by using ValidateEmail() function's functionality and returns status
    valid, status_msg = ValidateEmail(user_input)
    print(status_msg)

    # If the user's email is valid then it Extracts the user name from email by using ExtractUsername() function's functionality
    if valid:

        # Extracts user name and assign it to user_part
        user_part = ExtractUsername(user_input)

        # Displays user name (as raw format)
        print(f"👤 Username (raw): {user_part}")

        # Displays user name in lower-case form
        print(f"🔡 Lowercase: {user_part.lower()}")

        # Displays user name in upper-case form
        print(f"🔠 Uppercase: {user_part.upper()}")

        # Displays first 3 letters of user
        # If user name is less than 3
        if len(user_part) < 3:
            print(f"The user name '{user_input}' is too short...")  
        # If user name isn't less than 3
        else:
            print(f"✂️ First 3 letters: {user_part[:3]}")

        # If username consists of any '.' it will be replaced by '_'
        print(f"🔄 Clean username: {user_part.replace('.', '_')}") 
    
    # If user email isn't valid (not containing '@' '.')
    else:
        print("🚫 Please enter a valid email next time!")  
# calling main() to starting execution of program
if __name__ == "__main__":
    main()
