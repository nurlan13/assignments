# reads name.txt into a vriable my-name
with open('testwrite.txt') as f:
    full_text = f.read()

print(full_text)