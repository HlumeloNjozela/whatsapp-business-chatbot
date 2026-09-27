def show_menu():
    print("\n========================================")
    print("       NJOZELA ATTORNEYS INC.")
    print("========================================")
    print("How can we assist you?")
    print("1. Our services")
    print("2. Office hours")
    print("3. Book a consultation")
    print("4. Contact us")
    print("5. Speak to a person")
    print("6. Exit")


def chatbot():
    print("\n👋 Welcome to Njozela Attorneys Inc.")
    print("We're here to assist you with your enquiry.")

    name = input("\nWhat is your name? ")

    print(f"\nNice to meet you, {name}!")

    while True:
        show_menu()

        choice = input("\nPlease select an option: ")

        if choice == "1":
            print("\nOur services may include:")
            print("- Legal consultations")
            print("- Contract and commercial matters")
            print("- Litigation")
            print("- Family law matters")
            print("- Other legal services")

        elif choice == "2":
            print("\nOur office hours are:")
            print("Monday - Friday: 08:00 - 17:00")

        elif choice == "3":
            print("\nTo request a consultation, please provide:")
            print("- Your name")
            print("- Your preferred date")
            print("- A brief description of your enquiry")

            print("\nA member of our team can then contact you")
            print("to confirm the consultation.")

        elif choice == "4":
            print("\nNjozela Attorneys Inc.")
            print("Phone: [Business telephone number]")
            print("Email: [Business email address]")
            print("Website: [Business website]")

        elif choice == "5":
            print("\nI'll help you connect with a member of our team.")
            print("Please provide your contact details and enquiry.")

        elif choice == "6":
            print(f"\nThank you for contacting Njozela Attorneys Inc., {name}.")
            print("Goodbye! 👋")
            break

        else:
            print("\nSorry, I didn't understand that option.")
            print("Please choose a number from 1 to 6.")


chatbot()
