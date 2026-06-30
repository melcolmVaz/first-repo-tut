# Number guesser
import random

low = int(input("Enter the starting number : "))
high = int(input("Enter the ending number : "))
rand_num = random.randint(low, high)
n = 0
l = 0

# Track the length of the previous message to clear it properly
last_msg_len = 0 

while True:
    guess = int(input(f"Enter the number ranger from : {low} to {high}: "))
    
    if guess < rand_num:
        msg = "Hint: your Guess is Low!" if n == 0 else f"Hint: your Guess is Low! (x{n+1})"
        n += 1
        l = 0 # Reset high counter if they guess low
    elif guess > rand_num:
        msg = "Hint: your Guess is High!" if l == 0 else f"Hint: your Guess is High! (x{l+1})"
        l += 1
        n = 0 # Reset low counter if they guess high
    else:
        # Clear the hint line before showing the win message
        padding = " " * last_msg_len
        print(f"\r{padding}\rCorrect!\nThe number was {rand_num}!\nYou literally Won!")
        break

    # Calculate padding based on the *previous* message length
    clr_len = max(0, last_msg_len - len(msg))
    padd = " " * clr_len
    
    # Print \r FIRST, then the message, then the padding to clear old text
    print(f"\r{msg}{padd}", end="")
    
    # Save the current length for the next loop iteration
    last_msg_len = len(msg)

del n, l, last_msg_len
error=1