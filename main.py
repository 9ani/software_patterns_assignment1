from dress_factory import DressFactory
from user_interface import UserInterface

if __name__ == "__main__":
    factory = DressFactory()

    ui = UserInterface(factory)
    ui.display_menu()