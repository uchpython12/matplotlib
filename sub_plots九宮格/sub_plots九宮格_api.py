import io
import matplotlib.pyplot as plt # 匯入matplotlib 的pyplot 類別，並設定為plt
import xml.etree.ElementTree as ET
from matplotlib.patches import Shadow
from matplotlib.patches import ConnectionPatch
import numpy as np

def hat_graph(ax, xlabels, values, group_labels):
    """
    Create a hat graph.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The Axes to plot into.
    xlabels : list of str
        The category names to be displayed on the x-axis.
    values : (M, N) array-like
        The data values.
        Rows are the groups (len(group_labels) == M).
        Columns are the categories (len(xlabels) == N).
    group_labels : list of str
        The group labels displayed in the legend.
    """

    def label_bars(heights, rects):
        """Attach a text label on top of each bar."""
        for height, rect in zip(heights, rects):
            ax.annotate(f'{height}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 4),  # 4 points vertical offset.
                        textcoords='offset points',
                        ha='center', va='bottom')

    values = np.asarray(values)
    x = np.arange(values.shape[1])
    ax.set_xticks(x, labels=xlabels)
    spacing = 0.3  # spacing between hat groups
    width = (1 - spacing) / values.shape[0]
    heights0 = values[0]
    for i, (heights, group_label) in enumerate(zip(values, group_labels)):
        style = {'fill': False} if i == 0 else {'edgecolor': 'black'}
        rects = ax.bar(x - spacing/2 + i * width, heights - heights0,
                       width, bottom=heights0, label=group_label, **style)
        label_bars(heights, rects)


# 圖1
def subplots_char1(list_Label,listDate1, listy, xlabel, ylabel, title, ax=None):
    if ax is None:
        fig, ax = plt.subplots()  # 建立圖表 畫面分割成1個
    ax.plot(listDate1, listy[0], "ro",label=list_Label[0])
    ax.plot(listDate1, listy[1], "bo",label=list_Label[1])
    ax.plot(listDate1, listy[2], "go",label=list_Label[2])
    plt.legend(loc='upper right')  # 在右上角顯示標籤
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)


# 圖2
def subplots_char2(list_Label,listDate1,listy,xlabel,ylabel,title, ax=None):
    if ax is None:
        fig, ax = plt.subplots()  # 建立圖表 畫面分割成1個
    ax.plot(listDate1, listy[0], "r--",label=list_Label[0])
    ax.plot(listDate1, listy[1], "g--",label=list_Label[1])
    ax.plot(listDate1, listy[2], "b--",label=list_Label[2])
    plt.legend(loc='upper right')  # 在右上角顯示標籤
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)


# 圖三
def subplots_char3(list_Label,listDate1,listy,xlabel,ylabel,title, ax=None):
    xlabels = listDate1
    listy1 = np.array(listy[0])
    listy2 = np.array(listy[1])
    listy3 = np.array(listy[2])
    if ax is None:
        fig, ax = plt.subplots()
    hat_graph(ax, xlabels, [listy1, listy2, listy3], [list_Label[0], list_Label[1], list_Label[2]])

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_ylim(0, 3000)
    ax.set_title(title)
    ax.legend()


# 圖四
def subplots_char4(list_Label,listDate1,listy,xlabel,ylabel,title, ax=None):
    vegetables = list_Label
    farmers = listDate1

    harvest = np.array([listy[0], listy[1], listy[2]])

    ax輸入為空 = None
    if ax is None:
        fig, ax = plt.subplots()
        ax輸入為空 = True
    else:
        ax輸入為空 = False
    im = ax.imshow(harvest)

    # Show all ticks and label them with the respective list entries
    ax.set_xticks(np.arange(len(farmers)), labels=farmers)
    ax.set_yticks(np.arange(len(vegetables)), labels=vegetables)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(len(vegetables)):
        for j in range(len(farmers)):
            text = ax.text(j, i, harvest[i, j],
                           ha="center", va="center", color="r")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    if ax輸入為空 == True:
        fig.tight_layout()


