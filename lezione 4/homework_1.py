"""
Scrivi un programma che chieda all'utente la temperatura
in gradi Celsius e la converta in Fahrenheit,
secondo la seguente espressione:
F = (C x 9 / 5) + 32 """



def main():
    def celsius_to_fahrenheit(temp_celsius:float) -> float:
        return (temp_celsius*9/5) + 32
    
    input_str = input("What is the current temperature in Celsius?\n")
    
    try:
        temp_celsius = int(input_str)
    except ValueError as e:
        print(e)
    else:
        temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
        print(f"The current temperature in Fahrenheit is: {temp_fahrenheit}\n")
    finally:
        restart = input("Input Y to restart or any other key to close\n")
        if restart == "Y":
            main()
        
if __name__ == "__main__":
    main()