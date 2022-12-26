import matplotlib.pyplot as plt # 匯入matplotlib 的pyplot 類別，並設定為plt
#圖一
def char1(list_Label,listDate1,listy, title, xlabel, ylabel):
    plt.plot(listDate1, listy[0], "y--",label=list_Label[0])  # 建立圖表 x軸listDate1 y軸listy[0]
    plt.plot(listDate1, listy[1], "rp--", label=list_Label[1])  # 建立圖表 x軸 listDate1y軸listy[1]
    plt.plot(listDate1, listy[2], "cd--",label=list_Label[2])  # 建立圖表 x軸 listDate1y軸listy[2]
    plt.legend(loc='upper right')  # 在右上角顯示標籤
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig("chart_1.jpg")  # 保存圖片

# 圖二
def char2(list_Label,listDate1, listy, title, ylabel, xlabel):
    x = listDate1
    y1 = listy[0]
    max = 3
    plt.bar(x, y1,
            alpha=0.5,
            width=1 / max, edgecolor="black",
            linewidth=0.7, label=list_Label[0]
            )
    x2 = [i + (1 / max) for i in x]
    y2 = listy[1]
    plt.bar(x2, y2,
            alpha=0.5,
            width=1 / max, edgecolor="white",
            linewidth=0.7, label=list_Label[1])
    x3 = [i + (2 / max) for i in x]
    y3 = listy[2]
    plt.bar(x3, y3,
            alpha=0.5,
            width=1 / max, edgecolor="red",
            linewidth=0.7, label=list_Label[2])
    plt.legend(loc='upper right')  # 在右上角顯示標籤
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig("chart_2.jpg")


# 圖三
def char3(list_Label, listDate1,listy, xlabel, ylabel, title):
    plt.plot(listDate1, listy[0], "go", label=list_Label[0])
    plt.plot(listDate1, listy[1], "r_", label=list_Label[1])
    plt.plot(listDate1, listy[2], "y-", label=list_Label[2])
    plt.legend()  # 自動改變顯示的位置

    plt.title(title)
    plt.xlabel(xlabel)  # 顯示Y 座標的文字
    plt.ylabel(ylabel)  # 顯示Y 座標的文字

    plt.savefig("chart_3.jpg")


# 圖四
def char4(list_Label,x, y, xlabel, ylabel, title):
    list1 = ['ro', "go", "bo", "r-", "g-", "b-"]
    i = 0
    for y2 in y:
        plt.plot(x, y2, list1[i])
        i = i + 1

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=-90, fontsize=8)
    plt.savefig("chart_4.jpg")

# 圖五
def char5(list_Label,x, y, xlabel, ylabel, title):
    plt.bar(x, y[0], width=1,
            color="blue",  # 顏色 #ff0000 rgb 三原色
            alpha=0.9,  # 透明度
            edgecolor="white", linewidth=0.7)
    plt.xlabel(xlabel[0])
    plt.ylabel(ylabel[0])
    plt.title(title[0])
    plt.xticks(rotation=-90, fontsize=8)
    plt.savefig("chart_5.jpg")

# 圖六
def char6(list_Label,x, y, xlabel, ylabel, title):
    plt.plot(x, y[0], 'b|')
    plt.xlabel(xlabel[0])
    plt.ylabel(ylabel[0])
    plt.title(title[0])
    plt.xticks(rotation=-90, fontsize=8)
    plt.savefig("chart_6.jpg")

# 圖七
def char7(list_Label,x, y, xlabel, ylabel, title):
    plt.pie(y[0], labels=x,
            radius=1,  # 半徑
            center=(4, 4),  # 中心點
            wedgeprops={"linewidth": 1,
                        "edgecolor": "white"},
            frame=True)

    plt.xlabel(xlabel[0])
    plt.ylabel(xlabel[0])
    plt.title(title[0])
    plt.xticks(rotation=-90, fontsize=8)
    plt.savefig("chart_7.jpg")

# 圖八
def char8(list_Label,x, y, xlabel, ylabel, title):
    plt.plot(x, y[0], "r--")

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=-90, fontsize=8)
    plt.savefig("chart_8.jpg")

# 圖九
def char9(list_Label,x, y, xlabel, ylabel, title):
    plt.plot(x, y[0], "r*")

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=-90, fontsize=8)
    plt.savefig("chart_9.jpg")


#九宮格
def NineCharts(list_Label, listDate1, listy, ylabel, xlabel, title):

    plt.subplot(3,3,1) #, facecolor='y')
    char1(list_Label,listDate1,listy, title, ylabel, xlabel)
    plt.subplot(3,3,2)
    char2(list_Label,listDate1, listy, title, ylabel, xlabel)
    plt.subplot(3,3,3)
    char3(list_Label, listDate1,listy, xlabel, ylabel, title)
    plt.subplot(3, 3, 4)
    char4(list_Label,listDate1,listy, xlabel, ylabel, title)
    plt.subplot(3, 3, 5)
    char5(list_Label,listDate1,listy, xlabel, ylabel, title)
    plt.subplot(3, 3, 6)
    char6(list_Label,listDate1,listy, xlabel, ylabel, title)
    plt.subplot(3, 3, 7)
    char7(list_Label,listDate1,listy, xlabel, ylabel, title)
    plt.subplot(3, 3, 8)
    char8(list_Label,listDate1,listy, xlabel, ylabel, title)
    plt.subplot(3, 3, 9)
    char9(list_Label,listDate1,listy, xlabel, ylabel, title)
