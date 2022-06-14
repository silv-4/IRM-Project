# Commands used for data extraction
For the extraction of the data specific to my script and research several commands and techniques were needed.
There are two scripts: *script.py* and *script2.py*. 

Script.py has the input of two files: before_georgefloyd.txt and after_georgefloyd.txt, with the purpose of getting the output of how many mentions of BLM there are BEFORE the incident and how many there are AFTER the incident.

The second script, script2.py, has the input of one file that represents one individual day such as: 28.txt which represents tweets from the 28th of May. The output of this is the number of mentions on that particular day, this is necessary data for plotting a graph which showcases the day-to-day increase or decrease of the BLM mention in the period BEFORE and AFTER the incident which ranges from the 18th of May up until the 31st of May.

The process will be explained underneath, please read carefully. 

# First Script Information Extraction Commands (script.py):
For retrieving tweets for the week BEFORE George Floyd's death (May 18 - May 24), the following commands were applied:
```gunzip -c Tweets/2020/05/202005NUM:*.out.gz | ./tools/tweet2tab text > /home/s4953266/IRM/before_georgefloyd.txt```
```gunzip -c Tweets/2020/05/202005NUM:*.out.gz | ./tools/tweet2tab text >> /home/s4953266/IRM/before_georgefloyd.txt```

For retrieving tweets for the week AFTER George Floyd's death (May 25 - May 31), the following commands were applied:
```gunzip -c Tweets/2020/05/202005NUM:*.out.gz | ./tools/tweet2tab text > /home/s4953266/IRM/after_georgefloyd.txt```
```gunzip -c Tweets/2020/05/202005NUM:*.out.gz | ./tools/tweet2tab text >> /home/s4953266/IRM/after_georgefloyd.txt```

> With NUM in "/202005NUM" being: 18, 19, 20, 21, 22, 23, 24 (for before_georgefloyd.txt) AND 25, 26, 27, 28, 29, 30, 31 (for after_georgefloyd.txt)

# Second Script Information Extraction Commands (script2.py):
For retrieving tweets for the week BEFORE and AFTER George Floyd's death (May 18 - May 31), the following command were applied:
```gunzip -c Tweets/2020/05/202005NUM:*.out.gz | ./tools/tweet2tab text > /home/s4953266/IRM/NUM.txt```
> With NUM in "/202005NUM" and in "NUM.txt" being: 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, creating individual files for tweets of each day.

Then the files contained within the directory called "IRM" where copied from the server to local laptop by the following command:
```scp s4953266@karora.let.rug.nl:IRM/FILE.txt /home/silvanaxa```

> With FILE being: 18.txt, 19.txt, 20.txt, 21.txt, 22.txt, 23.txt, 24.txt, 25.txt, 26.txt, 27.txt, 28.txt, 29.txt, 30.txt, 31.txt, before_georgefloyd.txt, after_georgefloyd.txt

# Files
The final files needed are named as follows:
1. before_georgefloyd.txt -> contains textual data from the 18th of May 2020 until the 24th of May 2020 (This file is needed for script.py)
2. after_georgefloyd.txt -> contains textual data from the 25th of May 2020 until the 31st of May 2020 (This file is needed for script.py)
3. 18.txt -> contains textual data from specifically the 18th of May 2020; (This file and all of the rest below are needed for script2.py)
4. 19.txt -> the same for the 19th of May 2020
5. 20.txt -> the same for the 20th of May 2020, etc.
6. 21.txt 
7. 22.txt 
8. 23.txt 
9. 24.txt 
10. 25.txt
11. 26.txt 
12. 27.txt 
13. 28.txt 
14. 29.txt 
15. 30.txt 
16. 31.txt
