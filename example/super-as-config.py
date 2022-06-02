# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# define timeout for multipurpose_modmap
define_timeout(1)

# [Global modemap] Change modifier keys as in xmodmap
define_modmap({
    Key.CAPSLOCK: Key.LEFT_CTRL,
    # Refer:
    # https://qiita.com/junkoda/items/fc414a11f418766004f0#4-configpy-%E3%82%92%E7%B7%A8%E9%9B%86%E3%81%99%E3%82%8B
    Key.LEFT_META: Key.RIGHT_META,
})

# [Conditional modmap] Change modifier keys in certain applications
define_conditional_modmap(re.compile(r'Emacs'), {
    Key.RIGHT_CTRL: Key.ESC,
})

# [Multipurpose modmap] Give a key two meanings. A normal key when pressed and
# released, and a modifier key when held down with another key. See Xcape,
# Carabiner and caps2esc for ideas and concept.
define_multipurpose_modmap(
    # Enter is enter when pressed and released. Control when held down.
    {Key.ENTER: [Key.ENTER, Key.RIGHT_CTRL]}

    # Capslock is escape when pressed and released. Control when held down.
    # {Key.CAPSLOCK: [Key.ESC, Key.LEFT_CTRL]
    # To use this example, you can't remap capslock with define_modmap.
)

# [Conditional multipurpose modmap] Multipurpose modmap in certain conditions,
# such as for a particular device.
define_conditional_multipurpose_modmap(lambda wm_class, device_name: device_name.startswith("Microsoft"), {
   # Left shift is open paren when pressed and released.
   # Left shift when held down.
   Key.LEFT_SHIFT: [Key.KPLEFTPAREN, Key.LEFT_SHIFT],

   # Right shift is close paren when pressed and released.
   # Right shift when held down.
   Key.RIGHT_SHIFT: [Key.KPRIGHTPAREN, Key.RIGHT_SHIFT]
})


# Keybindings for Firefox/Chrome
define_keymap(re.compile("Firefox|Google-chrome"), {
    # Ctrl+Alt+j/k to switch next/previous tab
    K("Win-M-j"): K("Win-TAB"),
    K("Win-M-k"): K("Win-Shift-TAB"),
    # Type C-j to focus to the content
    K("Win-j"): K("Win-f6"),
    # very naive "Edit in editor" feature (just an example)
    K("Win-o"): [K("Win-a"), K("Win-c"), launch(["gedit"]), sleep(0.5), K("Win-v")]
}, "Firefox and Chrome")

# Keybindings for Zeal https://github.com/zealdocs/zeal/
# define_keymap(re.compile("Zeal"), {
#     # Ctrl+s to focus search area
#     K("Win-s"): K("Win-k"),
# }, "Zeal")

# Emacs-like keybindings in non-Emacs applications
define_keymap(lambda wm_class: wm_class not in ("Emacs", "URxvt"), {
    # Cursor
    K("Win-b"): with_mark(K("left")),
    K("Win-f"): with_mark(K("right")),
    K("Win-p"): with_mark(K("up")),
    K("Win-n"): with_mark(K("down")),
    K("Win-h"): with_mark(K("backspace")),
    # Forward/Backward word
    K("M-b"): with_mark(K("Win-left")),
    K("M-f"): with_mark(K("Win-right")),
    # Beginning/End of line
    K("Win-a"): with_mark(K("home")),
    K("Win-e"): with_mark(K("end")),
    # Page up/down
    K("M-v"): with_mark(K("page_up")),
    K("Win-v"): with_mark(K("page_down")),
    # Beginning/End of file
    K("M-Shift-comma"): with_mark(K("Win-home")),
    K("M-Shift-dot"): with_mark(K("Win-end")),
    # Newline
    K("Win-m"): K("enter"),
    K("Win-j"): K("enter"),
    K("Win-o"): [K("enter"), K("left")],
    # Copy
    K("Win-w"): [K("Win-x"), set_mark(False)],
    K("M-w"): [K("Win-c"), set_mark(False)],
    K("Win-y"): [K("Win-v"), set_mark(False)],
    # Delete
    K("Win-d"): [K("delete"), set_mark(False)],
    K("M-d"): [K("Win-delete"), set_mark(False)],
    # Kill line
    K("Win-k"): [K("Shift-end"), K("C-x"), set_mark(False)],
    # Undo
    K("Win-slash"): [K("Win-z"), set_mark(False)],
    K("Win-Shift-ro"): K("Win-z"),
    # Mark
    K("Win-space"): set_mark(True),
    K("Win-M-space"): with_or_set_mark(K("Win-right")),
    # Search
    K("Win-s"): K("F3"),
    K("Win-r"): K("Shift-F3"),
    K("M-Shift-key_5"): K("Win-h"),
    # Cancel
    K("Win-g"): [K("esc"), set_mark(False)],
    # Escape
    K("Win-q"): escape_next_key,
    # C-x YYY
    K("Win-x"): {
        # C-x h (select all)
        K("h"): [K("Win-home"), K("Win-a"), set_mark(True)],
        # C-x C-f (open)
        K("Win-f"): K("Win-o"),
        # C-x C-s (save)
        K("Win-s"): K("Win-s"),
        # C-x k (kill tab)
        K("k"): K("Win-f4"),
        # C-x C-c (exit)
        K("Win-c"): K("Win-q"),
        # cancel
        K("Win-g"): pass_through_key,
        # C-x u (undo)
        K("u"): [K("Win-z"), set_mark(False)],
    }
}, "Emacs-like keys")

