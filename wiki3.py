import requests
from bs4 import BeautifulSoup
import datetime
from info_urls import *
requests.packages.urllib3.disable_warnings()


def get_wiki_data(service=1,unp=""):
    unp=unp
    if int(service) == 1:
        file_name = "IaaS"
        url_ = URL_IAAS
        num_phone_col=4
        num_mail_col=5
        num_org_name=1
        i=1
    if int(service) == 2:
        url_ = URL_IAAS_62
        file_name = "IaaS_62"
        num_phone_col=4
        num_mail_col=5
        num_org_name=1
        i=1
    if int(service) == 3:
        url_ = URL_COLO
        file_name = "Colocation"
        num_phone_col=5
        num_mail_col=6
        num_org_name=1
        i=1
    if int(service) == 4:
        url_ = URL_COLO_62 
        file_name = "Colocation_62"
        num_phone_col=5
        num_mail_col=6
        num_org_name=1
        i=1
    if int(service) == 5:
        url_ = URL_SSS
        file_name = "S3"
        num_phone_col=4
        num_mail_col=5
        num_org_name=1
        i=0
    if int(service) == 6:
        url_ = URL_BAAS
        file_name = "BaaS"
        num_phone_col=4
        num_mail_col=5
        num_org_name=1
        i=1
    if int(service) == 7:
        url_ = URL_BAAS_62
        file_name = "BaaS_62"
        num_phone_col=4
        num_mail_col=5
        num_org_name=1
        i=1
    if int(service) == 8:
        url_ = URL_CC
        file_name = "CloudConnect"
        num_phone_col=4
        num_mail_col=5
        num_org_name=1
        i=1
    if int(service) == 9:
        url_ = URL_VMAAS
        file_name = "VMaaS"
        num_phone_col=4
        num_mail_col=5
        num_org_name=1
        i=0
    if int(service) == 10:
        url_ = URL_WAF
        file_name = "WAF"
        num_phone_col=4
        num_mail_col=5
        num_org_name=1
        i=0
    if int(service) == 11:
        url_ = URL_SIEM
        file_name = "SIEMaaS"
        num_phone_col=4
        num_mail_col=5
        num_org_name=1
        i=0
    if int(service) == 12:
        url_ = URL_DRAAS
        file_name = "DRaaS"
        num_phone_col=4
        num_mail_col=5
        num_org_name=1
        i=1


    try:
        respons = requests.get(url_,verify=False)
    except:
        print("\n\n\n\nне удалось установить соедение с wiki\n\n\n\n")
        return
    src = respons.text
    soup = BeautifulSoup(src, "lxml")

    #получаю таблицу со страницы
    find_tbody = soup.find("tbody")
    resault = ''
    resault2= ''
    id2=1
    id=1
 

    def calculator(num_phone_col,i,unp):
        resault=''
        id=1 #переенная для подсчета кол-ва эмейлов
        find_all_tr_list = find_tbody.find_all("tr")
        while i < (len(find_all_tr_list)):
            j=0
            find_all_td_list = find_all_tr_list[i].find_all("td")
            find_all_td_unp = find_all_td_list[2]
            #если в консоли ввели УНП и оно содержится в ячейке унп, то получаем информацию по email и номеру для данного УНП/ИНН
            if unp in find_all_td_unp.text:

                find_all_p_phone_list = find_all_td_list[num_phone_col].find_all("p")
                if len(find_all_p_phone_list)==0:
                    print(f"Проверяю сколько в текущей строке и текущем столбце тегов P если :{len(find_all_p_phone_list)}=0, иду дальше и проверяю есть ли тег DIV")
                    j=0
                    find_all_div_phone_list = find_all_td_list[num_phone_col].find_all("div")
                    print(f"     Проверяю, сколько получено {len(find_all_div_phone_list)}, если НЕ 0 - собираю информацию ")
                    if len(find_all_div_phone_list)!=0 :
                        # print("find_all_div_phone_list",find_all_div_phone_list)
                        while j < len(find_all_div_phone_list):
                            print("     Беру телефон из DIV вложенного в TD",curr_phone)
                            curr_phone = find_all_div_phone_list[j]
                            if len(curr_phone.text)>1:
                                resault += curr_phone.text+"\n"
                            id+=1
                            j+=1
                    #в противном случае получено 0 
                    else:
                        print(f"        в строке {i} нет тегов P и DIV, беру информацию из TD")
                        if len(find_all_td_list[num_phone_col].text)>2:
                            print("         беру текстовое поля из тега td:",find_all_td_list[num_phone_col].text)
                            resault+=find_all_td_list[num_phone_col].text+"\n"
                            id+=1
                else:
                    while j < len(find_all_p_phone_list):
                        curr_phone = find_all_p_phone_list[j]
                        # print("curr_phone=",curr_phone.text)
                        if len(curr_phone.text)>1:
                            resault += curr_phone.text+"\n"
                            id+=1    
                        j+=1
            i+=1
        id=id-1
        if len(resault)==0:
            resault+=f"По указанном УНП \"{unp}\" для выбраной услуги {file_name} - информация не найдена\n"

        return resault,id
    if unp == 'file':
        try:
            f = open('unp.txt', 'r')
        except:
            print("\n\n\nВ текущей дериктории отсутствует файл unp.txt !!!\n\n\n")
            return 
        counter=0
        resault_all=''
        resault3temp=''
        id_all=0
        id2_all=0
        id3_all=0
        for line in f:
            unp=line.replace("\n","")
            if len(unp)>2:
                resault,id = calculator(num_phone_col,i,unp)
                resault2,id2 = calculator(num_mail_col,i,unp)
                resault3,id3 = calculator(num_org_name,i,unp)
                counter+=1
                id_all+=id
                id2_all+=id2
                id3_all+=id3
                resault3temp+=unp +"    "+resault3
                resault_all +=resault+resault2
        resault=resault_all
        resault3=resault3temp
        id=id_all
        id2=id2_all
        id3=id3_all
    else:
        resault,id = calculator(num_phone_col,i,unp)
        resault2,id2 = calculator(num_mail_col,i,unp)
        id3=id2

        #сумирую результат
        resault += resault2
    

    cdt = datetime.datetime.now()
    file_name_ = file_name +f"_{cdt.date()}_count={id+id2}={id}p+{id2}m" 
    file_org_name = file_name +f"_{cdt.date()}_ORG={id3}" 
    
    try:
        with open(f'{file_name_}.txt','w') as fp:
            fp.write(resault)
        import subprocess as sp
        programName = "notepad.exe"
        sp.Popen([programName, file_name_])
        
        with open(f'{file_org_name}.txt','w') as fp:
            fp.write(resault3)
        import subprocess as sp
        programName = "notepad.exe"
        sp.Popen([programName, file_org_name])
        fp.close()
    except:
        print(resault)


while True:
    # os.system('cls' if os.name=='nt' else 'clear')
    menu = '1','2','3','4','5','6','7','8','9','10','11','12','q','Q','й','Й'
    print("Для получения списка контатных телефонов и email`ов клиентов по конкретной услуге, введите номер услуги:\n1)Для IaaS\n2)Для IaaS_62\n3)Для Colocation\n4)Для Colocation_62n\n5)Для S3\n6)Для BaaS\n7)Для BaaS_62\n8)Для CloudConnect\n9)Для WMaaS\n10)Для WAF\n11)Для SIEMaaS\n12)Для DRaaS\n       q\й\Q\Й)Для завершения работы программы")
    service = input("Ваш выбор:")
    while service not in menu:
        print(f"Введено некоректно значение {service}\nДля ввода доступны только варинаты: {menu}")
        service = input("Ваш выбор:")
    if service == "q" or service == "Q" or service == "й" or service == "Й":
        break
    print(".txt Файл должен находится в тойже дериктори что и сполняемый файл, и иметь имя - unp.txt")
    unp = input("Введите УНП для поиска или слово \"file\" для поиска УНП из файла \"unp.txt\" в дериктории данной программы:")
    

    get_wiki_data(service,unp)