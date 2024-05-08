import streamlit as st
from password_generator import generate_random_password, generate_memorable_password, generate_pin
from nltk.corpus import words

# Title of the application
st.image('./Images/banner.jpeg')
st.title(":zap: Password Generator")

option = st.radio("Password Type", ('Random Password', 'Memorable Password', 'Pin Code'))

if option == 'Random Password':
    length = st.slider("Length", min_value=5, max_value=50, value=8)
    include_numbers = st.toggle("Include Numbers")
    include_symbols = st.toggle("Include Symbols")

    password = generate_random_password(length, include_numbers, include_symbols)
elif option == 'Memorable Password':
    no_of_words = st.slider("Number of Words", min_value=2, max_value=10, value=5)
    separator = st.text_input("Separator", value='-')
    capitalization = st.toggle("Capitalization")

    password = generate_memorable_password(no_of_words, separator, capitalization, words.words())
else:
    length = st.slider("Length", min_value=2, max_value=10, value=4)

    password = generate_pin(length)

st.write("Your password is: ")
st.header(fr"``` {password} ```")