```
time ffmpeg -i ../sxf.mp4 -filter:v fps=fps=1/60 sxf/%d.jpg
```
Creates 24 frames in 50.1 seconds

```
time for i in {0..24} ; do ffmpeg -accurate_seek -ss `let "j = $i * 60" && echo $j` -i ../sxf.mp4   -frames:v 1 sxf/$i.jpg ; done
```
Creates 24 frames in 7.7 seconds

```
time ffmpeg -i ../sxf.mp4 -filter:v fps=fps=24 sxf/%d.jpg
```
Creates 34763 frames in 8:19 = 499 seconds


```
time for i in {0..34763} ; do ffmpeg -accurate_seek -ss `let "j = $i * 1" && echo $j` -i ../sxf.mp4 -frames:v 1 sxf/$i.jpg ; done
```
Creates 34763 frames in x seconds

ver 1 creates 1450 frames in 1:19 = 79 seconds

ver 2 creates 1450 frames in 8:50 = 530 seconds

