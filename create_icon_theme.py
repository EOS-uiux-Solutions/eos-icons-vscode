#!/usr/bin/python3

import shutil
import json
from os.path import dirname, join

from fontTools.ttLib import TTFont

dest = join(dirname(__file__), "./theme/eos-icons.woff")
shutil.copyfile(
    join(dirname(__file__), "./node_modules/eos-icons/dist/fonts/eos-icons.woff"),
    dest,
)

code_points = {}

with TTFont(dest, 0, ignoreDecompileErrors=True) as ttf:
    for x in ttf["cmap"].tables:
        for (code, name) in x.cmap.items():
            code_points[name] = code


icon_to_glyph_mapping = [
    ["accounts-view-bar-icon", "account_circle"],
    ["callhierarchy-incoming", "call_received"],
    ["callhierarchy-outgoing", "call_made"],
    ["callstack-view-session", "bug_report"],
    ["comments-view-icon", "comment"],
    ["debug-configure", "settings_applications"],
    ["extensions-manage", "settings_applications"],
    ["settings-view-bar-icon", "settings_applications"],
]

eos_icons_theme = {
    "fonts": [
        {
            "id": "eos-icons",
            "src": [
                {
                    "path": "./eos-icons.woff",
                    "format": "woff",
                },
            ],
            "weight": "normal",
            "style": "normal",
        },
    ],
    "iconDefinitions": {},
}

for (icon_name, glyph_name) in icon_to_glyph_mapping:
    eos_icons_theme["iconDefinitions"][icon_name] = {
        "fontCharacter": chr(code_points[glyph_name]),
    }

with open(
    join(dirname(__file__), "theme/eos-icons-product-icon-theme.json"), "w"
) as product_icon_file:
    product_icon_file.write(json.dumps(eos_icons_theme, indent=2))
