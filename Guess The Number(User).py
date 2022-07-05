import random

print("I will try to guess the number you think so please give me an upper limit")
limit = int(input("Upper Limit: "))

def guess(limit):
    guess = random.randint(1, limit)
    lower_limit = 1
    answer = ""
    while answer != "yes":
        answer = input(f"Is the number you chose {guess}? If not should I guess higher or lower? Please answer with 'yes', 'higher' or 'lower' ").lower()
        if answer == "higher":
            lower_limit = guess + 1
            if lower_limit != limit:
                guess = random.randint(lower_limit, limit)
            else:
                guess = lower_limit
        elif answer == "lower":
            limit = guess - 1
            if lower_limit != limit:
                guess = random.randint(lower_limit, limit)
            else:
                guess = lower_limit          
    print(f"I knew I could guess the number you chose. I didn't think you would choose {guess} though.")
guess(limit)
