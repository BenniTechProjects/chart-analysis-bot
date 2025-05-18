@echo off
cd /d %~dp0
python scripts\\chart_bot.py >> logs\\output.txt 2>&1
