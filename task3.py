import markovify

# --- Step 1: Read the text data from your file ---
# This part is the same as before.
try:
    with open('my_text.txt', 'r', encoding='utf-8') as f:
        text = f.read()
except FileNotFoundError:
    print("Error: 'my_text.txt' not found. Please make sure the file is in the same folder as the script.")
    exit()

# --- Step 2: Build the Markovify Model ---
# This one line does all the hard work of building the model!
text_model = markovify.Text(text)


# --- Step 3: Generate New Sentences ---
print("Generating 5 new sentences in the style of Romeo and Juliet:")
print("----------------------------------------------------------")

# Print 5 randomly generated sentences
for i in range(5):
    # The make_sentence() function creates a new sentence from the model.
    new_sentence = text_model.make_sentence()
    if new_sentence:
        print(f"{i+1}. {new_sentence}")
