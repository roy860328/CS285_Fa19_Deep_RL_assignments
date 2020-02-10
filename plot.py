import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

COLOR = ["r", "g", "b", "k", "c", "m", "y"]
LINE = ["-", "--", ":", "-.", '.', 'o', '^']
current_index = 0
#Thisisjustadummyfunctiontogeneratesomearbitrarydata
def getdata():
	basecond=[[18,20,19,18,13,4,1],
				[20,17,12,9,3,0,0],
				[20,20,20,12,5,3,0]]
	cond1=[[18,19,18,19,20,15,14],
			[19,20,18,16,20,15,9],
			[19,20,20,20,17,10,0],
			[20,20,20,20,7,9,1]]
	cond2=[[20,20,20,20,19,17,4],
			[20,20,20,20,20,19,7],
			[19,20,20,19,19,15,2]]
	cond3=[[20,20,20,20,19,17,12],
			[18,20,19,18,13,4,1],
			[20,19,18,17,13,2,0],
			[19,18,20,20,15,6,0]]

	return basecond, cond1, cond2, cond3

def input_data_to_plot(x, y):
	global current_index
	sns.tsplot(time=x,data=y,color=COLOR[current_index],linestyle=LINE[current_index])
	current_index = current_index+1 if current_index<len(COLOR) else 0


def main():
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('--folder_path', '-fp', type=str, required=True)  # relative to where you're running this script from
	args = parser.parse_args()

	# convert args to dictionary
	params = vars(args)
	params["folder_path"] = os.path.join(os.path.dirname(os.path.realpath(__file__)), params["folder_path"])
	print(params["folder_path"])

	##################################
	### INPUT DATA
	##################################
	fig = plt.figure()

	results = getdata()
	xdata = np.array([0,1,2,3,4,5,6])/5.
	for y in results:
		input_data_to_plot(xdata, y)

	##################################
	### VISUALIZE DATA
	##################################

	plt.ylabel("SuccessRate",fontsize=25)
	plt.xlabel("IterationNumber",fontsize=25,labelpad=-4)
	plt.title("AwesomeRobotPerformance",fontsize=30)
	plt.legend(loc="bottomleft")
	plt.show()

if __name__ == "__main__":
	main()