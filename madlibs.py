# Membaca isi file cerita
with open("story.txt", "r") as f:
    story = f.read()

# Menemukan kata-kata yang perlu diganti
words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    elif char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

# Mengumpulkan kata-kata dari pengguna
answers = {}

for word in words:
    answer = input("Masukkan kata untuk " + word + ": ")
    answers[word] = answer

# Menggantikan placeholder dengan kata dari pengguna
for word, answer in answers.items():
    story = story.replace(word, answer)

# Menampilkan cerita yang sudah diubah
print(story)
