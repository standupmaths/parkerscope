# parkerscope
Code used to log data from the ALX-1309 light meter, as seen in this Stand-up Maths video: 

It took a while to work out how to get data from the ALX-1309 without using the ancient Windows-only softwear it came with.

We are deeply in debt to this paper:
https://ieeexplore.ieee.org/abstract/document/7147178

Which contains this table:
TABLE II. THE CORRECT INTERPRETATION OF ACQUIRED ILLUMINATION DATA

Hexadecimal representation of the String	Array elements	Illumination (lux)	Illumination range (lux)
CE 00 80 14 92	0, 0, 80, 14, 92	1492	400-4000
CE 01 80 18 14	0, 1, 80, 18, 14	181,4	0-400
CE 01 88 04 95	0, 1, 88, 4, 95	49500	40000-400000
CE 02 88 09 17	0, 2, 88, 9, 17	9170	4000-40000
