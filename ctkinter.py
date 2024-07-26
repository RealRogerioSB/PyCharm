import os
import tkinter

import customtkinter as ctk
import tkinter as tk
from PIL import Image

ctk.set_appearance_mode("system")  # Modes: system (standard), dark, light
ctk.set_default_color_theme("blue")  # Themes: blue (standard), green, dark-blue


def tk1():
    class App1(ctk.CTk):
        def __init__(self):
            super().__init__()

            # configure window
            self.title("customtkinter complex example.py")
            self.geometry("1100x580")

            # configure grid layout (4x4)
            self.grid_columnconfigure(1, weight=1)
            self.grid_columnconfigure((2, 3), weight=0)
            self.grid_rowconfigure((0, 1, 2), weight=1)

            # create sidebar frame with widgets
            self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
            self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
            self.sidebar_frame.grid_rowconfigure(4, weight=1)
            self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="customtk", font=ctk.CTkFont(size=20,
                                                                                                 weight="bold"))
            self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
            self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
            self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
            self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
            self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
            self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
            self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
            self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
            self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
            self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["System", "Light", "Dark"],
                                                                 command=self.change_appearance_mode_event)
            self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
            self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
            self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
            self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame,
                                                         values=["80%", "90%", "100%", "110%", "120%"],
                                                         command=self.change_scaling_event)
            self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

            # create main entry and button
            self.entry = ctk.CTkEntry(self, placeholder_text="CTkEntry")
            self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

            self.main_button_1 = ctk.CTkButton(master=self, fg_color="transparent", border_width=2,
                                               text_color=("gray10", "#DCE4EE"))
            self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

            # create textbox
            self.textbox = ctk.CTkTextbox(self, width=250)
            self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

            # create tabview
            self.tabview = ctk.CTkTabview(self, width=250)
            self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
            self.tabview.add("CTkTabview")
            self.tabview.add("Tab 2")
            self.tabview.add("Tab 3")
            self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
            self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

            self.optionmenu_1 = ctk.CTkOptionMenu(self.tabview.tab("CTkTabview"), dynamic_resizing=False,
                                                  values=["Value 1", "Value 2", "Value Long Long Long"])
            self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
            self.combobox_1 = ctk.CTkComboBox(self.tabview.tab("CTkTabview"),
                                              values=["Value 1", "Value 2", "Value Long....."])
            self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
            self.string_input_button = ctk.CTkButton(self.tabview.tab("CTkTabview"), text="Open CTkInputDialog",
                                                     command=self.open_input_dialog_event)
            self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
            self.label_tab_2 = ctk.CTkLabel(self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
            self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

            # create radiobutton frame
            self.radiobutton_frame = ctk.CTkFrame(self)
            self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
            self.radio_var = tk.IntVar(value=0)
            self.label_radio_group = ctk.CTkLabel(master=self.radiobutton_frame, text="CTkRadioButton Group:")
            self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
            self.radio_button_1 = ctk.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0)
            self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
            self.radio_button_2 = ctk.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1)
            self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
            self.radio_button_3 = ctk.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2)
            self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

            # create slider and progressbar frame
            self.slider_progressbar_frame = ctk.CTkFrame(self, fg_color="transparent")
            self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
            self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
            self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
            self.seg_button_1 = ctk.CTkSegmentedButton(self.slider_progressbar_frame)
            self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
            self.progressbar_1 = ctk.CTkProgressBar(self.slider_progressbar_frame)
            self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
            self.progressbar_2 = ctk.CTkProgressBar(self.slider_progressbar_frame)
            self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
            self.slider_1 = ctk.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
            self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
            self.slider_2 = ctk.CTkSlider(self.slider_progressbar_frame, orientation="vertical")
            self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
            self.progressbar_3 = ctk.CTkProgressBar(self.slider_progressbar_frame, orientation="vertical")
            self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")

            # create scrollable frame
            self.scrollable_frame = ctk.CTkScrollableFrame(self, label_text="CTkScrollableFrame")
            self.scrollable_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
            self.scrollable_frame.grid_columnconfigure(0, weight=1)
            self.scrollable_frame_switches = []
            for i in range(20):
                switch = ctk.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
                switch.grid(row=i, column=0, padx=10, pady=(0, 20))
                self.scrollable_frame_switches.append(switch)

            # create checkbox and switch frame
            self.checkbox_slider_frame = ctk.CTkFrame(self)
            self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
            self.checkbox_1 = ctk.CTkCheckBox(master=self.checkbox_slider_frame)
            self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
            self.checkbox_2 = ctk.CTkCheckBox(master=self.checkbox_slider_frame)
            self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")
            self.checkbox_3 = ctk.CTkCheckBox(master=self.checkbox_slider_frame)
            self.checkbox_3.grid(row=3, column=0, pady=20, padx=20, sticky="n")

            # set default values
            self.sidebar_button_3.configure(state="disabled", text="Disabled CTkButton")
            self.checkbox_3.configure(state="disabled")
            self.checkbox_1.select()
            self.scrollable_frame_switches[0].select()
            self.scrollable_frame_switches[4].select()
            self.radio_button_3.configure(state="disabled")
            self.appearance_mode_optionemenu.set("Dark")
            self.scaling_optionemenu.set("100%")
            self.optionmenu_1.set("CTkOptionmenu")
            self.combobox_1.set("CTkComboBox")
            self.slider_1.configure(command=self.progressbar_2.set)
            self.slider_2.configure(command=self.progressbar_3.set)
            self.progressbar_1.configure(mode="indeterminnate")
            self.progressbar_1.start()
            self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing el" +
                                "itr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat," +
                                " sed diam voluptua.\n\n" * 20)
            self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
            self.seg_button_1.set("Value 2")

        @classmethod
        def open_input_dialog_event(cls):
            dialog = ctk.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
            print("CTkInputDialog:", dialog.get_input())

        @classmethod
        def change_appearance_mode_event(cls, new_appearance_mode: str):
            ctk.set_appearance_mode(new_appearance_mode)

        @classmethod
        def change_scaling_event(cls, new_scaling: str):
            new_scaling_float = int(new_scaling.replace("%", "")) / 100
            ctk.set_widget_scaling(new_scaling_float)

        @classmethod
        def sidebar_button_event(cls):
            print("sidebar_button click")

    if __name__ == "__main__":
        app = App1()
        app.mainloop()


