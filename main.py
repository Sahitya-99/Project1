import time
print("🧠 know your personality")
print("✨ Let's discover who you really are with some fun data magic!")
print("="*60)
Name=input("enter you name :")
age=int(input("enter you age :"))
city=input("enter the city u live :")
color=input("enter your fav color :")
food=input("enter ur fav food :")
animal=input("🐾 Your Spirit Animal :")
hobby=input("One Thing You LOVE Doing :")

if 0 >= age <= 18:
    tribe = "Young Explorer"
elif 19 >= age <= 30:
    tribe = "Adventurer"
else:
    tribe = "Wise Owl"

print("🔍 Scanning colors, foods, and animal energies...")
time.sleep(3)
print("💫 Calculating your personality type using complex non-scientific logic...")
time.sleep(3)
print("🎉 Hey Sahitya, here's your fun personality report!")

print(f"You're from {city}, a place of dreams!")
print(f"🍿 You love {food} and enjoy doing {hobby}.")
print(f"🎨 You vibe with the color {color} and your spirit animal is the {animal}.")
print(f"📅 You've lived approximately {age*12} months already.")
print(f"🧩 You belong to the 'Wise Owl' {tribe}.")
personality_code = Name[:2].upper() + str(age)[-1] + animal[0].upper() + color[0].upper()
print(f"🔐 Your Secret Personality Code is: {personality_code}")
time.sleep(3)
print("💡 Time to explore more hobbies? You’ve got hidden sparks waiting!")
time.sleep(3)
print("🌈 You are officially certified as: FUNKY AND FABULOUS! 😎")
