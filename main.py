import random
import string 

def get_random():
   letters = string.ascii_lowercase0
   return "".join(random.choice(letters) for _ in range(3))


print("secret code tool")
print("____________________")


msg = input("Enter your massage")
choice = input ("Press 1 for coding or 0 for Decoding")

words = msg.split()

result = []

if choice == "1"
    for W in words:
      if len(W) >= 3:
         start = get_random()
         end = get _random()
              
         new_word = start + W[1:] + end
         result.append(w[::-1]) 
   else:
         result.append(w[::-1])

 print("\nEncoded Massage:")
 print(" ".join(result))

elif choice == "0":
    for w in word:
        if len(w) >= 3:

          temp = w [3:-3]

           original = temp[-1] + temp[:-1]
           result.append(original)
else:
      result.appen(w[::-1])


   print("\nDecoded Message")
   print(" ".join(result))
  


else:
   print("Invalid input! Please enter 1 or 0.")




 
