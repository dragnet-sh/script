hs.hotkey.bind({"cmd", "alt", "ctrl"}, "R", function()
        hs.reload()
end)
hs.alert.show("Config Loaded")

hs.hotkey.bind({"cmd", "alt", "ctrl"}, "F", function()
        hs.osascript.applescript(
            'tell application "System Events" to tell process "Flux" to click menu bar item 1 of menu bar 1'
        )
end)