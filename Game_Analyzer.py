import mss
import mss.tools

def GetScreenResolution():
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        return monitor["width"], monitor["height"]

def TakeScreenShotAtSecionOfScreen(top_left, bottom_right):
    with mss.mss() as sct:
        region = {
            "left": top_left[0],
            "top": top_left[1],
            "width": bottom_right[0] - top_left[0],
            "height": bottom_right[1] - top_left[1]
        }

        img = sct.grab(region)
        mss.tools.to_png(img.rgb, img.size, output="region.png")

screen_width, screen_height = GetScreenResolution()

print(screen_width)
print(screen_height)

TakeScreenShotAtSecionOfScreen((0, 0), (screen_width, screen_height)) # in this case screenshot the section "entire screen"