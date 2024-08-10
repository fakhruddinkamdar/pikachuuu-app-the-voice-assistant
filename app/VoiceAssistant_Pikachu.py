import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import yfinance as yf
import wolframalpha
import translators as ts
import requests
import wikipedia






# wolfram_ alpha api
wolfram_api = 'GPA3TX-4PW3EHQH2J'

# new api
news_api_key = '250277b739a54ebf9d7012fe3fcc59eb'

#weather api
weather_api_key='2b6c49620e67485ba8b850f974c7acd1'

def wolfram_alpha_country_capital(text):
    client = wolframalpha.Client(wolfram_api)
    result = client.query(text)
    answer = next(result.results).text
    answer_split = answer.split()
    capital_result = 'The capital of ' + answer_split[-1] + ' is ' + answer_split[0]
    print(capital_result)
    pikachu_talk(capital_result)

def wolfram_alpha_calculator(text):
    client = wolframalpha.Client(wolfram_api)
    result = client.query(text)
    answer = next(result.results).text
    print('The answer is ' + answer)
    pikachu_talk('The answer is ' + answer)
    
def wolfram_alpha_president(text):
    client = wolframalpha.Client(wolfram_api)
    result = client.query(text)
    answer = next(result.results).text
    print('The president of the following nation is ' + answer)
    pikachu_talk('The president of the following nation is ' + answer)
    
def wolfram_alpha_distance(text):
    client = wolframalpha.Client(wolfram_api)
    result = client.query(text)
    answer = next(result.results).text
    print('Distance between this two nations is ' + answer)
    pikachu_talk('Distance between this two nations is ' + answer)
    
def translate_to_hindi(text):
    pikachu_talk_hindi(ts.translate_text(text, from_language='en', to_language='hi'))

def translate_to_german(text):
    pikachu_talk_german(ts.translate_text(text, from_language='en', to_language='de'))
    
def translate_to_japanese(text):
    pikachu_talk_japanese(ts.translate_text(text, from_language='en', to_language='ja'))

def get_news():
    news_url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=' + news_api_key
    news = requests.get(news_url).json()
    articles = news['articles']
    
    news_headlines = []
    for art in articles:
        news_headlines.append(art['title'])
    
    for i in range(5):
        print(news_headlines[i])
        pikachu_talk(news_headlines[i])
        
def get_weather():
    pikachu_talk('Sure, which city are you interested in?')
    weather_input = pikachu_listen()
    print(weather_input)
    
    weather_url = 'https://api.weatherbit.io/v2.0/current?city=' + weather_input + '&key=' + weather_api_key
    weather = requests.get(weather_url).json()
    temperature = weather['data'][0]['temp']
    description = weather['data'][0]['weather']['description']
    weather_result = 'The temperature in ' + weather_input + ' is ' + str(temperature) + ' degree and you can see ' + description
    print(weather_result)
    pikachu_talk(weather_result)
    
def wikipedia_info():
    pikachu_talk('let me know what i should search for you on wikipedia')
    wiki_input = pikachu_listen()
    print(wiki_input)
    wiki_result = wikipedia.summary(wiki_input,sentences=2)
    print(wiki_result)
    pikachu_talk(wiki_result)
    
# convert speech to text so we can use the text for the next step
def pikachu_listen():
    #create recognizer
    r = sr.Recognizer()
    # what we speak into the microphone should be our source
    with sr.Microphone() as source:
        # use the listen function so the recognizer can catch the source (our mic)
        audio = r.listen(source)
        text = ''

        try:
            text = r.recognize_google(audio)

        except sr.RequestError as re:
            print(re)

        except sr.UnknownValueError as uve:
            print(uve)

        except sr.WaitTimeoutError as wte:
            print(wte)

    text = text.lower()
    return text

# convert text to speech
def pikachu_talk(text):
    # create audio data
    file_name = 'audio_data.mp3'
    # convert text to speech
    tts = gTTS(text=text, lang='en')
    tts.save(file_name)
    # play file
    playsound.playsound(file_name)
    # remove file
    os.remove(file_name)
    
# convert text to speech in hindi
def pikachu_talk_hindi(text):
    # create audio data
    file_name = 'audio_data.mp3'
    # convert text to speech
    tts = gTTS(text=text, lang='hi')
    tts.save(file_name)
    # play file
    playsound.playsound(file_name)
    # remove file
    os.remove(file_name)

def pikachu_talk_german(text):
    # create audio data
    file_name = 'audio_data.mp3'
    # convert text to speech
    tts = gTTS(text=text, lang='de')
    tts.save(file_name)
    # play file
    playsound.playsound(file_name)
    # remove file
    os.remove(file_name)
    
def pikachu_talk_japanese(text):
    # create audio data
    file_name = 'audio_data.mp3'
    # convert text to speech
    tts = gTTS(text=text, lang='ja')
    tts.save(file_name)
    # play file
    playsound.playsound(file_name)
    # remove file
    os.remove(file_name)

