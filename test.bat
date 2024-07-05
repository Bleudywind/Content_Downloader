
cd /d src/Musiques
for /F "delims=" %%i in ('dir /b') do (rmdir "%%i" /s/q || del "%%i" /s/q)
cd ..
cd ..
echo ""
echo "Done everything as been downloaded !"