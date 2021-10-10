import json

file = open('RF_9.txt', 'r', encoding="utf8")
regions = []
nomer = 0
rusia_space = 17130000
rusia_count = 144100000
detected = False
difference = {}
parameters = (file.readline().strip('\n').split(" "))
for i in range(6):
    param = parameters[i].split("_")
    if param[0] == "Код":
        parameters[i] = "Код"
        nomer = param[1]

    parameters[i] = parameters[i].replace("_", " ")
while True:
    line = file.readline().strip("\n")
    if not line:
        break
    data = line.split(" ")
    region = {parameters[0]: data[0].replace("_", " "), parameters[1]: data[1].replace("_", " "),
              parameters[2]: data[2].replace("_", " "),
              parameters[3]: data[3].replace("_", " "),
              parameters[4]: data[4].replace("_", " "), parameters[5]: data[5].replace("_", " "),
              parameters[6]: data[6].replace("_", " ")}
    normalForm = {"Название": region.get("Название"), "Площадь": int(region.get("Площадь")),
                  "Население": int(region.get("Население")), "Округ": region.get("Округ"),
                  "Адм. центр/столица": region.get("Адм. центр/столица"), "Код ОКАТО": int(region.get("Код")),
                  "Часовой пояс": region.get("Часовой пояс"),
                  "Площадь(процент)": round(int(region.get("Площадь")) * 100 / rusia_space, 4),
                  "Население(процент)": round(int(region.get("Население")) * 100 / rusia_count, 4),
                  "Плотность": round(int(region.get("Население")) / int(region.get("Площадь")), 4)}
    regions.append(normalForm)
    if normalForm.get("Название") != "Владимирская область":
        if str(normalForm.get("Часовой пояс")) == "МСК":
            difference[normalForm.get("Название")] = 0
        else:
            difference[normalForm.get("Название")] = int(normalForm.get("Часовой пояс").replace("МСК", ""))
    if str(normalForm.get("Код ОКАТО")) == str(nomer):
        detected = True
        print("Субъект " + normalForm.get("Название") + " входящий в " + str(
            normalForm.get("Округ")) + " занимает площадь " + str(int(
            normalForm.get("Площадь")) / 1000) + " тыс. кв. км., на которой проживает " + str(int(
            normalForm.get("Население")) / 1000000) + " млн. чел.. Адм. центром является город " + normalForm.get(
            "Адм. центр/столица") + " . Код Окато - " + str(int(
            normalForm.get("Код ОКАТО"))) + " . Часовой пояс - " + normalForm.get("Часовой пояс"))
if detected == False:
    print("Субьекта с указанным ОКАТО не найдено")
print("Субъект " + normalForm.get("Название") + " входящий в " + str(
    normalForm.get("Округ")) + " занимает площадь " + str(int(
    normalForm.get("Площадь")) / 1000) + " тыс. кв. км., на которой проживает " + str(int(
    normalForm.get("Население")) / 1000000) + " млн. чел.. Адм. центром является город " + normalForm.get(
    "Адм. центр/столица") + " . Код Окато - " + str(int(
    normalForm.get("Код ОКАТО"))) + " . Часовой пояс - " + normalForm.get("Часовой пояс"))

dictionary = {"РФ": regions}
file.close()
print("Разница часового пояса в других регионах относительно Владимирской Области")
print(difference)
with open("new.json", "w", encoding="utf8") as file:
    json.dump(dictionary, file, indent=4, ensure_ascii=False)
