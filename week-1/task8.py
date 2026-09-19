introduction = "Hello, my name is Rohith. I am a student of ECE and I am learning Python programming."

with open("introduction.txt", "w") as file:
    file.write(introduction)

with open("introduction.txt", "r") as file:
    content = file.read()

print("File contents:")
print(content)