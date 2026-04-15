

marks= {
	"Amarjit":100,
	"shubham":78,
	"Rohan":45,
	0:"Harry"

}
print(marks.items())
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Amarjit":99})
print(marks.get("Amarjit"))# returns none if not matches
print(marks["Amarjit"]) # returns error
