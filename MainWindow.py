from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QWidget, QListView, QListWidget, QSizePolicy
from PySide2.QtCharts import QtCharts
from PySide2.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QTabWidget, QLabel
from PySide2.QtGui import QPainter
from PySide2.QtCore import QObject, Qt
import random
from  statistics import mean, median, mode
import time
from PySide2.QtCore import QTimer


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.count = 0
        self.init_gui()
        self.timer = QTimer()
        self.timer.timeout.connect(self.info)
        self.timer.setInterval(1500)
        self.timer.start()


    def info(self):
        self.max += 1
        self.min += 0.1
        self.chart.axisX().setRange(self.min, self.max)
        data = random.randint(-50, 50)
        self.dat.append(data)
        self.median_m = median(self.dat)
        self.median_.setText(("Median: {0}".format(self.median_m)))
        self.mean_m = mean(self.dat)
        self.mean_.setText("Mean: {0}".format(self.mean_m))
        
        # print(self.dat)
        # print(self.count)
        self.chart.series()[0].append(self.count, data)
        # print(self.chart_view.chart().series()[0])
        self.count += 1

        self.chart.scroll(self.max, 0)

        self.chart_view.update()
        self.chart.update()

    def clicked_theme(self, item):
        print(item)
        if item == 1:
            self.chart.setTheme(QtCharts.QChart.ChartThemeDark)
            self.chart.update()
        if item == 0:
            self.chart.setTheme(QtCharts.QChart.ChartThemeLight)
            self.chart.update()
        if item == 2:
            self.chart.setTheme(QtCharts.QChart.ChartThemeBrownSand)
            self.chart.update()


    '''def clicked_statistic(self, item):
        print(item)
        if item == 0:
            pass
        if item == 1:
            pass
        if item == 2:
            pass'''

    def init_gui(self):

        self.min = 0
        self.max = 10
        self.dat = [0]
        self.median_m = int()
        self.mean_m = int()
        self.mode_m = int()

        self.mode_list = [2, -34, 14, 14, 19, 15, -14, -13, 5]

        vbox = QVBoxLayout()
        print(self.median_m)
        layout = QHBoxLayout()
        text_layout = QHBoxLayout()
        self.median_ = QLabel(("Median: {0}".format(self.median_m)))
        self.mean_ = QLabel("Mean: {0}".format(self.mean_m))
        self.mode_ = QLabel("Mode: {0}".format(mode(self.mode_list)))
        text_layout.addWidget(self.median_)
        text_layout.addWidget(self.mean_)
        text_layout.addWidget(self.mode_)

        vbox.addLayout(text_layout)

        central_widget = QWidget()
        self.chart = QtCharts.QChart()
        self.chart_view = QtCharts.QChartView()
        self.chart_view.setChart(self.chart)

        self.series = QtCharts.QLineSeries()

        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart.addSeries(self.series)

        axis_y = QtCharts.QValueAxis()
        axis_y.setTickCount(21)
        axis_y.setTickInterval(5)
        axis_y.setRange(-50, 50)
        self.chart.addAxis(axis_y, Qt.AlignLeft)

        axis_x = QtCharts.QValueAxis()
        axis_x.setTickCount(5)
        axis_x.setTickInterval(1)
        axis_x.setRange(self.min, self.max)
        self.chart.addAxis(axis_x, Qt.AlignBottom)

        self.series.attachAxis(axis_x)
        self.series.attachAxis(axis_y)
        self.series.setName("Temp")

        list_ = QListWidget()
        list_.addItem("Light theme")
        list_.addItem("Dark theme")
        list_.addItem("Sand theme")
        # list_.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        list_.currentRowChanged.connect(self.clicked_theme)

        '''statistic_list = QListWidget()
        statistic_list.addItem("Median")
        statistic_list.addItem("Mode")
        statistic_list.addItem("Mean")
        # statistic_list.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        statistic_list.currentRowChanged.connect(self.clicked_statistic)'''

        tab_widget = QTabWidget()
        tab_widget.addTab(list_, "Themes")
        # tab_widget.addTab(statistic_list, "Statistic data")
        tab_widget.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        layout.addWidget(tab_widget)

        # layout.addWidget(list_)

        vbox.addWidget(self.chart_view)

        layout.addLayout(vbox)
        central_widget.setLayout(layout)


        self.setCentralWidget(central_widget)
