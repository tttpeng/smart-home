
on netis_running(appName)
	tell application "System Events" to (name of processes) contains appName
end netis_running

set musicRunner to netis_running("NeteaseMusic")

if musicRunner then
activate application "NeteaseMusic"
tell application "System Events"
	tell process "NeteaseMusic"
		tell menu item 1 of menu "控制" of menu bar item "控制" of menu bar 1
			perform action "AXPress"
		end tell
		set visible to false
	end tell
end tell
end if