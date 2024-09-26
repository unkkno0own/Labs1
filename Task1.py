def calculate_x(a, b):
  if a > b:
      return a * b - 3
  elif a == b:
      return 2
  elif a < b:
      return (a ** 3 + 1) / b

def main():
  try:
      a = float(input("Введіть значення a: "))
      b = float(input("Введіть значення b: "))

      if a > 0 and b > 0:
          print(f"Значення X: {calculate_x(a, b)}")
      elif 1 <= a <= 100 and 1 <= b <= 100:
          print(f"Значення X: {calculate_x(a, b)}")
      else:
          print("Значення повинні бути додатніми для варіантів 1-10 або від 1 до 100 для варіантів 10-20.")
  except ValueError:
      print("Введіть коректні числові значення!")

if __name__ == "__main__":
  main()
