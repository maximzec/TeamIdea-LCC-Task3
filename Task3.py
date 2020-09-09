import requests
import xml.dom.minidom


#делаем запрос к ЦБ РФ и получаем XML
request = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
xmlStr = request.text
dom = xml.dom.minidom.parseString(xmlStr)
#Находим все теги Valute , ищем нужное значение и получаем результат
valutes = dom.getElementsByTagName("Valute")
for valute in valutes:
    id = valute.getAttribute("ID")
    if id == 'R01625':
        value = valute.getElementsByTagName("Value")[0]
        print(value.firstChild.data)
