import sys

# Usage sliding_window.py <insertion_plot> <window_size>

filename = sys.argv[1]
window_size = int(sys.argv[2])

forward_insertions = list()
reverse_insertions = list()

plot_size=-1

with open(filename) as f:
    lines = f.readlines()
    plot_size=len(lines)
    for line in lines:
        insertions = line.rstrip().split(' ')
        forward_insertions.append(int(insertions[0]))
        reverse_insertions.append(int(insertions[1]))


for i in range(0,plot_size,window_size):
    forward_insertions_in_window=0
    reverse_insertions_in_window=0
    for j in range(i,min(plot_size,i+window_size)):
        forward_insertions_in_window=forward_insertions_in_window+forward_insertions[j]
        reverse_insertions_in_window=reverse_insertions_in_window+reverse_insertions[j]

    print(str(i+1) + ',' + str(i+window_size) + ',' + str(forward_insertions_in_window) + ',' + str(reverse_insertions_in_window) + ',' + str(forward_insertions_in_window+reverse_insertions_in_window))
        
