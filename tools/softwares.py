# coding: utf-8

import time
from typing import List, Optional, Tuple, Union

import pygame
import pygame.locals as pg

from tools import decorators


@decorators.singleton(parameters=False)
class Screen(object):
    """Simulate a screen software."""

    def __init__(self, size: (int, int) = (800, 600), color: (int, int, int) = (255, 255, 255),
                 title: str = "Pygame Window", flags: Optional[List[str]] = None):
        """Create the screen for the first time."""
        info = pygame.display.Info()
        self._fullscreen_size = (info.current_w, info.current_h)
        self._windowedscreen_size = size
        self._color = color
        self._title = title
        if flags is None:
            flags = []
        self._fullscreen = 'FULLSCREEN' in flags
        self._doublebuf = 'DOUBLEBUF' in flags
        self._hwsurface = 'HWSURFACE' in flags
        self._opengl = 'OPENGL' in flags
        self._resizable = 'RESIZABLE' in flags
        self._noframe = 'NOFRAME' in flags
        self.reset_screen()
        self.running = True
        self.size = size

    def reset_screen(self):
        """Reset some attributes of the screen."""
        pygame.display.set_mode(self.size, self.flags)
        self.reset_color()
        self.reset_title()

    def reset_color(self):
        """Reset the background color of the screen."""
        pygame.display.get_surface().fill(self.color)

    def reset_title(self):
        """Reset the title of the screen."""
        pygame.display.set_caption(self.title)

    def update(self, events: List[pygame.event.EventType]):
        """Update some events for the screen."""
        for event in events:
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.ACTIVEEVENT:
                pass
                # event.gain = [0, 1]
                # event.state = [?, 1, 2, ?, 6, ?]
            elif event.type == pg.VIDEOEXPOSE:
                pygame.display.update()
            elif event.type == pg.VIDEORESIZE:
                if event.size != self.size:
                    self.size = event.size

    def blit(self, source: pygame.Surface, destination: Union[Tuple[int, int], pygame.Rect],
             area: bool = None, special_flags: int = 0) -> pygame.Rect:
        """Display an image onto the screen."""
        return self.image.blit(source, destination, area, special_flags)

    @property
    def width(self) -> int:
        """Return the current screen width."""
        if self._fullscreen:
            return self._fullscreen_size[0]
        return self._windowedscreen_size[0]

    @width.setter
    def width(self, value: int):
        """Modify the screen width."""
        height = self._windowedscreen_size[1]
        self._windowedscreen_size = (value, height)
        self.reset_screen()

    @property
    def height(self) -> int:
        """Return the current screen height."""
        if self._fullscreen:
            return self._fullscreen_size[1]
        return self._windowedscreen_size[1]

    @height.setter
    def height(self, value: int):
        """Modify the screen height."""
        width = self._windowedscreen_size[0]
        self._windowedscreen_size = (width, value)
        self.reset_screen()

    @property
    def size(self) -> (int, int):
        """Return the current screen size."""
        if self._fullscreen:
            return self._fullscreen_size
        return self._windowedscreen_size

    @size.setter
    def size(self, value: (int, int)):
        """Modify the screen size."""
        self._windowedscreen_size = value
        self.reset_screen()

    @property
    def fullscreen(self) -> bool:
        """Return the current value of the full screen mode."""
        return self._fullscreen

    @fullscreen.setter
    def fullscreen(self, value: bool):
        """Turn the full screen mode to value."""
        self._fullscreen = value
        self.reset_screen()

    @property
    def fullscreen_width(self) -> int:
        """Return the current fullscreen width."""
        return self._fullscreen_size[0]

    @property
    def fullscreen_height(self) -> int:
        """Return the current fullscreen height."""
        return self._fullscreen_size[1]

    @property
    def fullscreen_size(self) -> (int, int):
        """Return the current fullscreen size."""
        return self._fullscreen_size

    @property
    def doublebuf(self) -> bool:
        """Return the current value of the double buf mode."""
        return self._doublebuf

    @doublebuf.setter
    def doublebuf(self, value: bool):
        """Turn the double buf mode to value."""
        self._doublebuf = value
        self.reset_screen()

    @property
    def hwsurface(self) -> bool:
        """Return the current value of the hwsurface mode."""
        return self._hwsurface

    @hwsurface.setter
    def hwsurface(self, value: bool):
        """Turn the hwsurface mode to value."""
        self._hwsurface = value
        self.reset_screen()

    @property
    def opengl(self) -> bool:
        """Return the current value of the opengl mode."""
        return self._opengl

    @opengl.setter
    def opengl(self, value: bool):
        """Turn the opengl mode to value."""
        self._opengl = value
        self.reset_title()

    @property
    def resizable(self) -> bool:
        """Return the current value of the resizable mode."""
        return self._resizable

    @resizable.setter
    def resizable(self, value: bool):
        """Turn the resizable mode to value."""
        self._resizable = value
        self.reset_screen()

    @property
    def noframe(self) -> bool:
        """Return the current value of the noframe mode."""
        return self._noframe

    @noframe.setter
    def noframe(self, value: bool):
        """Turn the noframe mode to value."""
        self._noframe = value
        self.reset_screen()

    @property
    def flags(self) -> int:
        """Return the current value of the screen flags."""
        flags = 0
        if self._fullscreen:
            flags += pg.FULLSCREEN
        if self._doublebuf:
            flags += pg.DOUBLEBUF
        if self._hwsurface:
            flags += pg.HWSURFACE
        if self._opengl:
            flags += pg.OPENGL
        if self._resizable:
            flags += pg.RESIZABLE
        if self._noframe:
            flags += pg.NOFRAME
        return flags

    @property
    def color(self) -> (int, int, int):
        """Return the current screen background color."""
        return self._color

    @color.setter
    def color(self, value: (int, int, int)):
        """Modify the screen background color."""
        self._color = value
        self.reset_color()

    @property
    def title(self) -> str:
        """Return the current screen title."""
        return self._title

    @title.setter
    def title(self, value: str):
        """Modify the screen title."""
        self._title = value
        self.reset_title()

    @property
    def image(self) -> pygame.Surface:
        """Return the current screen image."""
        return pygame.display.get_surface()

    @property
    def area(self) -> pygame.Rect:
        """Return the current screen area."""
        return pygame.display.get_surface().get_rect()


