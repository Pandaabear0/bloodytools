from bloodytools.simulations.legendary_simulator import LegendarySimulator
from bloodytools.simulations.race_simulator import RaceSimulator
from bloodytools.simulations.secondary_distribution_simulator import (
    SecondaryDistributionSimulator,
)
from bloodytools.simulations.simulator import SimulatorFactory
from bloodytools.simulations.soulbind_simulator import SoulbindSimulator
from bloodytools.simulations.talent_simulator import TalentSimulator
from bloodytools.simulations.tier_set_simulator import TierSetSimulator
from bloodytools.simulations.trinket_simulator import TrinketSimulator
from bloodytools.simulations.conduit_simulator import ConduitSimulator
from bloodytools.simulations.talent_removal_simulator import TalentRemovalSimulator
from bloodytools.simulations.talent_add_simulator import TalentAddSimulator
from bloodytools.simulations.talent_target_scaling_simulator import (
    TalentTargetScalingSimulator,
)

simulator_factory = SimulatorFactory()

simulator_factory.register_simulator(ConduitSimulator)
simulator_factory.register_simulator(LegendarySimulator)
simulator_factory.register_simulator(RaceSimulator)
simulator_factory.register_simulator(SecondaryDistributionSimulator)
simulator_factory.register_simulator(SoulbindSimulator)
simulator_factory.register_simulator(TalentAddSimulator)
simulator_factory.register_simulator(TalentRemovalSimulator)
simulator_factory.register_simulator(TalentSimulator)
simulator_factory.register_simulator(TalentTargetScalingSimulator)
simulator_factory.register_simulator(TierSetSimulator)
simulator_factory.register_simulator(TrinketSimulator)
