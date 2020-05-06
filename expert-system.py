from experta import *
from pre_process import *


global symptom_map, description_map, treatment_map


def func(disease):
    print("************************************")
    try:
        disease_details = description_map[disease]
        treatments = treatment_map[disease]
        print("A possibility is ", disease)
        print("\nDiagnosis", disease_details)
        print("\nTreatment", treatments)
    except Exception as e:
        print("No disease in our Database")


class ExpertSystem(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        print("Answer few yes no questions for diagnosis".center(40, "*"))
        yield Fact(action="initialCall")

    @Rule(Fact(action='initialCall'), NOT(Fact(headache=W())))
    def headAche(self):
        self.declare(Fact(headache=input("headache:  ")))

    @Rule(Fact(action='initialCall'), NOT(Fact(back_pain=W())))
    def backPain(self):
        self.declare(Fact(back_pain=input("Back Pain:  ")))

    @Rule(Fact(action='initialCall'), NOT(Fact(chest_pain=W())))
    def chestPain(self):
        self.declare(Fact(chest_pain=input("Chest Pain:  ")))

    @Rule(Fact(action='initialCall'), NOT(Fact(cough=W())))
    def cough(self):
        self.declare(Fact(cough=input("Cough:  ")))

    @Rule(Fact(action='initialCall'), NOT(Fact(fainting=W())))
    def fainting(self):
        self.declare(Fact(fainting=input("Fainting:  ")))

    @Rule(Fact(action='initialCall'), NOT(Fact(fatigue=W())))
    def fatigue(self):
        self.declare(Fact(fatigue=input("Fatigue:  ")))

    @Rule(Fact(action='initialCall'), NOT(Fact(sunken_eyes=W())))
    def sunkenEyes(self):
        self.declare(Fact(sunken_eyes=input("Sunken Eyes:  ")))

    @Rule(Fact(action='initialCall'), NOT(Fact(low_body_temp=W())))
    def lowBodyTemp(self):
        self.declare(Fact(low_body_temp=input("Low Body Temp:  ")))

    @Rule(Fact(action='initialCall'), NOT(Fact(restlessness=W())))
    def Restlessness(self):
        self.declare(Fact(restlessness=input("Restlessness:  ")))

    @Rule(Fact(action='initialCall'), NOT(Fact(sore_throat=W())))
    def soreThroat(self):
        self.declare(Fact(sore_throat=input("Sore Throat:  ")))

    @Rule(Fact(action='initialCall'), NOT(Fact(fever=W())))
    def fever(self):
        self.declare(Fact(fever=input("Fever:  ")))

    @Rule(Fact(action='initialCall'), NOT(Fact(nausea=W())))
    def nausea(self):
        self.declare(Fact(nausea=input("Nausea:  ")))

    @Rule(Fact(action='initialCall'), NOT(Fact(blurred_vision=W())))
    def blurredVision(self):
        self.declare(Fact(blurred_vision=input("Blurred vision:  ")))

    @Rule(Fact(action='initialCall'),
          Fact(headache="no"),
          Fact(fainting="no"),
          Fact(sore_throat="no"),
          Fact(fatigue="yes"),
          Fact(restlessness="no"),
          Fact(low_body_temp="no"),
          Fact(sunken_eyes="no"),
          Fact(chest_pain="no"),
          Fact(fever="yes"),
          Fact(back_pain="no"),
          Fact(nausea="yes"),
          Fact(cough="no"),
          Fact(blurred_vision="no"))
    def addJaundice(self):
        self.declare(Fact(disease="Jaundice"))

    @Rule(Fact(action='initialCall'),
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
    def addAlzheimers(self):
        self.declare(Fact(disease="Alzheimers"))

    @Rule(Fact(action='initialCall'),
          Fact(headache="no"),
          Fact(back_pain="yes"),
          Fact(chest_pain="no"),
          Fact(cough="no"),
          Fact(low_body_temp="no"),
          Fact(fainting="no"),
          Fact(fatigue="yes"),
          Fact(fever="no"),
          Fact(sunken_eyes="no"),
          Fact(restlessness="no"),
          Fact(sore_throat="no"),
          Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def addArthritis(self):
        self.declare(Fact(disease="Arthritis"))

    @Rule(Fact(action='initialCall'),
          Fact(cough="yes"),
          Fact(fainting="no"),
          Fact(sore_throat="no"),
          Fact(fatigue="no"),
          Fact(chest_pain="yes"),
          Fact(restlessness="no"),
          Fact(low_body_temp="no"),
          Fact(fever="yes"),
          Fact(back_pain="no"),
          Fact(sunken_eyes="no"),
          Fact(headache="no"),
          Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def addTuberculosis(self):
        self.declare(Fact(disease="Tuberculosis"))

    @Rule(Fact(action='initialCall'),
          Fact(headache="no"),
          Fact(back_pain="no"),
          Fact(chest_pain="yes"),
          Fact(fainting="no"),
          Fact(cough="yes"),
          Fact(low_body_temp="no"),
          Fact(restlessness="yes"),
          Fact(sore_throat="no"),
          Fact(fever="no"),
          Fact(sunken_eyes="no"),
          Fact(nausea="no"),
          Fact(fatigue="no"),
          Fact(blurred_vision="no"))
    def addAsthma(self):
        self.declare(Fact(disease="Asthma"))

    @Rule(Fact(action='initialCall'),
          Fact(headache="yes"),
          Fact(back_pain="no"),
          Fact(chest_pain="no"),
          Fact(cough="yes"),
          Fact(fainting="no"),
          Fact(sore_throat="yes"),
          Fact(restlessness="no"),
          Fact(nausea="no"),
          Fact(fatigue="no"),
          Fact(fever="yes"),
          Fact(low_body_temp="no"),
          Fact(sunken_eyes="no"),
          Fact(blurred_vision="no"))
    def addSinusitis(self):
        self.declare(Fact(disease="Sinusitis"))

    @Rule(Fact(action='initialCall'),
          Fact(headache="no"),
          Fact(back_pain="no"),
          Fact(chest_pain="no"),
          Fact(cough="no"),
          Fact(fainting="no"),
          Fact(sore_throat="no"),
          Fact(restlessness="no"),
          Fact(nausea="no"),
          Fact(sunken_eyes="no"),
          Fact(fatigue="yes"),
          Fact(fever="no"),
          Fact(low_body_temp="no"),
          Fact(blurred_vision="no"))
    def addEpilepsy(self):
        self.declare(Fact(disease="Epilepsy"))

    @Rule(Fact(action='initialCall'),
          Fact(headache="no"),
          Fact(back_pain="no"),
          Fact(chest_pain="yes"),
          Fact(cough="no"),
          Fact(low_body_temp="no"),
          Fact(fever="no"),
          Fact(sunken_eyes="no"),
          Fact(fainting="no"),
          Fact(nausea="yes"),
          Fact(fatigue="no"),
          Fact(restlessness="no"),
          Fact(sore_throat="no"),
          Fact(blurred_vision="no"))
    def addHeartDisease(self):
        self.declare(Fact(disease="Heart Disease"))

    @Rule(Fact(action='initialCall'),
          Fact(headache="no"),
          Fact(back_pain="no"),
          Fact(chest_pain="no"),
          Fact(fatigue="yes"),
          Fact(sunken_eyes="no"),
          Fact(cough="no"),
          Fact(fainting="no"),
          Fact(sore_throat="no"),
          Fact(nausea="yes"),
          Fact(restlessness="no"),
          Fact(low_body_temp="no"),
          Fact(fever="no"),
          Fact(blurred_vision="yes"))
    def addDiabetes(self):
        self.declare(Fact(disease="Diabetes"))

    @Rule(Fact(action='initialCall'),
          Fact(headache="yes"),
          Fact(fainting="no"),
          Fact(low_body_temp="no"),
          Fact(sunken_eyes="no"),
          Fact(sore_throat="no"),
          Fact(fever="no"),
          Fact(back_pain="no"),
          Fact(chest_pain="no"),
          Fact(cough="no"),
          Fact(fatigue="no"),
          Fact(restlessness="no"),
          Fact(nausea="yes"),
          Fact(blurred_vision="yes"))
    def addGlaucoma(self):
        self.declare(Fact(disease="Glaucoma"))

    @Rule(Fact(action='initialCall'),
          Fact(headache="no"),
          Fact(back_pain="no"),
          Fact(fainting="no"),
          Fact(sore_throat="no"),
          Fact(fatigue="yes"),
          Fact(restlessness="no"),
          Fact(sunken_eyes="no"),
          Fact(nausea="yes"),
          Fact(low_body_temp="no"),
          Fact(chest_pain="no"),
          Fact(cough="no"),
          Fact(fever="no"),
          Fact(blurred_vision="no"))
    def addHyperthyroidism(self):
        self.declare(Fact(disease="Hyperthyroidism"))

    @Rule(Fact(action='initialCall'),
          Fact(headache="yes"),
          Fact(cough="no"),
          Fact(fainting="no"),
          Fact(back_pain="no"),
          Fact(chest_pain="no"),
          Fact(low_body_temp="no"),
          Fact(fever="yes"),
          Fact(sunken_eyes="no"),
          Fact(sore_throat="no"),
          Fact(fatigue="no"),
          Fact(restlessness="no"),
          Fact(nausea="yes"),
          Fact(blurred_vision="no"))
    def addHeat(self):
        self.declare(Fact(disease="Heat Stroke"))

    @Rule(Fact(action='initialCall'),
          Fact(headache="no"),
          Fact(back_pain="no"),
          Fact(chest_pain="no"),
          Fact(cough="no"),
          Fact(fainting="yes"),
          Fact(sore_throat="no"),
          Fact(restlessness="no"),
          Fact(fever="no"),
          Fact(nausea="no"),
          Fact(fatigue="no"),
          Fact(low_body_temp="yes"),
          Fact(sunken_eyes="no"),
          Fact(blurred_vision="no"))
    def addHypothermia(self):
        self.declare(Fact(disease="Hypothermia"))

    @Rule(Fact(action='initialCall'), Fact(disease=MATCH.disease))
    def findDisease(self, disease):
        disease_details = description_map[disease]
        treatments = treatment_map[disease]
        print("\nDiagnosis", disease_details)
        print("\nTreatment", treatments)

    @Rule(Fact(action='initialCall'),
          Fact(fatigue="no"),
          Fact(restlessness="no"),
          Fact(low_body_temp="no"),
          Fact(headache="no"),
          Fact(back_pain="no"),
          Fact(chest_pain="no"),
          Fact(cough="no"),
          Fact(fainting="no"),
          Fact(fever="no"),
          Fact(sore_throat="no"),
          Fact(sunken_eyes="no"),
          Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def noDisease(self):
        print("Reffered to nearest Hospital")
        return

    @Rule(Fact(action='initialCall'),
          Fact(headache=MATCH.headache),
          Fact(fatigue=MATCH.fatigue),
          Fact(low_body_temp=MATCH.low_body_temp),
          Fact(restlessness=MATCH.restlessness),
          Fact(fever=MATCH.fever),
          Fact(sunken_eyes=MATCH.sunken_eyes),
          Fact(back_pain=MATCH.back_pain),
          Fact(sore_throat=MATCH.sore_throat),
          Fact(chest_pain=MATCH.chest_pain),
          Fact(cough=MATCH.cough),
          Fact(fainting=MATCH.fainting),
          Fact(nausea=MATCH.nausea),
          Fact(blurred_vision=MATCH.blurred_vision),
          NOT(Fact(disease=MATCH.disease)))
    def referHospital(self, headache, back_pain, chest_pain, cough, fainting,
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
    symptom_map, description_map, treatment_map = initialize()
    engine = ExpertSystem()
    engine.reset()
    engine.run()
