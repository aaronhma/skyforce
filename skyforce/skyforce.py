#
# MIT License
#
# Copyright (c) 2017 - 2020 Firebolt Inc,
# Copyright (c) 2020 - Present Aaron Ma.
# All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
from .error import SkyforceImportError
try:
    import time
except ImportError:
    raise SkyforceImportError("Random is not installed!")

__all__ = ["user", "timer", "random", "floor", "round", "calculator", "progress bar"]



# Progress Bar
def progress_bar(t):
    """Prints a progress bar that take t seconds to complete loading."""
    for i in range(1, 101):
        print("\r{:>6}% |{:<30}|".format(
            i, u"\u2588" * round(i // 3.333)), end='', flush=True)
        time.sleep(t/100)

    time.sleep(0.1)
    print("\n")