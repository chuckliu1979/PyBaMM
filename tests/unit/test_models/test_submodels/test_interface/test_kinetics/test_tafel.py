#
# Test base Tafel submodel
#
import pybamm
import tests
import unittest


class TestTafel(unittest.TestCase):
    def test_public_function(self):
        # Test forward Tafel on the negative
        param = pybamm.LithiumIonParameters()

        a_n = pybamm.FullBroadcast(
            pybamm.Scalar(0.5), ["negative electrode"], "current collector"
        )
        a_p = pybamm.FullBroadcast(
            pybamm.Scalar(0.5), ["positive electrode"], "current collector"
        )
        a = pybamm.Scalar(0.5)
        variables = {
            "Current collector current density": a,
            "Negative electrode potential": a_n,
            "Negative electrolyte potential": a_n,
            "Negative electrode open circuit potential": a_n,
            "Negative electrolyte concentration": a_n,
            "Negative particle surface concentration": a_n,
            "Negative electrode temperature": a_n,
            "Negative electrode surface area to volume ratio": a_n,
        }
        submodel = pybamm.interface.ForwardTafel(
            param,
            "Negative",
            "lithium-ion main",
            {
                "SEI film resistance": "none",
                "total interfacial current density as a state": "false",
                "particle size": "single"
            },
        )
        std_tests = tests.StandardSubModelTests(submodel, variables)

        std_tests.test_all()

        # Test backward Tafel on the positive
        variables = {
            "Current collector current density": a,
            "Positive electrode potential": a_p,
            "Positive electrolyte potential": a_p,
            "Positive electrode open circuit potential": a_p,
            "Positive electrolyte concentration": a_p,
            "Positive particle surface concentration": a_p,
            "Negative electrode interfacial current density": a_n,
            "Negative electrode exchange current density": a_n,
            "Positive electrode temperature": a_p,
            "Negative electrode surface area to volume ratio": a_n,
            "Positive electrode surface area to volume ratio": a_p,
            "X-averaged negative electrode interfacial current density": a,
            "X-averaged positive electrode interfacial current density": a,
            "Sum of electrolyte reaction source terms": 0,
            "Sum of negative electrode electrolyte reaction source terms": 0,
            "Sum of positive electrode electrolyte reaction source terms": 0,
            "Sum of x-averaged negative electrode "
            "electrolyte reaction source terms": 0,
            "Sum of x-averaged positive electrode "
            "electrolyte reaction source terms": 0,
            "Sum of interfacial current densities": 0,
            "Sum of negative electrode interfacial current densities": 0,
            "Sum of positive electrode interfacial current densities": 0,
            "Sum of x-averaged negative electrode interfacial current densities": 0,
            "Sum of x-averaged positive electrode interfacial current densities": 0,
        }
        submodel = pybamm.interface.BackwardTafel(
            param,
            "Positive",
            "lithium-ion main",
            {
                "SEI film resistance": "none",
                "total interfacial current density as a state": "false",
                "particle size": "single"
            },
        )
        std_tests = tests.StandardSubModelTests(submodel, variables)
        std_tests.test_all()


if __name__ == "__main__":
    print("Add -v for more debug output")
    import sys

    if "-v" in sys.argv:
        debug = True
    pybamm.settings.debug_mode = True
    unittest.main()
