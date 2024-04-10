row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
position_new=list(position)
print(position_new)
row=position_new[0]
column=position_new[1]
map.replace("⬜️","X")
print(f"{row1}\n{row2}\n{row3}")


