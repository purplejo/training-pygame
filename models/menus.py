# coding: utf-8

from typing import List, Optional, Tuple

import pygame

from tools import softwares, sprites

pygame.init()

clock = softwares.Clock()
screen = softwares.Screen()
keyboard = softwares.Keyboard()
mouse = softwares.Mouse()


class Option(sprites.Text):
    """Manage menu options."""

    def __init__(self, pos: (int, int) = (0, 0), font_filename: Optional[str] = None, font_size: int = 84,
                 antialias: bool = True, message: str = "OPTION", message_color_onblur: (int, int, int) = (0, 0, 0),
                 message_color_onfocus: (int, int, int) = (255, 0, 0),
                 background_color_onblur: Optional[Tuple[int, int, int]] = None,
                 background_color_onfocus: Optional[Tuple[int, int, int]] = None,
                 previous_option: Optional['Option'] = None, next_option: Optional['Option'] = None) -> None:
        """Create the option for the first time."""
        # CALL SUPER
        super(Option, self).__init__(pos=pos, font_filename=font_filename, font_size=font_size, antialias=antialias,
                                     message=message, message_color=message_color_onblur,
                                     background_color=background_color_onblur)
        # MANAGE MESSAGE COLORS
        self._message_color_onblur = message_color_onblur
        self._message_color_onfocus = message_color_onfocus
        # MANAGE BACKGROUND COLORS
        self._background_color_onblur = background_color_onblur
        self._background_color_onfocus = background_color_onfocus
        # MANAGE PREVIOUS OPTION
        if previous_option is not None:
            previous_option.next_option = self
        self.previous_option = previous_option
        # MANAGE NEXT OPTION
        if next_option is not None:
            next_option.previous_option = self
        self.next_option = next_option

    def onblur(self) -> None:
        """Manage option during 'onblur' events."""
        self._message_color = self._message_color_onblur
        self._background_color = self._background_color_onblur
        self.reset_image()

    def onfocus(self) -> None:
        """Manage option during 'onfocus' events."""
        self._message_color = self._message_color_onfocus
        self._background_color = self._background_color_onfocus
        self.reset_image()


class Menu(sprites.Surface):
    """Manage menus."""

    def __init__(self, options: Optional[List['Option']] = None, pos: (int, int) = (0, 0),
                 size: (int, int) = screen.size, background_color: (int, int, int) = (255, 255, 255)) -> None:
        """Create the menu for the first time."""
        # CALL SUPER
        super(Menu, self).__init__(pos=pos, size=size, color=background_color)
        # MANAGE OPTIONS
        self.options = options if options is not None else []
        self.reset_options()
        # MANAGE FOCUSED OPTION
        self.option = None
        if len(self.options) > 0:
            self.option = self.options[0]
            self.option.onfocus()
        # LOOP
        self.running = True

    def reset_options(self) -> None:
        """Manage some arguments of the menu options."""
        for (i, option) in enumerate(self.options):
            option.menu = self
            option.pos = ((self.width - option.width) / 2, sum([self.options[j].height for j in range(i)]) +
                          (self.height - sum([option.height for option in self.options])) / 2)

    def focus(self, option: Option) -> None:
        """Focus a new option in the menu."""
        if option is not None and option is not self.option:
            self.option.onblur()
            self.option = option
            self.option.onfocus()

    def apply(self) -> None:
        """Apply an action depending on the focused option. Need to be overridden."""
        print(self.option.message)

    def blit_on(self, surface: pygame.Surface) -> None:
        """Blit the menu onto the surface. Overriding method."""
        super(Menu, self).blit_on(surface)
        for option in self.options:
            option.blit_on(surface)

    def loop(self) -> None:
        """Manage events in the menu."""
        while screen.running and self.running:
            events = pygame.event.get()
            screen.update(events)
            keyboard.update(events)
            mouse.update(events)
            if self.option is not None:
                if keyboard.push('up', 0.233):
                    if self.option.previous_option is not None:
                        self.focus(self.option.previous_option)
                if keyboard.push('down', 0.233):
                    if self.option.next_option is not None:
                        self.focus(self.option.next_option)
                if mouse.move() and not mouse.inside(self.option.area):
                    for option in self.options:
                        if mouse.inside(option.area):
                            self.focus(option)
                            break
            self.blit_on(screen.image)
            pygame.display.update()
            clock.tick(20)
            if self.option is not None:
                if (any([keyboard.push(key, 99) for key in ['enter', 'return', 'keypad enter']])
                        or (mouse.push(1, 99) and mouse.inside(self.option.area))):
                    self.apply()
