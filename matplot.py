import matplotlib.pyplot as plt

exams =["unit1","sem1","unit2","sem2"]
marks =[50,75,100,80]
plt.figure(figsize=(3, 4))
plt.plot(exams, marks, marker = 'o', color = 'green', markerfacecolor ='red', linestyle = "-.", linewidth = 7)
plt.xlabel("exams")
plt.ylabel("marks")
plt.title("marks obtained")
plt.xticks(rotation = 45)
plt.grid(True)