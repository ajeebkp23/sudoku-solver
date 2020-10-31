import os
from django.urls import path
from django.shortcuts import render
filepath, extension = os.path.splitext(__file__)
ROOT_URLCONF = os.path.basename(filepath)

# Settings
# How to get one new SECRET_KEY ? => django-admin shell -c "from django.core.management import utils; print(utils.get_random_secret_key())"
SECRET_KEY='75dosfl!6328npa*5gs$55xq8s^wuifrc0a$3%d4r(nr**60&='
DEBUG=True
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['.'],
    }
]

# Views
def get_empty():
    inputs = []
    for box in range(9):
        inputs.append(['' for item in range(9)])
    return inputs

def ui(request):
    from django.http.response import HttpResponse
    from solver0 import solve
    outputs = []
    items = []
    inputs = get_empty()
    if request.method == "POST":
        #  Parse inputs into correct format
        items_all = request.POST.getlist('item')
        for box_count in range(9):
            box_list = items_all[box_count*9:((box_count+1)*9)]
            items.append([int(item) if item else '' for item in box_list])
            # items.append(f'{box_count*9}:{((box_count+1)*9) - 1}')
            # 0:8
            # 9:17
            # 18:26

        inputs = items
        outputs = solve(items)

    ctx = {
        'inputs' : inputs,
        'outputs' : outputs,
        'items': items
    }
    return render(request, 'index.html',ctx)

# urls
from django.conf.urls.static import static
urlpatterns = [
    path('',ui),
] + static('/', document_root='.')

# How to run ?
# PYTHONPATH=. DJANGO_SETTINGS_MODULE=djangoserver django-admin.py runserver
# OR after using following (copied from manage.py). Use python <thisfile>.py runserver
#  --noreload if taking more time for a reload
os.environ.setdefault('DJANGO_SETTINGS_MODULE', filepath)
from django.core.management import execute_from_command_line
import sys
execute_from_command_line(sys.argv)