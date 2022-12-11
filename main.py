from itertools import count
import win32con, win32api, os, sys, time, pywhatkit, csv

# crea archivo para almacenar datos enviados
open("backup.csv", 'a').close()
win32api.SetFileAttributes("backup.csv",win32con.FILE_ATTRIBUTE_HIDDEN)


def valid_fields (validate:list): 

    if validate.__len__() > 1:
        # filtrando campos vacios
        validate = [num[0] for num in validate[1:] if bool(num)==True]
        # filtrando cantida de numeros
        validate = [num for num in validate if num.__len__()==10]
        # validando numero de celular inicial 3
        validate = [ num for num in validate if num.startswith('3')]

        return validate
    return False
    

def valid_num_copy (path1:str, path2:str):
    """
        valida numeros y si hay copia se elimina uno
    """
    with open(path1, "r") as file_csv, open(path2, "r") as file_csv_copy:
        #data que llama a la funcion validar campos para no tener una lista vacia
        data = valid_fields(list(csv.reader(file_csv, delimiter=",")))
        data_copy = valid_fields(list(csv.reader(file_csv_copy, delimiter=",")))
        
        if data_copy != False:
            print('Recuerdo {} numeros enviados..'.format(data_copy.__len__()))
        else:
            print ('bd_copy es {} igual a 0'.format(data_copy))    
        if data_copy:
            # si exite numero en la copia, elimina numero existente en data 
            for num in data_copy:
                if num in data:
                    data.remove(num)
                else:
                    continue       
    return data
    
       
if __name__ == "__main__":
   
    message_csv = '------El archivo debe estar ubica en esta misma carpeta.------\nIngresa el nombre del archivo de la base de datos a leer con su respectiva extesion .csv '
    message_img = '------El archivo debe estar ubica en esta misma carpeta.------\nIngresa el nombre de la imagen a leer con su respectiva extesion .jpg-png: '
    message_valid_name = '---El archivo no existe, ingresa un archivo valido o preciona 0 para cancelar--- \n'
    file_bd_copy = 'backup.csv'

    print ('\n-----BIENVENIDO AL SISTEMA DE ENVIOS DE MENSAJES AUTOMATICOS PARA WHATSAPP-----\n --------Más información whatsapp: +573158048471-------- \n')

    while True:
        try:
            question=int(input('Seleccione: \n 1-Mensaje con imagen. \n 2-Solo mensaje. \n 0-Salir \n'))
            if question == 1:

                print ('='*20)
                file_bd_csv= str(input(message_csv))
                while os.path.exists(file_bd_csv) == False:
                    print (message_valid_name)
                    file_bd_csv= str(input(message_csv))
                    if file_bd_csv == '0':
                        sys.exit()
                
                print ('\n')
                print ('='*70)
                image = str(input(message_img))
                print (image)
                while os.path.exists(image) == False:
                    print (message_valid_name)
                    image = str(input(message_img))
                    if file_bd_csv == '0':
                        sys.exit()   
                                        
                message = str(input('Ingresa el mensaje a enviar:\n '))

                break

            elif question == 2:
                file_bd_csv= str(input(message_csv))
                while os.path.exists(file_bd_csv) == False:
                    print (message_valid_name)
                    file_bd_csv= str(input(message_csv))
                    if file_bd_csv == '0':
                        sys.exit()      

                message = str(input('Ingresa el mensaje a enviar:\n '))

                break

            elif question == 0:
                sys.exit()

        except ValueError:
            print ('='*70)
            print('\n ****Selecciona un opción(numero) valido****\n') 
            print ('='*70)

         
    #url_wsp = 'https://wa.me/c/573052477600'
    #message = 'Buen día. Me comunico de Guiatec; una empresa dedicada a brindar soluciones tecnológicas. Queremos ofrecer nuestros servicios. \nPedimos disculpas por molestias ocasionadas ✌🏼 y agradecemos por la atención prestada.😁.  \n' + url_wsp
    list_num = valid_num_copy(file_bd_csv, file_bd_copy)
      
    if bool(list_num):
        count_send = 0
        if question == 1:

            for num in list_num:
                print ('Enviado mensaje al nuemro {} .....'.format(num))
                count_send += 1
                print ('Mensajes eviados {} '.format(count_send))
                print ('Presiona Ctrl+C para cancelar')
                print ('='*70)
                time.sleep(4)
                pywhatkit.sendwhats_image('+57' + num, image, message, tab_close=True, close_time=15)        
                with open(file_bd_copy, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([num])
        elif question == 2:
            
            for num in list_num:
                print ('Enviado mensaje al nuemro {} .....'.format(num))
                count_send += 1
                print ('Mensajes eviados {} '.format(count_send))
                print ('Presiona Ctrl+C para cancelar')
                print ('='*70)
                time.sleep(4)
                pywhatkit.sendwhatmsg_instantly('+57' + num, message, tab_close=True, close_time=10)        
                with open(file_bd_copy, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([num])           
    else:
        print ('='*70)
        print ("..........No hay numeros nuevos para enviar..........") 