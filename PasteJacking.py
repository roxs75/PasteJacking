from jinja2 import Environment, FileSystemLoader
from flask import Flask, request, Response
import colored

# Define banner colors using named colors
banner_colors = [
    colored.fg("magenta") + colored.attr("bold"), 
    colored.fg("cyan") + colored.attr("bold"),
    colored.fg("yellow") + colored.attr("bold"),
    colored.fg("red") + colored.attr("bold"),  # Changed from hex to 'red'
    colored.fg("white") + colored.attr("bold"),
    colored.fg("green") + colored.attr("bold"),  # Changed from hex to 'green'
    colored.fg("white") + colored.bg("black") + colored.attr("bold"),
    colored.fg("green") + colored.bg("white") + colored.attr("bold")  # Changed from hex to 'green'
]

magenta = banner_colors[0]
cyan = banner_colors[1]
yellow = banner_colors[2]
red = banner_colors[3]
white = banner_colors[4]
green = banner_colors[5]
bold = banner_colors[6]
res = colored.attr('reset')

# Create banner
banner = f'''
{cyan}
          |\___/|                      \\
         =) ^Y^ (=   |\_/|              ||    '
          \  ^  /    )a a '._.-""""-.  //
           )=*=(    =\T_= /    ~  ~  \//
          /     \     `"`\   ~   / ~  /
          |     |         |~   \ |  ~/
         /| | | |\         \  ~/- \ ~\\
{res}
        {green}{bold}╔═╗┌─┐┌─┐┌┬┐┌─┐ ╦┌─┐┌─┐┬┌─┌─┐┬─┐{res}
        {green}{bold}╠═╝├─┤└─┐ │ ├┤  ║├─┤│  ├┴┐├┤ ├┬┘{res}
        {green}{bold}╩  ┴ ┴└─┘ ┴ └─┘╚╝┴ ┴└─┘┴ ┴└─┘┴└─{res}
                                    {white}[{red}=>{white}] {yellow}Created by{red}:{red}{bold} AbdulRahman Mohammed {res}{white}({cyan}De3vil{white}) {white}[{red}<={white}]
                                  \___________________________________________________/
'''

print(banner)

# Set payload input
globalvar = input(f"{red}set payload {white}: ")

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def index():
    global globalvar
    payload = request.args.get('payload', globalvar)
    
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('index.html')
    rendered_template = template.render(payload=payload)

    return Response(rendered_template, content_type='text/html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
