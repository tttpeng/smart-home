
on netis_running(appName)
	tell application "System Events" to (name of processes) contains appName
end netis_running

set musicRunner to netis_running("NeteaseMusic")
if musicRunner then
	tell application "System Events"
		tell application process "NeteaseMusic"
			tell menu item 1 of menu "控制" of menu bar item "控制" of menu bar 1
				click
			end tell
		end tell
	end tell
end if