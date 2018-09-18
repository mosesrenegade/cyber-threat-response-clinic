Installing the Headless Container in Dev mode:
sudo docker run -d -P -p 5900:5900 -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome-debug

