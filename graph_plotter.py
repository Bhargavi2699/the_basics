#using matplotlib - install it
import matplotlib.pyplot as plt #plt is an instance of pyplot that we imported

#x and y axis
# x = [2, 4, 5, 6]
# y = [2, 3, 6, 7]

left = [1, 2, 3, 4, 5]
height = [10, 11, 23, 36, 4]

tick_label = ['one', 'two', 'three', 'four', 'five']

plt.bar(left, height, tick_label = tick_label, width = 0.8, color = ['blue', 'orange'])

#label = 'Line 1' - to name the line if needed
#plt.plot(x, y, color = 'green', linestyle = 'dashed', linewidth = 3, marker = 'o', markerfacecolor = 'blue', markersize = 12)
#selecting x and y ranges(1, 8)

#below lines were selecting the range of the coordinates
# plt.ylim(1, 8)
# plt.xlim(1, 8)
# x2 = [1, 2, 3, 4]
# y2 = [1, 2, 3, 4]

# plt.plot(x2, y2, label = 'Line 2')

plt.xlabel('X Axis')

plt.ylabel('Y Axis')

plt.title('Demo Graph - Bar Chart')

#legend is to use different lines for each plot
# plt.legend()

plt.show()