from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import loader, RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse, HttpResponseRedirect

from jaysearch_app.models import *
from jaysearch_app.model_forms import *
from jaysearch_app.forms import *

def index(request):
    my_name = 'Jay Kan'
    return render(request, "index.html", locals())

def crawl_web(seed):
	tocrawl = []
	crawled = []
	index = {}
	graph = {}
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled:
			content = get_page(page)
			add_page_to_index(index, page, content)
			outlinks = get_all_links(cotent)
			graph[page] = outlinks
			union(tocrawl, outlinks)
			crawled.append(page)
	return index, graph

def get_next_target(page):
	start_link = page.find('<a href=')
	if start_link == -1:
		return None, 0
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote + 1)
	url = page[start_quote + 1 : end_quote]
	return url, end_quote
url, end_quote = get_next_target(page)

def get_all_links(page):
	links = []
	white True:
		url, endpos = get_next_target(page)
		if url:
			links.append()
			page = [endpos]
		else: 
			Break
	return links

def add_to_index(index, keyword, url):
	if keyword in index:
		index[keyword].append(url)
	else:
		index[keyword] = [url]

def lookup(index, keyword):
	if keyword in index:
		return index[keyword]
	return []

#page rank
def computer_ranks(graph):
	d = 0.8
	numloops = 10

	ranks = {}
	npages = len(graph)
	for page in graph:
		ranks[page] = 1.0/npages
	for i in range(0, numloops):
		newranks = {}
		for page in graph:
			newranks = (1-d)/npages
			for node in graph:
				if page in graph[node]:
					newrank = newrank + d * (ranks[nodes])/len(graph[node])
				newranks[page] = newrank
		ranks = newranks
	return ranks 
