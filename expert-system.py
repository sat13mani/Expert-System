from experta import *
from pre_process import *


global symptom_map, description_map, treatment_map


def func(disease):
    print("in func", disease)
    print("******")
    disease_details = description_map[disease]
    treatments = treatment_map[disease]
    print("\nDiagnosis", disease_details)
    print("\nTreatment", treatments)


class ExpertSystem(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        print("Answer few yes no questions for diagnosis".center(40, "*"))
        yield Fact(action="find_disease")

    @Rule(Fact(action='find_disease'), NOT(Fact(headache=W())))
    def sym0(self):
        self.declare(Fact(headache=input("headache:  ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(back_pain=W())))
    def sym1(self):
        self.declare(Fact(back_pain=input("Back Pain:  ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(chest_pain=W())))
    def sym2(self):
        self.declare(Fact(chest_pain=input("Chest Pain:  ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(cough=W())))
    def sym3(self):
        self.declare(Fact(cough=input("Cough:  ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(fainting=W())))
    def sym4(self):
        self.declare(Fact(fainting=input("Fainting:  ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(fatigue=W())))
    def sym5(self):
        self.declare(Fact(fatigue=input("Fatigue:  ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(sunken_eyes=W())))
    def sym6(self):
        self.declare(Fact(sunken_eyes=input("Sunken Eyes:  ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(low_body_temp=W())))
    def sym7(self):
        self.declare(Fact(low_body_temp=input("Low Body Temp:  ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(restlessness=W())))
    def sym8(self):
        self.declare(Fact(restlessness=input("Restlessness:  ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(sore_throat=W())))
    def sym9(self):
        self.declare(Fact(sore_throat=input("Sore Throat:  ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(fever=W())))
    def sym10(self):
        self.declare(Fact(fever=input("Fever:  ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(nausea=W())))
    def sym11(self):
        self.declare(Fact(nausea=input("Nausea:  ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(blurred_vision=W())))
    def sym12(self):
        self.declare(Fact(blurred_vision=input("Blurred vision:  ")))

    @Rule(Fact(action='find_disease'),
          Fact(headache="no"),
          Fact(back_pain="no"),
          Fact(chest_pain="no"),
          Fact(cough="no"),
          Fact(fainting="no"),
          Fact(sore_throat="no"),
          Fact(fatigue="yes"),
          Fact(restlessness="no"),
          Fact(low_body_temp="no"),
          Fact(fever="yes"),
          Fact(sunken_eyes="no"),
          Fact(nausea="yes"),
          Fact(blurred_vision="no"))
    def disease_0(self):
        self.declare(Fact(disease="Jaundice"))

    @Rule(Fact(action='find_disease'),
          Fact(headache="no"),
          Fact(back_pain="no"),
          Fact(chest_pain="no"),
          Fact(cough="no"),
          Fact(fainting="no"),
          Fact(sore_throat="no"),
          Fact(fatigue="no"),
          Fact(restlessness="yes"),
          Fact(low_body_temp="no"),
          Fact(fever="no"),
          Fact(sunken_eyes="no"),
          Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def disease_1(self):
        self.declare(Fact(disease="Alzheimers"))

    @Rule(Fact(action='find_disease'),
          Fact(headache="no"),
          Fact(back_pain="yes"),
          Fact(chest_pain="no"),
          Fact(cough="no"),
          Fact(fainting="no"),
          Fact(sore_throat="no"),
          Fact(fatigue="yes"),
          Fact(restlessness="no"),
          Fact(low_body_temp="no"),
          Fact(fever="no"),
          Fact(sunken_eyes="no"),
          Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def disease_2(self):
        self.declare(Fact(disease="Arthritis"))

    @Rule(Fact(action='find_disease'),
          Fact(headache="no"),
          Fact(back_pain="no"),
          Fact(chest_pain="yes"),
          Fact(cough="yes"),
          Fact(fainting="no"),
          Fact(sore_throat="no"),
          Fact(fatigue="no"),
          Fact(restlessness="no"),
          Fact(low_body_temp="no"),
          Fact(fever="yes"),
          Fact(sunken_eyes="no"),
          Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def disease_3(self):
        self.declare(Fact(disease="Tuberculosis"))

    @Rule(Fact(action='find_disease'),
          Fact(headache="no"),
          Fact(back_pain="no"),
          Fact(chest_pain="yes"),
          Fact(cough="yes"),
          Fact(fainting="no"),
          Fact(sore_throat="no"),
          Fact(fatigue="no"),
          Fact(restlessness="yes"),
          Fact(low_body_temp="no"),
          Fact(fever="no"),
          Fact(sunken_eyes="no"),
          Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def disease_4(self):
        self.declare(Fact(disease="Asthma"))

    @Rule(Fact(action='find_disease'),
          Fact(headache="yes"),
          Fact(back_pain="no"),
          Fact(chest_pain="no"),
          Fact(cough="yes"),
          Fact(fainting="no"),
          Fact(sore_throat="yes"),
          Fact(fatigue="no"),
          Fact(restlessness="no"),
          Fact(low_body_temp="no"),
          Fact(fever="yes"),
          Fact(sunken_eyes="no"),
          Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def disease_5(self):
        self.declare(Fact(disease="Sinusitis"))

    @Rule(Fact(action='find_disease'),
          Fact(headache="no"),
          Fact(back_pain="no"),
          Fact(chest_pain="no"),
          Fact(cough="no"),
          Fact(fainting="no"),
          Fact(sore_throat="no"),
          Fact(fatigue="yes"),
          Fact(restlessness="no"),
          Fact(low_body_temp="no"),
          Fact(fever="no"),
          Fact(sunken_eyes="no"),
          Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def disease_6(self):
        self.declare(Fact(disease="Epilepsy"))

    @Rule(Fact(action='find_disease'),
          Fact(headache="no"),
          Fact(back_pain="no"),
          Fact(chest_pain="yes"),
          Fact(cough="no"),
          Fact(fainting="no"),
          Fact(sore_throat="no"),
          Fact(fatigue="no"),
          Fact(restlessness="no"),
          Fact(low_body_temp="no"),
          Fact(fever="no"),
          Fact(sunken_eyes="no"),
          Fact(nausea="yes"),
          Fact(blurred_vision="no"))
    def disease_7(self):
        self.declare(Fact(disease="Heart Disease"))

    @Rule(Fact(action='find_disease'),
          Fact(headache="no"),
          Fact(back_pain="no"),
          Fact(chest_pain="no"),
          Fact(cough="no"),
          Fact(fainting="no"),
          Fact(sore_throat="no"),
          Fact(fatigue="yes"),
          Fact(restlessness="no"),
          Fact(low_body_temp="no"),
          Fact(fever="no"),
          Fact(sunken_eyes="no"),
          Fact(nausea="yes"),
          Fact(blurred_vision="yes"))
    def disease_8(self):
        self.declare(Fact(disease="Diabetes"))

    @Rule(Fact(action='find_disease'),
          Fact(headache="yes"),
          Fact(back_pain="no"),
          Fact(chest_pain="no"),
          Fact(cough="no"),
          Fact(fainting="no"),
          Fact(sore_throat="no"),
          Fact(fatigue="no"),
          Fact(restlessness="no"),
          Fact(low_body_temp="no"),
          Fact(fever="no"),
          Fact(sunken_eyes="no"),
          Fact(nausea="yes"),
          Fact(blurred_vision="yes"))
    def disease_9(self):
        self.declare(Fact(disease="Glaucoma"))

    @Rule(Fact(action='find_disease'),
          Fact(headache="no"),
          Fact(back_pain="no"),
          Fact(chest_pain="no"),
          Fact(cough="no"),
          Fact(fainting="no"),
          Fact(sore_throat="no"),
          Fact(fatigue="yes"),
          Fact(restlessness="no"),
          Fact(low_body_temp="no"),
          Fact(fever="no"),
          Fact(sunken_eyes="no"),
          Fact(nausea="yes"),
          Fact(blurred_vision="no"))
    def disease_10(self):
        self.declare(Fact(disease="Hyperthyroidism"))

    @Rule(Fact(action='find_disease'),
          Fact(headache="yes"),
          Fact(back_pain="no"),
          Fact(chest_pain="no"),
          Fact(cough="no"),
          Fact(fainting="no"),
          Fact(sore_throat="no"),
          Fact(fatigue="no"),
          Fact(restlessness="no"),
          Fact(low_body_temp="no"),
          Fact(fever="yes"),
          Fact(sunken_eyes="no"),
          Fact(nausea="yes"),
          Fact(blurred_vision="no"))
    def disease_11(self):
        self.declare(Fact(disease="Heat Stroke"))

    @Rule(Fact(action='find_disease'),
          Fact(headache="no"),
          Fact(back_pain="no"),
          Fact(chest_pain="no"),
          Fact(cough="no"),
          Fact(fainting="yes"),
          Fact(sore_throat="no"),
          Fact(fatigue="no"),
          Fact(restlessness="no"),
          Fact(low_body_temp="yes"),
          Fact(fever="no"),
          Fact(sunken_eyes="no"),
          Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def disease_12(self):
        self.declare(Fact(disease="Hypothermia"))

    @Rule(Fact(action='find_disease'), Fact(disease=MATCH.disease))
    def disease(self, disease):
        disease_details = description_map[disease]
        treatments = treatment_map[disease]
        print("\nDiagnosis", disease_details)
        print("\nTreatment", treatments)

    @Rule(Fact(action='find_disease'),
          Fact(headache=MATCH.headache),
          Fact(back_pain=MATCH.back_pain),
          Fact(chest_pain=MATCH.chest_pain),
          Fact(cough=MATCH.cough),
          Fact(fainting=MATCH.fainting),
          Fact(sore_throat=MATCH.sore_throat),
          Fact(fatigue=MATCH.fatigue),
          Fact(low_body_temp=MATCH.low_body_temp),
          Fact(restlessness=MATCH.restlessness),
          Fact(fever=MATCH.fever),
          Fact(sunken_eyes=MATCH.sunken_eyes),
          Fact(nausea=MATCH.nausea),
          Fact(blurred_vision=MATCH.blurred_vision),
          NOT(Fact(disease=MATCH.disease)))
    def not_matched(self, headache, back_pain, chest_pain, cough, fainting,
                    sore_throat, fatigue, restlessness, low_body_temp, fever,
                    sunken_eyes, nausea, blurred_vision):
        print("\nDid not find any disease that matches your exact symptoms")
        lis = [headache, back_pain, chest_pain, cough, fainting, sore_throat,
               fatigue, restlessness, low_body_temp, fever, sunken_eyes,
               nausea, blurred_vision]
        max_count = 0
        max_disease = ""
        for key, val in symptom_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(0, len(lis)):
                if(temp_list[j] == lis[j] and lis[j] == "yes"):
                    count = count + 1
            if count > max_count:
                max_count = count
                max_disease = val
        func(max_disease)


if __name__ == '__main__':
    # global symptom_map, description_map, treatment_map
    symptom_map, description_map, treatment_map = initialize()
    engine = ExpertSystem()
    engine.reset()
    engine.run()
    print("out")
