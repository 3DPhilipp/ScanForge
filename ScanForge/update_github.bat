@echo off
echo Updating GitHub Repository...
echo.

echo Checking status...
git status

echo.
echo Adding changes...
git add .

echo.
echo Committing changes...
set /p commit_msg="Enter commit message: "
git commit -m "%commit_msg%"

echo.
echo Pushing to GitHub...
git push origin main

echo.
echo Done!
pause 