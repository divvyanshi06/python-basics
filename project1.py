import datetime

def add_mood():
    today = datetime.date.today()
    mood = input("How are you feeling today? 😌: ")
    entry = f"{today} - Mood: {mood}\n"

    with open("mood_journal.txt", "a") as file:
        file.write(entry)

    print("✅ Mood saved successfully!")

def view_mood_history():
    try:
        with open("mood_journal.txt", "r") as file:
            content = file.read()
            if content.strip() == "":
                print("No mood entries found yet.")
            else:
                print("\n📖 Your Mood History:")
                print("---------------------")
                print(content)
    except FileNotFoundError:
        print("Mood journal not found. Add a mood first!")

# Main menu loop
while True:
    print("\n🧠 Mental Wellness Mood Journal")
    print("1. Add Mood")
    print("2. View Mood History")
    print("3. Exit")

    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        add_mood()
    elif choice == '2':
        view_mood_history()
    elif choice == '3':
        print("👋 Exiting Mood Journal. Take care!")
        break
    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")
