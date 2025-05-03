import time

Name=input("enter you name :").strip()
gender =input("enter you gender (male/female/other)")
age=int(input("enter you age :"))
city=input("enter the city u live :").strip()
symptoms=input("Main symptom (choose from: fever, cough, fatigue, headache, chest pain, breathlessness)")
temp=int(input("enter yor body temperature"))
sick=int(input("how many days u felt unwell"))
smoking=input("do you smoke ? (yes/no)")
sleep_time=int(input("how many hours do u sleep"))
mood=input("chosse one Mood (choose from: calm, anxious, sad, irritable)")
condition = input("do you have Pre-existing conditions (yes/no)")
risk_score=0
if(temp >= 102 or sick > 3):
  risk_score=+3
 
if (age >= 60 and "fever" in (symptoms)):
  risk_score += 2
if(sick >= 5 and "cough" in (symptoms)):
  risk_score += 2
if(age>30 and "fatigue" in (symptoms)):
  risk_score +=2
if("chest pain" in symptoms):
  risk_score += 3
if("Breathlessness" in symptoms):
  risk_score += 4
if(smoking == "yes"):
  risk_score += 2
if (sleep_time < 6):
  risk_score += 1
if(mood == "anxious" or "sad" or "irritable"):
  risk_score += 1
if(condition == "yes"):
  risk_score += 2
if (temp > 100 and "headache" in symptoms):
  risk_score += 2
print(risk_score)