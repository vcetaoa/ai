% Declare the symptom predicate as dynamic so we can assert new facts
:- dynamic symptom/1.

% Disease-Symptom Associations
has_symptom(flu, fever).
has_symptom(flu, cough).
has_symptom(flu, headache).
has_symptom(flu, fatigue).  % Common symptom

has_symptom(cold, sore_throat).
has_symptom(cold, runny_nose).
has_symptom(cold, fatigue).  % Common symptom
has_symptom(cold, sneezing).

has_symptom(covid19, fever).
has_symptom(covid19, cough).
has_symptom(covid19, fatigue).  % Common symptom
has_symptom(covid19, shortness_of_breath).

% Facts about diseases
disease(flu).
disease(cold).
disease(covid19).

% Rules to determine the disease
% Flu is suspected if fever, cough, headache, and fatigue are present.
diagnosis(flu) :- symptom(fever), symptom(cough), symptom(headache), symptom(fatigue).

% Cold is suspected if sore throat, runny nose, sneezing, and fatigue are present.
diagnosis(cold) :- symptom(sore_throat), symptom(runny_nose), symptom(sneezing), symptom(fatigue).

% COVID-19 is suspected if fever, cough, shortness of breath, and fatigue are present.
diagnosis(covid19) :- 
    symptom(fever), symptom(cough), symptom(fatigue), symptom(shortness_of_breath).

% Rule for displaying diagnosis after evaluation
evaluate_diagnosis :-
    findall(Disease, diagnosis(Disease), Diseases),
    ( Diseases = [] ->
        write('No diagnosis could be made based on the symptoms.'), nl
    ; write('Possible diagnoses: '), nl,
      display_diagnoses(Diseases)
    ).

% Display all possible diagnoses
display_diagnoses([]).
display_diagnoses([Disease|Rest]) :-
    write(Disease), nl,
    display_diagnoses(Rest).

% Asking for symptoms
ask_symptoms :-
    % Clear any previously asserted symptoms to avoid multiple diagnoses
    retractall(symptom(_)),

    write('Do you have fever? (yes/no): '), read(Answer1), handle_answer(fever, Answer1),
    write('Do you have cough? (yes/no): '), read(Answer2), handle_answer(cough, Answer2),
    write('Do you have headache? (yes/no): '), read(Answer3), handle_answer(headache, Answer3),
    write('Do you have fatigue? (yes/no): '), read(Answer4), handle_answer(fatigue, Answer4),
    write('Do you have sore throat? (yes/no): '), read(Answer5), handle_answer(sore_throat, Answer5),
    write('Do you have runny nose? (yes/no): '), read(Answer6), handle_answer(runny_nose, Answer6),
    write('Do you have sneezing? (yes/no): '), read(Answer7), handle_answer(sneezing, Answer7),
    write('Do you have shortness of breath? (yes/no): '), read(Answer8), handle_answer(shortness_of_breath, Answer8).

% Handle the answer to the symptoms
handle_answer(Symptom, yes) :-
    \+ symptom(Symptom),  % Check if the symptom is not already asserted
    assertz(symptom(Symptom)).

handle_answer(_, no).

% Start the diagnosis
start :-
    ask_symptoms,
    evaluate_diagnosis.



# remove this part of code while running this code
# -----------------------------------------------------------
# Queries
# 1) Manually Add Flu Symptoms:
#     ?- retractall(symptom(_)), assertz(symptom(fever)), assertz(symptom(cough)), assertz(symptom(headache)), assertz(symptom(fatigue)), evaluate_diagnosis.
# 2) Test for Cold Symptoms:
#     ?- retractall(symptom(_)), assertz(symptom(sore_throat)), assertz(symptom(runny_nose)), assertz(symptom(sneezing)), assertz(symptom(fatigue)), evaluate_diagnosis.
# 3) Test for COVID-19 Symptoms:
#     ?- retractall(symptom(_)), assertz(symptom(fever)), assertz(symptom(cough)), assertz(symptom(fatigue)), assertz(symptom(shortness_of_breath)), evaluate_diagnosis.
# 4) See All Symptoms Added So Far:
#     ?- listing(symptom).
# 5) Clear All Stored Symptoms (Reset):
#     ?- retractall(symptom(_)).

# this is enough 
