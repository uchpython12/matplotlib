import sub_plots九宮格_api
import matplotlib.pyplot as plt
import matplotlib轉中文字體
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
sub_plots九宮格_api.subplots_char1(list_Label, listDate1, listy, xlabel, ylabel, title)
plt.show()
# 圖2
sub_plots九宮格_api.subplots_char2(list_Label, listDate1, listy, xlabel, ylabel, title)
plt.show()
# 圖3
sub_plots九宮格_api.subplots_char3(list_Label, listDate1, listy, xlabel, ylabel, title)
plt.show()
# 圖4
sub_plots九宮格_api.subplots_char4(list_Label, listDate1, listy, xlabel, ylabel, title)
plt.show()
# 圖5 圓餅圖
sub_plots九宮格_api.subplots_char5(list_Label, listy, title)
plt.show()
# 圖6
sub_plots九宮格_api.subplots_char6(list_Label, listy)
plt.show()
# 圖7
sub_plots九宮格_api.subplots_char7(list_Label, listy)
plt.show()
# 圖8
sub_plots九宮格_api.subplots_char8(list_Label, listDate1, listy, xlabel, ylabel, title)
plt.show()
# 圖9
sub_plots九宮格_api.subplots_char9(list_Label, listDate1, listy, xlabel, ylabel, title)
plt.show()
# 9宮格
sub_plots九宮格_api.subplots_NineCharts(list_Label, listDate1, listy, xlabel, ylabel, title)
plt.show()
