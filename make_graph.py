# python -m pip install -U pip setuptools
# python -m pip install matplotlib
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import math

class MakeGraph:
    def __init__(self, x_vals=[], y_vals=[],x_label='',y_label='', title='',colors=[]):
        self._figure_num=0
        self._barlist = []
        if x_label and x_vals and y_label and y_vals:
            self.draw_figure(x_vals,y_vals,x_label,y_label,title, colors)


    def draw_figure(self,x_vals=[], y_vals=[],x_label='',y_label='',title='',colors=[]):
        self._figure_num+=1
        list = []
        colors = self.copy_colors(colors)
        for i in range(len(x_vals)):
            list.append([x_vals[i],y_vals[i],colors[i]])
        list.sort(key = lambda x: x[1])
        
        for i in range(len(list)):
            x_vals[i]=list[i][0]
            y_vals[i]=list[i][1]
            colors[i]=list[i][2]
        plt.figure(self._figure_num)
        y_pos = np.arange(len(x_vals))
        plt.ylim(0,max(y_vals)+0.2)
        
        self._barlist = plt.bar(y_pos, y_vals, align='center', alpha=0.5)
        
        for a in range(len(x_vals)):
            self._barlist[a].set_color(colors[a])
        plt.xticks(y_pos, x_vals, rotation=90)
        plt.ylabel(y_label)
        plt.xlabel(x_label)
        plt.title(title)
        plt.subplots_adjust(bottom=0.40)
    
    def draw_figure_no_sort(self,x_vals=[], y_vals=[],x_label='',y_label='',title='',colors=[], height=0):
        self._figure_num+=1
        
        plt.figure(self._figure_num)
        y_pos = np.arange(len(x_vals))
        plt.ylim(0,y_vals[-1]+1)
        if (height != 0):
            plt.ylim (0,height)
        else:
            plt.ylim (0, max(y_vals)+0.2)
        
        self._barlist = plt.bar(y_pos, y_vals, align='center', alpha=0.5)
        
        for a in range(len(x_vals)):
            self._barlist[a].set_color(colors[a])
        plt.xticks(y_pos, x_vals, rotation=90)
        plt.ylabel(y_label)
        plt.xlabel(x_label)
        plt.title(title)
        plt.subplots_adjust(bottom=0.40)
    
    
    
    def show_plts(self):
        plt.show()

    def copy_colors (self, colors):
        newcolor = []
        for color in colors:
            newcolor.append (color)
        return newcolor