@decorators.singleton(parameters=False)
class Keyboard(object):
    """Simulate a keyboard software."""

    def __init__(self):
        """Create the keyboard for the first time."""
        self._key_type = {}
        self._key_first = {}
        self._key_time = {}
        self._unicode = {}

    def update(self, events: List[pygame.event.EventType]):
        """Update events for the keyboard."""
        for event in events:
            if event.type == pg.KEYDOWN:
                self._key_type[event.key] = pg.KEYDOWN
                self._key_first[event.key] = True
                if event.unicode != '':
                    self._key_type[event.unicode] = pg.KEYDOWN
                    self._key_first[event.unicode] = True
                    self._unicode[(event.key, event.mod)] = event.unicode
                if pygame.key.name(event.key) != '':
                    self._key_type[pygame.key.name(event.key)] = pg.KEYDOWN
                    self._key_first[pygame.key.name(event.key)] = True
            elif event.type == pg.KEYUP:
                self._key_type[event.key] = pg.KEYUP
                if (event.key, event.mod) in self._unicode:
                    unicode = self._unicode[(event.key, event.mod)]
                    self._key_type[unicode] = pg.KEYUP
                if pygame.key.name(event.key) != '':
                    self._key_type[pygame.key.name(event.key)] = pg.KEYUP

    def push(self, key: Union[int, str], delay: float = 0) -> Optional[bool]:
        """Know if a keyboard key is pushed, depends on delay."""
        if key not in self._key_type or key not in self._key_first:
            return None
        elif self._key_first[key] is True:
            self._key_first[key] = False
            self._key_time[key] = time.time()
            return True
        elif self._key_type[key] is not pg.KEYDOWN:
            return False
        elif time.time() - self._key_time[key] >= delay:
            self._key_time[key] = time.time()
            return True
        return False


@decorators.singleton(parameters=False)
class Mouse(object):
    """Simulate a mouse software."""

    def __init__(self):
        """Create the mouse for the first time."""
        self._pos = (0, 0)
        self._rel = (0, 0)
        self._button_type = {}
        self._button_first = {}
        self._button_time = {}

    def update(self, events: List[pygame.event.EventType]):
        """Update events for the mouse."""
        self._rel = (0, 0)
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                self._button_type[event.button] = pg.MOUSEBUTTONDOWN
                self._button_first[event.button] = True
            elif event.type == pg.MOUSEBUTTONUP:
                self._button_type[event.button] = pg.MOUSEBUTTONUP
            elif event.type == pg.MOUSEMOTION:
                self._pos = event.pos
                self._rel = event.rel

    @property
    def xpos(self) -> int:
        """Return the current x mouse position."""
        return self._pos[0]

    @property
    def ypos(self) -> int:
        """Return the current y mouse position."""
        return self._pos[1]

    @property
    def pos(self) -> (int, int):
        """Return the current mouse position."""
        return self._pos

    @property
    def xrel(self) -> int:
        """Return the current relative x mouse position."""
        return self._rel[0]

    @property
    def yrel(self) -> int:
        """Return the current relative y mouse position."""
        return self._rel[1]

    @property
    def rel(self) -> (int, int):
        """Return the current relative mouse position."""
        return self._rel

    def move(self) -> bool:
        """Know if the mouse is moving."""
        return not self._rel == (0, 0)

    def push(self, button: int, delay: int = 0) -> bool:
        """Know if a mouse button is pushed, depends on delay."""
        if button not in self._button_type:
            return None
        elif self._button_first[button]:
            self._button_first[button] = False
            self._button_time[button] = time.time()
            return True
        elif self._button_type[button] is not pg.MOUSEBUTTONDOWN:
            return False
        elif time.time() - self._button_time[button] >= delay:
            self._button_time[button] = time.time()
            return True
        return False

    @staticmethod
    def set_visible(value: bool = True):
        """Turn the mouse cursor visibility to value."""
        pygame.mouse.set_visible(value)

    @staticmethod
    def set_pos(pos: (int, int)):
        """Permanently block the mouse cursor to a screen position."""
        pygame.mouse.set_pos(pos)

    def inside(self, area: pygame.Rect) -> bool:
        """Know if the mouse cursor is inside an area."""
        pos = self._pos
        top = area.topleft
        bot = area.bottomright
        if top[0] <= pos[0] <= bot[0] and top[1] <= pos[1] <= bot[1]:
            return True
        return False


