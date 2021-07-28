from django.http.response import HttpResponse
from django.shortcuts import render, redirect
import pymysql
from django.urls import reverse
import urllib.parse

# Create your views here.

def home(request):
    db = pymysql.connect(host="localhost",
                     user="sql6418117",
                     passwd="ixSFQAYA2h",
                     db="oggy")
    cur = db.cursor()
    cur.execute("select name from cities")
    results = cur.fetchall()
    cities = []
    for x in results:
        cities.append("".join(x))
    context = {
        'cities' : cities,
    }
    
    return render(request, 'index.html', context)

def restaurants(request):
    rest_city = request.GET.get('city')
    rest_name = request.GET.get('restaurant')
    db = pymysql.connect(host="localhost",
                     user="sql6418117",
                     passwd="ixSFQAYA2h",
                     db="oggy")
    cur = db.cursor()
    
    rest_name += "a"
    if rest_name != 'a':
        dec = {'city':rest_city, 'restaurant':rest_name}
        url = '{}?{}'.format(reverse('home-offer'), urllib.parse.urlencode(dec))
        return redirect(url)
    
    cur.execute("select name from cities")
    results = cur.fetchall()
    cities = []
    for x in results:
        cities.append("".join(x))
        
    cur.execute("select name, rating from restaurants_swiggy where city = %s", [rest_city])
    results = cur.fetchall()
    names = []
    ratings = []
    url = []
    for x in results:
        list_x = list(x)
        name = list_x[0]
        rating = list_x[1]
        if rating == "None":
            rating = "Not Enough Reviews"
        names.append(name)
        ratings.append(rating)
        url.append(urllib.parse.quote(name))
    zipped_data = zip(names, ratings, url)
        
    context = {
        'city' : rest_city,
        'name' : rest_name,
        'cities' : cities,
        'data' : zipped_data
    }
    return render(request, 'restaurants.html', context)
    

def login(request):
    return render(request, 'login.html')

def offer(request):
    def offer_checker(offer):
        if offer == ('None',):
            offer = 'No Offers'
        return offer
    rest_city = request.GET.get('city')
    rest_name = request.GET.get('restaurant')
    
    rest_name = rest_name[0:-1]
        
    db = pymysql.connect(host="localhost",
                     user="sql6418117",
                     passwd="ixSFQAYA2h",
                     db="oggy")
    cur = db.cursor()
    def converter(offer):
        try:
            if offer != None or ('(None,)') or "" or " ":
                offer = list(offer)
                offer = offer[0]
                return offer
        except:
            return offer
    def swiggy_converter(offer):
        try:
            if offer != None or ('(None,)'):
                offer = offer.split(',')
                return offer
        except:
            return offer
    cur.execute('select offers from restaurants_dineout where city = %s and name = %s', [rest_city, rest_name])
    offer_dineout = cur.fetchone()
    cur.execute('select offers from restaurants_swiggy where city = %s and name = %s', [rest_city, rest_name])
    offer_swiggy = cur.fetchone()
    cur.execute('select offers from restaurants_eazydiner where city = %s and name = %s', [rest_city, rest_name])
    offer_eazydiner = cur.fetchone()
    offer_dineout = converter(offer_dineout)
    offer_swiggy = converter(offer_swiggy)
    offer_eazydiner = converter(offer_eazydiner)
    offer_swiggy = swiggy_converter(offer_swiggy)
    offer_dineout = offer_checker(offer_dineout)
    offer_swiggy = offer_checker(offer_swiggy)
    offer_eazydiner = offer_checker(offer_eazydiner)
    
    
    cur.execute('select rating from restaurants_dineout where city = %s and name = %s', [rest_city, rest_name])
    rating = cur.fetchone()
    try:
        if rating != None or ('(None),'):
            rating = list(rating)
            rating = rating[0]
    except:
        rating = rating
    context = {
        'city' : rest_city,
        'name' : rest_name,
        'rating' : rating,
        'offer_dineout' : offer_dineout,
        'offer_swiggy' : offer_swiggy,
        'offer_eazydiner' : offer_eazydiner
    }
    return render(request, 'offer.html', context)

