from enum import Enum, unique


@unique
class BrowserType(Enum):
    CHROME = "Chrome"
    EDGE = "Edge"
    FIREFOX = "Firefox"
    OPERA = "Opera"
    SAFARI = "Safari"
    ELECTRON = "Electron"
