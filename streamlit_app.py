import streamlit as st

def keypad_to_letters(digit):
    keypad = {
        '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL',
        '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ',
        '1': '1', '0': '0'  # Treat 1 and 0 as themselves
    }
    return keypad.get(digit, digit)  # Return the digit itself if not in keypad

def generate_combinations(number):
    if number == "":
        return [""]
    first_digit = number[0]
    rest_of_number = number[1:]
    rest_combinations = generate_combinations(rest_of_number)
    result = []
    
    for letter in keypad_to_letters(first_digit):
        for combo in rest_combinations:
            result.append(letter + combo)
    return result

def main():
    st.title("Telephone Keypad to Alphabet Converter")
    
    # Input for number
    number = st.text_input("Enter a number (up to 6 digits):", "")
    
    if st.button("Convert"):
        if not number.isdigit() or len(number) > 6:
            st.error("Please enter a valid number up to 6 digits.")
        else:
            combinations = generate_combinations(number)
            if combinations:
                st.write(f"Possible combinations for {number}:")
                for combo in combinations:
                    st.write(combo)
            else:
                st.write("No combinations found.")

if __name__ == "__main__":
    main()