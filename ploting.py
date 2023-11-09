import matplotlib.pyplot as plt

# Sample data for the first line graph (MD5)
md5_x = [10, 20, 30, 50, 80, 100]
md5_y = [0.29, 1.26, 3.36, 10.87, 16.39, 24.28]

# Sample data for the second line graph (SHA)
sha1_x = [10, 20, 30, 50, 80, 100]
sha1_y = [0.64, 5.61, 7.95, 24.00, 47.25, 49.21]

# Plot the first line graph
plt.plot(md5_x, md5_y, label='md5', color='blue', marker='s')

# Plot the second line graph
plt.plot(sha1_x, sha1_y, label='sha-1', color='red', marker='^')

# Add labels and a legend
plt.xlabel('Number of members')
plt.ylabel('Time required')
plt.title('Comparing joining time taken by md5 and sha1')
plt.legend()

# Show the plot
plt.show()





