## Data Details
[Fields](https://open.fda.gov/apis/drug/event/searchable-fields/)

* patient.patientsex

    Value is one of the following
0 = Unknown
1 = Male
2 = Female
* patient.patientagegroup
    
    Populated with Patient Age Group code.

    Value is one of the following
1 = Neonate
2 = Infant
3 = Child
4 = Adolescent
5 = Adult
6 = Elderly
* patient.drug.medicinalproduct
    * search=patient.drug.medicinalproduct="FOO+BAR"
    
        This returns records with FOO *or* BAR in field
    * search=patient.drug.medicinalproduct="FOO+AND+BAR"
        
        This returns records with FOO *AND* BAR in field 
    * count=patient.drug.medicinalproduct
    
        This returns counts of records with FOO *or* BAR in field 
        
* patient.reaction.reactionmeddrapt

    Patient reaction, as a MedDRA term. Note that these terms are encoded in British English. For instance, diarrhea is spelled diarrohea. MedDRA is a standardized medical terminology.
    
    * count=patient.reaction.reactionmeddrapt
        
        This returns counts of specific patient reaction
* patient.reaction.reactionoutcome

    Outcome of the reaction in reactionmeddrapt at the time of last observation.

    Value is one of the following
1 = Recovered/resolved
2 = Recovering/resolving
3 = Not recovered/not resolved
4 = Recovered/resolved with sequelae (consequent health issues)
5 = Fatal
6 = Unknown
        
    