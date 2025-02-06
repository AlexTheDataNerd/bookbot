def main():
    with open("/Users/alexiakomp/Workspace/first_project/github.com/AlexTheDataNerd/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
      # Print the contents of the file
    return file_contents

main()
def count():
    file_contents = main()
    word_count = len(file_contents.split())
    return word_count
print(f"Word count: {count()}")

#lowercase function 
def count_lower():
 file_contents = main()
 lowered_file_contents = file_contents.lower()
 char_count = {}
 for char in lowered_file_contents :
    if char in char_count :
        char_count[char] += 1
    else :
        char_count[char] = 1
 print(char_count)
   


#alphacase function 
def count_alpha():
 file_contents = main()
 lowered_file_contents = file_contents.lower()
 char_count = {}
 for char in lowered_file_contents :
    if char.isalpha() :
        if char in char_count :
            char_count[char] += 1
        else :
            char_count[char] = 1
 return char_count

#annauncment 
def annauncment():
    file = count_alpha()
    for letter in file :
        print(f"The '{letter}' was found {file[letter]} times")

annauncment()