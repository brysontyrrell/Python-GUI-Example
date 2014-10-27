#!/usr/bin/python2.7
import base64
import Tkinter

# This is a base64 encoded GIF image. One neat trick with using Python to create GUIs
# is you can embed your graphics into the code so anything you want to display doesn't
# need to be pre-loaded or downloaded separately. You can only use GIFs in this way.
gifBase = '''
R0lGODlhQABAAPcAAO3t7RoaGg8PDw4ODqOho9TS1NbV1q2sraemp6alprSztRIRFBMTFw8PERERExUVFxoaHA4ODxMTFBUVFhkZGg0OFRARFxgZHx8hKxka
HxwdIhcaJhASGg4PEx0fJxARFR0eIiIjJwsNFBMWIRodKBwfKhIVHxQZKBUXHRkbIQ8QExESFRYXGhcYGxgZHBobHh8gIwwOEyMlKhMVGSAiJhMUFhscHiQl
JxETFhcZHBgaHRESExwdHhgZGRkaGh0eHiEiIicoKCUmJsPExMHCwqWmpg8QD7u8uyIiHhoaGaurqpWVlP/2Tv/yWv7uY/3nS/7jO/zkV9a3JbqcGb2eIvHN
N/3eXRwbFx4dGcumJeW9KxoYEdeqGoVpEYttEqCAFsOdHLeRGo9zFZp7GKeFG4RqGdWsKm1ZF9mxNu3HUM6cEpRzEM+hGndcD4FkE2BLD3xiFE8+DXRcFVRD
FFxJFlhHFy4lDdOtQ9+4TCciExoXDiQhGcmSD8CPEItnDKuAEJFtDsmVFdCaGG5TDltFDMWTG8uYHpJvF0k4DYxsGmVQGVA/FDktD59+K0AzEk4/GEc5Fr2Y
PCkhDkE1GDowFi0mFDgwHBUTDhcVECspJLqHD6Z6FaV9IcybKltFE5BvJEs6FGBLGjMoDolrJ5h4LaiGN0k6GSQdDjUsFx8aDyEeF0c1Eo9wL2pTJHxiLVVD
IIltNUY5HjIpFikmIBwaFl5JIU4+ISokGRMRDxUTERcVExEQDxMSEScmJRoZGdbV1bOysuzs7Orq6unp6eHh4dra2tbW1tXV1dTU1NPT09HR0c7OzsvLy8nJ
ycbGxr6+vry8vLu7u7q6uri4uLe3t7W1ta+vr6ioqKWlpaSkpKOjo6KioqCgoJ2dnZmZmY+Pj35+fnl5eXV1dXJycm9vb2xsbGpqamRkZFpaWllZWSoqKiYm
JiUlJSQkJCIiIiEhIR8fHx4eHhwcHBsbGxcXFxYWFhUVFRMTExISEhEREQwMDAsLCwkJCQcHBwUFBf///yH5BAEAAP8ALAAAAABAAEAAAAj/AAEIHEiwoMGD
CBMqXMiwocOHECNKnEixosWLGDNq3HgwGLFm0EKKHEmypMmTKFNCI1IsmMBg0pZwm8lt27Zs2BBcu6bkwAFr1oApoEZt2jRp0kY+C3kEqbRpRKspAAb0gJKd
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
''' 

