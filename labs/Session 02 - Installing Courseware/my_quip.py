# my_quip_instructor.py

def display_message():
    # ANSI escape codes for colors
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RESET = '\033[0m'

    name = "Cleo Lepart"
    quote = "Any sufficiently advanced technology is indistinguishable from magic."
    author = "Arthur C. Clarke"

    # Fun text formatting
    fun_name = f"{CYAN}{name}{RESET}"
    fun_quote = f"{YELLOW}{quote}{RESET}"
    fun_author = f"{GREEN}- {author}{RESET}"

    print(fun_name)
    print("\n" + fun_quote)
    print(fun_author)

if __name__ == "__main__":
    display_message()