def south(request):
    db = pymysql.connect(host="localhost",
                     user="sql6418117",
                     passwd="ixSFQAYA2h",
                     db="oggy")
    cur = db.cursor()
    cur.execute("select name, rating from restaurants_swiggy where cuisine REGEXP 'South'")
    names = cur.fetchall()
    swiggy_south_names = []
    swiggy_south_rating = []
    swiggy_south_encoded_url = []
    for x in names:
        list_x = list(x)
        name = list_x[0]
        rating = list_x[1]
        if rating == "None":
            rating = "Not Enough Reviews"
        swiggy_south_names.append(name)
        swiggy_south_rating.append(rating)
        swiggy_south_encoded_url.append(urllib.parse.quote(name))
    zipped_data = zip(swiggy_south_names, swiggy_south_rating, swiggy_south_encoded_url)
    
    context = {
        'data' : zipped_data
    }
    return render(request, 'south.html', context)
    
def pizza(request):
    db = pymysql.connect(host="localhost",
                     user="sql6418117",
                     passwd="ixSFQAYA2h",
                     db="oggy")
    cur = db.cursor()
    cur.execute("select name, rating from restaurants_swiggy where cuisine REGEXP 'Pizza'")
    names = cur.fetchall()
    swiggy_south_names = []
    swiggy_south_rating = []
    swiggy_south_encoded_url = []
    for x in names:
        list_x = list(x)
        name = list_x[0]
        rating = list_x[1]
        if rating == "None":
            rating = "Not Enough Reviews"
        swiggy_south_names.append(name)
        swiggy_south_rating.append(rating)
        swiggy_south_encoded_url.append(urllib.parse.quote(name))
    zipped_data = zip(swiggy_south_names, swiggy_south_rating, swiggy_south_encoded_url)
    
    context = {
        'data' : zipped_data
    }
    return render(request, 'pizza.html', context)
    
def burger(request):
    db = pymysql.connect(host="localhost",
                     user="sql6418117",
                     passwd="ixSFQAYA2h",
                     db="oggy")
    cur = db.cursor()
    cur.execute("select name, rating from restaurants_swiggy where name REGEXP 'Burger'")
    names = cur.fetchall()
    swiggy_south_names = []
    swiggy_south_rating = []
    swiggy_south_encoded_url = []
    for x in names:
        list_x = list(x)
        name = list_x[0]
        rating = list_x[1]
        if rating == "None":
            rating = "Not Enough Reviews"
        swiggy_south_names.append(name)
        swiggy_south_rating.append(rating)
        swiggy_south_encoded_url.append(urllib.parse.quote(name))
    zipped_data = zip(swiggy_south_names, swiggy_south_rating, swiggy_south_encoded_url)
    
    context = {
        'data' : zipped_data
    }
    return render(request, 'burger.html', context)

def dessert(request):
    db = pymysql.connect(host="localhost",
                     user="sql6418117",
                     passwd="ixSFQAYA2h",
                     db="oggy")
    cur = db.cursor()
    cur.execute("select name, rating from restaurants_swiggy where cuisine REGEXP 'Dessert'")
    names = cur.fetchall()
    swiggy_south_names = []
    swiggy_south_rating = []
    swiggy_south_encoded_url = []
    for x in names:
        list_x = list(x)
        name = list_x[0]
        rating = list_x[1]
        if rating == "None":
            rating = "Not Enough Reviews"
        swiggy_south_names.append(name)
        swiggy_south_rating.append(rating)
        swiggy_south_encoded_url.append(urllib.parse.quote(name))
    zipped_data = zip(swiggy_south_names, swiggy_south_rating, swiggy_south_encoded_url)
    
    context = {
        'data' : zipped_data
    }
    return render(request, 'dessert.html', context)
    
#filters

def price(request):
    db = pymysql.connect(host="localhost",
                     user="sql6418117",
                     passwd="ixSFQAYA2h",
                     db="oggy")
    cur = db.cursor()
    cur.execute('select name from restaurants_dineout where city = %s and name = %s')
    return render(request, 'price.html')

def rating(request):
    return render(request, 'rating.html')

def cuisine(request):
    return render(request, 'cuisine.html')

