
REM setlocal

:main
call :%*
goto :eof

:listim
docker images
goto :eof

:listco
docker ps -a
goto :eof

:rmco
for %%i in (%*) do (
    echo docker rm %%i
    for /f "tokens=1 delims= " %%j in ('docker ps -a ^| findstr "%%i"') do (
	echo docker stop %%j
	docker stop %%j
	echo docker rm %%j
	docker rm %%j
    )
)
goto :eof

:logsco
docker logs %1
goto :eof

:rmim
for %%i in (%*) do (
    echo docker rmi %%i
    REM docker rmi %%i
    for /f "tokens=3 delims= " %%j in ('docker images ^| findstr "%%i"') do (
        echo docker rmi %%j
        docker rmi %%j
    )
)
goto :eof

:dcup
echo docker-compose up -d
docker-compose up -d
goto :eof

:dcrund
echo docker-compose run -d $2
docker-compose run -d $2
goto :eof

:dcstop
echo docker-compose stop
docker-compose stop
goto :eof

:dcdown
echo docker-compose down
docker-compose down
goto :eof

:ebash
docker exec -it %1 bash
goto :eof

:ecmd
docker run -it --rm %1 cmd
goto :eof

:razzle
pushd e:\DCWA
call tools\lcsrazzle.cmd /Bin:e:\bins /Objects:e:\obj /Branch:lcsCMF /Source:CMF /Flavor:checked /Architecture:amd64 /nooacr
goto :eof

:diff
e:\DCWA\tools\sdpack\bin\windiff.exe %*
goto :eof

:adb
setlocal
REM @echo off
@set platformtoolsdir=%USERPROFILE%\AppData\Local\Android\sdk\platform-tools
@echo %platformtoolsdir%\adb.exe %*
@%platformtoolsdir%\adb.exe %*
endlocal
goto :eof

:android
setlocal
@echo off
set JAVA_HOME=%ProgramFiles%\Android\Android Studio\jre
set toolsdir=%USERPROFILE%\AppData\Local\Android\sdk\tools
call %toolsdir%\android.bat %*
endlocal
goto :eof

:hello
echo %cd% hello world...
goto :eof

REM endlocal
