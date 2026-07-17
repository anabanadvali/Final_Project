import logging

logging.basicConfig(
    filename='atm_logs',
    level=logging.INFO
)
balance = 500.0

while True:
    print("\nმენიუ")
    print("1. ბალანსის შემოწმება")
    print("2. თანხის შემოტანა")
    print("3. თანხის გატანა")
    print("4. ბანკომატიდან გამოსვლა")

    choice = input("აირჩიეთ სასურველი მოქმედება (1-4): ")

    if choice == "1":
        print(f"თქვენი მიმდინარე ბალანსია: {balance} ლარი")
    elif choice == "2":
        amount = float(input("შეიყვანეთ შესატანი თანხა (ლარში): "))

        if amount > 1000:
            print("შეცდომა: ერთჯერადად 1000 ლარზე მეტს ვერ შემოიტანთ!")
        else:
            balance += amount
            print(f"თანხა წარმატებით აისახა ბალანსზე. ახალი ბალანსი: {balance} ლარი")
        logging.info(f"თანხის შემოტანა: {amount} ლარი. ახალი ბალანსი: {balance} ლარი")

    elif choice == "3":
        amount = float(input("შეიყვანეთ გასატანი თანხა (ლარში): "))

        if amount > balance:
            print(f"შეცდომა: ანგარიშზე არ გაქვთ საკმარისი თანხა! ბალანსი: {balance} ლარი")
        else:
            balance -= amount
            print(f"თანხა გატანილია! დარჩენილი ბალანსი: {balance} ლარი")
            logging.info(f"თანხის გატანა: {amount} ლარი. დარჩენილი ბალანსი: {balance} ლარი")

    elif choice == "4":
        print("გმადლობთ, რომ სარგებლობთ ჩვენი მომსახურებით!")
        break