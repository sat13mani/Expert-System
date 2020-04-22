from experta import *


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

    @Rule(Fact(action='find_disease'), NOT(Fact(fatigue=W())))
    def sym12(self):
        self.declare(Fact(fatigue=input("Fatigue:  ")))


if __name__ == '__main__':
    engine = ExpertSystem()
    engine.reset()
    engine.run()
