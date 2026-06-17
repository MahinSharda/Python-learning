
import textwrap
name = input("What is your name ? ").strip()
profession = input("What's your profession ? ").strip()
passion = input("What's your passion ? ").strip()
emoji = input("Enter your favourite emoji ? ").strip()
website = input("Enter your handle ? ").strip()

print(f"\n Choose your style: ")
print(f"1. Simple Lines ")
print(f"2. Vertical Flair ")
print(f"3. Emoji Sandwich ")

style = input("Enter 1,2 or 3: ").strip()

def generate_bio(style):
    if style == "1":
        return f"{emoji} {name} | {professsion} \n 🧠 {passion} \n {website}"
    elif style == "2":
        return f"{emoji} {name} \n {profession} 🧠 \n {passion} \n {website}🧠 "
    elif style == "3":
        return f"{emoji*3}\n {name} - {profession}\n {passion} \n 🧠{website} \n {emoji*3}"

bio = generate_bio(style)

print(f"\n Your stylish bio ")
print(f"*" * 40)
print(textwrap.dedent(bio))
print(f"*" * 40)

save=input(f"Do you want to save this to a text file ? \n").lower()

if save == "yes":
    filename=f"{name.lower().replace(' ','_')}_bio.txt"
    with open(filename, "w", encoding = "utf-8") as f:
        f.write(bio)
    print("File saved")    