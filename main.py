import random
import string

def get_random():
    letters = string.ascii_lowercase
    s = ""
    for i in range(3):
        s = s + random.choice(letters)
    return s


print("secret code tool")
print("---------------")

msg = input("enter your message: ")
choice = input("1 for coding, 0 for decoding: ")

words = msg.split(" ")
final = []

if choice == "1":
    for word in words:
        if len(word) < 3:
            final.append(word[::-1])
        else:
            r1 = get_random()
            r2 = get_random()

            new = r1 + word[1:] + word[0] + r2
            final.append(new)

    print("encoded:")
    print(" ".join(final))


elif choice == "0":
    for word in words:
        if len(word) < 3:
            final.append(word[::-1])
        else:
            cut = word[3:-3]
            original = cut[-1] + cut[:-1]
            final.append(original)

    print("decoded:")
    print(" ".join(final))


else:
    print("wrong input")
