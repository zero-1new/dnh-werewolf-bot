$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
$env:PYTHONUNBUFFERED = "1"

& "$PSScriptRoot\.venv\Scripts\python.exe" "$PSScriptRoot\bot.py"
