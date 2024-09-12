from logic import *

CKnight = Symbol("Conner is a knight")
CKnave = Symbol("Conner is a knave")

SKnight = Symbol("Samuel is a knight")
SKnave = Symbol("Samuel is a knave")

HKnight = Symbol("Hillary is a knight")
HKnave = Symbol("Hillary is a knave")

KKnight = Symbol("Kirstin is a knight")
KKnave = Symbol("Kirstin is a knave")

DKnight = Symbol("Denise is a knight")
DKnave = Symbol("Denise is a knave")

GKnight = Symbol("Gwen is a knight")
GKnave = Symbol("Gwen is a knave")

#general knowledge applied to every KB
general_knowledge = And(
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),
    Or(SKnight, SKnave),
    Not(And(SKnight, SKnave)),
    Or(HKnight, HKnave),
    Not(And(HKnight, HKnave)),
    Or(KKnight, KKnave),
    Not(And(KKnight, KKnave)),
    Or(DKnight, DKnave),
    Not(And(DKnight,DKnave)),
    Or(GKnight, GKnave),
    Not(And(GKnight, GKnave))
)


# Puzzle
#Conner says "Samuel is a knave."
#Samuel says "Hillary is lying."
#Hillary says "Conner tells the truth."
#Kirstin says "Denise is a knight."
#Denise says "Gwen tells the truth."
#Conner says "Gwen is a knave and I am a knave."

knowledge = And(
    general_knowledge,
    Implication(CKnight, SKnave),
    Implication(CKnave, Not(SKnave)),
    Implication(SKnight, HKnave),
    Implication(SKnave, Not(HKnave)),
    Implication(HKnight, CKnight),
    Implication(HKnave, Not(CKnight)),
    Implication(KKnight, DKnight),
    Implication(KKnave, Not(DKnight)),
    Implication(DKnight, GKnight),
    Implication(DKnave, Not(GKnight)),
    Implication(CKnight, And(GKnave, CKnave)),
    Implication(CKnave, Not(And(GKnave, CKnave)))
)

def main():
    symbols = [CKnight, CKnave, SKnight, SKnave, HKnight, HKnave, KKnight, KKnave, DKnight, DKnave, GKnight,GKnave]
    if len(knowledge.conjuncts) == 0:
        print("     Not yet implemented.")
    else:
        for symbol in symbols:
            if model_check(knowledge, symbol):
                print(f"    {symbol}")


if __name__ == "__main__":
    main()
