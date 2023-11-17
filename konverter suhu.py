def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius_to_kelvin(celsius)
    return kelvin

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    fahrenheit = celsius_to_fahrenheit(celsius)
    return fahrenheit

# Pilihan pengguna untuk memilih konversi
print("Pilih konversi:")
print("1. Fahrenheit ke Celsius")
print("2. Celsius ke Fahrenheit")
print("3. Celsius ke Kelvin")
print("4. Kelvin ke Celsius")
print("5. Fahrenheit ke Kelvin")
print("6. Kelvin ke Fahrenheit")

choice = int(input("Masukkan pilihan (1-6): "))

if choice == 1:
    fahrenheit_input = float(input("Masukkan suhu dalam Fahrenheit: "))
    celsius_output = fahrenheit_to_celsius(fahrenheit_input)
    print(f"{fahrenheit_input} Fahrenheit sama dengan {celsius_output:.2f} Celsius.")
elif choice == 2:
    celsius_input = float(input("Masukkan suhu dalam Celsius: "))
    fahrenheit_output = celsius_to_fahrenheit(celsius_input)
    print(f"{celsius_input} Celsius sama dengan {fahrenheit_output:.2f} Fahrenheit.")
elif choice == 3:
    celsius_input = float(input("Masukkan suhu dalam Celsius: "))
    kelvin_output = celsius_to_kelvin(celsius_input)
    print(f"{celsius_input} Celsius sama dengan {kelvin_output:.2f} Kelvin.")
elif choice == 4:
    kelvin_input = float(input("Masukkan suhu dalam Kelvin: "))
    celsius_output = kelvin_to_celsius(kelvin_input)
    print(f"{kelvin_input} Kelvin sama dengan {celsius_output:.2f} Celsius.")
elif choice == 5:
    fahrenheit_input = float(input("Masukkan suhu dalam Fahrenheit: "))
    kelvin_output = fahrenheit_to_kelvin(fahrenheit_input)
    print(f"{fahrenheit_input} Fahrenheit sama dengan {kelvin_output:.2f} Kelvin.")
elif choice == 6:
    kelvin_input = float(input("Masukkan suhu dalam Kelvin: "))
    fahrenheit_output = kelvin_to_fahrenheit(kelvin_input)
    print(f"{kelvin_input} Kelvin sama dengan {fahrenheit_output:.2f} Fahrenheit.")
else:
    print("Pilihan tidak valid. Harap masukkan angka antara 1 dan 6.")