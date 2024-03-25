from random import choice

food = {
    'healthy': ['rice', 'salad'],
    'unhealthy': ['pizza', 'burger', 'ssam']
}

print("What type of food are you feeling today?")
type = input()

print(choice(food[type]))