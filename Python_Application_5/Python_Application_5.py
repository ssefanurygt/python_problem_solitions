# boş bir to do listesi oluşturalım 


to_do_list=[];
def add_task(to_do_list):
    task="yapilacak görevi giriniz";
    add_task.append(task)
    print("görev tamamlandı")


def show_task(to_do_list):
    print("yapilacak görevler:")
    for task in  to_do_list:
        print("-" + task)


def delete_task(to_do_list):
    task=input("silinecek gorevi secin")
    if task in to_do_list:
        to_do_list.remove(task)
        print("görev basariyla tamamlandı")
    else:
        print("görev bulunamadı")
        
while True:
    print("/n To-Do list Aplication")
    print("1. görev ekle")
    print("2. görev goster")
    print("3. görev sil")
    print("4. cikis")
    print("cikis")
    
    choice=input("seciminiz (1/2/3/4): ")
    
    if choice=="1":
        add_task(to_do_list)
    elif choice=="2":
        show_task(to_do_list)
    elif choice=="3":
        delete_task
    elif choice=="4":
        print("cikis ")
        break
    else:
        print("gecersiz secim yeniden deneyin")
   
        
        
    



