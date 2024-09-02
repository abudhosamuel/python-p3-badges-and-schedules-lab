def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(speaker):
    room_assignments = []
    for index, speaker in enumerate(speaker, start=1):
        room_assignments.append(f"Hello, {speaker}! You'll be assigned to room {index}!")
    return room_assignments
    

def printer(speaker):
    badges = batch_badge_creator(speaker)
    for badge in badges:
        print(badge)
    
    #print room assignments
    rooms=assign_rooms(speaker)
    for room in rooms:
        print(room)
  

print(badge_maker("Arel"))
print(batch_badge_creator(["Arel","Carol"]))
print(assign_rooms(["Arel","Carol"]))
printer(["Arel","Carol"])