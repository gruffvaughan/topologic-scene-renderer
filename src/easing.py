import math


def linear(t):
    return t


def ease_in_out_cubic(t):
    return 4 * t * t * t if t < 0.5 else 1 - pow(-2 * t + 2, 3) / 2


def ease_in_out_sine(t):
    return -(math.cos(math.pi * t) - 1) / 2


easing_functions = {
    "Linear": linear,
    "Ease In & Out, Cubic": ease_in_out_cubic,
    "Ease In & Out, Sine": ease_in_out_sine,
}
