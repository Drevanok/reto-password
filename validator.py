#Saul Eliseo Aparicio Vivar 21760641
# The password must be between 5 and 8 characters long.
# The password must be included in the file 10-million-password-list-top-1000000.

def clean_list(lines):
    return [line.strip().replace(" ", "") for line in lines]

def join_list(lines, separator=""):
    cleaned = clean_list(lines)
    return separator.join(cleaned)

def search_password(concatenated, target_password, window_start=0, window_end=6, initial_capacity=5):
    capacity = initial_capacity
    buffer = []

    while window_end < len(concatenated):
        for i in range(window_start, window_end + 1):
            if capacity == 14:
                capacity = 5
                window_start += 1
                buffer = []
                break

            buffer.append(concatenated[i])
            attempt = "".join(buffer)
            capacity += 1

            if capacity in [10, 11, 12, 13]:
                if target_password == attempt or target_password == attempt[::-1]:
                    return "Password found:", attempt

        window_end += 1

    return "Password not found."

def create_password(start, end, capacity):
    try:
        with open('10-million-password-list-top-1000000.txt', 'r') as file:
            lines = file.readlines()
            full_text = join_list(lines)
            return search_password(full_text, user_password, start, end, capacity)
    except FileNotFoundError:
        return "File not found."

# Input from user
user_password = input("Password: ")

# Execute
print(create_password(0, 6, 5))
