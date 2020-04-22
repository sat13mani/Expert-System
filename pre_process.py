import os


def initialize():
    symptom_map = {}
    description_map = {}
    treatment_map = {}
    symptoms = []
    with open("diseases.txt") as d_file:
        diseases = (d_file.read()).split('\n')
        print(diseases)
        for disease in diseases:
            path = os.getcwd()
            path1 = os.path.join(path, "Disease symptoms")
            path1 = os.path.join(path1, disease)
            symptom_file = str(path1) + ".txt"
            with open(symptom_file) as reader:
                symptom_list = (reader.read()).split('\n')
                symptom_map[str(symptom_list)] = disease
                symptoms.append(symptom_list)

            path2 = os.path.join(path, "Disease descriptions")
            path2 = os.path.join(path2, disease)
            description_file = str(path2) + ".txt"
            with open(description_file) as reader:
                d_data = reader.read()
                description_map[disease] = d_data

            path3 = os.path.join(path, "Disease treatments")
            path3 = os.path.join(path3, disease)
            treatment_file = str(path3) + ".txt"
            with open(treatment_file) as reader:
                t_data = reader.read()
                treatment_map[disease] = t_data

    for item in symptom_map.items():
        print((item))

    for item in description_map.items():
        print((item))

    for item in treatment_map.items():
        print((item))


initialize()
