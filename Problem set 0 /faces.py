def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text


def main():
    user_answer = input("Please Enter Something. ")
    converted_text = convert(user_answer)
    print(converted_text)

main()
