points = 0

print("Q1. What is 2 + 5/2 + 5/2?")
print("""A) 6
B) 7
C) 10
D) 5
""")
ans = input("Choose the correct option: ").lower()
if ans == "b":
    points += 1

print("\nQ2. What is 8 + 12 / 4?")
print("""A) 5
B) 11
C) 20
D) 8
""")
ans = input("Choose the correct option: ").lower()
if ans == "b":
    points += 1

print("\nQ3. What is the value of 3² + 4²?")
print("""A) 7
B) 25
C) 49
D) 12
""")
ans = input("Choose the correct option: ").lower()
if ans == "b":
    points += 1

print("\nQ4. What is 15 // 4 in Python?")
print("""A) 3
B) 4
C) 3.75
D) Error
""")
ans = input("Choose the correct option: ").lower()
if ans == "a":
    points += 1

print("\nQ5. What will len('Python') return?")
print("""A) 5
B) 6
C) 7
D) Error
""")
ans = input("Choose the correct option: ").lower()
if ans == "b":
    points += 1

print(f"\nResult: {points}/5")
