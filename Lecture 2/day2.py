faiz = 1.59
vade = 36
krediAdi = "İhtiyaç Kredisi"

print(vade + 12)

vade2 = "24"

# print(vade2 + 12)  # Error: can only concatenate str to str
# print(int(krediAdi)) #Error: invalid literal for int()

print(int(vade2)+12)

print(type(faiz)) # float 
faiz = str(faiz)
print(type(faiz)) # string

vadeInput = input("Lütfen istediğiniz vade miktarını giriniz: ")
print(vadeInput)
print(type(vadeInput)) # Inputs are treated as strings by the program.

# print(vadeInput + 12)  # Error: can only concatenate str to str
print(int(vadeInput)+12)

# If u want to take spesific inputs you should given a more information about input to program

vadeInputInt = int(input("Lütfen istediğiniz vade sayısını giriniz: "))
vadeInputInt += 20
print(vadeInputInt)

# ---------- String Interpolation ---------- #

# print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + vadeInputInt) #TypeError: can only concatenate str (not "int") to str
print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vadeInputInt)) # using str keyword
# or 
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vadeInputInt)) # using format keyword
# or 
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeInputInt}" ) # using f-strig




isim = input("İsminizi giriniz: ")
metin = "Merhaba {name}".format(name=isim)
print(metin)

# f-string
metin2 = f"Hoşgeldiniz {isim}, {2+2}=4"
print(metin2)

# lists, loops, functions

krediler = ["İhtiyaç kredisi", "Taşıt kredisi", "Konut kredisi"]
print(type(krediler))
print(krediler)
print(krediler[0])
print(len(krediler))

liste = ["Selam", 12 , 12.1]
print(liste)

krediler.append("Özel kredi") # we use append for when we need to add something to list
print(krediler)
krediler.append("X kredisi")
print(krediler)
krediler.pop(0) # we use pop for delete something in our list
print(krediler)
krediler.append("Taşıt kredisi") #add "Taşıt kredisi" to last
print(krediler) 
krediler.remove("Taşıt kredisi") #remove first item that name is "Taşıt kredisi"
print(krediler)


