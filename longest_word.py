# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


txt = input("Enter a sentence:")
if " " in txt:
    text = txt.split(" ")
    longest = max(text, key= len)
    print(f"The longest word is {longest}")