# 圖五 圓餅圖
def subplots_char5(list_Label,listy,title, ax=None):
    if ax is not None:
        ax.plot(listy[0])
    else:
        fig = plt.figure(figsize=(6, 6))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

        labels = list_Label
        fracs = [listy[0][0], listy[0][1], listy[0][2]]

        explode = (0, 0.05, 0)

        # We want to draw the shadow for each pie but we will not use "shadow"
        # option as it doesn't save the references to the shadow patches.
        pies = ax.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%')

        for w in pies[0]:
            # set the id with the label.
            w.set_gid(w.get_label())

            # we don't want to draw the edge of the pie
            w.set_edgecolor("none")

        for w in pies[0]:
            # create shadow patch
            s = Shadow(w, -0.01, -0.01)
            s.set_gid(w.get_gid() + "_shadow")
            s.set_zorder(w.get_zorder() - 0.1)
            ax.add_patch(s)

        # save
        f = io.BytesIO()
        plt.savefig(f, format="svg")

        # Filter definition for shadow using a gaussian blur and lighting effect.
        # The lighting filter is copied from http://www.w3.org/TR/SVG/filters.html

        # I tested it with Inkscape and Firefox3. "Gaussian blur" is supported
        # in both, but the lighting effect only in Inkscape. Also note
        # that, Inkscape's exporting also may not support it.

        filter_def = """
          <defs xmlns='http://www.w3.org/2000/svg'
                xmlns:xlink='http://www.w3.org/1999/xlink'>
            <filter id='dropshadow' height='1.2' width='1.2'>
              <feGaussianBlur result='blur' stdDeviation='2'/>
            </filter>

            <filter id='MyFilter' filterUnits='objectBoundingBox'
                    x='0' y='0' width='1' height='1'>
              <feGaussianBlur in='SourceAlpha' stdDeviation='4%' result='blur'/>
              <feOffset in='blur' dx='4%' dy='4%' result='offsetBlur'/>
              <feSpecularLighting in='blur' surfaceScale='5' specularConstant='.75'
                   specularExponent='20' lighting-color='#bbbbbb' result='specOut'>
                <fePointLight x='-5000%' y='-10000%' z='20000%'/>
              </feSpecularLighting>
              <feComposite in='specOut' in2='SourceAlpha'
                           operator='in' result='specOut'/>
              <feComposite in='SourceGraphic' in2='specOut' operator='arithmetic'
            k1='0' k2='1' k3='1' k4='0'/>
            </filter>
          </defs>
        """

        tree, xmlid = ET.XMLID(f.getvalue())

        # insert the filter definition in the svg dom tree.
        tree.insert(0, ET.XML(filter_def))

        for i, pie_name in enumerate(labels):
            pie = xmlid[pie_name]
            pie.set("filter", 'url(#MyFilter)')

            shadow = xmlid[pie_name + "_shadow"]
            shadow.set("filter", 'url(#dropshadow)')

        fn = "svg_filter_pie.svg"
        print(f"Saving '{fn}'")
        ET.ElementTree(tree).write(fn)
    ax.set_title(title)


# 圖六
def subplots_char6(list_Label, listy, ax=None):
    # Some data
    labels = list_Label[0]
    fracs = [listy[0][0], listy[0][1], listy[0][2]]

    # Make figure and axes
    if ax is None:
        fig, axs = plt.subplots(2, 2)
        ax1 = axs[0, 0]
        ax2 = axs[0, 1]
        ax3 = axs[1, 0]
        ax4 = axs[1, 1]
    else:
        ax1 = ax
        ax2 = None
        ax3 = None
        ax4 = None

    # A standard pie plot
    ax1.pie(fracs, labels=labels, autopct='%1.1f%%', shadow=True)

    # Shift the second slice using explode
    if ax2 is not None:
        ax2.pie(fracs, labels=labels, autopct='%.0f%%', shadow=True,
                explode=(0, 0.1, 0))

    # Adapt radius and text size for a smaller pie
    if ax3 is not None:
        patches, texts, autotexts = ax3.pie(fracs, labels=labels,
                                            autopct='%.0f%%',
                                            textprops={'size': 'smaller'},
                                            shadow=True, radius=0.5)
        # Make percent texts even smaller
        plt.setp(autotexts, size='x-small')
        autotexts[0].set_color('white')

    # Use a smaller explode and turn of the shadow for better visibility
    if ax4 is not None:
        patches, texts, autotexts = ax4.pie(fracs, labels=labels,
                                            autopct='%.0f%%',
                                            textprops={'size': 'smaller'},
                                            shadow=False, radius=0.5,
                                            explode=(0, 0.05, 0))
        plt.setp(autotexts, size='x-small')
        autotexts[0].set_color('white')


