fruts = ['яблоки','груши','персики']
vegetables = ['помидоры','огурцы','перец болгарский']
run = True
print("Добро пожаловать в наш каталог! Если Вы хотите ознакомиться с функционалом введите команду\"помощь\"")
while run:
   
    function = str(input())
   
    if function == "фрукты":
        print('Фрукты:',", ".join(fruts))
        next_step = str(input("если хотите выйти введите \"назад\", если хотите добавить позицию - введите название позиции, если вы хотите удалить позицию введите \"удалить\"\n"))
       
        if next_step !="назад":
            new_position = str(next_step)
            print(F"Вы добавили {new_position} в каталог \"фрукты\"")
            fruts.append(new_position)
       
        if next_step == "удалить":
            delite = str(input("Введите название позиции предлагаемой к удалению: "))
            vegetables.remove(delite)
   
    if function == "овощи":
        print('Овощи:',", ".join(vegetables))
        next_step = str(input("если хотите выйти введите \"назад\", если хотите добавить позицию - введите название позиции, если вы хотите удалить позицию введите \"удалить\"\n"))
       
        if next_step != "назад" and next_step != "удалить":
            new_position = str(next_step)
            print(F"Вы добавили {new_position} в каталог \"овощи\"")
            vegetables.append(new_position)
        
        if next_step == "удалить":
            delite = str(input("Введите название позиции предлагаемой к удалению: "))
            vegetables.remove(delite)
    
    if function == "помощь":   #вызывает справку-помощник
        print(F"Вы вызвали аннотацию ко всем функциям \nфрукты - вызывает каталог фруктов представленный в нашем магазине \nовощи - вызывает каталог овощей представленный в нашем магазине\nвыйти - закрывает приложение \nсортировать - сортирует список")
    
    if function == "сортировать":
        print("Выберите категорию и как Вы хотите сортировать:\nЕсли Вы хотите сортировать по алфавиту введите\"1\"\nЕсли по алфавиту (убывание) введите \"2\"")
        category_sort = str(input('Введите категорию которую хотите сортировать '))
        
        if category_sort == 'фрукты':
            category_sort = fruts
        
        elif category_sort == "овощи":
            category_sort = vegetables
        type_sort = int(input('Введите тип сортировки '))
        
        if type_sort == 1:
            category_sort.sort()
            print("Выполнено!")

        if type_sort == 2:
            category_sort.sort(reverse=True)
            print("Выполнено")

    if function == "выйти":
        print("До свидания!")
        run= False
