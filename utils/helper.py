
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    RESET = "\033[0m"


def success(text):
    return f"{Colors.GREEN}{text}{Colors.RESET}"


def error(text):
    return f"{Colors.RED}{text}{Colors.RESET}"


def info(text):
    return f"{Colors.CYAN}{text}{Colors.RESET}"


def warning(text):
    return f"{Colors.YELLOW}{text}{Colors.RESET}"