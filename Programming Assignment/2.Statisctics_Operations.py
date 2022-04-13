import statistics

num_list = [int (x) for x in input("Enter values :- ").split()]

#
# print("Minimum :",min(num_list))
# print("Maximum :",max(num_list))
# print("Mean :",statistics.mean(num_list))
# print("Standard Deviation : ",statistics.stdev(num_list))
# print("Variance : ",statistics.variance(num_list))

print(min(num_list),max(num_list),"{0:.2f}".format(statistics.mean(num_list)),"{0:.2f}".format(statistics.stdev(num_list)),"{0:.2f}".format(statistics.variance(num_list)))