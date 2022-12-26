import plots_九宮格_api
import matplotlib轉中文字體
import matplotlib.pyplot as plt
matplotlib轉中文字體.pyplot_中文()

listy = [[2578,2454,2268,2357,1918,2847],
         [2821,2718,2710,2626,1590,1822],
         [627,556,661,606,550,709]]


listDate1 = [713, 714, 715, 716, 717, 718]

list_Label=['物件1', '物件2', '物件3']
title="標題"
xlabel='x軸標籤'
ylabel= 'y軸標籤'

# 圖1
plots_九宮格_api.char1(list_Label, listDate1, listy, title, ylabel, xlabel)
plt.show()
#圖2
plots_九宮格_api.char2(list_Label, listDate1, listy, title, ylabel, xlabel)
plt.show()
#圖3
plots_九宮格_api.char3(list_Label, listDate1, listy, xlabel, ylabel, title)
plt.show()
#圖4
plots_九宮格_api.char4(list_Label, listDate1, listy, xlabel, ylabel, title)
plt.show()
#圖5
plots_九宮格_api.char5(list_Label, listDate1, listy, xlabel, ylabel, title)
plt.show()
#圖6
plots_九宮格_api.char6(list_Label, listDate1, listy, xlabel, ylabel, title)
plt.show()
#圖7
plots_九宮格_api.char7(list_Label, listDate1, listy, xlabel, ylabel, title)
plt.show()
#圖8
plots_九宮格_api.char8(list_Label, listDate1, listy, xlabel, ylabel, title)
plt.show()
#圖9
plots_九宮格_api.char9(list_Label, listDate1, listy, xlabel, ylabel, title)
plt.show()
# 9宮格
plots_九宮格_api.NineCharts(list_Label, listDate1, listy, ylabel, xlabel, title)
plt.show()



