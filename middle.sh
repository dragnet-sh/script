#! /usr/bin/env bash

ps aux | grep -i '[m]iddleclick' | awk '{print $2}' | xargs sudo kill -9
open -a ~/Applications/MiddleClick.app/
