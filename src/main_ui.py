import os
import tkinter as tk
import tkinter.messagebox
import customtkinter
from PIL import Image
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import filedialog

# os.environ['TCL_LIBRARY'] = "venv/lib/python3.10/site-packages/tkdnd2.8"

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("PDF to Excel")
        self.geometry(f"{1100}x{630}")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")),
                                                 size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")),
                                                       size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")),
                                                       size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")),
                                                 size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")),
                                                 size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
            dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  PDF to Excel",
                                                             image=self.logo_image,
                                                             compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.extraction_home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                              border_spacing=10,
                                                              text="Extraction",
                                                              fg_color="transparent", text_color=("gray10", "gray90"),
                                                              hover_color=("gray70", "gray30"),
                                                              image=self.home_image, anchor="w",
                                                              command=self.extraction_home_button_event)
        self.extraction_home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="About",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w",
                                                      command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Contact",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w",
                                                      command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # ============================================
        # ========== Create Extraction Page ==========
        # ============================================
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        # ==== Create first line frame ====
        self.first_line_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0)
        self.first_line_frame.grid(row=0, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.first_line_frame.grid_columnconfigure(0, weight=1)

        # ==== Création du cadre d'upload pour le fichier PDF ====
        self.upload_frame = customtkinter.CTkFrame(self.first_line_frame, corner_radius=0)
        self.upload_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.upload_frame.grid_columnconfigure(0, weight=1)

        self.upload_label = customtkinter.CTkLabel(self.upload_frame, text="Upload PDF file",
                                                   font=customtkinter.CTkFont(size=15, weight="bold"))
        self.upload_label.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        # Bouton pour choisir le fichier PDF
        self.choose_file_button = customtkinter.CTkButton(self.upload_frame, text="Choose PDF",
                                                          command=self.choose_pdf_file)
        self.choose_file_button.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.file_path_label = customtkinter.CTkLabel(self.upload_frame, text="")
        self.file_path_label.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        # # Utilisation d'un Label Tkinter standard pour le drag and drop, stylisé pour s'adapter
        # self.upload_box = tk.Label(self.upload_frame, text="Drag and drop the PDF file here",
        #                            bg="gray90", fg="gray50")
        # self.upload_box.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        #
        # # Configuration pour le drag and drop
        # self.upload_box.drop_target_register(DND_FILES)
        # self.upload_box.dnd_bind('<<Drop>>', self.on_drop)

        # ==== Create Extract Information frame ====
        self.extract_information_frame = customtkinter.CTkFrame(self.first_line_frame, corner_radius=0)
        self.extract_information_frame.grid(row=0, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.start_page_label = customtkinter.CTkLabel(self.extract_information_frame, text="Start Page")
        self.start_page_label.grid(row=0, column=0, padx=20, pady=10)
        self.start_page_entry = customtkinter.CTkEntry(self.extract_information_frame, placeholder_text="Start Page")
        self.start_page_entry.grid(row=0, column=1, padx=20, pady=10)

        self.end_page_label = customtkinter.CTkLabel(self.extract_information_frame, text="End Page")
        self.end_page_label.grid(row=1, column=0, padx=20, pady=10)
        self.end_page_entry = customtkinter.CTkEntry(self.extract_information_frame, placeholder_text="End Page")
        self.end_page_entry.grid(row=1, column=1, padx=20, pady=10)

        self.chunk_size_label = customtkinter.CTkLabel(self.extract_information_frame, text="Chunk Size")
        self.chunk_size_label.grid(row=2, column=0, padx=20, pady=10)
        self.chunk_size_entry = customtkinter.CTkEntry(self.extract_information_frame, placeholder_text="Chunk Size")
        self.chunk_size_entry.grid(row=2, column=1, padx=20, pady=10)

        self.fournisseur_label = customtkinter.CTkLabel(self.extract_information_frame, text="Fournisseur")
        self.fournisseur_label.grid(row=3, column=0, padx=20, pady=10)
        self.fournisseur_entry = customtkinter.CTkEntry(self.extract_information_frame, placeholder_text="Fournisseur")
        self.fournisseur_entry.grid(row=3, column=1, padx=20, pady=10)

        self.output_path_label = customtkinter.CTkLabel(self.extract_information_frame, text="Output Path")
        self.output_path_label.grid(row=4, column=0, padx=20, pady=10)
        self.output_path_entry = customtkinter.CTkEntry(self.extract_information_frame, placeholder_text="Output Path")
        self.output_path_entry.grid(row=4, column=1, padx=20, pady=10)

        # ==== Create Second line frame ====
        self.second_line_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0)
        self.second_line_frame.grid(row=1, column=0, padx=(20, 20), pady=(0, 0), sticky="nsew")
        self.second_line_frame.grid_columnconfigure(0, weight=1)

        self.second_half_1_line_frame = customtkinter.CTkFrame(self.second_line_frame, corner_radius=0)
        self.second_half_1_line_frame.grid(row=0, column=0, sticky="nsew")
        self.second_half_1_line_frame.grid_columnconfigure(0, weight=1)

        self.second_half_2_line_frame = customtkinter.CTkFrame(self.second_line_frame, corner_radius=0)
        self.second_half_2_line_frame.grid(row=0, column=1, sticky="nsew")
        self.second_half_2_line_frame.grid_columnconfigure(0, weight=1)

        # ==== Create Tab view to show the prompt used to clean and extract the data ====
        self.tab_view = customtkinter.CTkTabview(self.second_half_1_line_frame, corner_radius=10)
        self.tab_view.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
        self.tab_view.add("Nettoyage")
        self.tab_view.add("Extraction")

        # Create the "Nettoyage" tab
        # Inside the tab we have a text box to show the prompt used to clean the data
        # self.nettoyage_tab = customtkinter.CTkFrame(self.tab_view.tab("Nettoyage"), corner_radius=0, width=200,
        #                                             height=70)
        self.nettoyage_textbox = customtkinter.CTkTextbox(self.tab_view.tab("Nettoyage"), width=410, height=200)
        self.nettoyage_textbox.grid(row=1, column=1, padx=20, pady=10)
        # self.nettoyage_textbox.insert("0.0", "Prompt used to clean the data")

        # Create the "Extraction" tab
        # Inside the tab we have a text box to show the prompt used to extract the data
        self.extraction_textbox = customtkinter.CTkTextbox(self.tab_view.tab("Extraction"), width=410, height=200)
        self.extraction_textbox.grid(row=0, column=0, padx=20, pady=10)
        # self.extraction_textbox.insert("0.0", "Prompt used to extract the data")

        # ==== Create Options frame ====
        # CTkScrollableFrame
        self.options_frame = customtkinter.CTkFrame(self.second_half_2_line_frame, corner_radius=0)
        self.options_frame.grid(row=1, column=2, padx=10, pady=(20, 20), sticky="nsew")
        self.options_frame.grid_columnconfigure(0, weight=1)

        self.options_label = customtkinter.CTkLabel(self.options_frame, text="Options")
        # self.options_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        self.options_label.grid(row=0, column=0, padx=20, pady=10)

        self.description_switch = customtkinter.CTkSwitch(self.options_frame, text="Get Description")
        self.description_switch.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        # self.description_switch.grid(row=2, column=0, padx=10, pady=10)

        self.save_intermediate_switch = customtkinter.CTkSwitch(self.options_frame, text="Save Intermediate")
        self.save_intermediate_switch.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        # self.save_intermediate_switch.grid(row=3, column=0, padx=(10, 20), pady=10)

        self.bilan_switch = customtkinter.CTkSwitch(self.options_frame, text="Get Bilan")
        self.bilan_switch.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        # self.bilan_switch.grid(row=4, column=0, padx=(10, 20), pady=10)

        # ==== Create Model frame ====
        # Inside the model frame we have the following options:
        # - GPT-4
        # - GPT-3.5
        # - Other
        # You can only select one model. Use a check box to select the model
        self.model_frame = customtkinter.CTkFrame(self.second_half_2_line_frame, corner_radius=0)
        self.model_frame.grid(row=1, column=3, padx=10, pady=20, sticky="nsew")
        self.model_var = tkinter.IntVar(value=0)

        self.model_label = customtkinter.CTkLabel(self.model_frame, text="Model AI")
        self.model_label.grid(row=0, column=0, padx=20, pady=10)

        self.gpt4_checkbox = customtkinter.CTkRadioButton(self.model_frame, text="GPT-4", variable=self.model_var,
                                                          value=0)
        self.gpt4_checkbox.grid(row=1, column=0, padx=20, pady=10)

        self.gpt35_checkbox = customtkinter.CTkRadioButton(self.model_frame, text="GPT-3.5", variable=self.model_var,
                                                           value=1)
        self.gpt35_checkbox.grid(row=2, column=0, padx=20, pady=10)

        self.other_checkbox = customtkinter.CTkRadioButton(self.model_frame, text="Other", variable=self.model_var,
                                                           value=2)
        self.other_checkbox.grid(row=3, column=0, padx=20, pady=10)

        self.model_frame.grid_rowconfigure(0, weight=1)
        self.model_frame.grid_columnconfigure(0, weight=1)

        # ==== Create Third line frame ====
        self.third_line_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0)
        self.third_line_frame.grid(row=2, column=0, padx=(20, 20), pady=(0, 0), sticky="nsew")
        self.third_line_frame.grid_columnconfigure(0, weight=1)

        # ==== Create Extract button on the right side ====
        self.extract_button = customtkinter.CTkButton(self.third_line_frame, text="Extract", corner_radius=10,
                                                      height=40,
                                                      border_spacing=10)
        self.extract_button.grid(row=0, column=2, padx=20, pady=10)

        # ============================================
        # ========== Create About Page ==========
        # ============================================
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)

        self.about_label = customtkinter.CTkLabel(self.second_frame, text="About",
                                                  font=customtkinter.CTkFont(size=15, weight="bold"))
        self.about_label.grid(row=0, column=0, padx=20, pady=20)

        self.about_textbox = customtkinter.CTkTextbox(self.second_frame, width=200, height=70)
        self.about_textbox.grid(row=1, column=0, padx=20, pady=10)
        self.about_textbox.insert("0.0", "This is a simple example of CustomTkinter")

        # ============================================
        # ========== Create Contact Page ==========
        # ============================================
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame.grid_columnconfigure(0, weight=1)

        self.contact_label = customtkinter.CTkLabel(self.third_frame, text="Contact",
                                                    font=customtkinter.CTkFont(size=15, weight="bold"))
        self.contact_label.grid(row=0, column=0, padx=20, pady=20)

        self.contact_textbox = customtkinter.CTkTextbox(self.third_frame, width=200, height=70)
        self.contact_textbox.grid(row=1, column=0, padx=20, pady=10)
        self.contact_textbox.insert("0.0", "Contact us at: "
                                           "email: ... \n"
                                           "phone: ... \n"
                                           "address: ...")

        # set Default values
        self.select_frame_by_name("home")
        self.appearance_mode_menu.set("System")
        self.gpt4_checkbox.select()
        self.chunk_size_entry.insert(0, "4")
        self.description_switch.select()
        self.save_intermediate_switch.select()
        self.bilan_switch.select()
        #     Prompt used to clean the data
        self.nettoyage_textbox.insert("0.0", """Nettoie et extrait les informations des produits du catalogue PDF suivant.

À partir du texte extrait d'un catalogue PDF de fournisseur, nettoie le texte et identifie toutes les informations de chaque produit comme par exemple: le poids, la largeur, la hauteur, la capacité etc... L'idée est de nettoyer le texte en français pour qu'il soit plus lisible et d'extraire toutes les informations pour chaque produit. Attention, il se peut que chaque produit ait plusieurs familles de spécifications. Tu dois extraire toutes les informations que tu trouves pour chaque produit, sans rien omettre. Chaque produit possède une description et un tableau, ne sois pas intelligent je veux que tu récupère toutes les valeurs du tableaux pour chaque produit sans rien omettre. S'il vous plaît, fournissez une liste complète et détaillée de toutes les caractéristiques pour chaque modèle sans assumer de similitudes avec d'autres modèles ou omettre des détails. Même si certains modèles partagent des caractéristiques communes, veuillez répéter toutes les informations pertinentes pour chaque modèle individuellement. Regroupe les produits qui se ressemblent dans la même famille de produits. Récupère toutes les bullets points de chaque produit et place les dans "Description".

Envoie moi le texte nettoyé et formaté pour chaque produit sous forme de Markdown, pas de texte supplémentaire:
```Markdown
=============================================
**[nom de Famille du produit 1] - [Modèles 1]:** 
_Description:_  
* Bullet point 1 
* Bullet point 2
* Bullet point 3


_Données du produit:_
> Modèles: [nom du produit1]
Caractéristique 1: Valeur 1
Caractéristique 2: Valeur 2
... (autres caractéristiques)

> Modèles: [nom du produit1 200]
Caractéristique 1: Valeur 1
Caractéristique 2: Valeur 2

=============================================
**[nom de Famille du produit 2] - [Modèles 1]:**
_Description:_ 
* Bullet point 1
 

_Données du produit:_
> Modèles: [Nom du produit2]
Caractéristique 1: Valeur 1
Caractéristique 2: Valeur 2

=============================================
```

Change "[nom de Famille du produit 1]" et "[nom de Famille du produit 2]" par le nom de famille du produit correspondant. De même pour "[Nom du produit1]", "[Nom du produit1 200]" etc. avec les noms des produits. Assure-toi de bien formater les tableaux avec les bonnes colonnes et de bien aligner les valeurs, ne fais pas de truncation des colonnes, ne sois pas feignant. 

Voici le texte du catalogue PDF:""")
        #     Prompt used to extract the data
        self.extraction_textbox.insert("0.0", """Extrait les informations de chaque produit du catalogue PDF suivant.
À partir du texte extrait d'un catalogue PDF de fournisseur, identifie toutes les informations de chaque produit comme par exemple: le poids, la largeur, la hauteur, la capacité etc.. Récupère toutes les informations pertinentes pour chaque produit ainsi que le nom du produit en français. Attention, certains produits peuvent avoir plusieurs familles de spécifications, assure-toi de tous les récupérer. Regroupe les produits qui se ressemblent dans la même famille de produits, par exemple: mettre les "DONKEY LIGHT RUN 150" et "DONKEY LIGHT RUN 200" dans la famille "Diable monte-escaliers électrique acier à bras rotatif et déplacement motorisé 130kg - DONKEY" et les "DMEG" la famille "Diable monte-escaliers électrique aluminium avec bras rotatif 170kg - DMEG". Précise bien les noms des familles de produits.

Il y a certaines règles de typo à respecter pour les noms de colonnes, assure-toi de les respecter: 
* Transforme tous les "Dimensions" en "Dim." 
* Dimensions hors tout (L x l x h) et Dimensions hors tout (L x p x h) = Dim. HT (L x l x h) mm
* (L x p) = (L x l)
* Dimensions bavette (L x p) = Dim. bavette (L x l)
* Capacité kg = Cap. kg 
* Volume = Vol.

Envoie moi les tableaux sous format JSON python de cette manière, sans texte supplémentaire ou explication ni de sauts de ligne:
{
  "Famille du produit1": {
    "Nom du produit1 150": {
        "Poids kg": "10",
        "Largeur cm": "20",
        "Hauteur cm": "30",
        "Capacité kg": "100",
        ... (autres attributs),
        },
        "Nom du produit1 200": {
            "Poids kg": "15",
            ... (autres attributs),
        },
    },
    "Famille du produit2": {
        "Nom du produit2 150": {
            "Poids kg": "10",
            ... (autres attributs),
        }
    },
    ...
}
Assure-toi que le JSON est bien formatté et exploitable directement en Python. Donne moi TOUTES les valeurs sans exceptions, Ne fais pas de "..." des valeurs ni des sauts de lignes `\n`.
Je ne veux aucune phrase ou texte supplémentaire, juste les données des produits.
Voici le texte du catalogue PDF:""")


    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.extraction_home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def extraction_home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def on_drop(self, event):
        fichier_pdf_path = event.data
        if isinstance(fichier_pdf_path, list):  # Vérifier si l'événement renvoie une liste de chemins
            fichier_pdf_path = fichier_pdf_path[0]  # Prendre le premier élément de la liste
        fichier_pdf_path = fichier_pdf_path.strip("{}")  # Nettoyer le chemin du fichier
        print(f"Fichier déposé : {fichier_pdf_path}")

    def choose_pdf_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.file_path_label.config(text=file_path)  # Affiche le chemin du fichier sélectionné


if __name__ == "__main__":
    app = App()
    app.mainloop()
