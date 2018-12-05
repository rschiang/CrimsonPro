#!/usr/bin/env python3
"""Fix the font names for the Italic variable font"""
# TODO (M Foley) this shouldn't be required. Send fix to fontmake
from fontTools.ttLib import TTFont
from glob import glob
import os

font_paths = glob("../fonts/variable/*.ttf")

for path in font_paths:
    font = TTFont(path)
    if "CrimsonPro-Italic-VF.ttf" == os.path.basename(path):
        font["name"].setName("Crimson Pro ExtraLight Italic", 4, 3, 1, 1033)
        font["name"].setName("CrimsonPro-ExtraLightItalic", 6, 3, 1, 1033)
        font["name"].setName("ExtraLight Italic", 17, 3, 1, 1033)
        font["name"].setName("1.000;FoHa;CrimsonPro-ExtraLightItalic", 3, 3, 1, 1033)

    del font["MVAR"]
    font.save(path + ".fix")
