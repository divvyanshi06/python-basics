import datetime

# Get today's date
today = datetime.date.today()

# Ask user for mood
mood = input("How are you feeling today? 😌: ")

# Format the mood entry
entry = f"{today} - Mood: {mood}\n"

# Save it to a file
with open("mood_journal.txt", "a") as file:
    file.write(entry)

print("✅ Mood saved successfully!")
