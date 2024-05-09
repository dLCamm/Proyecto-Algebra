import customtkinter


def buttons(frame, frame2):
    print('')

    button_1 = customtkinter.CTkButton(master=frame, text='Operaciones entre matrices', height=125, width=250, font=("Arial", 15),
                                       fg_color="#3E4446")
    button_2 = customtkinter.CTkButton(master=frame, text='Matriz Inversa', height=125, width=250, font=("Arial", 15),
                                       fg_color="#3E4446")
    button_3 = customtkinter.CTkButton(master=frame, text='Determinante de una matriz', height=125, width=250,
                                       font=("Arial", 15),
                                       fg_color="#3E4446")
    button_4 = customtkinter.CTkButton(master=frame, text='Rango de una matriz', height=125, width=250,
                                       font=("Arial", 15),
                                       fg_color="#3E4446")
    button_5 = customtkinter.CTkButton(master=frame2, text='Cifrado por matrices', height=125, width=250,
                                       font=("Arial", 15),
                                       fg_color="#3E4446")
    button_6 = customtkinter.CTkButton(master=frame2, text='Cadenas de markov', height=125, width=250,
                                       font=("Arial", 15),
                                       fg_color="#3E4446")
    button_7 = customtkinter.CTkButton(master=frame2, text='Operaciones con vectores', height=125, width=250,
                                       font=("Arial", 15),
                                       fg_color="#3E4446")


    button_1.pack(pady=10, padx=10)
    button_2.pack(pady=10, padx=10)
    button_3.pack(pady=10, padx=10)
    button_4.pack(pady=10, padx=10)
    button_5.pack(pady=10, padx=10)
    button_6.pack(pady=10, padx=10)
    button_7.pack(pady=10, padx=10)


    return


def main_interact():
    root = customtkinter.CTk()
    customtkinter.set_appearance_mode('Light')
    customtkinter.set_default_color_theme('blue')

    root.title("MENU")
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=10, padx=10, fill='both', expand=True)
    frame2 = customtkinter.CTkFrame(master=frame, fg_color="White", width=50)
    frame2.pack(pady=10, padx=8, fill='both', expand=True, side='right')
    frame3 = customtkinter.CTkFrame(master=frame, fg_color="White")
    frame3.pack(pady=20, padx=8, fill='both', expand=True, side='left')

    buttons(frame3, frame2)

    frame.pack()
    root.geometry('800x650')
    root.mainloop()


main_interact()



