% Facts about symptoms
symptom(fever).
symptom(cough).
symptom(headache).
symptom(nausea).
symptom(sore_throat).
symptom(chills).
symptom(fatigue).

% Facts about diseases
disease(flu).
disease(cold).
disease(covid19).

% Disease-Symptom Associations
has_symptom(flu, fever).
has_symptom(flu, cough).
has_symptom(flu, headache).
has_symptom(flu, fatigue).

has_symptom(cold, cough).
has_symptom(cold, sore_throat).
has_symptom(cold, fatigue).

has_symptom(covid19, fever).
has_symptom(covid19, cough).
has_symptom(covid19, headache).
has_symptom(covid19, sore_throat).
has_symptom(covid19, fatigue).
has_symptom(covid19, chills).
has_symptom(covid19, nausea).

% Rule: Check if a disease has a specific symptom
disease_has_symptom(Disease, Symptom) :-
    disease(Disease),
    symptom(Symptom),
    has_symptom(Disease, Symptom).

% Rule: List all symptoms for a given disease
disease_symptoms(Disease, Symptoms) :-
    disease(Disease),
    findall(Symptom, has_symptom(Disease, Symptom), Symptoms).

% Rule: List all diseases that have a given symptom
symptom_diseases(Symptom, Diseases) :-
    symptom(Symptom),
    findall(Disease, has_symptom(Disease, Symptom), Diseases).

% Rule: Find common symptoms between two diseases
common_symptoms(Disease1, Disease2, CommonSymptoms) :-
    disease(Disease1),
    disease(Disease2),
    findall(Symptom, (has_symptom(Disease1, Symptom), has_symptom(Disease2, Symptom)), CommonSymptoms).

% Rule: List all diseases with common symptoms
diseases_with_common_symptoms(CommonSymptoms, Diseases) :-
    findall(Disease, (disease(Disease), forall(member(Symptom, CommonSymptoms), has_symptom(Disease, Symptom))), Diseases).

% Rule: List diseases and their symptoms
list_all_diseases_and_symptoms :-
    disease(Disease),
    write('Disease: '), write(Disease), nl,
    disease_symptoms(Disease, Symptoms),
    write('Symptoms: '), write(Symptoms), nl, nl.


# remove this part of code while running this code
# ------------------------------------------------------------------------
# Queries :
# 1) Check if a disease has a specific symptom: 
#     ?- disease_has_symptom(flu, fever).
# 2)  List symptoms for a disease::
#     ?- disease_symptoms(covid19, Symptoms).
# 3) List diseases with a specific symptom::
#     ?- symptom_diseases(cough, Diseases).
# 4) Find common symptoms between two diseases:
#     ?- common_symptoms(flu, covid19, CommonSymptoms).
# 5) List all diseases with common symptoms:
#     ?- diseases_with_common_symptoms([fever, cough], Diseases).
# 6) List all diseases and their symptoms:
#     ?- list_all_diseases_and_symptoms.
