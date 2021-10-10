import json

file = open('RF_9.txt', 'r', encoding="utf8")  # open file
regions = []  # create array
nomer = 10  # укажите номер ОКАТО
rusia_space = 17130000  # rashka square
rusia_count = 144100000  # rashka population
detected = False  # is our OKATO detected
difference = {}  # dick of difference
parameters = (file.readline().strip('\n').split(" "))  # abstract parameters


# func for printing info
def print_info():
    print("Субъект " + normalForm.get("Название") + " входящий в " + str(
        normalForm.get("Округ")) + " занимает площадь " + str(int(
        normalForm.get("Площадь")) / 1000) + " тыс. кв. км., на которой проживает " + str(int(
        normalForm.get("Население")) / 1000000) + " млн. чел.. Адм. центром является город " + normalForm.get(
        "Адм. центр/столица") + " . Код Окато - " + str(int(
        normalForm.get("Код ОКАТО"))) + " . Часовой пояс - " + normalForm.get("Часовой пояс"))


while True:
    line = file.readline().strip("\n")  # read line
    if not line:
        break
    data = line.split(" ")  # get data
    # create abstract
    region = {parameters[0].replace("_", " "): data[0].replace("_", " "),
              parameters[1].replace("_", " "): data[1].replace("_", " "),
              parameters[2].replace("_", " "): data[2].replace("_", " "),
              parameters[3].replace("_", " "): data[3].replace("_", " "),
              parameters[4].replace("_", " "): data[4].replace("_", " "),
              parameters[5].replace("_", " "): data[5].replace("_", " "),
              parameters[6].replace("_", " "): data[6].replace("_", " ")}
    # pull in correct form
    normalForm = {"Название": region.get("Название"), "Площадь": int(region.get("Площадь")),
                  "Население": int(region.get("Население")), "Округ": region.get("Округ"),
                  "Адм. центр/столица": region.get("Адм. центр/столица"), "Код ОКАТО": region.get("Код ОКАТО"),
                  "Часовой пояс": region.get("Часовой пояс"),
                  "Площадь(процент)": round(int(region.get("Площадь")) * 100 / rusia_space, 4),
                  "Население(процент)": round(int(region.get("Население")) * 100 / rusia_count, 4),
                  "Плотность": round(int(region.get("Население")) / int(region.get("Площадь")), 4)}
    # add to array
    regions.append(normalForm)
    # add to dick of difference
    if normalForm.get("Название") != "Владимирская область":
        if str(normalForm.get("Часовой пояс")) == "МСК":
            difference[normalForm.get("Название")] = 0
        else:
            difference[normalForm.get("Название")] = int(normalForm.get("Часовой пояс").replace("МСК", ""))
    # check for our OKATO
    if str(normalForm.get("Код ОКАТО")) == str(nomer):
        detected = True
        print_info()
# if our OKATO isn't detected
if not detected:
    print("Субьекта с указанным ОКАТО не найдено")
print_info()  # info about last
dictionary = {"РФ": regions}  # add array to dick
file.close()  # close file
print("Разница часового пояса в других регионах относительно Владимирской Области")
print(difference)  # print difference with Vladimirskaya Oblast
# save to json
with open("new.json", "w", encoding="utf8") as file:
    json.dump(dictionary, file, indent=4, ensure_ascii=False)
