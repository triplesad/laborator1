from ui.interface import show_main_page
from core.auth import login_user


def run():
    print("Запуск проекта 'Форум'")
    show_main_page()
    login_user("visitor")


if __name__ == "__main__":
    run()
