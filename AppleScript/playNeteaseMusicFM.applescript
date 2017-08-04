on is_running(appName)
	tell application "System Events" to (name of processes) contains appName
end is_running

set musicRunner to is_running("NeteaseMusic")

if musicRunner then
	openNetease()
	playMusic()
else
	openNetease()
	delay 2
	playMusic()
end if


on openNetease()
	tell application "System Events"
		tell application "NeteaseMusic"
			reopen
			activate
		end tell
	end tell
end openNetease

on playMusic()
	tell application "System Events"
		tell application process "NeteaseMusic"
			tell UI element of group 2 of group 1 of group 1 of group 3 of UI element 1 of scroll area 1 of window "网易云音乐"
				click
			end tell
		end tell
	end tell
	
end playMusic