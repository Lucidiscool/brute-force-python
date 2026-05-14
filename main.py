import itertools


def mock_login(password):
    target_password = "placeholder"
    return password == target_password


def brute_force_attack(characters, max_length):
    print("Starting brute-force attack...")
    attemps = 0

    for length in range(1, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            attemps += 1
            guess = ''.join(combination)
            if mock_login(guess):
                print(f"Password found: {guess}")
                print(f"Attempts made: {attemps}")
                return
            

            if attemps % 1000 == 0:
                print (f"Attempts so far: {attemps}")
    print("Password not found within the given parameters.")


def main():
    characters = 'abcdefghijklmnopqrstuvwxyz1234567890'
    max_length = 20
    brute_force_attack(characters, max_length)


if __name__ == "__main__":
    main()
