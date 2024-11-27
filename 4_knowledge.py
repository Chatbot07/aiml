class KnowledgeBase:
    def _init_(self):
        self.facts = {}  # Dictionary to store facts (key: fact name, value: fact value)
        self.rules = []  # List to store rules (each rule is a tuple (condition, conclusion))

    def add_fact(self, key, value):
        self.facts[key] = value

    def add_rule(self, condition, conclusion):
        self.rules.append((condition, conclusion))

    def apply_rules(self):
        changed = True
        while changed:
            changed = False
            for condition, conclusion in self.rules:
                if self.evaluate_condition(condition):
                    if conclusion[0] not in self.facts:
                        self.add_fact(conclusion[0], conclusion[1])
                        changed = True

    def evaluate_condition(self, condition):
        for fact_key, expected_value in condition:
            if self.facts.get(fact_key) != expected_value:
                return False
        return True

    def get_facts(self):
        return self.facts

# Create a knowledge base object
kb = KnowledgeBase()
# Add some initial facts
kb.add_fact('has_wings', True)
kb.add_fact('can_fly', True)
kb.add_fact('lays_eggs', True)
kb.add_fact('is_mammal', False)
 # Add some rules
kb.add_rule([('has_wings', True), ('can_fly', True)], ('is_bird', True))
kb.add_rule([('is_bird', True), ('lays_eggs', True)], ('is_oviparous', True))
kb.add_rule([('is_mammal', False), ('lays_eggs', True)], ('is_reptile', False))
kb.add_rule([('has_wings', True), ('is_mammal', False)], ('is_insect', False))
kb.add_rule([('is_bird', True), ('is_oviparous', True)], ('is_penguin', False))
kb.add_rule([('has_wings', True), ('is_mammal', True)], ('is_bat', True))


# Apply rules to infer new facts
kb.apply_rules()

# Print all facts
print("Facts in the Knowledge Base:")
for fact, value in kb.get_facts().items():
    print(f"{fact}: {value}")
