# FRemover


Do you watch movies with your children  on OTT? If yes, in most of the movies, abusive languages are spoken and they may generate toxicity in them. They will think that using abusive words is normal. My solution will tackle this problem of the society. This will censor bad words if found in an audio file. It uses google cloud speech to text to get timestamps of the words spoken in the audio and a beep sound is played when a bad word is detected in an audio. 

In later versions, it will support audio censoring in a video and in future, it will censor bad visuals in a video. 

Warning: if you are soft hearted, don't open AbusiveWords.txt. The authors intention was not to hurt anyone and instead protect this beautiful world from these abusive words.

## Docs 

### Requirements

Make sure you have a Google Cloud Account with speech to text api enabled and google cloud config file's path set up as environment variable. 

### Installation Instructions

#### 1 Clone this repo using git command:

<code>git clone https://github.com/Hardik14092009/FRemover.git</code>

#### 2 install necessary packages

<code>pip install google-cloud-speech</code>
<code>pip install pygame</code>

#### Run the code

--> Open FRemover.py in FRemover folder





