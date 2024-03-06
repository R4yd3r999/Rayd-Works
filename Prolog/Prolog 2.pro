borrar_todas(_, [], []).
borrar_todas(X, [X|Resto], Z) :- !, borrar_todas(X, Resto, Z).
borrar_todas(X, [Cabeza|Resto], [Cabeza|Z]) :- borrar_todas(X, Resto, Z).

% Predicado auxiliar para borrar la cabeza de la lista
borrar_cabeza([_|Resto], Resto).