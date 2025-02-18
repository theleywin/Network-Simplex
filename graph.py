def create_graph(type):
	if(type == 1):
		G = {
			"node": [
				{"point": 1, "pred": 0, "depth": 0, "thread": 1, "potential": 0, "balance": 6},
				{"point": 2, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 3, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 4, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 5, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 6, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 7, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
			],

			"arc": [
				{"sp": 1, "ep": 2, "cost": 4},
				{"sp": 1, "ep": 3, "cost": 2},
				{"sp": 1, "ep": 6, "cost": 3},
				{"sp": 2, "ep": 5, "cost": 3},
				{"sp": 2, "ep": 6, "cost": 1},
				{"sp": 3, "ep": 2, "cost": 1},
				{"sp": 3, "ep": 4, "cost": 4},
				{"sp": 4, "ep": 6, "cost": 1},
				{"sp": 4, "ep": 7, "cost": 3},
				{"sp": 5, "ep": 4, "cost": 1},
				{"sp": 5, "ep": 7, "cost": 4},
				{"sp": 6, "ep": 5, "cost": 2},

			]
		}

	elif(type == 2):
		G = {

			"node": [
				{"point": 1, "pred": 0, "depth": 0, "thread": 1, "potential": 0, "balance": 5},
				{"point": 2, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 3, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 4, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 5, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 6, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},

			],
			
			"arc": [
				{"sp": 1, "ep": 2, "cost": 12},
				{"sp": 1, "ep": 3, "cost": 7},
				{"sp": 2, "ep": 4, "cost": 6},
				{"sp": 2, "ep": 5, "cost": 4},
				{"sp": 3, "ep": 4, "cost": 5},
				{"sp": 3, "ep": 5, "cost": 8},
				{"sp": 4, "ep": 6, "cost": 13},
				{"sp": 5, "ep": 6, "cost": 5}
			]
		}

	elif(type == 3):
		G = {

			"node": [
				{"point": 1, "pred": 0, "depth": 0, "thread": 1, "potential": 0, "balance": 6},
				{"point": 2, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 3, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 4, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 5, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 6, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 7, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
			],
			
			"arc": [
				{"sp": 1, "ep": 3, "cost": 2},
				{"sp": 1, "ep": 4, "cost": 9},
				{"sp": 2, "ep": 4, "cost": 1},
				{"sp": 2, "ep": 6, "cost": 1},
				{"sp": 3, "ep": 2, "cost": 3},
				{"sp": 3, "ep": 5, "cost": 6},
				{"sp": 3, "ep": 7, "cost": 2},
				{"sp": 5, "ep": 6, "cost": 3},
				{"sp": 6, "ep": 3, "cost": 8},
				{"sp": 6, "ep": 4, "cost": 7},
				{"sp": 7, "ep": 5, "cost": 2}
			]
		}

	elif (type == 4):
		G = {

			"node": [
				{"point": 1, "pred": 0, "depth": 0, "thread": 1, "potential": 0, "balance": 5},
				{"point": 2, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 3, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 4, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 5, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 6, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1}
			],
			
			"arc": [
				{"sp": 1, "ep": 2, "cost": 1},
				{"sp": 1, "ep": 3, "cost": 2},
				{"sp": 2, "ep": 5, "cost": 1},
				{"sp": 3, "ep": 2, "cost": 3},
				{"sp": 3, "ep": 4, "cost": 3},
				{"sp": 4, "ep": 6, "cost": 2},
				{"sp": 5, "ep": 4, "cost": 2},
				{"sp": 5, "ep": 6, "cost": 5}
			]
		}
	elif(type == 5):
		G = {
			
			"node": [
				{"point": 1, "pred": 0, "depth": 0, "thread": 1, "potential": 0, "balance": 8},
				{"point": 2, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 3, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 4, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 5, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 6, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 7, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 8, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1},
				{"point": 9, "pred": 1, "depth": 0, "thread": 1, "potential": 0, "balance": -1}
			],
			
			"arc": [
				{"sp": 1, "ep": 2, "cost": 15},
				{"sp": 1, "ep": 3, "cost": 13},
				{"sp": 1, "ep": 4, "cost": 5},
				{"sp": 2, "ep": 8, "cost": 12},
				{"sp": 3, "ep": 2, "cost": 2},
				{"sp": 3, "ep": 6, "cost": 6},
				{"sp": 3, "ep": 4, "cost": 18},
				{"sp": 4, "ep": 5, "cost": 4},
				{"sp": 4, "ep": 9, "cost": 99},
				{"sp": 5, "ep": 3, "cost": 3},
				{"sp": 5, "ep": 6, "cost": 1},
				{"sp": 5, "ep": 7, "cost": 9},
				{"sp": 5, "ep": 9, "cost": 14},
				{"sp": 6, "ep": 2, "cost": 8},
				{"sp": 6, "ep": 8, "cost": 17},
				{"sp": 7, "ep": 6, "cost": 16},
				{"sp": 7, "ep": 8, "cost": 7},
				{"sp": 7, "ep": 9, "cost": 10},
				{"sp": 9, "ep": 8, "cost": 11}
			]
		}
	return G