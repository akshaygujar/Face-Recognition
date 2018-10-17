# Face-Recognition
It detect the face via webcam and recognized it by using Haar cascade files.

# Setup:
pip install opencv-contrib-python

pip uninstall opencv-python

pip install pillow

pip install numpy


#  Process
DatasetCreator.py will ask your Id. You need to enter your ID and hit enter. After that webcam will open and within 5-7 sec it takes your 
sample and save it in DataSet folder.

After this, run DatasetTrainner.py to build a model. Script automaticaly save model in Trainner folder. 

Then, run Detecter.py to detect and recognize your face by using your weebcam. 


Thank you...!