# Our GUI is going to be made into a class. If you're writing something simpler you can
# do without the class structure.
class App:
    def __init__(self):
        # This first line initializes our GUI.
        self.root = Tkinter.Tk()
        
        # This line will force our window on top of all other windows and remain there.
        self.root.call('wm', 'attributes', '.', '-topmost', True)
        
        # The title in our title bar.
        self.root.title("Log Uploader")
        
        # This gray will help our GUI look like a part of OS X. Here we will set the
        # overall background to this color. For each of the widgets below we will be
        # setting their background colors to match as well.
        bgColor = "#EDEDED"
        self.root.configure(bg=bgColor)
        
        # This dictionary will be an attribute for our GUI class. We'll use it for
        # capturing the integer values from the Checkbuttons below.
        self.Values = {}
        
        # Here we are loading our base64 image data and placing it in our window using
        # the Label widget.  You will also see the grid method. There are three styles
        # of window management in Tkinter. Using grid allows us to place widgets according
        # to X,Y coordinates which makes designing your GUI as easy as plotting it out on
        # a sheet paper before writing your code.
        gif = Tkinter.PhotoImage(data = gifBase)
        displayGif = Tkinter.Label(self.root, image = gif, borderwidth = 10, bg = bgColor).grid(row = 0, rowspan = 6, columnspan = 2)
        
        # This Label widget displays text. I've defined the font and size I want it
        # displayed. I'm also using additional parameters to add padding around the widget
        # and its alignment within the grid space.
        Tkinter.Label(self.root, text = "Select the logs you wish to upload:", font=("Helvetica Neue Bold", 14), bg = bgColor).grid(row = 0, column = 2, columnspan = 3, padx = (0, 10), pady = (10, 5), sticky = 'w')
        
        # IntVar is a type of Tkinter variable. Tkinter widgets cannot interact with the
        # standard Python variables. Here we are storing the variables for each of our
        # Checkbuttons (which return a 0 or a 1).
        self.Values['BoxSync'] = Tkinter.IntVar()
        
        # In the Checkbutton widget I've set its variable to be equal to the IntVar I
        # created in the line above. This means the value of this variable will change
        # based upon the state of the Checkbutton.
        Tkinter.Checkbutton(self.root, text = "Box Sync", font=("Helvetica Neue", 14), variable = self.Values['BoxSync'], bg = bgColor).grid(row = 1, column = 2, sticky = 'w')
        
        self.Values['CrashPlan'] = Tkinter.IntVar()
        Tkinter.Checkbutton(self.root, text = "CrashPlan PROe", font=("Helvetica Neue", 14), variable = self.Values['CrashPlan'], bg = bgColor).grid(row = 1, column = 3, columnspan = 2, padx = (0, 10), sticky = 'w')
        
        self.Values['HipChat'] = Tkinter.IntVar()
        Tkinter.Checkbutton(self.root, text = "HipChat", font=("Helvetica Neue", 14), variable = self.Values['HipChat'], bg = bgColor).grid(row = 2, column = 2, sticky = 'w')
        self.Values['Install'] = Tkinter.IntVar()
        Tkinter.Checkbutton(self.root, text = "Install Logs", font=("Helvetica Neue", 14), variable = self.Values['Install'], bg = bgColor).grid(row = 2, column = 3, columnspan = 2, padx = (0, 10), sticky = 'w')
        
        self.Values['System'] = Tkinter.IntVar()
        Tkinter.Checkbutton(self.root, text = "System", font=("Helvetica Neue", 14), variable = self.Values['System'], bg = bgColor).grid(row = 3, column = 2, sticky = 'w')
        
        Tkinter.Label(self.root, text = "Are you updating an existing ticket?", font=("Helvetica Neue Bold", 14), bg = bgColor).grid(row = 4, column = 2, columnspan = 4, padx = 10, sticky = 'w')
        Tkinter.Label(self.root, text = "Ticket Number:", font=("Helvetica Neue", 14), bg = bgColor).grid(row = 5, column = 2, padx = 10, sticky = 'w')
        
        # Just like out Checkbuttons, we will be setting a StringVar to populate the value
        # for our Entry box.
        self.TicketNumber = Tkinter.StringVar()
        Tkinter.Entry(self.root, textvariable = self.TicketNumber, justify = 'right', width = 10, font=("Helvetica Neue", 14), highlightbackground = bgColor).grid(row = 5, column = 3, columnspan = 2, sticky = 'w')
        
        Tkinter.Label(self.root, text = "Add a comment:", font=("Helvetica Neue Bold", 14), bg = bgColor).grid(row = 6, column = 1, columnspan = 4, padx = 10, sticky = 'w')
        
        # Think of the Frame widget just as the HTML equivalent. We are defining an area
        # of our GUI window to populate widgets into. In this case I am using a Frame to
        # embed a Comment widget into. Without the Frame the Comment fills the window
        # edge to edge and is less attractive.
        Frame1 = Tkinter.Frame(self.root, borderwidth = 1, relief = 'sunken')
        
        # The Comment widget is a multi-line text input field. Here you see I am setting
        # the parent to Frame1 and not self.root and also using the pack method. Pack
        # will draw a widget in the center of the parent. While it is usually not a good
        # practice to mix different window manager methods it makes sense here as I am
        # populating a single widget into a frame that will be occupying an area of my
        # grid layout.
        self.Comment = Tkinter.Text(Frame1, width = 60, height = 5, highlightbackground = bgColor, highlightcolor = "#7BAEDC", wrap = Tkinter.WORD, font=("Helvetica Neue", 12))
        self.Comment.pack()
        
        # The Frame is placed only after all widgets have been added to it.
        Frame1.grid(row = 7, column = 1, columnspan = 5, padx = 5)
        
        # The two buttons for triggering actions in our GUI will be drawn in the lower-
        # right of the windows just like any other OS X GUi. Instead of a variable we are
        # setting a command to execute when clicked. For both buttons we are calling
        # functions that are defined below.
        Tkinter.Button(self.root, text = "Exit", highlightbackground = bgColor, command = self.Exit).grid(row = 8, column = 3, pady = (5, 5), sticky = 'e')
        Tkinter.Button(self.root, text = "Submit", highlightbackground = bgColor, command = self.Submit).grid(row = 8, column = 4, pady = (5, 5), sticky = 'e')
        
        # The below code is a workaround that allows us to determine the window size in
        # pixels and then position the window wherever we want before drawing it.
        self.root.withdraw()
        self.root.update_idletasks()
        
        # These lines will position this window in the middle of the screen horizontally
        # and two thirds of the way up vertically (a position I prefer as it is a little
        # more catching to the eye and exact centering)
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 3
        self.root.geometry("+{0}+{1}".format(x, y))
        
        # This will prevent the user from resizing the window. Useful when you want to
        # be in control of your GUI's appearance.
        self.root.resizable(False,False)
        
        # We will now draw the window by calling the mainloop method.
        # In some cases you may want to have the mainloop method be called outside of
        # your GUI's class and within a main function.
        self.root.deiconify()
        self.root.mainloop()
        
    def Exit(self):
        # Calling the destroy() method on our GUI will close it.
        self.root.destroy()
        
    def Submit(self):
        # Here you would write your code to take action upon the user input collected.
        # In this example you can look at the Terminal to see output based upon input
        # and selections made.
        print("The user clicked the 'Submit' button.")
        for key, value in self.Values.iteritems():
            if key == 'BoxSync' and value.get():
                print("The user selected 'Box Sync' logs.")
                
            if key == 'CrashPlan' and value.get():
                print("The user selected 'CrashPlan PROe' logs.")
                
            if key == 'HipChat' and value.get():
                print("The user selected 'HipChat' logs.")
            
            if key == 'Install' and value.get():
                print("The user selected 'Install' logs.")
                
            if key == 'System' and value.get():
                print("The user selected 'System' logs.")
                
        if self.TicketNumber.get():
            print("The user entered a ticket number: {0}".format(self.TicketNumber.get()))
                
        # A Tkinter Comment is different from an Entry box. The code below will read all
        # characters from the first to the last. There are a lot of advanced options for
        # reading input from a Comment making it a very versatile means of user input.
        TextField = self.Comment.get('1.0', 'end')
        if TextField.rstrip():
            print("The user entered the following comment:\n\n{0}".format(TextField))

    	
# Calling the class will execute our GUI.
App()