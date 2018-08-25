# coding: utf-8

import pygame
import pygame.locals as cst

from tools import decorators
import time


@decorators.singleton(parameters=False)
class Screen(object):
    """Simulate a screen software."""

    def __init__(self, size=(800, 600), color=(255, 255, 255), title="pygame window", flags=None):
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

    def update(self, events=None):
        """Update some events for the screen."""
        if events is None:
            events = []
        for event in events:
            if event.type == cst.QUIT:
                self.running = False
            elif event.type == cst.ACTIVEEVENT:
                pass
                # event.gain = [0, 1]
                # event.state = [?, 1, 2, ?, 6, ?]
            elif event.type == cst.VIDEOEXPOSE:
                pygame.display.update()
            elif event.type == cst.VIDEORESIZE:
                if event.size != self.size:
                    self.size = event.size

    def blit(self, source, destination, area=None, special_flags=0):
        """Display an image onto the screen."""
        return self.image.blit(source, destination, area, special_flags)

    @property
    def width(self):
        """Return the current screen width."""
        if self._fullscreen:
            return self._fullscreen_size[0]
        return self._windowedscreen_size[0]

    @width.setter
    def width(self, value=800):
        """Modify the screen width."""
        height = self._windowedscreen_size[1]
        self._windowedscreen_size = (value, height)
        self.reset_screen()

    @property
    def height(self):
        """Return the current screen height."""
        if self._fullscreen:
            return self._fullscreen_size[1]
        return self._windowedscreen_size[1]

    @height.setter
    def height(self, value=600):
        """Modify the screen height."""
        width = self._windowedscreen_size[0]
        self._windowedscreen_size = (width, value)
        self.reset_screen()

    @property
    def size(self):
        """Return the current screen size."""
        if self._fullscreen:
            return self._fullscreen_size
        return self._windowedscreen_size

    @size.setter
    def size(self, value=(800, 600)):
        """Modify the screen size."""
        self._windowedscreen_size = value
        self.reset_screen()

    @property
    def fullscreen(self):
        """Return the current value of the full screen mode."""
        return self._fullscreen

    @fullscreen.setter
    def fullscreen(self, value=True):
        """Turn the full screen mode to value."""
        self._fullscreen = value
        self.reset_screen()

    @property
    def fullscreen_width(self):
        """Return the current fullscreen width."""
        return self._fullscreen_size[0]

    @property
    def fullscreen_height(self):
        """Return the current fullscreen height."""
        return self._fullscreen_size[1]

    @property
    def fullscreen_size(self):
        """Return the current fullscreen size."""
        return self._fullscreen_size

    @property
    def doublebuf(self):
        """Return the current value of the double buf mode."""
        return self._doublebuf

    @doublebuf.setter
    def doublebuf(self, value=True):
        """Turn the double buf mode to value."""
        self._doublebuf = value
        self.reset_screen()

    @property
    def hwsurface(self):
        """Return the current value of the hwsurface mode."""
        return self._hwsurface

    @hwsurface.setter
    def hwsurface(self, value=True):
        """Turn the hwsurface mode to value."""
        self._hwsurface = value
        self.reset_screen()

    @property
    def opengl(self):
        """Return the current value of the opengl mode."""
        return self._opengl

    @opengl.setter
    def opengl(self, value=True):
        """Turn the opengl mode to value."""
        self._opengl = value
        self.reset_title()

    @property
    def resizable(self):
        """Return the current value of the resizable mode."""
        return self._resizable

    @resizable.setter
    def resizable(self, value=True):
        """Turn the resizable mode to value."""
        self._resizable = value
        self.reset_screen()

    @property
    def noframe(self):
        """Return the current value of the noframe mode."""
        return self._noframe

    @noframe.setter
    def noframe(self, value=True):
        """Turn the noframe mode to value."""
        self._noframe = value
        self.reset_screen()

    @property
    def flags(self):
        """Return the current value of the screen flags."""
        flags = 0
        if self._fullscreen:
            flags += cst.FULLSCREEN
        if self._doublebuf:
            flags += cst.DOUBLEBUF
        if self._hwsurface:
            flags += cst.HWSURFACE
        if self._opengl:
            flags += cst.OPENGL
        if self._resizable:
            flags += cst.RESIZABLE
        if self._noframe:
            flags += cst.NOFRAME
        return flags

    @property
    def color(self):
        """Return the current screen background color."""
        return self._color

    @color.setter
    def color(self, value=(0, 0, 0)):
        """Modify the screen background color."""
        self._color = value
        self.reset_color()

    @property
    def title(self):
        """Return the current screen title."""
        return self._title

    @title.setter
    def title(self, value="pygame window"):
        """Modify the screen title."""
        self._title = value
        self.reset_title()

    @property
    def image(self):
        """Return the current screen image."""
        return pygame.display.get_surface()

    @property
    def area(self):
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

    def update(self, events=None):
        """Update events for the keyboard."""
        if events is None:
            events = []
        for event in events:
            if event.type == cst.KEYDOWN:
                self._key_type[event.key] = cst.KEYDOWN
                self._key_first[event.key] = True
                print(f':{event.unicode},{pygame.key.name(event.key)}:')
                print(event.unicode == cst.K_ESCAPE)
                if event.unicode != '':
                    self._key_type[event.unicode] = cst.KEYDOWN
                    self._key_first[event.unicode] = True
                    self._unicode[(event.key, event.mod)] = event.unicode
                if pygame.key.name(event.key) != '':
                    self._key_type[pygame.key.name(event.key)] = cst.KEYDOWN
                    self._key_first[pygame.key.name(event.key)] = True
            elif event.type == cst.KEYUP:
                self._key_type[event.key] = cst.KEYUP
                if (event.key, event.mod) in self._unicode:
                    unicode = self._unicode[(event.key, event.mod)]
                    self._key_type[unicode] = cst.KEYUP
                if pygame.key.name(event.key) != '':
                    self._key_type[pygame.key.name(event.key)] = cst.KEYUP

    def push(self, key, delay=0):
        """Know if a keyboard key is pushed, depends on delay."""
        if key not in self._key_type or key not in self._key_first:
            return None
        elif self._key_first[key] is True:
            self._key_first[key] = False
            self._key_time[key] = time.time()
            return True
        elif self._key_type[key] is not cst.KEYDOWN:
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

    def update(self, events=None):
        """Update events for the mouse."""
        if events is None:
            events = []
        self._rel = (0, 0)
        for event in events:
            if event.type == cst.MOUSEBUTTONDOWN:
                self._button_type[event.button] = cst.MOUSEBUTTONDOWN
                self._button_first[event.button] = True
            elif event.type == cst.MOUSEBUTTONUP:
                self._button_type[event.button] = cst.MOUSEBUTTONUP
            elif event.type == cst.MOUSEMOTION:
                self._pos = event.pos
                self._rel = event.rel

    @property
    def xpos(self):
        """Return the current x mouse position."""
        return self._pos[0]

    @property
    def ypos(self):
        """Return the current y mouse position."""
        return self._pos[1]

    @property
    def pos(self):
        """Return the current mouse position."""
        return self._pos

    @property
    def xrel(self):
        """Return the current relative x mouse position."""
        return self._rel[0]

    @property
    def yrel(self):
        """Return the current relative y mouse position."""
        return self._rel[1]

    @property
    def rel(self):
        """Return the current relative mouse position."""
        return self._rel

    def move(self):
        """Know if the mouse is moving."""
        return not self._rel == (0, 0)

    def push(self, button, delay=0):
        """Know if a mouse button is pushed, depends on delay."""
        if button not in self._button_type:
            return None
        elif self._button_first[button]:
            self._button_first[button] = False
            self._button_time[button] = time.time()
            return True
        elif self._button_type[button] is not cst.MOUSEBUTTONDOWN:
            return False
        elif time.time() - self._button_time[button] >= delay:
            self._button_time[button] = time.time()
            return True
        return False

    @staticmethod
    def set_visible(value=True):
        """Turn the mouse cursor visibility to value."""
        pygame.mouse.set_visible(value)

    @staticmethod
    def set_pos(pos=None):
        """Permanently block the mouse cursor to a screen position."""
        if pos is None:
            pos = [0, 0]
        pygame.mouse.set_pos(pos)

    def inside(self, area):
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

    def __init__(self, id_=0):
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

    def update(self, events=None):
        """Update events for the joystick."""
        if events is None:
            events = []
        for event in events:
            if event.type == cst.JOYBUTTONDOWN:
                if event.joy == self._id:
                    self._button_type[event.button] = cst.JOYBUTTONDOWN
                    self._button_first[event.button] = True
            elif event.type == cst.JOYBUTTONUP:
                if event.joy == self._id:
                    self._button_type[event.button] = cst.JOYBUTTONUP
            elif event.type == cst.JOYAXISMOTION:
                if event.joy == self._id:
                    # -1 <= event.value <= 1
                    self._axis_value[event.axis] = event.value
                    self._axis_first[event.axis] = True
            elif event.type == cst.JOYHATMOTION:
                if event.joy == self._id:
                    # (-1, -1) <= event.value <= (1, 1)
                    self._hat_value[event.hat] = event.value
                    self._hat_first[event.hat] = True
            elif event.type == cst.JOYBALLMOTION:
                if event.joy == self._id:
                    # event.rel = ?
                    self._ball_value[event.ball] = event.rel
                    self._ball_time[event.ball] = time.time()
                    self._ball_first[event.ball] = True

    @property
    def id(self):
        """Return the current joystick id."""
        return self._id

    @property
    def name(self):
        """Return the current joystick name."""
        return self._name

    def push_button(self, button, delay=0):
        """Know if a joystick button is pushed, depends on delay."""
        if button not in self._button_type:
            return None
        elif self._button_first[button]:
            self._button_first[button] = False
            self._button_time[button] = time.time()
            return True
        elif self._button_type[button] is not cst.JOYBUTTONDOWN:
            return False
        elif time.time() - self._button_time[button] >= delay:
            self._button_time[button] = time.time()
            return True
        return False

    def push_axis(self, axis, delay=0):
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

    def get_axis(self, axis):
        """Return the current value of the joystick axis."""
        return self._axis_value[axis] if axis in self._axis_value else None

    def push_hat(self, hat, delay=0):
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

    def get_hat(self, hat):
        """Return the current value of the joystick hat button."""
        return self._hat_value[hat] if hat in self._hat_value else None

# if __name__ == "__main__":
#     import sys
#
#     pygame.init()
#     clock = pygame.time.Clock()
#     screen = Screen()
#     keyboard = Keyboard()
#     while screen.running:
#         events = pygame.event.get()
#         screen.update(events)
#         keyboard.update(events)
#         if keyboard.push(cst.K_ESCAPE):
#             screen.running = False
#         if keyboard.push('+', 99):
#             print("+")
#         pygame.display.update()
#         clock.tick(120)
#     pygame.quit()
#     sys.exit()
