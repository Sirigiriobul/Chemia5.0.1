@echo off
call venv\scripts\activate
pytest -s -v --html .report\report.html
pause