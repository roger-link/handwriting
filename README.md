handwriting
===========

Django Application to test out google's Tesseract. This application uses pyocr as a wrapper to access Tesseract. It will allow the user to choose any image placed in the static/images directory and display the image and the text from Tesseract. The image to text translation is performed as a Celery task.


installation

clone the repo
pip install -r requirments.txt
python manage.py collectstatic

install tesseract - https://code.google.com/p/tesseract-ocr/
(ensure you can call "tesseract" from the command prompt)


python manage.py celery worker
python manage.py runserver
