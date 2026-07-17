registered_email = "user@gmail.com"
registered_username = "george777"
registered_password = "password123"

print("რეგისტრაცია")

while True:
    name = input("შეიყვანეთ თქვენი სახელი (მხოლოდ პატარა ლათინური ასოები): ")

    if name == "":
        print("შეცდომა: ველი არ უნდა იყოს ცარიელი!")
        continue

    has_uppercase = False
    has_digits = False
    has_symbols = False
    has_non_latin = False
    has_space = False


    for char in name:
        char_code = ord(char)
        is_latin_lowercase = (97 <= char_code <= 122)
        is_latin_uppercase = (65 <= char_code <= 90)

        if char == " ":
            has_space = True
        elif char.isdigit():
            has_digits = True
        elif is_latin_uppercase:
            has_uppercase = True
        elif not char.isalnum():
            has_symbols = True
        elif not is_latin_lowercase and not is_latin_uppercase:
            has_non_latin = True


    error_types = [has_uppercase, has_digits, has_symbols, has_non_latin, has_space]
    if sum(error_types) >= 2:
        print("შეცდომა: შემოყვანილია შერეული მონაცემები. შემოიყვანეთ მხოლოდ string პატარა რეგისტრში")
        continue


    if has_space:
        print("შეცდომა: შემოყვანილია სფეისი, შემოიყვანეთ მხოლოდ string პატარა რეგისტრში")
        continue
    if has_non_latin:
        print("შეცდომა: შემოყვანილია სხვა ენა, შემოიყვანეთ მხოლოდ string პატარა რეგისტრში")
        continue
    if has_symbols:
        print("შეცდომა: შემოყვანილია სიმბოლოები, შემოიყვანეთ მხოლოდ string პატარა რეგისტრში")
        continue
    if has_digits:
        print("შეცდომა: შემოყვანილია ციფრები, შემოიყვანეთ მხოლოდ string პატარა რეგისტრში")
        continue
    if has_uppercase:
        print("შეცდომა: შემოყვანილია დიდი ასოები, შემოიყვანეთ მხოლოდ string პატარა რეგისტრში")
        continue
    break

print("\nრეგისტრაცია წარმატებით დასრულდა!")
print(f"სახელი: {name}")
print(f"ელ-ფოსტა: {registered_email}")
print(f"ზედმეტსახელი: {registered_username}")
print(f"პაროლი: {registered_password}")