@decorators.singleton(parameters=True)
class Joystick(object):
    """Simulate a joystick software."""

    def __init__(self, id_: int = 0):
        """Create the joystick for the first time."""
        self._id = id_
        self._button_type = {}
        self._button_first = {}
        self._button_time = {}
        self._axis_value = {}
        self._axis_first = {}
        self._axis_time = {}
        self._hat_value = {}
        self._hat_first = {}
        self._hat_time = {}
        self._ball_value = {}
        self._ball_first = {}
        self._ball_time = {}
        self._name = "Joystick not detected by pygame."
        self.reset_joystick()

    def reset_joystick(self):
        """Reset some attributes of the joystick."""
        # If pygame do not detect the joystick
        if self._id >= pygame.joystick.get_count():
            pygame.joystick.quit()
            pygame.joystick.init()
        # If pygame detect the joystick
        if self._id < pygame.joystick.get_count():
            joystick = pygame.joystick.Joystick(self._id)
            joystick.init()
            self._name = joystick.get_name()

    def update(self, events: List[pygame.event.EventType]):
        """Update events for the joystick."""
        for event in events:
            if event.type == pg.JOYBUTTONDOWN:
                if event.joy == self._id:
                    self._button_type[event.button] = pg.JOYBUTTONDOWN
                    self._button_first[event.button] = True
            elif event.type == pg.JOYBUTTONUP:
                if event.joy == self._id:
                    self._button_type[event.button] = pg.JOYBUTTONUP
            elif event.type == pg.JOYAXISMOTION:
                if event.joy == self._id:
                    # -1 <= event.value <= 1
                    self._axis_value[event.axis] = event.value
                    self._axis_first[event.axis] = True
            elif event.type == pg.JOYHATMOTION:
                if event.joy == self._id:
                    # (-1, -1) <= event.value <= (1, 1)
                    self._hat_value[event.hat] = event.value
                    self._hat_first[event.hat] = True
            elif event.type == pg.JOYBALLMOTION:
                if event.joy == self._id:
                    # event.rel = ?
                    self._ball_value[event.ball] = event.rel
                    self._ball_time[event.ball] = time.time()
                    self._ball_first[event.ball] = True

    @property
    def id(self) -> int:
        """Return the current joystick id."""
        return self._id

    @property
    def name(self) -> str:
        """Return the current joystick name."""
        return self._name

    def push_button(self, button: int, delay: int = 0) -> bool:
        """Know if a joystick button is pushed, depends on delay."""
        if button not in self._button_type:
            return None
        elif self._button_first[button]:
            self._button_first[button] = False
            self._button_time[button] = time.time()
            return True
        elif self._button_type[button] is not pg.JOYBUTTONDOWN:
            return False
        elif time.time() - self._button_time[button] >= delay:
            self._button_time[button] = time.time()
            return True
        return False

    def push_axis(self, axis: int, delay: int = 0) -> bool:
        """Know if a joystick axis is pushed, depends on delay."""
        if axis not in self._axis_value:
            return None
        elif self._axis_first[axis]:
            self._axis_first[axis] = False
            self._axis_time[axis] = time.time()
            return True
        elif -0.1 <= self._axis_value[axis] <= 0.1:
            return False
        elif time.time() - self._axis_time[axis] >= delay:
            self._axis_time[axis] = time.time()
            return True
        return False

    def get_axis(self, axis: int) -> float:
        """Return the current value of the joystick axis."""
        return self._axis_value[axis] if axis in self._axis_value else None

    def push_hat(self, hat: int, delay: int = 0) -> bool:
        """Know if a joystick hat button is pushed, depends on delay."""
        if hat not in self._hat_value:
            return None
        elif self._hat_first[hat]:
            self._hat_first[hat] = False
            self._hat_time[hat] = time.time()
            return True
        elif self._hat_value[hat] == (0, 0):
            return False
        elif time.time() - self._hat_time[hat] >= delay:
            self._hat_time[hat] = time.time()
            return True
        return False

    def get_hat(self, hat: int) -> (int, int):
        """Return the current value of the joystick hat button."""
        return self._hat_value[hat] if hat in self._hat_value else None
