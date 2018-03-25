
import  pickle
from time import sleep
from tkinter import *
from tkinter import ttk

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_EXIT = 5
ACTION_SHOW_CONTACTS = 6

MENU_OPTIONS = [ACTION_ADD_CONTACT,
                ACTION_REMOVE_CONTACT,
                ACTION_FIND_CONTACT,
                ACTION_EXPORT_CONTACT,
                ACTION_SHOW_CONTACTS]

SAVE_FILE_NAME = "contacts.save"


def ask_until_option_expected(options):
    selected_action = ""

    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in options):
        selected_action = input("¿Qué opción deseas?")

    return int(selected_action)


def show_menu():
    print("Acciones disponibles a elegir")
    print("1--> Añadir contacto")
    print("2--> Eliminar contacto")
    print("3--> Buscar un contacto")
    print("4--> Exportar contactos a un CSV")
    print("5--> Salir")
    print("6--> Mostrar contactos guardados")

    return ask_until_option_expected(MENU_OPTIONS)


def ask_new_contact(contacts):
    print("\n\n Añadir contacto \n")
    add_contact(input("Nombre: "), input("Teléfono: "), input("Email:"))

    print("Se ha añadido el contacto {} correctamente \n".format(contacts["name"]))
    sleep(2)


def add_contact(contacts, name, phone, email):
    contact={
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    return contact



def remove_contact(contacts):
    print("Elige el contacto que quieres borrar de la lista \n")
    print("-----------------------------------------------------")
    print(contacts)
    contact_to_remove = input("¿Qué contacto quieres borrar?. Escribe el nombre del contacto")
    for contact in contacts:
        if contact["name"] == contact_to_remove:
            contacts.remove(contact)
    print("Tu contacto seleccionado se ha eliminado con éxito!")
    print("-----------------------------------------------------")


def find_contact(contacts):
    print("\n\nBuscar contacto\n")
    search_term = input("Introducir el nombre del contacto o parte de él: ")
    found_contacts = []

    print("He encontrado los siguientes contactos:")
    contact_indexes = []
    contact_counter = 0

    for contact in contacts:
        if contact["name"].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{} - {}".format(contact_counter, contact["name"]))
            contact_indexes.append(contact_counter)
            contact_counter += 1

    contact_index = 0

    if len(contact_indexes) > 1:
        contact_index = ask_until_option_expected(contact_indexes)
    elif len(contact_indexes) == 0:
        print("No se ha encontrado ninguno.")
        return

    print("\nInformación sobre {}\n".format(found_contacts[contact_index]["name"]))
    print("Nombre: {name}, Telefono: {phone}, Email: {email}\n\n".format(**found_contacts[contact_index]))
    sleep(2)


def export_contact(contacts):
    pass


def show_contacts(contacts):
    print(contacts)


def load_contacts():
    try:
        return pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
    print("Datos guardados satisfactoriamente!")

def add_contact_tk(contacts, name, phone, email, frame_contact_list):
    contact= add_contact(contacts, name, phone, email)
    cols, row= frame_contact_list.grid_size()
    ttk.Label(frame_contact_list, text=contact["name"]).grid(column=1, row=row)
    ttk.Label(frame_contact_list, text=contact["email"]).grid(column=2, row=row)
    ttk.Label(frame_contact_list, text= contact["phone"]).grid(column=3, row=row)


def main():

    contacts= []

#USER INTERFACES

    #Frame para los inputs de texto para añadir contactos.
    root= Tk()
    frame_add_contact= ttk.Frame(root, padding= "30 12 30 12")
    frame_add_contact.grid()

    #Frame para mostrar los datos añadidos.
    frame_contact_list = ttk.Frame(root, padding="30 12 30 12")
    frame_contact_list.grid()

    #Definicion de variables para la entrada de datos de los Entrys
    name= StringVar()
    phone= StringVar()
    email= StringVar()

    #Labels con los nombres de mail, teléfono y nombre.
    ttk.Label(frame_add_contact, text="Nombre").grid(column=1, row=1)
    ttk.Label(frame_add_contact, text="Email").grid(column=2, row=1)
    ttk.Label(frame_add_contact, text="Phone").grid(column=3, row=1)

    #Cuadra de texto del mail, telefono y nombre
    ttk.Entry(frame_add_contact, width=7, textvariable= name).grid(column=1, row=2)
    ttk.Entry(frame_add_contact, width= 7, textvariable= email).grid(column=2, row=2)
    ttk.Entry(frame_add_contact, width=7, textvariable= phone).grid(column=3, row=2)

    ttk.Label(frame_contact_list, text="Nombre").grid(column=1, row=1)
    ttk.Label(frame_contact_list, text="Email").grid(column=2, row=1)
    ttk.Label(frame_contact_list, text="Phone").grid(column=3, row=1)

    #Boton que añade los datos a la lista correspondiente
    ttk.Button(frame_add_contact,
               text="Añadir",
               command=lambda: add_contact_tk(contacts, name.get(), phone.get(), email.get(), frame_contact_list)
               ).grid(column=3, row=3)


    root.mainloop()

if __name__ == "__main__":
    main()