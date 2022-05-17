Run:
mplayer -vo jpeg ../../sxf.mp4

While in sxf directory

use time(mplayer...) to get running time

Clear sxf directory with
rm rf 
or use 
ls | grep -P ".*jpg" | xargs -d"\n" rm
to delete all jpg files in the current directory
