import matplotlib.pyplot as plt

accuracy_lenet5 = [
0.8767,
0.9147,
0.933,
0.9455,
0.9511,
0.9548,
0.9592,
0.9614,
0.9638,
0.9668,
0.9682,
0.9705,
0.9713,
0.9722,
0.9728,
0.9736,
0.9741,
0.9754,
0.9754,
0.9765
]

accuracy_birnn = [
0.1682,
0.268,
0.3908,
0.4523,
0.531,
0.6037,
0.6617,
0.7296,
0.8154,
0.8599,
0.8945,
0.9072,
0.923,
0.9303,
0.9411,
0.9463,
0.9466,
0.9496,
0.9524,
0.9569,
0.9589,
0.958
]

epoch_number_lenet5 = [i+1 for i in range(len(accuracy_lenet5))]
epoch_number_birnn = [i+1 for i in range(len(accuracy_birnn))]

plt.plot(epoch_number_lenet5, accuracy_lenet5)
plt.title("Obtained accuracy at number of epochs (lenet5)")
plt.xlabel("Number of epochs")
plt.ylabel("Accuracy")
plt.grid()
plt.plot([7], [accuracy_lenet5[7-1]], marker='o', markersize=3, color="red")
plt.show()

plt.plot(epoch_number_birnn, accuracy_birnn)
plt.title("Obtained accuracy at number of epochs (bi-rnn)")
plt.xlabel("Number of epochs")
plt.ylabel("Accuracy")
plt.grid()
plt.plot([11], [accuracy_birnn[11-1]], marker='o', markersize=3, color="red")
plt.show()