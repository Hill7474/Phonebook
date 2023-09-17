def add_contact(pb):
    # Adding a contact is the easiest because all you need to do is:
    # append another list of details into the already existing list
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Enter name: ")))
        if i == 1:
            dip.append(int(input("Enter number: ")))
        if i == 2:
            dip.append(str(input("Enter e-mail address: ")))
        if i == 3:
            dip.append(str(input("Enter date of birth(dd/mm/yy): ")))
        if i == 4:
            dip.append(
                str(input("Enter category(Family/Friends/Work/Others): ")))
    pb.append(dip)
    # And once you modify the list, you return it to the calling function wiz main, here.
    return pb
