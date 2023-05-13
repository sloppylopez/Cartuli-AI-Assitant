@echo off
for /f "tokens=2 delims=," %%a in ('tasklist /fi "imagename eq cmd.exe" /fo csv /nh') do taskkill /f /pid %%a