def tk2():
    class App2(ctk.CTk):
        width = 900
        height = 600

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.title("ctk example_background_image.py")
            self.geometry(f"{self.width}x{self.height}")
            self.resizable(False, False)

            # load and create background image
            current_path = os.path.dirname(os.path.realpath(__file__))
            self.bg_image = ctk.CTkImage(Image.open(current_path + "/img/bg_gradient.jpg"),
                                         size=(self.width, self.height))
            self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image)
            self.bg_image_label.grid(row=0, column=0)

            # create login frame
            self.login_frame = ctk.CTkFrame(self, corner_radius=0)
            self.login_frame.grid(row=0, column=0, sticky="ns")
            self.login_label = ctk.CTkLabel(self.login_frame, text="ctk\nPágina de Login",
                                            font=ctk.CTkFont(size=20, weight="bold"))
            self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
            self.username_entry = ctk.CTkEntry(self.login_frame, width=200, placeholder_text="usuário")
            self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
            self.password_entry = ctk.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="senha")
            self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
            self.login_button = ctk.CTkButton(self.login_frame, text="Logar", command=self.login_event, width=200)
            self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

            # create main frame
            self.main_frame = ctk.CTkFrame(self, corner_radius=0)
            self.main_frame.grid_columnconfigure(0, weight=1)
            self.main_label = ctk.CTkLabel(self.main_frame, text="ctk\nPágina Principal",
                                           font=ctk.CTkFont(size=20, weight="bold"))
            self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))
            self.back_button = ctk.CTkButton(self.main_frame, text="Voltar", command=self.back_event, width=200)
            self.back_button.grid(row=1, column=0, padx=30, pady=(15, 15))

        def login_event(self):
            print("Logar pressionado - usuário:", self.username_entry.get(), "e senha:", self.password_entry.get())

            self.login_frame.grid_forget()  # remove login frame
            self.main_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show main frame

        def back_event(self):
            self.main_frame.grid_forget()  # remove main frame
            self.login_frame.grid(row=0, column=0, sticky="ns")  # show login frame

    if __name__ == "__main__":
        app = App2()
        app.mainloop()


