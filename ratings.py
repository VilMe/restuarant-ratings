"""Restaurant rating lister."""

def resturant_ratings (rate_file):
	dicts_ratings = {}
	rate_file = open(rate_file, 'r')
	for line in rate_file:
		line = line.strip("\n")
		line_spl = line.split(":")
		dicts_ratings[line_spl[0]] = line_spl[1]
	sort_dictsR = sorted(dicts_ratings.items())
	for rest_name, rest_rate in sort_dictsR:
		print('{} is rated at {}.'. format(rest_name,rest_rate))

resturant_ratings("scores.txt")
# put your code here
