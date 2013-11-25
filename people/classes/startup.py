
from py2neo import neo4j, node
graph_db = neo4j.GraphDatabaseService(neo4j.DEFAULT_URI)

modifier_types = node('ModifierTypes')

ability_modifier = node('AbilityModifier')
neo4j.Path(ability_modifier, 'IS', modifier_types)
alchemical_bonus = node('AlchemicalBonus')
neo4j.Path(alchemical_bonus, 'IS', modifier_types)
armor_bonus = node('ArmorBonus')
neo4j.Path(armor_bonus, 'IS', modifier_types)