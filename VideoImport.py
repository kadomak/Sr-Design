"""
Name: VideoImport
Author: Kowe Kadoma
Purpose: Pull a video from the cloud and load into
         the program
Date: Jan 16, 2021
Functional: not yet tested
Challenges: scraping the video from google photos or google drive
            (google cloud storage isn't a free service)
"""

#Imports
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import datetime
import urllib.request as req
import cv2

cred = credentials.Certificate('Path\to\your\google-credential-file.json')
app = firebase_admin.initialize_app(cred, {'storageBucket': 'cnc-designs.appspot.com'}, name='storage')
bucket = storage.bucket(app=app)

def generate_image_url(blob_path):
    """ generate signed URL of a video stored on google storage.
        Valid for 300 seconds in this case. You can increase this
        time as per your requirement.
    """
    blob = bucket.blob(blob_path)
    return blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')


url = generate_image_url('sample1.mp4')
req.urlretrieve(url, "sample1.mp4")
cap = cv2.VideoCapture('sample1.mp4')

if cap.isOpened():
    print ("File Can be Opened")
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        #print cap.isOpened(), ret
        if frame is not None:
            # Display the resulting frame
            cv2.imshow('frame',frame)
            # Press q to close the video windows before it ends if you want
            if cv2.waitKey(22) & 0xFF == ord('q'):
                break
        else:
            print("Frame is None")
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    print ("Video stop")
else:
    print("Not Working")