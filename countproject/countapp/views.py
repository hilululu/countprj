from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
# text는 변수값
    text=request.GET['fulltext'] #fulltext는 home에서 받은 name
    word_list = text.split() # .split() 문자열 짜르기 len()은 문자열의 개수를 세줌
    word_dictionary = {} #빈 사전

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:

            word_dictionary[word] = 1
    return render(request, 'result.html', {'fulltext1' : text, 'total' : len(word_list), 'dictionary': word_dictionary.items()})
    # 앞에게 key 뒤에게 value key는 '' 사이에 쓴다.
    # return 3번째 인수는 사전형 객체 {}안에 쓴다.