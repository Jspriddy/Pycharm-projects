# farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
# wild_aminals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}
#
# all_aminals = farm_animals.union(wild_aminals)
# print(all_aminals)

from prescription_data import adverse_interactions

meds_to_watch = set()

for interaction in adverse_interactions:
    meds_to_watch = meds_to_watch.union(interaction)

print(sorted((meds_to_watch)))