import time
from rich import print

def printOutput(cityName, data):
    if data == " City Not Found ":
        print("[bold green]Loading...[/bold green]")

        for i in range(1, 6):
            print("[bold green]" + "." * i + "[/bold green]")
            time.sleep(1)

        print("-------------------------------------")
        print("[bold deep_sky_blue1]The city you are looking for is not found[/bold deep_sky_blue1]")
        print("-------------------------------------")

    else:
        print("[bold green]Loading...[/bold green]")

        for i in range(1, 6):
            print("[bold green]" + "." * i + "[/bold green]")
            time.sleep(1)

        print("-------------------------------------")
        print("[bold deep_sky_blue1]Weather Forecast for " + cityName + " :[/bold deep_sky_blue1]")
        print("[bold green]Weather:[/bold green] " + "[bold blue]" + data["Weather"] + "[/bold blue]")
        print("[bold green]Temprature:[/bold green] " + "[bold blue]" + str(data["main"]["Temprature"]) + " " + chr(176) + "C" + "[/bold blue]")
        print("[bold green]Feels Like:[/bold green] " + "[bold blue]" + str(data["main"]["Feels Like"]) + " " + chr(176) + "C" + "[/bold blue]") 
        print("[bold green]Minimum Temprature:[/bold green] " + "[bold blue]" + str(data["main"]["Minimum Temprature"]) + " " + chr(176) + "C" + "[/bold blue]")
        print("[bold green]Maximum Temprature:[/bold green] " + "[bold blue]" + str(data["main"]["Maximum Temprature"]) + " " + chr(176) + "C" + "[/bold blue]")
        print("[bold green]Pressure:[/bold green] " + "[bold blue]" + str(data["main"]["Pressure"]) + " hPa" + "[/bold blue]")
        print("[bold green]Humidity:[/bold green] " + "[bold blue]" + str(data["main"]["Humidity"]) + " %" + "[/bold blue]")
        print("[bold green]Wind Speed:[/bold green] " + "[bold blue]" + str(data["wind"]["Speed"]) + " m/s" + "[/bold blue]")
        print("[bold green]Wind Degree:[/bold green] " + "[bold blue]" + str(data["wind"]["Degree"]) + " " + chr(176) + "[/bold blue]")
        print("[bold green]Sunrise:[/bold green] " + "[bold blue]" + data["sun"]["Sunrise"] + "[/bold blue]")
        print("[bold green]Sunset:[/bold green] " + "[bold blue]" + data["sun"]["Sunset"] + "[/bold blue]")
        print("-------------------------------------")
