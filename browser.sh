/usr/bin/osascript -e 'tell application "Safari"' -e "activate" -e 'tell application "System Events"' -e 'keystroke "f" using {control down, command down}' -e 'tell process "Safari"' -e 'set frontmost to true' -e 'click menu item "Always Show Toolbar in Full Screen" of menu "View" of menu bar 1' -e 'end tell' -e 'delay 2' -e 'repeat 100 times' -e 'keystroke "+" using {command down}' -e 'keystroke "+" using {command down}' -e 'keystroke "+" using {command down}' -e 'keystroke "=" using {command down}' -e "end repeat" -e "end tell" -e "end tell"