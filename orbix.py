import webbrowser

ORBIX_URL = "https://orbix360.com/PJBx1umPs"


def open_orbix_url_on_keyword():
    # Prompt the user for input
    user_input = input("Enter your destination: ").strip().lower()

    # Check if the input matches 'principal office'
    if user_input == "principal office":
        print("Opening Orbix360 URL...")
        webbrowser.open(ORBIX_URL)
    else:
        print("Input does not match 'principal office'. URL will not be opened.")


if __name__ == "__main__":
    open_orbix_url_on_keyword()
