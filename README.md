# math-vision
Translate mathematical expressions in live or recorded lectures into LaTeX code. To help note taking during math lecture a bit less tedious.

Install dependencies:

```
pip install -r requirements.txt
```

## Description:
Currently this repo consists of 3 python scripts. stream.py is a simple opencv script that captures frames and store them inside frames folder. frame-selection.py is a similar script but it is a little bit more efficient in capturing frames. It only saves a frame when there is a significant change in frames. And lastly, hello.py reads the frame and hits open ai for interpretation.


## Run the app:

First start the video stream:

```
python frame-selection.py
```

Then hit openai: 

```
python hello.py
```

## Areas for improvement:
I am still working on a more efficient way for selecting frames. One way to make it more efficient is to define a ROI (Region of Interest). By defining a ROI, we will only detect frame selection algorithm on the region of interest. This reduces the number of frames sent to openai by a significant amount which saves a lot of computation and money. 