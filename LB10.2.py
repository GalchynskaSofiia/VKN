import os
print(os.listdir('lab10'))
for file in os.listdir("lab10"):
    if file.endswith(".txt"):
        os.remove(os.path.join("lab10", file))
