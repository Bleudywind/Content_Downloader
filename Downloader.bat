docker build -t yt-converter src
docker run -it --rm -v %cd%/src:/usr/src/app yt-converter
@echo off
@robocopy ./src/Musiques ./target/Musiques /s /e /r:0 /z /njh /njs /ndl /nc /ns
@robocopy ./src/Video ./target/Video /s /e /r:0 /z /njh /njs /ndl /nc /ns
@cd /d src/Musiques
@for /F "delims=" %%i in ('dir /b') do (rmdir "%%i" /s/q || del "%%i" /s/q)
@cd ..
@cd ..
@cd /d src/Video
@for /F "delims=" %%i in ('dir /b') do (rmdir "%%i" /s/q || del "%%i" /s/q)
@cd ..
@cd ..
@echo on
@echo:
@echo:
@echo Done everything as been downloaded !