# 圖七
def subplots_char7(list_Label, listy, ax=None):
    # make figure and assign axis objects
    if ax is None:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
        fig.subplots_adjust(wspace=0)
    else:
        ax1 = ax
        ax2 = None

    # pie chart parameters
    overall_ratios = [listy[0][0], listy[0][1], listy[0][2]]
    labels = list_Label[0]
    explode = [0.1, 0, 0]
    # rotate so that first wedge is split by the x-axis
    angle = -180 * overall_ratios[0]
    wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle,
                         labels=labels, explode=explode)

    # bar chart parameters
    age_ratios = [.33, .54, .07, .06]
    age_labels = ['Under 35', '35-49', '50-65', 'Over 65']
    bottom = 1
    width = .2

    # Adding from the top matches the legend.
    if ax2 is not None:
        for j, (height, label) in enumerate(reversed([*zip(age_ratios, age_labels)])):
            bottom -= height
            bc = ax2.bar(0, height, width, bottom=bottom, color='C0', label=label,
                         alpha=0.1 + 0.25 * j)
            ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type='center')

        ax2.set_title('Age of approvers')
        ax2.legend()
        ax2.axis('off')
        ax2.set_xlim(- 2.5 * width, 2.5 * width)

        # use ConnectionPatch to draw lines between the two plots
        theta1, theta2 = wedges[0].theta1, wedges[0].theta2
        center, r = wedges[0].center, wedges[0].r
        bar_height = sum(age_ratios)

        # draw top connecting line
        x = r * np.cos(np.pi / 180 * theta2) + center[0]
        y = r * np.sin(np.pi / 180 * theta2) + center[1]
        con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData,
                              xyB=(x, y), coordsB=ax1.transData)
        con.set_color([0, 0, 0])
        con.set_linewidth(4)
        ax2.add_artist(con)

        # draw bottom connecting line
        x = r * np.cos(np.pi / 180 * theta1) + center[0]
        y = r * np.sin(np.pi / 180 * theta1) + center[1]
        con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData,
                              xyB=(x, y), coordsB=ax1.transData)
        con.set_color([0, 0, 0])
        ax2.add_artist(con)
        con.set_linewidth(4)


# 圖八
def subplots_char8(list_Label,listDate1,listy,xlabel,ylabel,title, ax=None):
    if ax is None:
        fig, ax = plt.subplots()  # 建立圖表 畫面分割成1個

    x = listDate1
    y1 = listy[0]
    ax.bar(x, y1,
           alpha=0.5,
           width=1, edgecolor="black",
           linewidth=0.7, label=list_Label[0]
           )

    ax.legend(loc='upper right')  # 在右上角顯示標籤
    # ax.xlabel(xlabel)
    # ax.ylabel(ylabel)
    # ax.title(title)


# 圖9
def subplots_char9(list_Label,listDate1,listy,xlabel,ylabel,title, ax=None):
    if ax is None:
        fig, ax = plt.subplots()  # 建立圖表 畫面分割成1個
    ax.plot(listDate1, listy[0])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

# 九宮格
def subplots_NineCharts(list_Label,listDate1,listy,xlabel,ylabel,title):

    fig, ax = plt.subplots(3,3)  # 建立圖表 畫面分割成1個
    subplots_char1(list_Label,listDate1,listy,xlabel,ylabel,title,ax[0,0])
    subplots_char2(list_Label,listDate1,listy,xlabel,ylabel,title,ax[0,1])
    subplots_char3(list_Label,listDate1,listy,xlabel,ylabel,title,ax[0,2])
    subplots_char4(list_Label,listDate1,listy,xlabel,ylabel,title,ax[1,0])
    subplots_char5(list_Label,listy,title,ax[1,1])
    subplots_char6(list_Label, listy,ax[1,2])
    subplots_char7(list_Label, listy,ax[2,0])
    subplots_char8(list_Label,listDate1,listy,xlabel,ylabel,title,ax[2,1])
    subplots_char9(list_Label,listDate1,listy,xlabel,ylabel,title,ax[2,2])