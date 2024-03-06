añadir_sin_duplicar(X, Y, Z) :- member(X, Y), !, Z = Y.
añadir_sin_duplicar(X, Y, [X|Y]).