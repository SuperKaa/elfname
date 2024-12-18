ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
ELF_ADJECTIVES = ["Jolly", "Sparkly", "Tiny", "Joyful", "Lively", "Gleeful", "Merry", "Cheery", "Frosty", "Fluffy", "Giggly", "Shiny", "Twinkly", "Spicy", "Cute", "Naughty", "Flying", "Fizzy", "Cheeky", "Jazzy", "Glowy", "Mirthful", "Glimmering", "Shining", "Bouncing", "Snuggly"]
ELF_NOUNS = ["Snowball", "Candycane", "Cocoa", "Tinsel", "Frost", "Wreath", "Gingerbread", "Bauble", "Sleigh", "Cookie", "Holly", "Mistletoe"]




while True:
    userinput = input("enter the first character in you first name ").upper()
    if userinput in ALPHABET:
        break
    else:
        print("please chose from A-Z! ")

position = ALPHABET.index(userinput)

elf_adjective = ELF_ADJECTIVES[position]

userinput1 = int(input("enter 1-12 "))

elf_nouns = ELF_NOUNS[userinput1]

print(f"your elf name is {elf_adjective} {elf_nouns}")
