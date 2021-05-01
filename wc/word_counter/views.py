from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    sentence = request.POST.get('sentence')
    
    words = sentence.split()
    
    word_counts = {}

    for word in words:
        if word in word_counts.keys():
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    word_counts = list(word_counts.items())

    word_counts.sort(key = lambda t : -t[1])

    response = {
        'word_counts' : word_counts
    }

    return render(request, 'result.html', response)
