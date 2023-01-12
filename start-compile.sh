#!/bin/bash

# es wird die Verzeichnisstruktur von IntelliJ IDEA angenommen
# für Eclipse sind die Verzeichnisse entsprechend anzupassen

port=8554
# video=videos/htw.mjpeg
video=htw.mjpeg
# video=handyvideo.mjpeg
src=src
bin=out/production/RTSP-Streaming


# Kompilierung
echo "compile classes..."
javac -cp $src ${src}/Server.java  -d $bin 
javac -cp $src ${src}/Client.java  -d $bin 

# Start
echo "start classes..."
java -cp $bin  Server $port &
sleep 1
java -cp $bin  Client localhost $port $video &

# wait for ctrl+c is pressed, then kill all java processes and exit
trap "killall java; exit" SIGINT SIGTERM

# keep it open
while true; do sleep 1; done