def tk3():
    class App3(ctk.CTk):
        def __init__(self):
            super().__init__()

            self.title("image_example.py")
            self.geometry("700x450")

            # set grid layout 1x2
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=1)

            # load images with light and dark mode image
            image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")
            self.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")),
                                           size=(26, 26))
            self.large_test_image = ctk.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")),
                                                 size=(500, 150))
            self.image_icon_image = ctk.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")),
                                                 size=(20, 20))
            self.home_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                           dark_image=Image.open(os.path.join(image_path, "home_light.png")),
                                           size=(20, 20))
            self.chat_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                           dark_image=Image.open(os.path.join(image_path, "chat_light.png")),
                                           size=(20, 20))
            self.add_user_image = ctk.CTkImage(
                light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                dark_image=Image.open(os.path.join(image_path, "add_user_light.png")),
                size=(20, 20)
            )

            # create navigation frame
            self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
            self.navigation_frame.grid(row=0, column=0, sticky="nsew")
            self.navigation_frame.grid_rowconfigure(4, weight=1)

            self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="  Image Example",
                                                       image=self.logo_image, compound="left",
                                                       font=ctk.CTkFont(size=15, weight="bold"))
            self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

            self.home_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                             border_spacing=10, text="Home", fg_color="transparent",
                                             text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                             image=self.home_image, anchor="w", command=self.home_btn_event)
            self.home_button.grid(row=1, column=0, sticky="ew")

            self.frame_2_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                border_spacing=10, text="Frame 2", fg_color="transparent",
                                                text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                image=self.chat_image, anchor="w",
                                                command=self.frame_2_btn_event)
            self.frame_2_button.grid(row=2, column=0, sticky="ew")

            self.frame_3_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                border_spacing=10, text="Frame 3", fg_color="transparent",
                                                text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                image=self.add_user_image, anchor="w",
                                                command=self.frame_3_btn_event)
            self.frame_3_button.grid(row=3, column=0, sticky="ew")

            self.appearance_mode_menu = ctk.CTkOptionMenu(self.navigation_frame, values=["System", "Dark", "Light"],
                                                          command=self.change_appearance_mode_event)
            self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

            # create home frame
            self.home_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
            self.home_frame.grid_columnconfigure(0, weight=1)

            self.home_frame_large_image_label = ctk.CTkLabel(self.home_frame, text="", image=self.large_test_image)
            self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

            self.home_frame_button_1 = ctk.CTkButton(self.home_frame, text="", image=self.image_icon_image)
            self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
            self.home_frame_button_2 = ctk.CTkButton(self.home_frame, text="CTkButton",
                                                     image=self.image_icon_image, compound="right")
            self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
            self.home_frame_button_3 = ctk.CTkButton(self.home_frame, text="CTkButton",
                                                     image=self.image_icon_image, compound="top")
            self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
            self.home_frame_button_4 = ctk.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image,
                                                     compound="bottom", anchor="w")
            self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

            # create second frame
            self.second_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

            # create third frame
            self.third_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

            # select default frame
            self.select_frame_by_name("home")

        def select_frame_by_name(self, name):
            # set button color for selected button
            self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
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

        def home_btn_event(self):
            self.select_frame_by_name("home")

        def frame_2_btn_event(self):
            self.select_frame_by_name("frame_2")

        def frame_3_btn_event(self):
            self.select_frame_by_name("frame_3")

        @staticmethod
        def change_appearance_mode_event(new_appearance_mode):
            ctk.set_appearance_mode(new_appearance_mode)

    if __name__ == "__main__":
        app = App3()
        app.mainloop()


