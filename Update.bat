@echo off 
cd /d %~dp0

set GITDIR=%~dp0\system\git
set PATH=%GITDIR%\cmd;%PATH%

cd PDF-Parser
git reset --hard HEAD
git clean -f -d
git pull
