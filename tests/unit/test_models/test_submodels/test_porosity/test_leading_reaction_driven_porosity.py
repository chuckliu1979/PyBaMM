#
# Test leading-order porosity submodel
#

import pybamm
import tests
import unittest


class TestLeadingOrder(unittest.TestCase):
    def test_public_functions(self):
        # param = pybamm.LeadAcidParameters()
        param = pybamm.LithiumIonParameters()
        a = pybamm.PrimaryBroadcast(pybamm.Scalar(0), "current collector")
        variables = {
            "Total negative electrode SEI thickness [m]": a,
            "Negative electrode lithium plating thickness [m]": a,
            "Negative electrode surface area to volume ratio [m-1]": a,
        }
        options = {
            "SEI": "ec reaction limited",
            "SEI film resistance": "distributed",
            "SEI porosity change": "true",
            "lithium plating": "irreversible",
            "lithium plating porosity change": "true",
        }
        submodel = pybamm.porosity.ReactionDriven(param, options, True)
        std_tests = tests.StandardSubModelTests(submodel, variables)
        std_tests.test_all()


if __name__ == "__main__":
    print("Add -v for more debug output")
    import sys

    if "-v" in sys.argv:
        debug = True
    pybamm.settings.debug_mode = True
    unittest.main()
