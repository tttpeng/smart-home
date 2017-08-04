
on netis_running(appName)
	tell application "System Events" to (name of processes) contains appName
end netis_running

set musicRunner to netis_running("NeteaseMusic")

on is_running()
	tell application "System Events"
		tell application process "NeteaseMusic"
			tell menu "控制" of menu bar item "控制" of menu bar 1
				tell menu item 1 to title contains "暂停"
			end tell
		end tell
	end tell
end is_running

if musicRunner then
	set musicPlay to is_running()
	
	tell application "System Events"
		tell application process "NeteaseMusic"
			tell menu "控制" of menu bar item "控制" of menu bar 1
				if the title of menu item 1 contains "暂停" then
					return 1
				else
					return 0
				end if
			end tell
		end tell
	end tell
else
	return 1 
end if
