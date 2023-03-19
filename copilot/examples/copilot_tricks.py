#https://www.youtube.com/watch?v=S0zQoTkX_YQ

import requests
''' Get price of cryptocurrency from coingecko.com '''
def get_price(coin_id, currency):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=" + coin_id + "&vs_currencies=" + currency
    response = requests.get(url)
    data = response.json()
    return data[coin_id][currency]

print(get_price("bitcoin", "usd"))


# TODO ''' Get weather for a city without API key '''

''' Draw a house '''
def draw_a_house():
    import turtle
    t = turtle.Turtle()
    t.pensize(5)
    t.color("black", "red")
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(40, 100)
    t.pendown()
    t.color("black", "black")
    t.begin_fill()
    for i in range(3):
        t.forward(20)
        t.left(120)
    t.end_fill()

draw_a_house()

''' Draw a circle '''
def draw_a_circle():
    import turtle
    t = turtle.Turtle()
    t.pensize(5)
    t.color("black", "red")
    t.begin_fill()
    t.circle(100)
    t.end_fill()


draw_a_circle()