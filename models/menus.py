# coding: utf-8

from typing import Callable, Optional, Tuple

from tools import sprites


class Option(sprites.Text):
    """Manage menu options."""

    def __init__(self, pos: (int, int) = (0, 0), font_filename: Optional[str] = None, font_size: int = 84,
                 antialias: bool = True, message: str = "OPTION", message_color_onblur: (int, int, int) = (0, 0, 0),
                 message_color_onfocus: (int, int, int) = (255, 0, 0),
                 background_color_onblur: Optional[Tuple[int, int, int]] = None,
                 background_color_onfocus: Optional[Tuple[int, int, int]] = None,
                 previous_option: Optional['Option'] = None, next_option: Optional['Option'] = None,
                 action: Optional[Callable[[], None]] = None):
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
        # MANAGE ACTION
        self.action = action

    def onblur(self):
        """Manage option during 'onblur' events."""
        self._message_color = self._message_color_onblur
        self._background_color = self._background_color_onblur
        self.reset_image()

    def onfocus(self):
        """Manage option during 'onfocus' events."""
        self._message_color = self._message_color_onfocus
        self._background_color = self._background_color_onfocus
        self.reset_image()

    def apply(self):
        """Apply the option action."""
        try:
            self.action()
        except TypeError:  # WHEN THE ACTION IS NOT CALLABLE
            print(self.message)
