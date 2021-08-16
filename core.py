
def buildboard():

	b = [["E " for i in range(8)] for j in range(8)]
	for i in range(8):
		b[i][6] = "BP"
	b[0][0] = "WR"
	b[7][0] = "WR"

	return b

def main():
	board = buildboard()
	for i in range(7,-1,-1):
		for j in range(8):
			print (board[j][i], end=" ")
		print("")
		




if __name__ == "__main__":
	main()
