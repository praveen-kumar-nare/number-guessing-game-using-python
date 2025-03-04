def main():
    num = 2546
    y = num
    a = num % 10
    num = num // 10
    b = num % 10
    num = num // 10
    c = num % 10
    num = num // 10
    d = num % 10

    while True:
        print("Enter your first guess")
        for i in range(10):
            x = int(input())
            count = 0
            digits = [x % 10, (x // 10) % 10, (x // 100) % 10, (x // 1000) % 10]

            count += 10 if digits[0] == a else 2 if digits[0] in [b, c, d] else 0
            count += 10 if digits[1] == b else 2 if digits[1] in [a, c, d] else 0
            count += 10 if digits[2] == c else 2 if digits[2] in [a, b, d] else 0
            count += 10 if digits[3] == d else 2 if digits[3] in [a, b, c] else 0

            if count == 40:
                print("Hey!! you have guessed it right")
                print("Do you wanna try again? (1 for Yes, 0 for No)")
                q = int(input())
                if q == 0:
                    print("It seems that you are not interested in the game. Okay then, goodbye...")
                    return
                else:
                    break
            else:
                if i == 9:
                    print("If you want to try again, press 1 (0 for No)")
                    q = int(input())
                    if q == 0:
                        print("It seems that you are not interested in the game. Okay then, goodbye...")
                        return
                    else:
                        break
                print(f"Try again and your score is {count}")

if __name__ == "__main__":
    main()
