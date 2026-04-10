mark=int(input("Enter the Mark of the student find Grade:"));
result = "A" if 100>=mark>=76 else("B" if 75>=mark>=79 else ("C" if 60>=mark>=59 else"D"))
print(result);
