# importing required libraries 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtWebEngineWidgets import * 
from PyQt5.QtPrintSupport import * 
import os 
import sys

data = []


class Repositorios:
    productosList = dict()


class ProductoService:

    # Devuelve repositorio productoList
    def get_productosList(self):
        return Repositorios.productosList

    # parametros : Object producto
    # return: Key id
    def add_data(self, producto):
        lastKey = -1
        for key in Repositorios.productosList:
            lastKey = key
        id_new = int(lastKey) + 1
        Repositorios.productosList[id_new] = producto.__dict__
        return id_new


class Producto():

    def __init__(self, name=' ', descripcion=0):
        self.name = name
        self.descripcion = descripcion
        
    # ----- Nombre -----
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # ----- Descripcion -----
    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value


class Editar():

    # Agregar un producto
    def add_data(self, name, descr):
        producto = Producto(name, descr)
        ProductoService().add_data(producto)
        


# creating main window class 
class MainWindow(QMainWindow): 
  
    # constructor 
    def __init__(self, opacidad=0.5, *args, **kwargs):
        self.opacidad = opacidad 
        super(MainWindow, self).__init__(*args, **kwargs) 


        a = ""
        
        b = -1

        for x in Repositorios.productosList:
            print(x)
            b = b + 1
            
            a = a + f"""<li class="hex">
                            <div class="hexIn">
                            <a class="hexLink" href="#">
                                <img style="opacity: {self.opacidad};" src="https://media.giphy.com/media/l1J9EfOdAtsftvhWU/giphy.gif" alt="" />
                                <h1>{x['name']}</h1>
                                <p>{x['descripcion']}</p>
                            </a>
                            </div>
                        </li>"""


        f = open("index.html", "w")
        f.write(f"""
        <!doctype html>
        <html>
        <head>
            <meta charset="utf-8">
            <title></title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" type="text/css" href="main.css">
            <link href='https://fonts.googleapis.com/css?family=Raleway:300' rel='stylesheet' type='text/css'>
        </head>
        <body style="background-color: black;">
            <ul id="hexGrid">
            {a}
            </ul>
        </body>
        </html>
        """)
        f.close()

       
       
        # creating a QWebEngineView 
        self.browser = QWebEngineView()

        width = 1000
          
        # setting  the fixed width of window 
        self.setFixedWidth(width)

        height = 1000

        self.setFixedHeight(height)

     

        url = os.getcwd()
  
        # setting default browser url as google 
        self.browser.setUrl(QUrl("http://localhost:8080")) 
  
        # adding action when url get changed 
        self.browser.urlChanged.connect(self.update_urlbar) 
  
        # adding action when loading is finished 
        self.browser.loadFinished.connect(self.update_title) 
  
        # set this browser as central widget or main window 
        self.setCentralWidget(self.browser) 
        
        # creating a status bar object 
        self.status = QStatusBar() 
  
        # adding status bar to the main window 
        self.setStatusBar(self.status) 
  
        # creating QToolBar for navigation 
        navtb = QToolBar("Navigation") 
  
        # adding this tool bar tot he main window 
        self.addToolBar(navtb) 
  
        # adding actions to the tool bar 
        # creating a action for back 
        back_btn = QAction("Back", self) 
  
        # setting status tip 
        back_btn.setStatusTip("Back to previous page") 
  
        # adding action to the back button 
        # making browser go back 
        back_btn.triggered.connect(self.browser.back) 
  
        # adding this action to tool bar 
        navtb.addAction(back_btn) 
  
        # similarly for forward action 
        next_btn = QAction("Forward", self) 
        next_btn.setStatusTip("Forward to next page") 
  
        # adding action to the next button 
        # making browser go forward 
        next_btn.triggered.connect(self.browser.forward) 
        navtb.addAction(next_btn) 
  
        # similarly for reload action 
        reload_btn = QAction("Reload", self) 
        reload_btn.setStatusTip("Reload page") 
  
        # adding action to the reload button 
        # making browser to reload 
        reload_btn.triggered.connect(self.browser.reload) 
        navtb.addAction(reload_btn) 
  
        # similarly for home action 
        home_btn = QAction("Home", self) 
        home_btn.setStatusTip("Go home") 
        home_btn.triggered.connect(self.navigate_home) 
        navtb.addAction(home_btn) 
  
        # adding a separator in the tool bar 
        navtb.addSeparator() 
  
        # creating a line edit for the url 
        self.urlbar = QLineEdit() 
  
        # adding action when return key is pressed 
        self.urlbar.returnPressed.connect(self.navigate_to_url) 
  
        # adding this to the tool bar 
        navtb.addWidget(self.urlbar) 
  
        # adding stop action to the tool bar 
        stop_btn = QAction("Stop", self) 
        stop_btn.setStatusTip("Stop loading current page") 
  
        # adding action to the stop button 
        # making browser to stop 
        stop_btn.triggered.connect(self.browser.stop) 
        navtb.addAction(stop_btn) 
        
        # showing all the components 
        self.show()  
  
  
    # method for updating the title of the window 
    def update_title(self): 
        title = self.browser.page().title() 
        self.setWindowTitle("UnitTest Visual App") 
  
    # method called by the home action 
    def navigate_home(self): 
  
        # open the google 
        self.browser.setUrl(QUrl("http://localhost:8080")) 
  
    # method called by the line edit when return key is pressed 
    def navigate_to_url(self): 
  
        # getting url and converting it to QUrl objetc 
        q = QUrl(self.urlbar.text()) 
  
        # if url is scheme is blank 
        if q.scheme() == "": 
            # set url scheme to html 
            q.setScheme("http") 
  
        # set the url to the browser 
        self.browser.setUrl(q) 
  
    # method for updating url 
    # this method is called by the QWebEngineView object 
    def update_urlbar(self, q): 
  
        # setting text to the url bar 
        self.urlbar.setText(q.toString()) 
  
        # setting cursor position of the url bar 
        self.urlbar.setCursorPosition(0) 
  


def start_window():

    # creating a pyQt5 application 
    app = QApplication(sys.argv) 

    # setting name to the application 
    app.setApplicationName("UnitTest Visual App") 
    # creating a main window object 
    window = MainWindow() 
    app.exec_() 





