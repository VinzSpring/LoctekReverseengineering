# reverseengineering the loctek standing desk controller

## general

| PIN | FUN |
| --- | --- |
| 1   | 5V   |
| 2   | GND   |
| 3   | RX   |
| 4   | TX   |
| 5   | oin20  |
| 6   | -   |
| 7   | swim   |
| 8   | rst   |

baud-rate: 9600

## frames when going from 75 to 71cm (memory setting 1)
### RX
```
9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,07,12,07,CF,6F,A5,30,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,07,12,07,CF,7D,A8,B0,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,07,12,07,CF,66,A3,F0,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,07,12,07,CF,4F,7D,31,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,15,BF,C2,9D,9B,07,12,07,CF,06,8B,F0,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,07,12,07,DB,6F,A5,3F,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,07,12,07,DB,7D,A8,BF,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,15,BF,C2,9D,9B,07,12,07,DB,6D,64,BE,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,07,12,07,DB,4F,7D,3E,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,15,BF,C2,9D,9B,07,12,07,DB,06,8B,FF,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D,9B,04,11,7C,C3,9D
````
### TX 
```
0x9B, 0x06, 0x02, 0x02, 0x00, 0x0C, 0xA0, 0x9D //DOWN
0x9B, 0x06, 0x02, 0x01, 0x00, 0xFC, 0xA0, 0x9D //UP
0x9B, 0x06, 0x02, 0x00, 0x00, 0x6C, 0xA1, 0x9D //VOID
```


### assumptions:
packet-structure:

| Start | LEN (including LEN) | DATA | STOP |
| --- | --- | --- | --- |
| 9B | 04 | 15,BF,C2 | 9D |

### after sorting things we get these packets:

```
9B,04,11,7C,C3,9D
9B,04,15,BF,C2,9D
9B,06,02,00,00,6C,A1,9D //TX

9B,07,12,07,CF,06,8B,F0,9D
9B,07,12,07,CF,4F,7D,31,9D
9B,07,12,07,CF,66,A3,F0,9D
9B,07,12,07,CF,6F,A5,30,9D
9B,07,12,07,CF,7D,A8,B0,9D

9B,07,12,07,DB,06,8B,FF,9D
9B,07,12,07,DB,6D,64,BE,9D
9B,07,12,07,DB,6F,A5,3F,9D
9B,07,12,07,DB,4F,7D,3E,9D
9B,07,12,07,DB,7D,A8,BF,9D
```
When we look at the conroller board we can
identify a TM1650 LED controller. When looking at its
datasheet we can see how stuff works. Turns out the desk sends exactly
what to display as raw bytes. Now we can decode this information
(take a look at the python example) to get the displayed height.
Taddaaaaa.

Shoutout to @dev-manuel for being apart of this journey. 👍


Make sure to have a look at the utilities created alongside this project.
