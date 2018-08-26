# coding: utf-8

from typing import Optional, Tuple, Union

import pygame

from tools import decorators
from tools.softwares import Screen


class Sprite(object):
    """Manage sprites. Abstract class."""

    def __init__(self, pos: (int, int) = (0, 0)) -> None:
        """Create the sprite for the first time."""
        self._image = None
        self.reset_image()
        self._pos = pos
        self._area = None
        self.reset_area()

    def __getstate__(self) -> dict:
        """Use to pickle the sprite."""
        dict_ = self.__dict__.copy()
        dict_.pop('_image')
        dict_.pop('_area')
        return dict_

    def __setstate__(self, dict_: dict) -> None:
        """Use to unpickle the sprite."""
        self.__dict__ = dict_
        self.reset_image()
        self.reset_area()

    def reset_image(self) -> Exception:
        """Reset the sprite image from unpickler. Need to be overridden."""
        raise NotImplementedError()

    def reset_area(self) -> None:
        """Reset the sprite area from unpickler."""
        self._area = self._image.get_rect(topleft=self._pos)

    def blit_on(self, surface: Union[Screen, pygame.Surface]) -> None:
        """Display the sprite on a surface."""
        surface.blit(self._image, self._area)

    @property
    def image(self) -> pygame.Surface:
        """Return the current sprite image."""
        return self._image

    @property
    def area(self) -> pygame.Rect:
        """Return the current sprite area."""
        return self._area

    @property
    def x(self) -> int:
        """Return the current sprite topleft x position."""
        return self._pos[0]

    @x.setter
    def x(self, value: int) -> None:
        """Modify the sprite topleft x position."""
        y = self._pos[1]
        self._pos = (value, y)
        self._area.x = value

    @property
    def y(self) -> int:
        """Return the current sprite topleft y position."""
        return self._pos[1]

    @y.setter
    def y(self, value: int) -> None:
        """Modify the sprite topleft y position."""
        x = self._pos[0]
        self._pos = (x, value)
        self._area.y = value

    @property
    def pos(self) -> (int, int):
        """Return the current sprite topleft position."""
        return self._pos

    @pos.setter
    def pos(self, value: (int, int)) -> None:
        """Modify the sprite topleft position."""
        self._pos = value
        self._area.topleft = value

    @property
    def width(self) -> int:
        """Return the current sprite width."""
        return self._area.width

    @property
    def height(self) -> int:
        """Return the current sprite height."""
        return self._area.height

    @property
    def size(self) -> (int, int):
        """Return the current sprite size."""
        return self._area.size


class Surface(Sprite):
    """Manage surfaces."""

    def __init__(self, pos: (int, int) = (0, 0), size: (int, int) = (50, 50),
                 color: (int, int, int) = (0, 0, 0)) -> None:
        """Create the surface for the first time."""
        self._size = size
        self._color = color
        super(Surface, self).__init__(pos=pos)

    def reset_image(self) -> None:
        """Reset the surface image from unpickler. Overriding method."""
        self._image = pygame.Surface(self._size)
        self._image.fill(self._color)

    @property
    def width(self) -> int:
        """Return the current surface width."""
        return super(Surface, self).width

    @width.setter
    def width(self, value: int) -> None:
        """Modify the surface width."""
        height = self._size[0]
        self._size = (value, height)
        self.reset_image()
        self._area.width = value

    @property
    def height(self) -> int:
        """Return the current surface height."""
        return super(Surface, self).height

    @height.setter
    def height(self, value: int) -> None:
        """Modify the surface height."""
        width = self._size[0]
        self._size = (width, value)
        self.reset_image()
        self._area.height = value

    @property
    def size(self) -> (int, int):
        """Return the current surface size."""
        return super(Surface, self).size

    @size.setter
    def size(self, value: (int, int)) -> None:
        """Modify the surface size."""
        self._size = value
        self.reset_image()
        self._area.size = value

    @property
    def color(self) -> (int, int, int):
        """Return the current surface color."""
        return self._color

    @color.setter
    def color(self, value: (int, int, int)) -> None:
        """Modify the surface color."""
        self._color = value
        self._image.fill(value)


@decorators.singleton(parameters=True)
class Font(pygame.font.Font):
    """Overriding the pygame Font class to apply the singleton decorator."""
    pass


class Text(Sprite):
    """Manage texts."""

    def __init__(self, pos: (int, int) = (0, 0), antialias: bool = True,
                 font_filename: Optional[str] = None, font_size: int = 84,
                 message: str = "PYGAME", message_color: (int, int, int) = (0, 0, 0),
                 background_color: Optional[Tuple[int, int, int]] = None) -> None:
        """Create the text for the first time."""
        self._font_filename = font_filename
        self._font_size = font_size
        self._font = None
        self.reset_font()
        self._antialias = antialias
        self._message = message
        self._message_color = message_color
        self._background_color = background_color
        super(Text, self).__init__(pos=pos)

    def __getstate__(self) -> dict:
        """Use to pickle the sprite."""
        dict_ = super(Text, self).__getstate__()
        dict_.pop('_font')
        return dict_

    def __setstate__(self, dict_: dict) -> None:
        """Use to unpickle the sprite."""
        self.__dict__ = dict_
        self.reset_font()
        super(Text, self).__setstate__(self.__dict__)

    def reset_font(self) -> None:
        """Reset the text font."""
        self._font = Font(self._font_filename, self._font_size)

    def reset_image(self) -> None:
        """Reset the text image from unpickler."""
        self._image = self._font.render(self._message, self._antialias, self._message_color, self._background_color)

    @property
    def font_filename(self) -> str:
        """Return the current text font."""
        return self._font_filename

    @font_filename.setter
    def font_filename(self, value: Optional[str]) -> None:
        """Modify the text font."""
        self._font_filename = value
        self.reset_font()
        self.reset_image()
        self.reset_area()

    @property
    def font_size(self) -> int:
        """Return the current text font size"""
        return self._font_size

    @font_size.setter
    def font_size(self, value: int) -> None:
        """Modify the text font size."""
        self._font_size = value
        self.reset_font()
        self.reset_image()
        self.reset_area()

    @property
    def message(self) -> str:
        """Return the current text message."""
        return self._message

    @message.setter
    def message(self, value: str) -> None:
        """Modify the text message."""
        self._message = value
        self.reset_image()
        self.reset_area()

    @property
    def antialias(self) -> bool:
        """Return the current text antialias."""
        return self._antialias

    @antialias.setter
    def antialias(self, value: bool) -> None:
        """Modify the text antialias."""
        self._antialias = value
        self.reset_image()

    @property
    def message_color(self) -> (int, int, int):
        """Return the current text color."""
        return self._message_color

    @message_color.setter
    def message_color(self, value: (int, int, int)) -> None:
        """Modify the text color."""
        self._message_color = value
        self.reset_image()

    @property
    def background_color(self) -> Optional[Tuple[int, int, int]]:
        """Return the current text background color."""
        return self._background_color

    @background_color.setter
    def background_color(self, value: Optional[Tuple[int, int, int]]) -> None:
        """Modify the text background color."""
        self._background_color = value
        self.reset_image()
