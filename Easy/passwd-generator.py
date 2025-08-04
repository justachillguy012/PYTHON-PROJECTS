import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("WELCOME TO THE PASSWORD GENERATING SYSTEM, KING 👑")

    try:
        length = int(input("ENTER HOW LONG YOU WANT YOUR PASSWORD: "))

        if length <= 0:
            print("⚠️ YOUR PASSWORD LENGTH MUST BE A POSITIVE NUMBER.")
            return  # Exit the function early if invalid

        password = generate_password(length)
        print("✅ PASSWORD GENERATED:", password)

    except ValueError:
        print("❌ YO KING, ENTER A VALID NUMBER!")

if __name__ == "__main__":
    main()
