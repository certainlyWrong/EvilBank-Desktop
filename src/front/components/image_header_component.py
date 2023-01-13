from random import randint

from flet import (Image, ImageFit)


def imageHeaderComponent(height=200) -> Image:
    return Image(
        f"images/bg{randint(1, 6)}.jpg",
        height=height,
        width=20000,
        fit=ImageFit.FIT_WIDTH,
    )