# create a function which will give us back a reply based on input text
def pikachu_reply(text):
    # smalltalk - what is your name?
    if 'what' in text and 'name' in text:
        pikachu_talk('My name is Pikachu and I am your personal assistant')

    # smalltalk - why do you exist?
    elif 'why' in text and 'exist' in text:
        pikachu_talk('I was created  to work for you. I dont need a break and I will never ask for days off')
        
    # smalltalk - when do you sleep
    elif 'when' in text and 'sleep' in text:
        pikachu_talk('I never sleep. I was created to support you 24 hours')
        
    # smalltalk
    elif 'you' in text and 'single' in text:
        pikachu_talk('You are going in wrong direction, I am only your assistant')
        
    # smalltalk
    elif 'favorite' in text or 'favourite' in text and 'movie' in text:
        pikachu_talk('My favourite movie is The Chronicles of Narnia')
        
    # stalk price tata moters
    elif 'motors' in text:
        tatamotors = yf.Ticker('TATAMOTORS.NS')
        print(tatamotors.info['regularMarketDayHigh'])
        pikachu_talk('Current stock price of tata motors is' + str(tatamotors.info['regularMarketDayHigh']) + 'Indian Rupees')
        
     # stalk price tata power
    elif 'power' in text:
        tatapower = yf.Ticker('TATAPOWER.NS')
        print(tatapower.info['regularMarketDayHigh'])
        pikachu_talk('Current stock price of tata power is' + str(tatapower.info['regularMarketDayHigh']) + 'Indian Rupees')
        
     # stalk price tata steel
    elif 'steel' in text:
        tatasteel = yf.Ticker('TATASTEEL.NS')
        print(tatasteel.info['regularMarketDayHigh'])
        pikachu_talk('Current stock price of tata steel is' + str(tatasteel.info['regularMarketDayHigh']) + 'Indian Rupees')
        
     # stalk price adani enterprise
    elif 'enterprise' in text:
        adanienterprise = yf.Ticker('ADANIENT.NS')
        print(adanienterprise.info['regularMarketDayHigh'])
        pikachu_talk('Current stock price of adani enterprise is' + str(adanienterprise.info['regularMarketDayHigh']) + 'Indian Rupees')
        
     # stalk price adani ports
    elif 'ports' in text:
        adaniports = yf.Ticker('ADANIPORTS.NS')
        print(adaniports.info['regularMarketDayHigh'])
        pikachu_talk('Current stock price of adani ports is' + str(adaniports.info['regularMarketDayHigh']) + 'Indian Rupees')
        
     # stalk price hdfc bank
    elif 'hdfc' in text:
        hdfcbank = yf.Ticker('HDFCBANK.NS')
        print(hdfcbank.info['regularMarketDayHigh'])
        pikachu_talk('Current stock price of hdfc bank is' + str(hdfcbank.info['regularMarketDayHigh']) + 'Indian Rupees')
        
     # stalk price icici bank
    elif 'icici' in text:
        icicibank = yf.Ticker('ICICIBANK.NS')
        print(icicibank.info['regularMarketDayHigh'])
        pikachu_talk('Current stock price of icici bank is' + str(icicibank.info['regularMarketDayHigh']) + 'Indian Rupees')
        
    # wolfram alpha - capital of a country
    elif 'capital' in text and 'of' in text:
        wolfram_alpha_country_capital(text)
    
    # wolfram alpha - calculator
    elif '+' in text or '-' in text or 'x' in text or '/' in text or 'root' in text:
        wolfram_alpha_calculator(text)
        
    # wolfram alpha - president
    elif 'president' in text:
        wolfram_alpha_president(text)
        
    # wolfram alpha - distance
    elif 'distance' in text:
        wolfram_alpha_distance(text)
        
        
    # translate to english to hindi
    elif 'translate' in text and 'hindi' in text:
        pikachu_talk('sure, what you want to translate?')
        while True:
            text_to_translate = pikachu_listen()
            if text_to_translate != 'exit':
                translate_to_hindi(text_to_translate)
            else :
                pikachu_talk('the translator will be turned off.. what else can i do?')
                break
                
    # translate to english to german
    elif 'translate' in text and 'german' in text:
        pikachu_talk('sure, what you want to translate?')
        while True:
            text_to_translate = pikachu_listen()
            if text_to_translate != 'exit':
                translate_to_german(text_to_translate)
            else :
                pikachu_talk('the translator will be turned off.. what else can i do?')
                break
                
    # translate to english to japanese
    elif 'translate' in text and 'japanese' in text:
        pikachu_talk('sure, what you want to translate?')
        while True:
            text_to_translate = pikachu_listen()
            if text_to_translate != 'exit':
                translate_to_japanese(text_to_translate)
            else :
                pikachu_talk('the translator will be turned off.. what else can i do?')
                break
           
    # news section
    elif 'news' in text:
        pikachu_talk('here are top 5 news headlines')
        get_news()
        
    # weather section
    elif 'weather' in text:
        get_weather()
        
    #wikipedia
    elif 'wikipedia' in text:
        wikipedia_info()
        
    # smalltalk
    elif 'stop' in text:
        pikachu_talk('It was a pleasure to help you, I wish you a great day')

    
    else:
        pikachu_talk('Excuse me, I did not get that.')








def execute_assistant():
    # personalize name
    pikachu_talk('Hi, I am here to support you. Can you please tell me your name?')
    listen_name = pikachu_listen()
    pikachu_talk('Hello' + listen_name + 'how can i help you')
    
    while True:
        listen_pikachu = pikachu_listen()
        print(listen_pikachu)
        pikachu_reply(listen_pikachu)

        # if we use 'stop', we want to end the while loop and assistant should say goodye
        if 'stop' in listen_pikachu:
            break

#import tkinter as tk


#root = tk.Tk()
#root.title("Voice Assistant")

#Create text field
#text_field = tk.Text(root, height=10, width=50,)
#text_field.pack(pady=10)

 #Create record button
#record_button = tk.Button(root, text="Record", command=execute_assistant)
#record_button.pack(pady=5)



#root.mainloop()


#call function()
execute_assistant()