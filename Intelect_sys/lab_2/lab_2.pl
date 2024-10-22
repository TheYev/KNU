is_a(harley_davidson, cruiser_motorcycle).
is_a(indian, cruiser_motorcycle).
is_a(suzuki_gsxr, sport_motorcycle).
is_a(yamaha_r1, sport_motorcycle).
is_a(cruiser_motorcycle, street_motorcycle).
is_a(sport_motorcycle, street_motorcycle).
is_a(street_motorcycle, motorcycle).

is_a(kawasaki_kx450, dirt_bike).
is_a(honda_crf450, dirt_bike).
is_a(ktm_450_sx_f, motocross_bike).
is_a(motocross_bike, dirt_bike).
is_a(dirt_bike, off_road_motorcycle).
is_a(off_road_motorcycle, motorcycle).

is_a(bmw_r1200gs, adventure_motorcycle).
is_a(triumph_tiger_900, adventure_motorcycle).
is_a(adventure_motorcycle, touring_motorcycle).
is_a(touring_motorcycle, motorcycle).

is_a(honda_goldwing, touring_bike).
is_a(bmw_k1600, touring_bike).
is_a(touring_bike, luxury_motorcycle).
is_a(luxury_motorcycle, motorcycle).

is_a(motorcycle, motor_vehicle).





part_of(engine, harley_davidson).
part_of(wheel, suzuki_gsxr).
part_of(chain, kawasaki_kx450).
part_of(fork, honda_crf450).
part_of(handlebar, bmw_r1200gs).
part_of(tank, yamaha_r1).
part_of(seat, indian).
part_of(exhaust, ktm_450_sx_f).
part_of(headlight, triumph_tiger_900).
part_of(gearbox, honda_goldwing).
part_of(clutch, bmw_k1600).
part_of(brake, yamaha_r1).
part_of(tire, suzuki_gsxr).
part_of(frame, harley_davidson).
part_of(suspension, kawasaki_kx450).





inherits(X, Z) :- is_a(X, Z).
inherits(X, Z) :- is_a(X, Y), inherits(Y, Z).

contained_in(X, Z) :- part_of(X, Z).
contained_in(X, Z) :- part_of(X, Y), contained_in(Y, Z).
contained_in(X, Z) :- part_of(X, Y), inherits(Y, Z).


:- initialization(main).

main :-
    (inherits(harley_davidson, motorcycle) ->
        write('Harley Davidson is a motorcycle'), nl;
        write('Harley Davidson is not a motorcycle'), nl),

    (inherits(suzuki_gsxr, motor_vehicle) ->
        write('Suzuki GSX-R is a motor_vehicle'), nl;
        write('Suzuki GSX-R is not a motor_vehicle'), nl),

    (inherits(ktm_450_sx_f, motorcycle) ->
        write('KTM 450 SX-F is a motorcycle'), nl;
        write('KTM 450 SX-F is not a motorcycle'), nl),

    (inherits(bmw_k1600, motor_vehicle) ->
        write('BMW K1600 is a motor_vehicle'), nl;
        write('BMW K1600 is not a motor_vehicle'), nl),

    (inherits(kawasaki_kx450, street_motorcycle) ->
        write('Kawasaki KX450 is a street_motorcycle'), nl;
        write('Kawasaki KX450 is not a street_motorcycle'), nl),  %  Must be false

    (inherits(honda_goldwing, dirt_bike) ->
        write('Honda Goldwing is a dirt_bike'), nl;
        write('Honda Goldwing is not a dirt_bike'), nl),  %  Must be false

    (contained_in(engine, motor_vehicle) ->
        write('Engine is part_of motor_vehicle'), nl;
        write('Engine is not part_of motor_vehicle'), nl),

    (contained_in(wheel, street_motorcycle) ->
        write('Wheel is part_of street_motorcycle'), nl;
        write('Wheel is not part_of street_motorcycle'), nl),

    (contained_in(chain, motorcycle) ->
        write('Chain is part_of motorcycle'), nl;
        write('Chain is not part_of motorcycle'), nl),

    (contained_in(clutch, touring_motorcycle) ->
        write('Clutch is part_of touring_motorcycle'), nl;
        write('Clutch is not part_of touring_motorcycle'), nl),  %  Must be false

    (contained_in(frame, luxury_motorcycle) ->
        write('Frame is part_of luxury_motorcycle'), nl;
        write('Frame is not part_of luxury_motorcycle'), nl),  % Must be false

    halt.
