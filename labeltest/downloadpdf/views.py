# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse
from django.http.response import FileResponse

def download(request):


    with open('pdfmergerout.pdf', 'rb') as f:
        pdf_contents = f.read()

    os.remove("pdfmergerout.pdf")
    response = HttpResponse(pdf_contents, content_type='application/pdf')
    return response