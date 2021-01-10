tell application "Time Out"
	activate
end tell
delay 1
tell application "System Events"
	tell process "Time Out"
		
		-- 1. Activate Theme
		select row 3 of outline 1 of scroll area 1 of splitter group 1 of window "Time Out"
		click checkbox "Appearance" of splitter group 1 of window "Time Out"
		tell pop up button 1 of splitter group 1 of window "Time Out"
			click
			delay 0.5
			pick menu item "Inspirational Quotes" of menu 1
		end tell
		
		select row 4 of outline 1 of scroll area 1 of splitter group 1 of window "Time Out"
		click checkbox "Appearance" of splitter group 1 of window "Time Out"
		tell pop up button 1 of splitter group 1 of window "Time Out"
			click
			delay 0.5
			pick menu item "Falling Leaves" of menu 1
		end tell
		
		-- 2. Activate Menu Bar Mode
		
		select row 6 of outline 1 of scroll area 1 of splitter group 1 of window "Time Out"
		click checkbox "Show Time Out status in the menu bar" of splitter group 1 of window "Time Out"
		click radio button "Don't include Time Out in the Dock" of splitter group 1 of window "Time Out"
		
		delay 0.5
		
		-- 3. Close the Window
		click button 1 of window "Time Out"
		
	end tell
	
end tell
