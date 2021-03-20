#!/usr/bin/python3

import shutil
import json
from os.path import dirname, join

from fontTools.ttLib import TTFont

dest = join(dirname(__file__), "./theme/eos-icons.woff")
shutil.copyfile(
    join(
        dirname(__file__), "./node_modules/eos-icons/dist/fonts/eos-icons.woff"
    ),
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
    ["debug-console-evaluation-input", "arrow_right_alt"],
    ["debug-console-evaluation-prompt", "keyboard_arrow_right"],
    ["debug-pause", "pause"],
    ["debug-start", "play_arrow"],
    ["debug-stop", "stop"],
    ["diff-editor-next-change", "arrow_downward"],
    ["diff-editor-previous-change", "arrow_upward"],
    ["diff-insert", "add"],
    ["diff-diff-review-insert", "add"],
    ["diff-remove", "remove"],
    ["diff-review-remove", "remove"],
    ["diff-review-close", "close"],
    ["extensions-filter", "filter_alt"],
    ["extensions-info-message", "info"],
    ["extensions-install-count", "cloud_download"],
    ["extensions-install-local-in-remote", "cloud_download"],
    ["extensions-install-workspace-recommended", "cloud-download"],
    ["extensions-rating", "star_border"],
    ["extensions-refresh", "refresh"],
    ["extensions-star-empty", "star_outline"],
    ["extensions-star-full", "star"],
    ["extensions-star-half", "star_half"],
    ["extensions-sync-enabled", "sync"],
    ["extensions-sync-ignored", "sync_disabled"],
    ["extensions-warning-message", "warning"],
    ["find-collapsed","keyboard_arrow_right"]
    ["find-expanded", "keyboard_arrow_down"],
    ["find-next-match", "arrow_downward"],
    ["find-previous-match", "arrow_upward"],
    ["folding-collapsed", "keyboard_arrow_right"],
    ["folding-expanded", "keyboard_arrow_down"]
    ["getting-started-beginner", "lightbulb_outline"],
    ["getting-started-setup", "favorite_border"],
    ["goto-next-location", "arrow_downward"],
    ["goto-previous-location", "arrow_upward"],
    ["keybindings-add", "add"],
    ["keybindings-record-keys", "keyboard"],
    ["marker-navigation-next", "keyboard_arrow_down"] ,
    ["marker-navigation-previous", "keyboard_arrow_up"] ,
    ["markers-view-filter", "filter_list"],
    ["markers-view-icon", "warning"],
    ["markers-view-multi-line-collapsed", "keyboard_arrow_down"] ,
    ["markers-view-multi-line-expanded", "keyboard_arrow_up"] ,
    ["notebook-delete-cell", "delete_outline"],
    ["notebook-collapsed", "keyboard_arrow_right"] ,
    ["notebook-edit", "edit"] ,
    ["notebook-execute", "play_arrow"] ,
    ["notebook-expanded", "keyboard_arrow_down"] ,
    ["notebook-kernel-configure", "settings"] ,
    ["notebook-mimetype", "code"] ,
    ["notebook-move-down", "arrow_downward"] ,
    ["notebook-move-up", "arrow_upward"] ,
    ["notebook-open-as-text", "integration_instructions"] ,
    ["notebook-render-output", "preview"] ,
    ["notebook-revert", "undo"] ,
    ["notebook-state-error", "cancel"] ,
    ["notebook-state-success", "check"] ,
    ["notebook-stop-edit", "check"] ,
    ["notifications-clear", "close"] ,
    ["notifications-clear-all", "clear_all"] ,
    ["notifications-collapse", "keyboard_arrow_down"] ,
    ["notifications-configure", "settings"] ,
    ["notifications-expand", "keyboard_arrow_up"] ,
    ["notifications-hide", "keyboard_arrow_down"] ,
    ["open-editors-view-icon", "menu_book"] ,
    ["output-view-icon", "event_note"] ,
    ["panel-close", "close"] ,
    ["panel-maximize", "keyboard_arrow_up"] ,
    ["panel-restore", "keyboard_arrow_down"] ,
    ["parameter-hints-next", "keyboard_arrow_down"] ,
    ["parameter-hints-previous", "keyboard_arrow_up"] ,
    ["ports-forward-icon", "add"] ,
    ["ports-open-browser-icon", "language"] ,
    ["ports-stop-forward-icon", "close"] ,
    ["ports-view-icon", "power"] ,
    ["preferences-clear-input", "clear_all"] ,
    ["private-ports-view-icon", "lock_outline"] ,
    ["public-ports-view-icon", "visibility"] ,
    ["refactor-preview-view-icon", "lightbulb_outline"] ,
    ["remote-explorer-documentation", "menu_book"] ,
    ["remote-explorer-get-started", "star_outline"] ,
    ["remote-explorer-report-issues", "chat_bubble_outline"] ,
    ["remote-explorer-review-issues", "error_outline"] ,
    ["review-comment-collapse", "keyboard_arrow_up"] ,
    ["search-clear-results", "clear_all"] ,
    ["search-hide-replace", "keyboard_arrow_right"] ,
    ["search-new-editor", "note_add"] ,
    ["search-refresh", "refresh"] ,
    ["search-remove", "close"] ,
    ["search-show-replace", "keyboard_arrow_down"] ,
    ["search-view-icon", "search"] ,
    ["settings-add", "add"] ,
    ["settings-discard", "undo"] ,
    ["settings-edit", "edit"] ,
    ["settings-folder-dropdown", "arrow_drop_down"] ,
    ["settings-group-collapsed", "keyboard_arrow_right"] ,
    ["settings-group-expanded", "keyboard_arrow_down"] ,
    ["settings-more-action", "settings"] ,
    ["settings-remove", "close"] ,
    ["settings-sync-view-icon", "sync"] ,
    ["settings-view-bar-icon", "settings"] ,
    ["suggest-more-info", "keyboard_arrow_right"] ,
    ["tasks-list-configure", "settings"] ,
    ["tasks-remove", "close"] ,
    ["terminal-kill", "delete"] ,
    ["terminal-new", "add"] ,
    ["terminal-rename", "settings"] ,
    ["terminal-view-icon", "terminal"] ,
    ["test-view-icon", "flask"] ,
    ["testing-cancel-icon", "close"] ,
    ["testing-error-icon", "warning"] ,
    ["testing-failed-icon", "close"] ,
    ["testing-passed-icon", "check_circle_outline"] ,
    ["testing-queued-icon", "watch"] ,
    ["testing-run-icon", "play_arrow"] ,
    ["timeline-open", "history"] ,
    ["timeline-refresh", "refresh"] ,
    ["timeline-unpin", "push_pin"] ,
    ["timeline-view-icon", "history"] ,
    ["view-pane-container-collapsed", "keyboard_arrow_right"] ,
    ["view-pane-container-expanded", "keyboard_arrow_down"] ,
    ["watch-expressions-add", "add"] ,
    ["watch-expressions-add-function-breakpoint", "add"] ,
    ["widget-close", "close"] 
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