def tk4():
    class ScrollableCheckBoxFrame(ctk.CTkScrollableFrame):
        def __init__(self, master, item_list, command=None, **kwargs):
            super().__init__(master, **kwargs)

            self.command = command
            self.checkbox_list = []
            for i, item in enumerate(item_list):
                self.add_item(item)

        def add_item(self, item):
            checkbox = ctk.CTkCheckBox(self, text=item)
            if self.command is not None:
                checkbox.configure(command=self.command)
            checkbox.grid(row=len(self.checkbox_list), column=0, pady=(0, 10))
            self.checkbox_list.append(checkbox)

        def remove_item(self, item):
            for checkbox in self.checkbox_list:
                if item == checkbox.cget("text"):
                    checkbox.destroy()
                    self.checkbox_list.remove(checkbox)
                    return

        def get_checked_items(self):
            return [checkbox.cget("text") for checkbox in self.checkbox_list if checkbox.get() == 1]

    class ScrollableRadiobuttonFrame(ctk.CTkScrollableFrame):
        def __init__(self, master, item_list, command=None, **kwargs):
            super().__init__(master, **kwargs)

            self.command = command
            self.radiobutton_variable = ctk.StringVar()
            self.radiobutton_list = []
            for i, item in enumerate(item_list):
                self.add_item(item)

        def add_item(self, item):
            radiobutton = ctk.CTkRadioButton(self, text=item, value=item, variable=self.radiobutton_variable)
            if self.command is not None:
                radiobutton.configure(command=self.command)
            radiobutton.grid(row=len(self.radiobutton_list), column=0, pady=(0, 10))
            self.radiobutton_list.append(radiobutton)

        def remove_item(self, item):
            for radiobutton in self.radiobutton_list:
                if item == radiobutton.cget("text"):
                    radiobutton.destroy()
                    self.radiobutton_list.remove(radiobutton)
                    return

        def get_checked_item(self):
            return self.radiobutton_variable.get()

    class ScrollableLabelButtonFrame(ctk.CTkScrollableFrame):
        def __init__(self, master, command=None, **kwargs):
            super().__init__(master, **kwargs)
            self.grid_columnconfigure(0, weight=1)

            self.command = command
            self.radiobutton_variable = ctk.StringVar()
            self.label_list = []
            self.button_list = []

        def add_item(self, item, image=None):
            label = ctk.CTkLabel(self, text=item, image=image, compound="left", padx=5, anchor="w")
            button = ctk.CTkButton(self, text="Command", width=100, height=24)
            if self.command is not None:
                button.configure(command=lambda: self.command(item))
            label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
            button.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5)
            self.label_list.append(label)
            self.button_list.append(button)

        def remove_item(self, item):
            for label, button in zip(self.label_list, self.button_list):
                if item == label.cget("text"):
                    label.destroy()
                    button.destroy()
                    self.label_list.remove(label)
                    self.button_list.remove(button)
                    return

    class App4(ctk.CTk):
        def __init__(self):
            super().__init__()

            self.title("CTkScrollableFrame example")
            self.grid_rowconfigure(0, weight=1)
            self.columnconfigure(2, weight=1)

            # create scrollable checkbox frame
            self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(master=self, width=200,
                                                                     command=self.checkbox_frame_event,
                                                                     item_list=[f"item {i}" for i in range(50)])
            self.scrollable_checkbox_frame.grid(row=0, column=0, padx=15, pady=15, sticky="ns")
            self.scrollable_checkbox_frame.add_item("new item")

            # create scrollable radiobutton frame
            self.scrollable_radiobutton_frame = ScrollableRadiobuttonFrame(master=self, width=500,
                                                                           command=self.radiobutton_frame_event,
                                                                           item_list=[f"item {i}" for i in range(100)],
                                                                           label_text="ScrollableRadiobuttonFrame")
            self.scrollable_radiobutton_frame.grid(row=0, column=1, padx=15, pady=15, sticky="ns")
            self.scrollable_radiobutton_frame.configure(width=200)
            self.scrollable_radiobutton_frame.remove_item("item 3")

            # create scrollable label and button frame
            current_dir = os.path.dirname(os.path.abspath(__file__))
            self.scrollable_label_button_frame = ScrollableLabelButtonFrame(master=self, width=300,
                                                                            command=self.label_button_frame_event,
                                                                            corner_radius=0)
            self.scrollable_label_button_frame.grid(row=0, column=2, padx=0, pady=0, sticky="nsew")
            for i in range(20):  # add items with images
                self.scrollable_label_button_frame.add_item(f"image and item {i}",
                                                            image=ctk.CTkImage(Image.open(os.path.join(
                                                                current_dir, "img", "chat_light.png"))))

        def checkbox_frame_event(self):
            print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")

        def radiobutton_frame_event(self):
            print(f"radiobutton frame modified: {self.scrollable_radiobutton_frame.get_checked_item()}")

        @staticmethod
        def label_button_frame_event(item):
            print(f"label button frame clicked: {item}")

    if __name__ == "__main__":
        app = App4()
        app.mainloop()


if __name__ == '__main__':
    option = input("1, 2, 3 ou 4? ")
    match option:
        case "1": tk1()
        case "2": tk2()
        case "3": tk3()
        case "4": tk4()
