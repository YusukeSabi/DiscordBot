#!/bin/sh

pkill -KILL -f "python main.py"
cd /home/ec2-user/discord/DiscordBot/
python main.py &
