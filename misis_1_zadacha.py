import csv
with open ('C:\Users\sulej\Downloads\students.csv',encoding='utf8') as file:
    reader = csv.reader(file,delimeter=',')
    answer = list(reader)[1:]
    for id, name,titleProject_id,level,score in answer:
        if 'Хадаров Владимир' in name:
            print(f"Ты получил: {score}, за проект - {titleProject_id}")
            
