(define (domain smartcities)

    (:requirements :strips :typing)
    
    (:types motionsensor temperaturesensor lightsensor lightsensor door - object)
    
    (:predicates (at-detected ?x - motionsensor)
					(at-nodetected ?x - motionsensor)
					(at-hot ?x - temperaturesensor)
					(at-cold ?x - temperaturesensor)
					(at-high ?x - lightsensor)
					(at-low ?x - lightsensor)
					(at-press ?x - door)
					(at-notpress ?x - door)
		)
    
    (:action turnlighton
        :parameters (?x - motionsensor)
        :precondition (at-detected ?x)
        :effect (not(at-detected  ?x))
    )
    
	(:action turnlightoff
        :parameters (?x - motionsensor)
        :precondition (at-nodetected ?x)
        :effect (not(at-nodetected ?x))
    )
	
	(:action turnfanon
        :parameters (?x - temperaturesensor ?y - motionsensor)
        :precondition (and (at-detected ?y) (at-hot ?x))
        :effect (not(at-hot ?x))
    )
    
	(:action turnfanoff
        :parameters (?x - temperaturesensor)
        :precondition (at-cold ?x) 
        :effect (not(at-cold ?x))
    )
    
    (:action turnfrontlighton
        :parameters (?x - lightsensor)
        :precondition (at-low ?x)
        :effect (not(at-low ?x))
    )
    
    (:action turnfrontlightoff
        :parameters (?x - lightsensor)
        :precondition (at-high ?x) 
        :effect (not(at-high ?x))
    )
    
    (:action opendoor
        :parameters (?x - door)
        :precondition (at-press ?x)
        :effect (not(at-press ?x))
    )
    
    (:action closedoor
        :parameters (?x - door)
        :precondition (at-notpress ?x)
        :effect (not(at-notpress ?x))
    )
)