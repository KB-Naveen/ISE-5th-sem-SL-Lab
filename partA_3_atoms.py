def atomicDict():
    #(i)
    atoms = {"C":"Carbon","N":"Nitrogen","B":"Boron"}
    print("Atoms Dictionary :",atoms)

    #(ii)
    a = input("Enter an atom name to add :")
    s = input("Enter it's symbol :")
    if(s in atoms.keys()):
        print("Atom present in the dictionary, so updating it's values")
    else:
        print("Adding new atom to the dictionary")
    atoms[s] = a

    a = input("Enter an atom name to add :")
    s = input("Enter it's symbol :")
    if(s in atoms.keys()):
        print("Atom present in the dictionary, so updating it's values")
    else:
        print("Adding new atom to the dictionary")
    atoms[s] = a

    print("Atoms Dictionary :",atoms)

    #(iii)
    print("Number of elements in the list :",len(atoms))

    #(iv)
    s = input("Enter symbol of atom to search :")
    if(s in atoms.keys()):
        print("Atom found with name :",atoms[s])
    else:
        print("Atom not found")