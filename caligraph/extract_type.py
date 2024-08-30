with open("caligraph-instances_types.nt","r") as r, open("setname_elementname.csv","w") as w:
    w.write(f"set_name,element_name\n")
    i = 0
    while True:
        i = i+ 1
        print(i)
        line = r.readline()
        if len(line) == 0:
            break
        line = line.strip()
        line_list = line.split(" ")
        element_name = line_list[0]
        element_name = element_name.replace("<http://caligraph.org/resource/","")
        element_name = element_name.replace(">","")
        set_name = line_list[2]
        set_name = set_name.replace("<http://caligraph.org/ontology/","")
        set_name = set_name.replace("<http://www.w3.org/2002/07/owl","")
        set_name = set_name.replace(">","")
        set_name_final = ''
        element_name_final = ''
        for character in set_name:
            if character == '"':
                set_name_final = set_name_final + character + '"'
            else:
                set_name_final = set_name_final + character
        if ',' in set_name_final:
            set_name_final = f'"{set_name_final}"'
        for character in element_name:
            if character == '"':
                element_name_final = element_name_final + character + '"'
            else:
                element_name_final = element_name_final + character
        if ',' in element_name_final:
            element_name_final = f'"{element_name_final}"'
        w.write(f"{element_name_final},{set_name_final}\n")
        