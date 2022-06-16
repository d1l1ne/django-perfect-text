from django.http import HttpResponse
from django.shortcuts import render
from . import func_module as fm

def help_(request):
    return render(request, 'pt_help.html')

def home(request):
    return render(request, 'pt_home.html')

def result(request):
    get_text = request.POST['usertext']
    get_r = request.POST['urls']
    if get_r == 'urlsn':
        get_text = fm.del_multi_spaces(get_text)
        get_text = fm.del_punctuation_spaces(get_text)
        get_text = fm.del_brackets_spaces(get_text)
        get_text = fm.fix_dashes(get_text)
        get_text = fm.fix_separation_of_sentences(get_text)
    elif get_r == 'urlsy':
        get_text = fm.del_multi_spaces(get_text)
        get_text = fm.del_punctuation_spaces(get_text)
        get_text = fm.del_brackets_spaces(get_text)
        get_text = fm.fix_dashes(get_text)
        get_text = fm.fix_separation_wsites(get_text)
    
    return render(request, 'pt_result.html', {'processed_text':get_text})