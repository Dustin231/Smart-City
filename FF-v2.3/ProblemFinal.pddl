(define (problem pb_smartcities)
    (:domain smartcities)
    
    (:objects
        detected nodetected - motionsensor
        hot cold - temperaturesensor
        high low - lightsensor
        press notpress  - door
        )
        
    (:init 
            (at-detected detected)
            (at-hot hot)
            (at-high high)
            (at-notpress notpress)
    )
    
    (:goal (and (not (at-detected detected)) 
                (not (at-nodetected nodetected)) 
                (not (at-hot hot))
                (not (at-cold cold))
                (not (at-high high))
                (not (at-low low))
                (not (at-notpress notpress))
                (not (at-press press))
                ))
                
)