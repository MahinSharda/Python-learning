import datetime
name = input("What is your name ? ").strip()
age = input("How old are you ? ").strip()
city = input("Which city do you live in ? ").strip()
profession = input("What is your profession ? ").strip()
hobby = input("What is your favourite hobby ? ").strip()

intro_message = (
    f"Hello! My name is {name}, I'm {age} years old and live in {city} "
    f"I work as a {profession} and I absoultely enjoy {hobby} in my free time"
    f"Nice to meet youuu!!!\n"
) 

currentdate = datetime.date.today().isoformat()


border = "*" * 80
final_output = f"{border}\n{intro_message}\n{currentdate}\n{border}"
print(final_output)