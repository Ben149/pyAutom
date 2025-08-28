# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}
#
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
#
# print(count)

# More readable format
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

# Count the characters
for character in message:
    count.setdefault(character, 0)
    count[character] += 1

# Print results sorted by character
for char in sorted(count):
    print(f"'{char}': {count[char]}")