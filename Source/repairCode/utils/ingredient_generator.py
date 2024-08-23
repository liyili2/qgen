import random
import xml.etree.ElementTree as ET


def random_num():
    return random.randint(-1, 1)


def get_random_op():
    operators = ['+', '-', '*', '/', '%', '^', '$']
    return random.choice(operators)


class IngredientGenerator:
    APP_IDENTIFIER = 'f'

    def __init__(self, type_environment):
        self.type_environment: dict = type_environment
        self.vexp_factory = self.create_vexp_factory()

    def get_identifier(self, element):

        if element.tag == 'app':
            return self.APP_IDENTIFIER
        type_environment_identifiers = self.type_environment.keys()
        identifier = random.choice([type_environment_identifiers])
        return identifier

    def generate_let(self):
        let_el = ET.Element("Let")
        let_el.set("id", self.get_identifier(let_el))
        return let_el

    def generate_cuexp(self):
        cuexp_el = ET.Element("pexp")
        cuexp_el.set("gate", "CU")
        cuexp_el.set("id", self.get_identifier(cuexp_el))
        cuexp_el.append(self.vexp_factory.create_vexp())
        cuexp_el.append(self.create_nextexp())
        return cuexp_el

    def generate_match(self):
        match_el = ET.Element("match")
        match_el.set("id", self.get_identifier(match_el))
        return match_el

    def generate_skipexp(self):
        skipexp_el = ET.Element("pexp")
        skipexp_el.set("gate", "SKIP")
        skipexp_el.set("id", self.get_identifier(skipexp_el))
        skipexp_el.append(self.vexp_factory.create_vexp())
        return skipexp_el

    def generate_xexp(self):
        xexp_el = ET.Element("pexp")
        xexp_el.set("gate", "X")
        xexp_el.set("id", self.get_identifier(xexp_el))
        xexp_el.append(self.vexp_factory.create_vexp())
        return xexp_el

    def generate_srexp(self):
        srexp_el = ET.Element("pexp")
        srexp_el.set("gate", "SR")
        srexp_el.set("id", self.get_identifier(srexp_el))
        srexp_el.append(self.vexp_factory.create_vexp())
        return srexp_el

    def generate_qftexp(self):
        qftexp_el = ET.Element("pexp")
        qftexp_el.set("gate", "QFT")
        qftexp_el.set("id", self.get_identifier(qftexp_el))
        qftexp_el.append(self.vexp_factory.create_vexp())
        return qftexp_el

    def generate_lshiftexp(self):
        lshiftexp_el = ET.Element("pexp")
        lshiftexp_el.set("gate", "Lshift")
        lshiftexp_el.set("id", self.get_identifier(lshiftexp_el))
        return lshiftexp_el

    def generate_rshiftexp(self):
        rshiftexp_el = ET.Element("pexp")
        rshiftexp_el.set("gate", "Rshift")
        rshiftexp_el.set("id", self.get_identifier(rshiftexp_el))
        return rshiftexp_el

    def generate_revexp(self):
        revexp_el = ET.Element("pexp")
        revexp_el.set("gate", "Rev")
        revexp_el.set("id", self.get_identifier(revexp_el))
        return revexp_el

    def generate_rqftexp(self):
        rqftexp_el = ET.Element("pexp")
        rqftexp_el.set("gate", "RQFT")
        rqftexp_el.set("id", self.get_identifier(rqftexp_el))
        return rqftexp_el

    def create_exp(self):
        exp_types = [
            self.generate_let,
            self.generate_app,
            self.generate_cuexp,
            self.generate_if,
            self.generate_match,
            self.generate_skipexp,
            self.generate_xexp,
            self.generate_srexp,
            self.generate_qftexp,
            self.generate_lshiftexp,
            self.generate_rshiftexp,
            self.generate_revexp,
            self.generate_rqftexp
        ]

        random_exp_generator = random.choice(exp_types)
        return random_exp_generator()

    def create_program(self):
        return self.create_exp()

    def create_nextexp(self):
        next_el = ET.Element('next')
        next_el.append(self.create_program())
        return next_el

    def generate_if(self, target_element, ingredient_list):
        if_el = ET.Element("Ifa")
        if_el.append(self.vexp_factory.create_vexp())
        if_el.append(self.create_nextexp())
        if_el.append(self.create_nextexp())
        return if_el

    def generate_app(self):
        app_el = ET.Element("App")
        app_el.set("id", self.get_identifier(app_el))
        app_el.append(self.vexp_factory.create_vexp())
        return app_el

    def generate_pexp(self):
        gate_types_with_vexp = ["SKIP", "X", "SR", "QFT", "CU"]
        gate_types_without_vexp = ["Lshift", "Rshift", "Rev", "RQFT"]

        gate_types = gate_types_with_vexp + gate_types_without_vexp
        gate = random.choice(gate_types)

        pexp_el = ET.Element("pexp")
        pexp_el.set("gate", gate)
        pexp_el.set("id", self.get_identifier(pexp_el))

        if gate in gate_types_with_vexp:
            pexp_el.append(self.vexp_factory.create_vexp())
            if gate == "CU":
                pexp_el.append(self.create_nextexp())

        return pexp_el

    def generate_ingredients(self, target_element):
        block_functions = [self.generate_if, self.generate_app, self.generate_pexp]
        random_block = random.choice(block_functions)
        return random_block()

    def create_vexp_factory(self):
        return self.VexpFactory(self)

    class VexpFactory:
        def __init__(self, ingredient_generator):
            self.ingredient_generator = ingredient_generator
            self.vexp_types_not_nested = [self.create_vexp_num, self.create_vexp_idexp]
            self.vexp_types = self.vexp_types_not_nested + [self.create_vexp_nested]

        @staticmethod
        def et_vexp_element():
            return ET.Element('vexp')

        def create_vexp_idexp(self):
            idexp = self.et_vexp_element()
            idexp.set('op', 'id')
            idexp.text = self.ingredient_generator.get_identifier(idexp)
            return idexp

        def create_vexp_num(self):
            vexp = self.et_vexp_element()
            vexp.set('op', 'num')
            vexp.text = str(random_num())
            return vexp

        def create_vexp_nested(self):
            vexp = self.et_vexp_element()
            vexp.set('op', get_random_op())
            vexp.append(self.create_vexp(self.vexp_types_not_nested))
            vexp.append(self.create_vexp(self.vexp_types_not_nested))
            return vexp

        def create_vexp(self, possible_vexp_types=None):
            if possible_vexp_types is None:
                possible_vexp_types = self.vexp_types
            function = random.choice(possible_vexp_types)
            return function()


    def generate_ingredients(type_environment):
        generator = IngredientGenerator(type_environment)
        ingredient = generator.generate_ingredients()
        print(ET.tostring(ingredient))
        return ingredient
