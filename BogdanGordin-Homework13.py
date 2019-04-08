"""
    Its called HUD, what a nuts week.
    Bogdan Gordin
    December 3, 2017
    COMSC-122-0940
    Mr. Littlefield

Below are notes:

 *Thse are just in case...
  
"""

import tkinter
import tkinter.messagebox


Labelfont = ('times', 20, 'bold')

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        """Program frame"""
        self.test0_frame = tkinter.Frame(self.main_window)
        self.test0_label = tkinter.Label(self.test0_frame, text="Bogdan's Gordin Final Week Nutcase Program")
        self.test0_label.config(font=Labelfont)
        
        """LMC ID frame"""
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test1_label = tkinter.Label(self.test1_frame, text='LMC ID:')
        self.test1_label.config(font=Labelfont)
        self.test1_entry = tkinter.Entry(self.test1_frame, width=10)

        """Name frame"""
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test2_label = tkinter.Label(self.test2_frame, text='Name:')
        self.test2_label.config(font=Labelfont)
        self.test2_entry = tkinter.Entry(self.test2_frame, width=20)
        
        """Radiobutton frame"""
        self.test3_frame = tkinter.Frame(self.main_window)
        self.radio_var = tkinter.IntVar()
        self.rb1 = tkinter.Radiobutton(self.test3_frame, text='In favor Prop A?', variable=self.radio_var, value=1)
        self.rb1.config(font=Labelfont)
        self.rb2 = tkinter.Radiobutton(self.test3_frame, text='Againts Prop A?', variable=self.radio_var, value=2)
        self.rb2.config(font=Labelfont)
        self.radio_var.set(0)

        """Checkbox frams"""
        self.test5_frame = tkinter.Frame(self.main_window)
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb1 = tkinter.Checkbutton(self.test5_frame, text='Candidate B', variable=self.cb_var1)
        self.cb1.config(font=Labelfont)
        self.cb2 = tkinter.Checkbutton(self.test5_frame, text='Candidate C', variable=self.cb_var2)
        self.cb2.config(font=Labelfont)
        

        """Buttons frame"""
        self.test4_frame = tkinter.Frame(self.main_window)
        self.ok_button = tkinter.Button(self.test4_frame, text='VOTE', command=self.show_choice)
        self.ok_button.config(font=Labelfont)
        self.quit_button = tkinter.Button(self.test4_frame, text='Leave and VOTE', command=self.main_window.destroy)
        self.quit_button.config(font=Labelfont)

        
        """pack the bits of frames"""
        self.test0_label.pack(side='left')
        self.test1_label.pack(side='left')
        self.test1_entry.pack(side='left')
        self.test2_label.pack(side='left')
        self.test2_entry.pack(side='left')
        self.rb1.pack()
        self.rb2.pack()
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.cb1.pack()
        self.cb2.pack()

        """pack the frames"""
        self.test0_frame.pack()
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.test5_frame.pack()
        self.test4_frame.pack()
        
        
        """the message box"""
    def show_choice(self):
        if self.radio_var.get() == 1 and self.cb_var1.get() == 0 and self.cb_var2.get() == 0:
            tkinter.messagebox.showinfo('Voted', "You've chosen in favor Prop A and no candidate.")
            
        elif self.radio_var.get() == 2 and self.cb_var1.get() == 0 and self.cb_var2.get() == 0:
            tkinter.messagebox.showinfo('Voted', "You've chosen againts Prop A and no candidate.")
            
        elif self.radio_var.get() == 1 and self.cb_var1.get() == 1 and self.cb_var2.get() == 0:
            tkinter.messagebox.showinfo('Voted', "You've choosen in favor Prop A and Candidate B.")

        elif self.radio_var.get() == 1 and self.cb_var1.get() == 0 and self.cb_var2.get() == 1:
            tkinter.messagebox.showinfo('Voted', "You've choosen in favor Prop A and Candidate C.")

        elif self.radio_var.get() == 2 and self.cb_var1.get() == 1 and self.cb_var2.get() == 0:
            tkinter.messagebox.showinfo('Voted', "You've choosen againts Prop A and voted Candidate B.")

        elif self.radio_var.get() == 2 and self.cb_var1.get() == 0 and self.cb_var2.get() == 1:
            tkinter.messagebox.showinfo('Voted', "You've choosen againts Prop A and voted Candidate C.")

        elif self.radio_var.get() == 1 or self.radio_var.get() == 2 and self.cb_var1.get() == 1 and self.cb_var2.get() == 1:
            tkinter.messagebox.showinfo('ERROR', "Can't vote for two Candidates.")
            
        elif self.radio_var.get() == 0 and self.cb_var1.get() == 1 and self.cb_var2.get() == 0:
            tkinter.messagebox.showinfo('ERROR', "Prop choisce missing, but voted for Candiate B.")
            
        elif self.radio_var.get() == 0 and self.cb_var1.get() == 0 and self.cb_var2.get() == 1:
            tkinter.messagebox.showinfo('ERROR', "Prop choice missing, but voted for Candiate C.")

        elif self.radio_var.get() == 0 and self.cb_var1.get() == 1 and self.cb_var2.get() == 1:
            tkinter.messagebox.showinfo('ERROR', "Prop missing, also can't vote both Candidates.")

        elif self.radio_var.get() == 0:
            tkinter.messagebox.showinfo('ERROR', "Prop choice missing.")
            
        

my_GUI = myGUI()
