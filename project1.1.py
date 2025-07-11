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

# Run this function
view_mood_history()
