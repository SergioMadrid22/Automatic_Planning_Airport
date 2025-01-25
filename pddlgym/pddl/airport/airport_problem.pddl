(define (problem AEROPUERTO-TEST)
(:domain AEROPUERTO)
(:objects P1 P2 P3 P4 P5 P6 P7 P8 ZF RE OI - posicion
          M1 M2 - maquina
          V1 V2 V3 V4 V5 - vagon
          E1 E2 E3 E4 E5 E6 - equipaje
          N0 N1 N2 - numero)
(:init
    ; Vagones
    (at_vagon V1 P1) (at_vagon V2 P1) 
    (at_vagon V3 P1) (at_vagon V4 P5) (at_vagon V5 P5)
    (carga-actual V1 N0) (carga-actual V2 N0) 
    (carga-actual V3 N0) (carga-actual V4 N0) (carga-actual V5 N0)
    (next V1 N0 N1) (next V1 N1 N2)
    (next V2 N0 N1) (next V2 N1 N2)
    (next V3 N0 N1) (next V3 N1 N2)
    (next V4 N0 N1) (next V4 N1 N2)
    (next V5 N0 N1) (next V5 N1 N2)
    (vacio N0)

    ; Maquinas
    (at_maquina M1 RE) (at_maquina M2 RE)	
    (libre M1) (libre M2)

    ; Equipajes
    (at_equipaje E1 ZF) (at_equipaje E2 ZF) (at_equipaje E3 P6) 
    (at_equipaje E4 P6) (at_equipaje E5 P2) (at_equipaje E6 P2)
    (sospechoso E3) (sospechoso E6)
    (no-sospechoso E1) (no-sospechoso E2) 
    (no-sospechoso E4) (no-sospechoso E5)
    
    ; Posiciones
    (es-oficina-inspeccion OI)
    ;(no-enganchado V1) (no-enganchado V2) 
    ;(no-enganchado V3) (no-enganchado V4) (no-enganchado V5) 
    (adjacent P1 P3) (adjacent P3 P1) 
    (adjacent P3 P4) (adjacent P4 P3) 
    (adjacent P4 P2) (adjacent P2 P4) 
    (adjacent P2 ZF) (adjacent ZF P2) 
    (adjacent ZF OI) (adjacent OI ZF) 
    (adjacent ZF RE) (adjacent RE ZF)
    (adjacent OI RE) (adjacent RE OI) 
    (adjacent OI P1) (adjacent P1 OI) 
    (adjacent OI P5) (adjacent P5 OI) 
    (adjacent RE P6) (adjacent P6 RE) 
    (adjacent P6 P8) (adjacent P8 P6) 
    (adjacent P8 P7) (adjacent P7 P8) 
    (adjacent P5 P7) (adjacent P7 P5)
)
 
(:goal (and (at_equipaje E1 P4) (at_equipaje E2 P8) (at_equipaje E3 RE) 
            (at_equipaje E4 RE) (at_equipaje E5 RE) (at_equipaje E6 RE)))
)