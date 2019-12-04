#!/usr/bin/env python
# coding: utf-8

# In[38]:


import nltk
import numpy as np
import random
import string
import webbrowser
import time
import requests
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn


def get_joke():
  url = "http://api.icndb.com/jokes/random"
  resp = requests.get(url)
  resp.encoding = "utf-8"
  data = resp.json()
  print(data["value"]["joke"])



# In[39]:


f=open('chatbot.txt','r',errors = 'ignore')


# In[40]:


raw=f.read()
raw=raw.lower()
nltk.download('punkt')
nltk.download('wordnet') 
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)


# In[41]:


lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
	return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
	return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# In[42]:


#LemNormalize(raw)


# In[45]:


GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey")
GREETING_RESPONSES = ["hi", "hey", "how're you", "hi there", "hello", "I am glad you are talking to me!"]
COMMAND_INPUTS = ("jokes","youtube")
COMMAND_OUTPUTS = ["on it!...","hang on a minute..."]
def greeting(sentence):
	for word in sentence.split():
		if word.lower() in GREETING_INPUTS:
			return GREETING_RESPONSES[random.randint(0,5)]
def command(sentence,flag1):
	for word in sentence.split():
		if word.lower() in COMMAND_INPUTS:
			if (word in COMMAND_INPUTS[1]):
				if (flag1 == False):
					print ("SUJI: ",COMMAND_OUTPUTS[random.randint(0,1)])
					webbrowser.get().open("https://www.youtube.com/watch?v=G4I6PhHbH7o&list=RDG4I6PhHbH7o&start_radio=1")
					flag1 = True
					time.sleep(5)
			if (word in COMMAND_INPUTS[0]):
				if (flag1 == False):
					print ("SUJI: ",COMMAND_OUTPUTS[random.randint(0,1)])
					get_joke()
					flag1 = True
					#time.sleep(5)
			return COMMAND_OUTPUTS[random.randint(0,1)]


# In[46]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[47]:


def response(user_response):
	robo_response=''
	sent_tokens.append(user_response)
	TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
	tfidf = TfidfVec.fit_transform(sent_tokens)
	vals = cosine_similarity(tfidf[-1], tfidf)
	#byprint (vals)
	idx=vals.argsort()[0][-2]
	flat = vals.flatten()
	flat.sort()
	req_tfidf = flat[-2]
	if(req_tfidf==0):
		#if (flag1 !=False):
		robo_response=robo_response+"I don't know this. Sorry!"
		return robo_response
	else:
		robo_response = robo_response+sent_tokens[idx]
		return robo_response


# In[48]:


flag=True
flag1 = True
print("SUJI: My name is Suji. I will answer your queries. Meow! You can also command me to carry out a few instructions!")
while(flag==True):
	print ("YOU: ",end="")
	user_response = input()
	user_response=user_response.lower()
	if (user_response=='bye' or user_response=='goodbye' or user_response=='goodnight'):
		flag = False
		print ("SUJI: Bye...take care!")
	else:
		if(user_response=='thanks' or user_response=='thank you'):
			print("SUJI: You are welcome..Do you wanna ask another question?")
			user_response = input()
			user_response = user_response.lower()
			if(user_response=='no'):
				flag = False
				print ("SUJI: Bye...Hope I could help!")
		else:
			if (greeting(user_response)!=None):
				print("SUJI: "+greeting(user_response))
			elif (command(user_response,flag1)!=None):
				#print ("Meow")
				flag1 = False
				command(user_response,flag1)
			else:
				print("SUJI: ",end="")
				print(response(user_response))
				sent_tokens.remove(user_response)


# In[ ]:




