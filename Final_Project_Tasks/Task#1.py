library = [
    {"title": "ვეფხისტყაოსანი", "author": "შოთა რუსთაველი", "year": "12-ე საუკუნე"},
    {"title": "დიდოსტატის მარჯვენა", "author": "კონსტანტინე გამსახურდია", "year": "1939"},
    {"title": "ჯინსების თაობა", "author": "დათო ტურაშვილი", "year": "2001"},
    {"title": "ნატვრის ხე", "author": "გიორგი ლეონიძე", "year": "1962"},
    {"title": "სამოსელი პირველი", "author": "გურამ დოჩანაშვილი", "year": "1975"},
    {"title": "1984", "author": "ჯორჯ ორუელი", "year": "1949"},
    {"title": "უცხო", "author": "ალბერ კამიუ", "year": "1942"},
    {"title": "დათა თუთაშხია", "author": "ჭაბუა ამირეჯიბი", "year": "1975"},
    {"title": "ჰარი პოტერი", "author": "ჯ.კ. როულინგი", "year": "1997"},
    {"title": "დონ კიხოტი", "author": "მიგელ დე სერვანტესი", "year": "1605"}
]

while True:
    print("\n<<მინი-ბიბლიოთეკა>>")
    print("1. ყველა წიგნის ნახვა")
    print("2. ახალი წიგნის დამატება")
    print("3. წიგნის წასაკითხად გატანა")
    print("4. წიგნის ძებნა სათაურით")
    print("5. პროგრამიდან გასვლა")

    customer_choice = input("აირჩიეთ სასურველი მოქმედება (1-5): ")

    if customer_choice == "1":
        print(f"\nბიბლიოთეკაში ამჟამად არის {len(library)} წიგნი:")
        for index, book in enumerate(library, 1):
            print(f"{index}. \"{book['title']}\" - ავტორი: {book['author']} ({book['year']})")

    elif customer_choice == "2":
        title = input("შეიყვანეთ წიგნის სათაური: ")
        author = input("შეიყვანეთ ავტორი: ")
        year = input("შეიყვანეთ გამოცემის წელი: ")

        new_book = {"title": title, "author": author, "year": year}

        library.append(new_book)
        print(f"წიგნი \"{title}\" წარმატებით დაემატა!")

    elif customer_choice == "3":
        title_to_remove = input("რომელი წიგნის გატანა გსურთ? (შეიყვანეთ სათაური): ")
        found = False

        for book in library:
            if book["title"] == title_to_remove:
                library.remove(book)
                print(f"წიგნი \"{title_to_remove}\" გატანილია წასაკითხად!")
                found = True
                break

        if not found:
            print("სამწუხაროდ, ასეთი წიგნი ბიბლიოთეკაში არ მოიძებნა.")

    elif customer_choice == "4":
        search_title = input("შეიყვანეთ საძიებო წიგნის სათაური: ")
        found = False

        for book in library:
            if book["title"] == search_title:
                print(f"ნაპოვნია: \"{book['title']}\" - ავტორი: {book['author']} (გამოშვების წელი: {book['year']})")
                found = True
                break

        if not found:
            print("სამწუხაროდ, წიგნი ვერ მოიძებნა.")

    elif customer_choice == "5":
        print("გმადლობთ, რომ ხართ ჩვენი მკითხველი.")
        break

    else:
        print("არასწორი არჩევანი, გთხოვთ აირჩიოთ 1-დან 5-მდე ციფრი.")