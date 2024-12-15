import pgzrun

group_records = []


num_groups = int(input("Enter the number of groups: "))


for _ in range(num_groups):
        group_name = input("Enter the group name ")
        group_size = int(input("Enter the size of the group: "))
        competition_date = input("Enter the date of the competition (DD/MM/YYYY): ")
        venue = input("Enter the venue of the competition: ")
        medal_type = input("Enter the type of the medal (Gold/Silver/Bronze): ")

        group_record = (group_name, group_size, competition_date, venue, medal_type)

        group_records.append(group_record)

for record in group_records:
    print(f"Group Name: {record[0]}, Group Size: {record[1]}, Date: {record[2]}, Venue: {record[3]}, Medal Type: {record[4]}")


pgzrun.go()
