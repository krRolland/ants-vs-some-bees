import ants, importlib
importlib.reload(ants)
hive = ants.Hive(ants.AssaultPlan())
dimensions = (2, 9)
colony = ants.AntColony(None, hive, ants.ant_types(), ants.dry_layout, dimensions)

queen = ants.QueenAnt()
impostor = ants.QueenAnt()
container = ants.TankAnt()
colony.places['tunnel_0_3'].add_insect(container)
colony.places['tunnel_0_3'].add_insect(impostor)
colony.places['tunnel_0_3'].ant is container
impostor.action(colony)
colony.places['tunnel_0_3'].ant is container


