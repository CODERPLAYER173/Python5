
import pandas
student_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
words = {row.letter:row.code for (index , row) in student_data_frame.iterrows()}
user_word = input("Pls enter the word").upper()
split  = list(user_word)
final = [words[letter] for letter in split]
print(final)

