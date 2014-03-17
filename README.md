handwriting
===========

Django Application to test out google's Tesseract. This application uses pyocr as a wrapper to access Tesseract. It will allow the user to choose any image placed in the static/images directory and display the image and the text from Tesseract. The image to text translation is performed as a Celery task.


<strong>Installation</strong>

1. clone the repo
2. pip install -r requirments.txt
3. python manage.py collectstatic

4. install <a href='http://www.leptonica.com/'>leptonica</a> (Ubuntu instructions <a href='https://gist.github.com/roger-link/2a8f5df81f2a7ceabe45'>here</a>)
5. install <a href='https://code.google.com/p/tesseract-ocr/'>tesseract</a>(Ubuntu instructions <a href='https://gist.github.com/roger-link/2a8f5df81f2a7ceabe45'>here</a>)
   


5. python manage.py celery worker
6. python manage.py runserver
