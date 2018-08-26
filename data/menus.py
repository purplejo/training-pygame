# coding: utf-8

from models.menus import Menu, Option

from tools import softwares

screen = softwares.Screen()


class ExitMenu(Menu):
    """Manage the exit menu."""

    def __init__(self) -> None:
        """Create the exit menu for the first time."""
        # MANAGE OPTIONS
        self.YES = Option(message="YES")
        self.NO = Option(message="NO", previous_option=self.YES)
        # CALL SUPER
        super(ExitMenu, self).__init__(options=[self.YES, self.NO])

    def apply(self):
        """Apply an action depending on focused option. Overriding method."""
        if self.option is self.YES:
            screen.running = False
        elif self.option is self.NO:
            self.running = False


class MainMenu(Menu):
    """Manage the main menu."""

    def __init__(self) -> None:
        """Create the main menu for the first time."""
        # MANAGE OPTIONS
        self.PLAY = Option(message="PLAY")
        self.EDITOR = Option(message="EDITOR", previous_option=self.PLAY)
        self.OPTIONS = Option(message="OPTIONS", previous_option=self.EDITOR)
        self.EXIT = Option(message="EXIT", previous_option=self.OPTIONS, next_option=self.PLAY)
        # CALL SUPER
        super(MainMenu, self).__init__(options=[self.PLAY, self.EDITOR, self.OPTIONS, self.EXIT])

    def apply(self) -> None:
        """Apply an action depending on focused option. Overriding Method."""
        if self.option is self.PLAY:
            print(self.option.message)
        elif self.option is self.EDITOR:
            print(self.option.message)
        elif self.option is self.OPTIONS:
            print(self.option.message)
        elif self.option is self.EXIT:
            exit_menu = ExitMenu()
            exit_menu.loop()
