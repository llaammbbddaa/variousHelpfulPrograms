# variousHelpfulPrograms
just a few programs that i use on my computers to simplify certain tasks

## clenter
help keep the terminal a bit cleaner, especially if you are deep in directories and you dont want half of your screen to be the pwd message
use "clenter -i j" for the best one
### how to install
sudo mv clenter.sh /usr/local/bin/clenter
sudo chmod +x /usr/local/bin/clenter
sudo nano /etc/bash.bashrc
*add this to the bottom -> alias clenter='source /usr/local/bin/clenter'*
exec bash

## cowPlay
cli random music player with funny little cowsay guy
super SUPER simple program, but just something nice to have when i study, as the lack of gui makes for one less distraction

## count
for a particular folder with a bunch of pdfs in it, it will output the total number of pages across all of the files

## display
for a directory, it will output every file within every folder with each increasing level being a differnt color for optimal visualization

## fiftypdf
for a folder of pdfs, it will generate new pdfs of fifty pages each

## videoTime
for a given folder, and its subfolders, it will output the total watchtime for all of the videos

## ytStorage
for a given youtube channel, it will output the total number of videos, total channel duration, and total space it would take to store all of the videos in a couple formats
