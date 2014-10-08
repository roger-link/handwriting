from django.views.generic import FormView
from django.http import HttpResponse
from handwriting.forms import ImageForm
from handwriting.tasks import get_text_from_image
from django.conf import settings
import glob
import os


files = glob.glob(settings.PROJECT_PATH + '/handwriting/static/images/*')
choices = [((file, os.path.basename(file))) for file in files]


class HandwritingView(FormView):
    template_name = 'handwriting.html'
    form_class = ImageForm
    success_url = '/handwriting/'

    def get_form(self, form_class):
        # form = super(HandwritingView, self).get_form(form_class)
        # form.fields['images'].choices = choices
        return form

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        image_location = request.POST.get('images')
        if form.is_valid():
            result = get_text_from_image(image_location)
            return HttpResponse(result)
        else:
            return self.form_invalid(form)


