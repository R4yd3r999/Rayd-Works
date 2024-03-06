borrar_primera(_, [], []).
borrar_primera(X, [X|Resto], Resto) :- !.
borrar_primera(X, [Cabeza|Resto], [Cabeza|Z]) :- borrar_primera(X, Resto, Z).