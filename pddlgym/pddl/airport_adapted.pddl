(define (domain AEROPUERTO_ADAPTED)
	(:requirements :strips :typing :negative-preconditions)
	(:types tren equipaje maquina vagon posicion) ; numero

	(:predicates
		;(at ?x - (either maquina vagon equipaje) ?y - posicion)
		; modificacion para pddlgym 
		(at_maquina ?x - maquina ?y - posicion)
		(at_vagon ?x - vagon ?y - posicion)
		(at_equipaje ?x - equipaje ?y - posicion)
		(adjacent ?x - posicion ?y - posicion)
		(libre ?x - maquina)
		(sospechoso ?x - equipaje)
		(no-sospechoso ?x - equipaje)
		(vacio ?v - vagon) ; Ahora los vagones solo pueden llevar 1 equipaje
		;(no-enganchado ?x - vagon) me da que no hace falta esto, porque el at_vagon ya sirve
		(enganchado-a-maquina ?x - maquina ?y - vagon)
		(enganchado-a-vagon ?x - vagon ?y - vagon)
		(ultimo-vagon ?x - maquina ?y - vagon)
		(primer-vagon ?x - maquina ?y - vagon)
		(equipaje-cargado-en ?x - vagon ?y - equipaje)
		(es-oficina-inspeccion ?x - posicion)
		;(carga-actual ?v - vagon ?n - numero)  		; Eliminamos el conteo
		;(next ?v - vagon ?n1 - numero ?n2 - numero)	; Eliminamos el conteo
	)

	(:action move
		:parameters (?x - maquina ?y - posicion ?z - posicion)
		:precondition (and (at_maquina ?x ?y) (adjacent ?y ?z))
		:effect (and (not (at_maquina ?x ?y))
			(at_maquina ?x ?z))
	)

	(:action enganchar-primer-vagon
		:parameters (?x - maquina ?y - vagon ?z - posicion)
		:precondition (and (at_maquina ?x ?z) (at_vagon ?y ?z)
			(vacio ?y)
			(libre ?x))
		:effect (and (not (libre ?x))
			(not(at_vagon ?y ?z))
			(enganchado-a-maquina ?x ?y)
			(ultimo-vagon ?x ?y)
			(primer-vagon ?x ?y))
	)

	(:action enganchar-vagon
		:parameters (?x - maquina ?y - vagon ?z - vagon ?p - posicion)
		:precondition (and (at_maquina ?x ?p) (at_vagon ?z ?p)
			(vacio ?y)
			(ultimo-vagon ?x ?y))
		:effect (and (enganchado-a-maquina ?x ?z)
			(enganchado-a-vagon ?y ?z)
			(ultimo-vagon ?x ?z)
			(not(ultimo-vagon ?x ?y))
			(not(at_vagon ?z ?p)))
	)

	(:action desenganchar-primer-vagon
		:parameters (?x - maquina ?y - vagon ?p - posicion)
		:precondition (and (at_maquina ?x ?p)
			(ultimo-vagon ?x ?y)
			(primer-vagon ?x ?y)
			(vacio ?y)
			(enganchado-a-maquina ?x ?y))
		:effect (and (at_vagon ?y ?p)
			(not (ultimo-vagon ?x ?y))
			(not (primer-vagon ?x ?y))
			(not (enganchado-a-maquina ?x ?y))
			(libre ?x)
		)
	)

	(:action desenganchar-vagon
		:parameters (?x - maquina ?y - vagon ?z - vagon ?p - posicion)
		:precondition (and (at_maquina ?x ?p)
			(ultimo-vagon ?x ?z)
			(vacio ?y)
			(enganchado-a-maquina ?x ?y)
			(enganchado-a-maquina ?x ?z)
			(enganchado-a-vagon ?y ?z))
		:effect (and (at_vagon ?z ?p)
			(not (ultimo-vagon ?x ?z))
			(ultimo-vagon ?x ?y)
			(not (enganchado-a-maquina ?x ?z))
			(not (enganchado-a-vagon ?y ?z))
		)
	)

	(:action cargar-equipaje
		:parameters (?x - maquina ?y - vagon ?e - equipaje ?p - posicion)
		:precondition (and (at_maquina ?x ?p) (at_equipaje ?e ?p)
			(vacio ?y)
			(enganchado-a-maquina ?x ?y))
		:effect (and (equipaje-cargado-en ?y ?e)
			(not(vacio ?y))
			(not(at_equipaje ?e ?p)))
	)

	(:action descargar-un-equipaje
		:parameters (?x - maquina ?y - vagon ?e - equipaje ?p - posicion)
		:precondition (and (at_maquina ?x ?p)
			(no-sospechoso ?e)
			(enganchado-a-maquina ?x ?y)
			(equipaje-cargado-en ?y ?e))
		:effect (and (at_equipaje ?e ?p)
			(vacio ?y)
			(not(equipaje-cargado-en ?y ?e)))
	)

	(:action dejar-equipaje-en-oficina-de-inspeccion
		:parameters (?x - maquina ?y - vagon ?e - equipaje ?p - posicion)
		:precondition (and (at_maquina ?x ?p)
			(es-oficina-inspeccion ?p)
			(sospechoso ?e)
			(enganchado-a-maquina ?x ?y)
			(equipaje-cargado-en ?y ?e))
		:effect (and (at_equipaje ?e ?p)
			(vacio ?y)
			(not(equipaje-cargado-en ?y ?e)))
	)

	(:action investigar-equipaje
		:parameters (?e - equipaje ?p - posicion)
		:precondition (and (at_equipaje ?e ?p)
			(es-oficina-inspeccion ?p))
		:effect (and (not (sospechoso ?e)) (no-sospechoso ?e))
	)
)