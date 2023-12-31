# password_generator.py
import streamlit as st
import random
import string


def generate_password():
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_chars = letters + digits + symbols

    # 8자리 암호 생성
    password = ''.join(random.sample(all_chars, 8))
    return password


def main():
    st.title("암호 생성기")

    if st.button("암호 생성"):
        password = generate_password()
        st.success(f"생성된 암호: {password}")


if __name__ == '__main__':
    main()