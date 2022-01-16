from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run()

@app.route("/")
def age():
    ages = input("Please enter your age.")
    if ages < 25:
        return f"{ages}, Thats still young"
    elif (ages >= 25) & (ages <= 50):
        return f"{ages}, you are in your prime."
    elif (ages >= 50) & (ages <= 120):
        return f"{ages}! you old!"
    else : return print("thats not a valid input!")

