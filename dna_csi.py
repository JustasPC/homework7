dna = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

dna_hcolors = {
    "Black":"CCAGCAATCGC",
    "Brown":"GCCAGTGCCG",
    "Blonde":"TTAGCTATCGC"
    }

dna_face = {
    "Square":"GCCACGG",
    "Round":"ACCACAA",
    "Oval":"AGGCCTCA"
    }

dna_eyes = {
    "Blue":"TTGTGGTGGC",
    "Green":"GGGAGGTGGC",
    "Brown":"AAGTAGTGAC"
    }

dna_gender = {
    "Female":"TGAAGGACCTTC",
    "Male":"TGCAGGAACTTC"
    }

dna_race = {
    "White":"AAAACCTCA",
    "Black":"CGACTACAG",
    "Asian":"CGCGGGCCG"
    }


suspect = {
    "gender":"",
    "race":"",
    "hair":"",
    "eyes":"",
    "face":""
    }

def fun_check_dna(info,evidence):
    match = ""
    for x, y in info.items():
        if y in evidence:
            match = x
    return match

suspects_list = [
	{"Eva":{
           "gender":"Female",
           "race":"White",
           "hair":"Blonde",
           "eyes":"Blue",
           "face":"Oval"}
         },
        
        {"Miha":{
           "gender":"Male",
           "race":"White",
           "hair":"Brown",
           "eyes":"Green",
           "face":"Square"}
         },

        {"Matej" : {
           "gender":"Male",
           "race":"White",
           "hair":"Black",
           "eyes":"Blue",
           "face":"Oval" }
         },

        {"Larisa":{
            "gender":"Female",
            "race":"White",
            "hair":"Brown",
            "eyes":"Brown",
            "face":"Oval"}
        }
        ]

suspect["hair"] = fun_check_dna(dna_hcolors,dna)
suspect["face"] = fun_check_dna(dna_face,dna)
suspect["eyes"] = fun_check_dna(dna_eyes,dna)
suspect["gender"] = fun_check_dna(dna_gender,dna)
suspect["race"] = fun_check_dna(dna_race,dna)
            

for person in suspects_list:
    for name, bio in person.items():
        if bio == suspect:
            print("Ice killer is:", name)





    
